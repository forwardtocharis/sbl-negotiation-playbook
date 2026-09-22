# Build Plan: SBL Negotiation Playbook Demonstrator

Written for: agents (and Stuart) executing the build. Read `sbl_playbook_brief.md` first, then `brief_review.md`. This plan supersedes the brief where they differ.

Plan date: 2026-09-21. Repo root: `F:\SBL_Legal`.

---

## 0. Non-negotiable rules for every agent

1. **Side.** All positions are drafted from the lender's (private bank's) side.
2. **Synthetic only.** No real counterparties, client facts, bank names or branding anywhere in the repo, including test fixtures, examples and commit messages. Party names in fixtures are obviously fictional (e.g. "Borrower A", "Aldergrove Trust").
3. **Status discipline.** Every clause entry, rule, jurisdiction note and regulatory flag carries `status: stub | draft | reviewed`. Agents may write `stub` or `draft` only. Only Stuart sets `reviewed` and fills `reviewed_by` / `last_reviewed`.
4. **No invented law.** Every legal or market statement carries a `sources` entry. If you cannot find a source you have actually opened, write the statement with `verified: false` and the text prefix `[VERIFY]`, or leave the field as `stub`. Never fabricate a citation, statute section, case name or URL.
5. **No verbatim lifting.** Do not paste more than a short phrase from any filed agreement, bank terms or law-firm briefing. Paraphrase. Never include party names from source documents.
6. **Determinism.** Same intake + same library version = same output, byte for byte except timestamps. No randomness, no network calls in the core engine.
7. **Minimal stack.** Python 3.11+, `pyyaml`, `pydantic>=2`, `pytest`. Nothing else in the core. Phase 5 may add the Anthropic SDK behind an optional extra.
8. **Do not overclaim.** README, output headers and docstrings describe this as a demonstrator built from public sources. No wording that implies production use, regulatory approval, or validation against any institution's risk appetite.
9. **Every work package ends with its acceptance checks run and their output pasted into the hand-off note.** Report failures as failures.

---

## 1. Target repository layout

```
F:\SBL_Legal\
  README.md                       # disclaimer, what it is, how to run, walkthrough
  sbl_playbook_brief.md           # original brief (unchanged)
  brief_review.md                 # review (this plan's source)
  build_plan.md                   # this file
  pyproject.toml
  docs/
    glossary.md
    product_definition.md         # SBL vs securities lending; Lombard lending; document set
    not_automated_register.md
    source_register.md            # every source, graded, with retrieval date
    interview_walkthrough.md      # 3-minute script + anticipated questions
    demo_script.md                # exact commands + what to point at on screen
  playbook/
    schema/
      clause.schema.json          # generated from pydantic, committed for readability
      rule.schema.json
      intake.schema.json
    clauses/
      01_facility_type.yaml
      02_conditions_precedent.yaml
      ...                         # one file per clause, core twelve then deferred
    rules/
      rules.yaml                  # ordered list of rules
    jurisdictions/
      england_wales.yaml
      switzerland.yaml
      luxembourg.yaml
    flags/
      regulatory_flags.yaml       # flag definitions (id, name, description, who decides)
  deals/
    D01_plain_vanilla.yaml
    D02_trust_concentrated_pdmr.yaml
    D03_swiss_corporate_purpose.yaml
    D04_third_party_pledge_lux.yaml
    D05_real_estate_hard_stop.yaml
    D06_below_floor_request.yaml
  src/sbl/
    __init__.py
    models.py                     # pydantic models: Clause, Rule, Intake, RunResult
    loader.py                     # load + validate YAML, compute content hashes
    engine.py                     # deterministic rule evaluation
    markup.py                     # Markdown renderer
    audit.py                      # JSONL log writer
    cli.py                        # `python -m sbl validate | run | explain`
    __main__.py
  tests/
    test_schema_validation.py
    test_engine.py
    test_golden_deals.py          # each deal in deals/ vs expected/ snapshot
    expected/
      D01_plain_vanilla.md
      D01_plain_vanilla.json
      ...
  runs/                           # gitignored; audit logs and outputs from real runs
```

---

## 2. Data contracts (freeze these in WP1 before any content work)

### 2.1 Clause entry (`playbook/clauses/*.yaml`)

```yaml
id: margin_maintenance_cure            # snake_case, unique, stable
title: Margin maintenance, margin call mechanics and cure period
category: collateral                   # credit | collateral | default_enforcement | parties_reps | boilerplate
document: facility_letter              # facility_letter | security_agreement | account_control | all
risk_rating: high                      # high | medium | low
lender_objective: >
  One sentence: what the lender is protecting with this clause.
counterparty_asks:
  - Longer cure period (5+ business days)
  - Written notice as a precondition to any liquidation
positions:
  preferred:
    text: >
      Draft clause language, lender-side opening position.
    rationale: Why this is the opening position.
  acceptable:
    text: ...
    rationale: ...
    conditions: []                     # conditions that must hold to concede here
  fallback:
    text: ...
    rationale: ...
    conditions:
      - Diversified collateral only (no single-name > 25% of lending value)
    approval: senior lawyer            # who must sign off a concession to this tier
  unacceptable:
    text: >
      Description of the position the lender will not accept (not drafting).
    rationale: ...
default_floor: fallback                # lowest tier concedable without escalation, absent rules
escalation_triggers:
  - Any request for a cure period longer than X business days
depends_on: [enforcement_liquidation, lender_discretion_valuation]
jurisdiction_notes:
  england_wales: "..."
  switzerland: "..."
  luxembourg: "..."
regulatory_flags: [mifid_suitability]  # flag ids this clause is sensitive to
not_automated:
  - Whether to grant forbearance on a live margin call
sources:
  - ref: "Short label"
    type: primary_law | regulator | filed_agreement | bank_terms | law_firm_briefing | textbook
    url: "https://..."
    retrieved: 2026-09-21
    reliability: A | B | C            # A primary law/regulator, B filed agreement/bank terms, C commentary
    verified: false
    note: "What this source supports"
status: draft
reviewed_by: null
last_reviewed: null
```

Rules for text fields: `preferred`, `acceptable`, `fallback` contain draft clause language (paraphrased, lender-side). `unacceptable` contains a description, since the lender never drafts it. Numbers that are judgement calls (days, percentages) are written as `X` in `draft` entries with a comment listing the range seen in sources; Stuart fills the number on review.

### 2.2 Tier semantics (put this verbatim in `docs/glossary.md`)

| Tier | Meaning | Who may agree it |
|---|---|---|
| preferred | Lender's opening position | Deal lawyer, by default |
| acceptable | Routine concession; no loss of core protection | Deal lawyer, no escalation |
| fallback | Concession that costs real protection; only with the listed conditions satisfied | Named approver in the entry; concession logged |
| unacceptable | Walk-away line | Nobody. Any request here is a hard escalation |

The **floor** for a clause on a deal is the lowest tier the deal lawyer may concede to without escalation. Rules can only move the floor up (tighten). The **opening** is the tier the markup proposes first; rules can only move it up.

### 2.3 Intake (`deals/*.yaml`, validated by `Intake` model)

```yaml
deal_id: D02
description: Synthetic. Jersey discretionary trust, concentrated single stock, settlor is PDMR.
borrower:
  type: trust                          # individual | corporate | trust | partnership | fund
  domicile: JE                         # ISO 3166-1 alpha-2
  natural_person: false
  declared_high_net_worth: null        # true | false | null (individuals only)
  business_purpose_declared: null
pledgor:
  same_as_borrower: true
  type: null                           # if different from borrower
  domicile: null
  natural_person: null
  is_pdmr_of_pledged_issuer: true      # applies to borrower or pledgor or connected person
guarantor_present: false
facility:
  type: uncommitted_demand             # uncommitted_demand | committed_term
  purpose: general                     # general | acquire_securities | real_estate | business
  amount: 5000000
  currency: GBP
  benchmark: SONIA                     # SONIA | SARON | EURIBOR | fixed | other
  other_facilities_with_lender: false
collateral:
  governing_law: england_wales         # england_wales | switzerland | luxembourg | other
  custodian_location: GB
  lender_is_custodian: true
  currencies: [GBP, USD]
  composition:                         # list; percentages of lending value, must sum <= 100
    - asset_class: listed_equity       # cash | listed_equity | listed_bond | fund_daily | fund_gated | structured_product | unlisted | restricted_securities | real_estate
      pct: 90
      single_name_max_pct: 70          # largest single issuer exposure within this class
      issuer_restricted: false         # lock-ups, control stock, etc.
    - asset_class: cash
      pct: 10
      single_name_max_pct: null
      issuer_restricted: false
counterparty_requests: {}              # optional: clause_id -> {tier: fallback} or {text: "..."}
```

The model computes derived fields the rules can use: `derived.max_single_name_pct`, `derived.has_real_estate`, `derived.currency_mismatch`, `derived.third_party_security`, `derived.any_natural_person_pledgor`.

### 2.4 Rule (`playbook/rules/rules.yaml`)

```yaml
- id: R07_pdmr_pledged_issuer
  title: Pledgor or borrower is a PDMR / insider of a pledged issuer
  priority: 10                         # lower runs first; only affects log ordering
  when:
    all:
      - { field: pledgor.is_pdmr_of_pledged_issuer, op: eq, value: true }
  then:
    - { action: flag, flag: market_abuse, severity: high,
        message: "Pledge and any enforcement sale may constitute dealing; closed periods and disclosure obligations apply." }
    - { action: escalate, to: "senior lawyer + compliance",
        reason: "Insider status of pledgor must be cleared before term sheet." }
    - { action: set_floor, clause: enforcement_liquidation, tier: acceptable }
    - { action: require_rep, clause: capacity_authority,
        text: "Pledgor represents it is not in possession of inside information and will notify on becoming subject to a closed period." }
    - { action: require_cp, clause: conditions_precedent,
        text: "Compliance sign-off on insider status and any issuer consent requirements." }
  rationale: >
    Why the rule exists, in plain English.
  sources: [...]                       # same source structure as clauses
  status: draft
```

Condition grammar: `all: [...]`, `any: [...]`, `not: {...}`, nestable. Leaf: `{field, op, value}` with `op` in `eq, neq, in, not_in, gt, gte, lt, lte, contains, is_null`. `field` is a dotted path into the intake including `derived.*`. Unknown field = validation error at load time, not a silent false.

Action types and semantics:

| action | required keys | effect |
|---|---|---|
| flag | flag, severity, message | Adds a regulatory/commercial flag. `flag` must exist in `flags/regulatory_flags.yaml`. |
| escalate | to, reason | Hard stop. Markup header lists all escalations. Run exit code is 2 if any escalation. |
| set_floor | clause, tier | Raises floor for the clause. Never lowers. |
| set_opening | clause, tier | Raises opening for the clause. Never lowers. |
| require_cp | clause, text | Appends a condition precedent to the named clause's output. |
| require_rep | clause, text | Appends a representation/undertaking to the named clause's output. |
| note | clause, text | Adds a drafting note. |

Conflict resolution: tiers only tighten, so order never matters for the result. The log records every rule that touched each clause.

### 2.5 Run result and audit log

`RunResult` (JSON) contains: `run_id`, `timestamp`, `library_hash` (sha256 over sorted clause + rule + jurisdiction + flag files), `intake_hash`, `intake` (echoed), `clauses[]` each with `id, opening, floor, status, rules_applied[], cps[], reps[], notes[]`, `flags[]`, `escalations[]`, `counterparty_request_outcomes[]` (`accepted_within_floor | below_floor_escalated | unacceptable_escalated`). Appended as one line to `runs/audit.jsonl`. Markdown output is rendered from this object only; the renderer has no access to anything else, which is what makes the trace complete.

---

## 3. Clause set

### Core twelve (build these, in this order)

| # | id | Brief ref | Why it is core |
|---|---|---|---|
| 1 | facility_type | 1 | Demand vs term drives everything in enforcement |
| 2 | conditions_precedent | 4 | Where capacity, KYC, perfection are gated |
| 3 | eligible_collateral_lending_values | 5 | The risk spine |
| 4 | concentration_limits | 6 | The risk spine |
| 5 | lender_discretion_valuation | new (B4) | Most contested clause in practice |
| 6 | margin_maintenance_cure | 8 | The risk spine |
| 7 | security_structure_control | 9, widened (B5) | Pledge / charge / title transfer + control |
| 8 | events_of_default | 11 | Includes death/incapacity, insolvency, MAC |
| 9 | enforcement_liquidation | 12 | Notice, standard of conduct, self-help |
| 10 | capacity_authority | 13 | Trusts, corporates, partnerships |
| 11 | governing_law_jurisdiction | 16 | Cross-border overlay hangs off this |
| 12 | no_advice_non_reliance | new (B4) | Links to MiFID/FinSA suitability flag |

### Deferred (create as `status: stub` files with id, title, category, lender_objective only)

interest_benchmark_fallbacks (2), prepayment_breakage (3), collateral_substitution (7), cross_collateral_set_off (10), reps_source_of_funds_sanctions_tax (14), purpose_restrictions (15), transfer_assignment (17), confidentiality_bank_secrecy (18), tax_gross_up (19), third_party_security_waivers (new), information_undertakings (new), currency_mismatch_fx (new).

Stubs exist so rules can reference them (e.g. purpose rule → purpose_restrictions) and so the markup shows the shape of the full library.

---

## 4. Rules set (initial, all `status: draft`)

Each rule below must exist in `rules.yaml` with rationale and at least one source (or `[VERIFY]`).

| id | trigger (plain English) | actions |
|---|---|---|
| R01_trust_borrower | borrower.type == trust | require_cp trust deed review; require_rep trustee capacity & power to borrow/charge; set_floor capacity_authority=acceptable; note on trustee limited recourse asks |
| R02_corporate_or_partnership | borrower.type in [corporate, partnership, fund] | require_cp board/partner resolutions, constitutional docs; require_rep corporate benefit |
| R03_natural_person_borrower | borrower.natural_person == true | flag consumer_credit severity: high if no HNW/business declaration, medium if declared; escalate if no declaration; note on death/incapacity EoD |
| R04_natural_person_pledgor_england | derived.any_natural_person_pledgor AND collateral.governing_law == england_wales | flag fca_safe_harbour_uncertain (medium) with [VERIFY] text; note on security_structure_control |
| R05_third_party_security | derived.third_party_security | require_rep pledgor independent advice; set_floor capacity_authority=acceptable; flag financial_assistance_corporate_benefit if pledgor.type == corporate; note third_party_security_waivers |
| R06_concentration | derived.max_single_name_pct > 25 | set_floor concentration_limits=acceptable; set_floor margin_maintenance_cure=acceptable; note on lending value haircut |
| R06b_concentration_severe | derived.max_single_name_pct > 50 | set_opening margin_maintenance_cure=preferred (already), set_floor eligible_collateral_lending_values=acceptable; escalate to credit |
| R07_pdmr_pledged_issuer | pledgor.is_pdmr_of_pledged_issuer | as in §2.4 |
| R08_restricted_securities | any composition item issuer_restricted | flag restricted_securities; set_floor enforcement_liquidation=acceptable; require_cp issuer consent / lock-up review |
| R09_real_estate | derived.has_real_estate | flag mortgage_regulation high; escalate; note that real estate is out of scope for this playbook |
| R10_purpose_acquire_securities | facility.purpose == acquire_securities | flag mifid_suitability; require_rep purpose; set_floor no_advice_non_reliance=acceptable; note purpose_restrictions |
| R11_committed_term | facility.type == committed_term | set_floor events_of_default=acceptable; note on MAC and prepayment interaction |
| R12_third_party_custodian | collateral.lender_is_custodian == false | require_cp account control agreement executed; set_floor security_structure_control=acceptable; note per jurisdiction on control |
| R13_currency_mismatch | derived.currency_mismatch | note eligible_collateral_lending_values FX haircut; set_floor lender_discretion_valuation=acceptable |
| R14_swiss_booking | collateral.governing_law == switzerland OR custodian_location == CH | flag bank_secrecy_data (low); note on confidentiality_bank_secrecy; jurisdiction note switch |
| R15_illiquid_collateral | any asset_class in [fund_gated, unlisted, structured_product] | set_floor eligible_collateral_lending_values=acceptable; set_floor enforcement_liquidation=acceptable; note on valuation frequency |
| R16_counterparty_request_below_floor | (engine built-in, not YAML) requested tier below floor | escalate with clause id; unacceptable → escalate as hard stop |

Flags file must define: consumer_credit, mortgage_regulation, mifid_suitability, market_abuse, restricted_securities, fca_safe_harbour_uncertain, financial_assistance_corporate_benefit, bank_secrecy_data, prudential_awareness, emir_awareness. Each with `who_decides` and `description`.

---

## 5. Golden deals and expected outcomes

Each deal has an expected Markdown and JSON snapshot under `tests/expected/`. The table gives the minimum assertions `test_golden_deals.py` must make beyond snapshot equality.

| deal | key facts | must produce |
|---|---|---|
| D01_plain_vanilla | UK individual, HNW declared, diversified listed portfolio at lender custody, uncommitted demand, GBP, general purpose | no escalations; consumer_credit flag at medium; exit code 0; all clauses at default floor |
| D02_trust_concentrated_pdmr | Jersey trust, 70% single stock, settlor PDMR, England law, lender custody | R01, R06, R06b, R07 fire; escalations ≥ 2; enforcement_liquidation floor = acceptable; exit 2 |
| D03_swiss_corporate_purpose | Swiss holdco, Zurich custody, SARON, committed term, purpose acquire_securities, CHF loan with USD collateral | R02, R10, R11, R13, R14 fire; mifid_suitability + bank_secrecy_data flags; Swiss jurisdiction notes printed |
| D04_third_party_pledge_lux | Lux resident individual borrower; spouse pledgor; fund_daily interests at third-party Lux custodian | R03, R05, R12 fire; require_cp account control; Lux notes printed; consumer_credit flag |
| D05_real_estate_hard_stop | as D01 plus 30% residential real estate | R09 fires; escalation; exit 2; markup header says out of scope |
| D06_below_floor_request | as D01 plus counterparty_requests: margin_maintenance_cure → fallback, enforcement_liquidation → unacceptable | first request accepted within floor and logged; second is hard escalation; exit 2 |

---

## 6. Work packages

Dependencies: WP0 → WP1 → everything else. WP2, WP3, WP7, WP8 (content) run in parallel with WP4, WP5, WP6 (code) once WP1 is merged. WP9 needs WP3–WP8. WP10 needs WP9. WP11 is optional and last.

Estimates are agent time for scaffold + draft. Human review time is listed separately and is Stuart's.

### WP0. Repo scaffold (agent, 30 min)
- `git init`; `.gitignore` (runs/, __pycache__, .venv); `pyproject.toml` with the four dependencies and `[project.scripts] sbl = "sbl.cli:main"`; empty package; `README.md` with disclaimer block at top and a "Status: scaffolding" line.
- **Accept:** `pip install -e .` succeeds; `python -m sbl --help` prints usage.

### WP1. Schemas, models, loader (agent, 2–3 h)
- Implement `models.py` exactly per §2. Enums for every closed list. `Intake` computes `derived.*`.
- `loader.py`: load all YAML, validate, resolve cross-references (rule → clause ids, clause → flag ids, depends_on), compute `library_hash`. Any dangling reference is a hard error with file and line.
- Export JSON schemas to `playbook/schema/`.
- `sbl validate` command.
- Tests: valid fixtures load; each of ten deliberate errors (unknown field in rule, unknown clause id, tier lowered, percentages > 100, missing status, etc.) is rejected with a clear message.
- **Accept:** `pytest tests/test_schema_validation.py` green; `sbl validate` exits 0 on the stub library.
- **Freeze:** after WP1 merges, schema changes need a note in the hand-off and a rerun of all tests.

### WP2. Glossary and product definition (agent 1 h; human review 30 min)
- `docs/glossary.md`: tier table from §2.2 verbatim; canonical terms with synonyms (lending value / advance rate / LTV; margin call / shortfall; cure period / grace period; pledge / charge / title transfer; PDMR / insider; Lombard loan / SBL).
- `docs/product_definition.md`: SBL vs securities lending in one paragraph; Lombard lending terminology; the three-document set and what each one does; a one-paragraph description of the typical negotiation dynamic in PWM (client-relationship pressure vs. credit protection).
- **Accept:** every term used in clause files appears in the glossary (add a test that greps clause `title` fields against glossary headings; soft warning only).

### WP3. Core twelve clause entries (agent 8–12 h across parallel sub-agents; human review 1–2 h per clause)
- One sub-agent per two to three clauses. Each sub-agent receives: this plan, the schema, the glossary, the source-gathering procedure below, and its clause ids.
- Source-gathering procedure per clause: (1) search public regulator or primary-law text where relevant; (2) find at least one filed securities pledge or margin loan agreement on SEC EDGAR full-text search and read the relevant clause for structure, not wording; (3) find one published private-bank SBL/Lombard terms document; (4) find one law-firm or textbook note. Record every source in the entry and in `docs/source_register.md` with retrieval date and reliability grade.
- Draft all four tiers. Numbers as `X` with a comment giving the observed range. `rationale` fields must answer "why is this the lender's line" in two to four sentences and should be written to be said out loud.
- Fill `counterparty_asks` with at least two realistic borrower pushes.
- Fill `jurisdiction_notes` only where the clause genuinely varies; otherwise write "No jurisdiction-specific variation identified [VERIFY]".
- Fill `not_automated` with at least one item for high-risk clauses.
- **Accept:** `sbl validate` green; each entry has ≥ 3 sources of which ≥ 1 is reliability A or B; each tier has non-empty text and rationale; `status: draft`. Hand-off note lists, per clause, the two positions the sub-agent is least confident about, for Stuart's review priority.

### WP4. Intake CLI (agent, 1–2 h)
- `sbl run deals/D0x.yaml --out runs/` loads, validates and echoes the intake with derived fields.
- Optional `sbl intake --interactive` that prompts for each field and writes a deal YAML. Lowest priority in the plan; skip if time is short.
- **Accept:** all six deal files validate; a deal with composition summing to 110% is rejected.

### WP5. Rules engine (agent, 3–4 h)
- `engine.py`: evaluate conditions per §2.4 grammar; apply actions with tighten-only semantics; built-in R16 for counterparty requests; produce `RunResult`.
- Rules from §4 written into `rules.yaml` with rationale, sources, status.
- Tests: each rule fires on a minimal intake and does not fire on its negation; tighten-only property test (applying rules in reversed order gives identical floors/openings); unknown flag id rejected at load.
- **Accept:** `pytest tests/test_engine.py` green.

### WP6. Markup generator and audit log (agent, 2–3 h)
- `markup.py` renders Markdown from `RunResult` only. Layout:
  1. Header: deal id, description, timestamp, library hash, intake hash, review-status summary (n reviewed / n draft / n stub).
  2. **Escalations** (if any), each with rule id, who decides, reason.
  3. **Flags**, grouped by severity, each with who decides.
  4. **Clause-by-clause**: title, risk rating, status tag (`[REVIEWED]` / `[DRAFT]` / `[STUB]`), opening tier text + rationale, floor, the full ladder below it collapsed as a table (tier, one-line summary, conditions, approver), CPs and reps added by rules, notes, jurisdiction note for the deal's governing law, rules applied.
  5. **Counterparty request outcomes**.
  6. **Not automated on this deal**: union of `not_automated` items from clauses touched by escalations or flags.
  7. Footer: demonstrator disclaimer.
- `audit.py`: append `RunResult` as one JSON line; `sbl explain <run_id> <clause_id>` prints the rules that determined that clause's outcome.
- **Accept:** all six deals render; the Markdown contains no text that is not derivable from `RunResult` (test: render from a JSON file alone).

### WP7. Jurisdiction overlay (agent 3–4 h; human review 1 h per jurisdiction)
- One file per jurisdiction, each with the five questions from the brief plus the two additions from review §E, each answer with sources and `verified`. Fields: `creation`, `registration_filing`, `perfection_depends_on`, `enforcement_route`, `financial_collateral_regime` (scope, including whether natural-person collateral providers are covered), `governing_law_of_intermediated_securities`, `practical_notes`, `sources`, `status`.
- Research targets (agents: locate and read the primary text before writing; mark `[VERIFY]` if not read):
  - England & Wales: Financial Collateral Arrangements (No. 2) Regulations 2003; Companies Act 2006 charge registration for corporate chargors and whether the FCARs disapply it; enforcement by appropriation vs sale; scope re natural persons.
  - Switzerland: Code of Obligations pledge provisions; Federal Intermediated Securities Act (FISA / BEG) on security interests over intermediated securities and control agreements; private realisation (Privatverwertung) where agreed; Hague Securities Convention status; Debt Enforcement and Bankruptcy Act interaction.
  - Luxembourg: Law of 5 August 2005 on financial collateral arrangements; enforcement without prior notice where agreed; treatment of natural persons; insolvency-remoteness features.
- **Accept:** each file validates; every answer has ≥ 1 source; the rules R04 and R14 reference the file content correctly; markup prints the correct file for each deal's governing law.

### WP8. Regulatory flags (agent 2 h; human review 1 h)
- `flags/regulatory_flags.yaml` per §4 list with `description`, `trigger_summary`, `who_decides`, `sources`, `status`.
- Consumer credit entry must describe the exemption logic in plain English for UK and Switzerland with `[VERIFY]` markers where the threshold numbers have not been confirmed from a primary source.
- **Accept:** every flag referenced by a rule or clause exists; every flag has `who_decides`.

### WP9. Golden deals, snapshots, end-to-end tests (agent, 2 h)
- Write the six deals per §5. Generate snapshots. Encode the "must produce" assertions as explicit tests, not just snapshot equality.
- Add a `make check` / `check.ps1` script: `sbl validate && pytest -q && sbl run deals/*.yaml --out runs/`.
- **Accept:** `check.ps1` exits 0 (D02, D05, D06 exit 2 from `sbl run` is expected and the script must treat it as success for those deals).

### WP10. README, not-automated register, demo script, interview prep (agent 2 h; human edit 1 h)
- `docs/not_automated_register.md`: consolidated list from all clause `not_automated` fields plus system-level items (see §7). Each item: what the tool does instead (flag / escalate / print status), and why a human must own it.
- `docs/demo_script.md`: exact commands for D01 → D02 → D06 in that order (clean run, escalation-heavy run, counterparty request run), with the three things to point at on screen for each.
- `docs/interview_walkthrough.md`: the three-minute script from the brief §8 rewritten against the actual build, plus §8 below.
- README: disclaimer, product definition summary, how to run, layout, status counts (generated by `sbl validate --summary`).
- **Accept:** a fresh agent can follow README from clone to a rendered D02 in under ten minutes.

### WP11. Optional: LLM ingest (agent, open; do not start before WP10 is accepted)
- `sbl ingest <counterparty_draft.md>` uses the current Claude model (check model id in the API docs at build time) to (a) map counterparty clauses to library ids with a confidence score and (b) propose intake facts. Output is a deal YAML with every field tagged `source: llm_unverified` plus a mapping table. The user edits and confirms before `sbl run`.
- Hard constraints: the model never sees tier text; it never chooses tiers; no escalation logic in prompts; deterministic engine unchanged.
- **Accept:** works on one synthetic counterparty draft that the agent writes; README section states the constraints.

---

## 7. Not-automated register (seed list; extend from clause files)

System-level items to include regardless of clause content:
- The final determination that a borrower is or is not a consumer under any regime.
- Any concession below a clause's floor, and any request at `unacceptable`.
- Clearing a PDMR/insider position with compliance.
- Suitability or appropriateness conclusions.
- Any cross-border perfection or enforceability conclusion (tool cites; local counsel confirms).
- Sanctions, KYC and source-of-funds outcomes.
- Forbearance on a live margin call, waiver of an event of default, and the decision to enforce.
- Promotion of any entry from `draft` to `reviewed`.

---

## 8. Interview preparation (goes in `docs/interview_walkthrough.md`)

Three-minute script (per brief §8) with these concrete pointers: show D02 output header (escalations first), one clause ladder with its status tag, and the `sbl explain` trace for `enforcement_liquidation`.

Anticipated questions and the shape of the answer:
1. Why four tiers and not three? Because "acceptable" and "fallback" differ in who can agree them, not just in content. The approver field is the point.
2. What happens when two rules disagree? They cannot: rules only tighten. Show the log listing both.
3. What would you never automate? Read from the register; pick the consumer determination and the below-floor concession.
4. How would this be validated inside a bank? Every entry is `draft` until a named reviewer promotes it; the output labels status; the library hash is in every log line; you would validate against the institution's credit policy and local counsel, not against public sources.
5. SBL vs securities lending? One sentence from `product_definition.md`.
6. How do you know the law in the overlay is right? Answer honestly: sources listed, `verified` flags, `[VERIFY]` printed in output; name one point you checked against primary text and one you did not.
7. Why not an LLM for the whole thing? The reading is the easy part; the decision has to be reproducible and traceable, and escalation points have to be fixed in advance by a human.
8. What is the most contested clause in practice and where is your line? Lender discretion over lending values; explain the notice/threshold trade-off from the entry.

---

## 9. Definition of done

- `check.ps1` exits 0 on a clean clone.
- Twelve core clauses at `draft` or better with sources; twelve deferred stubs.
- Sixteen rules with tests; ten flags; three jurisdiction files.
- Six golden deals with snapshots and explicit assertions.
- README, glossary, product definition, not-automated register, source register, demo script, interview walkthrough all present.
- No real institution, person or client anywhere in the repo (test: grep for a denylist Stuart supplies; at minimum the name of the target employer).
- Hand-off note from each work package includes the pasted acceptance output and the sub-agent's lowest-confidence items for human review.
