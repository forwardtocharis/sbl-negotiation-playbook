# SBL negotiation markup — D91

- Deal: D91
- Description: Synthetic fixture. Aldergrove Trust, a Jersey discretionary trust, concentrated single-stock portfolio, settlor is a PDMR of the pledged issuer.
- Run id: 3d8e5c1f0a97b246
- Timestamp: 2026-09-21T11:42:07+00:00
- Library hash: 2bb077b8162abbd6094351ca30b7a7b30ecab21209d4a3cdf2a522ca3d893e58
- Intake hash: a71b3c5d9e02f4681c3a5b7d9e0f2143658a7b9c0d1e2f3a4b5c6d7e8f901234
- Governing law: england_wales
- Review status: 0 reviewed / 12 draft / 12 stub

Status warning: positions tagged [DRAFT] or [STUB] have not been reviewed by a named human reviewer and must not be relied on as the lender's settled position.

## Escalations

| Rule id | Clause | Who decides | Reason |
| --- | --- | --- | --- |
| R16_counterparty_request_below_floor | lender_discretion_valuation | Credit committee | Counterparty requested tier 'fallback' on lender_discretion_valuation, which is below the computed floor 'acceptable' for this deal. |
| R16_counterparty_request_below_floor | enforcement_liquidation | Senior lawyer and credit committee | Counterparty requested the unacceptable tier on enforcement_liquidation: no sale without the borrower's prior written consent is the walk-away line and nobody may agree it. |

Exit code: 2

## Flags

### High severity

- **market_abuse** — The pledgor is a PDMR of the pledged issuer, so the pledge and any enforcement sale may constitute dealing; closed periods and disclosure obligations apply.
  - Who decides: Compliance, with the senior deal lawyer
  - Triggering rule: R07_pdmr_pledged_issuer

### Medium severity

- **fcar_safe_harbour_uncertain** — [VERIFY] Whether the financial collateral regime extends to this collateral provider has not been confirmed against the primary text; treat the perfection and enforcement shortcuts as unavailable until it is.
  - Who decides: Senior lawyer, on local counsel advice
  - Triggering rule: R04_natural_person_pledgor_england

### Low severity

- **prudential_awareness** — Concentrated single-name collateral affects the lender's own large-exposure and capital reporting; raise with the credit team before the facility is sized.
  - Who decides: Credit risk
  - Triggering rule: R06b_concentration_severe

## Clause-by-clause

### Facility type: uncommitted demand or committed term [DRAFT]

- Clause id: facility_type
- Risk rating: high
- Category: credit
- Document: facility_letter

**Opening: preferred**

> The facility is uncommitted and repayable on demand. The lender may decline any utilisation request and may demand repayment in full at any time, without cause and without any event of default having occurred.

Rationale: An uncommitted demand facility is the lender's primary protection in securities-backed lending. It lets the lender exit before the collateral deteriorates without having to prove a default, which is what makes the rest of the risk framework workable.

**Floor: fallback** — approver: Senior lawyer, with credit sign-off on the term

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The facility is uncommitted and repayable on demand. | — | — |
| acceptable | The facility is uncommitted and repayable on demand, save that where no event of default is continuing the lender will give X business days' notice before deman... | Notice period no longer than X business days; No notice requirement where an event of default is continuing or a margin call is unmet | — |
| fallback | The facility is a committed term facility of X months, terminable by the lender on an event of default or on an unremedied margin shortfall, and not otherwise. | Unremedied margin shortfall is an express termination event; Term no longer than X months with no extension right in the borrower | Senior lawyer, with credit sign-off on the term |
| unacceptable (description of the walk-away line, not drafting) | A committed facility under which the lender cannot terminate for an unremedied margin shortfall, or under which the demand right is subject to a cure period the... | — | — |

**Escalation triggers**

- Any request to commit an uncommitted line for longer than X months
- Any request to make demand conditional on borrower agreement

**Jurisdiction note (england_wales)**

Under English law the on-demand characterisation is a matter of drafting rather than a statutory category, so the facility letter must say plainly that the facility is uncommitted and repayable on demand.

Rules applied: none

### Conditions precedent to first and each utilisation [DRAFT]

- Clause id: conditions_precedent
- Risk rating: high
- Category: credit
- Document: facility_letter

**Opening: preferred**

> No utilisation is available until the lender has confirmed in writing that it has received each condition precedent in form and substance satisfactory to it, including completed onboarding checks, constitutional and authority documents, executed security documents and evidence of perfection.

Rationale: Conditions precedent are the gate through which capacity, authority and perfection are cleared before money moves. Satisfaction in the lender's own judgement is the point: a reasonableness standard invites argument at the moment the lender least wants one.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | No utilisation is available until the lender has confirmed in writing that it has received each condition precedent in form and substance satisfactory to it, in... | — | — |
| acceptable | No utilisation is available until the lender confirms receipt of each condition precedent in form and substance satisfactory to it, acting reasonably, with an a... | The annexed list is exhaustive only as to documents, not as to the lender's onboarding outcome | — |
| fallback | The lender may waive or defer a condition precedent other than onboarding clearance, executed security documents and evidence of perfection, which may not be wa... | Deferral period no longer than X business days; No further utilisation while a deferred condition remains outstanding | Senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | Utilisation permitted before onboarding clearance, before the security documents are executed, or before the perfection steps for the relevant jurisdiction have... | — | — |

**Escalation triggers**

- Any request to utilise before perfection is evidenced
- Any request to waive onboarding clearance

**Conditions precedent added by rules**

- [R07_pdmr_pledged_issuer] Compliance sign-off on the pledgor's insider status and on any issuer consent requirement, obtained before the term sheet is issued.
- [R08_restricted_securities] Review of any lock-up, control-stock or transfer restriction affecting the pledged securities, with issuer consent obtained where required.
- Board minute of the custodian confirming the pledged account has been blocked to the lender's instructions.

**Drafting notes**

- [VERIFY] Whether issuer consent is required for the pledge itself, as distinct from an enforcement sale, has not been confirmed against a primary source.

**Jurisdiction note (england_wales)**

For an English law security agreement over intermediated securities, the perfection condition precedent should be tied to the control arrangements actually put in place, not to execution of the document alone.

Rules applied: R07_pdmr_pledged_issuer, R08_restricted_securities

### Eligible collateral and lending values [DRAFT]

- Clause id: eligible_collateral_lending_values
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> Only assets the lender has designated as eligible carry a lending value. Lending values are set by the lender by asset class and may be varied, reduced to zero, or an asset class removed from eligibility, at any time.

Rationale: The lending value schedule is the mechanism by which the lender prices collateral risk in real time. Fixing it in the document converts a risk control into a negotiated term that ages badly.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Only assets the lender has designated as eligible carry a lending value. | — | — |
| acceptable | Lending values are set out in a schedule by asset class. | Notification is after the event, never a precondition to the variation | — |
| fallback | The lender may vary lending values at any time; where the variation is not driven by a market, issuer or regulatory event the lender will give X business days'... | No notice where the variation follows a market, issuer, liquidity or regulatory event; Diversified collateral pool with no single name above X per cent of lending value | Senior lawyer, with credit sign-off on the notice period |
| unacceptable (description of the walk-away line, not drafting) | Lending values fixed for the life of the facility, or variable only with the borrower's consent or only on objectively defined external triggers. | — | — |

**Escalation triggers**

- Any request to fix lending values for a defined period
- Any request to make a variation subject to borrower consent

**Drafting notes**

- [R13_currency_mismatch] Collateral currencies include a currency other than the facility currency; apply the FX haircut to the non-matching lines.

**Jurisdiction note (england_wales)**

English law does not imply a reasonableness constraint on a contractual discretion of this kind automatically, but a discretion framed as wholly unfettered is more likely to be read down, so the rationale for a variation should be recorded at the time. [VERIFY] Not confirmed against a primary authority the drafting agent opened.

Rules applied: R06b_concentration_severe, R13_currency_mismatch

### Concentration limits on the collateral pool [DRAFT]

- Clause id: concentration_limits
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> No single issuer may account for more than X per cent of aggregate lending value. Lending value in excess of the limit is disregarded, and the lender may tighten the limit at any time.

Rationale: Disregarding the excess rather than triggering a default gives the lender an automatic, self-executing control that needs no notice and no decision.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | No single issuer may account for more than X per cent of aggregate lending value. | — | — |
| acceptable | No single issuer may account for more than X per cent of aggregate lending value. | The disregard mechanism itself is never subject to notice | — |
| fallback | Single-issuer concentration above X per cent is permitted for a named list of index-constituent issuers at a reduced lending value agreed at the outset. | Named issuers are liquid index constituents only; Reduced lending value of no more than X per cent applies to the excess; No restricted or lock-up securities in the carve-out | Credit committee |
| unacceptable (description of the walk-away line, not drafting) | No single-issuer limit at all, or a limit expressed as a target the breach of which has no consequence. | — | — |

**Escalation triggers**

- Any request to disapply the single-issuer limit entirely

**Drafting notes**

- [R06_concentration] Single-name exposure is above the playbook threshold; apply the reduced lending value to the excess rather than negotiating the limit itself.

Rules applied: R06_concentration, R06b_concentration_severe

### Lender discretion over valuation and eligibility [DRAFT]

- Clause id: lender_discretion_valuation
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> The lender determines the value of each asset in the collateral pool, the source and timing of prices used, and whether an asset remains eligible. Its determination is conclusive save for manifest error.

Rationale: Valuation is where the margin mechanics start. A contested valuation at the moment of a margin call is a contested margin call, and the facility cannot carry that risk.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The lender determines the value of each asset in the collateral pool, the source and timing of prices used, and whether an asset remains eligible. | — | — |
| acceptable | The lender determines value and eligibility acting in good faith and using pricing sources of a kind customarily used for assets of that type. | Manifest error remains the only challenge route | — |
| fallback | The lender determines value and eligibility acting reasonably. | No suspension of any margin call, cure period or enforcement step during a dispute; Borrower bears the cost of the second price | Senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | Any valuation dispute mechanism that suspends a margin call, extends a cure period, or delays enforcement while the dispute is resolved. | — | — |

**Escalation triggers**

- Any request for a valuation dispute right that suspends a margin call
- Any request to name a single external pricing source as binding

**Drafting notes**

- [R16_counterparty_request_below_floor] Counterparty asked for the fallback tier, which is below the computed floor for this deal; escalated rather than conceded.

**Jurisdiction note (england_wales)**

An English law contractual discretion of this kind is likely to be subject to an implied duty to act honestly and not arbitrarily, so the good-faith formulation at the acceptable tier is close to the position a court would reach anyway. [VERIFY] Not confirmed against a primary authority.

Rules applied: R16_counterparty_request_below_floor

### Margin maintenance, margin call mechanics and cure period [DRAFT]

- Clause id: margin_maintenance_cure
- Risk rating: high
- Category: collateral
- Document: security_agreement

**Opening: preferred**

> If at any time the aggregate lending value falls below the outstanding amount, the borrower must cure the shortfall by the close of business on the next business day, by posting eligible collateral or prepaying. Notice may be given by any agreed channel and is effective on despatch.

Rationale: A one-day cure keeps the lender's exposure to a falling portfolio to a single trading session. Effectiveness on despatch stops a dispute about receipt becoming a dispute about the call.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | If at any time the aggregate lending value falls below the outstanding amount, the borrower must cure the shortfall by the close of business on the next busines... | — | — |
| acceptable | The borrower must cure a shortfall within X business days of notice. | Lender retains the right to shorten the cure period for a large shortfall; Notice remains effective on despatch | — |
| fallback | The borrower must cure a shortfall within X business days of notice, with notice effective on receipt, provided that the cure period does not extend past the le... | Diversified collateral only, with no single name above X per cent of lending value; Daily-priced listed assets only; no gated funds, unlisted holdings or structured products; No cure period at all once an event of default is continuing | Credit committee, with the concession recorded on the file |
| unacceptable (description of the walk-away line, not drafting) | A cure period that runs from the borrower's acknowledgement of the call, or that may be extended at the borrower's request, or that continues to run after an ev... | — | — |

**Escalation triggers**

- Any request for a cure period longer than X business days
- Any request to make notice effective on acknowledgement

**Drafting notes**

- [R06_concentration] Concentrated pool: keep the right to shorten the cure period for a large shortfall, which is the protection that actually operates here.

**Jurisdiction note (england_wales)**

Where the security is intended to benefit from the English financial collateral regime, the margin mechanics should be drafted so that top-up collateral falls within the same security and control arrangements as the original pool.

Rules applied: R06_concentration

### Security structure, perfection and control of the pledged account [DRAFT]

- Clause id: security_structure_control
- Risk rating: high
- Category: collateral
- Document: security_agreement

**Opening: preferred**

> The borrower grants a first-ranking security interest over the pledged account and everything credited to it. Where the lender is not the custodian, an account control agreement in the lender's form is a condition precedent, and the custodian acts on the lender's instructions alone from the date of the facility.

Rationale: Control is what makes the security enforceable in practice rather than only on paper. A pledge over an account the lender cannot direct is an unsecured claim with extra documents.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The borrower grants a first-ranking security interest over the pledged account and everything credited to it. | — | — |
| acceptable | The borrower grants a first-ranking security interest over the pledged account. | Lender may give a notice of exclusive control at any time without cause; Custodian must acknowledge the control agreement before first utilisation | — |
| fallback | The borrower may continue to deal in the pledged account within agreed parameters until a notice of exclusive control is given, and the lender will notify the b... | Dealing parameters are expressed as eligibility and concentration limits already in the facility; No advance notice to the borrower before the custodian is notified | Senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | Any structure in which the custodian may act on the borrower's instructions after a control notice, or in which the lender must give the borrower advance notice... | — | — |

**Escalation triggers**

- Any request for advance notice before a control notice
- Any third-party custodian unwilling to sign the control agreement

**Jurisdiction note (england_wales)**

For an English law pledge over intermediated securities, possession or control is the practical perfection route; where the chargor is a company, consider whether the financial collateral regime disapplies the usual registration requirement. [VERIFY] Registration disapplication not confirmed against the primary text.

Rules applied: none

### Events of default [DRAFT]

- Clause id: events_of_default
- Risk rating: high
- Category: default_enforcement
- Document: facility_letter

**Opening: preferred**

> Events of default include non-payment, breach of any undertaking, an unremedied margin shortfall, insolvency or any analogous step, death or loss of capacity of an individual borrower or pledgor, any event the lender considers materially adverse, and any cross-default.

Rationale: On a demand facility the list matters less for stopping the lending, which needs no default, and more for unlocking enforcement against the collateral without further notice.

**Floor: fallback** — approver: Senior lawyer

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Events of default include non-payment, breach of any undertaking, an unremedied margin shortfall, insolvency or any analogous step, death or loss of capacity of... | — | — |
| acceptable | Events of default as above, with breaches of undertakings subject to a grace period of X business days where the breach is capable of remedy, and cross-default... | No grace period for non-payment, unremedied margin shortfall or insolvency | — |
| fallback | Events of default as above, with the material adverse change trigger qualified by reference to the borrower's ability to perform its payment and margin obligati... | Margin shortfall, insolvency and death or incapacity triggers remain unqualified | Senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | Removal of the unremedied margin shortfall trigger, or of death or loss of capacity for an individual borrower or pledgor. | — | — |

**Escalation triggers**

- Any request to remove the death or incapacity trigger

Rules applied: none

### Enforcement and liquidation of the collateral [DRAFT]

- Clause id: enforcement_liquidation
- Risk rating: high
- Category: default_enforcement
- Document: security_agreement

**Opening: preferred**

> On an event of default or an unmet demand the security becomes immediately enforceable and the lender may sell, appropriate or otherwise realise any or all of the collateral, at such time, in such order and on such terms as it thinks fit, without prior notice to the borrower.

Rationale: The lender's realisation window is measured in hours. A notice requirement or a prescribed order of realisation gives that window away at exactly the wrong moment.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | On an event of default or an unmet demand the security becomes immediately enforceable and the lender may sell, appropriate or otherwise realise any or all of t... | — | — |
| acceptable | The lender may realise any or all of the collateral by whichever route it elects (sale \| appropriation) without prior notice, and will notify the borrower promp... | Notification is always after the event, never before; Choice of realisation route (sale \| appropriation) stays with the lender | — |
| fallback | The lender will use reasonable endeavours to give the borrower X hours' notice before the first realisation step, save where the lender considers that delay wou... | Express carve-out where delay would prejudice the realisation; No notice obligation at all where the pledgor is subject to a market abuse or insider restriction; Diversified, daily-priced collateral only | Credit committee, with the concession recorded on the file |
| unacceptable (description of the walk-away line, not drafting) | Any requirement for the borrower's prior written consent to a sale, or a fixed notice period with no carve-out, or an obligation to realise in a borrower-specif... | — | — |

**Escalation triggers**

- Any request for prior consent to a sale
- Any request for a fixed notice period without a prejudice carve-out

**Representations/undertakings added by rules**

- [R08_restricted_securities] The pledgor represents that no lock-up, standstill or transfer restriction applies to the pledged securities other than those disclosed to the lender in writing.

**Drafting notes**

- [R07_pdmr_pledged_issuer] An enforcement sale may itself be dealing while the pledgor is an insider; the realisation route (sale | appropriation) must be cleared with compliance before any step is taken.
- [R16_counterparty_request_below_floor] Counterparty asked for the unacceptable tier. Hard escalation; nobody may agree this.

**Jurisdiction note (england_wales)**

Under English law, where the arrangement falls within the financial collateral regime, appropriation may be available as an alternative to sale provided the agreement expressly permits it and a commercially reasonable valuation basis is specified. [VERIFY] Scope of the regime as regards a natural-person collateral provider not confirmed against the primary text.

Rules applied: R07_pdmr_pledged_issuer, R08_restricted_securities, R16_counterparty_request_below_floor

### Capacity, authority and constitutional power [DRAFT]

- Clause id: capacity_authority
- Risk rating: high
- Category: parties_reps
- Document: facility_letter

**Opening: preferred**

> Each of the borrower and the pledgor represents, on the date of the facility and on each utilisation, that it has full power to enter into and perform the finance documents and to grant the security, that all necessary authorisations have been obtained, and that no constitutional or fiduciary restriction is breached.

Rationale: Capacity is the risk that does not show up until enforcement, and by then it is unfixable. A repeated representation keeps the position current rather than frozen at signing.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Each of the borrower and the pledgor represents, on the date of the facility and on each utilisation, that it has full power to enter into and perform the finan... | — | — |
| acceptable | Representations as above, given on the date of the facility and repeated on each utilisation, with the fiduciary restriction representation qualified by the ple... | Trust deed, constitutional documents or partnership agreement reviewed as a condition precedent | — |
| fallback | Representations given on the date of the facility only, with a separate undertaking to notify the lender of any change in capacity or authority. | Legal opinion or equivalent review obtained on the pledgor's capacity; Notification undertaking is an event of default if breached | Senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | Capacity and authority representations qualified by materiality, or given by the borrower only where a third party grants the security. | — | — |

**Escalation triggers**

- Any trustee request for limited recourse against the trust fund only
- Any request to drop the pledgor's own capacity representation

**Conditions precedent added by rules**

- [R01_trust_borrower] Trust deed reviewed for an express power to borrow and to charge trust assets, and for any restriction on the trustee's power to grant security.

**Representations/undertakings added by rules**

- [R01_trust_borrower] The trustee represents that it has full power under the trust instrument to borrow and to charge the trust fund, and that it is not in breach of any fiduciary duty in doing so.
- [R07_pdmr_pledged_issuer] The pledgor represents that it is not in possession of inside information in relation to the pledged issuer and will notify the lender on becoming subject to a closed period.

**Drafting notes**

- [R01_trust_borrower] Expect a trustee request for limited recourse to the trust fund; price that against the capacity representation rather than conceding both.

**Jurisdiction note (england_wales)**

For a trustee pledgor, English law practice is to review the trust instrument for an express power to borrow and to charge trust assets, and to take the representation from the trustee in its personal as well as its representative capacity where the trustee will not accept unlimited recourse.

Rules applied: R01_trust_borrower, R07_pdmr_pledged_issuer

### Governing law and jurisdiction [DRAFT]

- Clause id: governing_law_jurisdiction
- Risk rating: medium
- Category: boilerplate
- Document: all

**Opening: preferred**

> The finance documents are governed by English law and the English courts have exclusive jurisdiction, save that the lender may bring proceedings in any court of competent jurisdiction.

Rationale: A one-way jurisdiction clause lets the lender sue where the assets are while denying the borrower a choice of forum. On a secured facility the asset location is the point.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The finance documents are governed by English law and the English courts have exclusive jurisdiction, save that the lender may bring proceedings in any court of... | — | — |
| acceptable | The finance documents are governed by English law and the English courts have exclusive jurisdiction, save that the lender may bring enforcement proceedings in... | Security document governed by the law of the place of the collateral where local advice so requires | — |
| fallback | English law and exclusive English jurisdiction for both parties, with the security document governed by the law of the jurisdiction in which the pledged account... | Local counsel confirms enforceability and perfection under the security document's governing law | Senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | Governing law or jurisdiction in a forum where the lender has not obtained advice on the enforceability and perfection of the security. | — | — |

**Escalation triggers**

- Any governing law outside the three covered by this playbook

**Jurisdiction note (england_wales)**

Where English law governs the facility but the pledged account is held elsewhere, the law applicable to the proprietary aspects of the security is determined by the location of the account rather than by the parties' choice, so local advice remains necessary.

Rules applied: none

### No advice and non-reliance [DRAFT]

- Clause id: no_advice_non_reliance
- Risk rating: medium
- Category: parties_reps
- Document: facility_letter

**Opening: preferred**

> The borrower acknowledges that the lender gives no investment, tax, legal or accounting advice in connection with the facility, that no communication is a recommendation, and that the borrower relies on its own judgement and its own advisers in deciding to borrow against its portfolio and in selecting and retaining the pledged assets.

Rationale: A Lombard facility sits next to an advisory relationship, and the line between financing a portfolio and recommending one is the line the lender must be able to point to later.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The borrower acknowledges that the lender gives no investment, tax, legal or accounting advice in connection with the facility, that no communication is a recom... | — | — |
| acceptable | Acknowledgement as above, expressed to be without prejudice to any separate written advisory agreement between the parties and to any duty the lender owes under... | Carve-out is limited to a separate written agreement, not to the relationship generally | — |
| fallback | Acknowledgement as above, with the borrower confirming that it has had the opportunity to take independent advice, in place of a confirmation that it has taken... | Suitability or appropriateness assessment completed and recorded separately where required | Senior lawyer, with compliance sign-off |
| unacceptable (description of the walk-away line, not drafting) | Any drafting under which the lender accepts that a communication about the facility, the collateral or the pledged assets was a personal recommendation. | — | — |

**Escalation triggers**

- Any request for the lender to confirm the facility is suitable for the borrower

**Jurisdiction note (england_wales)**

A non-reliance acknowledgement may be subject to the reasonableness controls applying to contract terms, and it cannot displace a regulatory duty. [VERIFY] Interaction between the acknowledgement and the applicable conduct regime not confirmed against a primary source.

Rules applied: none

### Interest rate, benchmark and benchmark fallbacks [STUB]

- Clause id: interest_benchmark_fallbacks
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Prepayment and breakage costs [STUB]

- Clause id: prepayment_breakage
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Collateral substitution and release [STUB]

- Clause id: collateral_substitution
- Category: collateral

No drafted positions yet; status stub.

Rules applied: none

### Cross-collateralisation and set-off [STUB]

- Clause id: cross_collateral_set_off
- Category: collateral

No drafted positions yet; status stub.

Rules applied: none

### Representations: source of funds, sanctions and tax [STUB]

- Clause id: reps_source_of_funds_sanctions_tax
- Category: parties_reps

No drafted positions yet; status stub.

Rules applied: none

### Purpose restrictions and permitted use of proceeds [STUB]

- Clause id: purpose_restrictions
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Transfer and assignment [STUB]

- Clause id: transfer_assignment
- Category: boilerplate

No drafted positions yet; status stub.

Rules applied: none

### Confidentiality and bank secrecy [STUB]

- Clause id: confidentiality_bank_secrecy
- Category: boilerplate

No drafted positions yet; status stub.

Rules applied: none

### Tax gross-up and indemnity [STUB]

- Clause id: tax_gross_up
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Third-party security: waivers and independent advice [STUB]

- Clause id: third_party_security_waivers
- Category: parties_reps

No drafted positions yet; status stub.

**Drafting notes**

- [R01] Trustee pledgor: confirm whether an independent advice letter is expected even though the trustee is not a natural person.
- No drafted positions exist for this clause yet, so the note above is the whole of the playbook's output on it.

Rules applied: R01_trust_borrower

### Information undertakings [STUB]

- Clause id: information_undertakings
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Currency mismatch and FX haircuts [STUB]

- Clause id: currency_mismatch_fx
- Category: collateral

No drafted positions yet; status stub.

Rules applied: none

## Jurisdiction overlay — England and Wales [STUB]

- Creation: Security over intermediated securities is created by a pledge or a charge granted in a written security agreement; no statutory form is prescribed. [VERIFY]
- Registration / filing: A charge granted by a company is registrable at the companies registry unless a disapplication applies. [VERIFY] Not confirmed against the primary text.
- Perfection depends on: Possession or control of the pledged account in practice, evidenced by the custodian arrangements.
- Enforcement route: Sale, or appropriation where the agreement expressly permits it and the financial collateral regime applies. [VERIFY]
- Financial collateral regime: A financial collateral regime exists; whether it extends to a natural-person collateral provider has not been confirmed. [VERIFY]
- Governing law of intermediated securities: The proprietary aspects are generally determined by the location of the relevant account rather than by the parties' choice of law. [VERIFY]
- Practical notes: Local counsel should confirm perfection and enforcement before first utilisation. Nothing in this overlay has been reviewed by a named human.

## Counterparty request outcomes

| Clause | Requested tier | Requested text | Floor | Outcome |
| --- | --- | --- | --- | --- |
| margin_maintenance_cure | acceptable | — | acceptable | accepted_within_floor |
| lender_discretion_valuation | fallback | Lending values to change only on X business days' written notice. | acceptable | below_floor_escalated |
| enforcement_liquidation | unacceptable | No sale of pledged securities without the borrower's prior written consent. | acceptable | unacceptable_escalated |

## Not automated on this deal

- Clearing the pledgor's PDMR or insider position with compliance, and deciding whether a closed period blocks the pledge or an enforcement sale.
- Any concession below a clause's floor, and any counterparty request at the unacceptable tier.
- Whether to grant forbearance on a live margin call, waive an event of default, or begin enforcement.
- Any cross-border perfection or enforceability conclusion: the tool cites, local counsel confirms.

---

This markup was produced by the SBL Negotiation Playbook Demonstrator, a demonstration tool built from public sources and run against synthetic deals. It is not legal advice. It is not the work product of any institution, and it has not been validated against any institution's credit policy, risk appetite, house style or local counsel advice. Every position is drafted from the lender's side only. The status labels mean exactly what they say: [STUB] means no position has been drafted; [DRAFT] means an entry written from public sources that no named human reviewer has checked; [REVIEWED] means a named reviewer recorded in the library has checked it. Text carrying a [VERIFY] prefix has not been confirmed against a primary source the writer opened. Any concession below a clause's floor, and every item under "Not automated on this deal", is a human decision that this tool does not make.
