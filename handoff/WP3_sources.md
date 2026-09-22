# WP3 hand-off — shared source pool

**Task:** gather and record the shared source pool for WP3 (core twelve clause entries).
**Date:** 2026-09-21.
**Output:** `docs/research/clause_sources.md` (source pool table, per-clause map, observed ranges,
counterparty asks observed). This note is the hand-off summary only.

No other file in the repo was touched.

---

## 1. Count of sources by grade

23 distinct sources, all opened and read by the sourcing agent.

| grade | meaning (build plan §2.1) | count | refs |
|---|---|---|---|
| A | primary law / regulator | 5 | `REG-CH-01`, `REG-CH-02`, `LAW-EW-01`, `LAW-UK-02`, `LAW-LU-01` |
| B | filed agreement / bank terms | 15 | Filed (9): `EDGAR-ML-01` … `-04`, `EDGAR-PL-01` … `-03`, `EDGAR-PB-01`, `EDGAR-EN-01`. Bank/industry terms (6): `BANK-LU-01` … `-03`, `BANK-CH-01`, `BANK-US-01`, `IND-CH-01` |
| C | commentary | 3 | `FIRM-01`, `FIRM-02`, `FIRM-03` |

Against the WP3 acceptance test ("≥ 3 sources per entry of which ≥ 1 is reliability A or B"):
every one of the twelve clauses has at least three refs mapped and at least one A or B ref.

Against the brief's per-clause sourcing procedure — (a) a filed agreement on EDGAR, (b) a published
private-bank SBL/Lombard terms document, (c) a law-firm/textbook/regulator note — all twelve clauses
have (a) and (b). Two clauses lack a dedicated (c): see §2.

Coverage counts by clause (refs mapped):

| clause | refs | filed | bank terms | commentary/regulator |
|---|---|---|---|---|
| facility_type | 6 | yes | yes | yes |
| conditions_precedent | 7 | yes | yes | yes |
| eligible_collateral_lending_values | 8 | yes | yes | yes |
| concentration_limits | 9 | yes | yes | yes |
| lender_discretion_valuation | 8 | yes | yes | yes |
| margin_maintenance_cure | 12 | yes | yes | yes |
| security_structure_control | 9 | yes | yes | **no dedicated C** (covered by A: `LAW-EW-01`, `LAW-LU-01`) |
| events_of_default | 7 | yes | yes | yes |
| enforcement_liquidation | 9 | yes | yes | yes |
| capacity_authority | 6 | yes | yes | **no C and no A beyond `LAW-LU-01` art. 12 / `LAW-UK-02`** |
| governing_law_jurisdiction | 8 | yes | yes | **no dedicated C** |
| no_advice_non_reliance | 6 | yes | yes | yes (`IND-CH-01` is industry-standard disclosure, graded B) |

---

## 2. Clauses with thin coverage

Ranked worst first. These are where Stuart's review time will earn most.

1. **`capacity_authority` — thinnest.** Every filed document opened is either a corporate/SPV
   borrower (so capacity is a certified-resolutions exercise) or an individual/trust pledgor whose
   capacity is simply assumed and then policed by a death-and-incompetence event of default. No
   source was opened on **trustee** power to borrow and to charge trust assets under English law,
   trustee personal liability and limited-recourse drafting, beneficiary consents, or the trustee
   indemnity and lien. Rule R01 in build plan §4 depends on exactly that material. The one usable
   data point is negative: the private-bank drafting runs the *opposite* way to a limited-recourse
   ask, making a third-party pledgor's obligations absolute and unconditional with surety defences
   waived (`EDGAR-PB-01-B`).

2. **Lending values by asset class — no source found.** No published grid of advance rates for cash,
   listed equity, listed bonds, daily-dealing funds, gated funds or structured products was located
   in any opened document. Only the *drivers* are published (type, currency, quality, volatility,
   marketability, diversification) plus two isolated numbers: a 50% lending-value percentage in one
   filed private-bank margin addendum, and the Regulation U 50% haircut on margin stock for purpose
   credit. Any asset-class grid written into `eligible_collateral_lending_values` must carry
   `[VERIFY]` and be flagged as institutional risk appetite, not a market observation.

3. **Single-name concentration caps — no numeric source found.** Build plan §4 rules R06 (>25%) and
   R06b (>50%) have **no corroboration** in any source opened. The regulator names single-stock and
   undiversified collateral as the risk but sets no threshold; the bank terms use diversification as
   an input to the limit, a fee lever and a liquidation trigger rather than a cap. Recommend the
   clause entry states the percentage as `X` with a comment that no published threshold was found.

4. **`governing_law_jurisdiction` — geographically lopsided.** Every filed institutional margin loan
   and pledge opened is New York law / New York courts; the private-bank documents are New York or
   booking-location law. Luxembourg is covered well (`BANK-LU-01`, `LAW-LU-01`). **Switzerland has no
   governing-law or jurisdiction clause source at all** — the Swiss material in the pool is a product
   factsheet, the regulator's risk monitor, an industry risk booklet and a practitioner note on
   margin calls. Only one English-law security document was opened (`EDGAR-EN-01`), and it is an
   amendment notice rather than the underlying deed. WP7 (jurisdiction overlay) will need to source
   Switzerland separately; do not let WP3 imply Swiss coverage exists.

5. **`security_structure_control` — English natural-person question is identified but not resolved.**
   `LAW-EW-01` establishes that a security financial collateral arrangement requires both parties to
   be non-natural persons, so an individual pledgor falls outside the FCARs. What is **not** sourced
   is the consequence: whether Bills of Sale legislation bites, how Companies Act charge registration
   interacts, and what the market actually does for individual pledgors in England. This is exactly
   the `fca_safe_harbour_uncertain` flag in rule R04 and it should stay `[VERIFY]`.

6. **Death and incapacity — good on death, thin on incapacity.** Death is well sourced from three
   angles (a filed private-bank event of default reaching beneficial owners and settlors; a published
   retail agreement making death a stand-alone liquidation trigger; a pledge expressly surviving
   death and binding the estate). **Incapacity short of death** — loss of mental capacity of an
   individual borrower or of one of several trustees, and the effect of a power of attorney — is
   covered only by the phrase "becomes incompetent" in one filed document. No primary or secondary
   source on mental-capacity law was opened.

7. **`no_advice_non_reliance` — no MiFID or FinSA primary text opened.** The suitability link is
   sourced from an industry risk booklet (grade B) and a practitioner note (grade C), not from the
   directive, the Act or a regulator's rules. The `mifid_suitability` flag should stay `[VERIFY]`
   until WP8 sources it directly.

---

## 3. Things I could not open

All of these were attempted and failed; none is recorded in the source pool.

| source | url | failure |
|---|---|---|
| Law-firm note on FCAR appropriation (a second English view alongside `FIRM-02`) | https://www.hsfkramer.com/notes/bankinglitigation/2023-02/high-court-considers-enforcement-of-security-by-way-of-appropriation-under-the-financial-collateral-arrangements-no-2-regulations-2003-fcars | HTTP 403 |
| "Lombard loans in the crisis" (Swiss commentary) | https://www.lexology.com/library/detail.aspx?g=bb27dc55-8d63-42bf-a8c3-e9e6b01a6fa3 | HTTP 403 (Lexology blocks unauthenticated fetches; three further Lexology URLs failed the same way) |
| "In review: credit support and subordination in Switzerland" — intended Swiss pledge/FISA/private-realisation source | https://www.lexology.com/library/detail.aspx?g=8be3df3f-4f2b-42ff-b46b-edb944f37fc1 | HTTP 403. **This is the main reason Swiss security-law coverage is thin.** |
| Margin loan market commentary | https://debtexplorer.whitecase.com/leveraged-finance-commentary/margin-loans-come-to-private-markets | HTTP 403 |
| "The Lombard credit and the leverage effect" (Swiss journal article, would have covered bank discretion, margin deadlines and private realisation) | https://www.reiser.law/wp-content/uploads/2021/04/SJ-2021-II-47-1.pdf | redirected to an HTML block page; PDF not served |
| Law-firm briefing on lending to trustees (the gap at §2 item 1) | https://www.farrer.co.uk/news-and-insights/how-to-lend-to-trustees/ | HTTP 403 |
| Swiss bank Lombard loan factsheet (second Swiss bank-terms source) | https://www.cic.ch/dam/jcr:c6b6a7c7-55a2-468f-8074-e49569ddf233/factsheet_lombard_en.pdf | HTTP 404 |
| Securities-lending explainer (would have supported the WP2 SBL-vs-securities-lending distinction) | https://www.nomura.com/resources/europe/pdfs/equity-fianace.pdf | opened, but it is about securities lending and repo, not securities-backed lending. Read and discarded as off-point; **not** recorded in the pool. |

One structural limitation worth recording rather than treating as a failure: in every one of the four
filed institutional margin loan agreements opened, the LTV initial, margin call, maintenance/reset and
release **percentages are defined by reference to a confidential fee-and-ratio or additional-terms
letter and are redacted or simply absent from the public filing**. The mechanics are public; the
numbers are not. That is why the only unredacted trigger levels in the pool come from a 2008
private-bank composite exhibit (`EDGAR-PB-01`) and from one Luxembourg bank's published general
conditions (`BANK-LU-02`). Drafters should not expect to find more numbers on EDGAR by searching harder.

---

## 4. Notes for the clause-drafting sub-agents

- Cite by ref label. The full URL, retrieval date, grade and note are in
  `docs/research/clause_sources.md` §"Source pool"; copy those fields verbatim into each clause's
  `sources:` block so `docs/source_register.md` can be assembled mechanically later.
- `EDGAR-PB-01` has three sub-parts (`-A`, `-B`, `-C`). Cite the sub-part, not the parent, so a
  reviewer can find the passage.
- Do not name any bank, borrower, pledgor, issuer or trust. The pool file describes every filed
  document generically plus its accession number, and that is the form to carry into clause entries.
- Do not lift wording. Every observation in the pool file is already a paraphrase; paraphrase again
  rather than copying the pool file's sentences into clause `text:` fields.
- Where a number is a judgement call, write `X` and put the observed range from
  §"Observed ranges" in a YAML comment on the line, with the ref label. Do not pick a midpoint.
- The three "no source found" gaps (asset-class lending value grid, single-name concentration cap,
  Swiss security law) must be written as `[VERIFY]` and surfaced in the clause's hand-off note, not
  quietly filled from general knowledge.
