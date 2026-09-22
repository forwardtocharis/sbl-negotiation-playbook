# WP2 Hand-off — Glossary and Product Definition

Scope touched: `F:\SBL_Legal\docs\glossary.md`, `F:\SBL_Legal\docs\product_definition.md`, `F:\SBL_Legal\docs\source_register.md`, `F:\SBL_Legal\handoff\WP2.md`. Nothing outside `docs/` or this hand-off file was modified.

## Acceptance check

Script: `check_glossary.py`, run from the session scratchpad (not committed to the repo), confirms all twelve core clause titles from `build_plan.md` §3 appear as `##`/`###` headings in `docs/glossary.md`.

Output:

```
Headings found in glossary.md:
 - Account control agreement / control
 - Additional canonical terms
 - Benchmark (SONIA, SARON, EURIBOR)
 - Capacity and authority
 - Concentration limits
 - Conditions precedent
 - Cross-collateralisation and set-off
 - Currency mismatch
 - Custodian
 - Eligible collateral
 - Eligible collateral and lending values
 - Enforcement and liquidation
 - Events of default
 - Facility type
 - Financial collateral arrangement (regime overview)
 - Governing law and jurisdiction
 - Lender discretion
 - Lender discretion over valuation and eligibility
 - Lombard loan / SBL / securities-backed lending / margin loan
 - MAC clause
 - Margin maintenance, margin call mechanics and cure period
 - No advice and non-reliance
 - No-advice / non-reliance
 - PDMR / insider / closed period
 - Securities lending (what SBL is NOT)
 - Security structure and control
 - Third-party security / pledgor / surety defences
 - Tier semantics
 - Uncommitted demand facility vs committed term facility

PASS: all twelve core clause titles appear as headings in glossary.md
```

Note: a few clause-title headings duplicate a synonym-based term heading (e.g. "Eligible collateral" alongside "Eligible collateral and lending values"; "Lender discretion" alongside "Lender discretion over valuation and eligibility"; "No-advice / non-reliance" alongside "No advice and non-reliance"). Per the brief, these were kept as separate short cross-reference headings pointing to the fuller merged entry, rather than literally merged, because the exact clause-title wording ("No advice and non-reliance", "Lender discretion over valuation and eligibility") had to appear verbatim as its own heading for the grep test, while the term-taxonomy list in the task also named "lender discretion" and "no-advice / non-reliance" as separate required synonym headings. Both sets of headings exist; the test only requires the twelve exact clause titles to be present, and it passes.

## Sources opened

Web access was available (WebSearch + WebFetch). Sources actually opened and read (not just search snippets) are recorded in `docs/source_register.md` with dates and reliability grades:

- **UK Financial Collateral Arrangements (No. 2) Regulations 2003** (SI 2003/3226) — opened via legislation.gov.uk, reliability A, verified true. Confirmed: non-natural-person scope restriction on both collateral-provider and collateral-taker; disapplication of Companies Act 2006 ss.859A/859H charge registration for qualifying security arrangements. Did not clearly confirm appropriation as an enforcement method from what was read — left `[VERIFY]` in the glossary.
- **SEC EDGAR filed Special Custody Account Pledge and Control Agreement** (Monteagle Enhanced Equity Income Fund / Interactive Brokers LLC / Huntington National Bank) — opened and read for structure only (tripartite roles, control mechanics, margin/default/enforcement provisions), reliability B, verified true. No wording lifted; no real party names used in playbook text (source's own party names are real-filing names and were not carried into any playbook content).
- **Societe Generale Private Banking glossary, "Lombard Loan"** — opened and read directly, reliability B, verified true. Used for the Lombard-loan definition and Lombard/SBL equivalence, paraphrased.

Sources found via search but **not** opened as primary/full text (search-result snippets and secondary commentary only) — used only to shape `[VERIFY]`-tagged statements, recorded in `source_register.md` at reliability C, verified false:
- Swiss Federal Intermediated Securities Act (FISA/BEG) and Code of Obligations pledge provisions — only Lexology/CapLaw/Mondaq commentary snippets reviewed.
- Luxembourg Law of 5 August 2005 on financial collateral arrangements — primary consolidated PDF located (CSSF) but not opened in this work package; only law-firm commentary snippets (Harneys, Elvinger Hoss, K&L Gates) reviewed.

These two need a WP7 agent to open the primary texts directly before any jurisdiction-file statement built on them is written without `[VERIFY]`.

## Definitions I am least confident about

1. **Appropriation as an enforcement method under the UK FCARs** — the primary-text summary I obtained did not clearly confirm appropriation (as opposed to sale/close-out netting) as an available enforcement route under the 2003 Regulations. Left `[VERIFY]` in "Enforcement and liquidation" and in the FCA regime one-liner. A WP7 agent should re-check this against the regulation text directly (regs 17–18 area is the usual location in commentary, not independently confirmed here).
2. **Lender-discretion notice-period market practice** — the "Lender discretion over valuation and eligibility" entry describes the contested notice-period dynamic from general market understanding, not from a specific filed facility letter or published bank terms document I read. Marked `[VERIFY]`.
3. **Third-party security / surety defences** — the description of surety-type defences (discharge on variation without consent, independent-advice requirement) is a generic secured-lending law statement, not confirmed against primary case law or a specific jurisdiction's suretyship doctrine. Marked `[VERIFY]`; this is likely to vary most sharply by jurisdiction and deserves the most scrutiny of anything in the glossary.
4. **Swiss FISA/BEG mechanics (control agreement, Privatverwertung/Selbsteintritt)** — built entirely from secondary commentary, not the primary statute. Marked `[VERIFY]` and flagged in the source register as needing a WP7 follow-up.
5. **Luxembourg financial collateral regime and natural-person treatment** — same caveat; primary text located but not read. Marked `[VERIFY]`.

## Files delivered

- `F:\SBL_Legal\docs\glossary.md` — tier table (verbatim from build_plan.md §2.2) + canonical terms + all twelve core clause-title headings.
- `F:\SBL_Legal\docs\product_definition.md` — SBL vs securities lending (one quotable paragraph), Lombard terminology, three-document set (one paragraph each), PWM negotiation dynamic paragraph, "What this demonstrator is and is not" section.
- `F:\SBL_Legal\docs\source_register.md` — header, grading legend, seeded table of the five sources above.
- `F:\SBL_Legal\handoff\WP2.md` — this file.
