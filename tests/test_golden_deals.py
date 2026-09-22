"""End-to-end tests over the six golden deals (build_plan.md §5, WP9).

Two layers, deliberately kept apart:

1. **Explicit assertions.** One test function per deal, asserting the "must
   produce" conditions from `build_plan.md` §5 by name: which rules fired,
   which flags at which severity, which floors moved, the exit code, the
   jurisdiction overlay, and the counterparty-request outcomes. These say what
   the deal is *for*, and they fail with a readable message.
2. **Snapshot equality.** The rendered Markdown and the run JSON are compared
   byte for byte against `tests/expected/<deal file stem>.md` / `.json`, with
   `run_id` and `timestamp` — the only two non-deterministic fields in a
   `RunResult` — replaced by fixed placeholders. Regenerate with
   `SBL_UPDATE_SNAPSHOTS=1 pytest tests/test_golden_deals.py`.

Where §5's wording and the rule set as built disagree, the assertion here
records **what the engine actually does**, with the divergence named in a
comment and in `handoff/WP9.md` §3. Nothing is weakened silently.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from sbl.engine import NO_CHANGE_SUFFIX, evaluate
from sbl.loader import load_intake, load_library
from sbl.markup import render_markdown
from sbl.models import RunResult

ROOT = Path(__file__).resolve().parents[1]
DEALS_DIR = ROOT / "deals"
EXPECTED_DIR = Path(__file__).resolve().parent / "expected"

#: Fixed stand-ins for the two non-deterministic fields. Twelve zeros matches
#: the width of a real ``run_id`` so the Markdown header lines up.
RUN_ID_PLACEHOLDER = "000000000000"
TIMESTAMP_PLACEHOLDER = "1970-01-01T00:00:00+00:00"

#: Deal id -> deal file stem. The stem is also the snapshot file name, which is
#: the layout in build_plan.md §1.
DEAL_FILES: dict[str, str] = {
    "D01": "D01_plain_vanilla",
    "D02": "D02_trust_concentrated_pdmr",
    "D03": "D03_swiss_corporate_purpose",
    "D04": "D04_third_party_pledge_lux",
    "D05": "D05_real_estate_hard_stop",
    "D06": "D06_below_floor_request",
}

#: The floor every clause starts at when no rule touches it. A clause entry
#: without an explicit ``default_floor`` (every stub) gets ``fallback`` from
#: ``engine.STUB_DEFAULT_FLOOR``.
DEFAULT_FLOORS_OVERRIDE = {"facility_type": "acceptable"}


# ---------------------------------------------------------------------------
# Fixtures and helpers
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def library():
    return load_library(ROOT)


@pytest.fixture(scope="module")
def runs(library) -> dict[str, RunResult]:
    """Every golden deal, evaluated once."""
    out: dict[str, RunResult] = {}
    for deal_id, stem in DEAL_FILES.items():
        intake = load_intake(DEALS_DIR / f"{stem}.yaml")
        assert intake.deal_id == deal_id, (
            f"{stem}.yaml declares deal_id '{intake.deal_id}', expected '{deal_id}'"
        )
        out[deal_id] = evaluate(library, intake)
    return out


def rules_fired(result: RunResult) -> set[str]:
    """Every rule id that appears in any clause's ``rules_applied``.

    The ``(no change)`` suffix is stripped: for "did this rule fire on this
    deal" the distinction between "changed a clause" and "looked at a clause
    and changed nothing" does not matter. Where it does matter the test says so
    explicitly.
    """
    fired: set[str] = set()
    for clause in result.clauses:
        for entry in clause.rules_applied:
            fired.add(
                entry[: -len(NO_CHANGE_SUFFIX)]
                if entry.endswith(NO_CHANGE_SUFFIX)
                else entry
            )
    return fired


def floors(result: RunResult) -> dict[str, str]:
    return {c.id: c.floor.value for c in result.clauses}


def flags_by_id(result: RunResult) -> dict[str, str]:
    """Flag id -> severity. Ids are unique within a run in the current rule set."""
    return {f.id: f.severity.value for f in result.flags}


def default_floors(library) -> dict[str, str]:
    out = {}
    for clause_id, clause in library.clauses.items():
        out[clause_id] = (
            clause.default_floor.value if clause.default_floor else "fallback"
        )
    return out


def normalised_json(result: RunResult) -> str:
    """The run JSON with ``run_id`` and ``timestamp`` replaced, as text."""
    data = result.model_dump(mode="json")
    data["run_id"] = RUN_ID_PLACEHOLDER
    data["timestamp"] = TIMESTAMP_PLACEHOLDER
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def normalised_markdown(result: RunResult) -> str:
    """The rendered Markdown with the two non-deterministic values replaced.

    The substitution is done on the rendered text rather than on the model, so
    the renderer is exercised exactly as ``sbl run`` exercises it.
    """
    text = render_markdown(result)
    text = text.replace(result.run_id, RUN_ID_PLACEHOLDER)
    text = text.replace(result.timestamp, TIMESTAMP_PLACEHOLDER)
    return text


def _snapshot(path: Path, actual: str) -> None:
    """Compare against the snapshot, or rewrite it when asked to."""
    if os.environ.get("SBL_UPDATE_SNAPSHOTS") == "1":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(actual, encoding="utf-8", newline="\n")
        return
    assert path.exists(), (
        f"missing snapshot {path.relative_to(ROOT).as_posix()}. Regenerate with "
        f"SBL_UPDATE_SNAPSHOTS=1 pytest tests/test_golden_deals.py"
    )
    expected = path.read_text(encoding="utf-8")
    assert actual == expected, (
        f"{path.relative_to(ROOT).as_posix()} is out of date. If the change is "
        f"intended, regenerate with "
        f"SBL_UPDATE_SNAPSHOTS=1 pytest tests/test_golden_deals.py and read the diff."
    )


# ---------------------------------------------------------------------------
# All six deals: shared invariants
# ---------------------------------------------------------------------------


def test_all_six_deals_exist():
    """build_plan.md §5 names six deals; deals/ holds exactly those six."""
    on_disk = sorted(p.stem for p in DEALS_DIR.glob("*.yaml"))
    assert on_disk == sorted(DEAL_FILES.values())


@pytest.mark.parametrize("deal_id", sorted(DEAL_FILES))
def test_description_is_marked_synthetic(runs, deal_id):
    """build_plan.md §0 rule 2: every deal says it is synthetic, up front."""
    assert runs[deal_id].description.startswith("Synthetic.")


@pytest.mark.parametrize("deal_id", sorted(DEAL_FILES))
def test_exit_code_tracks_escalations(runs, deal_id):
    """build_plan.md §2.4: exit code is 2 if and only if something escalated."""
    result = runs[deal_id]
    assert result.exit_code == (2 if result.escalations else 0)


@pytest.mark.parametrize("deal_id", sorted(DEAL_FILES))
def test_every_clause_in_every_run(runs, library, deal_id):
    """Every clause in the library is scored on every deal, stubs included."""
    result = runs[deal_id]
    assert [c.id for c in result.clauses] == list(library.clauses)


@pytest.mark.parametrize("deal_id", sorted(DEAL_FILES))
def test_nothing_is_reviewed(runs, deal_id):
    """build_plan.md §0 rule 3: no agent may promote an entry to 'reviewed'."""
    assert runs[deal_id].status_summary.get("reviewed", 0) == 0


# ---------------------------------------------------------------------------
# D01 — plain vanilla
#
# §5: "no escalations; consumer_credit flag at medium; exit code 0; all clauses
# at default floor".
# ---------------------------------------------------------------------------


def test_D01_no_escalations_and_exit_zero(runs):
    result = runs["D01"]
    assert result.escalations == []
    assert result.exit_code == 0


def test_D01_consumer_credit_flag_at_medium(runs):
    result = runs["D01"]
    assert flags_by_id(result)["consumer_credit"] == "medium"
    assert any(
        f.id == "consumer_credit" and f.rule_id == "R03b_natural_person_borrower_declared"
        for f in result.flags
    )


def test_D01_also_raises_the_fcar_safe_harbour_flag(runs):
    """DIVERGENCE from §5, recorded rather than hidden (handoff/WP9.md §3, row 1).

    §5 names only ``consumer_credit`` for D01. R04 also fires, because the
    collateral provider is a natural person and the security is English law,
    which is exactly the combination R04 exists to catch. The flag is correct
    on these facts; §5 simply did not anticipate it. Asserting it here means a
    later change that silences R04 fails a test.
    """
    assert flags_by_id(runs["D01"])["fcar_safe_harbour_uncertain"] == "medium"
    assert sorted(flags_by_id(runs["D01"])) == [
        "consumer_credit",
        "fcar_safe_harbour_uncertain",
    ]


def test_D01_all_clauses_at_default_floor(runs, library):
    """§5's "all clauses at default floor" holds: no rule on D01 sets a floor."""
    defaults = default_floors(library)
    assert floors(runs["D01"]) == defaults


def test_D01_only_the_two_individual_borrower_rules_fire(runs):
    assert rules_fired(runs["D01"]) == {
        "R03b_natural_person_borrower_declared",
        "R04_natural_person_pledgor_england",
    }


def test_D01_no_counterparty_requests(runs):
    assert runs["D01"].counterparty_request_outcomes == []


# ---------------------------------------------------------------------------
# D02 — trust, concentrated, PDMR
#
# §5: "R01, R06, R06b, R07 fire; escalations >= 2; enforcement_liquidation
# floor = acceptable; exit 2".
# ---------------------------------------------------------------------------


def test_D02_the_four_named_rules_fire(runs):
    fired = rules_fired(runs["D02"])
    for rule_id in (
        "R01_trust_borrower",
        "R06_concentration",
        "R06b_concentration_severe",
        "R07_pdmr_pledged_issuer",
    ):
        assert rule_id in fired, f"{rule_id} did not fire on D02"


def test_D02_no_other_rule_fires(runs):
    """The four named rules are also the only ones: the deal is not noisy."""
    assert rules_fired(runs["D02"]) == {
        "R01_trust_borrower",
        "R06_concentration",
        "R06b_concentration_severe",
        "R07_pdmr_pledged_issuer",
    }


def test_D02_at_least_two_escalations(runs):
    result = runs["D02"]
    assert len(result.escalations) >= 2
    assert {e.rule_id for e in result.escalations} == {
        "R06b_concentration_severe",
        "R07_pdmr_pledged_issuer",
    }


def test_D02_enforcement_liquidation_floor_is_acceptable(runs):
    """R07 raises it from the clause default of fallback."""
    assert floors(runs["D02"])["enforcement_liquidation"] == "acceptable"


def test_D02_concentration_floors_raised_by_R06_and_R06b(runs):
    f = floors(runs["D02"])
    assert f["concentration_limits"] == "acceptable"
    assert f["margin_maintenance_cure"] == "acceptable"
    assert f["eligible_collateral_lending_values"] == "acceptable"
    assert f["capacity_authority"] == "acceptable"


def test_D02_market_abuse_flag_high(runs):
    assert flags_by_id(runs["D02"])["market_abuse"] == "high"


def test_D02_exit_two(runs):
    assert runs["D02"].exit_code == 2


def test_D02_R06b_recorded_as_no_change_on_margin_maintenance_cure(runs):
    """R06b sets that clause's *opening* to preferred, which it already is.

    The engine records the rule with the ``(no change)`` suffix rather than
    dropping it, so the log still answers "did R06b look at this clause?".
    """
    clause = next(
        c for c in runs["D02"].clauses if c.id == "margin_maintenance_cure"
    )
    assert "R06b_concentration_severe" + NO_CHANGE_SUFFIX in clause.rules_applied


# ---------------------------------------------------------------------------
# D03 — Swiss corporate, acquire securities
#
# §5: "R02, R10, R11, R13, R14 fire; mifid_suitability + bank_secrecy_data
# flags; Swiss jurisdiction notes printed".
# ---------------------------------------------------------------------------


def test_D03_the_five_named_rules_fire(runs):
    assert rules_fired(runs["D03"]) == {
        "R02_corporate_or_partnership",
        "R10_purpose_acquire_securities",
        "R11_committed_term",
        "R13_currency_mismatch",
        "R14_swiss_booking",
    }


def test_D03_flags(runs):
    severities = flags_by_id(runs["D03"])
    assert severities["mifid_suitability"] == "medium"
    assert severities["bank_secrecy_data"] == "low"
    assert sorted(severities) == ["bank_secrecy_data", "mifid_suitability"]


def test_D03_swiss_jurisdiction_summary(runs):
    result = runs["D03"]
    assert result.governing_law.value == "switzerland"
    assert result.jurisdiction is not None
    assert result.jurisdiction.id == "switzerland"


def test_D03_markdown_prints_the_swiss_overlay(runs):
    md = normalised_markdown(runs["D03"])
    assert "- Governing law: switzerland" in md
    assert "## Jurisdiction overlay — " in md
    assert "**Jurisdiction note (switzerland)**" in md
    # The overlay printed is the Swiss one, not another jurisdiction's.
    assert runs["D03"].jurisdiction.name in md
    assert "**Jurisdiction note (england_wales)**" not in md
    assert "**Jurisdiction note (luxembourg)**" not in md


def test_D03_floors_raised_by_R10_R11_R13(runs):
    f = floors(runs["D03"])
    assert f["no_advice_non_reliance"] == "acceptable"  # R10
    assert f["events_of_default"] == "acceptable"  # R11
    assert f["lender_discretion_valuation"] == "acceptable"  # R13


def test_D03_no_escalation_and_exit_zero(runs):
    """None of R02/R10/R11/R13/R14 escalates, so this cross-border deal is clean.

    §5 gives no exit code for D03; this records the one the rule set produces,
    and `check.ps1` expects it.
    """
    assert runs["D03"].escalations == []
    assert runs["D03"].exit_code == 0


# ---------------------------------------------------------------------------
# D04 — third-party pledge, Luxembourg
#
# §5: "R03, R05, R12 fire; require_cp account control; Lux notes printed;
# consumer_credit flag".
# ---------------------------------------------------------------------------


def test_D04_R03a_fires_not_R03b(runs):
    """DIVERGENCE from §5, recorded (handoff/WP9.md §3, rows 2 and 3).

    §5 names "R03". WP5 split it into R03a (no declaration: high, escalates)
    and R03b (declaration on file: medium, no escalation). D04's borrower has
    neither declaration, so R03a fires — and R03a escalates, which §5's D04 row
    does not mention. The escalation is the honest outcome on these facts.
    """
    fired = rules_fired(runs["D04"])
    assert "R03a_natural_person_borrower_no_declaration" in fired
    assert "R03b_natural_person_borrower_declared" not in fired


def test_D04_R05_and_R12_fire_but_not_R05b(runs):
    """R05b needs a *corporate* pledgor; D04's is an individual, so it stays out."""
    fired = rules_fired(runs["D04"])
    assert "R05_third_party_security" in fired
    assert "R12_third_party_custodian" in fired
    assert "R05b_third_party_corporate_pledgor" not in fired
    assert fired == {
        "R03a_natural_person_borrower_no_declaration",
        "R05_third_party_security",
        "R12_third_party_custodian",
    }


def test_D04_consumer_credit_flag_is_high_and_escalates(runs):
    """§5 says only "consumer_credit flag"; on these facts it lands at high."""
    result = runs["D04"]
    assert flags_by_id(result) == {"consumer_credit": "high"}
    assert [e.rule_id for e in result.escalations] == [
        "R03a_natural_person_borrower_no_declaration"
    ]
    assert result.escalations[0].to == "senior lawyer + compliance"
    assert result.exit_code == 2


def test_D04_require_cp_account_control_agreement(runs):
    """R12's condition precedent lands on conditions_precedent, rule id attached."""
    cps = next(
        c for c in runs["D04"].clauses if c.id == "conditions_precedent"
    ).cps
    matches = [
        cp
        for cp in cps
        if cp.startswith("[R12_third_party_custodian] ")
        and "Account control agreement" in cp
    ]
    assert matches, f"no account control CP in conditions_precedent: {cps}"


def test_D04_luxembourg_jurisdiction_summary_and_notes(runs):
    result = runs["D04"]
    assert result.governing_law.value == "luxembourg"
    assert result.jurisdiction is not None
    assert result.jurisdiction.id == "luxembourg"
    md = normalised_markdown(result)
    assert "- Governing law: luxembourg" in md
    assert "**Jurisdiction note (luxembourg)**" in md
    assert result.jurisdiction.name in md
    assert "**Jurisdiction note (england_wales)**" not in md
    assert "**Jurisdiction note (switzerland)**" not in md


def test_D04_floors_raised_by_R05_and_R12(runs):
    f = floors(runs["D04"])
    assert f["capacity_authority"] == "acceptable"  # R05
    assert f["security_structure_control"] == "acceptable"  # R12


# ---------------------------------------------------------------------------
# D05 — real estate hard stop
#
# §5: "R09 fires; escalation; exit 2; markup header says out of scope".
# ---------------------------------------------------------------------------


def test_D05_R09_fires(runs):
    assert "R09_real_estate" in rules_fired(runs["D05"])


def test_D05_is_D01_plus_R09(runs):
    """The only difference from D01's rule set is R09."""
    assert rules_fired(runs["D05"]) - rules_fired(runs["D01"]) == {"R09_real_estate"}
    assert rules_fired(runs["D01"]) - rules_fired(runs["D05"]) == set()


def test_D05_escalates_and_exits_two(runs):
    result = runs["D05"]
    assert [e.rule_id for e in result.escalations] == ["R09_real_estate"]
    assert result.escalations[0].clause == "eligible_collateral_lending_values"
    assert result.escalations[0].to == "senior lawyer"
    assert result.exit_code == 2


def test_D05_mortgage_regulation_flag_high(runs):
    assert flags_by_id(runs["D05"])["mortgage_regulation"] == "high"


def test_D05_markup_says_real_estate_is_out_of_scope(runs):
    """§5: "markup header says out of scope".

    The escalations table sits immediately under the header and carries R09's
    reason, "Real estate collateral is outside the scope of this playbook";
    R09's drafting note repeats it as "Real estate is out of scope for this
    playbook" on two clauses. Both wordings are asserted, so a rewording of
    either is a visible test failure rather than a quiet loss of the warning.
    """
    md = normalised_markdown(runs["D05"])
    header_and_escalations = md.split("## Flags", 1)[0]
    assert (
        "Real estate collateral is outside the scope of this playbook."
        in header_and_escalations
    )
    assert "Real estate is out of scope for this playbook." in md
    for clause_id in ("eligible_collateral_lending_values", "enforcement_liquidation"):
        clause = next(c for c in runs["D05"].clauses if c.id == clause_id)
        assert any(
            n.startswith("[R09_real_estate] ")
            and "out of scope for this playbook" in n
            for n in clause.notes
        ), f"R09's out-of-scope note is missing from {clause_id}"


def test_D05_r09_moves_no_floor(runs, library):
    """R09 stops the deal rather than repricing it: it sets no floor at all.

    So D05's floors are D01's floors, which are the library defaults.
    """
    assert floors(runs["D05"]) == default_floors(library)


# ---------------------------------------------------------------------------
# D06 — counterparty requests
#
# §5: "first request accepted within floor and logged; second is hard
# escalation; exit 2".
# ---------------------------------------------------------------------------


def test_D06_request_outcomes(runs):
    outcomes = {
        o.clause: o for o in runs["D06"].counterparty_request_outcomes
    }
    assert set(outcomes) == {"margin_maintenance_cure", "enforcement_liquidation"}

    cure = outcomes["margin_maintenance_cure"]
    assert cure.requested_tier.value == "fallback"
    assert cure.floor.value == "fallback"
    assert cure.outcome.value == "accepted_within_floor"

    enforcement = outcomes["enforcement_liquidation"]
    assert enforcement.requested_tier.value == "unacceptable"
    assert enforcement.outcome.value == "unacceptable_escalated"


def test_D06_accepted_request_is_logged_with_its_approver(runs):
    """"Accepted" is not silent: R16 writes a note naming tier, floor and approver."""
    clause = next(
        c for c in runs["D06"].clauses if c.id == "margin_maintenance_cure"
    )
    notes = [n for n in clause.notes if n.startswith("[R16] ")]
    assert len(notes) == 1
    assert "accepted within floor at tier 'fallback'" in notes[0]
    assert "approver:" in notes[0]
    assert "R16" in clause.rules_applied


def test_D06_unacceptable_request_is_a_hard_escalation(runs):
    result = runs["D06"]
    assert [e.rule_id for e in result.escalations] == ["R16"]
    escalation = result.escalations[0]
    assert escalation.clause == "enforcement_liquidation"
    assert escalation.to == "senior lawyer"
    assert "walk-away line" in escalation.reason
    assert result.exit_code == 2


def test_D06_is_D01_plus_R16(runs):
    """Only R16 separates D06 from D01: the requests are the whole difference."""
    assert rules_fired(runs["D06"]) - rules_fired(runs["D01"]) == {"R16"}


def test_D06_floors_unchanged_by_the_requests(runs, library):
    """A request is scored against the floor; it never moves one."""
    assert floors(runs["D06"]) == default_floors(library)


# ---------------------------------------------------------------------------
# Snapshots
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("deal_id", sorted(DEAL_FILES))
def test_markdown_snapshot(runs, deal_id):
    _snapshot(
        EXPECTED_DIR / f"{DEAL_FILES[deal_id]}.md", normalised_markdown(runs[deal_id])
    )


@pytest.mark.parametrize("deal_id", sorted(DEAL_FILES))
def test_json_snapshot(runs, deal_id):
    _snapshot(
        EXPECTED_DIR / f"{DEAL_FILES[deal_id]}.json", normalised_json(runs[deal_id])
    )


@pytest.mark.parametrize("deal_id", sorted(DEAL_FILES))
def test_snapshot_placeholders_are_the_only_normalisation(runs, deal_id):
    """The snapshot differs from a live run in exactly two values.

    If a third non-deterministic field ever creeps into `RunResult`, the
    snapshots start flapping; this test is the early warning.
    """
    result = runs[deal_id]
    live = json.loads(result.model_dump_json())
    snapshot = json.loads(normalised_json(result))
    differing = {k for k in live if live[k] != snapshot[k]}
    assert differing == {"run_id", "timestamp"}


# ---------------------------------------------------------------------------
# Determinism (build_plan.md §0 rule 6)
# ---------------------------------------------------------------------------


def test_D02_run_twice_is_byte_identical(library):
    """Same library plus same intake gives the same result, twice running."""
    intake = load_intake(DEALS_DIR / f"{DEAL_FILES['D02']}.yaml")
    first = evaluate(library, intake)
    second = evaluate(library, intake)
    assert normalised_json(first) == normalised_json(second)
    assert normalised_markdown(first) == normalised_markdown(second)
    # The run ids differ only because the timestamp does; everything the
    # markup shows is identical.
    assert first.intake_hash == second.intake_hash
    assert first.library_hash == second.library_hash


def test_reloading_the_deal_file_gives_the_same_intake_hash(library):
    """Loading the YAML twice hashes the same, so the snapshot is stable on disk."""
    path = DEALS_DIR / f"{DEAL_FILES['D02']}.yaml"
    a = evaluate(library, load_intake(path))
    b = evaluate(library, load_intake(path))
    assert a.intake_hash == b.intake_hash
