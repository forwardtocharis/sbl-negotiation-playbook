"""The README must carry the current ``library_hash``.

The README pastes the output of ``python -m sbl validate --summary``, which
includes the sha256 over every YAML file under ``playbook/``. That block goes
stale the moment any clause, rule, flag or jurisdiction file changes, and
nothing else in the repository notices. This test is the noticing: it computes
the hash the way the loader does and fails if the README does not contain it.

Fix a failure by re-running ``python -m sbl validate --summary`` and pasting the
block into the "Status counts" section of ``README.md`` (and into
``docs/demo_script.md``, which quotes the same value).
"""

from __future__ import annotations

from pathlib import Path

from sbl.loader import compute_library_hash

ROOT = Path(__file__).resolve().parents[1]


def test_readme_quotes_the_current_library_hash() -> None:
    expected = compute_library_hash(ROOT / "playbook")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert expected in readme, (
        "README.md does not contain the current library_hash "
        f"{expected}. Re-run 'python -m sbl validate --summary' and paste the "
        "block into the 'Status counts' section of README.md; docs/demo_script.md "
        "quotes the same value and should be updated with it."
    )
