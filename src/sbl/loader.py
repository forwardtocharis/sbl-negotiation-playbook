"""Load and validate the playbook library.

Responsibilities (build_plan.md §6, WP1):

* read every YAML file under ``playbook/``;
* validate it against the models in :mod:`sbl.models`;
* resolve every cross-reference (rule action -> clause, rule -> flag,
  clause -> flag, clause ``depends_on`` -> clause, jurisdiction_notes key ->
  jurisdiction);
* validate every rule condition ``field`` as a dotted path into the Intake
  model, including ``derived.*`` — an unknown field is a hard error at load
  time, never a silent false;
* compute ``library_hash``, a sha256 over the sorted (relative path, bytes) of
  every playbook YAML file.

Every error names the file, and the rule or entry id, with a line number where
one can be located.
"""

from __future__ import annotations

import hashlib
import types
import typing
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional

import yaml
from pydantic import BaseModel, ValidationError

from .models import (
    CLAUSE_TARGETING_ACTIONS,
    AllCondition,
    AnyCondition,
    Clause,
    Flag,
    FlagAction,
    Intake,
    Jurisdiction,
    LeafCondition,
    NotCondition,
    Rule,
    Status,
)

# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class LibraryError(Exception):
    """One or more problems found while loading the library."""

    def __init__(self, errors: list[str]) -> None:
        self.errors = errors
        n = len(errors)
        body = "\n".join(f"  - {e}" for e in errors)
        super().__init__(
            f"{n} problem{'s' if n != 1 else ''} found loading the playbook library:\n{body}"
        )


# ---------------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------------


def _rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def locate_value(text: str, key: str, value: str) -> Optional[int]:
    """Return the 1-based line of the scalar ``value`` held under ``key``.

    Uses YAML node marks rather than a text search, so quoting and indentation
    do not matter. Returns ``None`` when the pair cannot be located.
    """
    try:
        docs = list(yaml.compose_all(text))
    except yaml.YAMLError:
        return None

    found: list[int] = []

    def walk(node: Any) -> None:
        if isinstance(node, yaml.MappingNode):
            for k, v in node.value:
                if (
                    isinstance(k, yaml.ScalarNode)
                    and k.value == key
                    and isinstance(v, yaml.ScalarNode)
                    and v.value == value
                ):
                    found.append(v.start_mark.line + 1)
                walk(v)
        elif isinstance(node, yaml.SequenceNode):
            for item in node.value:
                walk(item)

    for doc in docs:
        if doc is not None:
            walk(doc)
    return found[0] if found else None


def _at(file_rel: str, line: Optional[int]) -> str:
    return f"{file_rel}:{line}" if line else file_rel


def _format_validation_error(
    exc: ValidationError, file_rel: str, entry: Optional[str] = None
) -> list[str]:
    where = f"{file_rel}" + (f" [{entry}]" if entry else "")
    out = []
    for err in exc.errors():
        # Drop the internal union tags of the condition tree ("cond_all" etc.)
        # so the path a reader sees matches the path in their YAML file.
        parts = [
            str(p)
            for p in err["loc"]
            if not (isinstance(p, str) and p.startswith("cond_"))
        ]
        loc = ".".join(parts) or "<root>"
        out.append(f"{where}: field '{loc}': {err['msg']}")
    return out


def _load_yaml(path: Path, root: Path, errors: list[str]) -> Any:
    text = path.read_text(encoding="utf-8")
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        line = mark.line + 1 if mark is not None else None
        errors.append(f"{_at(_rel(path, root), line)}: YAML syntax error: {exc}")
        return None


# ---------------------------------------------------------------------------
# Intake field paths (for rule condition validation)
# ---------------------------------------------------------------------------


def _unwrap_optional(ann: Any) -> Any:
    origin = typing.get_origin(ann)
    if origin in (typing.Union, types.UnionType):
        args = [a for a in typing.get_args(ann) if a is not type(None)]
        if len(args) == 1:
            return args[0]
    return ann


def _model_paths(model: type[BaseModel], prefix: str = "") -> set[str]:
    """Every dotted path addressable inside ``model``.

    Container paths are included as well as leaves, so that ``contains`` can be
    used against a list field. A ``list[SomeModel]`` also contributes its item
    fields as a projection (``collateral.composition.asset_class``); the engine
    defines the semantics of a projected path in WP5.
    """
    paths: set[str] = set()

    items: list[tuple[str, Any]] = [
        (name, f.annotation) for name, f in model.model_fields.items()
    ]
    items += [
        (name, f.return_type) for name, f in model.model_computed_fields.items()
    ]

    for name, ann in items:
        path = f"{prefix}{name}"
        paths.add(path)
        ann = _unwrap_optional(ann)
        origin = typing.get_origin(ann)
        if origin in (list, set, tuple):
            args = typing.get_args(ann)
            if args:
                inner = _unwrap_optional(args[0])
                if isinstance(inner, type) and issubclass(inner, BaseModel):
                    paths |= _model_paths(inner, f"{path}.")
        elif origin is dict:
            continue
        elif isinstance(ann, type) and issubclass(ann, BaseModel):
            paths |= _model_paths(ann, f"{path}.")
    return paths


def intake_field_paths() -> set[str]:
    """The set of dotted paths a rule condition may address, incl. ``derived.*``."""
    return _model_paths(Intake)


def iter_leaf_conditions(condition: Any) -> Iterable[LeafCondition]:
    """Yield every leaf of a condition tree."""
    if isinstance(condition, LeafCondition):
        yield condition
    elif isinstance(condition, AllCondition):
        for c in condition.all:
            yield from iter_leaf_conditions(c)
    elif isinstance(condition, AnyCondition):
        for c in condition.any:
            yield from iter_leaf_conditions(c)
    elif isinstance(condition, NotCondition):
        yield from iter_leaf_conditions(condition.not_)


# ---------------------------------------------------------------------------
# Library
# ---------------------------------------------------------------------------


@dataclass
class Library:
    """The validated playbook: clauses, rules, jurisdictions, flags and a hash."""

    root: Path
    clauses: dict[str, Clause] = field(default_factory=dict)
    rules: list[Rule] = field(default_factory=list)
    jurisdictions: dict[str, Jurisdiction] = field(default_factory=dict)
    flags: dict[str, Flag] = field(default_factory=dict)
    library_hash: str = ""
    files: list[str] = field(default_factory=list)

    def status_counts(self) -> dict[str, dict[str, int]]:
        """Counts by kind and status, for ``sbl validate --summary``."""

        def counts(entries: Iterable[Any]) -> dict[str, int]:
            out = {s.value: 0 for s in Status}
            for e in entries:
                out[e.status.value] += 1
            return out

        return {
            "clauses": counts(self.clauses.values()),
            "rules": counts(self.rules),
            "jurisdictions": counts(self.jurisdictions.values()),
            "flags": counts(self.flags.values()),
        }


# ---------------------------------------------------------------------------
# Hashing
# ---------------------------------------------------------------------------


def playbook_yaml_files(playbook_dir: Path) -> list[Path]:
    """Every YAML file under ``playbook/``, sorted by POSIX relative path."""
    files = [
        p
        for p in playbook_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in (".yaml", ".yml")
    ]
    return sorted(files, key=lambda p: _rel(p, playbook_dir))


def compute_library_hash(playbook_dir: Path) -> str:
    """sha256 over the sorted (relative path, file bytes) of all playbook YAML."""
    h = hashlib.sha256()
    for path in playbook_yaml_files(playbook_dir):
        rel = _rel(path, playbook_dir).encode("utf-8")
        data = path.read_bytes()
        h.update(len(rel).to_bytes(4, "big"))
        h.update(rel)
        h.update(len(data).to_bytes(8, "big"))
        h.update(data)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


def _load_clauses(playbook_dir: Path, root: Path, errors: list[str]) -> dict[str, Clause]:
    clauses: dict[str, Clause] = {}
    src_files: dict[str, str] = {}
    for path in sorted((playbook_dir / "clauses").glob("*.yaml")):
        rel = _rel(path, root)
        data = _load_yaml(path, root, errors)
        if data is None:
            continue
        if not isinstance(data, dict):
            errors.append(f"{rel}: expected a mapping (one clause per file)")
            continue
        try:
            clause = Clause.model_validate(data)
        except ValidationError as exc:
            errors.extend(
                _format_validation_error(exc, rel, str(data.get("id", "<no id>")))
            )
            continue
        if clause.id in clauses:
            errors.append(
                f"{rel}: duplicate clause id '{clause.id}' "
                f"(already defined in {src_files[clause.id]})"
            )
            continue
        clauses[clause.id] = clause
        src_files[clause.id] = rel
    return clauses


def _load_rules(playbook_dir: Path, root: Path, errors: list[str]) -> list[Rule]:
    path = playbook_dir / "rules" / "rules.yaml"
    rel = _rel(path, root)
    if not path.exists():
        errors.append(f"{rel}: missing rules file")
        return []
    data = _load_yaml(path, root, errors)
    if data is None:
        return []
    if not isinstance(data, list):
        errors.append(f"{rel}: expected a list of rules")
        return []
    text = path.read_text(encoding="utf-8")
    rules: list[Rule] = []
    seen: set[str] = set()
    for i, item in enumerate(data):
        rid = item.get("id") if isinstance(item, dict) else None
        line = locate_value(text, "id", str(rid)) if rid else None
        label = str(rid) if rid else f"rule[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{_at(rel, line)}: {label}: expected a mapping")
            continue
        try:
            rule = Rule.model_validate(item)
        except ValidationError as exc:
            errors.extend(_format_validation_error(exc, _at(rel, line), label))
            continue
        if rule.id in seen:
            errors.append(f"{_at(rel, line)}: duplicate rule id '{rule.id}'")
            continue
        seen.add(rule.id)
        rules.append(rule)
    return rules


def _load_jurisdictions(
    playbook_dir: Path, root: Path, errors: list[str]
) -> dict[str, Jurisdiction]:
    out: dict[str, Jurisdiction] = {}
    for path in sorted((playbook_dir / "jurisdictions").glob("*.yaml")):
        rel = _rel(path, root)
        data = _load_yaml(path, root, errors)
        if data is None:
            continue
        if not isinstance(data, dict):
            errors.append(f"{rel}: expected a mapping (one jurisdiction per file)")
            continue
        try:
            j = Jurisdiction.model_validate(data)
        except ValidationError as exc:
            errors.extend(
                _format_validation_error(exc, rel, str(data.get("id", "<no id>")))
            )
            continue
        if j.id in out:
            errors.append(f"{rel}: duplicate jurisdiction id '{j.id}'")
            continue
        out[j.id] = j
    return out


def _load_flags(playbook_dir: Path, root: Path, errors: list[str]) -> dict[str, Flag]:
    path = playbook_dir / "flags" / "regulatory_flags.yaml"
    rel = _rel(path, root)
    if not path.exists():
        errors.append(f"{rel}: missing flags file")
        return {}
    data = _load_yaml(path, root, errors)
    if data is None:
        return {}
    if not isinstance(data, list):
        errors.append(f"{rel}: expected a list of flag definitions")
        return {}
    text = path.read_text(encoding="utf-8")
    out: dict[str, Flag] = {}
    for i, item in enumerate(data):
        fid = item.get("id") if isinstance(item, dict) else None
        line = locate_value(text, "id", str(fid)) if fid else None
        label = str(fid) if fid else f"flag[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{_at(rel, line)}: {label}: expected a mapping")
            continue
        try:
            flag = Flag.model_validate(item)
        except ValidationError as exc:
            errors.extend(_format_validation_error(exc, _at(rel, line), label))
            continue
        if flag.id in out:
            errors.append(f"{_at(rel, line)}: duplicate flag id '{flag.id}'")
            continue
        out[flag.id] = flag
    return out


def _check_cross_references(
    library: Library, playbook_dir: Path, root: Path, errors: list[str]
) -> None:
    clause_ids = set(library.clauses)
    flag_ids = set(library.flags)
    jurisdiction_ids = set(library.jurisdictions)
    known_paths = intake_field_paths()

    # clauses -> flags, clauses -> clauses, clauses -> jurisdictions
    for path in sorted((playbook_dir / "clauses").glob("*.yaml")):
        rel = _rel(path, root)
        text = path.read_text(encoding="utf-8")
        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            continue
        cid = data.get("id")
        clause = library.clauses.get(cid) if isinstance(cid, str) else None
        if clause is None:
            continue
        for fid in clause.regulatory_flags:
            if fid not in flag_ids:
                line = locate_value(text, "id", clause.id)
                errors.append(
                    f"{_at(rel, line)}: clause '{clause.id}' references unknown flag id "
                    f"'{fid}'. Known flags: {', '.join(sorted(flag_ids)) or '(none)'}"
                )
        for dep in clause.depends_on:
            if dep not in clause_ids:
                line = locate_value(text, "id", clause.id)
                errors.append(
                    f"{_at(rel, line)}: clause '{clause.id}' depends_on unknown clause id "
                    f"'{dep}'"
                )
        for jid in clause.jurisdiction_notes:
            if jid not in jurisdiction_ids:
                line = locate_value(text, "id", clause.id)
                errors.append(
                    f"{_at(rel, line)}: clause '{clause.id}' has a jurisdiction_notes key "
                    f"'{jid}' that is not a known jurisdiction id. Known: "
                    f"{', '.join(sorted(jurisdiction_ids)) or '(none)'}"
                )

    # rules -> clauses, rules -> flags, rule condition field paths
    rules_path = playbook_dir / "rules" / "rules.yaml"
    rules_rel = _rel(rules_path, root)
    rules_text = rules_path.read_text(encoding="utf-8") if rules_path.exists() else ""
    for rule in library.rules:
        line = locate_value(rules_text, "id", rule.id) if rules_text else None
        at = _at(rules_rel, line)
        for action in rule.then:
            if isinstance(action, FlagAction):
                if action.flag not in flag_ids:
                    errors.append(
                        f"{at}: rule '{rule.id}' raises unknown flag id '{action.flag}'. "
                        f"Known flags: {', '.join(sorted(flag_ids)) or '(none)'}"
                    )
            elif isinstance(action, CLAUSE_TARGETING_ACTIONS):
                if action.clause not in clause_ids:
                    errors.append(
                        f"{at}: rule '{rule.id}' action '{action.action.value}' names "
                        f"unknown clause id '{action.clause}'"
                    )
            else:  # EscalateAction may optionally name a clause
                target = getattr(action, "clause", None)
                if target is not None and target not in clause_ids:
                    errors.append(
                        f"{at}: rule '{rule.id}' action '{action.action.value}' names "
                        f"unknown clause id '{target}'"
                    )
        for leaf in iter_leaf_conditions(rule.when):
            if leaf.field not in known_paths:
                errors.append(
                    f"{at}: rule '{rule.id}' condition references unknown intake field "
                    f"'{leaf.field}'. Field must be a dotted path into the Intake model "
                    f"(including derived.*)."
                )


def load_library(root: Path | str = ".") -> Library:
    """Load, validate and cross-check the whole playbook.

    Raises :class:`LibraryError` listing every problem found.
    """
    root = Path(root).resolve()
    playbook_dir = root / "playbook"
    errors: list[str] = []

    if not playbook_dir.is_dir():
        raise LibraryError([f"no playbook directory at {playbook_dir}"])

    library = Library(root=root)
    library.clauses = _load_clauses(playbook_dir, root, errors)
    library.rules = _load_rules(playbook_dir, root, errors)
    library.jurisdictions = _load_jurisdictions(playbook_dir, root, errors)
    library.flags = _load_flags(playbook_dir, root, errors)

    if not errors:
        _check_cross_references(library, playbook_dir, root, errors)

    if errors:
        raise LibraryError(errors)

    library.library_hash = compute_library_hash(playbook_dir)
    library.files = [_rel(p, root) for p in playbook_yaml_files(playbook_dir)]
    return library


def load_intake(path: Path | str) -> Intake:
    """Load and validate one deal intake file."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise LibraryError([f"{path.as_posix()}: YAML syntax error: {exc}"]) from exc
    if not isinstance(data, dict):
        raise LibraryError([f"{path.as_posix()}: expected a mapping (one deal per file)"])
    try:
        return Intake.model_validate(data)
    except ValidationError as exc:
        raise LibraryError(
            _format_validation_error(exc, path.as_posix(), str(data.get("deal_id", "")))
        ) from exc


__all__ = [
    "Library",
    "LibraryError",
    "load_library",
    "load_intake",
    "compute_library_hash",
    "playbook_yaml_files",
    "intake_field_paths",
    "iter_leaf_conditions",
    "locate_value",
]
