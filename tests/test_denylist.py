"""Repo-wide denylist: no real institution or firm is named anywhere (WP9).

`build_plan.md` §0 rule 2 says the repository holds nothing but synthetic
parties, and §9 makes "grep for a denylist Stuart supplies" part of the
definition of done. This is that grep, as a test, so it runs on every commit
rather than when somebody remembers.

Scope: `playbook/`, `deals/`, `docs/`, `README.md` and `tests/expected/` — the
content a reader or an interviewer actually sees. Source code and hand-off
notes are out of scope by design; hand-off notes are working history.

Two exclusions before matching, and only two:

* any `http…` token, because a citation URL to a primary text or a published
  briefing legitimately carries its publisher's domain; and
* any line containing `url:`, for the same reason in YAML.

The prose, the labels and the notes get no such licence: the labelling
convention (`docs/source_register.md`) is that a publisher's name appears
inside a URL and nowhere else. The terms live in `tests/denylist.txt`, one per
line, so extending the list needs no code change.

`KNOWN_UNFIXED` below is a ledger, not an exemption. One file — WP7's raw
research notes — was written before the labelling convention existed and still
names two law firms and one case in prose. WP9 does not own `docs/` and could
not clean it, so the hits are listed here by file and by term. The test asserts
that a file's hits are **exactly** its ledger entry, which means a new name in
that file fails, a name anywhere else fails, and cleaning the file also fails
until the ledger entry is deleted. Nothing can decay quietly in either
direction.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DENYLIST_PATH = Path(__file__).resolve().parent / "denylist.txt"

#: Directories and files swept. Relative to the repo root.
SCANNED_DIRS = ("playbook", "deals", "docs", "tests/expected")
SCANNED_FILES = ("README.md",)

#: Only text formats. A .pyc or an image has nothing to read.
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt", ".csv"}

#: Pre-existing, itemised, owned by somebody else. Repo-relative path -> the
#: exact set of denylist terms that file still contains in prose. See the module
#: docstring: this is a ledger that fails in both directions, not a waiver.
#:
#: Empty, and it should stay that way. The one entry it ever held —
#: docs/research/jurisdictions_research.md, naming two law firms in source
#: `ref:` labels and one case in full — was cleaned in WP10a by applying the
#: labelling convention to that file, so the entry was deleted with it.
KNOWN_UNFIXED: dict[str, set[str]] = {}

_URL_TOKEN = re.compile(r"http\S+", re.IGNORECASE)
_URL_LINE = re.compile(r"url\s*:", re.IGNORECASE)
_WHITESPACE = re.compile(r"\s+")


def load_denylist() -> list[str]:
    """The terms, in file order, with comments and blanks dropped."""
    terms: list[str] = []
    for raw in DENYLIST_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        terms.append(line)
    return terms


def scanned_paths() -> list[Path]:
    """Every text file in scope, sorted, as absolute paths."""
    found: set[Path] = set()
    for rel in SCANNED_DIRS:
        directory = ROOT / rel
        if not directory.is_dir():
            continue
        for path in directory.rglob("*"):
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                found.add(path)
    for rel in SCANNED_FILES:
        path = ROOT / rel
        if path.is_file():
            found.add(path)
    return sorted(found)


def strip_urls(text: str) -> str:
    """Drop `url:` lines and every `http…` token, then flatten whitespace.

    Whitespace is flattened to single spaces across the whole document so that
    a two-word term still matches when a YAML folded block has wrapped it over
    a line break. That errs towards catching, which is the right direction for
    this test.
    """
    kept = [line for line in text.splitlines() if not _URL_LINE.search(line)]
    joined = _URL_TOKEN.sub(" ", "\n".join(kept))
    return _WHITESPACE.sub(" ", joined)


def term_pattern(term: str) -> re.Pattern[str]:
    r"""Case-insensitive, word-boundary match.

    ``\b`` before ``&`` would never match, so the boundary is only asserted
    where the term actually starts and ends with a word character.
    """
    body = re.escape(term)
    prefix = r"\b" if term[:1].isalnum() else ""
    suffix = r"\b" if term[-1:].isalnum() else ""
    return re.compile(prefix + body + suffix, re.IGNORECASE)


PATHS = scanned_paths()
TERMS = load_denylist()


def test_denylist_file_is_not_empty():
    assert len(TERMS) >= 26, "tests/denylist.txt lost entries"


def test_something_is_actually_scanned():
    """A silent empty sweep would make every other test in this file vacuous."""
    assert len(PATHS) >= 25
    names = {p.name for p in PATHS}
    assert "README.md" in names
    assert any(p.parent.name == "clauses" for p in PATHS)
    assert any(p.parent.name == "deals" for p in PATHS)
    assert any(p.parent.name == "expected" for p in PATHS)


def test_ledger_names_only_files_that_exist():
    """A stale ledger entry would silently excuse nothing, so catch it."""
    for rel in KNOWN_UNFIXED:
        assert (ROOT / rel).is_file(), f"KNOWN_UNFIXED names a missing file: {rel}"
        assert (ROOT / rel) in PATHS, f"KNOWN_UNFIXED names an unscanned file: {rel}"


@pytest.mark.parametrize("path", PATHS, ids=lambda p: p.relative_to(ROOT).as_posix())
def test_no_denylisted_name_in_file(path: Path):
    rel = path.relative_to(ROOT).as_posix()
    haystack = strip_urls(path.read_text(encoding="utf-8", errors="replace"))
    hits: dict[str, str] = {}
    for term in TERMS:
        match = term_pattern(term).search(haystack)
        if match:
            start = max(0, match.start() - 70)
            end = min(len(haystack), match.end() + 70)
            hits[term.lower()] = f"...{haystack[start:end]}..."

    allowed = KNOWN_UNFIXED.get(rel, set())
    unexpected = sorted(set(hits) - allowed)
    assert not unexpected, (
        f"denylisted name(s) in {rel}:\n"
        + "\n".join(f"  {t!r} -> {hits[t]}" for t in unexpected)
        + "\n(URLs and 'url:' lines are already excluded, so this is prose. "
        "Neutralise the label the way docs/source_register.md does, or, if "
        "Stuart has decided the term is acceptable, remove it from "
        "tests/denylist.txt.)"
    )
    fixed = sorted(allowed - set(hits))
    assert not fixed, (
        f"{rel} no longer contains {fixed}. Good — now delete those terms from "
        f"KNOWN_UNFIXED in this file so the ledger stays honest."
    )


def test_stripper_removes_urls_but_not_prose():
    text = "ref: something\nurl: https://www.barclays.example/x\nsee https://hsbc.example/y and the point"
    cleaned = strip_urls(text)
    assert "barclays" not in cleaned.lower()
    assert "hsbc" not in cleaned.lower()
    assert "and the point" in cleaned


def test_stripper_does_not_hide_prose_mentions():
    """The exclusion is for URLs only; a firm named in prose still trips."""
    cleaned = strip_urls("note: advice from Linklaters on the point")
    assert term_pattern("linklaters").search(cleaned)


def test_term_matching_is_on_word_boundaries():
    """'ubs' must not fire on 'subs', 'suburb' or 'pubs'."""
    pattern = term_pattern("ubs")
    assert not pattern.search("the subs and the suburbs")
    assert pattern.search("a UBS-style structure")


def test_multi_word_terms_survive_a_line_break():
    """A folded YAML block wrapping a two-word name is still caught."""
    cleaned = strip_urls("note: >-\n  advice from Clifford\n  Chance on the point\n")
    assert term_pattern("clifford chance").search(cleaned)
