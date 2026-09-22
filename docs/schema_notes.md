# Schema notes — the frozen data contract

Written at the end of WP1. This is the contract every later work package builds on.
Source of truth is `src/sbl/models.py`; JSON schemas are exported to
`playbook/schema/` by `python scripts/export_schemas.py`. If a model changes after
WP1, note it in the hand-off and rerun all tests (`build_plan.md` §6, WP1 "Freeze").

All positions are drafted from the **lender's** (private bank's) side. Everything in
the repository is synthetic. Nothing here is legal advice.

---

## 1. Tier semantics: tighten only

| Tier | Meaning | Who may agree it |
|---|---|---|
| `preferred` | Lender's opening position | Deal lawyer, by default |
| `acceptable` | Routine concession; no loss of core protection | Deal lawyer, no escalation |
| `fallback` | Concession that costs real protection; only with the listed conditions satisfied | Named approver in the entry; concession logged |
| `unacceptable` | Walk-away line | Nobody. Any request here is a hard escalation |

Two derived values per clause per deal:

* **floor** — the lowest tier the deal lawyer may concede to without escalation.
* **opening** — the tier the markup proposes first.

**Rules may only move both upward (tighter).** "Tighter" means closer to `preferred`.

`TIER_ORDER = (preferred, acceptable, fallback, unacceptable)` and
`tier_rank()` returns `0..3`, so a *lower* rank is tighter. Use the helpers rather
than comparing strings:

```python
from sbl.models import tier_rank, is_tighter, is_tighter_or_equal, tighter, looser

tighter("fallback", "acceptable")   # -> Tier.acceptable
is_tighter("preferred", "fallback") # -> True
```

Because every action is `result = tighter(current, proposed)`, the outcome does not
depend on the order rules run in. Rule order affects the log only. The engine (WP5)
must preserve this property; there is a reversed-order property test in its
acceptance criteria.

---

## 2. Status discipline

Every clause, rule, jurisdiction file and flag carries:

* `status`: `stub` | `draft` | `reviewed`
* `reviewed_by`: string or null
* `last_reviewed`: date or null

Agents write `stub` or `draft` only. Only a named human sets `reviewed`. The schema
accepts the value `reviewed`, but a model validator rejects `reviewed` with a null
`reviewed_by`: a review has to be attributable. The markup generator prints the
status of every position it emits, so an unreviewed position is visibly labelled.

**Completeness follows status.** A `stub` clause needs only `id`, `title`,
`category`, `lender_objective`. A `draft` or `reviewed` clause must also have
`document`, `risk_rating`, `positions`, `default_floor` and at least one `sources`
entry. Setting `status: draft` on an incomplete entry is a load-time error that
names the missing fields.

---

## 3. Models and their fields

Every model sets `extra="forbid"`. An unknown key anywhere is a hard error, never a
silently ignored field. That is deliberate: a typo in `single_name_max_pct` must not
read as "no concentration".

### `Source`
`ref`, `type`, `url?`, `retrieved?`, `reliability`, `verified`, `note?`

`url` and `retrieved` are optional so that a placeholder source can be honest rather
than fabricated. Never invent a citation or URL: leave it null and mark
`verified: false`.

### `Position` (preferred / acceptable / fallback)
`text`, `rationale`, `conditions[]`, `approval?`

### `UnacceptablePosition`
`text`, `rationale`

A separate model on purpose: the walk-away tier has **no** `conditions` and **no**
`approval`, because nobody may agree it. `text` is a description of the position the
lender will not accept, not drafting.

### `Positions`
`preferred`, `acceptable`, `fallback`, `unacceptable` — all four required.

### `Clause` (`playbook/clauses/NN_<id>.yaml`, one per file)
`id`, `title`, `category`, `lender_objective`, `document?`, `risk_rating?`,
`counterparty_asks[]`, `positions?`, `default_floor?`, `escalation_triggers[]`,
`depends_on[]`, `jurisdiction_notes{}`, `regulatory_flags[]`, `not_automated[]`,
`sources[]`, `status`, `reviewed_by?`, `last_reviewed?`

`id` is snake_case and stable; the numeric filename prefix is ordering only and is
not part of the identity. `depends_on` and `regulatory_flags` and the keys of
`jurisdiction_notes` are all resolved at load time.

### `Rule` (`playbook/rules/rules.yaml`, a list)
`id`, `title`, `priority`, `when`, `then[]`, `rationale`, `sources[]`, `status`,
`reviewed_by?`, `last_reviewed?`

`priority` is lower-runs-first and affects log ordering only, never the result.

#### Condition grammar (`when`)
Nestable. Four node shapes:

```yaml
all: [ <condition>, ... ]
any: [ <condition>, ... ]
not: <condition>
{ field: <dotted path>, op: <op>, value: <any> }
```

`op` is one of `eq`, `neq`, `in`, `not_in`, `gt`, `gte`, `lt`, `lte`, `contains`,
`is_null`. `value` is required for every op except `is_null`, and must be a list for
`in` / `not_in`.

`field` is a dotted path into the `Intake` model, **including `derived.*`**. The
loader checks every leaf against the model at load time: an unknown field is a hard
error naming the file, line and rule id — never a silent false. Use
`sbl.loader.intake_field_paths()` to see the addressable set.

Container paths are addressable as well as leaves, so `contains` can be used against
a list (`collateral.currencies`). A list of objects also contributes its item fields
as a **projection**: `collateral.composition.asset_class` is an accepted path.
WP1 only accepts these paths; **WP5 must define and test their evaluation
semantics** (the natural reading is "the list of that field across all items", so
`{field: collateral.composition.asset_class, op: contains, value: fund_gated}` means
"any line is gated"). Until WP5 fixes that, prefer a `derived.*` field for anything
that needs to quantify over composition lines.

#### Action types (`then`)

| `action` | required keys | effect |
|---|---|---|
| `flag` | `flag`, `severity`, `message` | Adds a flag. `flag` must exist in `flags/regulatory_flags.yaml`. |
| `escalate` | `to`, `reason` (`clause` optional) | Hard stop. Run exit code is 2 if any escalation. |
| `set_floor` | `clause`, `tier` | Raises the floor. Never lowers. |
| `set_opening` | `clause`, `tier` | Raises the opening. Never lowers. |
| `require_cp` | `clause`, `text` | Appends a condition precedent to that clause's output. |
| `require_rep` | `clause`, `text` | Appends a representation/undertaking. |
| `note` | `clause`, `text` | Adds a drafting note. |

Actions are a discriminated union on `action`, so an unknown action type or a
missing required key is rejected with one clear message.

### `Flag` (`playbook/flags/regulatory_flags.yaml`, a list)
`id`, `name`, `description`, `trigger_summary`, `who_decides`, `sources[]`,
`status`, `reviewed_by?`, `last_reviewed?`

### `Jurisdiction` (`playbook/jurisdictions/<id>.yaml`, one per file)
`id`, `name`, `creation`, `registration_filing`, `perfection_depends_on`,
`enforcement_route`, `financial_collateral_regime`,
`governing_law_of_intermediated_securities`, `practical_notes`, `sources[]`,
`status`, `reviewed_by?`, `last_reviewed?`

The seven substantive fields are strings and are all required, so a jurisdiction file
cannot silently omit a question. A stub answers each with the literal `"stub"`.

### `Intake` (`deals/*.yaml`)
`deal_id`, `description`, `borrower`, `pledgor`, `guarantor_present`, `facility`,
`collateral`, `counterparty_requests{}`, plus computed `derived`.

* `Borrower`: `type`, `domicile` (ISO 3166-1 alpha-2), `natural_person`,
  `declared_high_net_worth?`, `business_purpose_declared?`
* `Pledgor`: `same_as_borrower`, `type?`, `domicile?`, `natural_person?`,
  `is_pdmr_of_pledged_issuer`. Where `same_as_borrower` is false, the other three
  become required.
* `Facility`: `type`, `purpose`, `amount` (> 0), `currency` (ISO 4217),
  `benchmark`, `other_facilities_with_lender`
* `Collateral`: `governing_law`, `custodian_location`, `lender_is_custodian`,
  `currencies[]`, `composition[]`
* `CompositionItem`: `asset_class`, `pct` (0..100), `single_name_max_pct?` (0..100
  or null), `issuer_restricted`
* `CounterpartyRequest`: `tier?`, `text?` — at least one must be given.

Composition percentages must each be 0..100 and must sum to **no more than 100**.
They are percentages of lending value, not of market value.

Note that "is the borrower a consumer?" is **not** an intake field. It is a
conclusion. The intake captures facts (`natural_person`, `domicile`,
`declared_high_net_worth`, `business_purpose_declared`); a rule raises the
`consumer_credit` flag; the determination itself is in the not-automated register.

### `Derived` — computed, addressable as `derived.*`

| field | definition |
|---|---|
| `max_single_name_pct` | Maximum of the non-null `single_name_max_pct` values across composition lines. `0.0` when none is given. |
| `has_real_estate` | Any composition line has `asset_class: real_estate` **and** `pct > 0`. **Changed in WP5** (was: whatever its percentage). |
| `currency_mismatch` | Any collateral currency differs from `facility.currency`. A GBP facility against `[GBP, USD]` collateral **is** a mismatch. Unchanged in WP5. |
| `third_party_security` | `pledgor.same_as_borrower` is false. |
| `any_natural_person_pledgor` | The effective collateral provider is a natural person: the borrower where the pledgor is the borrower, otherwise the third-party pledgor. |
| `any_issuer_restricted` | **Added in WP5.** Any composition line has `issuer_restricted: true`. Percentage is not considered: a restriction on any pledged line constrains enforcement. Used by R08. |
| `has_illiquid_collateral` | **Added in WP5.** Any composition line with `pct > 0` has `asset_class` in `fund_gated`, `unlisted`, `structured_product` (the set `models.ILLIQUID_ASSET_CLASSES`). Used by R15. |

These definitions are fixed. Rules depend on them, so changing one changes rule
behaviour silently — treat a change as a contract change. The two WP5 additions
replace the "projection over `collateral.composition`" approach that WP1 left
open (WP1 hand-off, lowest-confidence item 1): projected paths still evaluate
(see §3.1 below), but rules that need to quantify over composition lines use a
derived boolean, because a named boolean is testable and a projection is not
obvious in a YAML condition.

### `RunResult` (`runs/audit.jsonl`, one JSON line per run)

Extended in WP5 so the Markdown renderer can work from the run JSON alone
(`build_plan.md` §2.5: "the renderer has no access to anything else"). WP1
fields are unchanged; the new ones are marked.

`run_id`, `timestamp`, `library_hash`, `intake_hash`, `deal_id` *(new)*,
`description` *(new)*, `governing_law` *(new)*, `intake` (echoed),
`status_summary` *(new)*, `jurisdiction?` *(new)*, `clauses[]`, `flags[]`,
`escalations[]`, `counterparty_request_outcomes[]`, `not_automated[]` *(new)*,
`exit_code` *(new)*.

* `status_summary`: `{reviewed: int, draft: int, stub: int}` over the clauses in
  this run.
* `jurisdiction`: a `JurisdictionSummary` for `governing_law`, or `null` when the
  governing law is `other`.
* `not_automated`: deduplicated, sorted union of the `not_automated` items of
  every clause this run touched. A clause counts as touched when any rule left an
  entry in its `rules_applied`, or an escalation names it, or one of its
  `regulatory_flags` was raised on this run.
* `exit_code`: `2` if there is any escalation, otherwise `0`.
* `run_id` and `timestamp` are the **only** non-deterministic fields.
  `run_id` = first 12 hex characters of
  `sha256(library_hash + intake_hash + timestamp)`.
  `intake_hash` = `sha256` of `Intake.model_dump_json()` (derived fields
  included), so comments and formatting in the deal file do not change it.

* `ClauseResult`: `id`, `title` *(new)*, `category` *(new)*, `document?` *(new)*,
  `risk_rating?` *(new)*, `status`, `opening`, `floor`, `opening_text?` *(new)*,
  `opening_rationale?` *(new)*, `ladder[]` *(new)*, `jurisdiction_note?` *(new)*,
  `rules_applied[]`, `cps[]`, `reps[]`, `notes[]`, `escalation_triggers[]`
  *(new)*, `not_automated[]` *(new)*.
  `ladder` holds all four tiers in order `preferred → unacceptable` and is empty
  for a `stub` clause. `jurisdiction_note` is the clause's note for the deal's
  governing law, or null.
* `LadderRung` *(new)*: `tier`, `text`, `rationale`, `conditions[]`, `approval?`.
  The `unacceptable` rung always has empty `conditions` and a null `approval`.
* `JurisdictionSummary` *(new)*: `id`, `name`, `creation`,
  `registration_filing`, `perfection_depends_on`, `enforcement_route`,
  `financial_collateral_regime`,
  `governing_law_of_intermediated_securities`, `practical_notes`, `status`.
  Sources are deliberately not copied: the run records the library hash, and the
  overlay file is where the sources live.
* `FlagResult`: `id`, `severity`, `message`, `rule_id`, `who_decides?` —
  `who_decides` is populated by the engine from the flag definition.
* `Escalation`: `rule_id`, `to`, `reason`, `clause?`
* `CounterpartyRequestOutcome`: `clause`, `requested_tier?`, `requested_text?`,
  `floor?`, `outcome` — outcome is `accepted_within_floor`,
  `below_floor_escalated` or `unacceptable_escalated`.

The Markdown renderer (WP6) reads `RunResult` and nothing else. That constraint is
what makes the trace complete: if a sentence is in the markup, it came from this
object, and this object names the library hash that produced it.

`RunResult`'s JSON schema is exported to `playbook/schema/run_result.schema.json`
alongside the three WP1 schemas.

### 3.1 Engine conventions (WP5)

These are output conventions, not model fields, but a reader of a run JSON needs
them.

**Rule id prefixes.** Every string the engine appends to a clause's `cps`,
`reps` or `notes` is prefixed with the id of the rule that produced it, in
square brackets followed by one space:

```
[R07_pdmr_pledged_issuer] Compliance sign-off on the pledgor's insider status...
[R16] Counterparty request accepted within floor at tier 'acceptable'...
```

The id is the rule's id exactly as it appears in `playbook/rules/rules.yaml`, or
the literal `R16` for the built-in counterparty-request rule. A parser takes
everything between the leading `[` and the first `] `.

**`rules_applied`.** A bare rule id (`R06_concentration`) means the rule changed
something on that clause: it tightened the floor or the opening, added a CP, a
rep or a note, or raised an escalation naming the clause. The suffix
`" (no change)"` (`engine.NO_CHANGE_SUFFIX`) means the rule named the clause but
changed nothing — typically a `set_floor` to a tier another rule had already
reached. Both appear so the log answers "did this rule look at this clause?" as
well as "did it move it?". A rule appears at most once per clause.

**Order.** The engine sorts rules by `(priority, id)` whatever order they arrive
in, so file order can never change a result, and the order of `cps` / `reps` /
`notes` within a clause is that canonical rule order. R16 runs after every YAML
rule, because it scores requests against the floor those rules produced.

**Stub clauses.** A clause with no `default_floor` (that is, a `stub`) is given
floor `fallback` and opening `preferred`. Its `status: stub` travels into the
run result, so the reader can see the tiers are placeholders.

**Nulls.** A null on the left of a leaf condition makes every operator `False`
except `is_null`. "We do not know" must not read as "the rule fires", and must
not read as an error either.

**Projection.** A dotted path that crosses a list of models projects across it:
`collateral.composition.asset_class` evaluates to the list of that field across
every composition line, so `{op: contains, value: fund_gated}` means "any line
is gated".

---

## 4. Loading and cross-references

`sbl.loader.load_library(root)` returns a `Library` with `clauses` (dict by id),
`rules` (list), `jurisdictions` (dict by id), `flags` (dict by id), `library_hash`
and `files`. It raises `LibraryError` carrying **every** problem found, not just the
first, so one `sbl validate` shows the whole list.

Checked at load time:

1. every file parses and validates against its model;
2. no duplicate ids;
3. rule `flag` actions name a defined flag;
4. rule clause-targeting actions name a defined clause;
5. clause `regulatory_flags` name defined flags;
6. clause `depends_on` name defined clauses;
7. clause `jurisdiction_notes` keys name defined jurisdictions;
8. every rule condition `field` is an addressable Intake path.

Errors carry the relative file path and, for rules and flags, the line of the entry's
`id` (located through YAML node marks, so quoting does not matter).

`library_hash` is `sha256` over the sorted `(relative path, file bytes)` of every
YAML file under `playbook/`, with lengths mixed in so that path and content cannot be
confused. It goes in every audit line, so any output traces to the exact library
version that produced it.

---

## 5. Things a later agent should not do

* Do not add a field to `Intake` without updating this file — rules address it by
  dotted path and the loader will accept the new path silently.
* Do not relax `extra="forbid"`.
* Do not add an action that can loosen a tier. Every action is `tighter(...)`.
* Do not set `status: reviewed` or fill `reviewed_by`. That is Stuart's.
* Do not write a `sources` entry with a URL you have not opened.
