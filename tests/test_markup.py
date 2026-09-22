"""WP6 tests: Markdown renderer, audit log and ``explain``.

The fixtures under ``tests/fixtures/runresult_*.json`` are hand-written run
results, not engine output, so these tests run green while WP5 is still moving.
They are entirely synthetic: "Borrower A" and "Aldergrove Trust" are invented,
and no real institution, firm or person appears anywhere.

To refresh the ``.expected.md`` snapshots after a deliberate renderer change::

    SBL_UPDATE_SNAPSHOTS=1 .venv/Scripts/python -m pytest tests/test_markup.py -q

and then read the diff before committing it.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from sbl.audit import append_run, explain, find_run, load_runs, split_rule_prefix
from sbl.markup import STATUS_WARNING, render_markdown

FIXTURES = Path(__file__).parent / "fixtures"
FIXTURE_NAMES = ("runresult_clean", "runresult_escalated")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load(name: str) -> dict:
    return json.loads((FIXTURES / f"{name}.json").read_text(encoding="utf-8"))


def _flat(value: str) -> str:
    """As the renderer writes a value outside a table: whitespace collapsed."""
    return " ".join(str(value).split())


def _cell(value: str) -> str:
    """As the renderer writes a value inside a table cell: pipes escaped."""
    return _flat(value).replace("|", "\\|")


def _first_sentence(text: str, limit: int = 160) -> str:
    """Mirror of the renderer's one-line ladder summary, for assertions."""
    import re

    flat = _flat(text)
    match = re.search(r"[.!?](?=\s|$)", flat)
    if match is not None and match.end() <= limit:
        return flat[: match.end()]
    if len(flat) <= limit:
        return flat
    return flat[:limit].rstrip() + "..."


@pytest.fixture(params=FIXTURE_NAMES)
def fixture_name(request):
    return request.param


@pytest.fixture
def clean() -> dict:
    return _load("runresult_clean")


@pytest.fixture
def escalated() -> dict:
    return _load("runresult_escalated")


class _FakeRunResult:
    """Duck-typed stand-in for a pydantic ``RunResult``.

    Used instead of importing ``sbl.models`` so these tests do not depend on
    where WP5 has got to with the model definitions.
    """

    def __init__(self, data: dict):
        self._data = data

    def model_dump(self, mode: str | None = None) -> dict:  # noqa: ARG002
        return self._data


# ---------------------------------------------------------------------------
# Fixture sanity: synthetic content, and the shapes the tests below assume
# ---------------------------------------------------------------------------


def test_fixtures_have_the_shape_the_plan_describes(clean, escalated):
    for data in (clean, escalated):
        statuses = [c["status"] for c in data["clauses"]]
        assert statuses.count("draft") == 12, "expected twelve drafted core clauses"
        assert statuses.count("stub") == 12, "expected twelve deferred stubs"
        for clause in data["clauses"]:
            if clause["status"] == "draft":
                assert [r["tier"] for r in clause["ladder"]] == [
                    "preferred",
                    "acceptable",
                    "fallback",
                    "unacceptable",
                ]
            else:
                assert clause["ladder"] == []
        assert data["governing_law"] == "england_wales"
        assert data["jurisdiction"]["id"] == "england_wales"

    assert clean["escalations"] == []
    assert [f["severity"] for f in clean["flags"]] == ["medium"]
    assert clean["exit_code"] == 0

    assert len(escalated["escalations"]) == 2
    assert sorted(f["severity"] for f in escalated["flags"]) == [
        "high",
        "low",
        "medium",
    ]
    assert escalated["exit_code"] == 2
    assert {o["outcome"] for o in escalated["counterparty_request_outcomes"]} == {
        "accepted_within_floor",
        "below_floor_escalated",
        "unacceptable_escalated",
    }


# ---------------------------------------------------------------------------
# Rendering: structure
# ---------------------------------------------------------------------------


def test_renders_without_error(fixture_name):
    markdown = render_markdown(_load(fixture_name))
    assert markdown.strip()


def test_section_headings_appear_in_plan_order(fixture_name):
    data = _load(fixture_name)
    markdown = render_markdown(data)

    expected = ["# SBL negotiation markup", "## Escalations", "## Flags"]
    expected.append("## Clause-by-clause")
    expected.append("## Jurisdiction overlay")
    if data["counterparty_request_outcomes"]:
        expected.append("## Counterparty request outcomes")
    expected.append("## Not automated on this deal")

    positions = []
    for heading in expected:
        index = markdown.find("\n" + heading) if positions else markdown.find(heading)
        assert index != -1, f"heading missing: {heading}"
        positions.append(index)
    assert positions == sorted(positions), "headings are out of order"


def test_counterparty_section_omitted_when_there_are_none(clean):
    assert not clean["counterparty_request_outcomes"]
    assert "## Counterparty request outcomes" not in render_markdown(clean)


def test_header_carries_the_run_identity_and_status_warning(escalated):
    markdown = render_markdown(escalated)
    for value in (
        escalated["deal_id"],
        escalated["description"],
        escalated["run_id"],
        escalated["timestamp"],
        escalated["library_hash"],
        escalated["intake_hash"],
        escalated["governing_law"],
    ):
        assert _flat(value) in markdown
    summary = escalated["status_summary"]
    assert (
        f"{summary['reviewed']} reviewed / {summary['draft']} draft / "
        f"{summary['stub']} stub"
    ) in markdown
    assert STATUS_WARNING in markdown
    assert "not been reviewed by a named human reviewer" in markdown


def test_no_escalations_renders_the_explicit_line_and_exit_code(clean):
    markdown = render_markdown(clean)
    assert "No escalations." in markdown
    assert "Exit code: 0" in markdown


def test_escalations_render_as_a_table_with_who_decides(escalated):
    markdown = render_markdown(escalated)
    assert "| Rule id | Clause | Who decides | Reason |" in markdown
    for escalation in escalated["escalations"]:
        for key in ("rule_id", "clause", "to", "reason"):
            assert _cell(escalation[key]) in markdown
    assert "Exit code: 2" in markdown


def test_flags_are_grouped_high_then_medium_then_low(escalated):
    markdown = render_markdown(escalated)
    high = markdown.index("### High severity")
    medium = markdown.index("### Medium severity")
    low = markdown.index("### Low severity")
    assert high < medium < low
    for flag in escalated["flags"]:
        assert flag["id"] in markdown
        assert _flat(flag["message"]) in markdown
        assert _flat(flag["who_decides"]) in markdown
        assert flag["rule_id"] in markdown


def test_verify_prefix_on_a_flag_message_survives_intact(escalated):
    verify_flags = [f for f in escalated["flags"] if f["message"].startswith("[VERIFY]")]
    assert verify_flags, "fixture must carry a [VERIFY]-prefixed flag message"
    markdown = render_markdown(escalated)
    for flag in verify_flags:
        assert _flat(flag["message"]) in markdown
        assert "[VERIFY]" in markdown


def test_pipe_inside_a_table_cell_is_escaped(escalated):
    clause = next(
        c for c in escalated["clauses"] if c["id"] == "enforcement_liquidation"
    )
    rung = next(r for r in clause["ladder"] if r["tier"] == "acceptable")
    assert "|" in rung["text"], "fixture must carry a pipe inside a ladder rung"

    markdown = render_markdown(escalated)
    table_rows = [
        line
        for line in markdown.splitlines()
        if line.startswith("| ") and "appropriation" in line
    ]
    assert table_rows, "the rung with the pipe should appear in the ladder table"
    for row in table_rows:
        # Every pipe in a table row is either a column separator or escaped.
        stripped = row.replace("\\|", "")
        assert stripped.count("|") == 5, f"unescaped pipe in table row: {row}"
    assert "sale \\| appropriation" in markdown


# ---------------------------------------------------------------------------
# Rendering: every string that is meant to appear, does
# ---------------------------------------------------------------------------


def test_every_rendered_string_field_of_the_fixture_appears(fixture_name):
    data = _load(fixture_name)
    markdown = render_markdown(data)
    missing: list[str] = []

    def want(value, in_table_cell=False):
        if not value:
            return
        expected = _cell(value) if in_table_cell else _flat(value)
        if expected not in markdown:
            missing.append(expected)

    for clause in data["clauses"]:
        want(clause["title"])
        want(clause.get("jurisdiction_note"))
        for key in ("cps", "reps", "notes", "escalation_triggers"):
            for item in clause.get(key) or []:
                want(item)
        for rule_id in clause["rules_applied"]:
            want(rule_id)
        if clause["status"] == "stub":
            continue
        want(clause["opening_text"])
        want(clause["opening_rationale"])
        for rung in clause["ladder"]:
            want(_first_sentence(rung["text"]), in_table_cell=True)
            for condition in rung["conditions"]:
                want(condition, in_table_cell=True)
            want(rung.get("approval"), in_table_cell=True)

    for flag in data["flags"]:
        want(flag["id"])
        want(flag["message"])
        want(flag["who_decides"])
        want(flag["rule_id"])

    for escalation in data["escalations"]:
        for key in ("rule_id", "clause", "to", "reason"):
            want(escalation.get(key), in_table_cell=True)

    for outcome in data["counterparty_request_outcomes"]:
        for key in ("clause", "requested_tier", "requested_text", "floor", "outcome"):
            want(outcome.get(key), in_table_cell=True)

    for item in data["not_automated"]:
        want(item)

    for key, value in (data["jurisdiction"] or {}).items():
        if key != "status":
            want(value)

    assert not missing, "values missing from the markup:\n" + "\n".join(missing[:10])


def test_stub_clauses_render_compactly(clean):
    markdown = render_markdown(clean)
    stub = next(c for c in clean["clauses"] if c["status"] == "stub")
    start = markdown.index(f"### {stub['title']} [STUB]")
    end = markdown.index("### ", start + 4)
    section = markdown[start:end]
    assert "No drafted positions yet; status stub." in section
    assert "Rules applied: none" in section
    assert "**Position ladder**" not in section
    assert "**Opening:" not in section


def test_drafted_clause_shows_tag_opening_floor_and_ladder(clean):
    markdown = render_markdown(clean)
    clause = next(c for c in clean["clauses"] if c["id"] == "facility_type")
    start = markdown.index(f"### {clause['title']} [DRAFT]")
    end = markdown.index("### ", start + 4)
    section = markdown[start:end]
    assert f"- Risk rating: {clause['risk_rating']}" in section
    assert f"- Category: {clause['category']}" in section
    assert f"- Document: {clause['document']}" in section
    assert f"**Opening: {clause['opening']}**" in section
    assert f"**Floor: {clause['floor']}**" in section
    assert "| Tier | Summary | Conditions | Approver |" in section
    assert "unacceptable (description of the walk-away line, not drafting)" in section
    floor_rung = next(r for r in clause["ladder"] if r["tier"] == clause["floor"])
    assert f"approver: {_flat(floor_rung['approval'])}" in section
    assert f"**Jurisdiction note ({clean['governing_law']})**" in section


def test_clause_order_follows_the_result(fixture_name):
    data = _load(fixture_name)
    markdown = render_markdown(data)
    positions = [markdown.index(f"### {c['title']} ") for c in data["clauses"]]
    assert positions == sorted(positions)


def test_headings_omitted_when_the_underlying_list_is_empty(clean):
    markdown = render_markdown(clean)
    assert "**Conditions precedent added by rules**" not in markdown
    assert "**Representations/undertakings added by rules**" not in markdown
    assert "**Drafting notes**" not in markdown


def test_not_automated_heading_is_always_rendered():
    markdown = render_markdown({"run_id": "r", "timestamp": "t", "clauses": []})
    assert "## Not automated on this deal" in markdown
    assert "None triggered on this deal." in markdown


def test_footer_disclaimer_is_present(fixture_name):
    markdown = render_markdown(_load(fixture_name))
    for phrase in (
        "built from public sources",
        "synthetic deals",
        "not legal advice",
        "has not been validated against any institution",
    ):
        assert phrase.lower() in markdown.lower(), phrase


# ---------------------------------------------------------------------------
# Rendering: determinism and the "from JSON alone" property
# ---------------------------------------------------------------------------


def test_rendering_is_deterministic(fixture_name):
    data = _load(fixture_name)
    assert render_markdown(data) == render_markdown(data)
    assert render_markdown(_load(fixture_name)) == render_markdown(data)


def test_render_from_a_json_round_trip_is_identical(fixture_name):
    data = _load(fixture_name)
    assert render_markdown(data) == render_markdown(json.loads(json.dumps(data)))


def test_render_accepts_a_model_like_object(fixture_name):
    data = _load(fixture_name)
    assert render_markdown(_FakeRunResult(data)) == render_markdown(data)


def test_render_rejects_something_that_is_neither():
    with pytest.raises(TypeError):
        render_markdown("not a run result")


def test_output_has_no_trailing_whitespace_and_one_final_newline(fixture_name):
    markdown = render_markdown(_load(fixture_name))
    assert "\r" not in markdown
    assert markdown.endswith("\n")
    assert not markdown.endswith("\n\n")
    for lineno, line in enumerate(markdown.split("\n"), start=1):
        assert line == line.rstrip(), f"trailing whitespace on line {lineno}"


def test_no_date_other_than_the_result_timestamp(fixture_name):
    import re

    data = _load(fixture_name)
    markdown = render_markdown(data)
    dates = set(re.findall(r"\d{4}-\d{2}-\d{2}", markdown))
    assert dates <= {data["timestamp"][:10]}


def test_matches_the_committed_snapshot(fixture_name):
    markdown = render_markdown(_load(fixture_name))
    snapshot = FIXTURES / f"{fixture_name}.expected.md"
    if os.environ.get("SBL_UPDATE_SNAPSHOTS"):
        snapshot.write_text(markdown, encoding="utf-8", newline="\n")
    assert snapshot.exists(), f"missing snapshot {snapshot}"
    assert markdown == snapshot.read_text(encoding="utf-8"), (
        f"rendered markup differs from {snapshot.name}. If the change is "
        "deliberate, rerun with SBL_UPDATE_SNAPSHOTS=1 and read the diff."
    )


# ---------------------------------------------------------------------------
# Audit log
# ---------------------------------------------------------------------------


def test_append_then_load_round_trips(tmp_path, clean, escalated):
    log = tmp_path / "nested" / "audit.jsonl"
    append_run(clean, log)
    append_run(escalated, log)

    runs = load_runs(log)
    assert runs == [clean, escalated]
    assert log.read_bytes().count(b"\n") == 2
    assert b"\r\n" not in log.read_bytes()


def test_append_is_byte_stable_and_sorted(tmp_path, clean):
    first = tmp_path / "a.jsonl"
    second = tmp_path / "b.jsonl"
    append_run(clean, first)
    append_run(_FakeRunResult(clean), second)
    assert first.read_bytes() == second.read_bytes()

    line = json.loads(first.read_text(encoding="utf-8"))
    assert list(line) == sorted(line), "keys should be sorted for a stable diff"


def test_load_runs_on_a_missing_log_is_empty(tmp_path):
    assert load_runs(tmp_path / "nothing.jsonl") == []


def test_load_runs_rejects_a_malformed_line(tmp_path):
    log = tmp_path / "audit.jsonl"
    log.write_text("{not json}\n", encoding="utf-8")
    with pytest.raises(ValueError) as excinfo:
        load_runs(log)
    assert "audit.jsonl:1" in str(excinfo.value)


def test_appended_run_still_renders(tmp_path, escalated):
    log = tmp_path / "audit.jsonl"
    append_run(escalated, log)
    assert render_markdown(load_runs(log)[0]) == render_markdown(escalated)


# ---------------------------------------------------------------------------
# explain
# ---------------------------------------------------------------------------


@pytest.fixture
def log(tmp_path, clean, escalated) -> Path:
    path = tmp_path / "runs" / "audit.jsonl"
    append_run(clean, path)
    append_run(escalated, path)
    return path


def test_explain_finds_a_run_by_full_id(log, escalated):
    out = explain(escalated["run_id"], "enforcement_liquidation", log)
    assert escalated["run_id"] in out
    assert escalated["deal_id"] in out
    assert "Enforcement and liquidation of the collateral" in out


def test_explain_finds_a_run_by_unique_prefix(log, escalated):
    full = explain(escalated["run_id"], "enforcement_liquidation", log)
    short = explain(escalated["run_id"][:6], "enforcement_liquidation", log)
    assert short == full


def test_explain_reports_opening_floor_status_and_rules(log, escalated):
    clause = next(
        c for c in escalated["clauses"] if c["id"] == "enforcement_liquidation"
    )
    out = explain(escalated["run_id"], clause["id"], log)
    assert f"Opening: {clause['opening']}" in out
    assert f"Floor:   {clause['floor']}" in out
    assert f"Status:  {clause['status']}" in out
    for rule_id in clause["rules_applied"]:
        assert rule_id in out


def test_explain_attributes_each_item_to_its_originating_rule(log, escalated):
    clause = next(c for c in escalated["clauses"] if c["id"] == "capacity_authority")
    out = explain(escalated["run_id"], clause["id"], log)
    for item in clause["cps"] + clause["reps"] + clause["notes"]:
        rule_id, text = split_rule_prefix(item, clause["rules_applied"])
        assert text in out
        assert f"added by: {rule_id}" in out


def test_explain_handles_an_unprefixed_item_gracefully(log, escalated):
    clause = next(
        c for c in escalated["clauses"] if c["id"] == "third_party_security_waivers"
    )
    unprefixed = [
        n for n in clause["notes"] if split_rule_prefix(n, clause["rules_applied"])[0] is None
    ]
    assert unprefixed, "fixture must carry an item with no rule-id prefix"
    out = explain(escalated["run_id"], clause["id"], log)
    assert "originating rule not recorded on the item" in out
    for item in unprefixed:
        assert item in out


def test_explain_lists_escalations_and_requests_for_that_clause(log, escalated):
    out = explain(escalated["run_id"], "enforcement_liquidation", log)
    escalation = next(
        e for e in escalated["escalations"] if e["clause"] == "enforcement_liquidation"
    )
    assert escalation["rule_id"] in out
    assert escalation["to"] in out
    assert escalation["reason"] in out
    assert "unacceptable_escalated" in out


def test_explain_says_none_where_a_clause_is_untouched(log, clean):
    out = explain(clean["run_id"], "facility_type", log)
    assert "Rules applied: none" in out
    assert "Escalations naming this clause: none." in out
    assert "Counterparty requests on this clause: none." in out
    assert "Conditions precedent added by rules: none." in out


def test_explain_raises_on_an_unknown_run(log):
    with pytest.raises(LookupError) as excinfo:
        explain("deadbeef", "facility_type", log)
    assert "deadbeef" in str(excinfo.value)


def test_explain_raises_on_an_unknown_clause(log, escalated):
    with pytest.raises(LookupError) as excinfo:
        explain(escalated["run_id"], "not_a_clause", log)
    message = str(excinfo.value)
    assert "not_a_clause" in message
    assert "facility_type" in message, "the message should list real clause ids"


def test_explain_raises_on_an_empty_log(tmp_path):
    with pytest.raises(LookupError):
        explain("anything", "facility_type", tmp_path / "audit.jsonl")


def test_find_run_rejects_an_ambiguous_prefix(clean, escalated):
    a = dict(clean, run_id="abc111")
    b = dict(escalated, run_id="abc222")
    with pytest.raises(LookupError) as excinfo:
        find_run("abc", [a, b])
    assert "ambiguous" in str(excinfo.value)
    assert find_run("abc1", [a, b])["run_id"] == "abc111"


def test_explain_output_is_deterministic(log, escalated):
    first = explain(escalated["run_id"], "conditions_precedent", log)
    second = explain(escalated["run_id"], "conditions_precedent", log)
    assert first == second
    assert first.endswith("\n") and not first.endswith("\n\n")


# ---------------------------------------------------------------------------
# The rule-id prefix convention
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("item", "applied", "expected"),
    [
        ("[R07_pdmr_pledged_issuer] Clear insider status.", ["R07_pdmr_pledged_issuer"], ("R07_pdmr_pledged_issuer", "Clear insider status.")),
        ("[R01] Review the trust deed.", [], ("R01", "Review the trust deed.")),
        ("No prefix at all.", [], (None, "No prefix at all.")),
        ("[VERIFY] Not confirmed against a primary source.", ["R07_x"], (None, "[VERIFY] Not confirmed against a primary source.")),
        ("  [R06_concentration]  Spaced out.  ", ["R06_concentration"], ("R06_concentration", "Spaced out.")),
    ],
)
def test_split_rule_prefix(item, applied, expected):
    assert split_rule_prefix(item, applied) == expected
