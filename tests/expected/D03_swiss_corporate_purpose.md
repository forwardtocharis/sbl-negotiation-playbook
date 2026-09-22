# SBL negotiation markup — D03

- Deal: D03
- Description: Synthetic. Brantwood Holding AG, a Swiss corporate borrower, taking a committed term facility in Swiss francs on SARON to acquire securities, with the lender as custodian in Switzerland and a portfolio denominated in US dollars under Swiss law security. Fictional party; not a real deal.
- Run id: 000000000000
- Timestamp: 1970-01-01T00:00:00+00:00
- Library hash: 7d8caf2f1de399852e2edfb99fdaf1e4d23aaa90da1ce56e9804611cb31d2a72
- Intake hash: 3876af210a5775b9e436f6a583ee987941a8f1254ffd3472a24725ae3c8a4d33
- Governing law: switzerland
- Review status: 0 reviewed / 12 draft / 12 stub

Status warning: positions tagged [DRAFT] or [STUB] have not been reviewed by a named human reviewer and must not be relied on as the lender's settled position.

## Escalations

No escalations.

Exit code: 0

## Flags

### Medium severity

- **mifid_suitability** — The facility is being used to buy securities, which is the fact pattern where a lender is most often said to have advised on, or arranged, an investment. In Switzerland that is explicit: granting loans to finance transactions with financial instruments is itself a financial service, and where investment advice or portfolio management is provided the firm must run an appropriateness or suitability review, enquire into the client's financial situation and objectives, and advise the client against an instrument it thinks unsuitable. In the United Kingdom the conduct rules require a personal recommendation to be suitable and in line with the client's risk tolerance and ability to bear losses, and the regulator's guidance tells a firm to consider the suitability of the overall transaction where an instrument is linked directly or indirectly to a loan — so the leverage and the investment are assessed together, not separately. [VERIFY] The EU-side characterisation of this lending as an ancillary service, and the EU suitability wording, were not confirmed against the directive text.
  - Who decides: compliance
  - Triggering rule: R10_purpose_acquire_securities

### Low severity

- **bank_secrecy_data** — The deal has a Swiss element (governing law or custody), so two overlapping duties apply to client information. Article 47 of the Banking Act makes it a criminal offence, punishable by up to three years' imprisonment or a monetary penalty, intentionally to disclose a secret entrusted to a person in their capacity as a body member, employee, agent or liquidator of a bank, to induce such a breach, or for a recipient to pass on or exploit a secret disclosed that way; the penalty rises to five years where the offender obtains a pecuniary advantage, negligent breach carries a fine of up to CHF 250,000, and the duty survives the end of the relationship. Separately, the Federal Act on Data Protection allows personal data to be disclosed abroad only on an adequacy finding or one of the listed safeguards, subject to exceptions including explicit consent, disclosure directly connected with performing a contract with the data subject, and disclosure necessary to establish, exercise or enforce legal rights before a court or competent foreign authority. Confirm the disclosure route before client information reaches any non-Swiss custodian, adviser, credit committee, court or purchaser, and take an express consent and waiver in the facility and security documents. A data protection consent alone does not answer the criminal duty.
  - Who decides: legal + compliance for the booking centre
  - Triggering rule: R14_swiss_booking

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

**Drafting notes**

- [R11_committed_term] Commitment also shifts the risk of the gap between signing and funding: collateral values move in between, so a facility committed on day one can be in margin call on the funding date. That is why a drawdown condition tying the advance to the loan-to-value level on the funding date matters more on a committed deal than on a demand line.

**Jurisdiction note (switzerland)**

A published Swiss factsheet offers two shapes under the same pledge: a current-account line with no fixed term and flexible drawing, and a fixed advance which may be fixed for a period of up to 24 months with a stated minimum size, with the same collateral pool also able to support derivative exposure, letters of credit and guarantees (BANK-CH-01). That matters in negotiation, because a Swiss-booked client asking for "certainty of term" can often be answered with a fixed advance drawn under an uncommitted line rather than with a committed facility, which is a much cheaper concession than the fallback tier. Separately, Swiss practitioner commentary records that a bank's contractual discretions must be exercised in good faith and not abusively (FIRM-03), so an abrupt demand made for no articulable reason is a worse place to be in Switzerland than the contract alone suggests.

Rules applied: R11_committed_term

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

- [R02_corporate_or_partnership] Constitutional documents and certified board, member or partner resolutions authorising this borrowing and this security, together with an incumbency certificate or equivalent evidence of the signatories' authority, and a certificate that no borrowing or similar limit binding on the borrower would be exceeded by this facility.

**Jurisdiction note (switzerland)**

There is nothing to file and nothing to search, so the conditions precedent are the whole of the diligence and they are documentary. Take a custodian confirmation of the holdings in the pledged account, an express waiver or subordination of the custodian's own rights over the account, and a confirmation that no earlier control arrangement exists. [VERIFY] The statutory routes to a security interest over intermediated securities, the custodian's own statutory right of retention and foreclosure, and the requirement that any authorisation of a right of use be in writing and not in general terms and conditions unless the account holder is a qualified investor, are recorded in the WP7 research file (docs/research/jurisdictions_research.md) from the Federal Intermediated Securities Act; that primary text was not opened by this drafting agent and none of those points is supported by a source in the shared pool.

Rules applied: R02_corporate_or_partnership

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

- [R13_currency_mismatch] At least one collateral currency differs from the facility currency, so the lending value moves with the exchange rate as well as with the market. Currency is one of the stated drivers of lending value in published bank terms, alongside type, quality, volatility and marketability. Apply an FX haircut to the mismatched lines and state in the clause which rate and which source the lender uses, so the borrower cannot argue about the number during a margin call.

**Jurisdiction note (switzerland)**

The published Swiss drivers of lending value are the type, currency, quality, volatility and marketability of the securities plus the diversification of the portfolio, with the ratio reviewed at regular intervals rather than fixed at drawdown (BANK-CH-01). The Swiss regulator's risk monitors name concentrated and illiquid Lombard collateral as a supervisory focus and say in terms that applied haircuts may be too low (REG-CH-01, REG-CH-02), so on a Swiss booking expect the schedule and the percentages to be challenged upward rather than downward.

Rules applied: R13_currency_mismatch

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

**Jurisdiction note (switzerland)**

The Swiss regulator's risk monitors name concentration risk in Lombard books directly: loans secured on single securities or on undiversified collateral, and the correlated version of the same problem where several banks have lent against the same collateral (REG-CH-02), with supervision focused on concentrated and more illiquid collateral (REG-CH-01). A concentrated Swiss-booked facility should therefore expect supervisory attention and the file should record why the lending value applied is adequate for the exit, not merely for the price.

Rules applied: none

### Lender discretion over valuation, lending values and eligibility [DRAFT]

- Clause id: lender_discretion_valuation
- Risk rating: high
- Category: collateral
- Document: facility_letter

**Opening: preferred**

> The Bank may at any time, in its discretion and with immediate effect, determine and re-determine the market value of any pledged asset, change the lending value percentage applying to any asset class or to any individual holding, add an asset class to or remove one from the Eligible Collateral Schedule, and determine that a pledged asset has ceased to be eligible. The Bank values the collateral at least daily using pricing sources it selects. A change takes effect when the Bank makes it, whether or not the Bank has notified the Borrower and whether or not a margin call is then outstanding; the Bank will inform the Borrower of the change by any means it considers appropriate. No change requires the consent of the Borrower or of the Pledgor.

Rationale: The ability to reprice risk the same day is the core protection behind an uncommitted facility, and it is what the Bank has instead of covenants. If the Bank has to wait, it is holding a fixed-rate view of a moving portfolio, and the loss it takes in the waiting period is exactly the loss the haircut was set to avoid. Every published bank document opened for this playbook takes this position, so it is the market opening rather than an aggressive one. It is also honest about what the facility is: the Borrower is buying liquidity against a portfolio, not buying a fixed advance rate for a term.

**Floor: acceptable**

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

**Drafting notes**

- [R13_currency_mismatch] Discretion over the rate is not unlimited. Practitioner commentary on the Swiss position is that the bank must exercise its valuation discretion in good faith and not abusively, and must be able to produce the parameters behind its calculation. Naming the rate source in the clause is the cheapest way to satisfy that.

**Jurisdiction note (switzerland)**

Swiss practice limits the discretion from the outside rather than by negotiation: it must be exercised in good faith and must not be abusive, a valid margin call must state the amount called and the deadline to post it, and the Bank must be able to produce the calculation details, the parameters used and accounting documentation for any liquidation, with a Geneva appellate decision cited for the proposition that a bank failing those prerequisites exposes itself to liability (FIRM-03). On a Swiss booking, therefore, the "show your working" ask is close to a legal duty and should be conceded early rather than traded.

Rules applied: R13_currency_mismatch

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

**Jurisdiction note (switzerland)**

Swiss law puts its requirements into the call itself rather than into the length of the cure period. A valid margin call must state the amount called and the deadline for posting it, the Bank must be able to produce the calculation details and the parameters behind the call, and a Geneva appellate decision is cited for the proposition that a bank failing those prerequisites exposes itself to liability; practice allows no more than about two days to top up (FIRM-03). Where the Bank also manages the portfolio it may owe an independent duty to notify the client of a margin deficiency before acting (FIRM-03). The structural point is the interaction with enforcement: under the Federal Intermediated Securities Act the pre-realisation notice cannot be waived by a collateral provider who is not a qualified investor, and a private individual is not one (LAW-CH-01, arts. 5(d) and 32(1)). On a Swiss booking to a private client the cure clock and the statutory notice therefore run one after the other and both have to be built into the timetable, which makes a short and precisely drafted cure period more valuable here than elsewhere.

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

- [R14_swiss_booking] Where the securities are held in Switzerland the structure follows the intermediated securities regime rather than the English analysis: the Civil Code routes intermediated securities to that regime, third-party effectiveness comes from the statutory routes including a control agreement or an agreement with the custodian, and private realisation by sale or appropriation is available but has to be documented well enough to show the best price obtainable in the circumstances. Do not port an English pledge structure across without local confirmation.

**Jurisdiction note (switzerland)**

Security over intermediated securities is governed exclusively by the Federal Intermediated Securities Act, which supplies three routes and no register: credit of the securities to the Bank's own securities account (art. 24); an irrevocable control agreement between the account holder and the Custodian under which the Custodian must carry out the Bank's instructions without any further consent or cooperation from the account holder, capable of covering specific securities, the whole account or a proportion of it (art. 25); or, where the Bank is itself the Custodian, a simple agreement with the Custodian, effective against third parties on conclusion (art. 26) (LAW-CH-01). Two traps to close in the documents. The Custodian has its own statutory right of retention and foreclosure over securities credited to the account for debts arising from the custody or from financing their acquisition (art. 21), so where a third party holds, its ranking must be dealt with expressly; and a right of use in favour of the Custodian requires the account holder's authorisation which, unless the account holder is a qualified investor, must be in writing and may NOT be included in general terms and conditions (art. 22) - directly relevant to a private individual client. Cash balances are claims against the bank, sit outside that Act, and are pledged under the Civil Code provisions on the pledge of claims, which require a written pledge agreement. Practitioner sources describe the same two working structures: a pledge with an account control agreement, or a security transfer of legal title by crediting the secured party's account (FIRM-05).

Rules applied: R14_swiss_booking

### Events of default, including insolvency, death or incapacity and material adverse change [DRAFT]

- Clause id: events_of_default
- Risk rating: high
- Category: default_enforcement
- Document: facility_letter

**Opening: preferred**

> Each of the following is an Event of Default. The Borrower fails to pay any amount when due. The Borrower or the Pledgor fails to meet a margin call, to deliver additional collateral by the deadline set under the margin maintenance and cure clause, or to respond to a call. Any representation, warranty or information given by or on behalf of a Relevant Person is incorrect, incomplete or misleading when given or when repeated. A Relevant Person is subject to, or is threatened with, insolvency, bankruptcy, moratorium, composition, business failure, material litigation or the appointment of an insolvency officer, or takes any step towards any of them. A Relevant Person who is an individual dies or loses legal capacity, or a Relevant Person which is not an individual is dissolved, ceases to exist, loses a constitutive status on which the facility was granted, or has its constitutive documents amended, restated, revoked or invalidated. Any attachment, seizure, forfeiture, freezing or restraint order, subpoena, court order or regulatory proceeding affects a Relevant Person or a substantial part of its assets. The Bank considers that the collateral has become inadequate, impaired or insecure, or that the conditions on which the Bank granted the facility have changed. An event of default, termination event or acceleration occurs under any other facility, guarantee, hedging or derivative arrangement between a Relevant Person and the Bank or any member of the Bank's group, or under any financial indebtedness of a Relevant Person owed to any other person. Performance becomes unlawful, or a change in law, regulation or regulatory requirement increases the Bank's cost or reduces its return. The security ceases to be a valid, first-ranking and perfected interest in the collateral. "Relevant Person" means the Borrower, the Pledgor, any guarantor, any other provider of collateral, and any beneficial owner or settlor of any of them. On an Event of Default all amounts owing become immediately due and payable without notice or demand, the Bank's commitment (if any) is cancelled, and the Bank may enforce under the security documents without further notice.

Rationale: This list is the Bank's exit, and on this product the exit has to be available before the loss has crystallised rather than after. That is why the insolvency and deterioration limbs reach threatened events: by the time a private client's insolvency is a matter of record, the collateral has usually already moved. The width of "Relevant Person" is deliberate and is the single most contested definition in the clause; a facility to a trust or a personal holding vehicle is in practice a facility to the individual behind it, and the events that damage the credit are events in that individual's life, not in the vehicle's. Every limb here is observed in a published or filed document from this side of the market, so it is an opening position and not an aggressive one.

**Floor: acceptable**

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

- [R11_committed_term] On a committed facility the lender cannot simply demand repayment, so the events of default are the only exit. The institutional answer is an exhaustive negotiated list of mandatory prepayment events — issuer insolvency, change of control, delisting, trading suspension, a share price trigger — in place of a general material adverse change clause, so expect the borrower to push in that direction. If a material adverse change clause stays in, be clear about what it is for: a backstop for something the specific events did not anticipate, not a substitute for a demand right. Check that the margin shortfall event stands on its own and is not qualified by a materiality test.

**Jurisdiction note (switzerland)**

Swiss law constrains what happens after the Event of Default rather than what counts as one. The Bank's discretion must be exercised in good faith and must not be abusive, a valid margin call must state the amount called and the deadline to post it, and the Bank must be able to produce the calculation details, the parameters used and accounting documentation for any liquidation, with a Geneva appellate decision cited for the proposition that a bank failing those prerequisites exposes itself to liability (FIRM-03). The practical consequence for this clause is that the evidential trail behind a default - the call, the deadline, the notification, the valuation - matters as much as the drafting does. [VERIFY] no source opened for this playbook addresses how Swiss law treats the death or incapacity of an individual pledgor, or whether the wide "Relevant Person" formulation reaching settlors and beneficial owners is used or is enforceable in Swiss practice; the Swiss material in the pool is a product factsheet, the regulator's risk monitor, an industry risk booklet and a practitioner note on margin calls.

Rules applied: R11_committed_term

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

**Jurisdiction note (switzerland)**

Switzerland supplies the self-help power by statute and then makes the notice non-negotiable for the typical private client. Under the Federal Intermediated Securities Act the secured party may realise the securities in accordance with the security agreement either by selling them and setting off the proceeds, or by appropriating securities whose value can be determined objectively; that power is not affected by the commencement of debt enforcement, reorganisation or protective proceedings against the provider, and the custodian is neither bound nor entitled to check whether the conditions for realisation are met (LAW-CH-01, art. 31). Two consequences for this clause. First, appropriation is available only where value is determined objectively (art. 31(1)(b)); [VERIFY] the working conclusion that this means listed liquid lines qualify while gated funds, structured products and unlisted holdings do not, and must be enforced by a documented sale, is drawn in the WP7 research file (docs/research/jurisdictions_research.md) as a practice inference rather than taken from the statute. Second, art. 32(1) requires notice to the collateral provider before realisation and permits waiver only by a custodian or a qualified investor; a natural person is not a qualified investor under the closed definition in art. 5(d), so on a Swiss booking to a private client the preferred tier's no-notice position is simply not available and the notice must be built into the timetable. Practice adds that the Bank owes duties of care and loyalty in liquidating and must be able to produce accounting documentation for the liquidation (FIRM-03), and that private realisation should be organised and documented to obtain the best price obtainable in the circumstances (FIRM-05).

Rules applied: none

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

**Representations/undertakings added by rules**

- [R02_corporate_or_partnership] The borrower represents that entering into the facility and granting the security is within its objects and powers, has been duly authorised, and is for its own commercial benefit.

**Jurisdiction note (switzerland)**

[VERIFY] Swiss restrictions on upstream and cross-stream security by a company for the debts of a shareholder or affiliate, and the related capital-maintenance and corporate-benefit analysis, are routinely the reason a third-party corporate pledge is restructured rather than merely repapered, but no Swiss primary text was opened for this entry or recorded in the shared source pool, and the regulatory flags file records the same gap for the financial assistance and corporate benefit flag. Treat a Swiss corporate pledgor securing another person's debt as a local counsel question before the term sheet, not as a drafting question. [VERIFY] The Swiss statutory form requirement that an authorisation of a right of use over intermediated securities be in writing and not contained in general terms and conditions, unless the account holder is a qualified investor, is recorded in the WP7 research file and is an authority-adjacent trap for an individual client; that primary text was not opened by this drafting agent.

Rules applied: R02_corporate_or_partnership

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

**Drafting notes**

- [R14_swiss_booking] There is a Swiss element to this deal. Read the Switzerland entry in the jurisdiction overlay printed with this markup before settling the security structure or the enforcement route, and confirm with Swiss counsel; the overlay is a research summary, not advice.

**Jurisdiction note (switzerland)**

Switzerland is the outlier of the three and it works in the Bank's favour. It ratified the 2006 Hague Securities Convention on 14 September 2009 and the Convention entered into force on 1 April 2017 (HCCH-SEC-CONV-2006 status table); Swiss private international law routes the question straight to it, defining intermediated securities by reference to the Convention and providing that the law applicable to them is governed by it (CH-PILA-291 arts. 108a and 108c). Under the Convention the primary rule is the law expressly agreed in the account agreement as governing the Convention issues, or another law expressly designated there, provided the relevant intermediary has a qualifying office in that State, with sequential fall-backs to the office through which the account agreement was entered into, then incorporation, then principal place of business; the issues governed include the proprietary nature and effects of the interest, perfection, priority, the intermediary's duties to competing claimants and the requirements for realisation (HCCH-SEC-CONV-2006 arts. 2, 4 and 5). For assets that are not intermediated securities, such as cash claims, a choice of law is possible but cannot be asserted against third parties, and failing a choice the pledge of a claim is governed by the law of the pledgee's habitual residence (CH-PILA-291 art. 105). The drafting instruction that follows is specific: on a Swiss-booked account, make the proprietary choice in the account agreement, not in the facility letter, and check that the custodian has a qualifying office in the chosen State. [VERIFY] what a Swiss Lombard facility letter actually says about governing law and jurisdiction is unsourced: the shared source pool contains no Swiss governing-law or jurisdiction clause at all, and nothing in this entry should be presented as observed Swiss market practice.

Rules applied: R14_swiss_booking

### No advice, non-reliance and risk acknowledgement [DRAFT]

- Clause id: no_advice_non_reliance
- Risk rating: high
- Category: parties_reps
- Document: facility_letter

**Opening: preferred**

> Each of the Borrower and the Pledgor represents and acknowledges that it enters into the facility and the security documents on the basis of its own independent analysis and judgement and of such independent advice as it has thought fit to obtain, and is not relying on any statement, representation or assurance by the Bank as to the facility, the documents, the collateral, its value, liquidity or condition, or any other matter. The Bank acts on an execution-only basis in relation to the facility. The Bank gives no investment, tax, legal, accounting or regulatory advice in connection with the facility, makes no recommendation to borrow, to borrow any particular amount, to pledge any particular asset, or to acquire, retain or dispose of any asset, and expresses no view on whether the facility or any resulting position is suitable or appropriate for the Borrower or the Pledgor. Each of the Borrower and the Pledgor further represents that it has the knowledge and experience necessary to evaluate a facility of this kind and the instruments comprising the collateral; that it has access to, and the knowledge to use, the analytical tools needed to evaluate the collateral and the effect of the facility on its portfolio as a whole; and that it has the financial resources and liquidity to bear all the risks of the facility, including the loss of the entire value of the collateral and liability for any shortfall after realisation. Each acknowledges that it has received and read the Bank's risk disclosures; that borrowing against a portfolio magnifies gains and losses and that losses may exceed the amounts deposited; that a fall in value or a change in lending values may require immediate repayment or the delivery of further collateral; that the Bank may realise collateral at a time and on terms that are not of the Borrower's choosing; and that where the facility is in a different currency from the collateral, the currency exposure is the Borrower's. These representations are repeated on each drawing and on each day on which any amount is outstanding.

Rationale: This clause is not there to win an argument after the event; it is there to record what actually happened, which is that the client decided to borrow against its own portfolio. The sophisticated-investor limbs are worth keeping in full because each does different work: the knowledge limb answers "did you understand it", the analytical-tools limb answers "did you model it against the whole portfolio", and the ability-to-bear-loss limb is the only one that answers the question a regulator actually asks, which is whether the client could survive the downside. Execution-only is stated affirmatively rather than by implication, because both of the conduct regimes in scope treat an execution-only relationship differently from an advised one, and the Bank should be saying which one it is in. Every limb here is observed in a filed or published document from this side of the market.

**Floor: acceptable**

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

**Drafting notes**

- [R10_purpose_acquire_securities] Keep the non-reliance wording and the conduct consistent. A non-reliance clause will not help much if the relationship manager has been discussing which stocks to buy, so the clause is the floor, not the whole answer.

**Jurisdiction note (switzerland)**

Switzerland resolves the threshold question against the Bank and it is not negotiable: the granting of loans to finance transactions with financial instruments is a financial service in its own right (CH-FINSA-950.1 art. 3(c)(5)), and the industry's own risk booklet puts the same point in plain terms, that conventional lending sits under general civil law but a loan taken in order to invest is a financial service to which the investor-protection provisions apply in full (IND-CH-01). An appropriateness or suitability review is required where investment advice or portfolio management is provided, the enquiry must reach the client's financial situation and investment objectives as well as knowledge and experience where advice takes the portfolio into account, pure execution or transmission is exempt subject to notifying the client, and the firm must advise the client against an instrument it thinks unsuitable (CH-FINSA-950.1 arts. 10, 12, 13 and 14). Two drafting consequences. First, the execution-only acknowledgement in the preferred tier earns its place on a Swiss booking, because the exemption is expressly conditioned on the client being told. Second, where the Bank acts as discretionary manager or adviser it may owe a duty to notify the client of a margin deficiency independently of the contract (FIRM-03), so the unacceptable tier's refusal of a contractual duty to warn must not be presented to a Swiss client as a denial that any such duty can exist.

Rules applied: R10_purpose_acquire_securities

### Interest, benchmark rate and benchmark fallback provisions [STUB]

- Clause id: interest_benchmark_fallbacks
- Category: credit

No drafted positions yet; status stub.

Rules applied: none

### Prepayment and breakage costs [STUB]

- Clause id: prepayment_breakage
- Category: credit

No drafted positions yet; status stub.

**Drafting notes**

- [R11_committed_term] A committed facility usually carries a fixed funding cost, so breakage and prepayment interact with the events of default: an acceleration triggers the same breakage a voluntary prepayment would. Make sure the two clauses use the same definition and do not double count.

Rules applied: R11_committed_term

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

**Representations/undertakings added by rules**

- [R10_purpose_acquire_securities] The borrower represents that the facility will be applied only to the permitted purpose stated in the facility letter, and undertakes to notify the lender before applying any part of it to a different purpose.

**Drafting notes**

- [R10_purpose_acquire_securities] Borrowing to buy securities that are then pledged back gears the same risk twice: a fall in the market cuts the collateral and the borrower's ability to repay at the same time. Keep the purpose restriction tight enough that the lender knows what it is funding. Where the collateral includes US margin stock, purpose credit also carries its own collateralisation requirement, so the purpose statement has a regulatory consequence as well as a credit one.

Rules applied: R10_purpose_acquire_securities

### Transfer and assignment [STUB]

- Clause id: transfer_assignment
- Category: boilerplate

No drafted positions yet; status stub.

Rules applied: none

### Confidentiality, bank secrecy and permitted disclosure [STUB]

- Clause id: confidentiality_bank_secrecy
- Category: boilerplate

No drafted positions yet; status stub.

**Drafting notes**

- [R14_swiss_booking] Settle what the carve-outs need to cover before they are agreed: disclosure to group entities, to a custodian, to professional advisers, on enforcement, and in response to a regulator or a court outside Switzerland. The data protection exceptions do cover disclosure needed to perform the contract and to enforce legal rights abroad, but they do not displace the criminal duty, so take the client's express consent and waiver as well. A carve-out that is too narrow stops the lender doing ordinary things; one that is too wide may not be effective.

Rules applied: R14_swiss_booking

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

**Drafting notes**

- [R13_currency_mismatch] Decide whether the borrower or the lender carries the conversion risk on enforcement, and say so. [VERIFY] No opened source allocates that risk either way, so the lender-side position that the shortfall on conversion is the borrower's is a drafting preference rather than a market standard.

Rules applied: R13_currency_mismatch

## Jurisdiction overlay — Switzerland [DRAFT]

- Creation: Security over intermediated securities, meaning book-entry securities credited to a securities account with a custodian such as a bank, a securities firm, a fund management company for unit accounts, a central securities depository or the central bank, is governed exclusively by the Federal Intermediated Securities Act (FISA, also known as BEG, SR 957.1); the Civil Code says so expressly in Art. 901(3). FISA gives three ways to make the disposal effective against third parties: credit of the securities to the collateral taker's own securities account on the account holder's instruction under Art. 24, which transfers full legal rights where the disposition is framed that way; an irrevocable control agreement between the account holder and the custodian under Art. 25, by which the custodian must carry out the acquirer's instructions without any further consent or cooperation from the account holder, and which may cover specific securities, the whole account, or a proportion of the account up to a stated value; and, where the collateral taker is itself the custodian, a simple agreement with the custodian under Art. 26, effective against third parties on conclusion. Cash balances are claims against the bank and sit outside FISA: they are pledged under Civil Code Arts 899 and 900, which require a written pledge agreement, with the bank's own general terms lien and set-off usually doing the heavy lifting. Lender-side, if the bank is the custodian the Art. 26 route is the cleanest and fastest; if it is not, an Art. 25 control agreement is a condition precedent and not a post-closing item.
- Registration / filing: There is no registration, filing or public register for a pledge or a security transfer over intermediated securities or over cash claims in Switzerland. Third-party effectiveness comes from the FISA act of disposal itself, whether that is the credit under Art. 24, the control agreement under Art. 25 or the Art. 26 agreement with the custodian. Priority is determined by the time of the disposition under Art. 30(1), with a specific rule in Art. 30(2) subordinating a custodian's own earlier rights where it enters into an Art. 25 control agreement without expressly notifying the acquirer of them. That makes Swiss collateral quick to take, but it also means there is nothing to search, so the diligence is documentary rather than register-based. Obtain a custodian confirmation of the account holdings, an express waiver or subordination of the custodian's statutory right of retention and foreclosure under Art. 21 and of any general terms lien and set-off, and a confirmation that no earlier control agreement exists.
- Perfection depends on: Control, exercised through the custodian, is what does the work. There is nothing to file and nothing to notify beyond the custodian: either the securities are credited to the lender's account under Art. 24, or the custodian is irrevocably bound to follow the lender's instructions without the client's further consent under Art. 25, or the lender is itself the custodian and the agreement alone suffices under Art. 26. Two traps have to be closed in the documents. First, the custodian has its own statutory right of retention and foreclosure over securities credited to the account for debts arising from the custody or the financing of their acquisition under Art. 21, so where a third-party custodian holds, its ranking must be dealt with expressly. Second, a right of use in favour of the custodian requires the account holder's authorisation and, unless the account holder is a qualified investor, that authorisation must be in writing and may not be included in general terms and conditions under Art. 22, which matters directly for a private individual client.
- Enforcement route: FISA Art. 31 gives the secured party a statutory private realisation power: it may realise the intermediated securities in accordance with the terms of the security agreement either by selling them and offsetting the proceeds against the secured debt, or by appropriating securities whose value can be determined objectively and offsetting that value. Critically, Art. 31(2) provides that the power is not affected by the commencement of debt enforcement, reorganisation or protective proceedings against the collateral provider, and Art. 31(3) provides that the custodian is neither bound nor entitled to check whether the realisation conditions are met, with Art. 31(4) preserving the secured party's liability where they were not. Art. 32(1) requires the secured party to give notice to the provider before realisation, and that notice may be waived only by a provider that is a custodian or a qualified investor; Art. 32(2) requires an account and remittance of surplus proceeds. This is a real departure from the ordinary Swiss default, under which a pledge-secured claim is enforced through debt enforcement proceedings to realise the pledge (DEBA Art. 41 and Arts 151-158), private enforcement generally stops once bankruptcy is declared because pledged assets fall into the estate (DEBA Art. 198, with pledge-secured claims paid in advance from the proceeds under Art. 219(1)), and the Civil Code invalidates any agreement that a pledged chattel becomes the pledgee's property on default (Art. 894, the forfeiture prohibition). Note also the extraterritorial reach: FISA Art. 2(1bis) applies Art. 31(2) to intermediated securities held with a custodian in Switzerland or abroad, even where that custody is subject to foreign law.
- Financial collateral regime: Switzerland has no equivalent of Directive 2002/47/EC and no instrument called a financial collateral regime; FISA Chapters 5 and 6 do the same work for intermediated securities. The scope difference that matters most in private wealth is that natural persons ARE covered: FISA contains no requirement that either party be a non-natural person, so a private individual can be the collateral provider and the Art. 31 realisation power, including the insolvency override in Art. 31(2), still applies. The trade-off runs the other way on process, because an individual is not a qualified investor: Art. 5(d) limits that status to a custodian, a prudentially supervised insurance company, a public-law entity, a pension fund, or a company with professional treasury management. The consequence is that the pre-realisation notice in Art. 32(1) cannot be waived for a private client, and the Art. 22 right-of-use authorisation cannot be buried in general terms and conditions. Stated in lender terms, the benefits of the regime are self-help sale or appropriation without court involvement, survival of that power through the provider's insolvency or moratorium, and no obligation on the custodian to second-guess the enforcement.
- Governing law of intermediated securities: Switzerland is the outlier of the three jurisdictions and the difference works in the lender's favour. It ratified the 2006 Hague Securities Convention on 14 September 2009 and the Convention entered into force on 1 April 2017, and Swiss private international law channels the question straight to it: PILA Art. 108a defines intermediated securities by reference to the Convention and Art. 108c states that the law applicable to intermediated securities is governed by the Convention. Under the Convention the primary rule in Art. 4(1) is the law expressly agreed in the account agreement as governing the Convention issues, or another law expressly designated there, provided the relevant intermediary has a qualifying office in that State; Art. 5 supplies sequential fall-backs, being the office through which the account agreement was entered into, then incorporation or organisation, then principal place of business; and Art. 2 lists the issues governed, being the proprietary nature and effects, perfection, priority, the intermediary's duties to competing claimants, realisation requirements, and extension to distributions and proceeds. For claims and rights that are not intermediated securities, cash claims for example, PILA Art. 105 applies: the parties may choose the law governing the pledge but that choice cannot be asserted against third parties, and failing a choice the pledge of claims is governed by the law of the pledgee's habitual residence, with a law other than the one governing the pledged right not assertable against the debtor. So for a Swiss-booked account the proprietary law can in principle be fixed by agreement, which neither the English nor the Luxembourg account-location rule allows; the qualifying-office condition in Art. 4(1) is a real constraint and the point has not been seen applied to a facility of this kind, so treat the operational use of it as a matter for local counsel.
- Practical notes: (1) If the bank is the Swiss custodian, use the Art. 26 route and make sure the security agreement and the custody terms agree with each other; if a third-party custodian holds, an executed Art. 25 control agreement plus a waiver or subordination of the custodian's Art. 21 rights is a condition precedent. (2) Build the Art. 32(1) notice into the enforcement clause and into the operational runbook, because for a private individual pledgor it cannot be waived, so a facility that assumes instant liquidation without notice is wrong for that client type; define the notice period, the delivery method and the trigger, and keep evidence. (3) Rely on Art. 31(2) as the answer to the debt enforcement problem and say so in the enforcement clause, because without FISA a pledge would otherwise be dragged into pledge-realisation proceedings and, on bankruptcy, the pledged assets fall into the estate under DEBA Art. 198 with the pledgee taking priority in the proceeds under Art. 219(1). (4) Appropriation is available only where the value can be determined objectively under Art. 31(1)(b), so listed liquid securities yes, and gated funds, structured products and unlisted positions probably not, with those enforced by sale under a documented process; the translation of that statutory phrase into an asset-class test is judgement rather than law. (5) For a third-party pledgor, the Art. 32 notice goes to the provider of the security interest and not to the borrower, so identify the notice recipient correctly. (6) Bank secrecy under Banking Act Art. 47 and the cross-border data transfer restrictions in FADP Arts 16-17 are live on every Swiss booking; see the bank secrecy and data protection flag. (7) FinSA Art. 3(c)(5) makes the granting of loans to finance transactions with financial instruments a financial service in its own right, which pulls a purpose-to-invest facility into the FinSA conduct perimeter.

## Not automated on this deal

- Choosing the booking centre for a new relationship, which is a commercial, tax and regulatory decision as well as a legal one.
- Every cross-border perfection and enforceability conclusion. The playbook cites the rule; local counsel in the account's jurisdiction confirms it, and that confirmation is a condition precedent, not a drafting note.
- Every suitability and appropriateness conclusion. The tool records the purpose, raises the flag and tightens the floor; a person in compliance decides whether the leveraged position is suitable.
- Know-your-client, sanctions and source-of-funds outcomes, including any decision to decline or to exit.
- Reading the trust instrument. No rule in this library can tell anyone whether a power to borrow or to charge exists; a lawyer reads the deed and every deed of appointment, retirement and variation behind it.
- Setting the notice period and the term length. Only one opened source states either figure, and both are the institution's risk appetite.
- Setting the notice period itself. Only one opened source concedes one (15 days) and the number here is the institution's risk appetite.
- Setting the numeric grid itself. The demonstrator carries X placeholders because no public source opened for this playbook publishes one.
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
- Whether a specific holding is admitted to the Eligible Collateral Schedule, and at what lending value percentage.
- Whether an asset that becomes illiquid or restricted after drawdown is re-rated immediately or on notice.
- Whether an asymmetric jurisdiction clause will be given effect in the forum where the Bank would actually use it. [VERIFY] not sourced for this playbook.
- Whether an individual had capacity at signing, and what the Bank does on incapacity short of death. The intake records no fact that answers either, and the treatment of incapacity is an identified gap in this library.
- Whether an individual has lost legal capacity, and whether an attorney, deputy or other representative can give instructions that bind the Borrower or the Pledgor. [VERIFY] no mental-capacity source was opened for this playbook.
- Whether independent legal advice was genuinely given, genuinely independent and genuinely understood.
- Whether repeated forbearance has made an uncommitted line committed in substance. That is a course-of-dealing judgement, and no rule in this library can make it.
- Whether the Borrower is a consumer, and therefore whether a declaration and statement had to precede signing.
- Whether the Borrower or the Pledgor is capable of claiming immunity at all, which turns on its constitution and on the law of the place of enforcement.
- Whether the relationship is in fact execution-only, advisory or discretionary on the pledged portfolio. The clause must match the answer, and the answer is a fact about what people did, not a drafting choice.
- Whether to accept a client's existing custody relationship at all, which is a relationship decision as much as a credit one.
- Whether to accept a foreign-law legal opinion in the form offered, and what it must cover.
- Whether to call a default at all, as against forbearing while the relationship is discussed. Forbearance on a live margin call and waiver of an event of default are both human decisions.
- Whether to commence proceedings in a second jurisdiction, and the disclosure of client information that doing so entails in a bank-secrecy jurisdiction.
- Whether to decline the facility outright because the leveraged position is unsuitable, notwithstanding that the collateral supports it.
- Whether to disclose the full haircut matrix to a counterparty who asks for it during negotiation.
- Whether to enforce against a deceased individual's collateral before the estate is administered, which is a reputational and conduct decision as much as a legal one.
- Whether to exercise the demand right on a live facility, as against forbearing while the relationship is discussed. The clause fixes who decides; it does not decide.
- Whether to exercise the discretion at all on a live position, as against forbearing while the relationship is discussed.
- Whether to offer committed term at all for relationship reasons, and what that costs in lending value, price and commitment fee.
- Whether to register a charge protectively for a corporate chargor where reliance on the financial collateral regime is doubtful.
- Whether to take a concentrated but high-quality single holding at a reduced lending value rather than excluding it.
- Whether to waive a condition and advance anyway, against what undertaking and for how long.
- Which items belong in Part 1 and which in Part 2 of the fallback schedule on the particular facts. The test is in the rationale; applying it is a judgement.

---

This markup was produced by the SBL Negotiation Playbook Demonstrator, a demonstration tool built from public sources and run against synthetic deals. It is not legal advice. It is not the work product of any institution, and it has not been validated against any institution's credit policy, risk appetite, house style or local counsel advice. Every position is drafted from the lender's side only. The status labels mean exactly what they say: [STUB] means no position has been drafted; [DRAFT] means an entry written from public sources that no named human reviewer has checked; [REVIEWED] means a named reviewer recorded in the library has checked it. Text carrying a [VERIFY] prefix has not been confirmed against a primary source the writer opened. Any concession below a clause's floor, and every item under "Not automated on this deal", is a human decision that this tool does not make.
