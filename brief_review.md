# Review of `sbl_playbook_brief.md`

Reviewed 2026-09-21. The brief is sound in its framing: the four-tier ladder, deterministic rules, explicit escalation, and the "reasoning is the deliverable" stance are the right centre of gravity. The findings below are where the brief is inconsistent, under-specified for delegation to agents, or missing things an interviewer for this role will probe. Each finding has a recommended change. The build plan (`build_plan.md`) adopts all of them.

Severity key: **A** = will cause wrong or embarrassing output if not fixed; **B** = materially improves credibility; **C** = tidy-up.

---

## A. Structural inconsistencies

### A1. "Build the first twelve" but nineteen clauses are listed (A)
Section 3 lists 19 numbered clauses and section 6 says build 12. No cut is made. Agents cannot proceed without a decision.

**Change:** Fix the core twelve explicitly (plan §3). Selection principle: the clauses on the risk spine (collateral value, margin, enforcement) plus the two that most often kill a PWM deal (capacity, governing law), plus one that ties into regulatory exposure (no-advice / non-reliance). Everything else is a named "deferred" set.

### A2. Ground rule 1 conflicts with delegating the build to agents (A)
"Every substantive position must be researched and written by Stuart" versus a plan for agents to build the library.

**Change:** Reconcile with a **review-status field** on every clause entry, rule, jurisdiction note and flag: `stub` → `draft` → `reviewed`. Agents produce `draft` at most. Only Stuart promotes to `reviewed`. The markup generator prints the status of every position it emits, so an un-reviewed position is visibly labelled in the output. This turns ground rule 1 into a mechanism rather than an aspiration, and is itself a good interview point.

### A3. Effort estimates are not credible for researched content (B)
"12 entries, 4 tiers each, half a day" is achievable for scaffolding only. A defensible fallback ladder with sources is closer to one to two hours per clause.

**Change:** Split every content work package into (i) scaffold + draft, which agents do fast, and (ii) human review, budgeted separately. Plan §6 gives revised estimates.

### A4. The side we are on is never stated (A)
The playbook assumes lender-side (private bank) positions but never says so. Tier semantics are ambiguous without it.

**Change:** State "positions are drafted from the lender's side" and define the tiers precisely (plan §2.2): preferred = opening; acceptable = deal lawyer may concede; fallback = concede only if listed conditions are met and it is logged; unacceptable = walk-away, any request here is a hard escalation.

---

## B. Schema gaps (Module 1)

### B1. No link between intake parameters and tier selection (A)
The clause schema has no field telling the rules engine which tier applies in which circumstances. Without it the rules engine can only raise flags; it cannot pick positions.

**Change:** Two rule actions: `set_floor` (tighten the lowest tier the deal lawyer may concede to without escalation) and `set_opening` (change the opening position). Rules only ever tighten. Conflict resolution is then trivial and auditable: the most restrictive result wins, and every rule that touched a clause is listed in the log.

### B2. Missing fields (B)
Add to every clause entry: `document` (which document the clause lives in), `lender_objective`, `counterparty_asks` (what borrowers typically push for, so the ladder answers a real ask), `depends_on` (interdependencies, e.g. cure period and enforcement notice; lending values and concentration limits), `not_automated` (decisions on this clause the tool refuses to make), `status`, `reviewed_by`, `last_reviewed`, and a structured `sources` list with `verified: true|false`.

### B3. Terminology is mixed (C)
The brief uses "advance rate", "lending value" and LTV interchangeably. Swiss and UK practice use different words for the same thing.

**Change:** Add a glossary file. One canonical term in the schema (`lending_value_pct`) with synonyms listed.

### B4. Missing clauses that are central to PWM SBL practice (A)
Three clauses are absent and each is a frequent battleground:
- **Lender discretion to change lending values / eligibility** unilaterally, and on what notice. Arguably the most contested SBL clause.
- **No-advice / non-reliance / risk acknowledgement.** Ties directly to the MiFID/FinSA flag and the "leverage affects suitability" point.
- **Third-party security** (pledgor is not the borrower: spouse, trust, holdco) with waiver of suretyship-type defences. Very common in PWM.

Also worth naming: currency mismatch / FX haircuts, and information undertakings (e.g. duty to notify on becoming an insider).

**Change:** Add the first two to the core twelve; the rest go in the deferred set.

### B5. "Pledge vs charge" is too narrow (B)
Clause 9 should be "security structure": security interest (pledge / charge) **versus title-transfer** collateral arrangement, plus control and custody mechanics. Title transfer is a live option under all three target regimes and changes the insolvency analysis completely.

---

## C. Intake gaps (Module 2)

Missing fields, each of which drives a rule:
- **Pledgor identity distinct from borrower** (third-party security).
- **Is the lender also the custodian?** The single biggest driver of how easy control and perfection are.
- **Loan currency vs. collateral currency** mismatch.
- **Collateral liquidity class**: listed liquid / listed illiquid / fund with dealing frequency and gates / unlisted / structured product. Drives lending value and enforcement realism.
- **Guarantor** present?
- **Other facilities with the lender** (cross-default, cross-collateralisation).
- **Counterparty requests** (optional): a map of clause → requested tier or free text. This lets the demo show "request is below the floor → escalate", the most persuasive thing the tool can do live.

The brief's "is the borrower a consumer?" is a **conclusion**, not an intake fact. Capture facts (natural person? residence? declared HNW or business purpose?) and let a rule raise the consumer-credit flag, with the final determination listed as not-automated.

---

## D. Rules engine (Module 3)

- **No rule schema.** Plan §2.4 gives one: id, `when` with a small `all`/`any` condition grammar, `then` as a list of typed actions, rationale, sources, status.
- **No action taxonomy.** Define: `flag`, `escalate` (hard stop, names who decides), `set_floor`, `set_opening`, `require_cp`, `require_rep`, `note`.
- **No conflict resolution stated.** Resolved by B1: rules only tighten; all contributing rules are logged.
- **Rules in YAML, not Python.** Readability and auditability beat flexibility here. An eight-operator condition grammar covers every example rule in the brief.
- **Rules need tests.** Golden deals (plan §5) with expected flags, escalations and floors per clause.

---

## E. Jurisdictional overlay (Module 4)

The five questions per jurisdiction are right. Two additions that show real understanding, both to be researched and marked `verify` rather than asserted:

- **Natural-person pledgors and the financial collateral safe harbours.** The regimes differ on whether they apply when the collateral provider is an individual. This is the PWM question. Research whether the UK regulations require both parties to be non-natural persons, and how Luxembourg and Switzerland treat individuals. If confirmed, it becomes a rule: individual pledgor + England → safe-harbour treatment uncertain → flag.
- **Which law governs security over intermediated securities** (account-location / PRIMA principle; Hague Securities Convention status differs between Switzerland and the EU/UK). One paragraph per jurisdiction is enough.

Every statement in the overlay carries a source and a `verified` flag. Output prints "[VERIFY]" beside anything not reviewed.

---

## F. Regulatory flags (Module 5)

- Consumer credit needs the **exemption logic**, not just the trigger: HNW and business-purpose style exemptions (UK) and the Swiss thresholds and exclusions. Capture as intake facts; the rule sets severity by which exemption facts are present; final determination not automated.
- Add **bank secrecy / data protection**: trigger on a Swiss booking centre plus any cross-border disclosure (foreign custodian, foreign court).
- Add **financial assistance / corporate benefit** when a corporate pledgor secures someone else's debt.
- Keep CRD/prudential and EMIR as awareness-only, low severity, as the brief says.

---

## G. Missing modules and artefacts

- **Golden deals.** Five or six synthetic deals with expected outputs. Without them nothing is testable and the demo is not repeatable.
- **Not-automated register.** Walkthrough point 3 should be a file the interviewer can be shown, not an ad-lib.
- **Source register** with reliability grading, and a rule against pasting real filed drafting verbatim (paraphrase; short phrases only; no party names).
- **Library versioning in the audit log.** Log the content hash of library and rules with every run so a position traces to the exact version that produced it.
- **README with the demonstrator disclaimer** at the top, and the walkthrough script.
- **Anticipated interview questions** with prepared answers (plan §8).

---

## H. Phase 5 (LLM layer) constraints

The brief correctly puts this last. Add the constraints now so nobody builds it wrong: the model may (a) map counterparty clauses to library IDs and (b) extract intake facts from a draft. It may **never** select a tier or decide an escalation. Its output is labelled unverified and routed through the same deterministic engine. The demo story is then clean: the model reads, the rules decide, the human owns the exceptions.

---

## I. Minor

- Say once that SBL is called **Lombard lending** in Swiss and continental practice. The interviewer may use that term.
- Architecture diagram: the "(source refs)" arrow floats. Sources are a field of the library, not a module.
- "Purpose vs non-purpose" is US Reg U vocabulary. Keep the concept (loan used to buy more securities) but describe it neutrally; the plan does not target US law.
- Section 6 says "stop after Phase 3 if time runs out", but Phase 4 (jurisdiction + flags) is what the posting is actually about. Draft the three jurisdiction notes alongside the clause library, even if stubbed. The optional cut is the intake UI, not the overlay.
