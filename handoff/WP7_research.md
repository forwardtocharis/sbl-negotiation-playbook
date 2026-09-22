# WP7 hand-off — jurisdiction overlay, research half

Agent: WP7 research. Date: 2026-09-21. Status of output: `draft`.

**Deliverable:** `docs/research/jurisdictions_research.md` — seven fields for each of England & Wales,
Switzerland and Luxembourg, plus "Inputs for rules R04 and R14", "Consumer credit inputs for WP8"
(UK / Switzerland / Luxembourg, MiFID II & FinSA suitability on leverage, UK MAR Article 19), and a
`## Source register rows` table with every source listed once, ready to append to
`docs/source_register.md`.

**No YAML written.** Per instruction, `playbook/jurisdictions/*.yaml` was not created; the schema is
being frozen by another agent. The research file is structured field-by-field so the YAML author can
lift each `### <field>` answer and its `Sources:` block directly. No other file in the repo was
touched.

---

## 1. What I verified against primary text

I opened and read the text for every row marked `verified: true`. Specifically:

**England & Wales** — legislation.gov.uk
- FCARs 2003 (SI 2003/3226) reg 3 (current, as amended): the **both parties must be non-natural
  persons** requirement for *both* the security FCA and the title transfer FCA; the inclusive
  definition of possession (credit to an account in the taker's name, provider's rights limited to
  substitution of equal-or-greater value or withdrawal of excess); definitions of financial collateral
  and security interest.
- reg 4 (current): disapplies **CA 2006 ss.859A and 859H** (substituted for the old CA 1985 s.395
  reference with effect from 6 April 2013).
- regs 8, 17, 18, 19 (as made) and the full table of contents: the insolvency disapplications,
  appropriation without a court order, the **commercially reasonable manner** valuation duty, and the
  account-location conflict-of-laws rule.
- CA 2006 s.859A (21 days from the day after creation); LPA 1925 ss.101 and 103; IA 1986 s.285
  (subsection (4) preserving secured creditors' rights on personal bankruptcy).
- RAO 2001 arts 60C (GBP 25,000, wholly-or-predominantly business purpose, declaration and the
  "knows or has reasonable cause to suspect" carve-out) and 60H (individual borrower, credit exceeding
  **GBP 60,260**, declaration, statement of high net worth); CCA 1974 s.16B confirmed **omitted** from
  1 April 2014.
- FCA Handbook CONC App 1.4 (**GBP 150,000 net income / GBP 500,000 net assets**, exclusions, who may
  sign, declaration content) and COBS 9A.2 (9A.2.1R / 9A.2.7R / 9A.2.8R / **9A.2.17G** on the overall
  transaction where an instrument is linked to a loan).
- MAR Art. 19 (retained UK law) on legislation.gov.uk: three working days, EUR 5,000 threshold,
  **pledging and lending notifiable**, the custody-account pledge carve-out **until designated to
  secure a specific credit facility**, and the 30-calendar-day closed period.

**Switzerland** — fedlex.admin.ch official PDF-A texts, extracted and read in full for the relevant
articles (English translations except where noted)
- FISA / BEG (SR 957.1): Art. 2(1) and **Art. 2(1bis)** (Art. 31(2) reaches intermediated securities
  held abroad under foreign law), Art. 4 (custodians), **Art. 5(d)** (closed definition of qualified
  investor — a natural person is not one), Arts 21-23 (custodian's retention/foreclosure right, right
  of use requiring written authorisation not buried in GTCs), **Arts 24, 25, 26** (credit, control
  agreement, agreement with the custodian), Art. 30 (priorities and the custodian subordination rule),
  **Art. 31** (sale or appropriation where value is objectively determinable; **31(2)** power unaffected
  by debt enforcement, reorganisation or protective proceedings; 31(3) custodian need not verify), and
  **Art. 32** (pre-realisation notice, waivable only by a custodian or qualified investor; account and
  surplus).
- Civil Code (SR 210) Arts 884, 891, **894** (lex commissoria prohibition), 899, 900, **901(3)**
  (intermediated securities governed exclusively by FISA).
- PILA (SR 291) **Art. 105** and **Arts 108a-108d** (Hague Convention as the applicable-law rule).
- DEBA (SR 281.1) Arts 41, 198, 219(1).
- Banking Act (SR 952.0) **Art. 47** — German official text; no English PDF found at that ELI.
- FADP (SR 235.1) Arts 16-17.
- FinSA (SR 950.1) **Art. 3(c)(5)** and Arts 10-14.
- KKG (SR 221.214.1) Arts 1, 2, 3 and **Art. 7(1)(a)-(g)**, German official text — in particular
  **7(1)(b)** (credit covered by deposited customary bank collateral or sufficient assets the consumer
  holds with the lender) and **7(1)(e)** (below CHF 500 or above CHF 80,000).
- HCCH: status table for Convention #36 (Mauritius, Switzerland, USA; in force 1 April 2017; UK,
  Luxembourg and the EU are **not** parties) and the Convention full text Arts 2, 4(1) and 5.

**Luxembourg**
- Law of 5 August 2005 on financial collateral arrangements, CSSF consolidated text updated
  15 July 2024: Arts 1 (definitions incl. relevant account), **2(1)** ("merchant or a non-merchant"),
  2(2)-(6), 3, **4** (all-present-and-future pledge), **5** (the four possession routes for book-entry
  instruments, the custodian ranking waiver, notification for other instruments, claims perfected on
  conclusion), 10 (right of use), **11** (enforcement **without prior notice**; the seven routes;
  auction machinery; third-party custodian must transfer without the provider's consent), 12, 13,
  **20** (insolvency remoteness; **20(4)** carve-out for the Law of 8 December 2000 on
  over-indebtedness; death or incapacity of the provider), 21, **23** (PRIMA), 24, **26** (no
  registration formalities).
- Code de la consommation, Legilux consolidated version 31 December 2024: **Art. L.224-3(1)(a), (c),
  (h), (k)** and **L.224-3(5)** — in particular the **EUR 200 / EUR 75,000** bounds and the
  investment-firm/credit-institution carve-out for credit letting an investor carry out a transaction
  in MiFID Annex I Section C instruments.

**Commentary (grade C) actually opened and read**
- Clifford Chance, "Financial collateral remains a Gray area" (Nov 2012) — source of the verified
  citations *Gray v G-T-P Group Ltd (Re F2G Realisations Ltd)* [2010] EWHC 1772 (Ch) and *Re Lehman
  Brothers International (Europe) (in administration)* [2012] EWHC 2997 (Ch), and of the
  "dispossession" point.
- Bär & Karrer / Practical Law, "Lending and Taking Security in Switzerland: Overview" (law stated
  1 May 2025).
- Addleshaw Goddard, "Luxembourg Financial Collateral Law" (2022) — confirms the 2022 amendments on
  trading-venue sales and pledged insurance contracts, and is **silent** on natural persons, prior
  notice and insolvency remoteness (I say so in the note rather than implying more).

---

## 2. What is `[VERIFY]` (verified: false)

1. **MiFID II Art. 25(2) and Annex I Section B(2).** EUR-Lex would not return usable article text
   through the fetch tool; the response only restated my question, so I refused to treat it as read.
   The EU-side suitability and ancillary-service points are therefore unsourced. The UK-side points in
   the same paragraph are sourced to the FCA Handbook, which I did read.
2. **Luxembourg's exercise of the Directive 2002/47/EC Art. 1(3) option on natural persons.** I did
   **not** open the Luxembourg for Finance page; the URL is recorded with `verified: false`. My
   statement that individuals are in scope is an **inference from primary text** (Art. 2(1) "merchant
   or a non-merchant" plus the Art. 20(4) over-indebtedness carve-out), flagged as such in the file.
3. **CCA 1974 s.16A.** I confirmed s.16B is omitted; I did not check s.16A.
4. **CCA 1974 ss.140A-140C unfair relationship powers applying to exempt agreements.** Strongly
   implied by the CONC App 1.4 declaration wording, but I did not read s.140A.
5. **UK MAR Art. 19 monetary threshold as onshored** (EUR 5,000 / EUR 20,000) and whether the FCA has
   exercised the uplift.
6. **Luxembourg Code de la consommation cross-reference to Directive 2004/39/EC** in Art. L.224-3(1)(h)
   — the consolidated text still names the pre-MiFID II directive; read across, but confirm.
7. **Directive (EU) 2023/2225 (CCD2)** effect on the Luxembourg thresholds once transposed — not
   researched.
8. **English independent-legal-advice / undue influence authority** for third-party non-commercial
   pledgors — stated as practice, not sourced. No URL invented; the register row has an empty url.
9. **Whether the GBP 25,000, GBP 60,260, GBP 150,000 and GBP 500,000 figures have been amended** after
   the versions I read on 2026-09-21.

---

## 3. My three lowest-confidence statements

1. **"Luxembourg natural persons are within scope of the 2005 Law."** This is the load-bearing
   contrast with England for the R04 story, and it rests on an inference (Art. 2(1) "merchant or a
   non-merchant" + the Art. 20(4) over-indebtedness carve-out) rather than an express scope provision I
   read. The 2005 Law has no scope article naming eligible persons the way FCARs reg 3 does. Highest
   priority for Stuart or Luxembourg counsel.
2. **"For a Swiss-booked account you can fix the proprietary law by agreement."** The chain is sound
   article by article (PILA Art. 108c → Hague Convention Art. 4(1), subject to the qualifying-office
   test) but I have not seen it applied to a Lombard pledge, and Art. 4(1)'s qualifying-office
   condition is a real constraint I have stated only in summary. The practical conclusion — Switzerland
   differs structurally from the English and Luxembourg PRIMA rule — I am confident about; the
   operational advice to use it I am not.
3. **"FISA Art. 31(2) means private realisation survives the pledgor's bankruptcy."** The article text
   is unambiguous and I read it, but it sits against a general Swiss rule (DEBA Art. 198, and the
   Bär & Karrer overview) that pledged assets fall into the estate and private enforcement stops. I
   have presented FISA as the specific rule overriding the general one. That is the orthodox reading,
   but a bank would not enforce on my say-so, and the overview I read does not spell the interaction
   out. Also in this bucket: the exact scope of "value can be determined objectively" in
   Art. 31(1)(b), which I have translated into an asset-class test (listed liquid yes, gated funds /
   structured / unlisted no) that is judgement, not law.

---

## 4. Notes for the agents downstream

- **Flag id naming risk (WP8).** `fca_safe_harbour_uncertain` reads as an FCA (regulator) point. It is
  not — it is the **FCARs** point. Either rename to something like `fcar_safe_harbour_uncertain` or put
  the clarification in the flag `description`, otherwise the markup will mislead an interviewer.
- **R04 should say "uncertain", not "unavailable".** The file gives three reasons: the test is on the
  parties to the *collateral arrangement* (a corporate or trustee-company pledgor can still qualify
  even where the borrower is an individual), a trust may have a corporate trustee, and possession or
  control still has to be satisfied on the facts. Suggested flag text is in the file.
- **R14 severity `low` is right**, but the flag should not be a no-op: the Banking Act Art. 47 duty is
  criminal and is not cured by a data-protection consent. Suggested flag text is in the file.
- **Field-level jurisdiction notes.** The three jurisdictions genuinely diverge on
  `registration_filing` (England: registration unless the FCAR exemption applies; Switzerland and
  Luxembourg: none at all), on `enforcement_route` (Luxembourg: no prior notice by default;
  Switzerland: notice non-waivable for a private individual; England: appropriation only inside the
  FCARs), and on `financial_collateral_regime` natural-person scope. Those three are worth printing in
  the markup for every deal. `perfection_depends_on` converges on "control through the custodian" in
  all three, so a clause note there can be shared.
- **R12 (third-party custodian) has concrete CP text available** in all three jurisdictions: England —
  account control agreement delivering dispossession; Switzerland — FISA Art. 25 control agreement plus
  a waiver of the custodian's Art. 21 rights; Luxembourg — Art. 5(2)(a)(ii) agreement or notified
  agreement, noting it is treated as the custodian waiving its own ranking.
- **Acceptance checks for this half of WP7 were not run**, because they are defined against the YAML
  files (`sbl validate`, rules R04/R14 referencing the file, markup printing the right file per
  governing law). Those belong to the YAML-authoring half of WP7 and should be pasted into that
  agent's hand-off.

---

## 5. Working files

Primary-text extracts were taken with `pdftotext -layout` into the session scratchpad
(`.../scratchpad/`: `pila.txt`, `deba.txt`, `zgb.txt`, `finsa.txt`, `fadp.txt`, `bankg.txt`,
`kkg.txt`, `lux_fcl.txt`, `lux_conso.txt`, `cc_gray.txt`). These are temporary and outside the repo;
nothing was copied into `F:\SBL_Legal` except the two files named at the top.
