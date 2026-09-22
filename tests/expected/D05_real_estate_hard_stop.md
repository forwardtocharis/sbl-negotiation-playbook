# SBL negotiation markup — D05

- Deal: D05
- Description: Synthetic. Borrower A as in D01, a UK-resident individual with a high-net-worth declaration on file, but with thirty per cent of the collateral pool taken as residential real estate alongside the listed portfolio. Everything else is identical to D01. Fictional party; not a real deal.
- Run id: 000000000000
- Timestamp: 1970-01-01T00:00:00+00:00
- Library hash: 7d8caf2f1de399852e2edfb99fdaf1e4d23aaa90da1ce56e9804611cb31d2a72
- Intake hash: da98212e0fbad28c6862d8b16668b761b2c89c4eade0424f5a81f731b099894b
- Governing law: england_wales
- Review status: 0 reviewed / 12 draft / 12 stub

Status warning: positions tagged [DRAFT] or [STUB] have not been reviewed by a named human reviewer and must not be relied on as the lender's settled position.

## Escalations

| Rule id | Clause | Who decides | Reason |
| --- | --- | --- | --- |
| R09_real_estate | eligible_collateral_lending_values | senior lawyer | Real estate collateral is outside the scope of this playbook. The deal needs a real estate finance template and, where the property is residential, a regulatory assessment before terms are issued. |

Exit code: 2

## Flags

### High severity

- **mortgage_regulation** — Real estate has been offered as collateral, and lending secured on land is treated separately from securities-backed lending in all three playbook jurisdictions. In the United Kingdom entering into and administering a regulated mortgage contract are each specified regulated activities, and a contract is regulated where credit is given to an individual or to trustees on the security of a mortgage over land at least 40 per cent of which is used, or intended to be used, as or in connection with a dwelling. Switzerland takes credit secured by a real estate charge outside the Consumer Credit Act altogether, and Luxembourg likewise excludes credit secured on immovable property from the consumer credit chapter — in both cases because it is dealt with elsewhere, not because it is unregulated. [VERIFY] None of the substantive real estate finance regimes — creation, registration, priority or enforcement against land — has been researched for this playbook.
  - Who decides: senior lawyer + compliance
  - Triggering rule: R09_real_estate

### Medium severity

- **consumer_credit** — The borrower is an individual but a high-net-worth or business-purpose declaration is recorded, which is what the United Kingdom exemptions turn on. The risk drops rather than disappearing, because both routes have conditions beyond the declaration itself: on the business-purpose route the presumption created by the declaration is destroyed where the lender, or anyone acting for it, knows or has reasonable cause to suspect that the purpose is not wholly or predominantly a business one, so a file note describing a personal purpose defeats it. On the high-net-worth route the declaration has to sit in the agreement, be no less prominent than the other information, be signed, confirm receipt of the statement of high net worth and record that consumer credit protections are being given up, and the statement itself has to meet the regulator's thresholds and reach the lender before the agreement is made. Check the form, the sequence and whether the declaration is still true. [VERIFY] whether the monetary figures behind either route have been amended since 21 September 2026.
  - Who decides: senior lawyer + compliance
  - Triggering rule: R03b_natural_person_borrower_declared
- **fcar_safe_harbour_uncertain** — [VERIFY] Whether the financial collateral safe harbour is available on these particular facts has not been settled, and it is fact-dependent. What is settled is the rule: the collateral provider here is a natural person and the security is governed by English law, and regulation 3 of the Financial Collateral Arrangements (No. 2) Regulations 2003 requires both parties to a security or title transfer financial collateral arrangement to be non-natural persons, an individual being excluded. On those facts the arrangement is not a financial collateral arrangement and the statutory machinery is not available: no appropriation under an express power without a court order (reg 17), no commercially-reasonable-valuation framework for appropriation (reg 18), and no disapplication of the insolvency restrictions on enforcing security (regs 8 and 10). Two things keep this uncertain rather than closed: the test looks at the parties to the collateral arrangement, so an individual borrower with a corporate or trustee-company pledgor can still be inside the regime; and even with two non-natural persons the arrangement must still satisfy possession or control, which the English courts read as requiring real dispossession of the provider. Do not rely on appropriation in the enforcement clause; rely on an express power of sale with Law of Property Act 1925 s.103 disapplied, and confirm the analysis with counsel.
  - Who decides: senior lawyer
  - Triggering rule: R04_natural_person_pledgor_england

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

**Jurisdiction note (england_wales)**

The demand feature is at its most sensitive where the Borrower is an individual, because it is the regulated-credit perimeter rather than the contract that decides what "repayable on demand" is actually worth. The high-net-worth exemption route requires a prescribed declaration by the borrower giving up the protections of a regulated agreement together with a compliant statement of income or assets delivered to the lender before the agreement is made, with a credit threshold of GBP 60,260 where the agreement is not secured on land (LAW-UK-02). The sequencing is the practical point for this clause: the facility type and the declaration are settled together at signing, because a declaration signed afterwards does not cure the agreement.

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

**Drafting notes**

- [R03b_natural_person_borrower_declared] Keep the signed declaration and the statement of high net worth on file with the facility letter, and make the declaration a representation that repeats, so that a change in the borrower's circumstances is a matter the lender hears about rather than discovers.

**Jurisdiction note (england_wales)**

Perfection here is not a filing question and the conditions precedent should not be written as though it were. What matters is whether the Bank has possession or control for the purposes of the financial collateral regime: crediting collateral to an account in the collateral-taker's name counts as possession where the provider's rights are limited to substituting collateral of equal or greater value or withdrawing excess (LAW-EW-01, reg. 3). Where the arrangement qualifies as a security financial collateral arrangement, the company charge registration provisions of the Companies Act 2006 (s.859A, charges created by a company, and s.859H, the consequence of failing to register) are disapplied (LAW-EW-03, reg. 4(4)). The trap for this clause is that the disapplication is only as good as the qualification, and the regime does not reach an arrangement where the collateral provider is a natural person (LAW-EW-01, reg. 3), so where there is any doubt the CP list should carry a protective registration step: a registration that turns out to have been unnecessary costs a fee, and one that turns out to have been necessary cannot be made late.

Rules applied: R03b_natural_person_borrower_declared

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

**Drafting notes**

- [R09_real_estate] Real estate is out of scope for this playbook. This tool holds no positions, no lending values, no perfection steps and no enforcement route for land, and nothing in this output should be used for the real estate element of the deal.

**Jurisdiction note (england_wales)**

Draw the eligibility schedule so that everything in it can in fact be brought within the Bank's possession or control, because the financial collateral regime turns on that and on the collateral being cash, financial instruments or credit claims (LAW-EW-01). Assets that cannot be held in the controlled account, or that sit outside those categories, are outside the regime however comfortable the Bank is with them commercially. The regime also requires both the collateral-provider and the collateral-taker to be non-natural persons, so where the Pledgor is an individual the eligibility schedule is doing work the statutory regime will not back up.

Rules applied: R09_real_estate

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

**Jurisdiction note (england_wales)**

No jurisdiction-specific variation identified [VERIFY]

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

**Jurisdiction note (england_wales)**

Where the Bank ends up exercising this discretion on enforcement, the English standard is that the manner of valuation must be commercially reasonable judged objectively; the result itself need not be reasonable, the collateral-taker stays responsible even where it uses a third-party valuer, and a failure to comply does not unwind an appropriation but allows the court to substitute a compliant valuation (FIRM-02, on the 2022 English High Court decision on appropriation under the financial collateral regulations). An English-law security deed in the source pool applies the same good-faith-and-commercially-reasonable standard to determining excess financial collateral (EDGAR-EN-01). That is the argument for why conceding the acceptable tier is survivable in England: the standard governs process, not outcome.

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

**Jurisdiction note (england_wales)**

The cure sequence is where an English enforcement is won or lost, because the enforcement remedy may not be the statutory one. Where the collateral provider is an individual, the Financial Collateral Arrangements (No. 2) Regulations 2003 do not apply at all: reg. 3 requires both parties to be non-natural persons (LAW-EW-01). [VERIFY] The consequence usually drawn from that - that the Bank is left enforcing under an express contractual power of sale, subject to the mortgagee's equitable duty to take reasonable care to obtain a proper price - is stated in the WP7 research file (docs/research/jurisdictions_research.md) and was not confirmed against the primary text by this agent; build_plan.md and the WP3 brief both list it as a known gap. A documented call, a stated cure period, a dated notice and a record of what the Borrower said it would do are the evidence that the duty was discharged, which is why the acceptable tier is easier to defend in England than the demand-only preferred tier even though the preferred tier is commercially stronger. Note also that the Law of Property Act 1925 statutory power of sale is cut down by s.103, which requires notice plus three months' default, or two months' interest in arrear, or breach of another provision of the deed, so the security document should contract out of s.103 and rely on the cure mechanics in this clause instead (LAW-EW-02).

Rules applied: none

### Security structure: pledge, charge or title transfer, plus control and custody [DRAFT]

- Clause id: security_structure_control
- Risk rating: high
- Category: collateral
- Document: security_agreement

**Opening: preferred**

> The Pledgor grants to the Bank a first-ranking and continuing security interest over each Collateral Account, over all financial instruments and cash from time to time credited to it, over all rights attaching to them and over all proceeds, present and future, taking the form the Bank determines to be most effective under the law of the place where the Collateral Account is maintained, and the Pledgor will execute any further document and give any further instruction the Bank requires for that purpose. The Bank or a member of its group is the Custodian. No financial instrument or cash may be withdrawn, transferred, sold, substituted or otherwise dealt with, and no instruction to the Custodian is effective, without the Bank's prior consent, which the Bank may withhold; the Bank may release only such assets as it determines to be in excess of its requirements, taking lending values, currency exposure, tax and any other risk into account. The Pledgor will create no other security interest over, and will permit no filing, registration or notice in respect of, any Collateral Account or any asset credited to it, will defend the collateral against any adverse claim, and will bear the Bank's costs of perfecting, defending and enforcing the security. Voting and other rights attaching to the collateral are exercisable by the Pledgor only until the Bank gives notice, after which they are exercisable by the Bank or its nominee under an irrevocable power of attorney given by the Pledgor. The Bank reserves the right to use, transfer or dispose of the collateral to the extent permitted by the applicable law and any authorisation given by the Pledgor.

Rationale: What makes this product lendable is not the security document, it is that the Bank is holding the assets and can stop them moving. Where the Bank is the Custodian the structure is at its cheapest and its fastest in all three jurisdictions in this playbook: the pledge agreement alone perfects in Luxembourg, an agreement with the custodian alone does it in Switzerland, and in England the possession-or-control question answers itself. Full dominion with releases in the Bank's gift is also the observed private-bank position rather than an aggressive one. The reason to open here and not one tier down is that every concession in this clause is a concession about who can move an asset on the morning of a default, and that is the one question the Bank cannot afford to have argued about on the day.

**Floor: fallback** — approver: senior lawyer

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

- [R04_natural_person_pledgor_england] Draft the security so that it stands up without the financial collateral regime: an express contractual power of sale with s.103 of the Law of Property Act 1925 disapplied, a clear statement of the lender's control over the account, and no reliance on appropriation as the only enforcement route. Keep the equitable duty to take reasonable care to obtain a proper price and evidence it with a documented valuation and sale process. If the safe harbour turns out to be available, nothing is lost by having drafted around it.

**Jurisdiction note (england_wales)**

Two English points change the drafting rather than decorate it. First, form: a true common-law pledge depends on delivery of possession of a tangible thing, so English custody security is drafted as a mortgage or fixed charge over the securities account and its contents, with a floating charge fallback; the financial collateral regulations treat pledge, mortgage, fixed charge, floating charge and lien alike as security interests, so the label is not what decides whether the regime applies (LAW-EW-01; the point that a true common-law pledge is awkward over intangible custody assets, and that English custody security is therefore drafted as mortgage or charge language, is practice commentary recorded in FIRM-04 rather than statute). Second, scope: the regulations require BOTH parties to be non-natural persons, so where the collateral provider is an individual - the ordinary private-wealth case, and the classic third-party spouse or family pledgor - the arrangement is not a financial collateral arrangement (LAW-EW-01). [VERIFY] The consequence usually drawn from that, namely that the registration exemption, the insolvency disapplications and appropriation are all unavailable on those facts, comes from the WP7 research file (docs/research/jurisdictions_research.md) and was not confirmed against the primary text by this agent; the WP3 brief lists it as a known gap. Even with two non-natural persons, possession or control has to be real: the English decisions in this area have required actual dispossession of the provider, so a lender holding as a bare nominee with no more dominion than a custodian does not have control (FIRM-04). Practical consequences: draft an express power of sale and do not rely on appropriation; make the account control agreement deliver dispossession in substance; and for a corporate chargor decide the Companies Act registration question deliberately and record the decision, because relying on the exemption in reg. 4 is a bet on the arrangement qualifying at all (LAW-EW-03).

Rules applied: R04_natural_person_pledgor_england

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

- [R03b_natural_person_borrower_declared] Where the borrower is an individual, death and incapacity need to be handled expressly rather than left to the insolvency wording. Say what happens to the facility, who the lender may deal with, and whether the portfolio is frozen or may be liquidated in the meantime.

**Jurisdiction note (england_wales)**

The death or personal insolvency of an individual Borrower or Pledgor is where the English structural problem in this playbook bites hardest. A security financial collateral arrangement requires both the collateral provider and the collateral taker to be non-natural persons (LAW-EW-01), so where the Pledgor is an individual the Bank has none of the regime's self-help on a default: no appropriation under an express power, and none of the insolvency disapplications. On personal bankruptcy the secured creditor's right to enforce its security is preserved (UK-IA-1986 s.285), but what is preserved is a contractual power of sale, not the statutory conveniences. The drafting consequence is that the death and capacity limbs of this clause carry more weight in England than elsewhere, and that enforcement should be planned around a documented sale under a contractual power rather than around appropriation. [VERIFY] the wider consequences of the natural-person exclusion - bills of sale legislation, charge registration and what the market actually does for individual pledgors in England - were not sourced for this playbook and are the subject of the fcar_safe_harbour_uncertain flag.

Rules applied: R03b_natural_person_borrower_declared

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

**Drafting notes**

- [R09_real_estate] Real estate is out of scope for this playbook. Enforcement against land is slower and more formal than enforcement against a securities account, and the positions in this clause were not written with it in mind.
- [R04_natural_person_pledgor_england] What is lost where the provider is an individual is the self-help package, not the security itself: on personal bankruptcy s.285(4) of the Insolvency Act 1986 preserves a secured creditor's right to enforce. Plan for enforcement that takes longer and is more visible than an appropriation would have been.

**Jurisdiction note (england_wales)**

England gives the Bank a statutory self-help remedy and then takes it away from most private-wealth deals. Under the financial collateral regulations a collateral-taker whose arrangement contains an express appropriation power may appropriate without any court order for foreclosure (LAW-EW-04), and must value the collateral in accordance with the arrangement and in any event in a commercially reasonable manner, accounting for any excess (LAW-EW-05); the English authority on that provision holds that it is the MANNER of the valuation that must be commercially reasonable, judged objectively, that the result need not be reasonable, that responsibility stays with the collateral-taker even where a third-party valuer is used, and that a non-compliant valuation does not unwind the appropriation but lets the court substitute a compliant one (FIRM-02). But the regulations require both parties to be non-natural persons, so where the collateral provider is an individual the arrangement is not a financial collateral arrangement at all (LAW-EW-01). [VERIFY] The consequence usually drawn from that - that there is no self-help appropriation in English law outside the regulations, so the Bank is left enforcing under an express contractual power of sale subject to the equitable duty to take reasonable care to obtain a proper price - comes from the WP7 research file (docs/research/jurisdictions_research.md) and was not confirmed against the primary text by this agent; the WP3 brief lists it as a known gap, and it is the single most important thing to check before this clause is promoted beyond draft. Draft both powers, contract out of the Law of Property Act 1925 s.103 pre-conditions so the statutory power is not cut down by a three-month notice requirement (LAW-EW-02), and specify the valuation method so the commercially reasonable standard is evidenced by a process rather than argued about afterwards.

Rules applied: R09_real_estate, R04_natural_person_pledgor_england

### Capacity, authority and due execution for trusts, corporates and partnerships [DRAFT]

- Clause id: capacity_authority
- Risk rating: high
- Category: parties_reps
- Document: all

**Opening: preferred**

> Each of the Borrower and each Pledgor represents and warrants that it is duly constituted and validly existing; that it has the power and authority to enter into and perform the finance documents and to create the security; that every action, consent and authorisation required by its constitutional or trust documents, by any applicable law or by any agreement binding on it, including any shareholder, beneficiary, partner or protector consent, has been taken or obtained and is in full force; that the finance documents have been executed by persons authorised to do so; that its obligations are legal, valid, binding and enforceable; that entry into and performance of them does not conflict with its constitutional or trust documents, any law or any agreement binding on it; and that it is solvent and will not be rendered insolvent by the transaction. Where a party contracts as trustee, it further represents that it is duly appointed and is the sole trustee or is acting with all of its co-trustees; that the trust instrument and every deed of appointment, retirement or variation empower it to borrow, to charge the trust assets and to delegate as contemplated by the finance documents; that it is not acting in breach of trust and has no notice of any claim that it is; and that its right of indemnity out of the trust fund is not excluded, limited or impaired, and it undertakes not to exclude, limit or impair it, not to retire without a replacement trustee acceding to the finance documents, not to distribute or appoint trust property, and not to incur any liability ranking in priority to the Bank's claim on that indemnity, in each case without the Bank's prior written consent. The trustee contracts in both its personal and its trustee capacity and its liability is not limited to the trust fund. Where a party is a partnership, it represents that the borrowing and the security are within the ordinary course of the partnership business or have been authorised by all of the partners, that the partnership agreement permits them, and that each partner is jointly and, where its constitution permits, severally liable, and it undertakes to notify any change in the partners and to procure that any incoming partner accedes. Where a Pledgor is not the Borrower, its obligations are absolute and unconditional irrespective of the validity or enforceability of the Borrower's obligations, any variation of the facility, any release of other collateral or guarantees, or any other circumstance which would otherwise operate as a defence available to a surety, all of which are waived. Each Pledgor which is a company further represents that granting the security is for its corporate benefit as determined by its board and does not constitute unlawful financial assistance. Each representation is repeated on each utilisation date and on each day on which any amount is outstanding, and each of the Borrower and each Pledgor undertakes to notify the Bank immediately of any change in its beneficial owners, trustees, general partner or controllers, any such change being subject to fresh know-your-client review and to the Bank's approval.

Rationale: This clause is the one that decides whether the Bank has security at all, because a pledge granted by someone who lacked the power to grant it is not a weak pledge, it is no pledge. The cost of getting it right is a week of reading documents the client already has; the cost of getting it wrong surfaces on the day the Bank tries to sell, which is the day the beneficiaries or the minority shareholder appear. Full personal recourse against a trustee is the opening position rather than the answer, but it has to be the opening position, because the moment the Bank concedes limited recourse it is relying entirely on the trustee's indemnity and it needs to have asked about that indemnity first. The notification undertaking is the cheapest thing on the list and the most useful: capacity is not a fact about signing day, it is a fact about every day the loan is outstanding.

**Floor: fallback** — approver: senior lawyer + head of credit

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

**Jurisdiction note (england_wales)**

For an English company, capacity is largely not the risk and authority is: the validity of an act done by a company cannot be called into question on the ground of lack of capacity by reason of anything in the company's constitution (LAW-EW-07, Companies Act 2006 s.39), and in favour of a person dealing with a company in good faith the power of the directors to bind it is deemed free of any limitation under the constitution, with no duty to enquire, good faith presumed, and knowledge that an act is beyond the directors' powers not by itself bad faith (LAW-EW-06, s.40). What is left is the overlay: the directors' duty to act in the way they consider in good faith would be most likely to promote the success of the company for the benefit of its members as a whole (LAW-EW-09, s.172), which is why a third-party pledge needs a resolution that articulates the benefit to the pledgor rather than to the group; and the prohibition on a public company, or a subsidiary of one, giving financial assistance directly or indirectly for the purpose of an acquisition of its shares or to reduce or discharge a liability incurred for such an acquisition, subject to the principal-purpose and larger-purpose exceptions and to the requirement of good faith in the company's interests (LAW-EW-08, s.678). For trusts, there is a statutory power to raise money by sale, conversion, calling in or mortgage of trust property where the trustees are authorised by the trust instrument or by law to pay or apply capital money for any purpose, which applies notwithstanding anything to the contrary in the instrument but does not apply to trustees of charitable property or to settlement trustees who are not also statutory owners (LAW-EW-TA1925-S16, Trustee Act 1925 s.16); that power is conditional on there being an authorised purpose, so it does not remove the need to read the deed. The indemnity that the whole limited-recourse ladder depends on has its statutory anchor in the trustee's entitlement to be reimbursed from, or to pay out of, the trust funds expenses properly incurred when acting on behalf of the trust (LAW-EW-TA2000-S31, Trustee Act 2000 s.31) - note the word "properly", which is where an improper transaction loses the indemnity. For partnerships, every partner is an agent of the firm and of the other partners for the purpose of the partnership business, and acts in the ordinary course bind the firm unless the partner in fact had no authority and the counterparty either knew that or did not know or believe him to be a partner (LAW-EW-PA1890-S5, Partnership Act 1890 s.5) - which cuts both ways for a lender who has read the partnership agreement and therefore knows what it says. [VERIFY] Limited partnerships and limited liability partnerships are governed by different statutes which were not opened for this entry, and nothing here should be applied to them. [VERIFY] The undue influence and independent legal advice case law relied on in the unacceptable tier was not opened either; the drafting position is standard practice, not a sourced proposition.

Rules applied: none

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

**Jurisdiction note (england_wales)**

England applies a PRIMA rule to book entry securities collateral: the legal nature and proprietary effects of the collateral, the requirements for its provision and for third-party effectiveness, whether title is extinguished or subordinated by a competing interest or a good-faith acquisition, priority, and the steps required to realise the collateral after an enforcement event are all governed by the domestic law of the country in which the relevant account is maintained, with renvoi excluded (UK-FCAR-2003 reg 19). The United Kingdom is not a contracting party to the 2006 Hague Securities Convention (HCCH-SEC-CONV-2006 status table), so the proprietary law cannot be selected in the account agreement the way a Swiss-booked structure allows. Two consequences for this clause. First, an English governing-law clause in the facility letter settles the contract and not the security: if the account sits in Zurich or Luxembourg, the creation, third-party effectiveness and realisation questions are for that law and for local counsel. Second, the advantages of the English financial collateral regime turn on the status of the parties - both must be non-natural persons - and on possession or control, not on the choice of law, so choosing English law does not deliver the regime to a facility with an individual pledgor (LAW-EW-01). The one English-law security document opened in the source pool governs the deed, the amendment notice and any non-contractual obligations by English law, which is the drafting convention to follow (EDGAR-EN-01).

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

**Jurisdiction note (england_wales)**

The UK conduct rules do not ask whether the facility letter contains a non-reliance clause; they ask what the Bank did. A personal recommendation must be suitable and in accordance with the client's risk tolerance and ability to bear losses, the firm must obtain information on the source and extent of regular income, assets including liquid assets, investments and real property and regular financial commitments, and on holding period, risk preferences, risk profile and the purpose of the investment, and the firm is expressly told to consider the suitability of the overall transaction where an instrument is linked directly or indirectly to any form of loan or mortgage (UK-COBS-9A.2). That last point is the one that matters for this clause: where the Bank advises, the leverage and the investment are assessed together, so the no-advice wording has to be consistent with the advice actually given and the fallback tier's documented assessment is the real protection. [VERIFY] the effect of contractual non-reliance and basis-of-dealing wording under English law, and any statutory control on it, was not sourced for this playbook; the clause asserts nothing about whether such wording operates as an estoppel.

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

Rules applied: none

### Information undertakings and duty to notify [STUB]

- Clause id: information_undertakings
- Category: parties_reps

No drafted positions yet; status stub.

Rules applied: none

### Currency mismatch and foreign exchange haircuts [STUB]

- Clause id: currency_mismatch_fx
- Category: collateral

No drafted positions yet; status stub.

Rules applied: none

## Jurisdiction overlay — England and Wales [DRAFT]

- Creation: For a portfolio of intermediated securities and cash held with a custodian, English practice takes a security interest, normally an equitable mortgage or a fixed charge over the securities account, the securities credited to it, the cash balances and all proceeds, with a floating charge fallback; less commonly in this product the parties use a title transfer arrangement under which legal and beneficial ownership passes and the taker owes an obligation to deliver equivalent assets back. A true common-law pledge sits awkwardly here because it depends on delivery of possession of a tangible thing, which is why English custody security is drafted in mortgage and charge language rather than as a pledge. The financial collateral regulations treat pledge, mortgage, fixed charge, floating charge and lien alike as security interests, so the statutory benefits can attach to a charge where the other conditions are met. Lender-side, take a fixed charge or mortgage plus an express contractual power of sale and an express power of appropriation, and do not rely on the label the document uses. In a 2012 administration decision the court analysed a clause drafted as a general lien over intangible custody assets as a charge, so the substance of the dealing rights, not the heading, decides the characterisation.
- Registration / filing: For a corporate chargor, Companies Act 2006 s.859A would normally require a statement of particulars to reach the registrar within 21 days beginning with the day after creation, and s.859H makes an unregistered registrable charge void against a liquidator, administrator or creditor. Regulation 4(4) of the financial collateral regulations, as amended with effect from 6 April 2013, disapplies both s.859A and s.859H in relation to a security financial collateral arrangement and any charge created or arising under one, so a qualifying arrangement over a securities account needs no Companies House filing. The weak link is that the exemption is only as good as the qualification: if the arrangement turns out not to be a security financial collateral arrangement, because a party is an individual or because possession or control is not made out, the registration duty was live all along and the 21 days have gone. The lender-side line is therefore to register protectively wherever there is any doubt, because a needless registration costs almost nothing and a missed one is fatal. There is no public filing regime for security granted by an individual over intangible investments in England, so registration is simply not a live question for a natural-person pledgor.
- Perfection depends on: England has no filing-based perfection for this collateral, so two questions do the commercial work. The first is whether the charge is fixed rather than floating, which turns on how far the client is free to deal with the collateral without the lender's consent. The second is whether the collateral-taker has possession or control for the purposes of the financial collateral regulations: regulation 3 treats collateral as in the taker's possession where it is credited to an account in the taker's name and the provider's rights are limited to substituting collateral of the same or greater value or withdrawing excess. The reported case law requires real dispossession of the provider, so a lender holding assets as a pure nominee with no more dominion than a custodian does not have control. Where the lender is also the custodian, control is straightforward and should be documented in the security agreement and reflected in the account terms. Where a third-party custodian holds, take an account control agreement that switches off the client's dealing and withdrawal rights on a default notice and obliges the custodian to act on the lender's instructions alone.
- Enforcement route: There are two routes and a well-drafted facility keeps both open. Sale runs either under an express contractual power or under the Law of Property Act 1925 s.101 power where the security is made by deed; s.101 is cut down by s.103, which stops the power being exercised until notice requiring payment has been served and three months' default has run, or two months' interest is in arrear, or another provision of the mortgage deed has been breached, so lenders routinely contract out of s.103 and rely on express drafting while remaining subject to the equitable duty to take reasonable care to obtain a proper price. Appropriation runs under regulation 17, which lets a collateral-taker whose security financial collateral arrangement contains an appropriation power appropriate the collateral in accordance with its terms without any order for foreclosure from the court, and regulation 18 requires the taker to value the collateral in accordance with the arrangement and in any event in a commercially reasonable manner, accounting for any excess and leaving the provider liable for any shortfall. Outside those regulations there is no self-help appropriation in English law, because foreclosure needs the court, which is why the qualification question matters so much commercially. Regulation 8 disapplies the administration moratorium and the related Insolvency Act 1986 restrictions on enforcing security for financial collateral arrangements. For an individual chargor there is no equivalent need, because Insolvency Act 1986 s.285(4) already preserves the secured creditor's right to enforce notwithstanding the restrictions on creditors' remedies after a bankruptcy order.
- Financial collateral regime: The instrument is the Financial Collateral Arrangements (No. 2) Regulations 2003 (SI 2003/3226), implementing Directive 2002/47/EC and retained after EU exit. It recognises two arrangement types, the security financial collateral arrangement and the title transfer financial collateral arrangement. Both require written evidence, collateral consisting of cash, financial instruments or credit claims, and delivery or transfer so that the collateral is in the possession or under the control of the taker. Decisively for private wealth, natural-person collateral providers are NOT covered: regulation 3 requires both parties to the arrangement to be non-natural persons, a non-natural person being any corporate body, unincorporated firm, partnership or body with legal personality except an individual, including bodies formed under foreign or international law. The benefits that turn on that scope test are no Companies Act registration (regulation 4), disapplication of insolvency restrictions on enforcement and of certain avoidance provisions (regulations 8 and 10), close-out netting effective in accordance with its terms (regulation 12), protection where the taker was unaware of a winding-up or reorganisation (regulation 13), right of use (regulation 16), and appropriation without a court order (regulation 17) subject to commercially reasonable valuation (regulation 18). So where the collateral provider is an individual client or an individual third-party pledgor the whole package is off the table, and the enforcement clause must be built on a contractual power of sale instead; see the financial collateral safe-harbour flag in playbook/flags/regulatory_flags.yaml.
- Governing law of intermediated securities: Regulation 19 applies a PRIMA-style rule to book entry securities collateral: the listed questions are governed by the domestic law of the country in which the relevant account is maintained, with renvoi excluded. The questions covered are the legal nature and proprietary effects of the collateral, the requirements for provision and for third-party effectiveness, whether title is extinguished or subordinated by a competing interest or a good-faith acquisition, priority, and the steps required to realise the collateral after an enforcement event. The United Kingdom is not a contracting party to the 2006 Hague Securities Convention, whose contracting parties are Mauritius, Switzerland and the United States and which entered into force on 1 April 2017, so the proprietary law cannot be selected by agreement in the account agreement the way a Swiss-booked structure allows. The practical consequence for a deal lawyer is that the governing law clause in the facility and security documents does not settle the proprietary analysis; the booking location of the account does. If the facility is English law but the account is maintained in Zurich or Luxembourg, take local counsel on creation, third-party effectiveness and realisation.
- Practical notes: (1) Establish at intake whether every party to the collateral arrangement is a non-natural person; if not, delete or condition any reliance on appropriation and on the insolvency disapplications, and say so in the enforcement clause rather than leaving boilerplate that does not work. (2) Establish where the account is maintained, because regulation 19 makes that the proprietary law, and take local counsel if it is not England. (3) If the lender is not the custodian, make an executed account control agreement a condition precedent, and make sure it delivers dispossession in substance and not just a notice of charge. (4) For a corporate chargor, decide the registration question deliberately and record the decision, because relying on regulation 4 means betting the security on the qualification. (5) Draft both a sale power and an appropriation power, contract out of s.103, and specify the valuation method so that the commercially reasonable standard is evidenced by a process rather than argued about after the event. (6) For a third-party pledgor, take separate independent legal advice confirmations and consider undue influence and misrepresentation risk where the pledgor is a spouse or family member of the borrower, and corporate benefit and financial assistance questions where the pledgor is a company; [VERIFY] that independent-advice practice point is stated from general practice and has not been sourced to authority. (7) For a natural-person pledgor, bankruptcy leaves the right to enforce intact under s.285(4) but gives none of the statutory self-help, so plan for a sale under a contractual power, not appropriation.

## Not automated on this deal

- Choosing the booking centre for a new relationship, which is a commercial, tax and regulatory decision as well as a legal one.
- Every cross-border perfection and enforceability conclusion. The playbook cites the rule; local counsel in the account's jurisdiction confirms it, and that confirmation is a condition precedent, not a drafting note.
- Every suitability and appropriateness conclusion. The tool records the purpose, raises the flag and tightens the floor; a person in compliance decides whether the leveraged position is suitable.
- Know-your-client, sanctions and source-of-funds outcomes, including any decision to decline or to exit.
- Reading the trust instrument. No rule in this library can tell anyone whether a power to borrow or to charge exists; a lawyer reads the deed and every deed of appointment, retirement and variation behind it.
- Setting the Trigger Level, the Restoration Level, the Hard Floor and the number of business days. The sources give a band, not an answer.
- Setting the notice period and the term length. Only one opened source states either figure, and both are the institution's risk appetite.
- Setting the notice period itself. Only one opened source concedes one (15 days) and the number here is the institution's risk appetite.
- Setting the notice period. Three observations exist across one composite filing, and the number is risk appetite.
- Setting the numeric grid itself. The demonstrator carries X placeholders because no public source opened for this playbook publishes one.
- Setting the payment grace, covenant cure and death standstill periods. Only the institutional grace periods are observed in a source; the standstill is not observed at all.
- Setting the substitution threshold and the acknowledgement deadline. No opened source publishes either.
- The classification of the client that determines whether title transfer is available in the booking jurisdiction.
- The decision to enforce at all, as against forbearing while the relationship is discussed. The tool never makes that call.
- The final determination that a borrower is or is not a consumer or a retail client, which drives the withdrawal right, the risk-disclosure package and the classification of the facility.
- Whether a closed period, an issuer or underwriter consent or a volume limit blocks or delays a sale, and whether compliance has cleared it.
- Whether a condition has in fact been satisfied. This library lists the items and the rules add to the list; a named person signs each one off.
- Whether a corporate pledgor has corporate benefit, and whether the law of its incorporation restricts financial assistance, upstream or cross-stream security. This is a local counsel question on every deal where the pledgor is not the borrower.
- Whether a legal opinion is required, from whom, and what it must cover on a cross-border structure.
- Whether a limited recourse request is safe on the facts. It turns on the state of the indemnity, the standing of the trustee and the assets actually in the fund, none of which is an intake field.
- Whether a material adverse change or a substantial deterioration has actually occurred on a live position. The clause fixes who decides and on what standard; it does not decide.
- Whether a particular conversation between the relationship manager and the client amounted to a personal recommendation.
- Whether a particular custodian's standard control agreement actually delivers control under the law of the account's location. The tool prints the question; local counsel answers it.
- Whether a particular market move is a "rapid decline" that collapses the notice period. The clause defines who decides, not what the answer is.
- Whether a particular market move is a "rapid decline" that removes the notice period.
- Whether a particular market move is a "rapid decline" that stops the cure clock.
- Whether a proposed sale method is commercially reasonable on the facts of the day, including the choice between a bookbuild, a programme and a private placement.
- Whether a specific holding is admitted to the Eligible Collateral Schedule, and at what lending value percentage.
- Whether a written cure plan is credible, which is a judgement about a funding source and not a document check.
- Whether an asset that becomes illiquid or restricted after drawdown is re-rated immediately or on notice.
- Whether an asymmetric jurisdiction clause will be given effect in the forum where the Bank would actually use it. [VERIFY] not sourced for this playbook.
- Whether an individual had capacity at signing, and what the Bank does on incapacity short of death. The intake records no fact that answers either, and the treatment of incapacity is an identified gap in this library.
- Whether an individual has lost legal capacity, and whether an attorney, deputy or other representative can give instructions that bind the Borrower or the Pledgor. [VERIFY] no mental-capacity source was opened for this playbook.
- Whether independent legal advice was genuinely given, genuinely independent and genuinely understood.
- Whether notice is required by law and unwaivable in the booking jurisdiction, and on whom it must be served where the Pledgor is not the Borrower.
- Whether repeated forbearance has made an uncommitted line committed in substance. That is a course-of-dealing judgement, and no rule in this library can make it.
- Whether the Borrower is a consumer, and therefore whether a declaration and statement had to precede signing.
- Whether the Borrower or the Pledgor is capable of claiming immunity at all, which turns on its constitution and on the law of the place of enforcement.
- Whether the relationship is in fact execution-only, advisory or discretionary on the pledged portfolio. The clause must match the answer, and the answer is a fact about what people did, not a drafting choice.
- Whether to accept a client's existing custody relationship at all, which is a relationship decision as much as a credit one.
- Whether to accept a foreign-law legal opinion in the form offered, and what it must cover.
- Whether to call a default at all, as against forbearing while the relationship is discussed. Forbearance on a live margin call and waiver of an event of default are both human decisions.
- Whether to call at all on a relationship where the shortfall is small and the portfolio is recovering.
- Whether to commence proceedings in a second jurisdiction, and the disclosure of client information that doing so entails in a bank-secrecy jurisdiction.
- Whether to decline the facility outright because the leveraged position is unsuitable, notwithstanding that the collateral supports it.
- Whether to disclose the full haircut matrix to a counterparty who asks for it during negotiation.
- Whether to enforce against a deceased individual's collateral before the estate is administered, which is a reputational and conduct decision as much as a legal one.
- Whether to exercise the demand right on a live facility, as against forbearing while the relationship is discussed. The clause fixes who decides; it does not decide.
- Whether to exercise the discretion at all on a live position, as against forbearing while the relationship is discussed.
- Whether to grant forbearance on a live margin call, or to let an expired cure period stand without enforcing.
- Whether to offer committed term at all for relationship reasons, and what that costs in lending value, price and commitment fee.
- Whether to register a charge protectively for a corporate chargor where reliance on the financial collateral regime is doubtful.
- Whether to take a concentrated but high-quality single holding at a reduced lending value rather than excluding it.
- Whether to waive a condition and advance anyway, against what undertaking and for how long.
- Which items belong in Part 1 and which in Part 2 of the fallback schedule on the particular facts. The test is in the rationale; applying it is a judgement.

---

This markup was produced by the SBL Negotiation Playbook Demonstrator, a demonstration tool built from public sources and run against synthetic deals. It is not legal advice. It is not the work product of any institution, and it has not been validated against any institution's credit policy, risk appetite, house style or local counsel advice. Every position is drafted from the lender's side only. The status labels mean exactly what they say: [STUB] means no position has been drafted; [DRAFT] means an entry written from public sources that no named human reviewer has checked; [REVIEWED] means a named reviewer recorded in the library has checked it. Text carrying a [VERIFY] prefix has not been confirmed against a primary source the writer opened. Any concession below a clause's floor, and every item under "Not automated on this deal", is a human decision that this tool does not make.
