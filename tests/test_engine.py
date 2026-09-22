"""WP5 acceptance tests: the rules engine (build_plan.md §6, WP5).

Covers:

* every rule in ``playbook/rules/rules.yaml`` fires on an intake built for it
  and does not fire on the negation of that intake;
* tighten-only semantics, and the order-independence property (feeding the
  rules in reverse gives a byte-identical result, because the engine sorts);
* an unknown flag id is rejected at load, not at run;
* the built-in R16 produces each of its three outcomes, plus the free-text
  case;
* exit code 2 on any escalation, 0 otherwise;
* determinism: two runs differ only in ``run_id`` and ``timestamp``;
* the condition grammar, including null handling and list projection.

Every intake in this file is synthetic.
"""

from __future__ import annotations

import copy
import shutil
from pathlib import Path
from typing import Any

import pytest
import yaml

from sbl.engine import (
    NO_CHANGE_SUFFIX,
    R16_ID,
    EngineError,
    compute_run_id,
    evaluate,
    evaluate_condition,
    resolve_field,
    sorted_rules,
)
from sbl.loader import LibraryError, load_intake, load_library
from sbl.models import (
    AllCondition,
    AnyCondition,
    Intake,
    LeafCondition,
    NotCondition,
    RequestOutcome,
    RunResult,
    Status,
    Tier,
    tier_rank,
)

from test_intake import BASE, deep_merge  # noqa: E402 - the quiet synthetic intake

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
DEMO_INTAKE = FIXTURES / "wp5_demo_intake.yaml"


@pytest.fixture(scope="module")
def library():
    return load_library(REPO_ROOT)


def make_intake(**patch: Any) -> Intake:
    return Intake.model_validate(deep_merge(BASE, patch))


def fired_rule_ids(result: RunResult) -> set[str]:
    """Every rule id that left a trace anywhere in the run."""
    fired: set[str] = set()
    for clause in result.clauses:
        for entry in clause.rules_applied:
            fired.add(entry.removesuffix(NO_CHANGE_SUFFIX))
    fired.update(flag.rule_id for flag in result.flags)
    fired.update(escalation.rule_id for escalation in result.escalations)
    return fired


def clause_of(result: RunResult, clause_id: str):
    return next(c for c in result.clauses if c.id == clause_id)


# ---------------------------------------------------------------------------
# One positive and one negative intake per rule
# ---------------------------------------------------------------------------

#: rule id -> (patch that makes it fire, patch that makes it not fire).
#: BASE is a UK individual with a high-net-worth declaration, a diversified
#: GBP portfolio at the lender's own custody under English law, uncommitted and
#: for a general purpose, so it fires R03b and R04 and nothing else.
RULE_CASES: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {
    "R01_trust_borrower": (
        {"borrower": {"type": "trust", "natural_person": False, "declared_high_net_worth": None}},
        {"borrower": {"type": "corporate", "natural_person": False, "declared_high_net_worth": None}},
    ),
    "R02_corporate_or_partnership": (
        {"borrower": {"type": "partnership", "natural_person": False, "declared_high_net_worth": None}},
        {"borrower": {"type": "trust", "natural_person": False, "declared_high_net_worth": None}},
    ),
    "R03a_natural_person_borrower_no_declaration": (
        {"borrower": {"declared_high_net_worth": None, "business_purpose_declared": None}},
        {"borrower": {"declared_high_net_worth": True}},
    ),
    "R03b_natural_person_borrower_declared": (
        {"borrower": {"declared_high_net_worth": False, "business_purpose_declared": True}},
        {"borrower": {"declared_high_net_worth": None, "business_purpose_declared": None}},
    ),
    "R04_natural_person_pledgor_england": (
        {"collateral": {"governing_law": "england_wales"}},
        {"collateral": {"governing_law": "luxembourg"}},
    ),
    "R05_third_party_security": (
        {
            "pledgor": {
                "same_as_borrower": False,
                "type": "individual",
                "domicile": "LU",
                "natural_person": True,
            }
        },
        {"pledgor": {"same_as_borrower": True}},
    ),
    "R05b_third_party_corporate_pledgor": (
        {
            "pledgor": {
                "same_as_borrower": False,
                "type": "corporate",
                "domicile": "LU",
                "natural_person": False,
            }
        },
        {
            "pledgor": {
                "same_as_borrower": False,
                "type": "individual",
                "domicile": "LU",
                "natural_person": True,
            }
        },
    ),
    "R06_concentration": (
        {
            "collateral": {
                "composition": [
                    {"asset_class": "listed_equity", "pct": 90, "single_name_max_pct": 40}
                ]
            }
        },
        {
            "collateral": {
                "composition": [
                    {"asset_class": "listed_equity", "pct": 90, "single_name_max_pct": 25}
                ]
            }
        },
    ),
    "R06b_concentration_severe": (
        {
            "collateral": {
                "composition": [
                    {"asset_class": "listed_equity", "pct": 90, "single_name_max_pct": 70}
                ]
            }
        },
        {
            "collateral": {
                "composition": [
                    {"asset_class": "listed_equity", "pct": 90, "single_name_max_pct": 50}
                ]
            }
        },
    ),
    "R07_pdmr_pledged_issuer": (
        {"pledgor": {"is_pdmr_of_pledged_issuer": True}},
        {"pledgor": {"is_pdmr_of_pledged_issuer": False}},
    ),
    "R08_restricted_securities": (
        {
            "collateral": {
                "composition": [
                    {
                        "asset_class": "listed_equity",
                        "pct": 90,
                        "single_name_max_pct": 10,
                        "issuer_restricted": True,
                    }
                ]
            }
        },
        {},
    ),
    "R09_real_estate": (
        {
            "collateral": {
                "composition": [
                    {"asset_class": "real_estate", "pct": 30},
                    {"asset_class": "cash", "pct": 70},
                ]
            }
        },
        {
            "collateral": {
                "composition": [
                    {"asset_class": "real_estate", "pct": 0},
                    {"asset_class": "cash", "pct": 100},
                ]
            }
        },
    ),
    "R10_purpose_acquire_securities": (
        {"facility": {"purpose": "acquire_securities"}},
        {"facility": {"purpose": "general"}},
    ),
    "R11_committed_term": (
        {"facility": {"type": "committed_term"}},
        {"facility": {"type": "uncommitted_demand"}},
    ),
    "R12_third_party_custodian": (
        {"collateral": {"lender_is_custodian": False}},
        {"collateral": {"lender_is_custodian": True}},
    ),
    "R13_currency_mismatch": (
        {"collateral": {"currencies": ["GBP", "USD"]}},
        {"collateral": {"currencies": ["GBP"]}},
    ),
    "R14_swiss_booking": (
        {"collateral": {"custodian_location": "CH"}},
        {"collateral": {"custodian_location": "GB", "governing_law": "england_wales"}},
    ),
    "R15_illiquid_collateral": (
        {
            "collateral": {
                "composition": [
                    {"asset_class": "structured_product", "pct": 30},
                    {"asset_class": "cash", "pct": 70},
                ]
            }
        },
        {
            "collateral": {
                "composition": [
                    {"asset_class": "fund_daily", "pct": 30},
                    {"asset_class": "cash", "pct": 70},
                ]
            }
        },
    ),
}


def test_every_yaml_rule_has_a_test_case(library) -> None:
    """If a rule is added to rules.yaml, it must be exercised here."""
    assert {r.id for r in library.rules} == set(RULE_CASES)


@pytest.mark.parametrize("rule_id", sorted(RULE_CASES))
def test_rule_fires_on_its_trigger(library, rule_id: str) -> None:
    positive, _ = RULE_CASES[rule_id]
    result = evaluate(library, make_intake(**positive))
    assert rule_id in fired_rule_ids(result)


@pytest.mark.parametrize("rule_id", sorted(RULE_CASES))
def test_rule_does_not_fire_on_its_negation(library, rule_id: str) -> None:
    _, negative = RULE_CASES[rule_id]
    result = evaluate(library, make_intake(**negative))
    assert rule_id not in fired_rule_ids(result)


def test_every_rule_is_draft_and_carries_a_rationale_and_a_source(library) -> None:
    assert len(library.rules) >= 15
    for rule in library.rules:
        assert rule.status is Status.draft, rule.id
        assert len(rule.rationale.split()) >= 20, f"{rule.id}: rationale too thin"
        assert rule.sources, f"{rule.id}: no source"
        for source in rule.sources:
            # Relaxed in WP5b, which reconciled these sources against the
            # research files. A source is now honest in one of exactly two
            # ways: it was opened (verified, with the URL it was opened at),
            # or it was not (unverified, and marked [VERIFY] in the ref or the
            # note so the statement resting on it is visibly unconfirmed).
            if source.verified:
                assert source.url, f"{rule.id}: verified source without a url"
                assert not source.ref.startswith("[VERIFY]"), rule.id
            else:
                marked = source.ref.startswith("[VERIFY]") or (
                    source.note is not None and "[VERIFY]" in source.note
                )
                assert marked, (
                    f"{rule.id}: unverified source must carry [VERIFY] in its "
                    f"ref or its note: {source.ref!r}"
                )


def test_r04_flag_message_is_verify_prefixed(library) -> None:
    """build_plan.md §4: R04's fcar_safe_harbour_uncertain message is [VERIFY]."""
    result = evaluate(library, make_intake())
    message = next(f.message for f in result.flags if f.id == "fcar_safe_harbour_uncertain")
    assert message.startswith("[VERIFY]")


def test_r09_note_says_real_estate_is_out_of_scope(library) -> None:
    positive, _ = RULE_CASES["R09_real_estate"]
    result = evaluate(library, make_intake(**positive))
    notes = clause_of(result, "eligible_collateral_lending_values").notes
    assert any("out of scope for this playbook" in n for n in notes)
    assert any(e.rule_id == "R09_real_estate" for e in result.escalations)


def test_r03_severity_splits_on_the_declaration(library) -> None:
    undeclared = evaluate(
        library,
        make_intake(
            borrower={"declared_high_net_worth": None, "business_purpose_declared": None}
        ),
    )
    declared = evaluate(library, make_intake())
    assert [f.severity.value for f in undeclared.flags if f.id == "consumer_credit"] == [
        "high"
    ]
    assert [f.severity.value for f in declared.flags if f.id == "consumer_credit"] == [
        "medium"
    ]
    assert undeclared.exit_code == 2  # the undeclared case escalates
    assert declared.exit_code == 0


# ---------------------------------------------------------------------------
# Tighten-only and order independence
# ---------------------------------------------------------------------------


def test_rules_only_tighten_floors_and_openings(library) -> None:
    positive, _ = RULE_CASES["R06b_concentration_severe"]
    result = evaluate(library, make_intake(**positive))
    for clause in result.clauses:
        entry = library.clauses[clause.id]
        default_floor = entry.default_floor or Tier.fallback
        assert tier_rank(clause.floor) <= tier_rank(default_floor), clause.id
        assert tier_rank(clause.opening) <= tier_rank(clause.floor), clause.id


def test_reversed_rule_order_gives_an_identical_result(library) -> None:
    """The engine sorts by (priority, id), so file order cannot change a run."""
    intake = load_intake(DEMO_INTAKE)
    forward = evaluate(library, intake, timestamp="2026-01-01T00:00:00+00:00")

    shuffled = copy.copy(library)
    shuffled.rules = list(reversed(library.rules))
    backward = evaluate(shuffled, intake, timestamp="2026-01-01T00:00:00+00:00")

    assert backward.model_dump_json(indent=2) == forward.model_dump_json(indent=2)
    for a, b in zip(forward.clauses, backward.clauses):
        assert (a.floor, a.opening, a.notes, a.cps, a.reps, a.rules_applied) == (
            b.floor,
            b.opening,
            b.notes,
            b.cps,
            b.reps,
            b.rules_applied,
        )


def test_sorted_rules_is_priority_then_id(library) -> None:
    ordered = sorted_rules(library.rules)
    keys = [(r.priority, r.id) for r in ordered]
    assert keys == sorted(keys)


def test_a_later_looser_set_floor_cannot_loosen(library) -> None:
    """R06 raises concentration_limits to acceptable; nothing may put it back."""
    positive, _ = RULE_CASES["R06_concentration"]
    result = evaluate(library, make_intake(**positive))
    assert clause_of(result, "concentration_limits").floor is Tier.acceptable


def test_no_change_touches_are_logged_as_such(library) -> None:
    """R06b sets the margin-call opening to preferred, which it already is."""
    positive, _ = RULE_CASES["R06b_concentration_severe"]
    result = evaluate(library, make_intake(**positive))
    applied = clause_of(result, "margin_maintenance_cure").rules_applied
    assert "R06b_concentration_severe" + NO_CHANGE_SUFFIX in applied
    assert "R06_concentration" in applied  # this one did change the floor


def test_every_appended_string_carries_its_rule_id(library) -> None:
    result = evaluate(library, load_intake(DEMO_INTAKE))
    known = {r.id for r in library.rules} | {R16_ID}
    seen = 0
    for clause in result.clauses:
        for line in clause.cps + clause.reps + clause.notes:
            assert line.startswith("["), line
            rule_id = line[1 : line.index("] ")]
            assert rule_id in known, line
            seen += 1
    assert seen > 0


# ---------------------------------------------------------------------------
# Load-time rejection of an unknown flag id
# ---------------------------------------------------------------------------


def test_unknown_flag_id_is_rejected_at_load(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    shutil.copytree(REPO_ROOT / "playbook", root / "playbook")
    rules_path = root / "playbook" / "rules" / "rules.yaml"
    rules = yaml.safe_load(rules_path.read_text(encoding="utf-8"))
    rules[0]["then"].append(
        {
            "action": "flag",
            "flag": "basel_iv_awareness",
            "severity": "low",
            "message": "Synthetic test flag that is not defined.",
        }
    )
    rules_path.write_text(yaml.safe_dump(rules), encoding="utf-8")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    joined = "\n".join(exc.value.errors)
    assert "unknown flag id" in joined
    assert "basel_iv_awareness" in joined


# ---------------------------------------------------------------------------
# R16: counterparty requests
# ---------------------------------------------------------------------------


def test_r16_accepts_a_request_at_or_inside_the_floor(library) -> None:
    result = evaluate(
        library,
        make_intake(counterparty_requests={"margin_maintenance_cure": {"tier": "acceptable"}}),
    )
    outcome = result.counterparty_request_outcomes[0]
    assert outcome.clause == "margin_maintenance_cure"
    assert outcome.outcome is RequestOutcome.accepted_within_floor
    assert outcome.floor is Tier.fallback
    assert not [e for e in result.escalations if e.rule_id == R16_ID]
    notes = clause_of(result, "margin_maintenance_cure").notes
    assert any("accepted within floor" in n and "approver:" in n for n in notes)
    assert R16_ID in clause_of(result, "margin_maintenance_cure").rules_applied


def test_r16_escalates_a_request_below_the_floor(library) -> None:
    """R06 tightens concentration_limits to acceptable; fallback is then below it."""
    positive, _ = RULE_CASES["R06_concentration"]
    intake = make_intake(
        counterparty_requests={"concentration_limits": {"tier": "fallback"}}, **positive
    )
    result = evaluate(library, intake)
    outcome = result.counterparty_request_outcomes[0]
    assert outcome.outcome is RequestOutcome.below_floor_escalated
    assert outcome.floor is Tier.acceptable
    escalation = next(e for e in result.escalations if e.rule_id == R16_ID)
    assert escalation.clause == "concentration_limits"
    assert escalation.to == "senior lawyer"
    assert "looser than the floor" in escalation.reason
    assert result.exit_code == 2


def test_r16_escalates_a_request_at_the_unacceptable_tier(library) -> None:
    result = evaluate(
        library,
        make_intake(
            counterparty_requests={"enforcement_liquidation": {"tier": "unacceptable"}}
        ),
    )
    outcome = result.counterparty_request_outcomes[0]
    assert outcome.outcome is RequestOutcome.unacceptable_escalated
    escalation = next(e for e in result.escalations if e.rule_id == R16_ID)
    assert escalation.to == "senior lawyer"
    assert "walk-away" in escalation.reason
    assert result.exit_code == 2


def test_r16_free_text_request_is_escalated_for_manual_classification(library) -> None:
    result = evaluate(
        library,
        make_intake(
            counterparty_requests={
                "governing_law_jurisdiction": {"text": "Wants its own home courts."}
            }
        ),
    )
    outcome = result.counterparty_request_outcomes[0]
    assert outcome.requested_tier is None
    assert outcome.requested_text == "Wants its own home courts."
    assert outcome.outcome is RequestOutcome.below_floor_escalated
    escalation = next(e for e in result.escalations if e.rule_id == R16_ID)
    assert escalation.to == "deal lawyer"
    assert escalation.reason == (
        "unmapped counterparty request text requires manual classification"
    )
    notes = clause_of(result, "governing_law_jurisdiction").notes
    assert any("Wants its own home courts." in n for n in notes)


def test_r16_outcomes_are_in_clause_id_order(library) -> None:
    result = evaluate(library, load_intake(DEMO_INTAKE))
    clauses = [o.clause for o in result.counterparty_request_outcomes]
    assert clauses == sorted(clauses)
    assert {o.outcome for o in result.counterparty_request_outcomes} == {
        RequestOutcome.accepted_within_floor,
        RequestOutcome.below_floor_escalated,
        RequestOutcome.unacceptable_escalated,
    }


def test_r16_rejects_a_request_against_an_unknown_clause(library) -> None:
    data = deep_merge(BASE, {})
    data["counterparty_requests"] = {"margin_call_cure_period": {"tier": "fallback"}}
    with pytest.raises(EngineError) as exc:
        evaluate(library, Intake.model_validate(data))
    assert "unknown clause id" in str(exc.value)


# ---------------------------------------------------------------------------
# Exit codes, determinism, run shape
# ---------------------------------------------------------------------------


def test_quiet_intake_gives_exit_code_zero(library) -> None:
    result = evaluate(library, make_intake())
    assert result.escalations == []
    assert result.exit_code == 0


def test_any_escalation_gives_exit_code_two(library) -> None:
    positive, _ = RULE_CASES["R09_real_estate"]
    result = evaluate(library, make_intake(**positive))
    assert result.escalations
    assert result.exit_code == 2


def test_two_runs_differ_only_in_run_id_and_timestamp(library) -> None:
    intake = load_intake(DEMO_INTAKE)
    first = evaluate(library, intake).model_dump(mode="json")
    second = evaluate(library, intake).model_dump(mode="json")
    for key in ("run_id", "timestamp"):
        first.pop(key)
        second.pop(key)
    assert first == second


def test_run_id_is_derived_from_the_three_hashes(library) -> None:
    intake = load_intake(DEMO_INTAKE)
    result = evaluate(library, intake, timestamp="2026-01-01T00:00:00+00:00")
    assert result.run_id == compute_run_id(
        result.library_hash, result.intake_hash, result.timestamp
    )
    assert len(result.run_id) == 12
    assert result.library_hash == library.library_hash


def test_run_result_carries_everything_the_renderer_needs(library) -> None:
    result = evaluate(library, load_intake(DEMO_INTAKE))
    assert result.deal_id == "T99"
    assert result.governing_law.value == "switzerland"
    assert result.jurisdiction is not None
    assert result.jurisdiction.id == "switzerland"
    assert sum(result.status_summary.values()) == len(result.clauses)
    assert set(result.status_summary) == {"reviewed", "draft", "stub"}
    for clause in result.clauses:
        entry = library.clauses[clause.id]
        assert clause.title == entry.title
        assert clause.category is entry.category
        assert clause.status is entry.status
        assert clause.not_automated == entry.not_automated
        assert clause.escalation_triggers == entry.escalation_triggers
        if entry.positions is None:
            assert clause.ladder == []
        else:
            assert [r.tier.value for r in clause.ladder] == [
                "preferred",
                "acceptable",
                "fallback",
                "unacceptable",
            ]
            assert clause.ladder[3].conditions == []
            assert clause.ladder[3].approval is None
            assert clause.opening_text is not None


def test_governing_law_other_gives_no_jurisdiction_overlay(library) -> None:
    result = evaluate(library, make_intake(collateral={"governing_law": "other"}))
    assert result.jurisdiction is None
    assert all(c.jurisdiction_note is None for c in result.clauses)


def test_not_automated_is_deduplicated_and_sorted(library) -> None:
    result = evaluate(library, load_intake(DEMO_INTAKE))
    assert result.not_automated == sorted(set(result.not_automated))
    touched = {
        item
        for clause in result.clauses
        if clause.rules_applied
        for item in clause.not_automated
    }
    assert touched <= set(result.not_automated)


# ---------------------------------------------------------------------------
# Condition grammar
# ---------------------------------------------------------------------------


def test_dotted_paths_resolve_including_derived_and_projections() -> None:
    intake = load_intake(DEMO_INTAKE)
    assert resolve_field(intake, "borrower.type").value == "trust"
    assert resolve_field(intake, "derived.max_single_name_pct") == 55.0
    assert resolve_field(intake, "facility.amount") == 5000000
    projected = resolve_field(intake, "collateral.composition.asset_class")
    assert [a.value for a in projected] == ["listed_equity", "fund_gated", "cash"]


def test_resolving_an_unknown_path_is_an_engine_error() -> None:
    intake = load_intake(DEMO_INTAKE)
    with pytest.raises(EngineError) as exc:
        resolve_field(intake, "borrower.is_consumer")
    assert "borrower.is_consumer" in str(exc.value)


@pytest.mark.parametrize(
    "leaf,expected",
    [
        ({"field": "borrower.type", "op": "eq", "value": "individual"}, True),
        ({"field": "borrower.type", "op": "eq", "value": "trust"}, False),
        ({"field": "borrower.type", "op": "neq", "value": "trust"}, True),
        ({"field": "borrower.natural_person", "op": "eq", "value": True}, True),
        ({"field": "borrower.natural_person", "op": "eq", "value": 1}, False),
        ({"field": "facility.amount", "op": "gt", "value": 10}, True),
        ({"field": "facility.amount", "op": "lte", "value": 10}, False),
        ({"field": "collateral.currencies", "op": "contains", "value": "GBP"}, True),
        ({"field": "collateral.currencies", "op": "contains", "value": "CHF"}, False),
        ({"field": "borrower.domicile", "op": "contains", "value": "G"}, True),
        (
            {"field": "collateral.composition.asset_class", "op": "contains", "value": "cash"},
            True,
        ),
        (
            {"field": "collateral.composition.asset_class", "op": "contains", "value": "unlisted"},
            False,
        ),
        ({"field": "borrower.type", "op": "in", "value": ["individual", "trust"]}, True),
        ({"field": "borrower.type", "op": "not_in", "value": ["individual"]}, False),
        ({"field": "borrower.business_purpose_declared", "op": "is_null", "value": None}, True),
        ({"field": "borrower.declared_high_net_worth", "op": "is_null", "value": None}, False),
    ],
)
def test_leaf_operators(leaf: dict[str, Any], expected: bool) -> None:
    condition = LeafCondition.model_validate(leaf)
    assert evaluate_condition(condition, make_intake()) is expected


@pytest.mark.parametrize("op", ["eq", "neq", "gt", "gte", "lt", "lte", "contains"])
def test_every_comparison_on_a_null_field_is_false(op: str) -> None:
    """A null must never read as "the rule fires", and never as an error."""
    leaf = LeafCondition.model_validate(
        {"field": "borrower.business_purpose_declared", "op": op, "value": True}
    )
    assert evaluate_condition(leaf, make_intake()) is False


@pytest.mark.parametrize("op", ["in", "not_in"])
def test_membership_on_a_null_field_is_false(op: str) -> None:
    leaf = LeafCondition.model_validate(
        {"field": "borrower.business_purpose_declared", "op": op, "value": [True, False]}
    )
    assert evaluate_condition(leaf, make_intake()) is False


def test_all_any_and_not_nest() -> None:
    intake = make_intake()
    true_leaf = {"field": "borrower.natural_person", "op": "eq", "value": True}
    false_leaf = {"field": "borrower.type", "op": "eq", "value": "trust"}

    assert evaluate_condition(
        AllCondition.model_validate({"all": [true_leaf, true_leaf]}), intake
    )
    assert not evaluate_condition(
        AllCondition.model_validate({"all": [true_leaf, false_leaf]}), intake
    )
    assert evaluate_condition(
        AnyCondition.model_validate({"any": [true_leaf, false_leaf]}), intake
    )
    assert not evaluate_condition(
        NotCondition.model_validate({"not": true_leaf}), intake
    )
    assert evaluate_condition(
        NotCondition.model_validate({"not": {"any": [false_leaf]}}), intake
    )
