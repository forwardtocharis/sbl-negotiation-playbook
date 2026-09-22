"""Data contracts for the SBL Negotiation Playbook Demonstrator.

Frozen in WP1 per `build_plan.md` §2. Every later work package builds on these
models; schema changes after WP1 need a note in the hand-off and a full test
rerun (build_plan.md §6, WP1 "Freeze").

Conventions used throughout:

* Every model forbids unknown keys (``extra="forbid"``). A typo in a YAML file
  is an error, never a silently ignored field.
* Every library entry carries ``status`` in ``stub | draft | reviewed``. Agents
  may write ``stub`` or ``draft`` only; ``reviewed`` requires ``reviewed_by``.
* Positions are drafted from the lender's (private bank's) side.
* Tiers only ever tighten. See ``TIER_ORDER`` and ``tighter``.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Discriminator,
    Field,
    Tag,
    computed_field,
    field_validator,
    model_validator,
)

# ---------------------------------------------------------------------------
# Enums: every closed list in the contract
# ---------------------------------------------------------------------------


class Category(str, Enum):
    """Clause category (build_plan.md §2.1)."""

    credit = "credit"
    collateral = "collateral"
    default_enforcement = "default_enforcement"
    parties_reps = "parties_reps"
    boilerplate = "boilerplate"


class Document(str, Enum):
    """Which document of the SBL set the clause lives in."""

    facility_letter = "facility_letter"
    security_agreement = "security_agreement"
    account_control = "account_control"
    all = "all"


class RiskRating(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class Tier(str, Enum):
    """The four-tier position ladder, lender side."""

    preferred = "preferred"
    acceptable = "acceptable"
    fallback = "fallback"
    unacceptable = "unacceptable"


class Status(str, Enum):
    """Review status. Agents may write ``stub`` or ``draft`` only."""

    stub = "stub"
    draft = "draft"
    reviewed = "reviewed"


class SourceType(str, Enum):
    primary_law = "primary_law"
    regulator = "regulator"
    filed_agreement = "filed_agreement"
    bank_terms = "bank_terms"
    law_firm_briefing = "law_firm_briefing"
    textbook = "textbook"


class Reliability(str, Enum):
    """A primary law/regulator; B filed agreement/bank terms; C commentary."""

    A = "A"
    B = "B"
    C = "C"


class BorrowerType(str, Enum):
    individual = "individual"
    corporate = "corporate"
    trust = "trust"
    partnership = "partnership"
    fund = "fund"


class FacilityType(str, Enum):
    uncommitted_demand = "uncommitted_demand"
    committed_term = "committed_term"


class Purpose(str, Enum):
    general = "general"
    acquire_securities = "acquire_securities"
    real_estate = "real_estate"
    business = "business"


class Benchmark(str, Enum):
    SONIA = "SONIA"
    SARON = "SARON"
    EURIBOR = "EURIBOR"
    fixed = "fixed"
    other = "other"


class GoverningLaw(str, Enum):
    england_wales = "england_wales"
    switzerland = "switzerland"
    luxembourg = "luxembourg"
    other = "other"


class AssetClass(str, Enum):
    cash = "cash"
    listed_equity = "listed_equity"
    listed_bond = "listed_bond"
    fund_daily = "fund_daily"
    fund_gated = "fund_gated"
    structured_product = "structured_product"
    unlisted = "unlisted"
    restricted_securities = "restricted_securities"
    real_estate = "real_estate"


#: Asset classes treated as illiquid for ``derived.has_illiquid_collateral``
#: (WP5 managing-agent decision). Gated funds, unlisted holdings and structured
#: products share the same problem: no reliable daily price and no reliable
#: same-day exit.
ILLIQUID_ASSET_CLASSES: frozenset[AssetClass] = frozenset(
    {AssetClass.fund_gated, AssetClass.unlisted, AssetClass.structured_product}
)


class ActionType(str, Enum):
    """Rule action taxonomy (build_plan.md §2.4)."""

    flag = "flag"
    escalate = "escalate"
    set_floor = "set_floor"
    set_opening = "set_opening"
    require_cp = "require_cp"
    require_rep = "require_rep"
    note = "note"


class ConditionOp(str, Enum):
    """Leaf condition operators (build_plan.md §2.4)."""

    eq = "eq"
    neq = "neq"
    in_ = "in"
    not_in = "not_in"
    gt = "gt"
    gte = "gte"
    lt = "lt"
    lte = "lte"
    contains = "contains"
    is_null = "is_null"


class Severity(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class RequestOutcome(str, Enum):
    """Outcome of a counterparty request against the computed floor."""

    accepted_within_floor = "accepted_within_floor"
    below_floor_escalated = "below_floor_escalated"
    unacceptable_escalated = "unacceptable_escalated"


# ---------------------------------------------------------------------------
# Tier ordering: tighter == closer to preferred
# ---------------------------------------------------------------------------

#: Ordered tightest-first. ``preferred > acceptable > fallback > unacceptable``
#: in the sense of protection retained by the lender.
TIER_ORDER: tuple[Tier, ...] = (
    Tier.preferred,
    Tier.acceptable,
    Tier.fallback,
    Tier.unacceptable,
)

_TIER_RANK: dict[Tier, int] = {t: i for i, t in enumerate(TIER_ORDER)}


def tier_rank(tier: Tier | str) -> int:
    """Rank of ``tier``: 0 = preferred (tightest) .. 3 = unacceptable (loosest)."""
    return _TIER_RANK[Tier(tier)]


def is_tighter(a: Tier | str, b: Tier | str) -> bool:
    """True if ``a`` is strictly tighter (closer to preferred) than ``b``."""
    return tier_rank(a) < tier_rank(b)


def is_tighter_or_equal(a: Tier | str, b: Tier | str) -> bool:
    """True if ``a`` is tighter than or the same as ``b``."""
    return tier_rank(a) <= tier_rank(b)


def tighter(a: Tier | str, b: Tier | str) -> Tier:
    """Return whichever of ``a`` and ``b`` is tighter. Rules only ever tighten."""
    return Tier(a) if tier_rank(a) <= tier_rank(b) else Tier(b)


def looser(a: Tier | str, b: Tier | str) -> Tier:
    """Return whichever of ``a`` and ``b`` is looser. Provided for symmetry."""
    return Tier(a) if tier_rank(a) >= tier_rank(b) else Tier(b)


# ---------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------


class SBLModel(BaseModel):
    """Base model: unknown keys are a hard error everywhere."""

    model_config = ConfigDict(extra="forbid", use_enum_values=False)


class Reviewable(SBLModel):
    """Mixin for anything carrying review status.

    ``reviewed`` requires a named reviewer. The schema permits ``reviewed``
    (Stuart sets it); the validator only enforces that it is attributable.
    """

    status: Status
    reviewed_by: Optional[str] = None
    last_reviewed: Optional[date] = None

    @model_validator(mode="after")
    def _reviewed_needs_reviewer(self) -> "Reviewable":
        if self.status is Status.reviewed and not self.reviewed_by:
            raise ValueError(
                "status 'reviewed' requires a non-null 'reviewed_by' "
                "(only a named human reviewer may promote an entry to reviewed)"
            )
        return self


# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------


class Source(SBLModel):
    """A source reference. No invented law: ``verified`` is honest, not decorative."""

    ref: str = Field(..., min_length=1, description="Short label for the source")
    type: SourceType
    url: Optional[str] = Field(
        default=None,
        description="URL if there is one. Never fabricate; leave null instead.",
    )
    retrieved: Optional[date] = Field(
        default=None, description="Date the source was actually opened"
    )
    reliability: Reliability
    verified: bool = Field(
        default=False,
        description="True only if the writer opened the source and checked the statement",
    )
    note: Optional[str] = Field(
        default=None, description="What this source supports"
    )


# ---------------------------------------------------------------------------
# Clause
# ---------------------------------------------------------------------------


class Position(SBLModel):
    """A concedable tier: draft lender-side clause language plus why."""

    text: str = Field(..., min_length=1)
    rationale: str = Field(..., min_length=1)
    conditions: list[str] = Field(
        default_factory=list,
        description="Conditions that must hold before conceding to this tier",
    )
    approval: Optional[str] = Field(
        default=None, description="Who must sign off a concession to this tier"
    )


class UnacceptablePosition(SBLModel):
    """The walk-away line. A description, not drafting: the lender never drafts it.

    Has no ``conditions`` and no ``approval`` because nobody may agree it.
    """

    text: str = Field(..., min_length=1)
    rationale: str = Field(..., min_length=1)


class Positions(SBLModel):
    """The four-tier ladder."""

    preferred: Position
    acceptable: Position
    fallback: Position
    unacceptable: UnacceptablePosition


class Clause(Reviewable):
    """One negotiable clause (``playbook/clauses/NN_<id>.yaml``).

    A ``stub`` needs only ``id``, ``title``, ``category`` and ``lender_objective``.
    A ``draft`` or ``reviewed`` entry must also carry ``document``,
    ``risk_rating``, ``positions``, ``default_floor`` and at least one source.
    """

    id: str = Field(..., pattern=r"^[a-z][a-z0-9_]*$")
    title: str = Field(..., min_length=1)
    category: Category
    lender_objective: str = Field(..., min_length=1)

    document: Optional[Document] = None
    risk_rating: Optional[RiskRating] = None
    counterparty_asks: list[str] = Field(default_factory=list)
    positions: Optional[Positions] = None
    default_floor: Optional[Tier] = None
    escalation_triggers: list[str] = Field(default_factory=list)
    depends_on: list[str] = Field(default_factory=list)
    jurisdiction_notes: dict[str, str] = Field(default_factory=dict)
    regulatory_flags: list[str] = Field(default_factory=list)
    not_automated: list[str] = Field(default_factory=list)
    sources: list[Source] = Field(default_factory=list)

    @model_validator(mode="after")
    def _completeness_by_status(self) -> "Clause":
        if self.status is Status.stub:
            return self
        missing = [
            name
            for name in ("document", "risk_rating", "positions", "default_floor")
            if getattr(self, name) is None
        ]
        if not self.sources:
            missing.append("sources")
        if missing:
            raise ValueError(
                f"clause '{self.id}' has status '{self.status.value}' but is missing "
                f"required field(s): {', '.join(missing)}. Either complete the entry "
                f"or set status: stub."
            )
        return self

    @model_validator(mode="after")
    def _no_self_dependency(self) -> "Clause":
        if self.id in self.depends_on:
            raise ValueError(f"clause '{self.id}' lists itself in depends_on")
        return self


# ---------------------------------------------------------------------------
# Rule: condition tree + typed actions
# ---------------------------------------------------------------------------


class LeafCondition(SBLModel):
    """``{field, op, value}``. ``field`` is a dotted path into the Intake."""

    field: str = Field(..., min_length=1)
    op: ConditionOp
    value: Any = None

    @model_validator(mode="after")
    def _value_required_unless_is_null(self) -> "LeafCondition":
        if self.op is ConditionOp.is_null:
            return self
        if self.value is None:
            raise ValueError(
                f"condition on field '{self.field}' with op '{self.op.value}' "
                f"requires a 'value' (only op 'is_null' may omit it)"
            )
        if self.op in (ConditionOp.in_, ConditionOp.not_in) and not isinstance(
            self.value, list
        ):
            raise ValueError(
                f"condition on field '{self.field}' with op '{self.op.value}' "
                f"requires a list 'value'"
            )
        return self


class AllCondition(SBLModel):
    all: list["Condition"] = Field(..., min_length=1)


class AnyCondition(SBLModel):
    any: list["Condition"] = Field(..., min_length=1)


class NotCondition(SBLModel):
    not_: "Condition" = Field(..., alias="not")
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


def _condition_kind(value: Any) -> str:
    """Tag a condition node by its shape, so errors name one branch not four."""
    if isinstance(value, AllCondition):
        return "cond_all"
    if isinstance(value, AnyCondition):
        return "cond_any"
    if isinstance(value, NotCondition):
        return "cond_not"
    if isinstance(value, LeafCondition):
        return "cond_leaf"
    if isinstance(value, dict):
        for key in ("all", "any", "not"):
            if key in value:
                return f"cond_{key}"
    return "cond_leaf"


Condition = Annotated[
    Union[
        Annotated[AllCondition, Tag("cond_all")],
        Annotated[AnyCondition, Tag("cond_any")],
        Annotated[NotCondition, Tag("cond_not")],
        Annotated[LeafCondition, Tag("cond_leaf")],
    ],
    Discriminator(_condition_kind),
]

AllCondition.model_rebuild()
AnyCondition.model_rebuild()
NotCondition.model_rebuild()


class FlagAction(SBLModel):
    action: Literal[ActionType.flag]
    flag: str = Field(..., min_length=1)
    severity: Severity
    message: str = Field(..., min_length=1)


class EscalateAction(SBLModel):
    action: Literal[ActionType.escalate]
    to: str = Field(..., min_length=1)
    reason: str = Field(..., min_length=1)
    clause: Optional[str] = None


class SetFloorAction(SBLModel):
    action: Literal[ActionType.set_floor]
    clause: str = Field(..., min_length=1)
    tier: Tier


class SetOpeningAction(SBLModel):
    action: Literal[ActionType.set_opening]
    clause: str = Field(..., min_length=1)
    tier: Tier


class RequireCpAction(SBLModel):
    action: Literal[ActionType.require_cp]
    clause: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


class RequireRepAction(SBLModel):
    action: Literal[ActionType.require_rep]
    clause: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


class NoteAction(SBLModel):
    action: Literal[ActionType.note]
    clause: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


Action = Annotated[
    Union[
        FlagAction,
        EscalateAction,
        SetFloorAction,
        SetOpeningAction,
        RequireCpAction,
        RequireRepAction,
        NoteAction,
    ],
    Field(discriminator="action"),
]

#: Action types that name a clause id in a ``clause`` key.
CLAUSE_TARGETING_ACTIONS: tuple[type[SBLModel], ...] = (
    SetFloorAction,
    SetOpeningAction,
    RequireCpAction,
    RequireRepAction,
    NoteAction,
)


class Rule(Reviewable):
    """One rule (``playbook/rules/rules.yaml``)."""

    id: str = Field(..., pattern=r"^[A-Za-z0-9_]+$")
    title: str = Field(..., min_length=1)
    priority: int = Field(
        default=100, description="Lower runs first; affects log ordering only"
    )
    when: Condition
    then: list[Action] = Field(..., min_length=1)
    rationale: str = Field(..., min_length=1)
    sources: list[Source] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Regulatory flag
# ---------------------------------------------------------------------------


class Flag(Reviewable):
    """A regulatory or commercial flag definition."""

    id: str = Field(..., pattern=r"^[a-z][a-z0-9_]*$")
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trigger_summary: str = Field(..., min_length=1)
    who_decides: str = Field(..., min_length=1)
    sources: list[Source] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Jurisdiction overlay (fields per build_plan.md §6, WP7)
# ---------------------------------------------------------------------------


class Jurisdiction(Reviewable):
    """One jurisdiction overlay file (``playbook/jurisdictions/*.yaml``)."""

    id: str = Field(..., pattern=r"^[a-z][a-z0-9_]*$")
    name: str = Field(..., min_length=1)
    creation: str = Field(..., min_length=1)
    registration_filing: str = Field(..., min_length=1)
    perfection_depends_on: str = Field(..., min_length=1)
    enforcement_route: str = Field(..., min_length=1)
    financial_collateral_regime: str = Field(..., min_length=1)
    governing_law_of_intermediated_securities: str = Field(..., min_length=1)
    practical_notes: str = Field(..., min_length=1)
    sources: list[Source] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Intake
# ---------------------------------------------------------------------------


class Borrower(SBLModel):
    type: BorrowerType
    domicile: str = Field(..., pattern=r"^[A-Z]{2}$", description="ISO 3166-1 alpha-2")
    natural_person: bool
    declared_high_net_worth: Optional[bool] = Field(
        default=None, description="Individuals only; null where not applicable"
    )
    business_purpose_declared: Optional[bool] = None


class Pledgor(SBLModel):
    """The collateral provider. Where ``same_as_borrower``, the other fields are null."""

    same_as_borrower: bool
    type: Optional[BorrowerType] = None
    domicile: Optional[str] = Field(default=None, pattern=r"^[A-Z]{2}$")
    natural_person: Optional[bool] = None
    is_pdmr_of_pledged_issuer: bool = False

    @model_validator(mode="after")
    def _third_party_needs_details(self) -> "Pledgor":
        if not self.same_as_borrower:
            missing = [
                n
                for n in ("type", "domicile", "natural_person")
                if getattr(self, n) is None
            ]
            if missing:
                raise ValueError(
                    "pledgor.same_as_borrower is false, so a third-party pledgor must "
                    f"give: {', '.join(missing)}"
                )
        return self


class Facility(SBLModel):
    type: FacilityType
    purpose: Purpose
    amount: float = Field(..., gt=0)
    currency: str = Field(..., pattern=r"^[A-Z]{3}$", description="ISO 4217")
    benchmark: Benchmark
    other_facilities_with_lender: bool = False


class CompositionItem(SBLModel):
    """One asset-class line of the collateral, as a percentage of lending value."""

    asset_class: AssetClass
    pct: float = Field(..., ge=0, le=100)
    single_name_max_pct: Optional[float] = Field(
        default=None,
        ge=0,
        le=100,
        description="Largest single issuer exposure within this class",
    )
    issuer_restricted: bool = Field(
        default=False, description="Lock-ups, control stock, and the like"
    )


class Collateral(SBLModel):
    governing_law: GoverningLaw
    custodian_location: str = Field(..., pattern=r"^[A-Z]{2}$")
    lender_is_custodian: bool
    currencies: list[str] = Field(..., min_length=1)
    composition: list[CompositionItem] = Field(..., min_length=1)

    @field_validator("currencies")
    @classmethod
    def _currency_codes(cls, v: list[str]) -> list[str]:
        for c in v:
            if not (isinstance(c, str) and len(c) == 3 and c.isupper()):
                raise ValueError(
                    f"collateral currency '{c}' is not an ISO 4217 three-letter code"
                )
        return v

    @model_validator(mode="after")
    def _composition_sums(self) -> "Collateral":
        total = sum(item.pct for item in self.composition)
        if total > 100 + 1e-9:
            raise ValueError(
                f"collateral composition percentages sum to {total:g}, which exceeds 100"
            )
        return self


class CounterpartyRequest(SBLModel):
    """An optional counterparty ask against a clause: a tier, free text, or both."""

    tier: Optional[Tier] = None
    text: Optional[str] = None

    @model_validator(mode="after")
    def _at_least_one(self) -> "CounterpartyRequest":
        if self.tier is None and not self.text:
            raise ValueError("a counterparty request must give 'tier', 'text', or both")
        return self


class Derived(SBLModel):
    """Facts computed from the intake, for use by rules as ``derived.*``."""

    max_single_name_pct: float = Field(
        ...,
        description="Largest single_name_max_pct across composition lines; 0 if none given",
    )
    has_real_estate: bool = Field(
        ...,
        description=(
            "True if any composition line is asset_class real_estate with pct > 0"
        ),
    )
    currency_mismatch: bool = Field(
        ...,
        description="True if any collateral currency differs from the facility currency",
    )
    third_party_security: bool = Field(
        ..., description="True if the pledgor is not the borrower"
    )
    any_natural_person_pledgor: bool = Field(
        ..., description="True if the effective collateral provider is a natural person"
    )
    any_issuer_restricted: bool = Field(
        ...,
        description=(
            "True if any composition line is marked issuer_restricted "
            "(lock-ups, control stock and the like)"
        ),
    )
    has_illiquid_collateral: bool = Field(
        ...,
        description=(
            "True if any composition line with pct > 0 is fund_gated, unlisted or "
            "structured_product"
        ),
    )


class Intake(SBLModel):
    """A deal (``deals/*.yaml``). Synthetic only."""

    deal_id: str = Field(..., pattern=r"^[A-Za-z0-9_]+$")
    description: str = Field(..., min_length=1)
    borrower: Borrower
    pledgor: Pledgor
    guarantor_present: bool = False
    facility: Facility
    collateral: Collateral
    counterparty_requests: dict[str, CounterpartyRequest] = Field(default_factory=dict)

    # -- derived ------------------------------------------------------------

    @computed_field  # type: ignore[prop-decorator]
    @property
    def derived(self) -> Derived:
        """Computed facts the rules may reference as ``derived.*``.

        Definitions (fixed in WP1, relied on by WP5):

        * ``max_single_name_pct`` — maximum of the non-null ``single_name_max_pct``
          values across composition lines; ``0.0`` when none is given.
        * ``has_real_estate`` — any composition line has ``asset_class: real_estate``
          **and** ``pct > 0``. (Changed in WP5: a real-estate line at zero percent
          is not real-estate collateral, and R09 is a hard stop.)
        * ``currency_mismatch`` — any collateral currency differs from the facility
          currency (so a GBP facility against [GBP, USD] collateral is a mismatch).
        * ``third_party_security`` — ``pledgor.same_as_borrower`` is false.
        * ``any_natural_person_pledgor`` — the effective collateral provider is a
          natural person: the borrower where the pledgor is the borrower, otherwise
          the third-party pledgor.
        * ``any_issuer_restricted`` — any composition line is ``issuer_restricted``.
          (Added in WP5 for rule R08; percentage is not considered, because a
          restriction on any pledged line constrains enforcement.)
        * ``has_illiquid_collateral`` — any composition line with ``pct > 0`` is
          ``fund_gated``, ``unlisted`` or ``structured_product``. (Added in WP5 for
          rule R15.)
        """
        singles = [
            item.single_name_max_pct
            for item in self.collateral.composition
            if item.single_name_max_pct is not None
        ]
        third_party = not self.pledgor.same_as_borrower
        return Derived(
            max_single_name_pct=max(singles) if singles else 0.0,
            has_real_estate=any(
                item.asset_class is AssetClass.real_estate and item.pct > 0
                for item in self.collateral.composition
            ),
            currency_mismatch=any(
                c != self.facility.currency for c in self.collateral.currencies
            ),
            third_party_security=third_party,
            any_natural_person_pledgor=(
                bool(self.pledgor.natural_person)
                if third_party
                else self.borrower.natural_person
            ),
            any_issuer_restricted=any(
                item.issuer_restricted for item in self.collateral.composition
            ),
            has_illiquid_collateral=any(
                item.asset_class in ILLIQUID_ASSET_CLASSES and item.pct > 0
                for item in self.collateral.composition
            ),
        )


# ---------------------------------------------------------------------------
# Run result (build_plan.md §2.5)
# ---------------------------------------------------------------------------


class LadderRung(SBLModel):
    """One tier of a clause's position ladder, copied into the run result.

    Added in WP5 so the Markdown renderer can work from the run JSON alone
    (build_plan.md §2.5: "the renderer has no access to anything else").
    The ``unacceptable`` rung always carries an empty ``conditions`` and a null
    ``approval``: nobody may agree it.
    """

    tier: Tier
    text: str
    rationale: str
    conditions: list[str] = Field(default_factory=list)
    approval: Optional[str] = None


class ClauseResult(SBLModel):
    """Per-clause outcome of a run.

    ``id``, ``opening``, ``floor``, ``status``, ``rules_applied``, ``cps``,
    ``reps`` and ``notes`` are the WP1 contract. Everything else is copied from
    the clause entry by the engine so that the renderer needs nothing but this
    object.

    Every string in ``cps``, ``reps`` and ``notes`` is prefixed with the id of
    the rule that added it, in square brackets followed by one space, e.g.
    ``"[R07_pdmr_pledged_issuer] Compliance sign-off on insider status."``.
    """

    id: str
    title: str
    category: Category
    document: Optional[Document] = None
    risk_rating: Optional[RiskRating] = None
    status: Status
    opening: Tier
    floor: Tier
    opening_text: Optional[str] = None
    opening_rationale: Optional[str] = None
    ladder: list[LadderRung] = Field(
        default_factory=list,
        description=(
            "All four tiers in order preferred -> unacceptable. Empty for a stub "
            "clause, which has no positions yet."
        ),
    )
    jurisdiction_note: Optional[str] = Field(
        default=None,
        description="The clause's note for this deal's governing law, or null",
    )
    rules_applied: list[str] = Field(default_factory=list)
    cps: list[str] = Field(default_factory=list)
    reps: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    escalation_triggers: list[str] = Field(default_factory=list)
    not_automated: list[str] = Field(default_factory=list)


class FlagResult(SBLModel):
    """A flag raised on a run."""

    id: str
    severity: Severity
    message: str
    rule_id: str
    who_decides: Optional[str] = None


class Escalation(SBLModel):
    """A hard stop. Any escalation makes the run exit code 2."""

    rule_id: str
    to: str
    reason: str
    clause: Optional[str] = None


class CounterpartyRequestOutcome(SBLModel):
    """How a counterparty request landed against the computed floor."""

    clause: str
    requested_tier: Optional[Tier] = None
    requested_text: Optional[str] = None
    floor: Optional[Tier] = None
    outcome: RequestOutcome


class JurisdictionSummary(SBLModel):
    """The jurisdiction overlay for this deal's governing law, copied into the run.

    Added in WP5 so the renderer needs no access to the library. ``sources`` are
    deliberately not copied: the run result records the library hash, and the
    overlay file is the place to read its sources.
    """

    id: str
    name: str
    creation: str
    registration_filing: str
    perfection_depends_on: str
    enforcement_route: str
    financial_collateral_regime: str
    governing_law_of_intermediated_securities: str
    practical_notes: str
    status: Status


class RunResult(SBLModel):
    """The complete, self-contained record of one run.

    The Markdown renderer reads this object and nothing else; that is what makes
    the trace complete.

    ``run_id`` and ``timestamp`` are the only non-deterministic fields. Same
    library plus same intake gives the same result everywhere else, byte for
    byte. ``run_id`` is the first twelve hex characters of
    ``sha256(library_hash + intake_hash + timestamp)``.
    """

    run_id: str
    timestamp: str
    library_hash: str
    intake_hash: str
    deal_id: str
    description: str
    governing_law: GoverningLaw
    intake: Intake
    status_summary: dict[str, int] = Field(
        default_factory=dict,
        description="Counts of reviewed / draft / stub over the clauses in this run",
    )
    jurisdiction: Optional[JurisdictionSummary] = Field(
        default=None,
        description="The overlay for governing_law; null when governing_law is 'other'",
    )
    clauses: list[ClauseResult] = Field(default_factory=list)
    flags: list[FlagResult] = Field(default_factory=list)
    escalations: list[Escalation] = Field(default_factory=list)
    counterparty_request_outcomes: list[CounterpartyRequestOutcome] = Field(
        default_factory=list
    )
    not_automated: list[str] = Field(
        default_factory=list,
        description=(
            "Deduplicated, sorted union of not_automated items from every clause "
            "this run touched"
        ),
    )
    exit_code: int = Field(
        default=0, description="2 if there is any escalation, otherwise 0"
    )


__all__ = [
    # enums
    "Category",
    "Document",
    "RiskRating",
    "Tier",
    "Status",
    "SourceType",
    "Reliability",
    "BorrowerType",
    "FacilityType",
    "Purpose",
    "Benchmark",
    "GoverningLaw",
    "AssetClass",
    "ActionType",
    "ConditionOp",
    "Severity",
    "RequestOutcome",
    "ILLIQUID_ASSET_CLASSES",
    # tier helpers
    "TIER_ORDER",
    "tier_rank",
    "is_tighter",
    "is_tighter_or_equal",
    "tighter",
    "looser",
    # models
    "SBLModel",
    "Reviewable",
    "Source",
    "Position",
    "UnacceptablePosition",
    "Positions",
    "Clause",
    "LeafCondition",
    "AllCondition",
    "AnyCondition",
    "NotCondition",
    "Condition",
    "FlagAction",
    "EscalateAction",
    "SetFloorAction",
    "SetOpeningAction",
    "RequireCpAction",
    "RequireRepAction",
    "NoteAction",
    "Action",
    "CLAUSE_TARGETING_ACTIONS",
    "Rule",
    "Flag",
    "Jurisdiction",
    "Borrower",
    "Pledgor",
    "Facility",
    "CompositionItem",
    "Collateral",
    "CounterpartyRequest",
    "Derived",
    "Intake",
    "LadderRung",
    "JurisdictionSummary",
    "ClauseResult",
    "FlagResult",
    "Escalation",
    "CounterpartyRequestOutcome",
    "RunResult",
]
