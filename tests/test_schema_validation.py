"""WP1 acceptance tests: the frozen data contract.

Covers:

* the real stub library loads and validates;
* the three valid fixtures (clause, rule, intake) load;
* each of ten deliberate errors is rejected with a message that names the
  problem clearly enough to fix it;
* the derived fields on the D99 intake;
* the tier ordering helper (tighter == closer to preferred).

Every fixture is synthetic.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

from sbl.loader import (
    LibraryError,
    compute_library_hash,
    intake_field_paths,
    load_intake,
    load_library,
)
from sbl.models import (
    Clause,
    Intake,
    Rule,
    Status,
    Tier,
    is_tighter,
    tier_rank,
    tighter,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def stage_library(tmp_path: Path) -> Path:
    """Copy the real playbook into a temp root so fixtures can be dropped in."""
    root = tmp_path / "repo"
    root.mkdir()
    shutil.copytree(REPO_ROOT / "playbook", root / "playbook")
    return root


def add_clause(root: Path, fixture: str, filename: str | None = None) -> None:
    name = filename or f"99_{Path(fixture).stem}.yaml"
    shutil.copyfile(FIXTURES / fixture, root / "playbook" / "clauses" / name)


def set_rules(root: Path, fixture: str) -> None:
    shutil.copyfile(FIXTURES / fixture, root / "playbook" / "rules" / "rules.yaml")


def errors_of(exc_info: pytest.ExceptionInfo[LibraryError]) -> str:
    return "\n".join(exc_info.value.errors)


# ---------------------------------------------------------------------------
# The real library
# ---------------------------------------------------------------------------


def test_stub_library_loads() -> None:
    library = load_library(REPO_ROOT)
    assert len(library.clauses) == 24
    assert len(library.flags) == 10
    assert len(library.jurisdictions) == 3
    # Relaxed after WP1: WP5 writes the rule set and WP3 promotes clauses from
    # stub to draft, so this test asserts the shape of the library, not a
    # snapshot of how far the content work has got.
    assert len(library.rules) >= 15
    assert all(
        c.status in (Status.stub, Status.draft) for c in library.clauses.values()
    )


def test_library_hash_is_stable_and_content_sensitive(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    first = compute_library_hash(root / "playbook")
    assert first == compute_library_hash(root / "playbook")
    assert first == load_library(REPO_ROOT).library_hash
    target = root / "playbook" / "clauses" / "01_facility_type.yaml"
    target.write_text(
        target.read_text(encoding="utf-8") + "\n# touched\n", encoding="utf-8"
    )
    assert compute_library_hash(root / "playbook") != first


def test_status_counts_shape() -> None:
    counts = load_library(REPO_ROOT).status_counts()
    assert set(counts) == {"clauses", "rules", "flags", "jurisdictions"}
    assert sum(counts["clauses"].values()) == 24
    assert counts["clauses"]["reviewed"] == 0
    # No agent may set 'reviewed'; only a named human reviewer.
    assert all(kind["reviewed"] == 0 for kind in counts.values())


# ---------------------------------------------------------------------------
# Valid fixtures
# ---------------------------------------------------------------------------


def test_valid_draft_clause_loads_in_library(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    add_clause(root, "valid_clause_draft.yaml")
    library = load_library(root)
    clause = library.clauses["fixture_margin_call_notice"]
    assert clause.status is Status.draft
    assert clause.default_floor is Tier.fallback
    assert clause.positions is not None
    assert clause.positions.preferred.text.startswith("[DRAFT PLACEHOLDER]")
    # The unacceptable tier carries no conditions and no approver: nobody may agree it.
    assert not hasattr(clause.positions.unacceptable, "conditions")
    assert not hasattr(clause.positions.unacceptable, "approval")


def test_valid_rule_loads_in_library(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    set_rules(root, "valid_rule.yaml")
    library = load_library(root)
    assert [r.id for r in library.rules] == ["R07_pdmr_pledged_issuer"]
    rule = library.rules[0]
    assert rule.status is Status.draft
    assert {a.action.value for a in rule.then} == {
        "flag",
        "escalate",
        "set_floor",
        "require_rep",
        "require_cp",
        "note",
    }


def test_valid_intake_loads() -> None:
    intake = load_intake(FIXTURES / "valid_intake_D99.yaml")
    assert intake.deal_id == "D99"
    assert intake.borrower.type.value == "trust"
    assert intake.pledgor.is_pdmr_of_pledged_issuer is True


# ---------------------------------------------------------------------------
# Derived fields
# ---------------------------------------------------------------------------


def test_d99_derived_fields() -> None:
    d = load_intake(FIXTURES / "valid_intake_D99.yaml").derived
    assert d.max_single_name_pct == 70.0
    assert d.has_real_estate is False
    # GBP facility against [GBP, USD] collateral: at least one currency differs.
    assert d.currency_mismatch is True
    assert d.third_party_security is False
    assert d.any_natural_person_pledgor is False


def test_derived_third_party_natural_person_pledgor() -> None:
    data = yaml.safe_load((FIXTURES / "valid_intake_D99.yaml").read_text("utf-8"))
    data["pledgor"] = {
        "same_as_borrower": False,
        "type": "individual",
        "domicile": "LU",
        "natural_person": True,
        "is_pdmr_of_pledged_issuer": False,
    }
    d = Intake.model_validate(data).derived
    assert d.third_party_security is True
    assert d.any_natural_person_pledgor is True


def test_derived_real_estate_and_no_single_name() -> None:
    data = yaml.safe_load((FIXTURES / "valid_intake_D99.yaml").read_text("utf-8"))
    data["collateral"]["composition"] = [
        {"asset_class": "real_estate", "pct": 30, "single_name_max_pct": None},
        {"asset_class": "cash", "pct": 70, "single_name_max_pct": None},
    ]
    data["collateral"]["currencies"] = ["GBP"]
    d = Intake.model_validate(data).derived
    assert d.has_real_estate is True
    assert d.max_single_name_pct == 0.0
    assert d.currency_mismatch is False


def test_derived_is_addressable_by_rules() -> None:
    paths = intake_field_paths()
    for name in (
        "derived.max_single_name_pct",
        "derived.has_real_estate",
        "derived.currency_mismatch",
        "derived.third_party_security",
        "derived.any_natural_person_pledgor",
    ):
        assert name in paths


# ---------------------------------------------------------------------------
# The ten deliberate errors
# ---------------------------------------------------------------------------


def test_01_unknown_field_path_in_rule_condition(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    set_rules(root, "invalid_rule_unknown_field.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "unknown intake field" in msg
    assert "borrower.is_consumer" in msg
    assert "RX01_unknown_field" in msg
    assert "rules.yaml" in msg


def test_02_unknown_clause_id_in_action(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    set_rules(root, "invalid_rule_unknown_clause.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "unknown clause id" in msg
    assert "margin_call_cure_period" in msg
    assert "RX02_unknown_clause" in msg


def test_03_unknown_flag_id(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    set_rules(root, "invalid_rule_unknown_flag.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "unknown flag id" in msg
    assert "basel_iv_awareness" in msg


def test_04_composition_over_100_rejected() -> None:
    with pytest.raises(LibraryError) as exc:
        load_intake(FIXTURES / "invalid_intake_composition_over_100.yaml")
    msg = errors_of(exc)
    assert "exceeds 100" in msg


def test_05_missing_status_rejected(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    add_clause(root, "invalid_clause_missing_status.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "status" in msg
    assert "required" in msg.lower() or "missing" in msg.lower()


def test_06_reviewed_with_null_reviewer_rejected(tmp_path: Path) -> None:
    """The schema allows the value 'reviewed'; an unattributable review is rejected."""
    root = stage_library(tmp_path)
    add_clause(root, "invalid_clause_reviewed_no_reviewer.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "reviewed_by" in msg


def test_06b_reviewed_with_a_named_reviewer_is_accepted() -> None:
    data = yaml.safe_load(
        (FIXTURES / "invalid_clause_reviewed_no_reviewer.yaml").read_text("utf-8")
    )
    data["reviewed_by"] = "Reviewer Name"
    clause = Clause.model_validate(data)
    assert clause.status is Status.reviewed


def test_07_invalid_tier_name_rejected(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    add_clause(root, "invalid_clause_bad_tier.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "default_floor" in msg
    assert "last_resort" in msg or "preferred" in msg


def test_08_invalid_op_rejected(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    set_rules(root, "invalid_rule_bad_op.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "RX08_bad_op" in msg
    assert "op" in msg


def test_09_dangling_depends_on_rejected(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    add_clause(root, "invalid_clause_dangling_depends_on.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    msg = errors_of(exc)
    assert "depends_on unknown clause id" in msg
    assert "collateral_haircut_schedule" in msg


def test_10_unknown_top_level_key_in_intake_rejected() -> None:
    with pytest.raises(LibraryError) as exc:
        load_intake(FIXTURES / "invalid_intake_unknown_key.yaml")
    msg = errors_of(exc)
    assert "borrower_is_consumer" in msg
    assert "not permitted" in msg or "extra" in msg.lower()


# ---------------------------------------------------------------------------
# Error quality: file and line
# ---------------------------------------------------------------------------


def test_rule_errors_name_file_and_line(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    set_rules(root, "invalid_rule_unknown_field.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    assert any("rules/rules.yaml:" in e for e in exc.value.errors)


def test_clause_errors_name_file(tmp_path: Path) -> None:
    root = stage_library(tmp_path)
    add_clause(root, "invalid_clause_dangling_depends_on.yaml")
    with pytest.raises(LibraryError) as exc:
        load_library(root)
    assert any("playbook/clauses/" in e for e in exc.value.errors)


# ---------------------------------------------------------------------------
# Other contract invariants
# ---------------------------------------------------------------------------


def test_extra_keys_forbidden_everywhere() -> None:
    with pytest.raises(Exception):
        Clause.model_validate(
            {
                "id": "x",
                "title": "t",
                "category": "collateral",
                "lender_objective": "o",
                "status": "stub",
                "unexpected": 1,
            }
        )


def test_draft_clause_must_be_complete() -> None:
    with pytest.raises(Exception) as exc:
        Clause.model_validate(
            {
                "id": "x",
                "title": "t",
                "category": "collateral",
                "lender_objective": "o",
                "status": "draft",
            }
        )
    assert "missing required field" in str(exc.value)


def test_stub_clause_needs_only_four_fields() -> None:
    clause = Clause.model_validate(
        {
            "id": "x",
            "title": "t",
            "category": "collateral",
            "lender_objective": "o",
            "status": "stub",
        }
    )
    assert clause.positions is None


def test_tier_ordering_tighter_is_closer_to_preferred() -> None:
    assert tier_rank(Tier.preferred) == 0
    assert tier_rank(Tier.unacceptable) == 3
    assert is_tighter(Tier.preferred, Tier.acceptable)
    assert is_tighter(Tier.acceptable, Tier.fallback)
    assert is_tighter(Tier.fallback, Tier.unacceptable)
    assert not is_tighter(Tier.fallback, Tier.acceptable)
    assert tighter(Tier.fallback, Tier.acceptable) is Tier.acceptable
    assert tighter(Tier.preferred, Tier.unacceptable) is Tier.preferred


def test_counterparty_request_needs_tier_or_text() -> None:
    data = yaml.safe_load((FIXTURES / "valid_intake_D99.yaml").read_text("utf-8"))
    data["counterparty_requests"] = {"margin_maintenance_cure": {"tier": "fallback"}}
    intake = Intake.model_validate(data)
    assert intake.counterparty_requests["margin_maintenance_cure"].tier is Tier.fallback
    data["counterparty_requests"] = {"margin_maintenance_cure": {}}
    with pytest.raises(Exception):
        Intake.model_validate(data)


def test_rule_condition_tree_nests() -> None:
    rule = Rule.model_validate(
        {
            "id": "RX_nested",
            "title": "Nested condition",
            "when": {
                "all": [
                    {"any": [{"field": "guarantor_present", "op": "eq", "value": True}]},
                    {"not": {"field": "derived.has_real_estate", "op": "eq", "value": True}},
                ]
            },
            "then": [{"action": "note", "clause": "facility_type", "text": "n"}],
            "rationale": "r",
            "status": "draft",
        }
    )
    assert rule.when.all[1].not_.field == "derived.has_real_estate"
