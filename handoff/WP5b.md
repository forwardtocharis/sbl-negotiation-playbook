# Hand-off: WP5b (sourcing and reconciliation pass over `playbook/rules/rules.yaml`)

Agent hand-off, 2026-09-21. Follows `handoff/WP5.md`, which left every rule source as
`[VERIFY]` / `verified: false` because the drafting agent had opened nothing. WP5b replaces those
placeholders with the sources the research work packages actually opened, and rewrites the rule
strings that were written blind.

Everything in the repository is synthetic. Nothing here is legal advice. All 18 rules stay
`status: draft`; `reviewed_by` and `last_reviewed` are null throughout. **WP5b opened no new source
of its own**: every `verified: true` entry is lifted from a document that `docs/research/
jurisdictions_research.md` (WP7) or `docs/research/clause_sources.md` (WP3) records as opened and
read on 2026-09-21, and the note on each entry says what that source supports *for that rule*.

Rule `id`, `when` and `then` action structure are unchanged, so WP9's golden deals are unaffected.
Only `message`, `reason`, `text` and `rationale` strings, and the `sources` blocks, were touched —
plus three added `note` actions, listed in §4.

---

## 1. Acceptance output (pasted verbatim)

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: c503ee43bf66ab70b6872b3097da93840941ab1fe37232eecaab2daf092335b8
validate exit=0
```

```
$ .venv/Scripts/python -m sbl validate --summary
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: c503ee43bf66ab70b6872b3097da93840941ab1fe37232eecaab2daf092335b8

kind              stub   draft  reviewed   total
------------------------------------------------
clauses             12      12         0      24
rules                0      18         0      18
flags                0      10         0      10
jurisdictions        0       3         0       3

Entries not marked 'reviewed' have not been checked by a named human reviewer.
exit=0
```

```
$ .venv/Scripts/python -m pytest -q
........................................................................ [ 29%]
........................................................................ [ 59%]
........................................................................ [ 88%]
...........................                                              [100%]
243 passed in 34.01s
```

The clause line (12 stub / 12 draft) moves as the concurrent WP3 group A/C/D agents land content;
the rule line is this work package's. The library hash moves on every write by any agent.

No test failed at any point after the one relaxation in §3. No failure had to be attributed to a
clause file another agent was mid-editing.

---

## 2. Source counts, before and after

**Before (end of WP5):** 18 rules, 20 sources, **0 `verified: true`**, **20 `verified: false`**,
every one with `url: null` and a `[VERIFY]` ref.

**After (end of WP5b):** 18 rules, 76 sources, **62 `verified: true`**, **14 `verified: false`**.
Every verified entry carries the URL it was opened at and `retrieved: 2026-09-21`. Every unverified
entry carries `[VERIFY]` in its ref and in its note.

| rule | verified true | verified false | reliability grades of the verified sources |
|---|---|---|---|
| R01_trust_borrower | 1 | 1 | B |
| R02_corporate_or_partnership | 2 | 1 | A, B |
| R03a_natural_person_borrower_no_declaration | 6 | 1 | A×6 |
| R03b_natural_person_borrower_declared | 3 | 0 | A×3 |
| R04_natural_person_pledgor_england | 5 | 0 | A×4, C |
| R05_third_party_security | 1 | 1 | B |
| R05b_third_party_corporate_pledgor | 2 | 1 | A×2 |
| R06_concentration | 5 | 1 | A×2, B×2, C |
| R06b_concentration_severe | 3 | 1 | A, B, C |
| R07_pdmr_pledged_issuer | 1 | 1 | A |
| R08_restricted_securities | 3 | 1 | B×2, C |
| R09_real_estate | 3 | 1 | A×3 |
| R10_purpose_acquire_securities | 5 | 1 | A×3, B, C |
| R11_committed_term | 4 | 0 | B×3, C |
| R12_third_party_custodian | 5 | 1 | A×3, B×2 |
| R13_currency_mismatch | 4 | 1 | B×3, C |
| R14_swiss_booking | 5 | 0 | A×4, C |
| R15_illiquid_collateral | 4 | 1 | A×2, B, C |
| **total** | **62** | **14** | 33 A, 19 B, 10 C |

Four rules now have no `[VERIFY]` source at all: **R03b, R04, R11, R14**. R03b, R04 and R14 still
carry a `[VERIFY]` inside a message string for a specific unconfirmed point (§5).

---

## 3. The one test that was relaxed

`tests/test_engine.py::test_every_rule_is_draft_and_carries_a_rationale_and_a_source`. It asserted
that **every** rule source is `verified: false`, `[VERIFY]`-prefixed and `url: None` — a snapshot of
WP5's own honesty position, which became a lie-detector pointing the wrong way once real sources
landed. It now asserts that each source is honest in one of exactly two ways:

* `verified: true` → must have a `url`, and must **not** be `[VERIFY]`-prefixed; or
* `verified: false` → must carry `[VERIFY]` in its `ref` **or** in its `note`.

Everything else in that test is untouched: 15+ rules, every rule `draft`, rationale of at least 20
words, at least one source per rule. No other test was modified anywhere in the repository.

`test_r04_flag_message_is_verify_prefixed` was **not** modified and still passes: R04's message keeps
its `[VERIFY]` prefix, now attached to the sentence that genuinely is unconfirmed (see §4, R04).

---

## 4. Strings that changed

Nothing was fabricated. Every new statement below is traceable to the research file passage cited in
the corresponding source note.

| rule | field | what changed |
|---|---|---|
| **R01** | added `note` (events_of_default) | New: loss or amendment of a pledgor's constitutive status as the entity analogue of incapacity, from the filed private-bank exhibit. Existing CP, rep and capacity note unchanged. |
| **R02** | `require_cp` text | Added the borrowing-limit certificate to the CP list, from the filed corporate CP package. |
| **R03a** | `flag` message | Rewritten from a "may apply / nothing confirmed" placeholder to the actual exemption logic: UK Regulated Activities Order arts 60C (credit above GBP 25,000, wholly or predominantly business purpose) and 60H (credit above GBP 60,260 or security on land, prescribed declaration, compliant statement of net income ≥ GBP 150,000 or net assets ≥ GBP 500,000 delivered before the agreement), the move out of the 1974 Act on 1 April 2014, the Swiss Art. 7(1)(b) collateral exclusion and Art. 7(1)(e) CHF 80,000 ceiling, and the Luxembourg EUR 75,000 ceiling plus the investment-transaction carve-out. `[VERIFY]` now attaches only to whether the figures have been amended and to the unfair-relationship point. No longer `[VERIFY]`-prefixed as a whole. |
| **R03a** | `note` (conditions_precedent) | Now says *why* the sequence matters: the statement of high net worth must reach the lender before the agreement is made, so it cannot be regularised later. |
| **R03b** | `flag` message | Rewritten to the two ways a declaration still fails: the art. 60C presumption destroyed where the lender or anyone acting for it knows or has reasonable cause to suspect otherwise, and the art. 60H / handbook requirements on the declaration's form, prominence, signature and content plus the pre-execution statement. `[VERIFY]` kept only for whether the figures are current. |
| **R03b** | `note` (conditions_precedent) | Adds the statement of high net worth to what is kept on file. |
| **R04** | `flag` message | Rewritten to the actual point. It is not a conduct-regulator point: reg 3 of the Financial Collateral Arrangements (No. 2) Regulations 2003 requires **both** parties to be non-natural persons, an individual being excluded, so the reg 17 appropriation right, the reg 18 valuation framework and the regs 8/10 insolvency disapplications are not available on these facts. Two reasons it stays "uncertain" rather than "unavailable" are stated: the test is on the parties to the *collateral arrangement* (a corporate or trustee-company pledgor can still be inside), and possession or control must independently be satisfied, which the English courts read as requiring real dispossession. The `[VERIFY]` prefix is kept and now attaches to the first sentence — whether the safe harbour is available on these particular facts — which is the part that is genuinely fact-dependent and unconfirmed. |
| **R04** | `note` (security_structure_control) | `[VERIFY]` removed; now definite and specific: express power of sale with Law of Property Act 1925 s.103 disapplied, documented valuation and sale process evidencing the equitable duty. |
| **R04** | added `note` (enforcement_liquidation) | New: what is lost is the self-help package, not the security — Insolvency Act 1986 s.285(4) preserves enforcement rights on personal bankruptcy. |
| **R04** | `rationale` | Second sentence now states the rule rather than hedging it ("the regulations do not reach the arrangement at all, which is the classic private-wealth case and the classic family pledgor"). |
| **R05** | `note` (third_party_security_waivers) | Added the filed-practice sentence: obligations absolute and unconditional irrespective of the validity of the underlying documents, changes in terms or release of other collateral, surety defences waived. |
| **R05b** | `flag` message | Rewritten from "restrictions may apply, unconfirmed" to the sourced English position: the directors' duty to promote the success of the company as the basis of a corporate benefit analysis, and the Companies Act 2006 s.678 prohibition on a public company or its subsidiary giving financial assistance for an acquisition of its shares, with the principal-purpose and incidental-part exceptions. `[VERIFY]` kept, and confined to the Swiss and Luxembourg equivalents, which nobody has researched. |
| **R06** | added `note` (concentration_limits) | New: the three fallback levers observed in published bank terms (diversification as an input to the limit, differentiated fees, insufficient diversification as a liquidation ground) plus the institutional same-class negative pledge — concrete alternatives for a negotiator who cannot hold a hard percentage. |
| **R07** | `flag` message | Rewritten to the Market Abuse Regulation art. 19 point: pledging and lending are notifiable transactions for a person discharging managerial responsibilities; the custody-account carve-out falls away once the pledge is **designated to secure a specific credit facility**, so signing these documents starts the clock; notification promptly and within three working days once the year's transactions reach the EUR 5,000 aggregate (raisable to EUR 20,000); and the art. 19(11) 30-calendar-day closed period before interim and year-end reports. `[VERIFY]` confined to the onshored threshold figure and to non-UK regimes. |
| **R07** | added `note` (conditions_precedent) | New: the timing consequence — agree with compliance who tells the client, and when, before execution. |
| **R08** | `flag` message | Rewritten to name the shape of the restriction (holding period, current public information, volume, manner-of-sale and notice-filing conditions on an affiliate sale) and the contractual case (underwriter lock-up attaching to the pledged stock in a recent filed margin loan). `[VERIFY]` confined to the English, Swiss and Luxembourg equivalents, which are a known gap carried from WP8. |
| **R08** | `require_cp` text | Adds the filed collateral-quality condition: satisfaction that the shares carry no undisclosed transfer restrictions and settle through the ordinary book-entry system, with bona fide pledge and holding-period representations. |
| **R09** | `flag` message | Rewritten from "none of those regimes has been researched" to the three sourced perimeter points: UK regulated mortgage contract (credit to an individual or trustees, land at least 40 per cent used as a dwelling, entering into and administering each a specified activity); the Swiss real-estate-charge exclusion from the Consumer Credit Act; the Luxembourg immovable-property exclusion from the consumer credit chapter. `[VERIFY]` kept for the substantive real estate finance law, which remains unresearched. The two "out of scope for this playbook" notes are unchanged. |
| **R10** | `flag` message | Rewritten to the FinSA Art. 3(c)(5) point (granting loans to finance transactions with financial instruments is itself a financial service, with the Arts 10–14 duties) and the UK handbook point (suitability by risk tolerance and ability to bear losses; consider the suitability of the **overall** transaction where the instrument is linked to a loan). `[VERIFY]` confined to the EU-side wording, which the research could not retrieve. |
| **R10** | `note` (purpose_restrictions) | Adds that purpose credit secured by US margin stock carries its own collateralisation requirement, so the purpose statement has a regulatory consequence as well as a credit one. |
| **R11** | `note` (events_of_default) | Adds the institutional counter-model: an exhaustive negotiated list of mandatory prepayment events in place of a general material adverse change clause, which is the direction the borrower will push. |
| **R11** | added `note` (facility_type) | New: commitment shifts the signing-to-funding gap, so a facility committed on day one can be in margin call on the funding date; a drawdown condition on the loan-to-value level matters more here than on a demand line. |
| **R12** | `note` (security_structure_control) | `[VERIFY]` removed. Now states what control actually depends on in each of the three playbook jurisdictions: the English possession-or-control test and dispossession; the Swiss statutory routes to third-party effectiveness including a control agreement or an agreement with the custodian; the Luxembourg agreed third-party holder who must transfer on notice of an enforcement event without the provider's consent. Still ends with the overlay and local counsel. |
| **R13** | `note` (eligible_collateral_lending_values) | Adds that currency is one of the stated lending-value drivers in published bank terms. |
| **R13** | `note` (currency_mismatch_fx) | Now explicitly labels the lender-side allocation of conversion risk as a drafting preference, not a market standard, with `[VERIFY]` — an honesty downgrade from the previous flat assertion that the shortfall is the borrower's. |
| **R13** | added `note` (lender_discretion_valuation) | New: valuation discretion must be exercised in good faith and not abusively, and the bank must be able to produce the parameters behind its calculation. |
| **R14** | `flag` message | Rewritten to the Banking Act Art. 47 point (criminal offence, up to three years, five where a pecuniary advantage is obtained, CHF 250,000 fine for negligence, duty survives the relationship, reaches onward disclosure by a recipient) and the FADP Arts 16–17 point (adequacy or listed safeguards for transfers abroad, with the consent, contract-performance and enforcement-of-rights exceptions), ending with the sentence that matters commercially: a data protection consent alone does not answer the criminal duty. `[VERIFY]` removed. |
| **R14** | all three `note`s | `[VERIFY]` removed from each. The confidentiality note now distinguishes what the data protection exceptions do and do not cure; the security-structure note now names the intermediated-securities regime, Civil Code art. 901(3) routing, the statutory routes to third-party effectiveness and the requirement that private realisation be documented to show the best price obtainable. |
| **R15** | `note` (lender_discretion_valuation) | Adds how unlisted holdings are actually valued in filed practice (sponsor-reported value with negotiated appraisal and sometimes dispute rights). |
| **R15** | `note` (enforcement_liquidation) | Adds that the statutory shortcuts assume a priceable asset — listed instruments at market price, fund units at a published net asset value under a year old or at the redemption price — so collateral fitting none of those has no fast exit. |
| **R15** | `note` (eligible_collateral_lending_values) | Adds the supervisor's stated concern that haircuts are set too low rather than too high. |

### Rationale check

Every `rationale` was re-read against the two-to-four-sentence, lender-side, sayable-out-loud test.
Seventeen passed unchanged. **R04's was rewritten** because its middle sentence ("the kind of point a
lender should not assume in its own favour") was hedging a question the research had answered; it now
states the rule and names the two fact patterns it bites on. All 18 remain three or four sentences,
carry no citations, and are commercial explanations rather than statements of law.

---

## 5. Remaining `[VERIFY]` items

### 5.1 Fourteen unverified source entries, by rule

| rule | the gap |
|---|---|
| R01 | Trust law: trustee powers, the right of indemnity, limited recourse drafting. Nothing opened in any work package. |
| R02 | Capacity, authority and corporate benefit for partnerships, funds and non-English entities. |
| R03a | Whether the 1974 Act's unfair-relationship powers still reach an exempt agreement; Luxembourg transposition of Directive (EU) 2023/2225. |
| R05 | English undue influence and independent legal advice for third-party non-commercial security. Carried over from `docs/source_register.md`; still unresearched. |
| R05b | Swiss and Luxembourg equivalents of the financial assistance and corporate benefit restrictions. |
| R06 / R06b | The 25 per cent and 50 per cent single-name thresholds themselves. |
| R07 | Market abuse and insider dealing regimes outside the United Kingdom. |
| R08 | English, Swiss and Luxembourg equivalents of the resale restrictions on control and affiliate securities. |
| R09 | Substantive real estate finance law (creation, registration, priority, enforcement against land). |
| R10 | The EU markets-in-financial-instruments directive articles — recorded with its URL and `verified: false`, because the research's fetch returned no usable article text. |
| R12 | Perfection against a custodian in any jurisdiction outside the three covered. |
| R13 | Which party bears the conversion shortfall on enforcement. |
| R15 | Gating, redemption suspension, and the valuation of structured products as collateral. |

### 5.2 `[VERIFY]` inside rule strings

* **R04 flag message** — prefix retained; attaches to whether the safe harbour is available on these
  particular facts (fact-dependent, per §4).
* **R03a / R03b flag messages** — whether the monetary figures read on 2026-09-21 have since been
  amended; plus, in R03a, the unfair-relationship point.
* **R05b flag message** — the Swiss and Luxembourg restrictions.
* **R07 flag message** — the onshored threshold figure and whether the regulator exercised the
  uplift; and non-UK regimes.
* **R08 flag message** — the three playbook jurisdictions' equivalents.
* **R09 flag message** — the substantive real estate regimes.
* **R10 flag message** — the EU-side characterisation and suitability wording.
* **R13 `currency_mismatch_fx` note** — the allocation of conversion risk.

No other rule string carries a `[VERIFY]`. In particular R12's and R14's notes no longer do.

---

## 6. Lowest-confidence items, in priority order

1. **R01 is the weakest rule in the file now.** It fires on a trust borrower — a core private-wealth
   fact pattern, and one of WP9's golden deals — and the only thing standing behind its central
   assertion (that the trustee's indemnity is what connects the trust assets to the debt, and that
   limited recourse is acceptable only where the indemnity is intact) is general practice. Its one
   verified source is a filed agreement supporting the *document* asks, not the indemnity analysis.
   This is where WP5's "everything is unsourced" problem still lives.
2. **R05's independent-advice point.** Same shape, one level less exposed because the ask is cheap
   and standard. The register has carried this gap since WP7 and nobody has closed it. Both R01 and
   R05 need a textbook or an authority, which no agent in this build has had access to.
3. **The two concentration thresholds.** 25 per cent and 50 per cent drive a floor tightening and a
   credit escalation respectively, and neither is observed anywhere: the published bank terms in the
   pool deliberately avoid a numeric single-name cap and use diversification-as-an-input instead.
   These are credit-policy numbers wearing a rule's clothes. Of everything in the file, these are the
   most likely to be wrong *and* the most likely to be noticed.
4. **R08 is built on a US resale rule.** The playbook's jurisdictions are England, Switzerland and
   Luxembourg. The message is now written to describe the shape rather than to assert the law, and
   says so, but a reader could still take it as a statement of English or Swiss law. This is WP8's
   lowest-confidence item 2, inherited unchanged.
5. **R07's threshold figures are in euros in a retained-UK instrument.** The legislation.gov.uk text
   read gives EUR 5,000 / EUR 20,000. Whether that is the operative onshored figure, and whether the
   uplift has been exercised, is unconfirmed — and it is exactly the kind of detail an interviewer
   would probe.
6. **R14 now asserts criminal-law consequences from a German-language official text.** The research
   agent read the German text because no English version was located at that identifier. The
   penalties and the survival of the duty are stated confidently on that basis. Grade A and opened,
   but translated by the reader.
7. **R04 is no longer the least certain statement in the rule set** — that was WP5's §6.1 headline
   and it is now resolved: reg 3 was read, the point is the non-natural-person gate, and the flag
   says so. What remains genuinely uncertain is narrower and correctly scoped (whether *this* deal's
   arrangement is inside, given the parties and the possession-or-control test). **The flag's id
   remains misleading** — `fca_safe_harbour_uncertain` reads as a conduct-regulator point and is not
   one. WP8 recorded the same objection and kept the id for compatibility. The rename to
   `fcar_safe_harbour_uncertain` is mechanical (flag id, R04's `flag:` value, any clause reference)
   and should be done once the concurrent clause agents are finished.

---

## 7. Files this work package touched

```
playbook/rules/rules.yaml                 sources replaced; messages/notes/rationales per §4
playbook/clauses/24_currency_mismatch_fx.yaml   regulatory_flags: [emir_awareness] added (§8)
tests/test_engine.py                      one assertion relaxed (§3)
docs/source_register.md                   new "## Sources — WP5b rules" section, rows only
handoff/WP5b.md                           this file
```

Nothing else was written. The concurrent WP3 group A/C/D clause files were not touched.

---

## 8. Note on the clause path in the instruction

The instruction named `playbook/clauses/23_currency_mismatch_fx.yaml`. That file does not exist:
`23_` is `information_undertakings` and the currency clause is **`24_currency_mismatch_fx.yaml`**.
Creating a `23_currency_mismatch_fx.yaml` would have produced a duplicate clause id, so the flag
list was added to `24_`, which is the clause the instruction meant. It stays a stub otherwise — no
`not_automated`, no positions, no sources, `status: stub`.

```yaml
regulatory_flags:
  - emir_awareness
```

The loader accepts it: `sbl validate` exits 0 with 24 clauses, and
`load_library().clauses['currency_mismatch_fx'].regulatory_flags` is `['emir_awareness']` with
`status` still `stub`. This closes WP8's design note that `emir_awareness` was defined but
referenced by nothing and could therefore never appear in any output. It is an awareness reference
only: the clause holds no position on derivatives and the intake captures no derivative facts, so
the flag prints where that clause prints and nothing computes from it.
