# Not-automated register

This is the list of decisions this demonstrator deliberately does **not** make.

It is a demonstrator built from public sources. It has not been validated against any institution's
credit policy or risk appetite, it carries no regulatory approval, and nothing in it is legal
advice. The register exists for the same reason the status tags and the audit log exist: so that a
reader can tell, without reading the code, exactly where the tool stops and a person starts.

Two kinds of item are collected below.

* **Clause items** are the `not_automated` entries in `playbook/clauses/*.yaml`, carried here
  verbatim and grouped by clause. Section 1 is generated from the YAML, so it cannot drift from the
  library.
* **System-level items** are the eight in `build_plan.md` section 7. They apply on every deal
  regardless of which clauses are in play.

For each item the register records **what the tool does instead** - raise a flag, escalate, tighten
a floor, print a status or a placeholder, or nothing at all - and **why a human must own it**.
"Nothing at all" is a deliberate answer rather than a gap: several of these decisions are taken
after the document is signed, against a live position, on facts that never appear in an intake file.

At run time the markup prints a per-deal subset of the clause items under the heading
**"Not automated on this deal"**: the deduplicated union of the `not_automated` entries of every
clause the run touched, where a clause counts as touched when a rule left an entry in its
`rules_applied`, an escalation names it, or one of its `regulatory_flags` was raised on that run.
This register is the complete list; the run output is the slice that matters for that deal.

---

## 1. Clause items

### Facility type: uncommitted and repayable on demand versus committed term

`facility_type` | `playbook/clauses/01_facility_type.yaml` | risk rating high | default floor `acceptable` | status `draft`

**Whether to exercise the demand right on a live facility, as against forbearing while the relationship is discussed. The clause fixes who decides; it does not decide.**

- *Tool does instead:* Nothing. The clause prints the ladder and the escalation trigger for a conversion request; no rule reads a live exposure.
- *Why a human owns it:* Calling a demand line is a relationship and credit decision taken on the day, against client conduct and market facts that no intake field records.

**Whether to offer committed term at all for relationship reasons, and what that costs in lending value, price and commitment fee.**

- *Tool does instead:* Rule `R11_committed_term` fires only once the deal is already committed: it raises the `events_of_default` floor to `acceptable` and adds a note. The tool never recommends the product.
- *Why a human owns it:* Pricing a commitment trades lending value, fee and capital against a client relationship, and that trade belongs to credit and the business.

**Whether repeated forbearance has made an uncommitted line committed in substance. That is a course-of-dealing judgement, and no rule in this library can make it.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* Course of dealing is a pattern across time and across documents, and the engine sees one deal at one moment.

**Setting the notice period and the term length. Only one opened source states either figure, and both are the institution's risk appetite.**

- *Tool does instead:* Prints `X` inside the fallback text and lists any longer request as an escalation trigger.
- *Why a human owns it:* One opened source states either figure, so both numbers are the institution's risk appetite and only credit can set them.


### Conditions precedent to first and each utilisation

`conditions_precedent` | `playbook/clauses/02_conditions_precedent.yaml` | risk rating high | default floor `fallback` | status `draft`

**Whether a condition has in fact been satisfied. This library lists the items and the rules add to the list; a named person signs each one off.**

- *Tool does instead:* Lists the conditions, and rules `R01`, `R02`, `R05b`, `R07`, `R08` and `R12` append more. It never marks one satisfied.
- *Why a human owns it:* Satisfaction is a documentary judgement that a named person signs off, and that signature is the control.

**Whether to waive a condition and advance anyway, against what undertaking and for how long.**

- *Tool does instead:* Nothing. No action in the rule grammar can remove a condition precedent.
- *Why a human owns it:* A waiver trades perfection or capacity risk for speed, and only the approver named in the clause can price that trade.

**Know-your-client, sanctions and source-of-funds outcomes, including any decision to decline or to exit.**

- *Tool does instead:* Prints them as conditions precedent and repeats them in the run's not-automated section.
- *Why a human owns it:* These are financial-crime determinations reserved to compliance by regulation, not drafting positions.

**Whether the Borrower is a consumer, and therefore whether a declaration and statement had to precede signing.**

- *Tool does instead:* `R03a` raises the `consumer_credit` flag at high severity and escalates where no declaration is recorded; `R03b` raises it at medium where one is.
- *Why a human owns it:* Build plan section 7 reserves the final consumer determination to a human, and the exemption thresholds behind the flag are themselves `[VERIFY]`.

**Whether a legal opinion is required, from whom, and what it must cover on a cross-border structure.**

- *Tool does instead:* Prints the jurisdiction overlay for the deal's governing law; `R12` adds an executed account control agreement as a condition precedent.
- *Why a human owns it:* Scoping an opinion is a cross-border enforceability conclusion, and the tool cites while local counsel confirms.

**Which items belong in Part 1 and which in Part 2 of the fallback schedule on the particular facts. The test is in the rationale; applying it is a judgement.**

- *Tool does instead:* Prints the test in the fallback rationale.
- *Why a human owns it:* Applying “can this still be fixed the day after the money moves?” is a judgement on the facts of the particular file.


### Eligible collateral and lending values by asset class

`eligible_collateral_lending_values` | `playbook/clauses/03_eligible_collateral_lending_values.yaml` | risk rating high | default floor `fallback` | status `draft`

**Whether a specific holding is admitted to the Eligible Collateral Schedule, and at what lending value percentage.**

- *Tool does instead:* Nothing on the individual line. `R06`, `R08`, `R13` and `R15` add notes, and `R06b` and `R15` raise the floor to `acceptable`.
- *Why a human owns it:* Eligibility and the advance rate on a named security are credit decisions, and no public source opened for this playbook publishes a grid to copy.

**Setting the numeric grid itself. The demonstrator carries X placeholders because no public source opened for this playbook publishes one.**

- *Tool does instead:* Prints `X` placeholders in the clause text and repeats the item in the run output.
- *Why a human owns it:* Inventing a number with no source behind it is exactly what build plan section 0 rule 4 forbids.

**Whether an asset that becomes illiquid or restricted after drawdown is re-rated immediately or on notice.**

- *Tool does instead:* `R08` and `R15` raise floors and add notes, but only on the facts recorded at intake.
- *Why a human owns it:* Re-rating is a decision taken on a live position against a market the engine never sees.

**Whether to take a concentrated but high-quality single holding at a reduced lending value rather than excluding it.**

- *Tool does instead:* `R06` and `R06b` tighten the floor and `R06b` escalates to credit.
- *Why a human owns it:* The choice between excluding the holding and discounting it is the very question the escalation exists to put in front of credit.


### Concentration limits by issuer, asset class and currency

`concentration_limits` | `playbook/clauses/04_concentration_limits.yaml` | risk rating high | default floor `fallback` | status `draft`

**Setting the single-name and sector limits themselves. No opened source supports a number; this is the institution's risk appetite and credit owns it.**

- *Tool does instead:* Uses 25 and 50 per cent as the `R06` and `R06b` triggers and prints `X` in the clause text.
- *Why a human owns it:* No opened source supports either figure, so they are credit-policy numbers wearing a rule's clothes.

**Whether two issuers are correlated enough to be treated as one exposure.**

- *Tool does instead:* Nothing. The intake records a largest single-issuer percentage per asset class and no correlation fact.
- *Why a human owns it:* Collapsing two names into one exposure is a risk-modelling judgement with nothing in the intake to support it.

**Whether to grandfather an existing concentrated holding, and at what reduced lending value.**

- *Tool does instead:* `R06` raises the floor to `acceptable` and adds a lending-value haircut note.
- *Why a human owns it:* Grandfathering suspends a limit for a named client, which is a credit concession rather than a drafting tier.

**Whether a concentrated position that is also restricted or PDMR-connected should be taken at all, rather than discounted.**

- *Tool does instead:* `R06`, `R06b`, `R07` and `R08` all fire; two of them escalate.
- *Why a human owns it:* Whether to take the position at all, rather than discount it, is the credit-and-compliance decision the escalations exist to force.


### Lender discretion over valuation, lending values and eligibility

`lender_discretion_valuation` | `playbook/clauses/05_lender_discretion_valuation.yaml` | risk rating high | default floor `fallback` | status `draft`

**Whether a particular market move is a "rapid decline" that collapses the notice period. The clause defines who decides, not what the answer is.**

- *Tool does instead:* Prints the carve-out and the escalation trigger attached to it.
- *Why a human owns it:* The clause fixes who decides; whether today's move qualifies is a judgement on live market data the engine does not hold.

**Whether to exercise the discretion at all on a live position, as against forbearing while the relationship is discussed.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* Forbearance is a relationship decision taken outside the document and after it is signed.

**Setting the notice period itself. Only one opened source concedes one (15 days) and the number here is the institution's risk appetite.**

- *Tool does instead:* Prints `X`; `R13` raises this clause's floor to `acceptable` where there is a currency mismatch.
- *Why a human owns it:* The only observation behind the number is a single sub-part of a single filing, so the operative figure is risk appetite.

**Whether to disclose the full haircut matrix to a counterparty who asks for it during negotiation.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* Disclosing the Bank's own risk methodology in a negotiation is a confidentiality and strategy call, not a clause position.


### Margin maintenance, margin call mechanics and cure period

`margin_maintenance_cure` | `playbook/clauses/06_margin_maintenance_cure.yaml` | risk rating high | default floor `fallback` | status `draft`

**Whether to grant forbearance on a live margin call, or to let an expired cure period stand without enforcing.**

- *Tool does instead:* Nothing. Build plan section 7 lists it, and the run output repeats it whenever this clause is touched.
- *Why a human owns it:* Forbearance is decided against a live shortfall on facts that no intake field records.

**Whether a written cure plan is credible, which is a judgement about a funding source and not a document check.**

- *Tool does instead:* Prints the fallback tier's conditions.
- *Why a human owns it:* Judging whether a funding source will actually arrive is a credit assessment, not a document check.

**Setting the Trigger Level, the Restoration Level, the Hard Floor and the number of business days. The sources give a band, not an answer.**

- *Tool does instead:* Prints the `X`, `Y` and `Z` placeholders; `R06` raises the floor to `acceptable` on a concentrated portfolio.
- *Why a human owns it:* The opened sources give a band and one two-level retail structure, which is not an answer for this institution.

**Whether a particular market move is a "rapid decline" that stops the cure clock.**

- *Tool does instead:* Prints the carve-out.
- *Why a human owns it:* The same live-market judgement as the valuation clause, and here it decides whether the borrower gets any time at all.

**Whether to call at all on a relationship where the shortfall is small and the portfolio is recovering.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* Deciding not to call is a relationship decision, and repeating it is the course-of-dealing risk the facility-type clause warns about.


### Security structure: pledge, charge or title transfer, plus control and custody

`security_structure_control` | `playbook/clauses/07_security_structure_control.yaml` | risk rating high | default floor `fallback` | status `draft`

**Whether a particular custodian's standard control agreement actually delivers control under the law of the account's location. The tool prints the question; local counsel answers it.**

- *Tool does instead:* `R12` adds an executed account control agreement as a condition precedent, raises the floor to `acceptable` and prints the jurisdiction overlay for the account's law.
- *Why a human owns it:* Perfection under the law of the account's location is a local counsel conclusion; the tool prints the question and cites, and counsel answers it.

**Whether to accept a client's existing custody relationship at all, which is a relationship decision as much as a credit one.**

- *Tool does instead:* `R12` tightens the floor and adds a per-jurisdiction note on control.
- *Why a human owns it:* Taking on a third-party custodian is an operations and relationship decision as much as a credit one.

**The classification of the client that determines whether title transfer is available in the booking jurisdiction.**

- *Tool does instead:* `R04` raises `fcar_safe_harbour_uncertain` where a natural person provides collateral under English law.
- *Why a human owns it:* Classification turns on regulatory status facts the intake does not capture, and the safe-harbour point behind the flag is itself `[VERIFY]`.

**Whether to register a charge protectively for a corporate chargor where reliance on the financial collateral regime is doubtful.**

- *Tool does instead:* Prints the England and Wales jurisdiction note on registration and on the disapplication.
- *Why a human owns it:* Paying for belt-and-braces registration where reliance on the financial collateral regime is doubtful is an institutional policy choice.

**Setting the substitution threshold and the acknowledgement deadline. No opened source publishes either.**

- *Tool does instead:* Prints the `Y` placeholder.
- *Why a human owns it:* No opened source publishes either number, so both are risk appetite stated as drafting.


### Events of default, including insolvency, death or incapacity and material adverse change

`events_of_default` | `playbook/clauses/08_events_of_default.yaml` | risk rating high | default floor `fallback` | status `draft`

**Whether a material adverse change or a substantial deterioration has actually occurred on a live position. The clause fixes who decides and on what standard; it does not decide.**

- *Tool does instead:* `R11` raises this clause's floor to `acceptable` on a committed facility and adds a material adverse change note.
- *Why a human owns it:* The clause fixes who decides and on what standard; the determination itself is made on live facts after signing.

**Whether to call a default at all, as against forbearing while the relationship is discussed. Forbearance on a live margin call and waiver of an event of default are both human decisions.**

- *Tool does instead:* Nothing. Build plan section 7 reserves waiver of an event of default.
- *Why a human owns it:* Calling or waiving a default is a relationship, credit and conduct decision taken together, and it is hard to reverse.

**Whether an individual has lost legal capacity, and whether an attorney, deputy or other representative can give instructions that bind the Borrower or the Pledgor. [VERIFY] no mental-capacity source was opened for this playbook.**

- *Tool does instead:* Nothing. The item carries `[VERIFY]` and prints with it.
- *Why a human owns it:* No mental-capacity source was opened for this playbook, and the intake records no fact that would answer the question.

**Whether to enforce against a deceased individual's collateral before the estate is administered, which is a reputational and conduct decision as much as a legal one.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* It is a reputational and conduct decision as much as a legal one, and it is taken while an estate is being administered.

**Setting the payment grace, covenant cure and death standstill periods. Only the institutional grace periods are observed in a source; the standstill is not observed at all.**

- *Tool does instead:* Prints `X`.
- *Why a human owns it:* Only the institutional grace periods are observed in a source; the death standstill is unobserved and is a proposal, not a market position.


### Enforcement and liquidation: notice, standard of conduct and self-help sale

`enforcement_liquidation` | `playbook/clauses/09_enforcement_liquidation.yaml` | risk rating high | default floor `fallback` | status `draft`

**The decision to enforce at all, as against forbearing while the relationship is discussed. The tool never makes that call.**

- *Tool does instead:* `R07`, `R08` and `R15` raise the floor to `acceptable` and the ladder prints; build plan section 7 reserves the decision itself.
- *Why a human owns it:* It is the most consequential judgement in the product and the tool never makes it.

**Whether a particular market move is a "rapid decline" that removes the notice period.**

- *Tool does instead:* Prints the carve-out.
- *Why a human owns it:* A live-market judgement, and here it decides whether the borrower is told before the sale.

**Whether a proposed sale method is commercially reasonable on the facts of the day, including the choice between a bookbuild, a programme and a private placement.**

- *Tool does instead:* Prints the standard and the pre-agreed acknowledgements of what is commercially reasonable.
- *Why a human owns it:* What is reasonable on the day depends on book depth and market conditions the engine never sees.

**Whether a closed period, an issuer or underwriter consent or a volume limit blocks or delays a sale, and whether compliance has cleared it.**

- *Tool does instead:* `R07` raises `market_abuse` at high severity and escalates to senior lawyer and compliance; `R08` raises `restricted_securities` and adds an issuer-consent condition precedent.
- *Why a human owns it:* Build plan section 7 reserves clearing a PDMR or insider position with compliance, and the timing of a sale is where that bites.

**Whether notice is required by law and unwaivable in the booking jurisdiction, and on whom it must be served where the Pledgor is not the Borrower.**

- *Tool does instead:* Prints the jurisdiction overlay, including the Swiss point that pre-realisation notice cannot be waived by a party who is neither a custodian nor a qualified investor.
- *Why a human owns it:* It is a cross-border enforceability conclusion, and the printed overlay is a citation rather than a confirmation.

**Setting the notice period. Three observations exist across one composite filing, and the number is risk appetite.**

- *Tool does instead:* Prints `X`.
- *Why a human owns it:* Three observations across one composite filing is not a market norm, so the number is risk appetite.


### Capacity, authority and due execution for trusts, corporates and partnerships

`capacity_authority` | `playbook/clauses/10_capacity_authority.yaml` | risk rating high | default floor `fallback` | status `draft`

**Reading the trust instrument. No rule in this library can tell anyone whether a power to borrow or to charge exists; a lawyer reads the deed and every deed of appointment, retirement and variation behind it.**

- *Tool does instead:* `R01` adds a trust deed review as a condition precedent, requires a trustee capacity and power representation, and raises the floor to `acceptable`.
- *Why a human owns it:* No rule can tell anyone whether a power to borrow or charge exists; a lawyer reads the deed and everything behind it.

**Whether a limited recourse request is safe on the facts. It turns on the state of the indemnity, the standing of the trustee and the assets actually in the fund, none of which is an intake field.**

- *Tool does instead:* Prints the fallback tier's conditions and its named approver.
- *Why a human owns it:* It turns on the state of the trustee's indemnity, the standing of the trustee and the assets actually in the fund, none of which is an intake field.

**Whether a corporate pledgor has corporate benefit, and whether the law of its incorporation restricts financial assistance, upstream or cross-stream security. This is a local counsel question on every deal where the pledgor is not the borrower.**

- *Tool does instead:* `R05b` raises `financial_assistance_corporate_benefit` and adds a condition precedent; the non-English half of that flag is `[VERIFY]`.
- *Why a human owns it:* It is a local counsel question on every deal where the pledgor is not the borrower, and the library has no primary text outside England.

**Whether independent legal advice was genuinely given, genuinely independent and genuinely understood.**

- *Tool does instead:* `R05` requires a representation that the pledgor took independent advice.
- *Why a human owns it:* The representation records that advice was taken; whether it was real, independent and understood is a judgement about a conversation.

**Whether an individual had capacity at signing, and what the Bank does on incapacity short of death. The intake records no fact that answers either, and the treatment of incapacity is an identified gap in this library.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* Incapacity short of death is an identified gap in this library and the intake records no fact that answers it.

**Whether to accept a foreign-law legal opinion in the form offered, and what it must cover.**

- *Tool does instead:* Prints the jurisdiction overlay for the deal's governing law.
- *Why a human owns it:* Scoping and accepting an opinion is a legal judgement reserved to the deal lawyer with local counsel.


### Governing law, jurisdiction and service of process

`governing_law_jurisdiction` | `playbook/clauses/11_governing_law_jurisdiction.yaml` | risk rating high | default floor `fallback` | status `draft`

**Every cross-border perfection and enforceability conclusion. The playbook cites the rule; local counsel in the account's jurisdiction confirms it, and that confirmation is a condition precedent, not a drafting note.**

- *Tool does instead:* Prints the jurisdiction file for the deal's governing law, with its sources, `verified` values and `[VERIFY]` markers.
- *Why a human owns it:* Build plan section 7 puts it plainly: the tool cites and local counsel confirms, and that confirmation is a condition precedent, not a drafting note.

**Whether an asymmetric jurisdiction clause will be given effect in the forum where the Bank would actually use it. [VERIFY] not sourced for this playbook.**

- *Tool does instead:* Prints the tier with its `[VERIFY]` marker.
- *Why a human owns it:* Whether a forum honours a one-sided clause is unsourced for this playbook and turns on that forum's own law.

**Choosing the booking centre for a new relationship, which is a commercial, tax and regulatory decision as well as a legal one.**

- *Tool does instead:* `R14` switches the jurisdiction overlay and raises `bank_secrecy_data` on a Swiss booking.
- *Why a human owns it:* It is a commercial, tax and regulatory decision as well as a legal one, and it is taken before any clause is drafted.

**Whether to commence proceedings in a second jurisdiction, and the disclosure of client information that doing so entails in a bank-secrecy jurisdiction.**

- *Tool does instead:* `R14` adds a note on `confidentiality_bank_secrecy`.
- *Why a human owns it:* Suing abroad discloses client information in a bank-secrecy jurisdiction, which legal and compliance in the booking centre own.

**Whether the Borrower or the Pledgor is capable of claiming immunity at all, which turns on its constitution and on the law of the place of enforcement.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* It turns on the counterparty's own constitution and on the law of the place of enforcement, neither of which is an intake fact.


### No advice, non-reliance and risk acknowledgement

`no_advice_non_reliance` | `playbook/clauses/12_no_advice_non_reliance.yaml` | risk rating high | default floor `fallback` | status `draft`

**Every suitability and appropriateness conclusion. The tool records the purpose, raises the flag and tightens the floor; a person in compliance decides whether the leveraged position is suitable.**

- *Tool does instead:* `R10` raises `mifid_suitability` and tightens this clause's floor to `acceptable`.
- *Why a human owns it:* Build plan section 7 reserves suitability conclusions, and the flag names compliance as the decider.

**Whether the relationship is in fact execution-only, advisory or discretionary on the pledged portfolio. The clause must match the answer, and the answer is a fact about what people did, not a drafting choice.**

- *Tool does instead:* Nothing. The intake has no relationship-type field.
- *Why a human owns it:* It is a fact about what people actually did, not a drafting choice, and the clause is only defensible if it matches that fact.

**Whether a particular conversation between the relationship manager and the client amounted to a personal recommendation.**

- *Tool does instead:* Nothing.
- *Why a human owns it:* Whether something was a personal recommendation is a conduct determination on evidence the tool never sees.

**The final determination that a borrower is or is not a consumer or a retail client, which drives the withdrawal right, the risk-disclosure package and the classification of the facility.**

- *Tool does instead:* `R03a` and `R03b` raise `consumer_credit` at high or medium severity, and `R03a` escalates where no declaration is recorded.
- *Why a human owns it:* Build plan section 7 reserves the final determination, and the thresholds behind the flag are `[VERIFY]`.

**Whether to decline the facility outright because the leveraged position is unsuitable, notwithstanding that the collateral supports it.**

- *Tool does instead:* Raises flags and escalations, and never declines.
- *Why a human owns it:* Turning business away is the institution's decision and no document can make it.


### Deferred stub clauses

These twelve clauses exist so that rules can reference them and so that the markup shows the shape of the full library. They are `status: stub`, carry no positions and therefore have no `not_automated` entries yet. The tool prints them with a `[STUB]` tag and nothing else, so every decision under them is, for now, entirely a human's.

- `interest_benchmark_fallbacks` - Interest, benchmark rate and benchmark fallback provisions
- `prepayment_breakage` - Prepayment and breakage costs
- `collateral_substitution` - Collateral substitution rights
- `cross_collateral_set_off` - Cross-collateralisation and set-off
- `reps_source_of_funds_sanctions_tax` - Representations on source of funds, sanctions and tax status
- `purpose_restrictions` - Purpose restrictions and permitted use of proceeds
- `transfer_assignment` - Transfer and assignment
- `confidentiality_bank_secrecy` - Confidentiality, bank secrecy and permitted disclosure
- `tax_gross_up` - Tax gross-up and withholding
- `third_party_security_waivers` - Third-party security: suretyship-type defences and waivers
- `information_undertakings` - Information undertakings and duty to notify
- `currency_mismatch_fx` - Currency mismatch and foreign exchange haircuts

---

## 2. System-level items

From `build_plan.md` section 7. These apply on every deal, whichever clauses are in play. Several are also carried by a clause above; they are repeated here because they hold even on a deal where that clause is never touched.

**1. The final determination that a borrower is or is not a consumer under any regime.**

- *Tool does instead:* `R03a` raises the `consumer_credit` flag at high severity and escalates; `R03b` raises it at medium where a high-net-worth or business declaration is recorded. The flag names senior lawyer and compliance as the deciders.
- *Why a human owns it:* The exemption logic turns on declarations, thresholds and the lender's own state of mind about the borrower's purpose, and the threshold figures in the flag are `[VERIFY]`.

**2. Any concession below a clause's floor, and any request at `unacceptable`.**

- *Tool does instead:* The built-in counterparty-request check (`R16`, implemented in the engine rather than in `rules.yaml`) records the outcome as `accepted_within_floor`, `below_floor_escalated` or `unacceptable_escalated`, escalates the last two, and sets the run's exit code to 2.
- *Why a human owns it:* The floor is the point at which the library stops deciding; going below it is a named person accepting a loss of protection, which is the whole purpose of the approver field.

**3. Clearing a PDMR or insider position with compliance.**

- *Tool does instead:* `R07_pdmr_pledged_issuer` raises `market_abuse` at high severity, escalates to senior lawyer and compliance, tightens `enforcement_liquidation` to `acceptable`, and adds an insider-status representation and a compliance sign-off condition precedent.
- *Why a human owns it:* Whether a pledge or an enforcement sale can proceed depends on closed periods, disclosure obligations and issuer consents that only compliance can check against live facts.

**4. Suitability or appropriateness conclusions.**

- *Tool does instead:* `R10_purpose_acquire_securities` raises `mifid_suitability` and tightens `no_advice_non_reliance` to `acceptable`; the flag names compliance as the decider.
- *Why a human owns it:* Suitability is a conclusion about a client's circumstances and understanding, which is not a fact the intake carries and not a position a clause can take.

**5. Any cross-border perfection or enforceability conclusion.**

- *Tool does instead:* Prints the jurisdiction file for the deal's governing law with its sources, `verified` values and `[VERIFY]` markers, and `R12` makes an executed account control agreement a condition precedent where the lender is not the custodian.
- *Why a human owns it:* The library cites public law; local counsel in the account's jurisdiction confirms it, and that confirmation is a condition precedent rather than a drafting note.

**6. Sanctions, know-your-client and source-of-funds outcomes.**

- *Tool does instead:* Prints them as conditions precedent under `conditions_precedent`, and repeats them in the run's not-automated section.
- *Why a human owns it:* These are financial-crime determinations reserved to compliance by regulation, and a negative outcome ends the deal rather than moving a tier.

**7. Forbearance on a live margin call, waiver of an event of default, and the decision to enforce.**

- *Tool does instead:* Nothing. The relevant clauses print their ladders, and rules `R06`, `R07`, `R08`, `R11` and `R15` tighten floors at intake only.
- *Why a human owns it:* All three are decisions taken after signature, against a live position, on facts the engine has never seen.

**8. Promotion of any entry from `draft` to `reviewed`.**

- *Tool does instead:* Prints the status tag (`[REVIEWED]`, `[DRAFT]`, `[STUB]`) beside every clause, counts them in the run header, and prints a standing warning that unreviewed positions are not the lender's settled position. Agents may write `stub` or `draft` only.
- *Why a human owns it:* `reviewed` is a named human's signature on a position, with `reviewed_by` and `last_reviewed` filled, and it is the only thing that would make the library usable.

---

## 3. Counts

- Clause items carried: **59**, across **12** drafted clauses.
- Deferred stub clauses with no items yet: **12**.
- System-level items: **8**.

Section 1 is generated from `playbook/clauses/*.yaml` by `scripts/gen_not_automated_register.py`. If a clause gains or loses a `not_automated` entry, rerun that script rather than editing this file by hand: it carries every entry verbatim and fails loudly on any entry it has no annotation for, so an item cannot be dropped silently.
