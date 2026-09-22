"""WP4 acceptance tests: the intake contract (build_plan.md §2.3).

Covers every closed list, every validator and every derived field on the
``Intake`` model, including the three WP5 changes to ``Derived``:

* ``any_issuer_restricted`` (new),
* ``has_illiquid_collateral`` (new),
* ``has_real_estate`` now requires ``pct > 0``.

Every fixture here is synthetic. No real person, entity or portfolio appears.
"""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import pytest
import yaml
from pydantic import ValidationError

from sbl.cli import echo_intake, expand_deal_paths
from sbl.loader import LibraryError, intake_field_paths, load_intake
from sbl.models import Intake, Tier

FIXTURES = Path(__file__).resolve().parent / "fixtures"
DEMO_INTAKE = FIXTURES / "wp5_demo_intake.yaml"


# ---------------------------------------------------------------------------
# A minimal, valid, quiet intake to mutate
# ---------------------------------------------------------------------------

BASE: dict[str, Any] = {
    "deal_id": "T01",
    "description": "Synthetic test intake. Not a real deal.",
    "borrower": {
        "type": "individual",
        "domicile": "GB",
        "natural_person": True,
        "declared_high_net_worth": True,
        "business_purpose_declared": None,
    },
    "pledgor": {
        "same_as_borrower": True,
        "type": None,
        "domicile": None,
        "natural_person": None,
        "is_pdmr_of_pledged_issuer": False,
    },
    "guarantor_present": False,
    "facility": {
        "type": "uncommitted_demand",
        "purpose": "general",
        "amount": 1000000,
        "currency": "GBP",
        "benchmark": "SONIA",
        "other_facilities_with_lender": False,
    },
    "collateral": {
        "governing_law": "england_wales",
        "custodian_location": "GB",
        "lender_is_custodian": True,
        "currencies": ["GBP"],
        "composition": [
            {
                "asset_class": "listed_equity",
                "pct": 80,
                "single_name_max_pct": 10,
                "issuer_restricted": False,
            },
            {
                "asset_class": "cash",
                "pct": 20,
                "single_name_max_pct": None,
                "issuer_restricted": False,
            },
        ],
    },
    "counterparty_requests": {},
}


def deep_merge(base: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
    """Recursive dict merge used to describe one deviation from BASE."""
    out = copy.deepcopy(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = deep_merge(out[key], value)
        else:
            out[key] = copy.deepcopy(value)
    return out


def make_intake(**patch: Any) -> Intake:
    return Intake.model_validate(deep_merge(BASE, patch))


def test_base_intake_is_valid() -> None:
    intake = make_intake()
    assert intake.deal_id == "T01"
    assert intake.facility.amount == 1000000


# ---------------------------------------------------------------------------
# Closed lists and formats
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "patch",
    [
        {"borrower": {"type": "charity"}},
        {"facility": {"type": "revolving"}},
        {"facility": {"purpose": "yacht"}},
        {"facility": {"benchmark": "LIBOR"}},
        {"collateral": {"governing_law": "jersey"}},
        {"collateral": {"composition": [{"asset_class": "crypto", "pct": 10}]}},
    ],
)
def test_values_outside_a_closed_list_are_rejected(patch: dict[str, Any]) -> None:
    with pytest.raises(ValidationError):
        make_intake(**patch)


@pytest.mark.parametrize(
    "patch",
    [
        {"borrower": {"domicile": "GBR"}},
        {"borrower": {"domicile": "gb"}},
        {"collateral": {"custodian_location": "CHE"}},
        {"facility": {"currency": "GB"}},
        {"facility": {"currency": "gbp"}},
    ],
)
def test_iso_codes_are_checked(patch: dict[str, Any]) -> None:
    with pytest.raises(ValidationError):
        make_intake(**patch)


def test_collateral_currency_must_be_iso_4217() -> None:
    with pytest.raises(ValidationError) as exc:
        make_intake(collateral={"currencies": ["GBP", "dollars"]})
    assert "ISO 4217" in str(exc.value)


def test_facility_amount_must_be_positive() -> None:
    with pytest.raises(ValidationError):
        make_intake(facility={"amount": 0})


def test_unknown_key_anywhere_is_rejected() -> None:
    with pytest.raises(ValidationError) as exc:
        make_intake(borrower={"is_consumer": True})
    assert "not permitted" in str(exc.value)


def test_deal_id_pattern() -> None:
    with pytest.raises(ValidationError):
        make_intake(deal_id="D 02")


# ---------------------------------------------------------------------------
# Composition
# ---------------------------------------------------------------------------


def test_composition_summing_to_110_is_rejected() -> None:
    """build_plan.md §6, WP4 acceptance: a 110% portfolio must not validate."""
    with pytest.raises(ValidationError) as exc:
        make_intake(
            collateral={
                "composition": [
                    {"asset_class": "listed_equity", "pct": 70},
                    {"asset_class": "listed_bond", "pct": 40},
                ]
            }
        )
    assert "exceeds 100" in str(exc.value)
    assert "110" in str(exc.value)


def test_composition_summing_to_exactly_100_is_accepted() -> None:
    intake = make_intake(
        collateral={
            "composition": [
                {"asset_class": "listed_equity", "pct": 60},
                {"asset_class": "cash", "pct": 40},
            ]
        }
    )
    assert sum(i.pct for i in intake.collateral.composition) == 100


def test_composition_may_sum_to_less_than_100() -> None:
    intake = make_intake(
        collateral={"composition": [{"asset_class": "cash", "pct": 50}]}
    )
    assert len(intake.collateral.composition) == 1


def test_composition_may_not_be_empty() -> None:
    with pytest.raises(ValidationError):
        make_intake(collateral={"composition": []})


def test_currencies_may_not_be_empty() -> None:
    with pytest.raises(ValidationError):
        make_intake(collateral={"currencies": []})


@pytest.mark.parametrize("pct", [-1, 101])
def test_composition_pct_is_bounded(pct: float) -> None:
    with pytest.raises(ValidationError):
        make_intake(
            collateral={"composition": [{"asset_class": "cash", "pct": pct}]}
        )


def test_single_name_max_pct_is_bounded() -> None:
    with pytest.raises(ValidationError):
        make_intake(
            collateral={
                "composition": [
                    {
                        "asset_class": "listed_equity",
                        "pct": 50,
                        "single_name_max_pct": 120,
                    }
                ]
            }
        )


# ---------------------------------------------------------------------------
# Pledgor
# ---------------------------------------------------------------------------


def test_third_party_pledgor_must_give_its_details() -> None:
    with pytest.raises(ValidationError) as exc:
        make_intake(pledgor={"same_as_borrower": False})
    message = str(exc.value)
    assert "third-party pledgor" in message
    for field in ("type", "domicile", "natural_person"):
        assert field in message


def test_third_party_pledgor_with_details_is_accepted() -> None:
    intake = make_intake(
        pledgor={
            "same_as_borrower": False,
            "type": "individual",
            "domicile": "LU",
            "natural_person": True,
        }
    )
    assert intake.pledgor.natural_person is True


# ---------------------------------------------------------------------------
# Counterparty requests
# ---------------------------------------------------------------------------


def test_counterparty_request_needs_a_tier_or_text() -> None:
    with pytest.raises(ValidationError) as exc:
        make_intake(counterparty_requests={"margin_maintenance_cure": {}})
    assert "'tier', 'text', or both" in str(exc.value)


def test_counterparty_request_accepts_tier_text_or_both() -> None:
    intake = make_intake(
        counterparty_requests={
            "margin_maintenance_cure": {"tier": "fallback"},
            "enforcement_liquidation": {"text": "Wants written notice first."},
            "concentration_limits": {"tier": "acceptable", "text": "And a carve-out."},
        }
    )
    requests = intake.counterparty_requests
    assert requests["margin_maintenance_cure"].tier is Tier.fallback
    assert requests["margin_maintenance_cure"].text is None
    assert requests["enforcement_liquidation"].tier is None
    assert requests["concentration_limits"].text == "And a carve-out."


# ---------------------------------------------------------------------------
# Derived fields
# ---------------------------------------------------------------------------


def test_derived_defaults_on_the_quiet_base() -> None:
    d = make_intake().derived
    assert d.max_single_name_pct == 10.0
    assert d.has_real_estate is False
    assert d.currency_mismatch is False
    assert d.third_party_security is False
    assert d.any_natural_person_pledgor is True  # the borrower is an individual
    assert d.any_issuer_restricted is False
    assert d.has_illiquid_collateral is False


def test_max_single_name_pct_is_the_maximum_and_zero_when_absent() -> None:
    assert (
        make_intake(
            collateral={
                "composition": [
                    {"asset_class": "listed_equity", "pct": 40, "single_name_max_pct": 12},
                    {"asset_class": "listed_bond", "pct": 40, "single_name_max_pct": 33},
                ]
            }
        ).derived.max_single_name_pct
        == 33.0
    )
    assert (
        make_intake(
            collateral={"composition": [{"asset_class": "cash", "pct": 100}]}
        ).derived.max_single_name_pct
        == 0.0
    )


def test_currency_mismatch_is_any_currency_differing() -> None:
    """WP1's reading, kept in WP5: [GBP, USD] against a GBP facility is a mismatch."""
    assert make_intake(collateral={"currencies": ["GBP", "USD"]}).derived.currency_mismatch
    assert make_intake(collateral={"currencies": ["USD"]}).derived.currency_mismatch
    assert not make_intake(collateral={"currencies": ["GBP"]}).derived.currency_mismatch


def test_third_party_security_and_natural_person_pledgor_follow_the_pledgor() -> None:
    d = make_intake(
        pledgor={
            "same_as_borrower": False,
            "type": "corporate",
            "domicile": "LU",
            "natural_person": False,
        }
    ).derived
    assert d.third_party_security is True
    # The effective collateral provider is the company, not the individual borrower.
    assert d.any_natural_person_pledgor is False


def test_any_natural_person_pledgor_falls_back_to_the_borrower() -> None:
    d = make_intake(
        borrower={"type": "corporate", "natural_person": False, "declared_high_net_worth": None}
    ).derived
    assert d.third_party_security is False
    assert d.any_natural_person_pledgor is False


# -- the three WP5 changes --------------------------------------------------


def test_has_real_estate_requires_a_positive_percentage() -> None:
    """WP5 change: a real-estate line at zero per cent is not real-estate collateral."""
    zero = make_intake(
        collateral={
            "composition": [
                {"asset_class": "real_estate", "pct": 0},
                {"asset_class": "cash", "pct": 100},
            ]
        }
    )
    assert zero.derived.has_real_estate is False

    some = make_intake(
        collateral={
            "composition": [
                {"asset_class": "real_estate", "pct": 30},
                {"asset_class": "cash", "pct": 70},
            ]
        }
    )
    assert some.derived.has_real_estate is True


def test_any_issuer_restricted() -> None:
    """WP5 addition for R08. Percentage is not considered: any restricted line counts."""
    assert not make_intake().derived.any_issuer_restricted
    assert make_intake(
        collateral={
            "composition": [
                {
                    "asset_class": "listed_equity",
                    "pct": 100,
                    "single_name_max_pct": 10,
                    "issuer_restricted": True,
                }
            ]
        }
    ).derived.any_issuer_restricted


@pytest.mark.parametrize(
    "asset_class,expected",
    [
        ("fund_gated", True),
        ("unlisted", True),
        ("structured_product", True),
        ("fund_daily", False),
        ("listed_bond", False),
        ("cash", False),
        ("restricted_securities", False),
    ],
)
def test_has_illiquid_collateral_covers_exactly_three_asset_classes(
    asset_class: str, expected: bool
) -> None:
    """WP5 addition for R15: fund_gated, unlisted and structured_product only."""
    intake = make_intake(
        collateral={
            "composition": [
                {"asset_class": asset_class, "pct": 30},
                {"asset_class": "cash", "pct": 70},
            ]
        }
    )
    assert intake.derived.has_illiquid_collateral is expected


def test_has_illiquid_collateral_requires_a_positive_percentage() -> None:
    intake = make_intake(
        collateral={
            "composition": [
                {"asset_class": "fund_gated", "pct": 0},
                {"asset_class": "cash", "pct": 100},
            ]
        }
    )
    assert intake.derived.has_illiquid_collateral is False


def test_new_derived_fields_are_addressable_by_rules() -> None:
    paths = intake_field_paths()
    assert "derived.any_issuer_restricted" in paths
    assert "derived.has_illiquid_collateral" in paths


# ---------------------------------------------------------------------------
# Loading from file, and the CLI helpers
# ---------------------------------------------------------------------------


def test_demo_intake_file_loads_and_is_synthetic() -> None:
    intake = load_intake(DEMO_INTAKE)
    assert intake.deal_id == "T99"
    assert "synthetic" in intake.description.lower()
    d = intake.derived
    assert d.max_single_name_pct == 55.0
    assert d.any_issuer_restricted is True
    assert d.has_illiquid_collateral is True
    assert d.currency_mismatch is True
    assert d.has_real_estate is False


def test_load_intake_reports_file_and_problem(tmp_path: Path) -> None:
    data = deep_merge(BASE, {})
    data["collateral"]["composition"] = [
        {"asset_class": "listed_equity", "pct": 70},
        {"asset_class": "listed_bond", "pct": 40},
    ]
    path = tmp_path / "bad_deal.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(LibraryError) as exc:
        load_intake(path)
    joined = "\n".join(exc.value.errors)
    assert "bad_deal.yaml" in joined
    assert "exceeds 100" in joined


def test_echo_intake_round_trips_and_shows_derived_fields() -> None:
    intake = load_intake(DEMO_INTAKE)
    text = echo_intake(intake)
    data = yaml.safe_load(text)
    assert data["deal_id"] == "T99"
    assert data["derived"]["has_illiquid_collateral"] is True
    assert data["collateral"]["governing_law"] == "switzerland"


def test_expand_deal_paths_globs_and_passes_literals_through(tmp_path: Path) -> None:
    (tmp_path / "a.yaml").write_text("", encoding="utf-8")
    (tmp_path / "b.yaml").write_text("", encoding="utf-8")
    pattern = (tmp_path / "*.yaml").as_posix()
    assert [Path(p).name for p in expand_deal_paths([pattern])] == ["a.yaml", "b.yaml"]
    assert expand_deal_paths(["deals/D01.yaml"]) == ["deals/D01.yaml"]
    # A wildcard that matches nothing is passed through so the error names it.
    missing = (tmp_path / "nothing_*.yaml").as_posix()
    assert expand_deal_paths([missing]) == [missing]
