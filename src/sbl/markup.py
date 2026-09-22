"""Markdown renderer for a :class:`~sbl.models.RunResult` (build_plan.md §6, WP6).

The renderer reads the run result **and nothing else**. That constraint is what
makes the trace complete: if a sentence appears in the markup, it came from the
run result object, and that object names the library hash that produced it.

Because of it, this module deliberately does *not* import the pydantic models at
import time. :func:`render_markdown` accepts either a ``RunResult`` instance or
the plain dict you get back from ``json.load`` on an audit line, and works off
the dict either way. Rendering a run from a JSON file alone is therefore a
meaningful test of the "no hidden inputs" property.

Output is deterministic: stable ordering, no dates other than the result's own
timestamp, no trailing whitespace, LF line endings, exactly one trailing
newline.
"""

from __future__ import annotations

import re
from typing import Any, Iterable, Mapping, Optional

__all__ = ["render_markdown", "DISCLAIMER", "STATUS_WARNING"]


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

#: Severity groups, in the order the Flags section prints them.
SEVERITY_ORDER: tuple[str, ...] = ("high", "medium", "low")

#: The four-tier ladder, tightest first. Used only to order an unordered ladder.
TIER_ORDER: tuple[str, ...] = ("preferred", "acceptable", "fallback", "unacceptable")

#: Status tag printed against every clause heading.
STATUS_TAGS: dict[str, str] = {
    "reviewed": "[REVIEWED]",
    "draft": "[DRAFT]",
    "stub": "[STUB]",
}

#: Placeholder for an empty table cell.
EMPTY_CELL = "—"

#: Maximum length of the one-line ladder summary before it is truncated.
SUMMARY_LIMIT = 160

DISCLAIMER = (
    "This markup was produced by the SBL Negotiation Playbook Demonstrator, a "
    "demonstration tool built from public sources and run against synthetic "
    "deals. It is not legal advice. It is not the work product of any institution, "
    "and it has not been validated against any institution's credit policy, risk "
    "appetite, house style or local counsel advice. Every position is drafted from "
    "the lender's side only. The status labels mean exactly what they say: [STUB] "
    "means no position has been drafted; [DRAFT] means an entry written from public "
    "sources that no named human reviewer has checked; [REVIEWED] means a named "
    "reviewer recorded in the library has checked it. Text carrying a [VERIFY] "
    "prefix has not been confirmed against a primary source the writer opened. Any "
    "concession below a clause's floor, and every item under \"Not automated on this "
    "deal\", is a human decision that this tool does not make."
)

STATUS_WARNING = (
    "Status warning: positions tagged [DRAFT] or [STUB] have not been reviewed by a "
    "named human reviewer and must not be relied on as the lender's settled position."
)


# ---------------------------------------------------------------------------
# Small helpers: lenient access over dicts or models
# ---------------------------------------------------------------------------


def _as_dict(result: Any) -> dict[str, Any]:
    """Return ``result`` as a plain dict, whether it is a model or already a dict."""
    if isinstance(result, Mapping):
        return dict(result)
    dump = getattr(result, "model_dump", None)
    if callable(dump):  # pydantic v2
        try:
            return dump(mode="json")
        except TypeError:  # pragma: no cover - defensive
            return dump()
    legacy = getattr(result, "dict", None)
    if callable(legacy):  # pragma: no cover - pydantic v1 fallback
        return legacy()
    raise TypeError(
        "render_markdown expects a RunResult or a dict decoded from one, "
        f"not {type(result).__name__}"
    )


def _scalar(value: Any) -> str:
    """Render a scalar as text, unwrapping Enum members."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (str, int, float)):
        return str(value)
    inner = getattr(value, "value", None)
    if inner is not None:
        return str(inner)
    return str(value)


def _get(obj: Any, key: str, default: Any = None) -> Any:
    """Read ``key`` from a mapping, or the attribute of the same name."""
    if isinstance(obj, Mapping):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _text(obj: Any, key: str, default: str = "") -> str:
    """Read ``key`` as a stripped string; ``default`` when absent, null or blank."""
    out = _scalar(_get(obj, key)).strip()
    return out if out else default


def _list(obj: Any, key: str) -> list[Any]:
    """Read ``key`` as a list; an empty list when absent or null."""
    raw = _get(obj, key)
    if raw is None:
        return []
    if isinstance(raw, (str, bytes, Mapping)):
        return [raw]
    if isinstance(raw, Iterable):
        return list(raw)
    return [raw]


def _strings(obj: Any, key: str) -> list[str]:
    """Read ``key`` as a list of non-empty strings, order preserved."""
    return [s for s in (_scalar(v).strip() for v in _list(obj, key)) if s]


def _collapse(text: Any) -> str:
    """Collapse all runs of whitespace (including newlines) to single spaces."""
    return " ".join(_scalar(text).split())


def _cell(text: Any) -> str:
    """Render a value safe to drop into a Markdown table cell."""
    out = _collapse(text).replace("|", "\\|")
    return out if out else EMPTY_CELL


def _blockquote(text: str) -> list[str]:
    """Render ``text`` as a Markdown blockquote, one output line per input line."""
    normalised = _scalar(text).replace("\r\n", "\n").replace("\r", "\n")
    lines: list[str] = []
    for raw in normalised.split("\n"):
        stripped = raw.strip()
        lines.append("> " + stripped if stripped else ">")
    while lines and lines[-1] == ">":
        lines.pop()
    return lines


def _one_line_summary(text: str, limit: int = SUMMARY_LIMIT) -> str:
    """First sentence of ``text``, else its first ``limit`` characters."""
    flat = _collapse(text)
    if not flat:
        return ""
    match = re.search(r"[.!?](?=\s|$)", flat)
    if match is not None and match.end() <= limit:
        return flat[: match.end()]
    if len(flat) <= limit:
        return flat
    return flat[:limit].rstrip() + "..."


def _table(header: list[str], rows: list[list[str]]) -> list[str]:
    """Render a Markdown table. Cells must already have been through ``_cell``."""
    lines = ["| " + " | ".join(header) + " |"]
    lines.append("| " + " | ".join("---" for _ in header) + " |")
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def _bullets(items: Iterable[str]) -> list[str]:
    return ["- " + _collapse(item) for item in items]


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------


def _status_summary(data: Mapping[str, Any]) -> tuple[int, int, int]:
    """``(reviewed, draft, stub)`` from the result, else counted off the clauses."""
    summary = _get(data, "status_summary")
    if summary:
        return (
            int(_get(summary, "reviewed", 0) or 0),
            int(_get(summary, "draft", 0) or 0),
            int(_get(summary, "stub", 0) or 0),
        )
    counts = {"reviewed": 0, "draft": 0, "stub": 0}
    for clause in _list(data, "clauses"):
        key = _text(clause, "status")
        if key in counts:
            counts[key] += 1
    return counts["reviewed"], counts["draft"], counts["stub"]


def _header(data: Mapping[str, Any]) -> list[str]:
    intake = _get(data, "intake") or {}
    deal_id = _text(data, "deal_id") or _text(intake, "deal_id")
    description = _text(data, "description") or _text(intake, "description")
    reviewed, draft, stub = _status_summary(data)

    title = (
        f"SBL negotiation markup — {deal_id}"
        if deal_id
        else "SBL negotiation markup"
    )
    lines = [f"# {title}", ""]

    for label, value in (
        ("Deal", deal_id),
        ("Description", description),
        ("Run id", _text(data, "run_id")),
        ("Timestamp", _text(data, "timestamp")),
        ("Library hash", _text(data, "library_hash")),
        ("Intake hash", _text(data, "intake_hash")),
        ("Governing law", _text(data, "governing_law")),
    ):
        if value:
            lines.append(f"- {label}: {_collapse(value)}")
    lines.append(f"- Review status: {reviewed} reviewed / {draft} draft / {stub} stub")
    lines.append("")
    lines.append(STATUS_WARNING)
    return lines


def _escalations(data: Mapping[str, Any]) -> list[str]:
    lines = ["## Escalations", ""]
    escalations = _list(data, "escalations")
    if escalations:
        rows = [
            [
                _cell(_text(e, "rule_id")),
                _cell(_text(e, "clause")),
                _cell(_text(e, "to")),
                _cell(_text(e, "reason")),
            ]
            for e in escalations
        ]
        lines += _table(["Rule id", "Clause", "Who decides", "Reason"], rows)
    else:
        lines.append("No escalations.")
    lines.append("")
    exit_code = _get(data, "exit_code")
    lines.append(
        f"Exit code: {_scalar(exit_code)}"
        if exit_code is not None
        else "Exit code: not recorded."
    )
    return lines


def _flag_entry(flag: Any) -> list[str]:
    flag_id = _text(flag, "id", "(flag id not recorded)")
    message = _collapse(_text(flag, "message"))
    who = _text(flag, "who_decides", "not recorded in the flag definition")
    rule_id = _text(flag, "rule_id", "not recorded")
    head = f"- **{flag_id}** — {message}" if message else f"- **{flag_id}**"
    return [
        head,
        f"  - Who decides: {_collapse(who)}",
        f"  - Triggering rule: {_collapse(rule_id)}",
    ]


def _flags(data: Mapping[str, Any]) -> list[str]:
    lines = ["## Flags", ""]
    flags = _list(data, "flags")
    if not flags:
        lines.append("No flags raised.")
        return lines

    grouped: dict[str, list[Any]] = {s: [] for s in SEVERITY_ORDER}
    other: list[Any] = []
    for flag in flags:
        grouped.get(_text(flag, "severity"), other).append(flag)

    first = True
    for severity in SEVERITY_ORDER:
        if not grouped[severity]:
            continue
        if not first:
            lines.append("")
        first = False
        lines.append(f"### {severity.capitalize()} severity")
        lines.append("")
        for flag in grouped[severity]:
            lines += _flag_entry(flag)
    if other:
        if not first:
            lines.append("")
        lines.append("### Severity not recorded")
        lines.append("")
        for flag in other:
            lines += _flag_entry(flag)
    return lines


def _ladder_rows(clause: Any) -> list[list[str]]:
    rungs = _list(clause, "ladder")
    if not rungs:
        return []
    indexed = sorted(
        enumerate(rungs),
        key=lambda pair: (
            TIER_ORDER.index(_text(pair[1], "tier"))
            if _text(pair[1], "tier") in TIER_ORDER
            else len(TIER_ORDER),
            pair[0],
        ),
    )
    rows: list[list[str]] = []
    for _, rung in indexed:
        tier = _text(rung, "tier", "(tier not recorded)")
        label = (
            f"{tier} (description of the walk-away line, not drafting)"
            if tier == "unacceptable"
            else tier
        )
        rows.append(
            [
                _cell(label),
                _cell(_one_line_summary(_text(rung, "text"))),
                _cell("; ".join(_strings(rung, "conditions"))),
                _cell(_text(rung, "approval")),
            ]
        )
    return rows


def _rung_for_tier(clause: Any, tier: str) -> Optional[Any]:
    for rung in _list(clause, "ladder"):
        if _text(rung, "tier") == tier:
            return rung
    return None


def _rule_added_block(clause: Any) -> list[str]:
    """Conditions precedent, representations and drafting notes added by rules."""
    lines: list[str] = []
    for key, heading in (
        ("cps", "Conditions precedent added by rules"),
        ("reps", "Representations/undertakings added by rules"),
        ("notes", "Drafting notes"),
    ):
        items = _strings(clause, key)
        if not items:
            continue
        lines += ["", f"**{heading}**", ""]
        lines += _bullets(items)
    return lines


def _jurisdiction_note_block(clause: Any, governing_law: str) -> list[str]:
    note = _text(clause, "jurisdiction_note")
    if not note:
        return []
    label = governing_law or "governing law not recorded"
    return ["", f"**Jurisdiction note ({label})**", "", _collapse(note)]


def _rules_applied_line(clause: Any) -> str:
    applied = _strings(clause, "rules_applied")
    return "Rules applied: " + (", ".join(applied) if applied else "none")


def _clause_section(clause: Any, governing_law: str) -> list[str]:
    status = _text(clause, "status")
    tag = STATUS_TAGS.get(status, "[STATUS NOT RECORDED]")
    clause_id = _text(clause, "id", "(clause id not recorded)")
    title = _text(clause, "title") or clause_id
    lines = ["", f"### {title} {tag}", ""]

    if clause_id != title:
        lines.append(f"- Clause id: {clause_id}")
    for label, key in (
        ("Risk rating", "risk_rating"),
        ("Category", "category"),
        ("Document", "document"),
    ):
        value = _text(clause, key)
        if value:
            lines.append(f"- {label}: {value}")

    if status == "stub":
        lines += ["", "No drafted positions yet; status stub."]
        lines += _rule_added_block(clause)
        lines += _jurisdiction_note_block(clause, governing_law)
        lines += ["", _rules_applied_line(clause)]
        return lines

    opening = _text(clause, "opening", "(opening tier not recorded)")
    opening_rung = _rung_for_tier(clause, opening) or {}
    opening_text = _text(clause, "opening_text") or _text(opening_rung, "text")
    opening_rationale = _text(clause, "opening_rationale") or _text(
        opening_rung, "rationale"
    )

    lines += ["", f"**Opening: {opening}**"]
    if opening_text:
        lines.append("")
        lines += _blockquote(opening_text)
    if opening_rationale:
        lines += ["", f"Rationale: {_collapse(opening_rationale)}"]

    floor = _text(clause, "floor", "(floor tier not recorded)")
    approver = _text(_rung_for_tier(clause, floor) or {}, "approval")
    lines.append("")
    lines.append(
        f"**Floor: {floor}** — approver: {_collapse(approver)}"
        if approver
        else f"**Floor: {floor}**"
    )

    rows = _ladder_rows(clause)
    if rows:
        lines += ["", "**Position ladder**", ""]
        lines += _table(["Tier", "Summary", "Conditions", "Approver"], rows)

    triggers = _strings(clause, "escalation_triggers")
    if triggers:
        lines += ["", "**Escalation triggers**", ""]
        lines += _bullets(triggers)

    lines += _rule_added_block(clause)
    lines += _jurisdiction_note_block(clause, governing_law)
    lines += ["", _rules_applied_line(clause)]
    return lines


def _clauses(data: Mapping[str, Any]) -> list[str]:
    lines = ["## Clause-by-clause"]
    clauses = _list(data, "clauses")
    if not clauses:
        return lines + ["", "No clauses in this run."]
    governing_law = _text(data, "governing_law")
    for clause in clauses:
        lines += _clause_section(clause, governing_law)
    return lines


def _jurisdiction(data: Mapping[str, Any]) -> list[str]:
    juris = _get(data, "jurisdiction")
    if not juris:
        return []
    name = _text(juris, "name") or _text(juris, "id", "jurisdiction not recorded")
    tag = STATUS_TAGS.get(_text(juris, "status"), "[STATUS NOT RECORDED]")
    lines = ["", f"## Jurisdiction overlay — {name} {tag}", ""]
    for label, key in (
        ("Creation", "creation"),
        ("Registration / filing", "registration_filing"),
        ("Perfection depends on", "perfection_depends_on"),
        ("Enforcement route", "enforcement_route"),
        ("Financial collateral regime", "financial_collateral_regime"),
        (
            "Governing law of intermediated securities",
            "governing_law_of_intermediated_securities",
        ),
        ("Practical notes", "practical_notes"),
    ):
        value = _text(juris, key)
        if value:
            lines.append(f"- {label}: {_collapse(value)}")
    return lines


def _counterparty_requests(data: Mapping[str, Any]) -> list[str]:
    outcomes = _list(data, "counterparty_request_outcomes")
    if not outcomes:
        return []
    rows = [
        [
            _cell(_text(o, "clause")),
            _cell(_text(o, "requested_tier")),
            _cell(_text(o, "requested_text")),
            _cell(_text(o, "floor")),
            _cell(_text(o, "outcome")),
        ]
        for o in outcomes
    ]
    return ["", "## Counterparty request outcomes", ""] + _table(
        ["Clause", "Requested tier", "Requested text", "Floor", "Outcome"], rows
    )


def _not_automated(data: Mapping[str, Any]) -> list[str]:
    lines = ["", "## Not automated on this deal", ""]
    items = _strings(data, "not_automated")
    return lines + (_bullets(items) if items else ["None triggered on this deal."])


def _footer() -> list[str]:
    return ["", "---", "", DISCLAIMER]


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def render_markdown(result: Any) -> str:
    """Render ``result`` as Markdown.

    ``result`` may be a ``RunResult`` instance or the plain dict produced by
    ``json.loads`` on a line of ``runs/audit.jsonl``. Nothing outside the object
    is consulted, so the two render identically.

    The output has LF line endings, no trailing whitespace on any line, and ends
    with exactly one newline.
    """
    data = _as_dict(result)

    lines: list[str] = []
    lines += _header(data)
    lines.append("")
    lines += _escalations(data)
    lines.append("")
    lines += _flags(data)
    lines.append("")
    lines += _clauses(data)
    lines += _jurisdiction(data)
    lines += _counterparty_requests(data)
    lines += _not_automated(data)
    lines += _footer()

    out: list[str] = []
    for line in (raw.rstrip() for raw in lines):
        if not line and out and not out[-1]:
            continue  # never two blank lines in a row
        out.append(line)
    while out and not out[-1]:
        out.pop()
    return "\n".join(out) + "\n"
