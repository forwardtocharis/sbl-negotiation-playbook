"""Deterministic rule evaluation (build_plan.md §6, WP5).

The engine takes a validated :class:`~sbl.loader.Library` and a validated
:class:`~sbl.models.Intake` and produces one :class:`~sbl.models.RunResult`.
It makes no network calls, reads no files and uses no randomness. The only
non-deterministic values in the output are ``timestamp`` and the ``run_id``
derived from it.

Three properties the rest of the build relies on:

**Tighten only.** Every tier assignment is ``tighter(current, proposed)``.
A rule can raise a floor or an opening; nothing can lower one. The opening
starts at ``preferred`` and the floor at the clause's ``default_floor``, so the
invariant "opening is tighter than or equal to floor" holds by construction and
is asserted before the result is returned.

**Order independence.** Rules are sorted by ``(priority, id)`` inside
:func:`evaluate`, whatever order they arrive in. Feeding the same rules in a
different order therefore produces a byte-identical result, and the ordering of
``cps`` / ``reps`` / ``notes`` within a clause is the canonical rule order
rather than an accident of file layout.

**Traceability.** Every string the engine appends to a clause's ``cps``,
``reps`` or ``notes`` is prefixed with the id of the rule that produced it, in
square brackets followed by one space::

    [R07_pdmr_pledged_issuer] Compliance sign-off on insider status.

and every clause records in ``rules_applied`` each rule that touched it. The
prefix is always ``"[" + rule_id + "] "`` where ``rule_id`` is the rule's id
exactly as it appears in ``playbook/rules/rules.yaml`` (or the literal ``R16``
for the built-in counterparty-request rule). A reader takes everything between
the leading ``[`` and the first ``] `` as the id.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel

from .loader import Library
from .models import (
    TIER_ORDER,
    AllCondition,
    AnyCondition,
    Clause,
    ClauseResult,
    Condition,
    ConditionOp,
    CounterpartyRequest,
    CounterpartyRequestOutcome,
    Escalation,
    EscalateAction,
    FlagAction,
    FlagResult,
    GoverningLaw,
    Intake,
    JurisdictionSummary,
    LadderRung,
    LeafCondition,
    NotCondition,
    NoteAction,
    RequestOutcome,
    RequireCpAction,
    RequireRepAction,
    RunResult,
    Rule,
    SetFloorAction,
    SetOpeningAction,
    Status,
    Tier,
    is_tighter_or_equal,
    tier_rank,
    tighter,
)

#: The rule id used for the built-in counterparty-request rule. It is not in
#: ``rules.yaml``: it has no ``when``, because it fires on the presence of a
#: request rather than on a fact about the deal.
R16_ID = "R16"

#: Appended to a ``rules_applied`` entry when the rule named the clause but
#: changed nothing on it (for example a ``set_floor`` to a tier that is not
#: tighter than the floor already reached, or a note that is already present).
NO_CHANGE_SUFFIX = " (no change)"

#: Default floor for a clause whose entry has no ``default_floor`` — that is,
#: for a ``stub`` clause. ``fallback`` is the plan's default concedable floor;
#: the clause's ``stub`` status is carried through to the output so the reader
#: can see that the number is a placeholder, not a reviewed position.
STUB_DEFAULT_FLOOR = Tier.fallback


class EngineError(Exception):
    """A problem the engine cannot evaluate around, such as an unknown path."""


# ---------------------------------------------------------------------------
# Field resolution
# ---------------------------------------------------------------------------


def _unwrap(value: Any) -> Any:
    """Normalise an enum to its value so YAML scalars compare cleanly."""
    return value.value if isinstance(value, Enum) else value


def resolve_field(intake: Intake, path: str) -> Any:
    """Resolve a dotted path into ``intake``, including ``derived.*``.

    Crossing a list of models projects: ``collateral.composition.asset_class``
    resolves to the list of that field across every composition line, which is
    what makes ``{op: contains}`` mean "any line". The loader has already
    checked that every rule's field paths are addressable; an unknown path here
    is a programming error and raises :class:`EngineError`.
    """
    current: Any = intake
    walked: list[str] = []
    for part in path.split("."):
        walked.append(part)
        current = _step(current, part, path, ".".join(walked))
    return current


def _step(current: Any, part: str, full_path: str, so_far: str) -> Any:
    if current is None:
        return None
    if isinstance(current, list):
        return [_step(item, part, full_path, so_far) for item in current]
    if isinstance(current, BaseModel):
        if part in type(current).model_fields or part in type(
            current
        ).model_computed_fields:
            return getattr(current, part)
        raise EngineError(
            f"cannot resolve field path '{full_path}': "
            f"'{type(current).__name__}' has no field '{part}' (at '{so_far}')"
        )
    if isinstance(current, dict):
        return current.get(part)
    raise EngineError(
        f"cannot resolve field path '{full_path}': '{so_far}' is not a model, "
        f"a list of models or a mapping"
    )


# ---------------------------------------------------------------------------
# Condition evaluation
# ---------------------------------------------------------------------------


def _values_equal(actual: Any, expected: Any) -> bool:
    a, b = _unwrap(actual), _unwrap(expected)
    if isinstance(a, bool) or isinstance(b, bool):
        # True == 1 in Python. A boolean field only ever equals a boolean value.
        return isinstance(a, bool) and isinstance(b, bool) and a is b
    return bool(a == b)


def _compare(actual: Any, expected: Any, op: ConditionOp) -> bool:
    """Ordered comparison. Anything not orderable, or null, is False."""
    a, b = _unwrap(actual), _unwrap(expected)
    if a is None or b is None:
        return False
    if isinstance(a, bool) or isinstance(b, bool):
        return False
    try:
        if op is ConditionOp.gt:
            return bool(a > b)
        if op is ConditionOp.gte:
            return bool(a >= b)
        if op is ConditionOp.lt:
            return bool(a < b)
        return bool(a <= b)
    except TypeError:
        return False


def _contains(actual: Any, expected: Any) -> bool:
    if actual is None:
        return False
    if isinstance(actual, str):
        wanted = _unwrap(expected)
        return isinstance(wanted, str) and wanted in actual
    if isinstance(actual, (list, tuple, set, frozenset)):
        return any(_values_equal(item, expected) for item in actual)
    return False


def evaluate_leaf(leaf: LeafCondition, intake: Intake) -> bool:
    """Evaluate one ``{field, op, value}`` condition.

    A null on the left-hand side makes every operator False except ``is_null``.
    That is deliberate: "we do not know" must never read as "the rule fires",
    and it must never read as an error either, because most intake fields are
    legitimately null on most deals.
    """
    actual = resolve_field(intake, leaf.field)
    op = leaf.op

    if op is ConditionOp.is_null:
        return actual is None
    if actual is None:
        return False
    if op is ConditionOp.eq:
        return _values_equal(actual, leaf.value)
    if op is ConditionOp.neq:
        return not _values_equal(actual, leaf.value)
    if op is ConditionOp.in_:
        return any(_values_equal(actual, candidate) for candidate in leaf.value)
    if op is ConditionOp.not_in:
        return not any(_values_equal(actual, candidate) for candidate in leaf.value)
    if op is ConditionOp.contains:
        return _contains(actual, leaf.value)
    return _compare(actual, leaf.value, op)


def evaluate_condition(condition: Condition, intake: Intake) -> bool:
    """Evaluate a condition tree (``all`` / ``any`` / ``not`` / leaf)."""
    if isinstance(condition, LeafCondition):
        return evaluate_leaf(condition, intake)
    if isinstance(condition, AllCondition):
        return all(evaluate_condition(c, intake) for c in condition.all)
    if isinstance(condition, AnyCondition):
        return any(evaluate_condition(c, intake) for c in condition.any)
    if isinstance(condition, NotCondition):
        return not evaluate_condition(condition.not_, intake)
    raise EngineError(f"unknown condition node type: {type(condition).__name__}")


# ---------------------------------------------------------------------------
# Per-clause working state
# ---------------------------------------------------------------------------


@dataclass
class _ClauseState:
    clause: Clause
    floor: Tier
    opening: Tier
    rules_applied: list[str] = field(default_factory=list)
    cps: list[str] = field(default_factory=list)
    reps: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def add_text(self, bucket: str, rule_id: str, text: str) -> bool:
        """Append ``[rule_id] text`` to one of cps/reps/notes. True if new."""
        target: list[str] = getattr(self, bucket)
        line = f"[{rule_id}] {text}"
        if line in target:
            return False
        target.append(line)
        return True

    def record_rule(self, rule_id: str, changed: bool) -> None:
        label = rule_id if changed else rule_id + NO_CHANGE_SUFFIX
        if label in self.rules_applied:
            return
        if changed and (rule_id + NO_CHANGE_SUFFIX) in self.rules_applied:
            # A later action of the same rule did change something: upgrade.
            self.rules_applied[
                self.rules_applied.index(rule_id + NO_CHANGE_SUFFIX)
            ] = rule_id
            return
        if not changed and rule_id in self.rules_applied:
            return
        self.rules_applied.append(label)


# ---------------------------------------------------------------------------
# Hashing
# ---------------------------------------------------------------------------


def compute_intake_hash(intake: Intake) -> str:
    """sha256 over the canonical JSON of the intake, derived fields included.

    Hashing the model rather than the file means comments and formatting do not
    change the hash, and the derived facts the rules actually read are inside
    it.
    """
    return hashlib.sha256(intake.model_dump_json().encode("utf-8")).hexdigest()


def compute_run_id(library_hash: str, intake_hash: str, timestamp: str) -> str:
    """First twelve hex characters of sha256(library + intake + timestamp)."""
    digest = hashlib.sha256(
        (library_hash + intake_hash + timestamp).encode("utf-8")
    ).hexdigest()
    return digest[:12]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


# ---------------------------------------------------------------------------
# The engine
# ---------------------------------------------------------------------------


def sorted_rules(rules: list[Rule]) -> list[Rule]:
    """Canonical evaluation order: priority ascending, then id."""
    return sorted(rules, key=lambda r: (r.priority, r.id))


def evaluate(
    library: Library, intake: Intake, *, timestamp: Optional[str] = None
) -> RunResult:
    """Run ``intake`` against ``library`` and return the complete run record."""
    states: dict[str, _ClauseState] = {
        cid: _ClauseState(
            clause=clause,
            floor=clause.default_floor or STUB_DEFAULT_FLOOR,
            opening=Tier.preferred,
        )
        for cid, clause in library.clauses.items()
    }

    flags: list[FlagResult] = []
    escalations: list[Escalation] = []
    raised_flag_ids: set[str] = set()

    for rule in sorted_rules(library.rules):
        if not evaluate_condition(rule.when, intake):
            continue
        touched: dict[str, bool] = {}
        for action in rule.then:
            if isinstance(action, FlagAction):
                definition = library.flags.get(action.flag)
                flags.append(
                    FlagResult(
                        id=action.flag,
                        severity=action.severity,
                        message=action.message,
                        rule_id=rule.id,
                        who_decides=definition.who_decides if definition else None,
                    )
                )
                raised_flag_ids.add(action.flag)
                continue

            if isinstance(action, EscalateAction):
                escalations.append(
                    Escalation(
                        rule_id=rule.id,
                        to=action.to,
                        reason=action.reason,
                        clause=action.clause,
                    )
                )
                if action.clause is not None:
                    # An escalation naming a clause materially changes that
                    # clause's outcome, so it counts as a change.
                    touched[action.clause] = True
                continue

            state = states.get(action.clause)
            if state is None:  # pragma: no cover - the loader forbids this
                raise EngineError(
                    f"rule '{rule.id}' action '{action.action.value}' names unknown "
                    f"clause id '{action.clause}'"
                )

            if isinstance(action, SetFloorAction):
                new = tighter(state.floor, action.tier)
                changed = new is not state.floor
                state.floor = new
            elif isinstance(action, SetOpeningAction):
                new = tighter(state.opening, action.tier)
                changed = new is not state.opening
                state.opening = new
            elif isinstance(action, RequireCpAction):
                changed = state.add_text("cps", rule.id, action.text)
            elif isinstance(action, RequireRepAction):
                changed = state.add_text("reps", rule.id, action.text)
            elif isinstance(action, NoteAction):
                changed = state.add_text("notes", rule.id, action.text)
            else:  # pragma: no cover - the action union is closed
                raise EngineError(f"unknown action type on rule '{rule.id}'")

            touched[action.clause] = touched.get(action.clause, False) or changed

        for clause_id, changed in touched.items():
            states[clause_id].record_rule(rule.id, changed)

    # -- built-in R16: counterparty requests --------------------------------
    outcomes = _apply_r16(intake, states, escalations)

    # -- assemble -----------------------------------------------------------
    governing_law = intake.collateral.governing_law
    escalated_clause_ids = {e.clause for e in escalations if e.clause}

    clause_results: list[ClauseResult] = []
    not_automated: set[str] = set()
    status_summary = {Status.reviewed.value: 0, Status.draft.value: 0, Status.stub.value: 0}

    for clause_id, state in states.items():
        clause = state.clause
        if not is_tighter_or_equal(state.opening, state.floor):
            raise EngineError(
                f"clause '{clause_id}': opening '{state.opening.value}' is looser than "
                f"floor '{state.floor.value}'. The engine may only tighten; this is a "
                f"bug, not a data problem."
            )
        status_summary[clause.status.value] += 1

        ladder = _build_ladder(clause)
        opening_text: Optional[str] = None
        opening_rationale: Optional[str] = None
        for rung in ladder:
            if rung.tier is state.opening:
                opening_text = rung.text
                opening_rationale = rung.rationale

        jurisdiction_note = (
            clause.jurisdiction_notes.get(governing_law.value)
            if governing_law is not GoverningLaw.other
            else None
        )

        clause_results.append(
            ClauseResult(
                id=clause_id,
                title=clause.title,
                category=clause.category,
                document=clause.document,
                risk_rating=clause.risk_rating,
                status=clause.status,
                opening=state.opening,
                floor=state.floor,
                opening_text=opening_text,
                opening_rationale=opening_rationale,
                ladder=ladder,
                jurisdiction_note=jurisdiction_note,
                rules_applied=list(state.rules_applied),
                cps=list(state.cps),
                reps=list(state.reps),
                notes=list(state.notes),
                escalation_triggers=list(clause.escalation_triggers),
                not_automated=list(clause.not_automated),
            )
        )

        flagged = any(fid in raised_flag_ids for fid in clause.regulatory_flags)
        if state.rules_applied or clause_id in escalated_clause_ids or flagged:
            not_automated.update(clause.not_automated)

    jurisdiction = _jurisdiction_summary(library, governing_law)

    timestamp = timestamp or _now()
    intake_hash = compute_intake_hash(intake)
    run_id = compute_run_id(library.library_hash, intake_hash, timestamp)

    return RunResult(
        run_id=run_id,
        timestamp=timestamp,
        library_hash=library.library_hash,
        intake_hash=intake_hash,
        deal_id=intake.deal_id,
        description=intake.description,
        governing_law=governing_law,
        intake=intake,
        status_summary=status_summary,
        jurisdiction=jurisdiction,
        clauses=clause_results,
        flags=flags,
        escalations=escalations,
        counterparty_request_outcomes=outcomes,
        not_automated=sorted(not_automated),
        exit_code=2 if escalations else 0,
    )


def _build_ladder(clause: Clause) -> list[LadderRung]:
    """All four tiers, preferred first. Empty for a stub clause."""
    if clause.positions is None:
        return []
    rungs: list[LadderRung] = []
    for tier in TIER_ORDER:
        position = getattr(clause.positions, tier.value)
        rungs.append(
            LadderRung(
                tier=tier,
                text=position.text,
                rationale=position.rationale,
                conditions=list(getattr(position, "conditions", []) or []),
                approval=getattr(position, "approval", None),
            )
        )
    return rungs


def _jurisdiction_summary(
    library: Library, governing_law: GoverningLaw
) -> Optional[JurisdictionSummary]:
    if governing_law is GoverningLaw.other:
        return None
    entry = library.jurisdictions.get(governing_law.value)
    if entry is None:
        return None
    return JurisdictionSummary(
        id=entry.id,
        name=entry.name,
        creation=entry.creation,
        registration_filing=entry.registration_filing,
        perfection_depends_on=entry.perfection_depends_on,
        enforcement_route=entry.enforcement_route,
        financial_collateral_regime=entry.financial_collateral_regime,
        governing_law_of_intermediated_securities=(
            entry.governing_law_of_intermediated_securities
        ),
        practical_notes=entry.practical_notes,
        status=entry.status,
    )


# ---------------------------------------------------------------------------
# R16: counterparty requests (built in, not in rules.yaml)
# ---------------------------------------------------------------------------


def _approver_for(clause: Clause, tier: Tier) -> str:
    if clause.positions is None:
        return "no approver recorded (this clause entry is still a stub)"
    if tier is Tier.unacceptable:
        return "nobody"
    approval = getattr(clause.positions, tier.value).approval
    return approval or "no named approver recorded for this tier"


def _apply_r16(
    intake: Intake,
    states: dict[str, _ClauseState],
    escalations: list[Escalation],
) -> list[CounterpartyRequestOutcome]:
    """Score each counterparty request against the floor this run computed.

    Three outcomes, per build_plan.md §2.5:

    * ``unacceptable_escalated`` — the request is at the walk-away tier.
    * ``below_floor_escalated`` — the request is looser than the floor, **or**
      it is free text with no tier, which the engine will not guess at.
    * ``accepted_within_floor`` — the request is at or tighter than the floor;
      a note records the concession and the approver for that tier.
    """
    outcomes: list[CounterpartyRequestOutcome] = []
    for clause_id in sorted(intake.counterparty_requests):
        request: CounterpartyRequest = intake.counterparty_requests[clause_id]
        state = states.get(clause_id)
        if state is None:
            raise EngineError(
                f"counterparty request names unknown clause id '{clause_id}'. "
                f"Requests are keyed by clause id; known ids are in playbook/clauses/."
            )
        floor = state.floor
        tier = request.tier

        if tier is None:
            state.add_text(
                "notes",
                R16_ID,
                "Free-text counterparty request; the engine does not map prose to a "
                f'position tier. Request text: "{request.text}". A lawyer must '
                "classify it against the ladder before it can be scored.",
            )
            escalations.append(
                Escalation(
                    rule_id=R16_ID,
                    to="deal lawyer",
                    reason=(
                        "unmapped counterparty request text requires manual "
                        "classification"
                    ),
                    clause=clause_id,
                )
            )
            state.record_rule(R16_ID, True)
            outcomes.append(
                CounterpartyRequestOutcome(
                    clause=clause_id,
                    requested_tier=None,
                    requested_text=request.text,
                    floor=floor,
                    outcome=RequestOutcome.below_floor_escalated,
                )
            )
            continue

        suffix = f' Request text: "{request.text}".' if request.text else ""

        if tier is Tier.unacceptable:
            state.add_text(
                "notes",
                R16_ID,
                "Counterparty asked for the 'unacceptable' tier on this clause. That "
                "is the walk-away line: nobody may agree it." + suffix,
            )
            escalations.append(
                Escalation(
                    rule_id=R16_ID,
                    to="senior lawyer",
                    reason=(
                        f"Counterparty requested the 'unacceptable' tier on clause "
                        f"'{clause_id}'. This is the lender's walk-away line and "
                        f"nobody may agree it."
                    ),
                    clause=clause_id,
                )
            )
            outcome = RequestOutcome.unacceptable_escalated
        elif tier_rank(tier) > tier_rank(floor):
            state.add_text(
                "notes",
                R16_ID,
                f"Counterparty request at tier '{tier.value}' is looser than the floor "
                f"'{floor.value}' computed for this deal, so it cannot be agreed by the "
                "deal lawyer." + suffix,
            )
            escalations.append(
                Escalation(
                    rule_id=R16_ID,
                    to="senior lawyer",
                    reason=(
                        f"Counterparty requested tier '{tier.value}' on clause "
                        f"'{clause_id}', which is looser than the floor "
                        f"'{floor.value}' this deal's facts produce."
                    ),
                    clause=clause_id,
                )
            )
            outcome = RequestOutcome.below_floor_escalated
        else:
            state.add_text(
                "notes",
                R16_ID,
                f"Counterparty request accepted within floor at tier '{tier.value}' "
                f"(floor '{floor.value}'); approver: {_approver_for(state.clause, tier)}."
                + suffix,
            )
            outcome = RequestOutcome.accepted_within_floor

        state.record_rule(R16_ID, True)
        outcomes.append(
            CounterpartyRequestOutcome(
                clause=clause_id,
                requested_tier=tier,
                requested_text=request.text,
                floor=floor,
                outcome=outcome,
            )
        )
    return outcomes


__all__ = [
    "EngineError",
    "R16_ID",
    "NO_CHANGE_SUFFIX",
    "STUB_DEFAULT_FLOOR",
    "evaluate",
    "evaluate_condition",
    "evaluate_leaf",
    "resolve_field",
    "sorted_rules",
    "compute_intake_hash",
    "compute_run_id",
]
