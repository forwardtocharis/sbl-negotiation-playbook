# Hand-off: WP0 (repo scaffold) and WP1 (schemas, models, loader)

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP0 and WP1.
Everything in the repository is synthetic. Nothing written here is legal advice.
No entry has been set to `reviewed`; no `verified: true` source exists anywhere.

---

## 1. Acceptance output (pasted verbatim)

### WP0 — `pip install -e .` succeeds

Run in a project-local virtualenv (`.venv/`, gitignored). See "Deviations" §4.1 —
installing into the system Python failed on a Windows permissions error unrelated to
the package.

```
$ python -m venv .venv
$ .venv/Scripts/python.exe -m pip install -e ".[test]"
...
Building editable for sbl (pyproject.toml): finished with status 'done'
Successfully built sbl
Installing collected packages: typing-extensions, pyyaml, pygments, pluggy, packaging,
  iniconfig, colorama, annotated-types, typing-inspection, pytest, pydantic-core, pydantic, sbl
Successfully installed annotated-types-0.8.0 colorama-0.4.6 iniconfig-2.3.0 packaging-26.3
  pluggy-1.6.0 pydantic-2.13.5 pydantic-core-2.46.5 pygments-2.21.0 pytest-9.1.1
  pyyaml-6.0.3 sbl-0.1.0 typing-extensions-4.16.0 typing-inspection-0.4.4
```

### WP0 — `python -m sbl --help` prints usage

```
$ python -m sbl --help
usage: sbl [-h] [--root ROOT] command ...

SBL Negotiation Playbook Demonstrator. Demonstrator built from public sources. Synthetic deals. Not legal advice. Not validated against any institution's policy.

positional arguments:
  command
    validate   Load and validate the playbook library
    run        Run a deal intake through the rules engine
    explain    Explain how one clause outcome was reached in a past run

options:
  -h, --help   show this help message and exit
  --root ROOT  Repository root holding playbook/ (default: found by walking up
               from cwd)
```

The `sbl` console script is also installed and works (`.venv/Scripts/sbl.exe validate`
gives identical output).

### WP1 — `sbl validate` exits 0 on the stub library

```
$ python -m sbl validate
OK: 24 clauses, 0 rules, 10 flags, 3 jurisdictions validated.
library_hash: 2bb077b8162abbd6094351ca30b7a7b30ecab21209d4a3cdf2a522ca3d893e58
exit code: 0
```

### WP1 — `sbl validate --summary` prints counts

```
$ python -m sbl validate --summary
OK: 24 clauses, 0 rules, 10 flags, 3 jurisdictions validated.
library_hash: 2bb077b8162abbd6094351ca30b7a7b30ecab21209d4a3cdf2a522ca3d893e58

kind              stub   draft  reviewed   total
------------------------------------------------
clauses             24       0         0      24
rules                0       0         0       0
flags               10       0         0      10
jurisdictions        3       0         0       3

Entries not marked 'reviewed' have not been checked by a named human reviewer.
exit code: 0
```

### WP1 — `pytest tests/test_schema_validation.py -q` green

```
$ pytest tests/test_schema_validation.py -q
.............................                                            [100%]
29 passed in 2.11s
```

### Placeholder subcommands exit 1

```
$ python -m sbl run deals/x.yaml
sbl run: not yet implemented
run exit=1
$ python -m sbl explain r1 c1
sbl explain: not yet implemented
explain exit=1
```

### The ten deliberate errors, with the message each produces

```
--- 01 unknown field path in rule condition ---
  playbook/rules/rules.yaml:2: rule 'RX01_unknown_field' condition references unknown intake field 'borrower.is_consumer'. Field must be a dotted path into the Intake model (including derived.*).

--- 02 unknown clause id in action ---
  playbook/rules/rules.yaml:2: rule 'RX02_unknown_clause' action 'set_floor' names unknown clause id 'margin_call_cure_period'

--- 03 unknown flag id ---
  playbook/rules/rules.yaml:2: rule 'RX03_unknown_flag' raises unknown flag id 'basel_iv_awareness'. Known flags: bank_secrecy_data, consumer_credit, emir_awareness, fca_safe_harbour_uncertain, financial_assistance_corporate_benefit, market_abuse, mifid_suitability, mortgage_regulation, prudential_awareness, restricted_securities

--- 04 composition > 100 ---
  tests/fixtures/invalid_intake_composition_over_100.yaml [D98]: field 'collateral': Value error, collateral composition percentages sum to 110, which exceeds 100

--- 05 missing status ---
  playbook/clauses/99_x.yaml [fixture_missing_status]: field 'status': Field required

--- 06 status 'reviewed' with null reviewed_by ---
  playbook/clauses/99_x.yaml [fixture_reviewed_no_reviewer]: field '<root>': Value error, status 'reviewed' requires a non-null 'reviewed_by' (only a named human reviewer may promote an entry to reviewed)

--- 07 invalid tier name ---
  playbook/clauses/99_x.yaml [fixture_bad_tier]: field 'default_floor': Input should be 'preferred', 'acceptable', 'fallback' or 'unacceptable'

--- 08 invalid op ---
  playbook/rules/rules.yaml:2 [RX08_bad_op]: field 'when.all.0.op': Input should be 'eq', 'neq', 'in', 'not_in', 'gt', 'gte', 'lt', 'lte', 'contains' or 'is_null'

--- 09 dangling depends_on ---
  playbook/clauses/99_x.yaml:2: clause 'fixture_dangling_depends_on' depends_on unknown clause id 'collateral_haircut_schedule'

--- 10 unknown top-level key in intake ---
  tests/fixtures/invalid_intake_unknown_key.yaml [D97]: field 'borrower_is_consumer': Extra inputs are not permitted
```

Rule and flag errors carry a line number located through YAML node marks (so quoting
and indentation do not matter). Clause errors carry the line of the entry's `id` for
cross-reference failures; pydantic field errors carry the file and the entry id but
not a line, because the failure is not tied to a single node.

---

## 2. The frozen contract — every model's fields

Source of truth: `src/sbl/models.py`. Prose description: `docs/schema_notes.md`.
JSON schemas: `playbook/schema/{clause,rule,intake}.schema.json`, regenerated by
`python scripts/export_schemas.py`. `?` marks an optional field.

**Every model sets `extra="forbid"`.** An unknown key anywhere is a hard error.

### Enums (closed lists)

| Enum | Values |
|---|---|
| `Category` | credit, collateral, default_enforcement, parties_reps, boilerplate |
| `Document` | facility_letter, security_agreement, account_control, all |
| `RiskRating` | high, medium, low |
| `Tier` | preferred, acceptable, fallback, unacceptable |
| `Status` | stub, draft, reviewed |
| `SourceType` | primary_law, regulator, filed_agreement, bank_terms, law_firm_briefing, textbook |
| `Reliability` | A, B, C |
| `BorrowerType` | individual, corporate, trust, partnership, fund |
| `FacilityType` | uncommitted_demand, committed_term |
| `Purpose` | general, acquire_securities, real_estate, business |
| `Benchmark` | SONIA, SARON, EURIBOR, fixed, other |
| `GoverningLaw` | england_wales, switzerland, luxembourg, other |
| `AssetClass` | cash, listed_equity, listed_bond, fund_daily, fund_gated, structured_product, unlisted, restricted_securities, real_estate |
| `ActionType` | flag, escalate, set_floor, set_opening, require_cp, require_rep, note |
| `ConditionOp` | eq, neq, in, not_in, gt, gte, lt, lte, contains, is_null |
| `Severity` | high, medium, low |
| `RequestOutcome` | accepted_within_floor, below_floor_escalated, unacceptable_escalated |

### Models

| Model | Fields |
|---|---|
| `SBLModel` | (base; `extra="forbid"`) |
| `Reviewable` | `status`, `reviewed_by?`, `last_reviewed?` |
| `Source` | `ref`, `type`, `url?`, `retrieved?`, `reliability`, `verified`, `note?` |
| `Position` | `text`, `rationale`, `conditions[]`, `approval?` |
| `UnacceptablePosition` | `text`, `rationale` (no `conditions`, no `approval`) |
| `Positions` | `preferred`, `acceptable`, `fallback`, `unacceptable` |
| `Clause` | `id`, `title`, `category`, `lender_objective`, `document?`, `risk_rating?`, `counterparty_asks[]`, `positions?`, `default_floor?`, `escalation_triggers[]`, `depends_on[]`, `jurisdiction_notes{}`, `regulatory_flags[]`, `not_automated[]`, `sources[]`, `status`, `reviewed_by?`, `last_reviewed?` |
| `LeafCondition` | `field`, `op`, `value?` |
| `AllCondition` | `all[]` |
| `AnyCondition` | `any[]` |
| `NotCondition` | `not` |
| `FlagAction` | `action`, `flag`, `severity`, `message` |
| `EscalateAction` | `action`, `to`, `reason`, `clause?` |
| `SetFloorAction` | `action`, `clause`, `tier` |
| `SetOpeningAction` | `action`, `clause`, `tier` |
| `RequireCpAction` | `action`, `clause`, `text` |
| `RequireRepAction` | `action`, `clause`, `text` |
| `NoteAction` | `action`, `clause`, `text` |
| `Rule` | `id`, `title`, `priority`, `when`, `then[]`, `rationale`, `sources[]`, `status`, `reviewed_by?`, `last_reviewed?` |
| `Flag` | `id`, `name`, `description`, `trigger_summary`, `who_decides`, `sources[]`, `status`, `reviewed_by?`, `last_reviewed?` |
| `Jurisdiction` | `id`, `name`, `creation`, `registration_filing`, `perfection_depends_on`, `enforcement_route`, `financial_collateral_regime`, `governing_law_of_intermediated_securities`, `practical_notes`, `sources[]`, `status`, `reviewed_by?`, `last_reviewed?` |
| `Borrower` | `type`, `domicile`, `natural_person`, `declared_high_net_worth?`, `business_purpose_declared?` |
| `Pledgor` | `same_as_borrower`, `type?`, `domicile?`, `natural_person?`, `is_pdmr_of_pledged_issuer` |
| `Facility` | `type`, `purpose`, `amount`, `currency`, `benchmark`, `other_facilities_with_lender` |
| `CompositionItem` | `asset_class`, `pct`, `single_name_max_pct?`, `issuer_restricted` |
| `Collateral` | `governing_law`, `custodian_location`, `lender_is_custodian`, `currencies[]`, `composition[]` |
| `CounterpartyRequest` | `tier?`, `text?` (at least one required) |
| `Derived` (computed) | `max_single_name_pct`, `has_real_estate`, `currency_mismatch`, `third_party_security`, `any_natural_person_pledgor` |
| `Intake` | `deal_id`, `description`, `borrower`, `pledgor`, `guarantor_present`, `facility`, `collateral`, `counterparty_requests{}`, `derived` (computed) |
| `ClauseResult` | `id`, `opening`, `floor`, `status`, `rules_applied[]`, `cps[]`, `reps[]`, `notes[]` |
| `FlagResult` | `id`, `severity`, `message`, `rule_id`, `who_decides?` |
| `Escalation` | `rule_id`, `to`, `reason`, `clause?` |
| `CounterpartyRequestOutcome` | `clause`, `requested_tier?`, `requested_text?`, `floor?`, `outcome` |
| `RunResult` | `run_id`, `timestamp`, `library_hash`, `intake_hash`, `intake`, `clauses[]`, `flags[]`, `escalations[]`, `counterparty_request_outcomes[]` |

### Tier helpers

`TIER_ORDER = (preferred, acceptable, fallback, unacceptable)`;
`tier_rank()` returns 0..3 where **lower is tighter**;
`is_tighter(a, b)`, `is_tighter_or_equal(a, b)`, `tighter(a, b)`, `looser(a, b)`.

### Derived field definitions (fixed; WP5 depends on these)

| field | definition |
|---|---|
| `max_single_name_pct` | max of the non-null `single_name_max_pct` values across composition lines; `0.0` when none given |
| `has_real_estate` | any composition line has `asset_class: real_estate`, whatever its percentage |
| `currency_mismatch` | **any** collateral currency differs from `facility.currency` (so GBP facility + `[GBP, USD]` collateral **is** a mismatch) |
| `third_party_security` | `pledgor.same_as_borrower` is false |
| `any_natural_person_pledgor` | the *effective* collateral provider is a natural person: the borrower where the pledgor is the borrower, otherwise the third-party pledgor |

### Cross-references checked at load time

rule `flag` action → flag id; rule clause-targeting action → clause id; clause
`regulatory_flags` → flag id; clause `depends_on` → clause id; clause
`jurisdiction_notes` keys → jurisdiction id; every rule condition `field` → an
addressable `Intake` path including `derived.*`.

`load_library()` collects **all** problems and raises one `LibraryError` listing them,
so a single `sbl validate` shows the whole list rather than the first failure.

`library_hash` = sha256 over the sorted (relative POSIX path, file bytes) of every
`*.yaml` / `*.yml` under `playbook/`, with path and content lengths mixed in so the
two cannot be confused.

---

## 3. What was built

```
.gitignore  pyproject.toml  README.md          (WP0; git init done, NOT committed)
src/sbl/{__init__,__main__,models,loader,cli}.py
scripts/export_schemas.py
playbook/clauses/01..24_*.yaml                 24 stubs, §3 order, all status: stub
playbook/rules/rules.yaml                      empty list
playbook/jurisdictions/{england_wales,switzerland,luxembourg}.yaml   all fields "stub"
playbook/flags/regulatory_flags.yaml           the ten §4 flags, all stub
playbook/schema/{clause,rule,intake}.schema.json   generated, committed
tests/test_schema_validation.py                29 tests
tests/fixtures/                                3 valid + 10 invalid
docs/schema_notes.md
handoff/WP1.md                                 this file
```

Clause ids in file order (01–12 core, 13–24 deferred): `facility_type`,
`conditions_precedent`, `eligible_collateral_lending_values`, `concentration_limits`,
`lender_discretion_valuation`, `margin_maintenance_cure`, `security_structure_control`,
`events_of_default`, `enforcement_liquidation`, `capacity_authority`,
`governing_law_jurisdiction`, `no_advice_non_reliance`, `interest_benchmark_fallbacks`,
`prepayment_breakage`, `collateral_substitution`, `cross_collateral_set_off`,
`reps_source_of_funds_sanctions_tax`, `purpose_restrictions`, `transfer_assignment`,
`confidentiality_bank_secrecy`, `tax_gross_up`, `third_party_security_waivers`,
`information_undertakings`, `currency_mismatch_fx`.

`git init` has been run. **Nothing is committed** — Stuart commits.

---

## 4. Deviations from the plan, and why

**4.1 Project-local virtualenv.** `pip install -e .` into the system Python
(`C:\Python312`) failed twice with `OSError: [WinError 2] ... 'pygmentize.exe' ->
'pygmentize.exe.deleteme'` — the sandbox this agent runs in cannot write to
`C:\Python312\Scripts`. The failure is environmental, not a packaging problem:
the wheel built cleanly both times. I created `.venv/` in the repo (already in
`.gitignore`) and installed there. Stuart should be able to run `pip install -e .`
directly. **If he cannot, this is a failure to report, not a pass.**

**4.2 `Source.url` and `Source.retrieved` are optional.** `build_plan.md` §2.1 shows
both populated. Making them optional lets a placeholder source be honest —
`url: null`, `verified: false` — rather than requiring a fabricated URL, which §0.4
forbids. All three test fixtures use this.

**4.3 `Clause` completeness is status-conditional, and `draft` requires ≥ 1 source.**
Requested behaviour for the first part. The sources requirement is mine, from §0.4
("every legal or market statement carries a `sources` entry"). WP3's own acceptance
is stricter (≥ 3 sources, ≥ 1 at reliability A or B) and is not enforced by the
schema — that check belongs in WP3's tests, not here, because a low bar at schema
level lets WP3 iterate.

**4.4 `UnacceptablePosition` is a separate model, not `Position` with nulls.** The
plan says the unacceptable tier has no `conditions`/`approval`; a separate model makes
supplying them a hard error rather than a convention.

**4.5 `EscalateAction` has an optional `clause`.** §2.4 requires only `to` and
`reason`. R16 (the engine's built-in below-floor escalation) needs to name a clause,
and the plan's §5 D06 expectations imply escalations carry clause ids. Optional, so
§2.4's shape still validates.

**4.6 `Rule.priority` defaults to 100.** The plan does not give a default. Chosen so
an explicit low priority (e.g. 10) sorts first without every rule having to state one.

**4.7 Condition union uses a callable discriminator with `cond_*` tags.** Without it,
one bad `op` produced twenty pydantic errors (one per union branch); with it, one.
The tag names are stripped from the reported field path by the loader, so the path a
reader sees (`when.all.0.op`) is the path in their YAML.

**4.8 `tests/expected/` not created.** It is WP9's; git does not track empty
directories anyway.

**4.9 Not a deviation but worth flagging:** a WP2 agent wrote `docs/glossary.md`,
`docs/product_definition.md`, `docs/source_register.md` and `handoff/WP2.md`
concurrently with this work package. The plan makes WP2 depend on WP1. Nothing in
WP2's output touches the schema, so there is no conflict, but its `source_register.md`
asserts several URLs and `verified: true` entries that I have not checked and that are
outside my scope.

---

## 5. Lowest-confidence items (in priority order for review)

1. **Projected paths over `collateral.composition`.** The loader accepts
   `collateral.composition.asset_class` and its siblings as valid rule fields, but
   WP1 does not define what they *evaluate to*. Rules R08 and R15 in §4 both need
   "any composition line where…", which the leaf grammar cannot express directly.
   **WP5 must either define projection semantics and test them, or add derived
   booleans (`derived.any_issuer_restricted`, `derived.has_illiquid_collateral`) —
   the latter is cleaner and I would take it.** This is the single most likely place
   for WP5 to build on an assumption I did not fix.

2. **`currency_mismatch` is broad.** Defined as *any* collateral currency differing
   from the facility currency. The §2.3 example (GBP facility, `[GBP, USD]`
   collateral) therefore has `currency_mismatch: true`. The alternative reading —
   "the facility currency is absent from the collateral currencies" — would make it
   false. My reading is the economically correct one for an FX haircut, and R13 only
   adds a note and tightens a floor (no escalation), so D01's "no escalations"
   expectation survives either way. But if D01's snapshot is expected to be quiet,
   this will show up as an extra note. **Confirm before WP9 snapshots are cut.**

3. **`has_real_estate` ignores percentage.** A `real_estate` line at `pct: 0` still
   trips R09, which is a hard stop. Literal and predictable, but arguably a false
   positive. Easy to change to `pct > 0` if Stuart prefers.

4. **Clause `category` assignments for the 24 stubs are mine.** `conditions_precedent`
   → `credit` and `purpose_restrictions` → `credit` are both defensible as
   `parties_reps` / `boilerplate`. They affect grouping in the markup only, but WP3
   should sanity-check them while writing the entries.

5. **`lender_objective` one-liners on all 24 stubs are mine.** They are structural
   statements about what the lender is protecting, not statements of law, so they
   carry no sources. WP3 should treat them as a starting point and rewrite freely.

6. **Line numbers on clause validation errors.** Cross-reference failures get the
   line of the entry's `id`; pydantic field errors get file + entry id but no line.
   Locating the exact failing node inside a pydantic error would need a mark-aware
   loader. Adequate for one-clause-per-file, and I did not think it worth the
   complexity.

7. **`Flag.who_decides` is a free string.** Approvers appear as free strings in three
   places (`Position.approval`, `EscalateAction.to`, `Flag.who_decides`). An enum
   would be tighter, but I had no authority to fix the list of approver roles. WP8
   should propose one if the strings start to drift.

---

## 6. Notes for the next work packages

* **WP3 (clauses):** set `status: draft` only when `document`, `risk_rating`,
  `positions` (all four tiers), `default_floor` and ≥ 1 source are all present —
  otherwise the loader rejects the file and names what is missing. Write judgement
  numbers as `X` per §2.1. `jurisdiction_notes` keys must be `england_wales`,
  `switzerland` or `luxembourg`.
* **WP5 (engine):** read §1 of `docs/schema_notes.md` before writing `engine.py`.
  Every tier assignment is `tighter(current, proposed)`. Resolve open item 1 above
  first.
* **WP7 (jurisdictions):** all seven substantive fields are required strings, so you
  cannot silently skip a question; answer with `"[VERIFY] ..."` if unresearched.
* **Anyone changing a model:** rerun `python scripts/export_schemas.py`, rerun
  `pytest`, and record the change in a hand-off note (`build_plan.md` §6, WP1 Freeze).
