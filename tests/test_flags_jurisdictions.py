"""Tests for the WP7 jurisdiction overlay and the WP8 regulatory flags.

These tests guard four things:

1. the library still loads with the jurisdiction and flag files in place;
2. every flag id referenced from a rule or a clause actually exists, and every
   flag carries a ``who_decides`` role, so the markup can always name a human;
3. every jurisdiction file answers all seven questions and cites at least one
   source per file, so an overlay cannot silently skip a question;
4. nothing in these two directories is marked ``reviewed`` (only a named human
   promotes an entry), and no real institution name appears in any non-URL text
   (``build_plan.md`` §0 rule 2 — publisher names may appear inside a URL only).

``rules.yaml`` is written by a different work package and may still be empty when
these tests run; the rule-reference test skips itself in that case rather than
passing vacuously by accident.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

from sbl.loader import load_library
from sbl.models import Status

ROOT = Path(__file__).resolve().parents[1]
JURISDICTION_DIR = ROOT / "playbook" / "jurisdictions"
FLAGS_FILE = ROOT / "playbook" / "flags" / "regulatory_flags.yaml"
RULES_FILE = ROOT / "playbook" / "rules" / "rules.yaml"

#: The seven substantive questions every jurisdiction overlay must answer.
JURISDICTION_FIELDS = (
    "creation",
    "registration_filing",
    "perfection_depends_on",
    "enforcement_route",
    "financial_collateral_regime",
    "governing_law_of_intermediated_securities",
    "practical_notes",
)

#: Real institution names that must not appear outside a URL. Matched
#: case-insensitively on word boundaries, so ordinary English words that happen
#: to contain one of these strings (substitution, challenge, citizen) do not trip
#: the test while the institution name itself still does.
DENYLIST = (
    "societe",
    "generale",
    "ubs",
    "credit suisse",
    "julius",
    "pictet",
    "lombard odier",
    "barclays",
    "hsbc",
    "coutts",
    "goldman",
    "morgan",
    "citi",
    "clifford",
    "allen",
    "linklaters",
    "freshfields",
    "addleshaw",
    "karrer",
    "lenz",
    "loyens",
    "elvinger",
    "arendt",
)

URL_RE = re.compile(r"http\S+")


def _strip_urls(text: str) -> str:
    """Remove every URL, so a publisher's name inside one does not trip the test."""
    return URL_RE.sub(" ", text)


def _guarded_files() -> list[Path]:
    return sorted(JURISDICTION_DIR.glob("*.yaml")) + [FLAGS_FILE]


@pytest.fixture(scope="module")
def library():
    return load_library(ROOT)


# ---------------------------------------------------------------------------
# 1. The library loads
# ---------------------------------------------------------------------------


def test_library_loads(library):
    assert library.flags, "no flags loaded"
    assert library.jurisdictions, "no jurisdictions loaded"


def test_three_jurisdiction_files_present(library):
    assert set(library.jurisdictions) == {
        "england_wales",
        "switzerland",
        "luxembourg",
    }


# ---------------------------------------------------------------------------
# 2. Flag references resolve, and every flag names a decider
# ---------------------------------------------------------------------------


def _flag_ids_used_by_rules() -> set[str]:
    raw = yaml.safe_load(RULES_FILE.read_text(encoding="utf-8")) or []
    used: set[str] = set()
    for rule in raw:
        for action in rule.get("then", []) or []:
            if action.get("action") == "flag" and action.get("flag"):
                used.add(action["flag"])
    return used


def test_every_flag_id_used_by_a_rule_exists(library):
    raw = yaml.safe_load(RULES_FILE.read_text(encoding="utf-8")) or []
    if not raw:
        pytest.skip("rules.yaml is empty (written by another work package)")
    missing = sorted(_flag_ids_used_by_rules() - set(library.flags))
    assert not missing, f"rules reference undefined flag ids: {missing}"


def test_every_flag_id_used_by_a_clause_exists(library):
    missing: list[str] = []
    for clause in library.clauses.values():
        for flag_id in clause.regulatory_flags:
            if flag_id not in library.flags:
                missing.append(f"{clause.id} -> {flag_id}")
    assert not missing, f"clauses reference undefined flag ids: {missing}"


def test_every_flag_has_a_non_empty_who_decides(library):
    empty = [f.id for f in library.flags.values() if not f.who_decides.strip()]
    assert not empty, f"flags with no who_decides: {empty}"


def test_flag_ids_are_the_ten_agreed_ids(library):
    assert set(library.flags) == {
        "consumer_credit",
        "mortgage_regulation",
        "mifid_suitability",
        "market_abuse",
        "restricted_securities",
        "fcar_safe_harbour_uncertain",
        "financial_assistance_corporate_benefit",
        "bank_secrecy_data",
        "prudential_awareness",
        "emir_awareness",
    }


# ---------------------------------------------------------------------------
# 3. Jurisdiction completeness
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("field", JURISDICTION_FIELDS)
def test_every_jurisdiction_answers_every_question(library, field):
    blank = [
        j.id
        for j in library.jurisdictions.values()
        if not getattr(j, field).strip() or getattr(j, field).strip() == "stub"
    ]
    assert not blank, f"jurisdictions with no answer for '{field}': {blank}"


def test_every_jurisdiction_has_at_least_one_source(library):
    missing = [j.id for j in library.jurisdictions.values() if len(j.sources) < 1]
    assert not missing, f"jurisdictions with no sources: {missing}"


def test_every_flag_has_at_least_one_source(library):
    missing = [f.id for f in library.flags.values() if len(f.sources) < 1]
    assert not missing, f"flags with no sources: {missing}"


# ---------------------------------------------------------------------------
# 4. Status discipline and the institution-name denylist
# ---------------------------------------------------------------------------


def test_no_reviewed_status_in_flags_or_jurisdictions(library):
    reviewed = [
        entry.id
        for entry in list(library.flags.values()) + list(library.jurisdictions.values())
        if entry.status is Status.reviewed
    ]
    assert not reviewed, (
        "only a named human reviewer may set status 'reviewed'; found: " f"{reviewed}"
    )


@pytest.mark.parametrize("path", _guarded_files(), ids=lambda p: p.name)
def test_no_real_institution_names_outside_urls(path: Path):
    text = _strip_urls(path.read_text(encoding="utf-8"))
    hits = sorted(
        {
            name
            for name in DENYLIST
            if re.search(rf"\b{re.escape(name)}\b", text, flags=re.IGNORECASE)
        }
    )
    assert not hits, (
        f"{path.name} names a real institution outside a URL: {hits}. "
        "Publisher names belong in the url field only (build_plan.md §0 rule 2)."
    )
