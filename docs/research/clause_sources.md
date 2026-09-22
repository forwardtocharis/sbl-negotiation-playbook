# WP3 shared source pool — core twelve clauses

Prepared for WP3 (core twelve clause entries), build plan §3. All entries below were opened
and read by the sourcing agent on **2026-09-21**. Nothing here is drafting language: every
observation is a paraphrase of the *structure* of a position, in the sourcing agent's own words.

Rules applied to this file:

- **No party names from filed agreements.** Filed documents are described by what they are plus
  the EDGAR accession number. Accession numbers and URLs are recorded so anything can be re-opened.
- **No bank branding beyond identifying a public document as a source.** Bank-published documents
  are described generically ("published Lombard loan agreement of a Luxembourg bank") with the URL.
  No bank wording is reproduced.
- **Reliability grades** follow build plan §2.1: `A` primary law / regulator, `B` filed agreement /
  bank terms, `C` commentary.
- `verified: true` means the sourcing agent opened the document itself and read the passage relied
  on. It does **not** mean a human has reviewed the proposition. Every clause entry that uses these
  sources still carries `status: draft` until Stuart reviews.

---

## Source pool

| ref | type | url | retrieved | reliability | verified | note |
|---|---|---|---|---|---|---|
| `EDGAR-ML-01` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1370880/000119312520323316/d161224dex99e.htm | 2026-09-21 | B | true | Full margin loan agreement over listed shares filed as an exhibit to a Schedule 13D, EDGAR accession 0001193125-20-323316. Complete LTV / collateral-shortfall / cure architecture, but the numeric levels sit in a confidential "Additional Terms Letter". |
| `EDGAR-ML-02` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1166388/000119312520167769/d942873dex996.htm | 2026-09-21 | B | true | Series A margin loan agreement over listed shares, EDGAR accession 0001193125-20-167769. Adds a capital-call cure extension mechanic on top of the standard cure. Numeric levels again in a side letter. |
| `EDGAR-ML-03` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1333493/000119312521187800/d467983dex3.htm | 2026-09-21 | B | true | Margin loan agreement over listed shares, EDGAR accession 0001193125-21-187800. Explicit **2 business day** cure (3 with a certificate), full CP schedule, full EoD list, New York law. |
| `EDGAR-ML-04` | filed_agreement | https://www.sec.gov/Archives/edgar/data/2068577/000149315225028763/ex7.htm | 2026-09-21 | B | true | Margin loan agreement over listed shares, EDGAR accession 0001493152-25-028763 (filed Dec 2025 — the most recent in this pool). Three named LTV levels (Margin Call / Reset / Release), all redacted; cure time and shortfall-stacking rule are in the clear. |
| `EDGAR-PL-01` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1723128/000089843224000401/exh99-5.htm | 2026-09-21 | B | true | Pledge and security agreement supporting a margin loan, EDGAR accession 0000898432-24-000401. Security grant, pledgor covenants, lender beneficial-ownership cap ("Ownership and Bust-Up"), power of attorney, remedies. |
| `EDGAR-PL-02` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1658566/000110465916164555/a16-23883_1ex99d7.htm | 2026-09-21 | B | true | Pledge and security agreement supporting a margin loan, EDGAR accession 0001104659-16-164555. Very full control/custody build-out and the most detailed pre-agreed commercial-reasonableness carve-outs in this pool. |
| `EDGAR-PL-03` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1120193/000114036124012544/ef20022496_ex7-15.htm | 2026-09-21 | B | true | Pledge and security agreement plus a secured custodian securities account control agreement and a deposit account control agreement, EDGAR accession 0001140361-24-012544. Third-party custodian / depositary agent structure. |
| `EDGAR-PB-01` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1293153/000095012308001840/y49893exv99w7w05.htm | 2026-09-21 | B | true | Composite exhibit, EDGAR accession 0000950123-08-001840, containing three separate private-bank securities-lending documents given by **individual** pledgors and a trust pledgor. Sub-parts cited below as `-A` (guarantee and pledge agreement), `-B` (pledge plus pledge addendum for margin loans), `-C` (security agreement). This is the single richest source in the pool for the retail/private-wealth position, and the only filed source with unredacted lending values, trigger levels and cure days. |
| `EDGAR-EN-01` | filed_agreement | https://www.sec.gov/Archives/edgar/data/1530238/000110465919067794/tv533539_sc13da.htm | 2026-09-21 | B | true | Schedule 13D/A, EDGAR accession 0001104659-19-067794, annexing an English-law amendment notice under a security deed over listed shares held by an SPV. Only English-law-governed securities security document opened in this pool; expressly plugs into the Financial Collateral Arrangements (No. 2) Regulations 2003. |
| `BANK-LU-01` | bank_terms | https://links.imagerelay.com/cdn/2958/ql/lombard-loan-contract-sqbe-en-01072023 | 2026-09-21 | B | true | Published Lombard loan agreement template of a Luxembourg bank (CSSF-supervised). Covers, in one seven-page document, almost every one of the core twelve clauses from the lender side. |
| `BANK-LU-02` | bank_terms | https://www.delen.bank/hubfs/dot-bank/assets/general_banking_conditions_2025.pdf?hsLang=en-lu | 2026-09-21 | B | true | Published 2025 general banking conditions of a Luxembourg private bank. Contains the only explicit **two-tier numeric** cover trigger found in bank terms (130% top-up / 120% immediate realisation). |
| `BANK-LU-03` | bank_terms | https://assetsgarantibbva.com/assets/pdf/en/other/Luxembourg_Branch.pdf | 2026-09-21 | B | true | Published general terms and conditions of a bank's Luxembourg branch. Automatic (ipso jure) general pledge over everything entrusted to the bank, enforcement routed through the Law of 5 August 2005, right of retention. |
| `BANK-CH-01` | bank_terms | https://www.ubs.com/content/dam/assets/microsites/credit-suisse/static/doc/lombardkredit-factsheet-en.pdf | 2026-09-21 | B | true | Published Lombard loan product factsheet of a Swiss bank. Names the lending-value drivers, the two facility forms (current account / fixed advance) and the top-up-or-liquidate consequence. Marketing material, and says so. |
| `BANK-US-01` | bank_terms | https://www.privatebank.citibank.com/we-offer/margin-lending | 2026-09-21 | B | true | Published securities-backed / margin lending disclosures of a global private bank. The clearest published statement of the demand-facility + no-notice + no-extension position. |
| `IND-CH-01` | bank_terms | https://www.swissbanking.ch/_Resources/Persistent/e/1/8/d/e18dc86d8033b556db0c7db772e9b025042db1d5/SBA_Risks_Involved_in_Trading_Financial_Instruments_2023_EN.pdf | 2026-09-21 | B | true | Swiss banking industry association risk-disclosure booklet, 2023 English edition. Treats a Lombard loan taken to invest as a financial service inside the Swiss conduct regime and sets out the credit-financed-investment risk block. |
| `REG-CH-01` | regulator | https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/finma-publikationen/risikomonitor/20241118-finma-risikomonitor-2024.pdf | 2026-09-21 | A | true | Swiss regulator risk monitor 2024. Lombard portfolios as a material share of large international banks' assets; supervisory focus on concentrated and illiquid collateral; explicit concern that applied haircuts may be too low. |
| `REG-CH-02` | regulator | https://www.finma.ch/en/~/media/finma/dokumente/dokumentencenter/myfinma/finma-publikationen/risikomonitor/20251117-finma-risikomonitor-2025.pdf?sc_lang=en | 2026-09-21 | A | true | Swiss regulator risk monitor 2025. Repeats and sharpens the 2024 position; names single-stock lending and undiversified collateral, and correlated exposure across banks lending against the same collateral. |
| `LAW-EW-01` | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/regulation/3 | 2026-09-21 | A | true | Financial Collateral Arrangements (No. 2) Regulations 2003, reg. 3 (definitions). Read for: the "possession or control" requirement, the definition of financial collateral, and the requirement that **both** parties be non-natural persons. |
| `LAW-UK-02` | primary_law | https://www.legislation.gov.uk/uksi/2001/544/article/60H | 2026-09-21 | A | true | Regulated Activities Order 2001, art. 60H (exempt agreements — high net worth borrowers). Read for the declaration/statement architecture and the £60,260 credit threshold. |
| `LAW-LU-01` | primary_law | https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf | 2026-09-21 | A | true | Luxembourg Law of 5 August 2005 on financial collateral arrangements, consolidated text published by the regulator (updated 15 July 2024). Read arts. 3–5, 11, 12, 13, 13-1, 18–20, 22. |
| `FIRM-01` | law_firm_briefing | https://www.stblaw.com/docs/default-source/related-link-pdfs/global-legal-insights-fund-finance-2022_backleverage-financings--insights-into-the-margin-loan.pdf?sfvrsn=b1f56e21_2 | 2026-09-21 | C | true | US law-firm chapter on margin loan / backleverage financings in a practitioner guide. The best single explanation of the Trigger-LTV / Reset-LTV architecture, cure norms, mandatory prepayment events and Regulation U in the pool. |
| `FIRM-02` | law_firm_briefing | https://www.mayerbrown.com/en/insights/publications/2022/12/security-enforcement-english-high-court-guidance-on-the-appropriation-of-collateral-under-the-financial-collateral-regulations | 2026-09-21 | C | true | Law-firm note on *ABT Auto Investments Ltd v Aapico Investment Pte Ltd* [2022] EWHC 2839 (Comm) — the English authority on valuation when appropriating financial collateral. |
| `FIRM-03` | law_firm_briefing | https://www.mondaq.com/commoditiesderivativesstock-exchanges/985220/margin-calls-how-can-investors-protect-their-position | 2026-09-21 | C | true | Swiss practitioner note on margin calls under Swiss law and standard Lombard pledge terms: what a valid call must contain, typical top-up windows, and the limits Swiss courts place on contractual no-notice liquidation rights. |

**Pool size: 23 sources** — 5 grade A, 14 grade B, 3 grade C, plus `EDGAR-EN-01` counted in B. See the
hand-off note for the grade breakdown and coverage gaps.

---

## Per-clause map

### facility_type

Applies: `BANK-LU-01`, `BANK-CH-01`, `BANK-US-01`, `EDGAR-ML-03`, `EDGAR-ML-04`, `EDGAR-PB-01`, `FIRM-01`

- `BANK-LU-01` — The facility is an authorisation to run a debit balance on a named account up to a
  Limit, granted at the bank's sole discretion, for an indefinite period. Either side may walk away
  on 90 days' notice, but the bank may terminate with immediate effect on any listed event of
  default. There is no commitment language anywhere: the bank sets the Limit and may cut it.
- `BANK-CH-01` — Offers a choice of two shapes under one pledge: a current-account line with no
  fixed term and flexible drawing, or a fixed advance which can be fixed for up to 24 months with a
  stated minimum size. The same collateral pool supports both, and the same limit can also back
  derivative exposure, letters of credit and guarantees.
- `BANK-US-01` — States the demand position in the plainest terms found anywhere in the pool: the
  bank may demand repayment of a demand facility at any time, for any reason or no reason.
- `EDGAR-ML-03` / `EDGAR-ML-04` — The institutional counter-model. These are **term** facilities
  with a maturity date, committed advances on named funding dates, make-whole/breakage on early
  repayment, and no demand feature. Everything that a demand right would otherwise do is done by an
  exhaustive, negotiated list of mandatory prepayment events and events of default.
- `EDGAR-PB-01-A` — The private-bank hybrid: a continuing guarantee and pledge supporting whatever
  credit arrangements exist from time to time, revocable by the guarantor only on seven days'
  written notice, and with revocation not touching anything already incurred or already committed.
- `FIRM-01` — Notes that committed margin financing is possible but that the value of the collateral
  moves between signing and funding, so a facility committed on day one can be in margin call on the
  funding date; this is why refinancing rather than acquisition funding is the more common use.

### conditions_precedent

Applies: `EDGAR-ML-03`, `EDGAR-ML-04`, `EDGAR-PL-02`, `EDGAR-PL-03`, `BANK-LU-01`, `LAW-UK-02`, `FIRM-01`

- `EDGAR-ML-03` — Splits CPs in two. Section 4.1 holds the *state of the world* conditions: reps
  true in all material respects at signing, closing and each funding date; no default, event of
  default, mandatory prepayment event or adjustment event continuing; the shares actually credited
  to the collateral accounts; and, immediately after drawing, the LTV ratio not above the initial
  LTV level. Section 4.2 holds the *paper*: legal opinion, constitutional documents, good-standing
  certificate, board resolutions, incumbency, and a financial officer's certificate confirming
  ownership of the shares and that no borrowing limit binding the borrower is exceeded. Acceptance
  of the proceeds is deemed to re-make the section 4.1 conditions as representations.
- `EDGAR-ML-03` — Also makes collateral *quality* a CP in its own right: the lenders must be
  reasonably satisfied that the pledged shares carry no transfer restrictions beyond those
  disclosed, no restrictive conditions, and settle through the ordinary book-entry system.
  Separate reps confirm the pledge is a bona fide pledge and that the holding period has run.
- `EDGAR-PL-02` — Perfection is built as a CP chain, not an undertaking: custody agreement
  acceptable to the secured party, collateral cash and share sub-accounts opened, a control
  agreement with the custodian, a counsel opinion, a recent lien search in the pledgor's UCC
  "location" showing no liens, and filed financing statements — only then are shares re-registered
  into the custodian's name.
- `EDGAR-PL-03` — Adds the third-party-custodian variant: a secured custodian securities account
  control agreement plus a deposit account control agreement, both with a depositary agent that is
  not the lender, executed before perfection is asserted.
- `BANK-LU-01` — The retail analogue reduces the whole CP schedule to one condition: the agreement
  does not come into force and no obligation arises until the bank's credit risk assessment of the
  client has been completed to the bank's satisfaction, and the bank may withhold or terminate if
  it is not.
- `LAW-UK-02` — Supplies a CP that the filed agreements never need: where the borrower is an
  individual, the high-net-worth exemption depends on a borrower declaration giving up regulated-
  agreement protections plus a statement of income or assets meeting the regulator's rules,
  delivered *before* the agreement is entered into. Getting the sequence wrong is not curable later.

### eligible_collateral_lending_values

Applies: `BANK-LU-01`, `BANK-CH-01`, `BANK-US-01`, `EDGAR-PB-01`, `FIRM-01`, `REG-CH-01`, `REG-CH-02`, `LAW-LU-01`

- `BANK-LU-01` — Defines the lending value as market value of eligible pledged assets minus the
  applicable haircut, calculated by the bank — but adds one important qualifier: calculated by the
  bank **acting in good faith**. Separately, the Limit is set on named criteria: a percentage of
  collateral value, the nature of the assets, their risk profile (volatility and liquidity are
  called out), and the level of diversification across asset types.
- `BANK-CH-01` — Gives the fullest published list of lending-value drivers: type, currency,
  quality, volatility and marketability of the securities, plus the diversification of the
  portfolio; and says the ratio is reviewed at regular intervals rather than fixed at drawdown.
- `EDGAR-PB-01-A` — Structures it as a covenant rather than a ratio: the pledgor must at all times
  maintain collateral, in which the bank holds a first-priority perfected security interest, with a
  lending value of not less than 100% of everything outstanding, including amounts not yet matured
  and contingent amounts. Lending value is a bank-set percentage of a bank-determined fair market
  value, per class of collateral, floored by any regulatory maximum margin percentage.
- `EDGAR-PB-01-B` — The only opened filed document with a hard number: a lending value percentage
  of 50% of the margin collateral, expressly reducible or increasable at the bank's sole and
  absolute discretion. What counts as acceptable margin collateral is also at the bank's sole
  discretion, and the bank reserves the right to change the accepted types.
- `FIRM-01` — Explains that valuation method follows collateral type: exchange-listed common stock
  marked to market (often daily) sits at the reliable end; private-company collateral is instead
  valued off the value the sponsor vehicle reports to its own investors and creditors, with heavily
  negotiated appraisal and sometimes dispute rights. Also records the Regulation U constraint in the
  US: purpose credit secured by margin stock must be fully collateralised with a 50% haircut on the
  margin stock, so $100m of purpose credit needs at least $200m of margin stock.
- `REG-CH-01` / `REG-CH-02` — The regulator's side of the same question: pledged securities can
  fall by more than the haircut applied to them, and the supervisor's stated concern is that
  haircuts may be set too low. This is the source to cite for why the lender's opening position on
  lending values should not be negotiable downward without credit input.
- `LAW-LU-01` — Art. 11(1)(e)–(f) shows what "eligible" looks like from the exit side: listed
  instruments can be appropriated at market price; fund units at the last published net asset value
  provided that publication is not more than a year old, or redeemed at the fund's redemption
  price. Collateral that cannot be priced by one of those routes has no fast exit.

### concentration_limits

Applies: `REG-CH-02`, `REG-CH-01`, `BANK-LU-01`, `BANK-CH-01`, `FIRM-01`, `EDGAR-ML-03`, `EDGAR-PL-01`, `EDGAR-PL-02`, `EDGAR-ML-04`

- `REG-CH-02` — Names the risk directly: concentration risk where loans are secured on single
  securities (single-stock lending) or on undiversified collateral, and the correlated version of
  the same problem where many banks have lent against the same collateral. This is the cleanest
  regulator-level authority for a concentration clause existing at all.
- `REG-CH-01` — Records that supervision of the Lombard book is focused specifically on risks
  emerging from concentrated or more illiquid collateral.
- `BANK-LU-01` — Handles concentration without a numeric cap, in three ways at once: diversification
  is an input to the Limit; the bank may charge differentiated commissions or fees where, in its
  opinion, the portfolio is not sufficiently diversified; and insufficient diversification is itself
  a free-standing ground for unilateral liquidation without prior notice.
- `BANK-CH-01` — Same approach, softer: diversification is one of the stated inputs into the
  loan-to-value ratio applied to the portfolio.
- `FIRM-01` — Shows the institutional single-name equivalent: a "Future Financing" or "Restricted
  Transactions" covenant that stops affiliates of the borrower pledging securities of the *same
  class* to secure other financings, precisely to stop several margin loans stacking on one stock
  and creating an overhang on exit.
- `EDGAR-ML-03` — Carries that covenant as a representation that no loan party or affiliate is
  party to a restricted transaction.
- `EDGAR-PL-01` / `EDGAR-PL-02` — Show concentration cutting the other way: an "Ownership and
  Bust-Up" section caps the *lender's* deemed beneficial ownership of the issuer, aggregated across
  the lender, its affiliates and any group it is deemed part of, and conditions enforcement sales on
  staying inside that cap. Concentration is therefore a two-sided constraint, not just a borrower
  limit.
- `EDGAR-ML-04` — Uses a 10% beneficial-ownership threshold and a 50% change-of-control threshold
  as structural triggers, and attaches an underwriter lock-up agreement to the pledged stock —
  a worked example of restricted-securities concentration in a recent transaction.

### lender_discretion_valuation

Applies: `BANK-LU-01`, `BANK-US-01`, `EDGAR-PB-01`, `FIRM-03`, `EDGAR-ML-03`, `EDGAR-EN-01`, `FIRM-01`, `FIRM-02`

- `BANK-LU-01` — The high-water mark of lender discretion in the pool. The bank may reduce the
  Limit at any time, slightly or substantially, with no obligation to give notice; it routinely
  re-evaluates the haircut on each pledged asset and may amend haircuts at any time without notice,
  which may reduce or entirely withdraw the Limit; and if it considers the conditions on which the
  Limit was granted have changed, it may reduce or withdraw with immediate effect and without
  notice, informing the client afterwards by whatever channel it thinks appropriate. The single
  counterweight is that the lending value itself is calculated "acting in good faith".
- `BANK-US-01` — Publishes the same position for a demand facility: collateral is marked to market
  daily, margin requirements may be increased at any time, and the firm is not required to give
  advance written notice.
- `EDGAR-PB-01-A` — Same structure in a filed document: lending value is a bank percentage of a
  bank-determined fair market value, and unless specifically agreed in writing the bank may change
  or eliminate the percentage for any class of collateral at any time without prior notice.
- `EDGAR-PB-01-B` — The only version that puts a notice period on the discretion: the margin
  requirement may be modified at the bank's sole and absolute discretion on **15 days' prior written
  notice**, but the notice period collapses to immediate effect if the change is required by
  applicable law or if the value of the collateral is rapidly diminishing. This is the most
  drafter-useful formulation in the pool because it concedes a period and then carves it out.
- `FIRM-03` — The Swiss judicial limit on all of the above: the discretion must be exercised in good
  faith and must not be abusive; a valid margin call must state the amount of collateral called and
  set the deadline to post it; the bank must be able to produce the calculation details and the
  relevant parameters, and accounting documentation for any liquidation. A Geneva appellate decision
  is cited for the proposition that a bank which fails those prerequisites exposes itself to
  liability.
- `EDGAR-ML-03` — The negotiated institutional middle. The calculation agent's determinations are
  repeatedly qualified: "reasonably determined", and in the market-disruption definition, "acting in
  good faith and in a commercially reasonable manner". Discretion is preserved but is expressly
  standard-bound rather than absolute.
- `EDGAR-EN-01` — English-law equivalent: the secured party's determination that shares are "excess
  financial collateral" for FCAR purposes must be made in good faith and in a commercially
  reasonable manner before collateral is released.
- `FIRM-01` — Notes that where no commercially reasonable adjustment to a facility is possible
  following a facility adjustment event, the consequence is a full mandatory prepayment and
  termination — i.e. discretion has a defined terminal outcome rather than an open-ended one.
- `FIRM-02` — The English valuation standard when discretion is exercised on enforcement: the
  manner of valuation must be commercially reasonable judged objectively; the *result* need not be
  reasonable; the collateral-taker remains responsible even when it uses a third-party valuer; and
  non-compliance does not unwind the appropriation but lets the court substitute a compliant
  valuation. Useful for explaining to a counterparty why an objective-standard concession is
  survivable.

### margin_maintenance_cure

Applies: `EDGAR-PB-01`, `EDGAR-ML-03`, `EDGAR-ML-04`, `EDGAR-ML-01`, `EDGAR-ML-02`, `BANK-LU-01`, `BANK-LU-02`, `BANK-US-01`, `BANK-CH-01`, `FIRM-01`, `FIRM-03`, `IND-CH-01`

- `EDGAR-PB-01-B` — The most complete numeric cure mechanic opened. Lending value percentage 50%;
  margin requirement (the ratio of everything outstanding to collateral value) 75%; if the margin
  ratio exceeds 75% the pledgor has **5 business days** either to pay down or to post additional
  collateral, and in each case the restoration target is back to the 50% lending value percentage,
  not merely back inside the 75% trigger. Separately, the pledgor must deliver a written statement
  of *how* it will address the deficit within **1 business day** of the call being issued. The
  document then disclaims the whole mechanic: notwithstanding the bank's general policy of giving
  notice of a deficiency, the bank is not obliged to call at all, and if the ratio rises above 75%
  there may be circumstances in which it must liquidate without notice.
- `EDGAR-PB-01-B` (pledge, separate clause) — A second, shorter route: if the bank determines in its
  sole discretion that collateral value has fallen or that collateral is for any reason no longer
  satisfactory, and notifies, the pledgor has **3 business days** to deliver additional collateral,
  and failure is itself a default entitling the bank to realise.
- `EDGAR-ML-03` — Institutional version with the tightest published clock: on a margin call notice
  delivered by 8:00 p.m., cash must be in the collateral accounts by 5:00 p.m. on the date **two
  business days** after delivery; if the borrower delivers a specified certificate by 5:00 p.m. on
  the next business day, the deadline stretches to **three business days**. The restoration target
  is the LTV maintenance level, computed off the share value on the call date rather than a moving
  price. A separate, lower release level governs getting cash back out.
- `EDGAR-ML-04` — Cure time is 5:00 p.m. on the **second scheduled trading day** after the collateral
  call notice, with an anti-stacking rule: if a fresh shortfall occurs while an earlier one is still
  uncured, the cure time for the new shortfall shortens to the later of the old cure time or 5:00
  p.m. on the **first business day** after the new notice. Three separate levels are named — margin
  call, reset and release — with all three percentages redacted from the public filing.
- `EDGAR-ML-01` / `EDGAR-ML-02` — Show the drafting convention that the levels and the cure time are
  defined by reference to a confidential side letter, so the agreement is public and the numbers are
  not. `EDGAR-ML-02` adds a capital-call cure: if the fund parent delivers a capital call
  confirmation package before the ordinary cure time, an extended cure time applies and a standstill
  runs for the capital call period. `EDGAR-ML-01` permits cure by a permitted sale, treated as cured
  on delivery of eligible trade tickets before the cure time, with proceeds swept on settlement, and
  makes the cure amount notionally deductible when testing whether a *further* shortfall has arisen
  the next day.
- `BANK-LU-02` — The only bank-terms document with two numeric levels: the bank may call for further
  cover once the lendable exchange value of the pledged assets falls below **130%** of outstandings,
  with the client required to agree a suitable arrangement within a period the bank sets; and if the
  lendable value falls below **120%** of the debt, the bank may liquidate and realise part or all of
  the pledge **straightaway without any notice**.
- `BANK-LU-01` — No cure period at all as a matter of drafting. The bank will, on a best-endeavours
  basis only, notify when it judges the lending value is about to become insufficient; the
  communication is at the bank's sole discretion, creates no right in the client, and failure to
  send it does not prejudice the bank. Amounts are stated to be due and payable immediately and
  without prior notice, and any deferral is a discretionary favour.
- `BANK-US-01` — Published in one line: the client is not entitled to an extension of time on a
  margin call, and collateral may be liquidated without consent if the deadline is missed.
- `BANK-CH-01` — The client-facing framing: if the securities fall in value *and/or* their
  loan-to-value ratios are adjusted, the client must post more or repay; if that is not done on
  time, the bank may restructure the portfolio or liquidate the pledged assets.
- `FIRM-01` — Market colour on the cure period: cures are required within "a couple of business
  days" and this is generally consistent across facilities. Also notes lenders are generally
  reluctant to accept *additional pledged securities* as a cure, preferring cash or repayment, and
  that in practice the cure cash comes from the fund parent rather than the borrower.
- `FIRM-03` — Swiss practice: banks typically allow no more than two days to top up.
- `IND-CH-01` — The disclosure-side description of the same event: if value falls below a level the
  lender may call for more collateral or repayment, and if the client does not deliver, the lender
  may liquidate at an inopportune moment, which is itself an additional liquidity risk to the client.

### security_structure_control

Applies: `EDGAR-PL-02`, `EDGAR-PL-03`, `EDGAR-PL-01`, `EDGAR-PB-01`, `LAW-EW-01`, `LAW-LU-01`, `BANK-LU-03`, `BANK-LU-01`, `EDGAR-EN-01`

- `EDGAR-PL-02` — The fullest control build in the pool. A first-priority security interest plus a
  right of set-off; a custodian acceptable to the secured party; separate cash and share collateral
  accounts with sub-accounts for initial and additional collateral; a control agreement between
  pledgor, custodian and secured party; financing statements filed; shares re-registered into the
  custodian's name. Two lender-side points worth lifting: the secured party expressly may **not**
  rehypothecate, use, lend, pledge or sell the collateral shares except as the documents allow or
  with consent; and voting stays with the pledgor until an event of default, at which point an
  irrevocable proxy flips voting to the secured party.
- `EDGAR-PL-03` — The third-party-custodian variant: a secured custodian securities account control
  agreement and a deposit account control agreement with a depositary agent that is not the lender,
  plus UCC filings, with the security stated to be a valid, perfected, first-priority interest in
  the accounts, in all financial assets credited to them, in the security entitlements and in the
  cash. This is the structure to cite when the lender is not the custodian.
- `EDGAR-PL-01` — Adds the pledgor negative covenants that protect the structure: defend the
  collateral against adverse claims, never allow a financing statement naming anyone else as
  secured party, create no lien other than the lender's and permitted liens, and bear the costs of
  defending and enforcing the security interest.
- `EDGAR-PB-01-C` — The private-bank end of the spectrum: the bank takes a security interest,
  pledge, lien, charge, assignment, hypothecation and right of set-off over everything in named
  accounts, asserts **full dominion and control** with no withdrawals permitted, and may release
  only such excess as it decides, taking loanable values, currency risk, tax liabilities and other
  risks into account. It states that the agreement creates a valid and perfected first fixed charge
  and first-priority security interest.
- `LAW-EW-01` — The English scope trap. A security financial collateral arrangement requires the
  collateral to be delivered, transferred, held, registered or otherwise designated so as to be in
  the possession or under the control of the collateral-taker, *and* requires both the
  collateral-provider and the collateral-taker to be **non-natural persons**. An individual pledgor
  therefore falls outside the regime, and the FCAR conveniences (no registration formalities,
  appropriation, insolvency disapplications) are not available. This is the single most important
  jurisdictional point for a private-wealth playbook drafted in England.
- `LAW-LU-01` — The Luxembourg contrast. The law applies to pledge agreements over collateral
  generally (Part II, art. 3), with no non-natural-person gate of the English kind; possession may
  be constituted through an agreed third-party holder (art. 5). But it contains its own retail rule
  in the other direction: credit institutions and investment firms providing investment services are
  **prohibited, on pain of nullity**, from concluding a transfer of title for security purposes with
  a retail client (art. 13), and must document their consideration of title-transfer use in any
  case (art. 13-1). So in Luxembourg the structural choice for a retail-classified client is pledge,
  not title transfer.
- `BANK-LU-03` — Shows how a bank makes the structure automatic: by force of the general terms and
  the 2005 law, everything entrusted by the client to the bank is pledged ipso jure for whatever the
  client owes now or in future, the bank cannot be compelled to release it, and the bank also holds
  a retention right over the pledged collateral.
- `BANK-LU-01` — Points the retail Lombard facility at the same general deed of pledge in the
  general terms, and pledges the assets in *all* the client's accounts including joint accounts of
  which the client is one holder.
- `EDGAR-EN-01` — English-law security deed over listed shares held through a custodian for an SPV
  holder, expressly framed against the FCARs, with releases conditioned on an excess-financial-
  collateral determination and on no event of default subsisting.

### events_of_default

Applies: `EDGAR-ML-03`, `EDGAR-PB-01`, `BANK-LU-01`, `BANK-LU-03`, `FIRM-01`, `EDGAR-ML-04`, `EDGAR-ML-01`

- `EDGAR-ML-03` — The negotiated institutional list, with graduated cures: misrepresentation in any
  material respect; non-payment of principal with no grace, of interest and fees with a **1 business
  day** grace (**2 business days** if the failure was purely administrative or operational error),
  and of a margin call amount with no grace; cross-default above a threshold amount after any
  applicable grace; breach of the negative covenants and of named structural covenants with no cure;
  breach of any other covenant with a **30 day** cure running from the earlier of notice and a
  responsible officer's knowledge, except where the breach by its nature cannot be cured; involuntary
  insolvency proceedings undismissed for **30 days**; voluntary insolvency with automatic
  acceleration; unsatisfied judgments above a threshold for **30 consecutive days**; repudiation of
  the loan documents; the security ceasing to be a valid first-priority perfected interest; plan-
  asset status; and illegality. Acceleration on the voluntary-insolvency limb is automatic and
  requires no notice; every other limb requires a notice first.
- `EDGAR-PB-01-C` — The private-bank list, which is far broader and far less curable: default however
  defined under the credit documents; any obligation breached for any reason including the actual or
  *threatened* effect of any law, regulation, order or decree; a false representation by or on behalf
  of any "Material Person", a defined term reaching the borrower, the pledgor, any other guarantor or
  collateral provider **and any beneficial owner or settlor of any of them**; any Material Person
  dying, becoming incompetent, or having its existence terminated or threatened with termination;
  actual or threatened insolvency, business failure or material litigation of a Material Person;
  attachment, seizure, forfeiture, subpoena, court order or regulatory proceedings against a Material
  Person or a substantial part of its property as determined in the bank's sole discretion; and the
  bank deeming the collateral inadequate, impaired or insecure.
- `BANK-LU-01` — The retail list used as both a termination trigger and a liquidation trigger:
  failure to meet a repayment request; an impending or actual fall in lending value or the lending
  value otherwise proving insufficient; failure to post additional collateral by the stipulated
  deadline; failure to respond to a request for additional collateral; a further fall in lending
  value after notification but before the deadline; collateral not sufficiently diversified in the
  bank's opinion; substantial deterioration in economic, regulatory or financial conditions or loss
  of market confidence endangering normal market functioning; unauthorised overrun; inaccurate or
  incomplete information given in the application; breach of any provision; the client's solvency
  being in doubt; the **death of the client**; and change of law increasing the bank's cost or
  reducing its income.
- `BANK-LU-03` — Immediate termination where the customer gave incorrect or incomplete information
  on identity or financial condition, where a substantial deterioration in financial condition occurs
  **or threatens to occur**, where the collateral obtained is or becomes insufficient, or where
  required collateral has not been delivered; with everything falling immediately due.
- `FIRM-01` — Explains the institutional substitute for a general MAC: mandatory prepayment events,
  each meant to capture a change in the assumptions the loan was made on — issuer insolvency, change
  of control of the borrower, delisting of the pledged securities, a trading suspension continuing
  beyond a set number of trading days, nationalisation of the issuer. It also describes the share
  price trigger as a *separate* lever from the margin call mechanics, and gives the intuition that
  at a price less than half the closing price the financing has fundamentally changed.
- `EDGAR-ML-04` — Recent worked example: mandatory prepayment events limited to change of control, a
  defined issuer event, a regulatory event and a specified prepayment event, with change of control
  defined off a 50% beneficial-ownership threshold.
- `EDGAR-ML-01` — Carries a reference price trigger event (reference price below a stated threshold)
  and gap triggers with multiple levels, all defined by reference to the confidential terms letter.

### enforcement_liquidation

Applies: `EDGAR-PL-02`, `EDGAR-PB-01`, `BANK-LU-01`, `BANK-LU-02`, `BANK-LU-03`, `LAW-LU-01`, `FIRM-02`, `FIRM-03`, `EDGAR-ML-03`

- `EDGAR-PL-02` — The most valuable enforcement clause in the pool because it pre-agrees the
  commercial-reasonableness standard rather than relying on it. On default the secured party may take
  control of proceeds, transfer collateral into its own or a nominee's name, and sell publicly or
  privately without demand or notice of intention except where applicable law forbids waiver. The
  pledgor then acknowledges, in advance, that: the pledged block is far larger than can be sold
  quickly on the exchange; sale timing and manner may produce materially less than another timing
  would; the secured party has **no obligation to dribble the stock out over time**; it may sell
  immediately on default **without seeking strategic buyers or any control premium**, notwithstanding
  a significant discount; a sale following a customary bookbuild counts as a public sale, with the
  relevant UCC public-sale protection waived to the extent inconsistent; and a private placement
  made in good faith where a public sale would raise securities-law issues is deemed commercially
  reasonable and is not unreasonable merely for being restricted. Deficiency liability survives, and
  the duty of care is reduced to reasonable physical safekeeping or reasonable care in selecting a
  bailee.
- `EDGAR-PB-01-B` — The private-bank version: at least **5 business days'** prior notice of the time
  and place of any public sale, or of the time after which a private sale is to be made, agreed in
  advance to be reasonable — but with **no notice at all required** where the collateral threatens to
  decline speedily in value or is of a type customarily sold on a recognised market, which is most of
  a listed securities portfolio. The bank is not obliged to sell even after giving notice, and may
  adjourn a sale by announcement without further notice.
- `EDGAR-PB-01-A` — Same structure at **3 business days'** notice where notice is required by law,
  with the same recognised-market and speedily-declining carve-outs.
- `EDGAR-PB-01-C` — At **3 days'** notice if notice is required by law, with a deeming provision that
  on certain seizure or regulatory-process events the bank is treated as having appropriated
  collateral equal to the obligations *before* it received notice of the event — a direct answer to
  the freeze-order problem.
- `BANK-LU-01` — Unilateral liquidation on the appropriate exchange or the open market, without prior
  notice, on any of a long list of triggers; the client is expressly informed of that right; and no
  failure or delay in exercising it is a waiver.
- `BANK-LU-02` — Two-speed: at the 130% level, liquidate only such positions as the bank deems
  necessary after the client has failed to take suitable steps within the period the bank set; at the
  120% level, realise part or all of the pledge straightaway with no notice.
- `BANK-LU-03` — Enumerates the realisation routes under the 2005 law, including private transaction
  at arm's-length conditions, sale on a stock exchange, public sale, and set-off against the client's
  claims on the bank after formal notice.
- `LAW-LU-01` — The statutory menu, art. 11(1): on an enforcement event the pledgee may, unless
  otherwise agreed, act **without prior notice** to appropriate at a price set by the agreed valuation
  method; assign by private sale in a commercially reasonable manner, on a trading venue where the
  collateral is admitted to trading, or by public auction; obtain a judgment retaining the collateral
  against an expert valuation; net; appropriate listed instruments at market price or fund units at
  the last published NAV (not older than one year); redeem fund units; or exercise rights under a
  pledged insurance contract. Art. 11(2) sets the public-auction formalities including **8 working
  days'** advance newspaper notice and minutes within **3 working days**. Art. 11(3) is the control
  answer: an agreed third-party custodian must transfer on notice of an enforcement event without the
  collateral provider's consent and without informing it in advance. Art. 20 makes the arrangements,
  the agreed enforcement events and the agreed valuation and enforcement measures effective against
  insolvency officials notwithstanding reorganisation or winding-up proceedings. Art. 22 invalidates
  a loss-of-securities opposition filed in the window between the agreed notice and realisation,
  provided that window does not exceed one month.
- `FIRM-02` — The English constraint on appropriation: the valuation must follow the terms of the
  arrangement and in any event be conducted in a commercially reasonable manner, judged objectively;
  the outcome need not be reasonable, only the manner; responsibility stays with the collateral-taker
  even where a third-party valuer is used; and a non-compliant valuation does not void the
  appropriation but permits the court to substitute a compliant one.
- `FIRM-03` — The Swiss constraint: standard clauses do allow liquidation without prior warning, but
  the bank owes duties of care and loyalty in liquidating, must be able to produce accounting
  documentation for the liquidation, and where it acts as discretionary manager or adviser it may owe
  a duty to notify the client of a margin deficiency first.
- `EDGAR-ML-03` — Multi-lender enforcement: each lender may exercise or refrain from exercising
  remedies against the collateral under its own control agreement in its sole discretion, owes no
  fiduciary duty to the other lenders, and agrees not to interfere with or support a challenge to the
  commercial reasonableness of another lender's disposal.

### capacity_authority

Applies: `EDGAR-ML-03`, `EDGAR-PB-01`, `BANK-LU-01`, `LAW-LU-01`, `LAW-UK-02`, `EDGAR-PL-02`

- `EDGAR-ML-03` — The corporate CP package as an authority test: certified constitutional documents,
  good-standing certificate, certified resolutions authorising execution, delivery and performance
  and confirming they have not been amended or rescinded, incumbency and specimen signatures, a
  second officer's certificate as to the certifying officer, and a financial officer's certificate
  confirming that no borrowing or similar limit binding on the borrower would be exceeded.
- `EDGAR-PB-01-C` — Compresses the same thing for a mixed group of individual and non-individual
  grantors: each non-individual grantor certifies it is duly organised and in good standing and that
  all actions and consents required by its statutes, charter documents, applicable law **or
  agreements** — shareholder consents expressly included — have been taken. The individual grantors
  give no such certificate, which is itself the point: individual capacity is assumed and only
  tested through the death/incompetence event of default.
- `EDGAR-PB-01-B` — For third-party security, makes the pledgor's obligations absolute and
  unconditional irrespective of the validity or enforceability of the documents evidencing the
  obligations, any change in terms, any release of other collateral or guarantees, or any other
  circumstance that would be a surety defence, with all such defences waived.
- `EDGAR-PB-01-A` — Also takes a solvency representation from the guarantor, with a three-limb
  definition (fair saleable value of assets exceeds liabilities including contingent ones and the
  amount needed to meet probable liability; sufficient capital to conduct the business; able to meet
  debts as they mature), plus a savings clause reducing the guaranteed amount to whatever a court
  would uphold if the full amount were set aside.
- `BANK-LU-01` — The retail authority set is done by representation rather than by document: no
  existing default, no pending or threatened litigation that could materially affect ability to
  perform, tax compliance, AML and anti-corruption compliance, and — commercially the most useful —
  that the client acts for its own account and not for third parties, with an undertaking to notify
  immediately on any change of beneficial owner, that change being subject to fresh KYC and formal
  bank approval.
- `LAW-LU-01` — Art. 12 removes one authority obstacle by statute: shareholder approval is not needed
  to realise a pledge over all the shares of a Luxembourg private limited company granted in one
  transaction, and in other cases approval may be given irrevocably in advance.
- `LAW-UK-02` — Where the borrower is an individual, capacity questions are joined by regulatory
  perimeter questions: the exemption depends on a declaration by the borrower and a compliant
  income/assets statement delivered before the agreement, and the credit exceeding £60,260 (unless
  the agreement is secured on land).
- `EDGAR-PL-02` — Authority to *act on* the collateral after default: an irrevocable power of attorney
  coupled with an interest, exercisable only on and during an event of default, to take any action
  and execute any document including selling collateral in the pledgor's name, and to receive,
  endorse and collect distributions and give discharge.

### governing_law_jurisdiction

Applies: `EDGAR-ML-03`, `EDGAR-ML-01`, `EDGAR-PL-03`, `EDGAR-PB-01`, `EDGAR-EN-01`, `BANK-LU-01`, `LAW-LU-01`, `LAW-EW-01`

- `EDGAR-ML-03` / `EDGAR-ML-01` / `EDGAR-PL-03` — Every filed institutional margin loan and pledge
  opened in this pool is governed by New York law, with submission to the New York courts, regardless
  of where the borrower, the issuer or the collateral sits. The observation to carry into the clause
  entry is the *uniformity*, not the choice: the market standardises on one law for the loan and
  security package and handles local-law questions by opinion rather than by splitting the governing
  law.
- `EDGAR-PB-01-A` — Private-bank version with three layers: a negotiation period of 45 days followed
  by mandatory AAA arbitration seated in Manhattan before three New York banking lawyers, with
  punitive, consequential and lost-profit claims waived and confidentiality imposed; New York
  governing law for the whole relationship; and, if the arbitration clause fails, exclusive
  submission to the federal and state courts of New York **but with the bank free to proceed where
  the guarantor resides or does business**.
- `EDGAR-PB-01-B` — The booking-location variant, which is the most transferable idea for a
  private-wealth playbook: governing law of the state where the pledge is booked, and suit permitted,
  at the bank's election, in the courts of either the state where the obligations are booked or the
  state where the collateral is booked, held or managed, on a non-exclusive basis; with a process
  agent appointed by the pledgor and renewed annually, and immunity waived.
- `EDGAR-PB-01-C` — Same asymmetry more briefly: New York law; grantor submits to non-exclusive
  jurisdiction in New York City and agrees not to plead forum non conveniens; bank may nonetheless
  sue in other jurisdictions; sovereign and other immunity irrevocably waived.
- `EDGAR-EN-01` — The English-law data point: the security deed, the amendment notice and any
  non-contractual obligations arising out of them are governed by English law.
- `BANK-LU-01` — Luxembourg law, "in particular" the Law of 5 August 2005 on financial collateral
  arrangements — i.e. the governing-law clause names the enforcement statute it is relying on.
  Luxembourg is the sole place of performance, place of debt collection for clients domiciled abroad
  and sole place of jurisdiction, **but** the bank reserves the right to sue at the client's domicile
  or before any other competent authority, in which case Luxembourg law still applies exclusively;
  all subject to mandatory conflicts rules.
- `LAW-LU-01` — Shows why that choice is made: arts. 18–20 make the netting, the agreed enforcement
  events and the agreed valuation and enforcement measures effective against third parties,
  commissioners, receivers and liquidators notwithstanding domestic *or foreign* reorganisation or
  winding-up proceedings.
- `LAW-EW-01` — Shows the opposite consideration for England: the regime's advantages turn on the
  status of the parties (both non-natural persons) and on possession or control, so a governing-law
  choice does not by itself deliver the FCAR treatment.

### no_advice_non_reliance

Applies: `EDGAR-PB-01`, `BANK-LU-01`, `BANK-CH-01`, `IND-CH-01`, `BANK-US-01`, `EDGAR-PL-02`

- `EDGAR-PB-01-C` — The tightest non-reliance wording found: the grantor represents that it enters
  the agreement on its **own independent analysis** and is not in any way relying on any statement or
  representation by the bank as to the borrower, the loan, the credit documents, the collateral, its
  value or condition, or any other matter. It is paired with a statement that the grantor chose to
  take on the obligations free from any bank requirement, and that the obligations are independent of
  the investment performance of the collateral.
- `EDGAR-PB-01-B` — The suitability-facing version: a sophisticated-investor representation with
  three limbs — sufficient knowledge and experience of margin lending and the relevant instruments;
  access to and knowledge of appropriate analytical tools to evaluate the collateral and its effect
  on the overall portfolio; and sufficient financial resources and liquidity to bear all the risks
  including loss of the entire principal.
- `EDGAR-PB-01-A` — Handles the conflict rather than denying it: where collateral sits in an account
  the bank or an affiliate manages on a discretionary basis, the guarantor acknowledges that the dual
  role of creditor and discretionary manager could give rise to a conflict of interest, and consents
  to it. Worth flagging because it is a *consent* structure, not a *disclaimer* structure.
- `BANK-LU-01` — Points at a published investment and risk warning notice and a separate risk
  disclosure for the more volatile asset classes, then takes a representation that the client has
  read and accepted them and is aware of the risks, repeated at all times until termination. It also
  carries a consumer-facing **14 calendar day** withdrawal right for a retail client under a distance
  contract where the facility has not been used.
- `BANK-CH-01` — Carries a marketing-material disclaimer stating the document is not investment advice
  and is not based on the addressee's personal circumstances, while in the body recommending that the
  client obtain detailed advice that the borrowing matches their objectives. The tension between
  those two is exactly the exposure this clause exists to manage.
- `IND-CH-01` — The industry risk booklet puts the point in regulatory terms: conventional lending
  sits under general civil law, but where a client takes a loan in order to invest in financial
  instruments, for instance a Lombard loan, that is a financial service and the investor-protection
  provisions apply **in full**. Its credit-financed-investment block names the leverage effect
  (fixed borrowing costs against uncertain returns, with losses potentially exceeding the amount
  invested), margin requirements and liquidity squeezes, and currency risk where the loan is taken
  in a foreign currency for the lower rate.
- `BANK-US-01` — Publishes the two standard limbs: a risk statement that the risk of loss in
  financing a transaction by depositing collateral is significant and that losses may exceed the
  cash and other assets deposited; and a scope limitation that the firm does not provide tax or
  legal advice.
- `EDGAR-PL-02` — The lender-side complement: an exculpation for everything except wilful misconduct,
  gross negligence or fraud, and an acknowledgement that the secured party is under no duty to
  realise the collateral at all, or in any particular manner or order.

---

## Observed ranges

Every row is an observation from a document actually opened. Where a source states a position without
a number, the row records the *shape* of the position rather than inventing one. `X` in a clause entry
should be filled by Stuart from the ranges below, not from this table's midpoint.

### Cure periods (time to meet a margin call)

| observation | ref |
|---|---|
| 5 business days to restore, with a written statement of *how* the deficit will be met due within 1 business day of the call | `EDGAR-PB-01-B` |
| 3 business days to deliver additional collateral where the bank determines in its sole discretion that collateral is no longer satisfactory | `EDGAR-PB-01-B` (pledge, separate limb) |
| 2 business days from delivery of the call notice, extended to 3 business days if a specified certificate is delivered by 5 p.m. the next business day | `EDGAR-ML-03` |
| 2 scheduled trading days from the call notice; shortened to the later of the existing cure time or 1 business day where a second shortfall arises during an uncured cure period | `EDGAR-ML-04` |
| Cure time defined only by reference to a confidential side letter; an extended cure time available on delivery of a capital call package, running as a standstill | `EDGAR-ML-01`, `EDGAR-ML-02` |
| "A couple of business days", described as generally consistent across the margin loan market | `FIRM-01` |
| Typically not more than two days allowed to top up (Swiss practice) | `FIRM-03` |
| No fixed period: notification on a best-endeavours basis only, amounts due immediately and without prior notice, any deferral discretionary | `BANK-LU-01` |
| No fixed period: "within the period of time set by the Bank" | `BANK-LU-02` |
| No entitlement to an extension of time on a margin call | `BANK-US-01` |
| 10 calendar days' notice before realisation where the acceleration arises from a change of law / increased cost event | `EDGAR-PB-01-B` |
| Payment grace of 1 business day for interest and fees, 2 business days where the failure was purely administrative or operational; no grace for principal or for a margin call amount | `EDGAR-ML-03` |
| 30 days to cure a general covenant breach, from the earlier of notice and a responsible officer's knowledge | `EDGAR-ML-03` |

### Margin call trigger vs restoration level

| observation | ref |
|---|---|
| Lending value 50% of collateral; call triggered when the outstanding-to-collateral ratio exceeds 75%; restoration target is back to the 50% lending value, not merely back inside 75% | `EDGAR-PB-01-B` |
| Collateral lending value must be at least 100% of all outstandings at all times, including unmatured and contingent amounts; top-up is immediate | `EDGAR-PB-01-A` |
| Top-up call when the lendable exchange value falls below 130% of outstandings (≈ 77% LTV); immediate realisation without notice below 120% (≈ 83% LTV) | `BANK-LU-02` |
| Three named levels — margin call, maintenance/reset, and a lower release level — with restoration measured off the price on the shortfall date, not a moving price | `EDGAR-ML-03`, `EDGAR-ML-04`, `EDGAR-ML-01` |
| Trigger LTV / Reset LTV architecture described as the basic tenet, with a separate, lower pro forma level gating collateral releases and sales | `FIRM-01` |
| Numeric levels deliberately moved into a confidential fee-and-ratio or additional-terms letter so that the filed agreement discloses the mechanic and not the numbers | `EDGAR-ML-01`, `EDGAR-ML-02`, `EDGAR-ML-03`, `EDGAR-ML-04` |
| Independent share-price trigger set at a level unrelated to the LTV mechanic; commentary intuition is that below roughly half the closing price the financing has fundamentally changed | `EDGAR-ML-01`, `FIRM-01` |
| Regulation U: purpose credit secured by margin stock must be fully collateralised with a 50% haircut on the margin stock — $100m of purpose credit requires at least $200m of margin stock | `FIRM-01` |

### Lending value by asset class

No source opened publishes a table of advance rates by asset class. What was found instead:

| observation | ref |
|---|---|
| Lending value = market value of eligible pledged assets minus the bank's haircut, calculated by the bank **acting in good faith** | `BANK-LU-01` |
| Limit set on: a percentage of collateral value, the nature of the assets, their risk profile (volatility and liquidity named), and the level of diversification across shares, bonds, fund units and other classes | `BANK-LU-01` |
| Lending value driven by type, currency, quality, volatility and marketability of the securities plus portfolio diversification, and reviewed at regular intervals | `BANK-CH-01` |
| 50% lending value percentage on the margin collateral, changeable at the bank's sole and absolute discretion | `EDGAR-PB-01-B` |
| Bank-set percentage per class of a bank-determined fair market value, floored by any applicable regulatory maximum margin percentage | `EDGAR-PB-01-A` |
| Exchange-listed common stock marked to market, often daily; private-company collateral valued off sponsor-reported value with negotiated appraisal and sometimes dispute rights | `FIRM-01` |
| Listed instruments realisable at market price; fund units realisable at the last published NAV provided it is under a year old, or at the fund's redemption price | `LAW-LU-01` art. 11 |
| Regulator's position: pledged securities can fall by more than the haircuts applied, and haircuts may be set too low | `REG-CH-01`, `REG-CH-02` |

**Gap:** no cash / listed equity / bond / fund / structured-product advance-rate grid was obtained
from any published source. Mark any such grid in a clause entry `[VERIFY]`.

### Single-name concentration caps

No numeric single-name cap appears in any source opened. What was found:

| observation | ref |
|---|---|
| Supervisory concern named as single-stock lending and undiversified collateral, plus correlated exposure where many banks lend against the same collateral | `REG-CH-02` |
| Supervision of the Lombard book focused on risks from concentrated or more illiquid collateral | `REG-CH-01` |
| No cap; instead three levers — diversification as an input to the Limit, differentiated fees where the portfolio is not sufficiently diversified, and insufficient diversification as a stand-alone liquidation trigger | `BANK-LU-01` |
| Diversification as one input into the loan-to-value ratio | `BANK-CH-01` |
| "Future Financing" / "Restricted Transactions" covenant barring borrower affiliates from pledging same-class securities to secure other financings, to prevent stacked margin loans and exit overhang | `FIRM-01`, `EDGAR-ML-03` |
| Concentration cap on the **lender's** side: deemed beneficial ownership of the issuer aggregated across the lender, its affiliates and any deemed group, with enforcement disposals conditioned on staying inside it | `EDGAR-PL-01`, `EDGAR-PL-02` |
| 10% beneficial-ownership and 50% change-of-control thresholds used as structural triggers; pledged stock subject to an underwriter lock-up | `EDGAR-ML-04` |

**Gap:** the 25% / 50% thresholds assumed in build plan §4 rules R06 and R06b are not corroborated by
any source opened. They must be treated as the institution's own risk appetite, not a market observation.

### Notice periods for changing lending values / haircuts

| observation | ref |
|---|---|
| 15 days' prior written notice to modify the margin requirement — collapsing to immediate effect if the change is required by law or if collateral value is rapidly diminishing | `EDGAR-PB-01-B` |
| May change or eliminate the lending-value percentage for any class of collateral at any time without prior notice, unless specifically agreed in writing | `EDGAR-PB-01-A` |
| May amend haircuts and reduce or withdraw the Limit at any time, without notice, with immediate effect, informing the client afterwards by a channel of the bank's choosing | `BANK-LU-01` |
| May increase margin requirements at any time and is not required to give advance written notice | `BANK-US-01` |
| Loan-to-value ratio "reviewed at regular intervals"; an adjustment to the ratio is itself a top-up trigger | `BANK-CH-01` |
| Lendable exchange values decided in the interests of the bank alone and relinquishable at the bank's will | `BANK-LU-02` |
| Limit on the above: discretion must be exercised in good faith and not abusively; the call must state the amount and the deadline, and the bank must be able to produce the calculation parameters | `FIRM-03` |

### Material adverse change formulations

| observation | ref |
|---|---|
| "The bank deems the collateral inadequate, impaired or insecure" — a pure subjective-satisfaction MAC over the collateral rather than over the borrower | `EDGAR-PB-01-C` |
| Collateral "no longer satisfactory to the bank" as determined in its sole discretion, triggering a 3 business day top-up and then default | `EDGAR-PB-01-B` |
| Actual or **threatened** effect of any law, regulation, order or decree; actual or **threatened** insolvency, business failure or material litigation of any Material Person | `EDGAR-PB-01-C` |
| "If for any other reason the Bank considers that the conditions enabling the Bank to grant the Limit have changed"; and separately, a substantial deterioration in economic, regulatory or financial conditions or loss of market confidence endangering the normal functioning of markets | `BANK-LU-01` |
| Substantial deterioration in the customer's financial status or condition which occurs **or threatens to occur**; collateral "is or becomes insufficient" | `BANK-LU-03` |
| No general MAC at all. Replaced by a closed list of mandatory prepayment events — issuer insolvency, change of control, delisting, trading suspension beyond a set number of trading days, nationalisation — plus an independent share price trigger and an average-daily-volume trigger | `FIRM-01`, `EDGAR-ML-01`, `EDGAR-ML-02`, `EDGAR-ML-04` |
| Change of law / increased cost treated as a default in the private-bank documents, but with 10 calendar days' notice before realisation; treated as an illegality event of default or an increased-costs indemnity in the institutional documents | `EDGAR-PB-01-B`, `EDGAR-ML-03` |
| Facility adjustment events where the calculation agent determines no commercially reasonable adjustment is practicable, producing mandatory prepayment and termination | `EDGAR-ML-01`, `FIRM-01` |

### Death and incapacity of individuals

| observation | ref |
|---|---|
| Death **or incompetence** of any "Material Person" — defined to reach the borrower, the pledgor, any other guarantor or collateral provider and any beneficial owner or settlor of any of them — permits the bank to declare everything immediately due without notice or demand and to appropriate, sell or set off | `EDGAR-PB-01-C` |
| Death of the client is an express, stand-alone ground for unilateral realisation of the pledged assets without prior notice | `BANK-LU-01` |
| The pledge is **not** terminated by the death or dissolution of the pledgor and binds the pledgor's successors, representatives and estate | `EDGAR-PB-01-B` |
| Loss of a specified constitutive status, or the pledgor's constitutive documents being amended, restated, revoked, dissolved or invalidated, is a separate liquidation trigger — the entity analogue of incapacity | `EDGAR-PB-01-B` |
| A continuing guarantee is revocable only on seven days' written notice, and revocation does not release obligations already arising or arising under a pre-existing commitment | `EDGAR-PB-01-A` |
| No death or incapacity event of default at all — the borrower is an SPV, so the nearest analogue is a change-of-control mandatory prepayment event | `EDGAR-ML-01`, `EDGAR-ML-02`, `EDGAR-ML-03`, `EDGAR-ML-04` |
| The regulatory overlay that makes this sensitive for individuals: where the borrower is an individual, exemption from the regulated-credit regime depends on a pre-agreement declaration and income/assets statement, so the estate of a deceased individual borrower cannot regularise it after the fact | `LAW-UK-02` |

---

## Counterparty asks observed

Pushes below are either recorded in the commentary as things borrowers request, or are the visible
negotiated outcome in a filed agreement (i.e. the clause as filed *is* the concession). Marked
`[observed-in-filing]` or `[commentary]` accordingly.

### facility_type
- Convert the demand line into a committed term facility with a stated maturity and no demand right,
  accepting instead an exhaustive negotiated list of mandatory prepayment events `[observed-in-filing:
  EDGAR-ML-03, EDGAR-ML-04]`.
- Where the facility stays uncommitted, a fixed minimum notice period before the bank may terminate
  for convenience — the published retail analogue is 90 days `[observed-in-filing: BANK-LU-01]`.
- A committed facility that survives collateral movement between signing and funding, which lenders
  resist because the LTV on the funding date may already be in call `[commentary: FIRM-01]`.

### conditions_precedent
- Replace an open-ended "such other documents as the lender may reasonably request" with a closed
  list; the filed compromise keeps the sweeper but qualifies it by reasonableness
  `[observed-in-filing: EDGAR-ML-03]`.
- Satisfy collateral-quality CPs by representation rather than by lender satisfaction; the filed
  compromise is "reasonably satisfied" `[observed-in-filing: EDGAR-ML-03]`.
- For an individual borrower, defer the high-net-worth declaration and statement until after signing
  — not available, since the statement must precede the agreement `[LAW-UK-02]`.

### eligible_collateral_lending_values
- A contractual lending-value grid by asset class that cannot be changed unilaterally. No source
  opened concedes this; every bank-terms document reserves the right to change
  `[BANK-LU-01, BANK-US-01, EDGAR-PB-01-A]`.
- Where collateral is not exchange-listed, appraisal rights and a dispute mechanism over the
  lender's valuation — conceded in some private-company margin loans `[commentary: FIRM-01]`.
- A good-faith qualifier on the calculation of lending value — conceded in a published retail
  document `[observed-in-filing: BANK-LU-01]`.
- Notice of a haircut change before it bites, rather than after `[EDGAR-PB-01-B concedes 15 days;
  BANK-LU-01 and BANK-US-01 refuse]`.

### concentration_limits
- No single-name cap at all where the whole facility is a single-stock margin loan; the lender's
  answer is a lower LTV plus a same-class negative pledge on affiliates rather than a cap
  `[commentary: FIRM-01; observed-in-filing: EDGAR-ML-03]`.
- Carve the borrower's other vehicles out of the same-class negative pledge `[commentary: FIRM-01,
  which records the covenant as generally accepted notwithstanding that it reaches beyond the borrower]`.
- Remove insufficient diversification as a stand-alone liquidation trigger and make it a repricing
  event only `[BANK-LU-01 retains both the fee lever and the liquidation trigger]`.

### lender_discretion_valuation
- Replace "sole and absolute discretion" with "good faith and in a commercially reasonable manner"
  `[observed-in-filing: EDGAR-ML-03, EDGAR-EN-01]`.
- Require the lender to show its working — the calculation details and parameters behind a call
  `[commentary: FIRM-03, as a Swiss-law duty rather than a negotiated term]`.
- Require notice before a haircut change, and no change during an open margin call
  `[EDGAR-PB-01-B concedes 15 days with a rapid-decline carve-out]`.
- Cap the frequency of revaluation, or require revaluation only at stated intervals; the published
  documents instead assert daily mark-to-market or review "at regular intervals"
  `[BANK-US-01, BANK-CH-01]`.

### margin_maintenance_cure
- A longer cure period — the observed concession ladder runs 1 business day → 2 business days →
  3 business days on a certificate → 5 business days in private-banking documents
  `[EDGAR-ML-04, EDGAR-ML-03, EDGAR-PB-01-B]`.
- An extended cure where the cash must come from a parent or a capital call, structured as a
  standstill and collapsing immediately if the funding source fails `[observed-in-filing:
  EDGAR-ML-02; commentary: FIRM-01]`.
- Cure by posting additional securities rather than cash — generally resisted `[commentary: FIRM-01]`.
- Cure by selling collateral, deemed cured on delivery of trade tickets before the cure time with
  proceeds swept on settlement `[observed-in-filing: EDGAR-ML-01]`.
- Written notice as a precondition to any liquidation, and the removal of the "the bank is not
  obliged to call at all" disclaimer `[EDGAR-PB-01-B and BANK-LU-01 both retain the disclaimer]`.
- Restoration to the trigger level rather than to the lower maintenance/reset level — refused in
  every document opened, all of which restore to the lower level `[EDGAR-ML-03, EDGAR-ML-04,
  EDGAR-PB-01-B]`.

### security_structure_control
- No rehypothecation or reuse of the pledged securities — conceded expressly
  `[observed-in-filing: EDGAR-PL-02]`.
- Voting rights to remain with the pledgor until an event of default — conceded, with an irrevocable
  proxy flipping on default `[observed-in-filing: EDGAR-PL-02]`.
- Permit withdrawals and substitutions of collateral without case-by-case consent; the private-bank
  documents refuse, subjecting all withdrawals and substitutions to the bank's discretion and, in one,
  asserting full dominion with no withdrawals permitted `[EDGAR-PB-01-A, EDGAR-PB-01-C]`.
- Use a third-party custodian rather than the lender, answered by control agreements rather than by
  refusing `[observed-in-filing: EDGAR-PL-03, EDGAR-PL-02]`.
- For a retail-classified client in Luxembourg, resist title transfer — this is a statutory
  prohibition, not a negotiation `[LAW-LU-01 art. 13]`.

### events_of_default
- Delete the general MAC and replace it with an enumerated list — this is the institutional market
  standard `[observed-in-filing: EDGAR-ML-03; commentary: FIRM-01]`.
- Materiality and grace periods on covenant and payment defaults — conceded as 1–2 business days on
  payment and 30 days on general covenants `[observed-in-filing: EDGAR-ML-03]`.
- Narrow the definition of the persons whose death, incapacity, insolvency or misstatement triggers
  default — the private-bank drafting reaches beneficial owners and settlors
  `[EDGAR-PB-01-C]`.
- Remove "threatened" from insolvency, litigation and change-of-law limbs `[EDGAR-PB-01-C,
  BANK-LU-03 both retain it]`.
- Remove death of the client as a stand-alone liquidation trigger, replacing it with a standstill
  while the estate is administered `[BANK-LU-01 retains it as a liquidation trigger]`.

### enforcement_liquidation
- Notice before any sale, with no recognised-market or rapid-decline carve-out — the observed
  concession ladder is 3 days → 3 business days → 5 business days, in each case with the carve-outs
  retained `[EDGAR-PB-01-C, EDGAR-PB-01-A, EDGAR-PB-01-B]`.
- An obligation to sell in an orderly way — a dribble-out or VWAP programme, or an obligation to seek
  strategic buyers or a control premium — expressly negated in advance
  `[observed-in-filing: EDGAR-PL-02]`.
- Delete the pre-agreed deeming of bookbuild sales as public sales and of restricted private sales as
  commercially reasonable `[observed-in-filing: EDGAR-PL-02, which retains both]`.
- A standstill period after an event of default before remedies may be exercised, or a requirement
  that lenders act together; refused, with each lender free to act alone and the others agreeing not
  to challenge commercial reasonableness `[observed-in-filing: EDGAR-ML-03]`.
- Non-recourse for any deficiency after realisation; refused in every document opened
  `[EDGAR-PL-02, EDGAR-PB-01-B, BANK-CH-01]`.
- In Luxembourg, contract out of the no-prior-notice default in art. 11(1) — available, since the
  statute applies "unless otherwise provided for" `[LAW-LU-01]`.

### capacity_authority
- Trustee limited recourse: liability confined to the trust fund, with no personal liability for the
  trustee. Not present in any document opened; the private-bank drafting runs the other way, making
  a third-party pledgor's obligations absolute and unconditional with all surety defences waived
  `[EDGAR-PB-01-B]`.
- Drop the solvency representation, or qualify it to knowledge `[EDGAR-PB-01-A takes it flat, with a
  three-limb definition]`.
- Drop the requirement to notify and re-KYC on any change of beneficial owner `[BANK-LU-01 retains
  it, with continued service conditional on the bank's approval]`.
- Limit the constitutional-authority certificate to constitutional documents and law, excluding
  "or agreements" `[EDGAR-PB-01-C reaches agreements expressly]`.

### governing_law_jurisdiction
- Mutual exclusive jurisdiction rather than an asymmetric clause letting the lender sue anywhere;
  refused in every private-bank document opened, all of which reserve the lender's right to sue at
  the client's domicile or elsewhere `[EDGAR-PB-01-A, EDGAR-PB-01-B, EDGAR-PB-01-C, BANK-LU-01]`.
- Litigation rather than arbitration, or at least a carve-out for interim relief
  `[EDGAR-PB-01-A imposes AAA arbitration with a 45-day negotiation window first]`.
- Governing law of the client's home jurisdiction rather than the booking location
  `[EDGAR-PB-01-B ties both law and forum to the booking location at the bank's election]`.
- Delete the immunity and forum-non-conveniens waivers `[EDGAR-PB-01-B, EDGAR-PB-01-C retain both]`.

### no_advice_non_reliance
- Soften the sophisticated-investor representation to a knowledge qualifier, or delete the limb on
  having sufficient resources to bear loss of the entire principal `[EDGAR-PB-01-B takes all three
  limbs flat]`.
- Carve out from non-reliance any statement the bank actually made about the collateral or the
  facility `[EDGAR-PB-01-C excludes reliance on any statement as to the borrower, the loan, the
  documents, the collateral, its value or condition, or any other matter]`.
- Where the bank also manages the portfolio, a duty to warn of an impending margin deficiency; the
  filed answer is a conflict acknowledgement and consent rather than a duty, but Swiss case law
  imposes a notification duty on a discretionary manager independently `[EDGAR-PB-01-A;
  commentary: FIRM-03]`.
- Resist the characterisation of the Lombard loan as a financial service attracting full
  investor-protection duties — not available in Switzerland `[IND-CH-01]`.
- For a retail client on a distance contract, the 14 calendar day withdrawal right where the facility
  is unused `[observed-in-filing: BANK-LU-01]`.
