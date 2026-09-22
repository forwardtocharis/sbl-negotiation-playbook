# SBL negotiation markup — D04

- Deal: D04
- Description: Synthetic. Borrower D, a Luxembourg-resident individual, with no high-net-worth or business-purpose declaration on file, borrowing against daily-dealing fund interests pledged by their spouse and held at a third-party custodian in Luxembourg under Luxembourg law security. Fictional parties; not a real deal.
- Run id: 000000000000
- Timestamp: 1970-01-01T00:00:00+00:00
- Library hash: 7d8caf2f1de399852e2edfb99fdaf1e4d23aaa90da1ce56e9804611cb31d2a72
- Intake hash: b5922cd936c3539f10077c2086b852fc57d6c43e07bdb456eb69f57bdc05ef05
- Governing law: luxembourg
- Review status: 0 reviewed / 12 draft / 12 stub

Status warning: positions tagged [DRAFT] or [STUB] have not been reviewed by a named human reviewer and must not be relied on as the lender's settled position.

## Escalations

| Rule id | Clause | Who decides | Reason |
| --- | --- | --- | --- |
| R03a_natural_person_borrower_no_declaration | — | senior lawyer + compliance | Individual borrower with no high-net-worth or business-purpose declaration on file. Whether this facility is consumer credit is not a determination this tool makes. |

Exit code: 2

## Flags

### High severity

- **consumer_credit** — The borrower is an individual and no high-net-worth or business-purpose declaration is recorded, so no exemption is made out on the facts the tool holds. In the United Kingdom the exemption logic has sat in the Regulated Activities Order since 1 April 2014 rather than in the Consumer Credit Act 1974: the business-purpose route (art. 60C) needs credit exceeding GBP 25,000 and a wholly or predominantly business purpose, and the high-net-worth route (art. 60H) needs credit exceeding GBP 60,260 or security on land, a prescribed borrower declaration giving up the protections of a regulated agreement, and a compliant statement of net income of at least GBP 150,000 or net assets of at least GBP 500,000 given to the lender before the agreement is made. A Swiss-booked facility usually falls outside the Consumer Credit Act twice over, because Art. 7(1)(b) excludes credit covered by deposited customary bank collateral or by sufficient assets held with the lender and Art. 7(1)(e) excludes credit above CHF 80,000; a Luxembourg-booked facility is outside the consumer credit chapter above EUR 75,000 and again where the credit lets an investor transact in financial instruments. [VERIFY] whether any of those figures has been amended since 21 September 2026, and whether the 1974 Act's unfair-relationship powers continue to reach an exempt agreement. Whether this borrower is a consumer is not a determination this tool makes.
  - Who decides: senior lawyer + compliance
  - Triggering rule: R03a_natural_person_borrower_no_declaration

## Clause-by-clause

### Facility type: uncommitted and repayable on demand versus committed term [DRAFT]

- Clause id: facility_type
- Risk rating: high
- Category: credit
- Document: facility_letter

**Opening: preferred**

> The facility is uncommitted. The Bank is not obliged to make any advance, and each utilisation is a separate decision of the Bank whether or not the conditions precedent are satisfied and whether or not the Limit is undrawn. The facility has no fixed term. The Bank may at any time, in its discretion and without giving a reason, reduce, suspend or cancel the Limit and may demand immediate repayment of all principal, interest, fees and other amounts outstanding, whether or not any Event of Default has occurred and whether or not the Borrower is in compliance with the margin requirement. A demand is effective when made, and the Bank is not required to give any notice beyond the demand itself. No failure or delay by the Bank in demanding repayment or in cancelling the Limit operates as a waiver of the right to do so, and no course of dealing converts the facility into a committed one.

Rationale: The demand right is what the Bank has instead of covenants, and it is the reason this product can be priced and sized the way it is. If the Bank has to prove an event of default before it can stop, it is arguing about materiality while the collateral is moving, and the argument costs more than the margin it was protecting. Every published private-bank document opened for this playbook takes this position, so it is the market opening rather than an aggressive one. What the Borrower buys with it is price, size and speed of execution, which is the whole appeal of borrowing against a portfolio instead of against a covenant package.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The facility is uncommitted. | — | — |
| acceptable | The facility is uncommitted and all amounts outstanding are repayable on demand. | — | — |
| fallback | The Bank commits to make advances up to the Limit until the date falling X months after the date of the facility letter, subject to the conditions precedent bei... | Collateral is exchange-listed or daily-dealt and within the concentration limit at signing and on each funding date.; The Bank or a member of its group is the Custodian, or an executed account control agreement is in place.; Credit has priced the commitment, including breakage and the cost of the undrawn line.; Where the Borrower is an individual, any declaration and statement on which the facility's regulatory treatment depends is in place before signing.; The mandatory prepayment list has been read against the events of default clause so that nothing is lost in the gap between them.; The lending values applied have been reduced to reflect that the Bank cannot exit the commitment at will. | credit committee |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not agree a committed facility with no collateral-linked mandatory prepayment right; will not commit to advance on a funding date irrespective of... | — | — |

**Escalation triggers**

- Any request to convert the facility from uncommitted demand to committed term.
- Any request for a notice period longer than X days before the Bank may cancel or reduce the Limit.
- Any request that a notice period apply where an Event of Default, an uncured margin shortfall, an illegality or a regulatory requirement has occurred.
- Any request that the demand right be exercisable only on an Event of Default, or be subject to a cure period.
- Any request for automatic renewal, rollover or an evergreen commitment.
- Any request that the Bank commit to advance without re-testing the lending value on the funding date.

**Jurisdiction note (luxembourg)**

The published Luxembourg template is the closest thing in the source pool to the acceptable tier written out: an authorisation to run a debit balance up to a Limit, granted at the bank's sole discretion for an indefinite period, with either party able to terminate on 90 days' notice and the bank able to terminate with immediate effect on any listed event of default (BANK-LU-01). The same document also records a 14 calendar day withdrawal right for a retail client on a distance contract where the facility is unused, which is a consumer-protection feature of the booking centre rather than a negotiated term and should be checked with the booking centre before the facility letter is issued.

Rules applied: none

### Conditions precedent to first and each utilisation [DRAFT]

- Clause id: conditions_precedent
- Risk rating: high
- Category: credit
- Document: facility_letter

**Opening: preferred**

> The Bank is not obliged to make the first advance until it has received, in form and substance satisfactory to it, each of the following: (a) identification, know-your-client, sanctions screening and source-of-funds and source-of-wealth evidence for the Borrower, each Pledgor and each beneficial owner, controller, settlor, protector and authorised signatory of either; (b) the constitutional, trust or partnership documents establishing that the Borrower and each Pledgor exists, and the resolutions, consents and authorities establishing that it has power to enter into the finance documents and to grant the security and that the signatories are authorised; (c) the facility letter, the security agreement and, where the Custodian is not the Bank or a member of its group, the account control agreement, each executed; (d) evidence that every step required to make the security effective and to give the Bank possession or control under the law governing the security has been completed, including the opening of the pledged accounts and the booking, earmarking or notification required by that law; (e) a confirmation from the Custodian of the holdings in the pledged accounts and of the waiver or subordination of the Custodian's own liens, rights of retention and rights of set-off over those accounts; (f) a legal opinion satisfactory to the Bank where any obligor, pledgor or asset is outside the jurisdiction whose law governs the security; (g) evidence satisfactory to the Bank that the pledged assets are eligible collateral, are free of transfer restrictions other than those disclosed, and settle through the ordinary book-entry system; (h) each compliance, tax and regulatory sign-off that the Bank requires in connection with the facility, the Borrower, any Pledgor or the pledged assets; and (i) such other documents, evidence, authorisations and assurances as the Bank may require. Each condition in this clause must also be satisfied on the date of, and immediately after, each further utilisation, and by accepting the proceeds of any advance the Borrower is deemed to repeat, on that date, the representations to which those conditions relate. Nothing in this clause obliges the Bank to make any advance, whether or not every condition has been satisfied.

Rationale: Conditions precedent are the only point in the life of a facility where the Bank has complete leverage, because nothing has left the building yet, and everything on this list is materially harder to obtain the day after drawdown than the day before. The list is also where the whole library plugs in: capacity, insider status, perfection and the regulatory perimeter are all cleared here rather than being blocked at the term sheet, which is why the playbook rules add to this clause rather than stopping the deal. Re-testing on each utilisation is not belt-and-braces on an uncommitted facility; it is what stops a clean day-one file being used to draw into a portfolio that has since changed. Saying yes to the list costs the Borrower a week of administration; saying no to it costs the Bank its security.

**Floor: fallback** — approver: senior lawyer

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The Bank is not obliged to make the first advance until it has received, in form and substance satisfactory to it, each of the following: (a) identification, kn... | — | — |
| acceptable | The Bank is not obliged to make the first advance until it has received each of the documents and items listed in the conditions precedent schedule, in form and... | The sweeper survives in qualified form; it is not deleted.; Reasonableness attaches to the Bank's satisfaction, not to the question whether an item is required at all. | — |
| fallback | The conditions precedent are those set out in the conditions precedent schedule, together with any condition the Bank notifies to the Borrower before the facili... | Part 2 contains no item that affects the existence, validity, priority or enforceability of the security.; Part 2 contains no item required by law or regulation to exist before the facility letter is entered into.; Part 2 contains no compliance, sanctions or source-of-funds item.; The Bank or a member of its group is the Custodian, or the account control agreement is already executed.; The Borrower is not an individual to whom a consumer or regulated-credit regime may apply, or the position has been cleared by compliance. | senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not accept know-your-client, sanctions, source-of-funds, capacity or authority evidence, security perfection steps (including an account control a... | — | — |

**Escalation triggers**

- Any request to satisfy know-your-client, sanctions or source-of-funds conditions after first drawdown.
- Any request that perfection, or an account control agreement where the Custodian is a third party, be an undertaking rather than a condition to advance.
- Any request to delete the "such other documents" sweeper entirely rather than qualify it.
- Any request that conditions be deemed satisfied by lapse of time or by the Bank not responding within a period.
- Any request to defer a declaration, statement or consent that must precede the facility letter under any applicable law or regulation.
- Any request that the Bank's satisfaction be judged objectively or be determined by a third party or an expert.
- Any request to waive a condition precedent added to this clause by a playbook rule.

**Conditions precedent added by rules**

- [R12_third_party_custodian] Account control agreement executed by the third-party custodian, acknowledging the lender's security, agreeing to act on the lender's instructions without further consent from the account holder, and subordinating or waiving the custodian's own liens and rights of set-off over the account.

**Drafting notes**

- [R03a_natural_person_borrower_no_declaration] Obtain and file any high-net-worth or business-purpose declaration before drawdown if the facility is to be documented on that basis. The high-net-worth route requires the statement of net income or assets to be given to the lender before the agreement is made, so the sequence is part of the exemption and a declaration signed after the event cannot be regularised later.
- [R05_third_party_security] Record how independent advice was given and by whom. The point of the certificate is to answer an undue-influence argument years later, so it has to name the adviser and the date.

**Jurisdiction note (luxembourg)**

The conditions precedent should name which of the statutory possession routes the deal is using, because they are alternatives and the security agreement has to match the one chosen. For book-entry financial instruments the routes are: concluding the pledge agreement where the pledgee is itself the custodian; a three-party agreement with the custodian, or a two-party agreement notified to it, under which the custodian will act on the pledgee's instructions without any further agreement of the provider; booking the instruments to an account of the pledgee; or earmarking them in the custodian's books (LAW-LU-01, art. 5(2)(a)). Where the deal uses any route other than the first, the custodian is treated as having waived its own pledge ranking unless otherwise agreed or notified, so the CP should capture that in writing. A right of substitution, a right to withdraw excess collateral, a right to collect proceeds and a reserved right of the provider to give instructions do not prejudice the collateral having been provided (LAW-LU-01, art. 2(3)), which is a materially easier position than the English one and means the CP list does not have to strip the client's ordinary account rights. [VERIFY] The WP7 research file additionally records that instruments evidencing a financial collateral arrangement are not subject to registration formalities under art. 26 of the same law; that article was not among those read by the sourcing agent or by this drafting agent.

Rules applied: R03a_natural_person_borrower_no_declaration, R12_third_party_custodian, R05_third_party_security

### Eligible collateral and lending values by asset class [DRAFT]

- Clause id: eligible_collateral_lending_values
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> Eligible collateral is limited to the asset classes listed in the Eligible Collateral Schedule to this facility letter. The lending value of a pledged asset is the market value of that asset as determined by the Bank multiplied by the lending value percentage the Bank applies to the relevant asset class from time to time, and the Bank may apply a different percentage to an individual holding. An asset that is not listed in the Eligible Collateral Schedule has a lending value of nil, and each of the following has a lending value of nil whether or not its asset class is listed: any security subject to a transfer restriction, lock-up, escrow arrangement or issuer consent requirement; any unlisted security or other asset for which the Bank does not have a pricing source it considers reliable; any interest in a fund whose redemptions are suspended, gated, deferred or side-pocketed; and any security suspended from trading or subject to a market-wide or issuer-specific trading restriction. Where a pledged asset is denominated in a currency other than the currency of the facility, its lending value is reduced by a further X percentage points to reflect currency risk. The Bank may amend the Eligible Collateral Schedule and any lending value percentage in accordance with the lender discretion clause of this facility letter.

Rationale: This is the clause that decides how much money leaves the building against a given portfolio, so the Bank keeps both halves of the calculation: what counts as collateral, and at what rate. Every published bank document opened for this playbook states the lending value as a bank-set percentage of a bank-determined value and reserves the right to change it. The exclusions are not decoration: an asset the Bank cannot price, or cannot sell on the day it needs to sell, has no lending value whatever its screen price, and the Swiss regulator's stated concern about Lombard books is that haircuts are set too low, not too high. The currency haircut is there because an exchange-rate move can exhaust the cover without the securities moving at all.

**Floor: fallback** — approver: head of credit

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Eligible collateral is limited to the asset classes listed in the Eligible Collateral Schedule to this facility letter. | — | — |
| acceptable | Eligible collateral is limited to the asset classes listed in the Eligible Collateral Schedule. | — | — |
| fallback | The lending value percentages applying to the holdings identified in Part 1 of the Eligible Collateral Schedule are fixed for X months from the date of this fac... | Collateral is limited to exchange-listed securities, daily-dealt funds and cash.; No holding in Part 1 of the Schedule is a restricted, locked-up or control security.; Single-name exposure is within the concentration limit set for the facility.; The Bank or a member of its group is the Custodian, or an executed account control agreement is in place.; Credit has priced both the fixed percentages and the length of the fixing period. | head of credit |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not agree a lending-value grid fixed for the life of the facility or amendable only with the Borrower's consent; will not give a positive lending... | — | — |

**Escalation triggers**

- Any request to fix lending value percentages for longer than X months, or for the life of the facility.
- Any request to admit unlisted, gated, suspended, restricted or locked-up assets to the Eligible Collateral Schedule at a positive lending value.
- Any request for a valuation supplied or appointed by the Borrower to bind the Bank.
- Any bespoke lending value percentage above the Bank's standard percentage for that asset class.
- Any request to remove the currency haircut where the facility currency and a collateral currency differ.

**Jurisdiction note (luxembourg)**

Draw the eligibility schedule against the statutory exit routes: listed instruments can be appropriated at market price, and fund units at the last published net asset value provided it is less than a year old, or at the fund's redemption price (LAW-LU-01, art. 11(1)(e)-(f)). Collateral that cannot be priced by one of those routes has no fast exit under Luxembourg law, which is a direct argument for giving it a nil lending value rather than a low one.

Rules applied: none

### Concentration limits by issuer, asset class and currency [DRAFT]

- Clause id: concentration_limits
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> Collateral is eligible only to the extent it is diversified in accordance with this clause. So much of the lending value attributable to securities of any one issuer as exceeds X per cent. of the total lending value of the collateral is disregarded, and so much as is attributable to issuers within the same group, the same industry sector or the same currency as exceeds X per cent. of the total lending value is likewise disregarded. The Bank determines whether issuers form a group, sector or correlated set. Neither the Borrower nor any of its affiliates or connected persons will grant security over, or agree to pledge, securities of the same class as any pledged security to any other financier without the Bank's consent. If the Bank considers that the collateral is not sufficiently diversified it may, at its option and without prejudice to its other rights, reduce the lending value of the affected securities, require the Borrower to post further eligible collateral or repay, charge a differentiated fee, or treat the position as an event entitling the Bank to realise the collateral in accordance with this facility letter.

Rationale: Concentration is the risk this product actually fails on: the Bank can be perfectly secured on paper and still not get out, because selling a large stake in one name moves the price against it. That is why the clause bites on lending value rather than market value, and why correlated names are grouped rather than counted separately. The Swiss regulator names single-stock lending and undiversified collateral as a supervisory focus, so the Bank is not inventing a concern here. The same-class negative pledge matters as much as the cap: several margin loans stacked on one stock create an overhang that turns three lenders' exits into one queue.

**Floor: fallback** — approver: credit committee

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Collateral is eligible only to the extent it is diversified in accordance with this clause. | — | — |
| acceptable | The single-name limit is X per cent. | — | — |
| fallback | The single-name limit is X per cent. | The grandfathered holding is exchange-listed, liquid and not restricted, locked-up or control stock.; The excess is carried at a reduced lending value percentage priced by credit.; The Borrower undertakes not to increase the grandfathered holding.; Neither the Borrower nor the Pledgor is a PDMR or insider of the concentrated issuer.; The margin maintenance cure period for this facility is at or tighter than its default floor. | credit committee |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not lend against a concentrated portfolio with no concentration discipline at all, meaning no single-name limit, no reduction in lending value for... | — | — |

**Escalation triggers**

- Any single-name exposure above X per cent. of total lending value at drawdown.
- Any request to grandfather an existing holding above the single-name limit.
- Any request to remove or narrow the same-class negative pledge beyond entities the Borrower controls.
- Any request to fix the single-name limit for the life of the facility or to require the Borrower's consent to change it.
- Any request to test concentration against market value rather than lending value.

**Jurisdiction note (luxembourg)**

A published Luxembourg bank template treats insufficient diversification as an input to the limit, as a ground for differentiated fees, and as a stand-alone ground for unilateral realisation without prior notice (BANK-LU-01), which is consistent with enforcement without prior notice being the statutory default under the financial collateral law unless the parties provide otherwise (LAW-LU-01, art. 11). The practical point for drafting is that the stand-alone diversification trigger is worth more in Luxembourg than elsewhere, so give it up knowingly rather than as a tidy-up.

Rules applied: none

### Lender discretion over valuation, lending values and eligibility [DRAFT]

- Clause id: lender_discretion_valuation
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> The Bank may at any time, in its discretion and with immediate effect, determine and re-determine the market value of any pledged asset, change the lending value percentage applying to any asset class or to any individual holding, add an asset class to or remove one from the Eligible Collateral Schedule, and determine that a pledged asset has ceased to be eligible. The Bank values the collateral at least daily using pricing sources it selects. A change takes effect when the Bank makes it, whether or not the Bank has notified the Borrower and whether or not a margin call is then outstanding; the Bank will inform the Borrower of the change by any means it considers appropriate. No change requires the consent of the Borrower or of the Pledgor.

Rationale: The ability to reprice risk the same day is the core protection behind an uncommitted facility, and it is what the Bank has instead of covenants. If the Bank has to wait, it is holding a fixed-rate view of a moving portfolio, and the loss it takes in the waiting period is exactly the loss the haircut was set to avoid. Every published bank document opened for this playbook takes this position, so it is the market opening rather than an aggressive one. It is also honest about what the facility is: the Borrower is buying liquidity against a portfolio, not buying a fixed advance rate for a term.

**Floor: fallback** — approver: head of credit

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The Bank may at any time, in its discretion and with immediate effect, determine and re-determine the market value of any pledged asset, change the lending valu... | — | — |
| acceptable | The Bank may at any time determine and re-determine the market value of any pledged asset, change the lending value percentage applying to any asset class or ho... | — | — |
| fallback | Where the Bank changes the lending value percentage applying to an asset class or removes an asset class from the Eligible Collateral Schedule, the change takes... | Collateral is diversified within the concentration limit and is exchange-listed or daily-dealt.; The facility is the Bank's only exposure to the Borrower, or other exposures have been considered by credit.; The Bank or a member of its group is the Custodian, or an executed account control agreement is in place.; The margin maintenance cure period is at or tighter than its default floor for this deal.; Credit has confirmed the notice period is priced into the lending values applied. | head of credit |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not make a change to lending values, haircuts or eligibility conditional on the Borrower's or the Pledgor's consent; will not accept a notice peri... | — | — |

**Escalation triggers**

- Any request for a notice period longer than X business days before a change in lending values takes effect.
- Any request to remove or narrow one of the four immediate-effect carve-outs, and in particular the rapid-decline or open-margin-call carve-out.
- Any request that the Bank may not change lending values while a margin call is outstanding.
- Any request for a binding third-party valuation, or for a dispute mechanism that suspends a change pending determination.
- Any request to limit revaluation to fixed intervals or to defined external market events.
- Any request that a change requires the Borrower's or the Pledgor's consent.

**Jurisdiction note (luxembourg)**

The Bank's valuation discretion is bounded at the exit by the statutory pricing routes: on appropriation, listed instruments are taken at market price and fund units at the last published net asset value provided it is less than a year old, or at the fund's redemption price (LAW-LU-01, art. 11(1)(e)-(f)). [VERIFY] Luxembourg practice is also said to be to specify the agreed valuation method in the security agreement, because appropriation under art. 11(1)(a) is priced by that agreed method; that point comes from the WP7 research file (docs/research/jurisdictions_research.md) and was not confirmed against the primary text by this agent. Note separately that a published Luxembourg template is the high-water mark of lender discretion in the whole source pool (BANK-LU-01), so a Luxembourg counterparty is unlikely to be able to say the preferred position is off-market.

Rules applied: none

### Margin maintenance, margin call mechanics and cure period [DRAFT]

- Clause id: margin_maintenance_cure
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> A Collateral Shortfall arises whenever the Lending Value of the pledged assets is less than X per cent of the aggregate of all amounts outstanding and all contingent and unmatured liabilities of the Borrower to the Bank (the Trigger Level), as determined by the Bank at any time. On a Collateral Shortfall the Borrower must immediately, on demand and without any prior notice being required, either repay, or pledge further Eligible Collateral acceptable to the Bank, or a combination of the two, in an amount sufficient to restore the Lending Value to Y per cent of those amounts (the Restoration Level), calculated on the values determined by the Bank on the day the demand is made. The Bank may notify the Borrower of a Collateral Shortfall and may allow a period within which it is to be met, but is obliged to do neither; any period the Bank allows is revocable by the Bank at any time, does not arise again on a subsequent Collateral Shortfall, and is not a condition precedent to, and does not suspend, any right of the Bank under the enforcement clause. A second Collateral Shortfall arising while an earlier one is uncured does not extend any period then running.

Rationale: The Bank is lending against a price it does not control, so the only protection it has is the speed with which it can turn a fall in that price back into cash. The two-level structure is what makes that work: a call that only restores the position to the Trigger Level puts the Borrower straight back on the edge of the next call, so the Bank would be having the same conversation every morning in a falling market. Every published private-bank document opened for this playbook takes the no-fixed-period position, so this is the market opening rather than an aggressive one. Keeping the call itself discretionary matters just as much: the Bank must never be in the position where a failure to send a notice is the reason it cannot enforce.

**Floor: fallback** — approver: head of credit

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | A Collateral Shortfall arises whenever the Lending Value of the pledged assets is less than X per cent of the aggregate of all amounts outstanding and all conti... | — | — |
| acceptable | On a Collateral Shortfall the Bank will notify the Borrower, and the Borrower must restore the Lending Value to the Restoration Level by 5.00 p.m. | — | — |
| fallback | Where, on or before the expiry of the cure period, the Borrower delivers a written cure plan identifying the source of the funds, the steps required to release... | Collateral is diversified within the concentration limit and is exchange-listed or daily-dealt.; No line of the portfolio is issuer-restricted, locked up or subject to a trading suspension.; The Bank or a member of its group is the Custodian, or an executed account control agreement is in place.; The funding source named in the cure plan is identified, committed and independent of the pledged portfolio.; The facility is not already in default for any other reason, and no earlier extension has been granted on the same shortfall.; Credit has confirmed that the extension is priced into the lending values applied to this portfolio. | head of credit |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not agree that a margin call, a notice or the expiry of a cure period is a condition precedent to enforcement in all cases; will not agree a cure... | — | — |

**Escalation triggers**

- Any request for a cure period longer than X business days, or for more than one extension on the same shortfall.
- Any request that a cure period continue to run below the Hard Floor, during a rapid decline, or after an Event of Default.
- Any request that notice of a margin call be a condition precedent to enforcement.
- Any request to restore only to the Trigger Level, or to measure restoration on a moving price rather than on the price on the notice date.
- Any request to cure by pledging additional securities rather than by cash or repayment.
- Any request to remove the anti-stacking rule.
- Any request that the cure period and the enforcement notice period run cumulatively.

**Jurisdiction note (luxembourg)**

The published Luxembourg documents are the two poles of this clause. One states no cure period at all - notification on a best-endeavours basis only, at the bank's sole discretion, creating no client right, with amounts due immediately and any deferral a discretionary favour (BANK-LU-01). The other is the only bank-terms document opened with two numeric levels, calling for further cover once the lendable exchange value falls below 130 per cent of outstandings and permitting realisation of part or all of the pledge straight away and without any notice below 120 per cent (BANK-LU-02) - which is exactly the Trigger Level and Hard Floor architecture used above, and a useful answer to a counterparty who says the Hard Floor is invented. Keep the cure period in the facility letter and out of the security agreement: enforcement without prior notice is the statutory default under the Law of 5 August 2005 only "unless otherwise provided for", so a cure period drafted into the security document narrows the statutory enforcement power itself (LAW-LU-01, art. 11(1)).

Rules applied: none

### Security structure: pledge, charge or title transfer, plus control and custody [DRAFT]

- Clause id: security_structure_control
- Risk rating: high
- Category: collateral
- Document: security_agreement

**Opening: preferred**

> The Pledgor grants to the Bank a first-ranking and continuing security interest over each Collateral Account, over all financial instruments and cash from time to time credited to it, over all rights attaching to them and over all proceeds, present and future, taking the form the Bank determines to be most effective under the law of the place where the Collateral Account is maintained, and the Pledgor will execute any further document and give any further instruction the Bank requires for that purpose. The Bank or a member of its group is the Custodian. No financial instrument or cash may be withdrawn, transferred, sold, substituted or otherwise dealt with, and no instruction to the Custodian is effective, without the Bank's prior consent, which the Bank may withhold; the Bank may release only such assets as it determines to be in excess of its requirements, taking lending values, currency exposure, tax and any other risk into account. The Pledgor will create no other security interest over, and will permit no filing, registration or notice in respect of, any Collateral Account or any asset credited to it, will defend the collateral against any adverse claim, and will bear the Bank's costs of perfecting, defending and enforcing the security. Voting and other rights attaching to the collateral are exercisable by the Pledgor only until the Bank gives notice, after which they are exercisable by the Bank or its nominee under an irrevocable power of attorney given by the Pledgor. The Bank reserves the right to use, transfer or dispose of the collateral to the extent permitted by the applicable law and any authorisation given by the Pledgor.

Rationale: What makes this product lendable is not the security document, it is that the Bank is holding the assets and can stop them moving. Where the Bank is the Custodian the structure is at its cheapest and its fastest in all three jurisdictions in this playbook: the pledge agreement alone perfects in Luxembourg, an agreement with the custodian alone does it in Switzerland, and in England the possession-or-control question answers itself. Full dominion with releases in the Bank's gift is also the observed private-bank position rather than an aggressive one. The reason to open here and not one tier down is that every concession in this clause is a concession about who can move an asset on the morning of a default, and that is the one question the Bank cannot afford to have argued about on the day.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The Pledgor grants to the Bank a first-ranking and continuing security interest over each Collateral Account, over all financial instruments and cash from time... | — | — |
| acceptable | The security is a pledge or charge and not a transfer of title. | The Custodian is a regulated institution in a jurisdiction where local counsel has confirmed the perfection route.; The executed control agreement, and any acknowledgement required by local law, are conditions precedent to first drawing.; Statements and valuations are delivered by the Custodian direct to the Bank. | — |
| fallback | Where the Pledgor's Custodian will not enter into a tripartite control agreement, the Bank may accept a pledge or charge notified to the Custodian together with... | Local counsel in the place the Collateral Account is maintained has confirmed the structure in writing.; The Custodian is a regulated institution and is not an affiliate of the Borrower or the Pledgor.; The Custodian's acknowledgement is received before first drawing, and its liens are subordinated or waived.; The portfolio is exchange-listed or daily-dealt and is within the concentration limit.; Daily position and valuation reporting is received direct from the Custodian.; No line of the portfolio is issuer-restricted, locked up or subject to a transfer restriction. | senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not take a structure whose perfection, or whose enforcement, depends on an act, consent, instruction or cooperation of the Pledgor, the Borrower o... | — | — |

**Escalation triggers**

- Any request that the Bank rely on a security interest over a Collateral Account in a jurisdiction where the perfection route has not been confirmed by local counsel.
- Any request that the Custodian retain the right to seek the Pledgor's consent before acting on the Bank's instructions.
- Any request that the Custodian keep its own lien, right of retention, right of use or right of set-off ahead of, or equal with, the Bank's security.
- Any request for a transfer of title for security purposes where the Pledgor is, or may be, a retail-classified or natural-person client.
- Any request for substitution or withdrawal rights beyond Y per cent of the Lending Value in a month, or for release on the Pledgor's own calculation of excess.
- Any request to limit the security to named holdings, or to exclude future assets, proceeds or joint accounts.
- Any request that the Bank give up the irrevocable power of attorney or the right to vote after an Event of Default.

**Drafting notes**

- [R12_third_party_custodian] Where the lender does not hold the account, control is whatever the custodian agrees to plus whatever the law governing the securities account requires, and the three playbook jurisdictions answer that differently. English law asks whether the collateral is in the taker's possession or under its control, which turns on real dispossession of the provider. Swiss law on intermediated securities gives three routes to third-party effectiveness, including a control agreement with the custodian and an agreement with the custodian itself. The Luxembourg collateral law lets possession be constituted through an agreed third-party holder, who must then transfer on notice of an enforcement event without the provider's consent. Read the jurisdiction overlay printed with this markup before settling the structure, and confirm with local counsel.

**Jurisdiction note (luxembourg)**

Luxembourg is the most collateral-taker-friendly of the three on structure, and the one with a hard statutory prohibition in it. The Law of 5 August 2005 allows an all-present-and-future pledge without specific designation of the collateral (art. 4), which is what a revolving Lombard portfolio needs, and expressly provides that a right of substitution, a right to withdraw excess collateral, a right to collect proceeds until further notice and a reserved right of the provider to give instructions do not prejudice the collateral having been provided (art. 2(3)) - so the client can keep trading the portfolio without undermining the pledge, which English law does not allow as freely. Possession is defined functionally: where the Bank is the Custodian, concluding the pledge agreement is enough; otherwise a tripartite agreement, or a two-party agreement notified to the Custodian under which it acts on the Bank's instructions without further agreement of the provider, or booking to the Bank's account, or earmarking in the Custodian's books (art. 5(2)(a)), with routes other than the first treated as a waiver of the Custodian's own ranking unless otherwise agreed. There are no registration formalities (art. 26). The prohibition: a credit institution or investment firm providing investment services may not conclude a transfer of title for security purposes with a retail client, on pain of nullity, and must in any event document its consideration of the use of title transfer (art. 13 and art. 13-1). For a retail-classified Luxembourg client the structural choice is therefore pledge, and the point is not negotiable (LAW-LU-01).

Rules applied: R12_third_party_custodian

### Events of default, including insolvency, death or incapacity and material adverse change [DRAFT]

- Clause id: events_of_default
- Risk rating: high
- Category: default_enforcement
- Document: facility_letter

**Opening: preferred**

> Each of the following is an Event of Default. The Borrower fails to pay any amount when due. The Borrower or the Pledgor fails to meet a margin call, to deliver additional collateral by the deadline set under the margin maintenance and cure clause, or to respond to a call. Any representation, warranty or information given by or on behalf of a Relevant Person is incorrect, incomplete or misleading when given or when repeated. A Relevant Person is subject to, or is threatened with, insolvency, bankruptcy, moratorium, composition, business failure, material litigation or the appointment of an insolvency officer, or takes any step towards any of them. A Relevant Person who is an individual dies or loses legal capacity, or a Relevant Person which is not an individual is dissolved, ceases to exist, loses a constitutive status on which the facility was granted, or has its constitutive documents amended, restated, revoked or invalidated. Any attachment, seizure, forfeiture, freezing or restraint order, subpoena, court order or regulatory proceeding affects a Relevant Person or a substantial part of its assets. The Bank considers that the collateral has become inadequate, impaired or insecure, or that the conditions on which the Bank granted the facility have changed. An event of default, termination event or acceleration occurs under any other facility, guarantee, hedging or derivative arrangement between a Relevant Person and the Bank or any member of the Bank's group, or under any financial indebtedness of a Relevant Person owed to any other person. Performance becomes unlawful, or a change in law, regulation or regulatory requirement increases the Bank's cost or reduces its return. The security ceases to be a valid, first-ranking and perfected interest in the collateral. "Relevant Person" means the Borrower, the Pledgor, any guarantor, any other provider of collateral, and any beneficial owner or settlor of any of them. On an Event of Default all amounts owing become immediately due and payable without notice or demand, the Bank's commitment (if any) is cancelled, and the Bank may enforce under the security documents without further notice.

Rationale: This list is the Bank's exit, and on this product the exit has to be available before the loss has crystallised rather than after. That is why the insolvency and deterioration limbs reach threatened events: by the time a private client's insolvency is a matter of record, the collateral has usually already moved. The width of "Relevant Person" is deliberate and is the single most contested definition in the clause; a facility to a trust or a personal holding vehicle is in practice a facility to the individual behind it, and the events that damage the credit are events in that individual's life, not in the vehicle's. Every limb here is observed in a published or filed document from this side of the market, so it is an opening position and not an aggressive one.

**Floor: fallback** — approver: head of credit

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Each of the following is an Event of Default. | — | — |
| acceptable | Each of the following is an Event of Default. | — | — |
| fallback | The word "threatened" is deleted from every limb. | The facility is uncommitted and repayable on demand, so the events of default are not the Bank's only exit.; Collateral is exchange-listed or daily-dealt, diversified within the concentration limit, and priced at least daily.; The Bank or a member of its group is the Custodian, or an executed account control agreement is in place.; There is no third-party pledgor who is an individual, or the death standstill has been excluded for that pledgor.; The Borrower has no other facilities with the Bank or its group that would be prejudiced by the longer cure and standstill periods.; Credit has confirmed the standstill and cure periods are acceptable on this collateral pool. | head of credit |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not accept a grace period, a cure period or a materiality qualifier on the failure to meet a margin call or to deliver additional collateral, beca... | — | — |

**Escalation triggers**

- Any request for a grace period, cure period or materiality qualifier on the margin call limb or on principal.
- Any request to delete the material adverse change limb without an enumerated substitute, or to delete the residual value-and-liquidity limb from that substitute.
- Any request for a payment grace period longer than X business days, or a general covenant cure longer than X days.
- Any request to remove death or loss of capacity of an individual Borrower, Pledgor or guarantor, or for a standstill on death longer than X business days or one that survives an open margin call.
- Any request to narrow "Relevant Person" so that it no longer reaches an individual whose death or incapacity would affect the ability to deal with the collateral.
- Any request to exclude other facilities with the Bank or its group from the cross-default limb.
- Any counterparty request on this clause where the facility is committed rather than repayable on demand.

**Drafting notes**

- [R03a_natural_person_borrower_no_declaration] Where the borrower is an individual, death and incapacity need to be handled expressly rather than left to the insolvency wording. Say what happens to the facility, who the lender may deal with, and whether the portfolio is frozen or may be liquidated in the meantime.

**Jurisdiction note (luxembourg)**

Luxembourg is the most favourable of the three on exactly the point that worries a private bank. The financial collateral law applies whether the arrangement is entered into by a merchant or a non-merchant, so an individual pledgor is inside the regime rather than outside it; the arrangements, the agreed enforcement events and the agreed valuation and enforcement measures are effective against third parties, commissioners, receivers and liquidators notwithstanding domestic or foreign reorganisation or winding-up proceedings; and the same rules are stated to apply on the death or incapacity of the collateral provider or the debtor (LAW-LU-01, arts. 2(1) and 20(4)). The one carve-out is the over-indebtedness procedure for private individuals, which is excepted from the general disapplication of insolvency law, so full insolvency remoteness cannot be assumed against a Luxembourg-resident individual. At the commercial end, a published Luxembourg template treats the death of the client as a free-standing ground for unilateral realisation without prior notice and carries a deterioration limb reaching loss of market confidence (BANK-LU-01), so a Luxembourg counterparty is not well placed to argue that the preferred position on death is off-market.

Rules applied: R03a_natural_person_borrower_no_declaration

### Enforcement and liquidation: notice, standard of conduct and self-help sale [DRAFT]

- Clause id: enforcement_liquidation
- Risk rating: high
- Category: default_enforcement
- Document: security_agreement

**Opening: preferred**

> On an Event of Default the Bank may, without demand, advertisement or notice of intention, all of which the Pledgor waives to the fullest extent permitted by law, take control of the Collateral Account and of all proceeds, transfer the collateral into its own name or that of a nominee, sell or otherwise dispose of all or any part of the collateral publicly or privately, at such time, place, price, in such order and on such terms as the Bank determines, and apply the proceeds against the secured obligations in such order as the Bank determines. Where notice is required by law and may not be waived, the Bank will give such notice as the law requires; no notice is required where the collateral is of a type customarily sold on a recognised market or where the Bank determines that it threatens to decline speedily in value. The Bank may instead appropriate all or any part of the collateral where the applicable law permits, at a value determined in accordance with this agreement. The Pledgor acknowledges that the Bank is not obliged to sell in tranches or over any period, to seek any strategic buyer or any control premium, to delay a sale in order to obtain a better price, or to sell at all after giving any notice, and that a sale may be at a material discount. The Pledgor remains liable for any shortfall after application of the proceeds, together with the Bank's costs of enforcement.

Rationale: The value of this clause is measured in hours. A portfolio that can be sold on the day of default is worth its market price; a portfolio that can be sold in a week is worth whatever the market does in that week, and the Bank did not price that risk. The pre-agreed acknowledgements are the most useful drafting in the whole pool and they are worth explaining rather than just inserting: the dispute after an enforcement is almost never about whether the Bank could sell, it is about whether it should have sold differently, and these acknowledgements answer that question in advance in the Pledgor's own words. The recognised-market carve-out is not a trick either - for a listed portfolio it is simply accurate, which is why every private-bank document opened for this playbook concedes a notice period and then removes it in the same breath for the collateral this product is secured on.

**Floor: fallback** — approver: credit committee

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | On an Event of Default the Bank may, without demand, advertisement or notice of intention, all of which the Pledgor waives to the fullest extent permitted by la... | — | — |
| acceptable | On an Event of Default the Bank may sell or otherwise dispose of all or any part of the collateral publicly or privately, or appropriate it where the applicable... | — | — |
| fallback | On an Event of Default the Bank will give the Pledgor not less than X business days' notice of the time and place of any public sale of the collateral, or of th... | The portfolio is exchange-listed or daily-dealt, and no line is issuer-restricted, locked up or subject to a transfer restriction.; No pledgor, borrower or connected person is an insider or a person discharging managerial responsibilities of a pledged issuer.; Collateral is within the concentration limit and the currency of the collateral matches the facility, or an FX haircut has been applied.; The Bank or a member of its group is the Custodian, or an executed account control agreement is in place.; The margin maintenance cure period is at or tighter than its default floor for this deal.; Credit has confirmed the notice period is priced into the lending values applied. | credit committee |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not accept a notice period that applies where the collateral is of a type customarily sold on a recognised market, where value or liquidity is fal... | — | — |

**Escalation triggers**

- Any request for a notice period longer than X business days before a sale or an appropriation.
- Any request to remove or narrow the recognised-market, rapid-decline, unlawful-notice or insolvency-process carve-outs.
- Any request for a standstill after an Event of Default, or for a right to cure once an enforcement notice has been given.
- Any request for an obligation to sell in an orderly or scheduled manner, or to seek a strategic buyer or a control premium.
- Any request for a court order, an independent valuation or the Pledgor's consent as a precondition to appropriation or sale.
- Any request for non-recourse, or for a cap on the Pledgor's liability for a deficiency.
- Any request to delete the pre-agreed acknowledgements of what is commercially reasonable.

**Jurisdiction note (luxembourg)**

Luxembourg is the strongest of the three and the enforcement clause should be drafted to use it rather than to restate it. Article 11(1) of the Law of 5 August 2005 lets the pledgee, unless otherwise provided for and WITHOUT PRIOR NOTICE, appropriate the collateral at a price set by the agreed valuation method, assign it by private sale in a commercially reasonable manner or on a trading venue where it is admitted to trading or by public auction, obtain a judicial attribution against an expert valuation, net, appropriate listed instruments at market price or fund units at the last published net asset value provided it is under a year old, or request redemption of fund units. Article 11(3) obliges an agreed third-party custodian to transfer the instruments on notice of an enforcement event without the provider's consent and without informing it in advance, and article 20 makes the arrangement, the agreed enforcement events and the agreed valuation and enforcement measures effective against insolvency officials notwithstanding reorganisation or winding-up proceedings (LAW-LU-01). Two drafting warnings. Avoid the public auction route unless it is needed: article 11(2) imposes at least eight working days' press notice and minutes within three working days, which is the slowest option on the menu. And because article 11(1) applies only "unless otherwise provided for", a negotiated notice period written into the security agreement narrows the statutory power itself - if a client insists on notice, put it in the facility letter as an undertaking rather than as a condition of the enforcement right. Published Luxembourg bank documents take exactly this position, realising on the exchange or the open market without prior notice (BANK-LU-01, BANK-LU-03) and permitting immediate realisation below the lower cover level (BANK-LU-02).

Rules applied: none

### Capacity, authority and due execution for trusts, corporates and partnerships [DRAFT]

- Clause id: capacity_authority
- Risk rating: high
- Category: parties_reps
- Document: all

**Opening: preferred**

> Each of the Borrower and each Pledgor represents and warrants that it is duly constituted and validly existing; that it has the power and authority to enter into and perform the finance documents and to create the security; that every action, consent and authorisation required by its constitutional or trust documents, by any applicable law or by any agreement binding on it, including any shareholder, beneficiary, partner or protector consent, has been taken or obtained and is in full force; that the finance documents have been executed by persons authorised to do so; that its obligations are legal, valid, binding and enforceable; that entry into and performance of them does not conflict with its constitutional or trust documents, any law or any agreement binding on it; and that it is solvent and will not be rendered insolvent by the transaction. Where a party contracts as trustee, it further represents that it is duly appointed and is the sole trustee or is acting with all of its co-trustees; that the trust instrument and every deed of appointment, retirement or variation empower it to borrow, to charge the trust assets and to delegate as contemplated by the finance documents; that it is not acting in breach of trust and has no notice of any claim that it is; and that its right of indemnity out of the trust fund is not excluded, limited or impaired, and it undertakes not to exclude, limit or impair it, not to retire without a replacement trustee acceding to the finance documents, not to distribute or appoint trust property, and not to incur any liability ranking in priority to the Bank's claim on that indemnity, in each case without the Bank's prior written consent. The trustee contracts in both its personal and its trustee capacity and its liability is not limited to the trust fund. Where a party is a partnership, it represents that the borrowing and the security are within the ordinary course of the partnership business or have been authorised by all of the partners, that the partnership agreement permits them, and that each partner is jointly and, where its constitution permits, severally liable, and it undertakes to notify any change in the partners and to procure that any incoming partner accedes. Where a Pledgor is not the Borrower, its obligations are absolute and unconditional irrespective of the validity or enforceability of the Borrower's obligations, any variation of the facility, any release of other collateral or guarantees, or any other circumstance which would otherwise operate as a defence available to a surety, all of which are waived. Each Pledgor which is a company further represents that granting the security is for its corporate benefit as determined by its board and does not constitute unlawful financial assistance. Each representation is repeated on each utilisation date and on each day on which any amount is outstanding, and each of the Borrower and each Pledgor undertakes to notify the Bank immediately of any change in its beneficial owners, trustees, general partner or controllers, any such change being subject to fresh know-your-client review and to the Bank's approval.

Rationale: This clause is the one that decides whether the Bank has security at all, because a pledge granted by someone who lacked the power to grant it is not a weak pledge, it is no pledge. The cost of getting it right is a week of reading documents the client already has; the cost of getting it wrong surfaces on the day the Bank tries to sell, which is the day the beneficiaries or the minority shareholder appear. Full personal recourse against a trustee is the opening position rather than the answer, but it has to be the opening position, because the moment the Bank concedes limited recourse it is relying entirely on the trustee's indemnity and it needs to have asked about that indemnity first. The notification undertaking is the cheapest thing on the list and the most useful: capacity is not a fact about signing day, it is a fact about every day the loan is outstanding.

**Floor: acceptable**

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Each of the Borrower and each Pledgor represents and warrants that it is duly constituted and validly existing; that it has the power and authority to enter int... | — | — |
| acceptable | The trustee's liability under the finance documents is limited to the assets of the trust from time to time and to the trustee's right of indemnity out of them,... | The trustee is a professional or institutional trustee, or a corporate trustee of substance.; The trust instrument has been read and confirms the power to borrow and to charge.; The indemnity representation and the anti-impairment undertakings are given and are not qualified by knowledge.; Personal liability survives for fraud, wilful default, negligence and breach of the capacity representations. | — |
| fallback | The trustee's liability under the finance documents is limited to the assets of the trust from time to time, and no claim may be made against the trustee person... | An institutional trustee of substance, regulated in its jurisdiction.; A legal opinion from counsel qualified in the law governing the trust, confirming the power to borrow and to charge, due authorisation, and that the trustee's right of indemnity is unimpaired.; The Bank has first-ranking security over the trust assets and is subrogated to the trustee's indemnity and lien.; Consent rights over further borrowing by the trust, over distributions and appointments, and over any change of trustee; notification of any mandatory distribution.; The governing law of the finance documents and the location of the trust assets have been checked against any statutory limited-recourse protection being relied on.; Lending values have been reduced by credit to reflect the loss of personal recourse. | senior lawyer + head of credit |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not accept recourse limited to the trust fund where the trustee's right of indemnity is excluded, limited or impaired, or where the trustee will n... | — | — |

**Escalation triggers**

- Any request for recourse limited to the trust fund where the trustee's indemnity is excluded, limited or cannot be confirmed.
- Any request to remove the fraud or wilful default carve-out from a limited recourse clause.
- Any request to delete the representation that the trustee is not acting in breach of trust, or the anti-impairment undertakings.
- Any request that the Bank accept a certificate in place of the trust instrument, constitutional documents or partnership agreement.
- Any corporate pledgor securing another person's debt where local counsel has not confirmed the corporate benefit, financial assistance and upstream security position.
- Any request to delete the surety-defence waivers, and any third-party individual pledgor declining independent legal advice.
- Any request to remove the undertaking to notify a change of trustee, general partner, controller or beneficial owner.

**Jurisdiction note (luxembourg)**

One authority obstacle is removed by statute at the point it would otherwise bite hardest: shareholder approval is not required to realise a pledge over all the shares of a Luxembourg private limited company granted in a single transaction, and in other cases the approval may be given irrevocably in advance (LAW-LU-01, art. 12). That is worth knowing at signing rather than at enforcement, because it tells the deal team which consents actually have to be collected as conditions precedent. Separately, the published Luxembourg template shows how a booking centre handles authority for a private client largely by representation rather than by document, including a representation that the client acts for its own account and not for third parties with an undertaking to notify immediately on any change of beneficial owner, that change being subject to fresh know-your-client review and formal approval (BANK-LU-01) - which is the model for the notification undertaking in the preferred tier. [VERIFY] Luxembourg corporate benefit and financial assistance restrictions on a corporate pledgor were not researched for this entry.

Rules applied: R05_third_party_security

### Governing law, jurisdiction and service of process [DRAFT]

- Clause id: governing_law_jurisdiction
- Risk rating: high
- Category: boilerplate
- Document: all

**Opening: preferred**

> The facility letter and any non-contractual obligations arising out of it are governed by the law of the jurisdiction in which the Bank books the facility. The security agreement and any non-contractual obligations arising out of it are governed by the law of the jurisdiction in which the collateral account is maintained, and where that account is maintained in a jurisdiction which permits the applicable law to be chosen in the account agreement, the account agreement expressly designates that same law as governing the proprietary questions relating to the collateral. The Borrower and the Pledgor irrevocably submit to the jurisdiction of the courts of the jurisdiction in which the Bank books the facility, waive any objection on the ground of venue or forum non conveniens, and agree that a judgment of those courts is conclusive and enforceable in any other jurisdiction. That submission is for the benefit of the Bank only: nothing in it limits the Bank's right to bring proceedings, or to seek interim, protective or enforcement relief, in the courts of the jurisdiction in which the collateral account is maintained, in which the Borrower or the Pledgor is domiciled or has assets, or in any other court of competent jurisdiction, and the Bank may bring concurrent proceedings in more than one jurisdiction. Each of the Borrower and the Pledgor which is not resident in the jurisdiction of the Bank's booking location irrevocably appoints a process agent in that jurisdiction to receive service on its behalf, will maintain that appointment for so long as any amount is outstanding, and will appoint a replacement within X days if the appointment ceases to be effective; failure to do so entitles the Bank to appoint a replacement at the Borrower's cost. Each of the Borrower and the Pledgor irrevocably waives, to the fullest extent permitted by law, any immunity from suit, from jurisdiction, from any order for specific performance or recovery of property, and from attachment, execution or other enforcement against its assets, and agrees that it enters into the documents in respect of commercial and not governmental activity.

Rationale: The Bank's opening position is the one every private-bank document opened for this playbook takes: the client submits to one forum, and the Bank keeps the right to go wherever the assets are. That is not greed, it is the shape of the product. Enforcement in this business means getting at a securities account, and the account is wherever the custodian keeps it, which is frequently not where the client is and not where the facility is booked. The split governing law is the point a counterparty most often misses and the Bank should explain rather than trade: in England and in Luxembourg the proprietary questions are assigned by statute to the law of the place where the account is maintained, so governing the security document by some other law does not move the analysis, it just creates a mismatch between the document and the law that will decide the case.

**Floor: fallback** — approver: senior lawyer

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | The facility letter and any non-contractual obligations arising out of it are governed by the law of the jurisdiction in which the Bank books the facility. | — | — |
| acceptable | The facility letter is governed by the law of the jurisdiction in which the Bank books the facility and the security agreement is governed by the law of the jur... | — | — |
| fallback | The facility letter is governed by the law of, and the courts of, the jurisdiction agreed between the parties, which may be the jurisdiction in which the Borrow... | The agreed forum is one in which the Bank's counsel confirms a money judgment can be obtained and enforced against the Borrower's assets.; The collateral account is maintained in England and Wales, Switzerland or Luxembourg, and the security document is governed by that jurisdiction's law.; Local counsel in the account's jurisdiction has confirmed that the interim-relief and realisation carve-out is effective there.; A process agent is appointed in the agreed forum and the immunity waiver is unchanged.; Where arbitration is agreed, the interim-relief and collateral-realisation carve-out is in the arbitration clause itself, not only in the facility letter.; Credit and the relevant booking centre have confirmed they can operate an enforcement in the agreed forum. | senior lawyer |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not agree that the security agreement is governed by a law other than that of the jurisdiction in which the collateral account is maintained, or t... | — | — |

**Escalation triggers**

- Any request that the security agreement be governed by a law other than that of the jurisdiction in which the collateral account is maintained.
- Any request to remove the Bank's right to seek interim, protective or conservatory relief, or to realise the collateral, outside the agreed forum.
- Any request to delete or qualify the waiver of immunity where the Borrower or the Pledgor is a trust, a fund, a state or a state-linked entity.
- Any request for arbitration, or for a mandatory negotiation or mediation period, without an unqualified carve-out for interim relief and for steps against the collateral.
- Any request to drop the process agent, or for a replacement period longer than X days, where the Borrower or the Pledgor is not resident in the agreed forum.
- Any deal in which the collateral account is maintained outside England and Wales, Switzerland or Luxembourg, since the jurisdiction overlay in this playbook does not cover it.
- Any request to select the proprietary law of the collateral in the facility letter rather than in the account agreement on a Swiss-booked account.

**Jurisdiction note (luxembourg)**

Luxembourg mirrors England on the conflicts rule and differs from it on everything else. Article 23 of the 2005 Law is a PRIMA rule covering the legal nature and proprietary effects, the requirements for provision and third-party effectiveness, extinction or subordination by a competing interest or good-faith acquisition, the custodian's obligations to a competing claimant, the conditions for realisation after an enforcement event, and the extent of the arrangement over income and proceeds, all governed by the domestic law of the country where the relevant account is maintained with renvoi excluded; and the relevant account may be one maintained by the collateral taker itself (LAW-LU-01, arts. 1(3) and 23). Luxembourg is not a party to the 2006 Hague Convention (HCCH-SEC-CONV-2006 status table), so there is no account-agreement route around that. What makes Luxembourg law worth choosing for the security is arts. 18-20: the netting, the agreed enforcement events and the agreed valuation and enforcement measures are effective against third parties, commissioners, receivers and liquidators notwithstanding domestic or foreign reorganisation or winding-up proceedings (LAW-LU-01). The observed market drafting matches the preferred position here: a published Luxembourg template chooses Luxembourg law and names the 2005 Law as the statute it relies on, makes Luxembourg the sole place of performance, of debt collection for clients domiciled abroad and of jurisdiction, and then reserves the bank's right to sue at the client's domicile or before any other competent authority with Luxembourg law still applying exclusively, all expressly subject to mandatory conflicts rules (BANK-LU-01).

Rules applied: none

### No advice, non-reliance and risk acknowledgement [DRAFT]

- Clause id: no_advice_non_reliance
- Risk rating: high
- Category: parties_reps
- Document: facility_letter

**Opening: preferred**

> Each of the Borrower and the Pledgor represents and acknowledges that it enters into the facility and the security documents on the basis of its own independent analysis and judgement and of such independent advice as it has thought fit to obtain, and is not relying on any statement, representation or assurance by the Bank as to the facility, the documents, the collateral, its value, liquidity or condition, or any other matter. The Bank acts on an execution-only basis in relation to the facility. The Bank gives no investment, tax, legal, accounting or regulatory advice in connection with the facility, makes no recommendation to borrow, to borrow any particular amount, to pledge any particular asset, or to acquire, retain or dispose of any asset, and expresses no view on whether the facility or any resulting position is suitable or appropriate for the Borrower or the Pledgor. Each of the Borrower and the Pledgor further represents that it has the knowledge and experience necessary to evaluate a facility of this kind and the instruments comprising the collateral; that it has access to, and the knowledge to use, the analytical tools needed to evaluate the collateral and the effect of the facility on its portfolio as a whole; and that it has the financial resources and liquidity to bear all the risks of the facility, including the loss of the entire value of the collateral and liability for any shortfall after realisation. Each acknowledges that it has received and read the Bank's risk disclosures; that borrowing against a portfolio magnifies gains and losses and that losses may exceed the amounts deposited; that a fall in value or a change in lending values may require immediate repayment or the delivery of further collateral; that the Bank may realise collateral at a time and on terms that are not of the Borrower's choosing; and that where the facility is in a different currency from the collateral, the currency exposure is the Borrower's. These representations are repeated on each drawing and on each day on which any amount is outstanding.

Rationale: This clause is not there to win an argument after the event; it is there to record what actually happened, which is that the client decided to borrow against its own portfolio. The sophisticated-investor limbs are worth keeping in full because each does different work: the knowledge limb answers "did you understand it", the analytical-tools limb answers "did you model it against the whole portfolio", and the ability-to-bear-loss limb is the only one that answers the question a regulator actually asks, which is whether the client could survive the downside. Execution-only is stated affirmatively rather than by implication, because both of the conduct regimes in scope treat an execution-only relationship differently from an advised one, and the Bank should be saying which one it is in. Every limb here is observed in a filed or published document from this side of the market.

**Floor: fallback** — approver: senior lawyer and compliance

**Position ladder**

| Tier | Summary | Conditions | Approver |
| --- | --- | --- | --- |
| preferred | Each of the Borrower and the Pledgor represents and acknowledges that it enters into the facility and the security documents on the basis of its own independent... | — | — |
| acceptable | The representations in the preferred position are given as acknowledgements of fact, and are qualified as follows. | — | — |
| fallback | Where the Bank or any member of its group provides investment advice or portfolio management to the Borrower or the Pledgor in respect of the portfolio over whi... | The Bank or a member of its group in fact provides advice or portfolio management on the pledged portfolio, so the carve-out matches the relationship.; Compliance has confirmed the suitability or appropriateness assessment meets the applicable conduct rules in the booking jurisdiction and in the client's jurisdiction.; The assessment covers the facility and the portfolio together rather than the investment alone.; The declared purpose of the facility, and any purpose representation, are consistent with the assessment on file.; The Borrower is not an individual in respect of whom a consumer or retail classification is unresolved.; Any applicable withdrawal or cooling-off right has been identified and the facility has been documented accordingly. | senior lawyer and compliance |
| unacceptable (description of the walk-away line, not drafting) | The Bank will not give, or allow the documents to imply, any representation or acknowledgement that it has recommended the facility, approved the leveraged stra... | — | — |

**Escalation triggers**

- Any request to delete the acknowledgement that losses may exceed the amounts deposited or that the Borrower remains liable for a shortfall.
- Any request for a contractual duty on the Bank to warn of an impending or actual collateral shortfall, or to advise on the portfolio.
- Any request to make a margin call, a liquidation or an acceleration conditional on suitability or on the adequacy of a warning.
- Any request for a general carve-out from non-reliance covering statements made by the Bank's staff, rather than a specific written statement the Bank has agreed may be relied on.
- Any deal where the declared purpose is to acquire securities and no documented suitability or appropriateness assessment of the leveraged position is on file, or where the assessment is older than X days.
- Any deal where the Bank or a member of its group advises or manages the pledged portfolio and the conflict acknowledgement and consent has been deleted.
- Any assertion by a counterparty that the facility is outside the conduct perimeter because it is "only lending".

**Jurisdiction note (luxembourg)**

The Luxembourg approach observed in a published template is documentary rather than representational: the facility points at a published investment and risk warning notice and a separate risk disclosure for the more volatile asset classes, then takes a representation that the client has read and accepted them and is aware of the risks, repeated at all times until termination; and it carries a 14 calendar day withdrawal right for a retail client under a distance contract where the facility has not been used (BANK-LU-01). Two practical points follow. The incorporation-by-reference structure means the risk package has to be delivered and its delivery evidenced, which is an operational control rather than a clause. And the withdrawal right has to be identified at intake, because it is a feature of the client's classification and the channel, not of the negotiation. Separately, Luxembourg's consumer credit regime excludes credit granted by a credit institution or investment firm to let an investor carry out a transaction in the relevant financial instruments (LU-CODE-CONSO art. L.224-3), which cuts in the Bank's favour on classification but does nothing for the conduct question this clause is about.

Rules applied: none

### Interest, benchmark rate and benchmark fallback provisions [STUB]

- Clause id: interest_benchmark_fallbacks
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Prepayment and breakage costs [STUB]

- Clause id: prepayment_breakage
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Collateral substitution rights [STUB]

- Clause id: collateral_substitution
- Category: collateral

No drafted positions yet; status stub.

Rules applied: none

### Cross-collateralisation and set-off [STUB]

- Clause id: cross_collateral_set_off
- Category: collateral

No drafted positions yet; status stub.

Rules applied: none

### Representations on source of funds, sanctions and tax status [STUB]

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

### Confidentiality, bank secrecy and permitted disclosure [STUB]

- Clause id: confidentiality_bank_secrecy
- Category: boilerplate

No drafted positions yet; status stub.

Rules applied: none

### Tax gross-up and withholding [STUB]

- Clause id: tax_gross_up
- Category: boilerplate

No drafted positions yet; status stub.

Rules applied: none

### Third-party security: suretyship-type defences and waivers [STUB]

- Clause id: third_party_security_waivers
- Category: parties_reps

No drafted positions yet; status stub.

**Representations/undertakings added by rules**

- [R05_third_party_security] The pledgor confirms that it understands it is securing another person's debt, that it has been advised to take independent legal advice and has had a genuine opportunity to do so, and that it is not relying on the lender for advice about the transaction.

**Drafting notes**

- [R05_third_party_security] Take the standard third-party waivers: no subrogation or contribution until the secured debt is paid in full, no marshalling, no right to require the lender to enforce elsewhere first, and consent to variations of the facility without further notice. Filed private-bank security makes the pledgor's obligations absolute and unconditional irrespective of the validity of the underlying documents, any change in terms or any release of other collateral, with the surety defences waived. Without that the pledgor can interfere with enforcement at exactly the wrong moment.

Rules applied: R05_third_party_security

### Information undertakings and duty to notify [STUB]

- Clause id: information_undertakings
- Category: parties_reps

No drafted positions yet; status stub.

**Drafting notes**

- [R12_third_party_custodian] Require statements and valuations direct from the custodian rather than through the borrower. If the lender is valuing a portfolio it cannot see, the margin mechanics do not work.

Rules applied: R12_third_party_custodian

### Currency mismatch and foreign exchange haircuts [STUB]

- Clause id: currency_mismatch_fx
- Category: collateral

No drafted positions yet; status stub.

Rules applied: none

## Jurisdiction overlay — Luxembourg [DRAFT]

- Creation: The Law of 5 August 2005 on financial collateral arrangements, as amended, most recently by the laws of 20 July 2022 and 15 July 2024, governs the whole field. Collateral means financial instruments and claims, and financial instruments is given the broadest possible meaning, expressly including shares, units in collective investment undertakings, bonds and certificates of deposit. A pledge is created by agreement; the provision of collateral must be capable of being evidenced in writing, in electronic or other durable form, and must allow the collateral to be identified, and for book-entry financial instruments and cash claims it is enough to show that they have been credited to, or form a credit in, a designated account. Article 4 allows the parties to agree an all-present-and-future pledge without needing to designate the collateral specifically, which is exactly what a revolving portfolio needs. Article 2(4) allows collateral to be provided to a person acting for the account of beneficiaries, a fiduciary or a trustee for determined or determinable third-party beneficiaries, who then enjoy the same rights as direct beneficiaries. The Law also covers title transfer for security purposes and fiduciary transfer under Article 13, where a fiduciary must be a financial sector professional, and repurchase agreements under Articles 15 to 17.
- Registration / filing: There is none. Article 26 provides that instruments evidencing a financial collateral arrangement are not subject to registration formalities, and are registered at the fixed rate if voluntarily submitted to the registration formality. There is no equivalent of the English companies charge register for a financial collateral arrangement and no notice filing, which is one of the reasons Luxembourg collateral is quick to take. As in Switzerland, the corollary is that there is nothing to search: priority is determined by the date on which each pledge became enforceable against third parties under Article 5(6). The diligence is therefore documentary, meaning custodian confirmations and express treatment of the custodian's own ranking, rather than a register search.
- Perfection depends on: Possession, defined functionally through the custodian, is what does the work. Article 5(1) provides that the privilege only remains on the pledged collateral if it has been and remains, or is deemed to have remained, in the possession of the pledgee or an agreed third party. For book-entry financial instruments, Article 5(2)(a) gives four alternatives: simply concluding the pledge agreement, where the pledgee is the custodian; a three-party agreement between provider, pledgee and custodian, or a two-party agreement notified to the custodian, under which the custodian will act on the pledgee's instructions without any further agreement of the provider; booking the instruments to an account of the pledgee; or earmarking them, without number specification, in the custodian's books on an account in the provider's or an agreed third-party custodian's name. The second, third and fourth routes are treated as a waiver by the custodian of its own pledge ranking unless otherwise agreed or notified. For other financial instruments, Article 5(3) requires notification to or acknowledgement by the issuer or the third-party custodian, and for a pledge over claims including cash balances, Article 5(4) makes it effective against the debtor and third parties on the mere conclusion of the pledge contract, although the account debtor can still validly pay the provider until it learns of the pledge. Article 2(3) confirms that a right of substitution, a right to withdraw excess collateral, a right to collect proceeds until further notice, and a reserved right of the provider to give instructions do not prejudice the collateral having been provided, which is a materially more collateral-taker-friendly position than the English dispossession case law.
- Enforcement route: Article 11(1) is the centrepiece: on an enforcement event the pledgee may, unless otherwise provided for and without prior notice, appropriate the pledged collateral or have a third party appropriate it at a price determined before or after appropriation by the agreed valuation method; assign it or cause it to be assigned by private sale in a commercially reasonable manner, on a trading venue on which it is admitted to trading, or by public auction; obtain a judgment attributing the collateral in payment on an expert valuation; net under Part V; appropriate listed financial instruments at the market price, or units in a collective investment undertaking at that price or at the last published net asset value provided it is not more than a year old; request redemption of pledged fund units at the redemption price; or exercise the rights under a pledged insurance contract, including surrender. Article 11(3) obliges a third-party custodian to transfer the instruments to the pledgee on notice of an enforcement event without the provider's consent and without informing it in advance, and allows the pledgee to demand payment directly from the debtor of a pledged monetary claim. Article 11(2) sets out the public-auction machinery in detail, with a Luxembourg bailiff or notary as auctioneer, at least eight working days' press notice with prescribed content, sale to the highest bidder with payment permitted by set-off against the secured obligations, and minutes within three working days. The enforcement event is whatever the parties agree under Article 1(6). Lender-side, choose and specify the route and the valuation method in the security agreement, because Article 11 is a menu and the opening words "unless otherwise provided for" mean the drafting can narrow it as well as widen it.
- Financial collateral regime: The instrument is the Law of 5 August 2005 on financial collateral arrangements, transposing Directive 2002/47/EC and repealing the earlier repurchase and transfer-of-ownership-for-security laws. On the scope of persons, natural-person collateral providers ARE covered, in contrast to England: the Law contains no requirement that both parties be non-natural persons, Article 2(1) expressly contemplates financial collateral arrangements and netting agreements entered into either by a merchant or a non-merchant, and Article 20(4) carves the Law of 8 December 2000 on over-indebtedness out of the general disapplication of insolvency law, a carve-out that only makes sense if private individuals are within scope. [VERIFY] that last step is an inference from the primary text rather than an express scope provision, the Law having no scope article naming eligible persons, and it must be confirmed by Luxembourg counsel before it leaves draft. The core benefits sit in Articles 20 and 21: financial collateral arrangements, the agreed enforcement events, netting agreements and the agreed valuation and enforcement measures are valid and enforceable against third parties, commissioners, receivers and liquidators notwithstanding reorganisation measures, winding-up proceedings or any other similar national or foreign proceedings under Article 20(1); termination, valuation, enforcement and netting triggered by an enforcement procedure or protective measure are deemed to have occurred before it under Article 20(2); the listed civil, commercial and national or foreign insolvency, attachment and similar provisions do not apply, with the over-indebtedness law the sole carve-out under Article 20(4); the same rules apply on the death or incapacity of the collateral provider or the debtor under the final paragraph of Article 20(4); arrangements made on the day of opening but before the court decision are valid, and arrangements made after it are valid if the taker proves it neither knew nor should have known, under Article 21. Article 24 confirms that the disapplied national provisions remain disapplied where the collateral provider is established or resident in Luxembourg.
- Governing law of intermediated securities: Article 23 is Luxembourg's PRIMA rule and it mirrors the English account-location rule almost exactly: any question on the listed matters arising in relation to financial collateral over financial instruments transferable by book entry is governed by the law of the country in which the relevant account is maintained, meaning its domestic law with renvoi excluded. The matters covered are the legal nature and proprietary effects, the requirements for provision and for third-party effectiveness, extinction or subordination by a competing interest or a good-faith acquisition, the custodian's obligations to a competing claimant, the conditions for realisation after an enforcement event, and the extent of the arrangement over dividends, income, distributions, reimbursements and proceeds. Relevant account is defined in Article 1(3) as the register or account in which the entries providing the collateral are made, which may be maintained by the collateral taker itself. Luxembourg is not a contracting party to the 2006 Hague Securities Convention, so there is no choice-of-law route to displace the account-location rule. The practical consequence is the same as England's: the account booking location, not the governing law of the pledge agreement, drives the proprietary analysis.
- Practical notes: (1) If the bank is the Luxembourg custodian, Article 5(2)(a)(i) means the pledge agreement alone perfects, which is the cheapest structure of the three jurisdictions; if a third-party custodian holds, use the Article 5(2)(a)(ii) route and take the custodian's acknowledgement in writing, remembering that this route is treated as the custodian waiving its own ranking unless it says otherwise. (2) Use the Article 4 all-present-and-future formulation so that substitutions in a revolving portfolio do not need new security, and rely on Article 2(3) so that the client's right to trade the portfolio until a default notice does not undermine the pledge, which is a genuine structural advantage over English law. (3) Specify the valuation method in the security agreement, because Article 11(1)(a) appropriation is priced by the agreed valuation method, and without one the lender is pushed toward private sale in a commercially reasonable manner or auction. (4) Enforcement without prior notice is the statutory default, but Article 11(1) opens with "unless otherwise provided for", so do not let a negotiated notice period creep into the security agreement unless it is meant, and if the client insists put it in the facility letter as a courtesy undertaking rather than as a condition of the enforcement power. (5) For a natural-person pledgor the Law applies, but the over-indebtedness carve-out in Article 20(4) means full insolvency remoteness cannot be assumed against a Luxembourg-resident individual, so have Luxembourg counsel scope the over-indebtedness procedure for the specific client. (6) For a third-party pledgor the Law is comfortable with security for a third party's obligations and with fiduciary or agent structures under Article 2(4), and Article 2(6) even allows the provider to waive its recourse claims against the principal debtor, valid against third parties, but corporate benefit and, for an individual, independent advice remain ordinary diligence items. (7) The death or incapacity rule in Article 20(4) is directly useful for a private-client pledgor and is worth citing in the events-of-default rationale.

## Not automated on this deal

- Every suitability and appropriateness conclusion. The tool records the purpose, raises the flag and tightens the floor; a person in compliance decides whether the leveraged position is suitable.
- Know-your-client, sanctions and source-of-funds outcomes, including any decision to decline or to exit.
- Reading the trust instrument. No rule in this library can tell anyone whether a power to borrow or to charge exists; a lawyer reads the deed and every deed of appointment, retirement and variation behind it.
- Setting the Trigger Level, the Restoration Level, the Hard Floor and the number of business days. The sources give a band, not an answer.
- Setting the notice period and the term length. Only one opened source states either figure, and both are the institution's risk appetite.
- Setting the notice period itself. Only one opened source concedes one (15 days) and the number here is the institution's risk appetite.
- Setting the payment grace, covenant cure and death standstill periods. Only the institutional grace periods are observed in a source; the standstill is not observed at all.
- Setting the substitution threshold and the acknowledgement deadline. No opened source publishes either.
- The classification of the client that determines whether title transfer is available in the booking jurisdiction.
- The final determination that a borrower is or is not a consumer or a retail client, which drives the withdrawal right, the risk-disclosure package and the classification of the facility.
- Whether a condition has in fact been satisfied. This library lists the items and the rules add to the list; a named person signs each one off.
- Whether a corporate pledgor has corporate benefit, and whether the law of its incorporation restricts financial assistance, upstream or cross-stream security. This is a local counsel question on every deal where the pledgor is not the borrower.
- Whether a legal opinion is required, from whom, and what it must cover on a cross-border structure.
- Whether a limited recourse request is safe on the facts. It turns on the state of the indemnity, the standing of the trustee and the assets actually in the fund, none of which is an intake field.
- Whether a material adverse change or a substantial deterioration has actually occurred on a live position. The clause fixes who decides and on what standard; it does not decide.
- Whether a particular conversation between the relationship manager and the client amounted to a personal recommendation.
- Whether a particular custodian's standard control agreement actually delivers control under the law of the account's location. The tool prints the question; local counsel answers it.
- Whether a particular market move is a "rapid decline" that collapses the notice period. The clause defines who decides, not what the answer is.
- Whether a particular market move is a "rapid decline" that stops the cure clock.
- Whether a written cure plan is credible, which is a judgement about a funding source and not a document check.
- Whether an individual had capacity at signing, and what the Bank does on incapacity short of death. The intake records no fact that answers either, and the treatment of incapacity is an identified gap in this library.
- Whether an individual has lost legal capacity, and whether an attorney, deputy or other representative can give instructions that bind the Borrower or the Pledgor. [VERIFY] no mental-capacity source was opened for this playbook.
- Whether independent legal advice was genuinely given, genuinely independent and genuinely understood.
- Whether repeated forbearance has made an uncommitted line committed in substance. That is a course-of-dealing judgement, and no rule in this library can make it.
- Whether the Borrower is a consumer, and therefore whether a declaration and statement had to precede signing.
- Whether the relationship is in fact execution-only, advisory or discretionary on the pledged portfolio. The clause must match the answer, and the answer is a fact about what people did, not a drafting choice.
- Whether to accept a client's existing custody relationship at all, which is a relationship decision as much as a credit one.
- Whether to accept a foreign-law legal opinion in the form offered, and what it must cover.
- Whether to call a default at all, as against forbearing while the relationship is discussed. Forbearance on a live margin call and waiver of an event of default are both human decisions.
- Whether to call at all on a relationship where the shortfall is small and the portfolio is recovering.
- Whether to decline the facility outright because the leveraged position is unsuitable, notwithstanding that the collateral supports it.
- Whether to disclose the full haircut matrix to a counterparty who asks for it during negotiation.
- Whether to enforce against a deceased individual's collateral before the estate is administered, which is a reputational and conduct decision as much as a legal one.
- Whether to exercise the demand right on a live facility, as against forbearing while the relationship is discussed. The clause fixes who decides; it does not decide.
- Whether to exercise the discretion at all on a live position, as against forbearing while the relationship is discussed.
- Whether to grant forbearance on a live margin call, or to let an expired cure period stand without enforcing.
- Whether to offer committed term at all for relationship reasons, and what that costs in lending value, price and commitment fee.
- Whether to register a charge protectively for a corporate chargor where reliance on the financial collateral regime is doubtful.
- Whether to waive a condition and advance anyway, against what undertaking and for how long.
- Which items belong in Part 1 and which in Part 2 of the fallback schedule on the particular facts. The test is in the rationale; applying it is a judgement.

---

This markup was produced by the SBL Negotiation Playbook Demonstrator, a demonstration tool built from public sources and run against synthetic deals. It is not legal advice. It is not the work product of any institution, and it has not been validated against any institution's credit policy, risk appetite, house style or local counsel advice. Every position is drafted from the lender's side only. The status labels mean exactly what they say: [STUB] means no position has been drafted; [DRAFT] means an entry written from public sources that no named human reviewer has checked; [REVIEWED] means a named reviewer recorded in the library has checked it. Text carrying a [VERIFY] prefix has not been confirmed against a primary source the writer opened. Any concession below a clause's floor, and every item under "Not automated on this deal", is a human decision that this tool does not make.
