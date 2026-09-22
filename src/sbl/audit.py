"""Audit log (JSONL) and the ``sbl explain`` trace (build_plan.md §2.5, §6 WP6).

One run, one line. The line is the whole :class:`~sbl.models.RunResult`, so a
past run can be re-rendered or explained months later without the library that
produced it — and the ``library_hash`` on the line says which library that was.

Like :mod:`sbl.markup`, nothing here imports the pydantic models at module
import time: both ``append_run`` and ``explain`` work off plain dicts, so an
audit line written by one version of the models can still be read by the next.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional

__all__ = ["append_run", "load_runs", "find_run", "explain", "split_rule_prefix"]


# ---------------------------------------------------------------------------
# Writing and reading
# ---------------------------------------------------------------------------


def _as_dict(result: Any) -> dict[str, Any]:
    """Return ``result`` as a JSON-safe dict, whether model or dict."""
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
        "append_run expects a RunResult or a dict decoded from one, "
        f"not {type(result).__name__}"
    )


def append_run(result: Any, path: Path) -> None:
    """Append ``result`` to the JSONL audit log at ``path``.

    Compact separators, sorted keys and ``ensure_ascii=False``, so the same run
    always produces the same bytes. Parent directories are created.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(
        _as_dict(result),
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
        default=str,
    )
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")


def load_runs(path: Path) -> list[dict[str, Any]]:
    """Read every run from the JSONL log at ``path``, oldest first.

    A missing log is an empty list, not an error: a first run has nothing to
    read. A malformed line is an error naming the line number.
    """
    path = Path(path)
    if not path.exists():
        return []
    runs: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            text = raw.strip()
            if not text:
                continue
            try:
                runs.append(json.loads(text))
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"{path}:{lineno}: audit line is not valid JSON: {exc}"
                ) from exc
    return runs


# ---------------------------------------------------------------------------
# Lookup
# ---------------------------------------------------------------------------


def _get(obj: Any, key: str, default: Any = None) -> Any:
    if isinstance(obj, Mapping):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _text(obj: Any, key: str, default: str = "") -> str:
    raw = _get(obj, key)
    if raw is None:
        return default
    value = getattr(raw, "value", raw) if not isinstance(raw, (str, int, float)) else raw
    out = str(value).strip()
    return out if out else default


def _strings(obj: Any, key: str) -> list[str]:
    raw = _get(obj, key) or []
    if isinstance(raw, (str, bytes, Mapping)):
        raw = [raw]
    return [s for s in (str(getattr(v, "value", v)).strip() for v in raw) if s]


def find_run(run_id: str, runs: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    """Find one run by exact id, or by an unambiguous id prefix.

    Raises ``LookupError`` when nothing matches, and when a prefix matches more
    than one run (naming the candidates, so the caller can lengthen it).
    """
    candidates = list(runs)
    if not candidates:
        raise LookupError(
            f"no runs recorded, so run '{run_id}' cannot be found. "
            "Run a deal first (`sbl run deals/<deal>.yaml`)."
        )
    for run in candidates:
        if _text(run, "run_id") == run_id:
            return dict(run)
    prefixed = [r for r in candidates if _text(r, "run_id").startswith(run_id)]
    if len(prefixed) == 1:
        return dict(prefixed[0])
    if not prefixed:
        known = ", ".join(sorted({_text(r, "run_id") for r in candidates})[:10])
        raise LookupError(
            f"no run matches id or prefix '{run_id}'. Known run ids include: {known}"
        )
    matched = ", ".join(sorted(_text(r, "run_id") for r in prefixed))
    raise LookupError(
        f"run id prefix '{run_id}' is ambiguous: it matches {len(prefixed)} runs "
        f"({matched}). Give more characters."
    )


def _find_clause(run: Mapping[str, Any], clause_id: str) -> dict[str, Any]:
    clauses = _get(run, "clauses") or []
    for clause in clauses:
        if _text(clause, "id") == clause_id:
            return dict(clause)
    known = ", ".join(sorted(_text(c, "id") for c in clauses)[:12])
    raise LookupError(
        f"run '{_text(run, 'run_id')}' has no clause '{clause_id}'. "
        f"Clauses in this run include: {known}"
    )


# ---------------------------------------------------------------------------
# Rule-id prefixes on rule-added items
# ---------------------------------------------------------------------------

#: ``[R07_pdmr_pledged_issuer] text`` -> ("R07_pdmr_pledged_issuer", "text")
_PREFIX_RE = re.compile(r"^\[([A-Za-z0-9_]+)\]\s*(.*)$", re.DOTALL)


def split_rule_prefix(
    item: str, rules_applied: Iterable[str] = ()
) -> tuple[Optional[str], str]:
    """Split ``"[R07_x] text"`` into ``("R07_x", "text")``.

    WP5 prefixes every rule-added condition precedent, representation and note
    with the id of the rule that added it. Items without a prefix are returned
    unchanged with ``None`` for the rule, so an older or hand-written line still
    explains cleanly.

    A bracketed token is only treated as a rule id when it is one of
    ``rules_applied`` or looks like a rule id (``R`` followed by a digit). That
    keeps a ``[VERIFY]`` prefix, which marks an unconfirmed statement rather
    than a rule, out of the "added by" column.
    """
    match = _PREFIX_RE.match(item.strip())
    if match is None:
        return None, item.strip()
    token, rest = match.group(1), match.group(2).strip()
    applied = set(rules_applied)
    if token in applied or re.match(r"^R\d", token):
        return token, rest
    return None, item.strip()


# ---------------------------------------------------------------------------
# explain
# ---------------------------------------------------------------------------


def _item_lines(
    heading: str, items: list[str], rules_applied: list[str]
) -> list[str]:
    if not items:
        return [f"{heading}: none."]
    out = [f"{heading} ({len(items)}):"]
    for item in items:
        rule_id, text = split_rule_prefix(item, rules_applied)
        origin = rule_id if rule_id else "originating rule not recorded on the item"
        out.append(f"  - {text}")
        out.append(f"      added by: {origin}")
    return out


def explain(run_id: str, clause_id: str, path: Path) -> str:
    """Explain how one clause outcome was reached in a past run.

    ``run_id`` may be the full id or any unambiguous prefix of one. Returns the
    trace as text; raises ``LookupError`` with a message that names what was
    looked for if the run or the clause is not in the log.
    """
    runs = load_runs(path)
    if not runs:
        raise LookupError(
            f"audit log '{path}' is empty or does not exist, so run '{run_id}' "
            "cannot be explained."
        )
    run = find_run(run_id, runs)
    clause = _find_clause(run, clause_id)

    intake = _get(run, "intake") or {}
    deal_id = _text(run, "deal_id") or _text(intake, "deal_id", "not recorded")
    rules_applied = _strings(clause, "rules_applied")

    lines: list[str] = [
        f"Run {_text(run, 'run_id', 'not recorded')} - deal {deal_id}",
        f"Timestamp:    {_text(run, 'timestamp', 'not recorded')}",
        f"Library hash: {_text(run, 'library_hash', 'not recorded')}",
        f"Intake hash:  {_text(run, 'intake_hash', 'not recorded')}",
        "",
        f"Clause: {_text(clause, 'id', clause_id)}"
        + (f" - {_text(clause, 'title')}" if _text(clause, "title") else ""),
        f"Status:  {_text(clause, 'status', 'not recorded')}",
        f"Opening: {_text(clause, 'opening', 'not recorded')}",
        f"Floor:   {_text(clause, 'floor', 'not recorded')}",
        "",
    ]

    if rules_applied:
        lines.append(f"Rules applied ({len(rules_applied)}):")
        lines += [f"  - {rule}" for rule in rules_applied]
    else:
        lines.append("Rules applied: none. This clause is at its library defaults.")
    lines.append("")

    lines += _item_lines(
        "Conditions precedent added by rules", _strings(clause, "cps"), rules_applied
    )
    lines.append("")
    lines += _item_lines(
        "Representations/undertakings added by rules",
        _strings(clause, "reps"),
        rules_applied,
    )
    lines.append("")
    lines += _item_lines(
        "Drafting notes added by rules", _strings(clause, "notes"), rules_applied
    )
    lines.append("")

    escalations = [
        e for e in (_get(run, "escalations") or []) if _text(e, "clause") == clause_id
    ]
    if escalations:
        lines.append(f"Escalations naming this clause ({len(escalations)}):")
        for esc in escalations:
            lines.append(
                f"  - {_text(esc, 'rule_id', 'not recorded')} -> "
                f"{_text(esc, 'to', 'not recorded')}"
            )
            lines.append(f"      reason: {_text(esc, 'reason', 'not recorded')}")
    else:
        lines.append("Escalations naming this clause: none.")
    lines.append("")

    outcomes = [
        o
        for o in (_get(run, "counterparty_request_outcomes") or [])
        if _text(o, "clause") == clause_id
    ]
    if outcomes:
        lines.append(f"Counterparty requests on this clause ({len(outcomes)}):")
        for out in outcomes:
            requested = _text(out, "requested_tier", "no tier requested")
            lines.append(
                f"  - requested {requested} against floor "
                f"{_text(out, 'floor', 'not recorded')}: "
                f"{_text(out, 'outcome', 'not recorded')}"
            )
            text = _text(out, "requested_text")
            if text:
                lines.append(f"      requested text: {text}")
    else:
        lines.append("Counterparty requests on this clause: none.")

    lines += [
        "",
        "This trace is derived entirely from the audit line for this run. "
        "Nothing here is legal advice.",
    ]

    cleaned = [line.rstrip() for line in lines]
    while cleaned and not cleaned[-1]:
        cleaned.pop()
    return "\n".join(cleaned) + "\n"
