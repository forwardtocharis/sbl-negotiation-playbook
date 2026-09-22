"""Export JSON schemas from the pydantic models into ``playbook/schema/``.

The generated files are committed so the contract is readable without running
Python. Run after any model change:

    python scripts/export_schemas.py

Output is deterministic (sorted keys, trailing newline).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sbl.models import Clause, Intake, RunResult, Rule  # noqa: E402

TARGETS = {
    "clause.schema.json": Clause,
    "rule.schema.json": Rule,
    "intake.schema.json": Intake,
    # Added in WP5: the Markdown renderer works from RunResult alone, so its
    # shape is part of the contract and worth reading without running Python.
    "run_result.schema.json": RunResult,
}


def main() -> int:
    out_dir = ROOT / "playbook" / "schema"
    out_dir.mkdir(parents=True, exist_ok=True)
    for filename, model in TARGETS.items():
        schema = model.model_json_schema(mode="serialization")
        schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        text = json.dumps(schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        (out_dir / filename).write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote playbook/schema/{filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
