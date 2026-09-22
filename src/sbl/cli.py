"""Command line interface: ``python -m sbl validate | run | explain``.

``validate`` loads and cross-checks the library (WP1). ``run`` loads a deal,
evaluates it and writes the run result (WP4/WP5). ``explain`` reads back a past
run from the audit log; it is implemented in WP6's :mod:`sbl.audit` and this
module delegates to it if it is importable.

``sbl.markup`` and ``sbl.audit`` are imported lazily inside the command, so
this package works before WP6 lands and gains the Markdown and audit output the
moment it does.
"""

from __future__ import annotations

import argparse
import glob as globlib
import sys
from pathlib import Path
from typing import Optional

import yaml

from .engine import evaluate
from .loader import LibraryError, load_intake, load_library
from .models import Intake, RunResult

DISCLAIMER = (
    "Demonstrator built from public sources. Synthetic deals. Not legal advice. "
    "Not validated against any institution's policy."
)


def _default_root() -> Path:
    """Repository root: the directory that holds ``playbook/``.

    Walks up from the working directory so the CLI works from a subdirectory.
    """
    here = Path.cwd().resolve()
    for candidate in (here, *here.parents):
        if (candidate / "playbook").is_dir():
            return candidate
    return here


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sbl",
        description="SBL Negotiation Playbook Demonstrator. " + DISCLAIMER,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root holding playbook/ (default: found by walking up from cwd)",
    )
    sub = parser.add_subparsers(dest="command", metavar="command")

    p_validate = sub.add_parser(
        "validate", help="Load and validate the playbook library"
    )
    p_validate.add_argument(
        "--summary",
        action="store_true",
        help="Print counts of clauses, rules, flags and jurisdictions by status",
    )

    p_run = sub.add_parser("run", help="Run a deal intake through the rules engine")
    p_run.add_argument(
        "deal",
        nargs="*",
        help="One or more deal YAML files. A '*' in an argument is expanded here "
        "as well as by the shell, for Windows.",
    )
    p_run.add_argument(
        "--out",
        default=None,
        help="Directory to write <deal_id>_<run_id>.json (and .md, and audit.jsonl) into",
    )
    p_run.add_argument(
        "--echo",
        action="store_true",
        help="Print the validated intake, derived fields included, as YAML",
    )

    p_explain = sub.add_parser(
        "explain", help="Explain how one clause outcome was reached in a past run"
    )
    p_explain.add_argument("run_id", nargs="?", help="Run id from runs/audit.jsonl")
    p_explain.add_argument("clause_id", nargs="?", help="Clause id to explain")
    p_explain.add_argument(
        "--audit",
        default=None,
        help="Path to the audit log (default: <root>/runs/audit.jsonl)",
    )

    return parser


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------


def _cmd_validate(args: argparse.Namespace) -> int:
    root = args.root or _default_root()
    try:
        library = load_library(root)
    except LibraryError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    n_clauses = len(library.clauses)
    n_rules = len(library.rules)
    n_jurisdictions = len(library.jurisdictions)
    n_flags = len(library.flags)
    print(
        f"OK: {n_clauses} clauses, {n_rules} rules, {n_flags} flags, "
        f"{n_jurisdictions} jurisdictions validated."
    )
    print(f"library_hash: {library.library_hash}")

    if args.summary:
        counts = library.status_counts()
        print("")
        print(f"{'kind':<14}{'stub':>8}{'draft':>8}{'reviewed':>10}{'total':>8}")
        print("-" * 48)
        for kind in ("clauses", "rules", "flags", "jurisdictions"):
            c = counts[kind]
            total = c["stub"] + c["draft"] + c["reviewed"]
            print(
                f"{kind:<14}{c['stub']:>8}{c['draft']:>8}{c['reviewed']:>10}{total:>8}"
            )
        print("")
        print(
            "Entries not marked 'reviewed' have not been checked by a named human "
            "reviewer."
        )
    return 0


# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------


def expand_deal_paths(patterns: list[str]) -> list[str]:
    """Expand any '*' in an argument ourselves.

    The Windows shell does not glob, so ``sbl run deals/*.yaml`` arrives as a
    literal. Arguments without a wildcard are passed through unchanged so that a
    missing file still produces a "no such file" error rather than vanishing.
    """
    out: list[str] = []
    for pattern in patterns:
        if any(ch in pattern for ch in "*?["):
            matches = sorted(globlib.glob(pattern))
            if not matches:
                out.append(pattern)
            else:
                out.extend(matches)
        else:
            out.append(pattern)
    return out


def echo_intake(intake: Intake) -> str:
    """The validated intake as YAML, derived fields included."""
    return yaml.safe_dump(
        intake.model_dump(mode="json"),
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )


def _write_outputs(result: RunResult, out_dir: Path) -> list[Path]:
    """Write the run JSON, plus Markdown and the audit line if WP6 has landed."""
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    stem = f"{result.deal_id}_{result.run_id}"
    json_path = out_dir / f"{stem}.json"
    json_path.write_text(
        result.model_dump_json(indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    written.append(json_path)

    try:  # WP6
        from .markup import render_markdown
    except ImportError:
        render_markdown = None  # type: ignore[assignment]
    if render_markdown is not None:
        md_path = out_dir / f"{stem}.md"
        md_path.write_text(render_markdown(result), encoding="utf-8", newline="\n")
        written.append(md_path)

    try:  # WP6
        from .audit import append_run
    except ImportError:
        append_run = None  # type: ignore[assignment]
    if append_run is not None:
        audit_path = out_dir / "audit.jsonl"
        append_run(result, audit_path)
        written.append(audit_path)

    return written


def _summary_line(result: RunResult, written: list[Path]) -> str:
    counts = result.status_summary
    bits = [
        f"{result.deal_id} run {result.run_id}",
        f"{len(result.clauses)} clauses "
        f"({counts.get('reviewed', 0)} reviewed / {counts.get('draft', 0)} draft / "
        f"{counts.get('stub', 0)} stub)",
        f"{len(result.flags)} flags",
        f"{len(result.escalations)} escalations",
        f"exit {result.exit_code}",
    ]
    if written:
        bits.append("wrote " + ", ".join(p.name for p in written))
    return " | ".join(bits)


def _cmd_run(args: argparse.Namespace) -> int:
    root = args.root or _default_root()
    if not args.deal:
        print("sbl run: give at least one deal YAML file", file=sys.stderr)
        return 1

    try:
        library = load_library(root)
    except LibraryError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    out_dir = Path(args.out) if args.out else None
    worst = 0
    for raw in expand_deal_paths(list(args.deal)):
        path = Path(raw)
        try:
            intake = load_intake(path)
        except LibraryError as exc:
            # LibraryError's own message talks about the library; an intake
            # failure is about one deal file, so say so.
            print(f"FAIL: {path.as_posix()} is not a valid intake:", file=sys.stderr)
            for problem in exc.errors:
                print(f"  - {problem}", file=sys.stderr)
            worst = max(worst, 1)
            continue
        except OSError as exc:
            print(f"FAIL: cannot read {path}: {exc}", file=sys.stderr)
            worst = max(worst, 1)
            continue

        if args.echo:
            print(f"# intake: {path.as_posix()} (validated, derived fields included)")
            print(echo_intake(intake), end="")

        result = evaluate(library, intake)
        written = _write_outputs(result, out_dir) if out_dir else []
        print(_summary_line(result, written))
        worst = max(worst, result.exit_code)

    return worst


# ---------------------------------------------------------------------------
# explain
# ---------------------------------------------------------------------------


def _cmd_explain(args: argparse.Namespace) -> int:
    if not args.run_id or not args.clause_id:
        print("sbl explain: give a run_id and a clause_id", file=sys.stderr)
        return 1
    try:  # WP6
        from .audit import explain
    except ImportError:
        print(
            "sbl explain: not implemented (sbl.audit is not available in this build)",
            file=sys.stderr,
        )
        return 1

    root = args.root or _default_root()
    audit_path = Path(args.audit) if args.audit else root / "runs" / "audit.jsonl"
    try:
        print(explain(args.run_id, args.clause_id, audit_path))
    except (OSError, KeyError, ValueError) as exc:
        print(f"sbl explain: {exc}", file=sys.stderr)
        return 1
    return 0


# ---------------------------------------------------------------------------


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0
    if args.command == "validate":
        return _cmd_validate(args)
    if args.command == "run":
        return _cmd_run(args)
    if args.command == "explain":
        return _cmd_explain(args)
    parser.print_help()
    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
