# Hand-off: WP7 (jurisdiction overlay) — YAML half

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP7, the YAML half only.
The research half is `docs/research/jurisdictions_research.md` and `handoff/WP7_research.md`.

Everything in the repository is synthetic. Nothing here is legal advice. No entry has been set to
`reviewed`; `reviewed_by` and `last_reviewed` are null in all three files. Every legal statement is
lifted from the research file, paraphrased, and carries the sources the research recorded for it.

---

## 1. Acceptance output (pasted verbatim)

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 8aaa41bfe806aba151feaef9308c125d76881ffb2760ab665490e07875874ee8
validate exit=0
```

```
$ .venv/Scripts/python -m sbl validate --summary
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 8aaa41bfe806aba151feaef9308c125d76881ffb2760ab665490e07875874ee8

kind              stub   draft  reviewed   total
------------------------------------------------
clauses             21       3         0      24
rules                0      18         0      18
flags                0      10         0      10
jurisdictions        0       3         0       3

Entries not marked 'reviewed' have not been checked by a named human reviewer.
validate --summary exit=0
```

```
$ .venv/Scripts/python -m pytest tests/test_flags_jurisdictions.py -q
....................                                                     [100%]
20 passed in 2.26s
```

The library hash moves on every write by any agent, so the value above is the one current when this
hand-off was written, not a fixed property of WP7.

WP7's plan acceptance also asks that R04 and R14 reference the file content correctly and that the
markup prints the correct file per governing law. Both belong to other agents' files (`rules.yaml`,
`markup.py`) and were not written here. What can be said from this side: `rules.yaml` at the time of
writing contains `R04_natural_person_pledgor_england` raising `fca_safe_harbour_uncertain` at medium
and `R14_swiss_booking` raising `bank_secrecy_data` at low, which is what the research recommends,
and both flag definitions are now written to match.

---

## 2. What was written

```
playbook/jurisdictions/england_wales.yaml     status: draft, 14 sources
playbook/jurisdictions/switzerland.yaml       status: draft, 10 sources
playbook/jurisdictions/luxembourg.yaml        status: draft,  4 sources
docs/source_register.md                       new section "Sources — WP7 and WP8", 40 rows appended
tests/test_flags_jurisdictions.py             new, 20 tests (shared with WP8)
handoff/WP7.md, handoff/WP8.md                these notes
```

No file outside that list was touched. `src/sbl/`, `playbook/rules/rules.yaml`,
`playbook/clauses/*` and the rest of `tests/` belong to concurrent agents.

Each file carries the seven required fields as folded scalars of roughly four to seven sentences,
written lender-side, plus `sources`, `status: draft`, `reviewed_by: null`, `last_reviewed: null`.

**The `Jurisdiction` model was sufficient — no field was missing and `models.py` was not touched.**
Two pieces of content that do not have a field of their own were put into `practical_notes` and are
flagged here so a reader knows where to look: the Swiss bank secrecy and data protection point
(note 6, with the substance in the `bank_secrecy_data` flag) and the Swiss conduct-perimeter point
that lending to finance transactions in financial instruments is itself a financial service
(note 7, with the substance in the `mifid_suitability` flag).

`financial_collateral_regime` states the natural-person question explicitly in each file, in the
same words each time so the three are comparable when printed side by side: England — natural-person
collateral providers are **NOT** covered; Switzerland — natural persons **ARE** covered, but an
individual is not a qualified investor so the pre-realisation notice cannot be waived; Luxembourg —
natural-person collateral providers **ARE** covered, subject to the over-indebtedness carve-out and
subject to the `[VERIFY]` below.

---

## 3. Every `[VERIFY]` in the three files

| file | field | the statement carrying `[VERIFY]` |
|---|---|---|
| luxembourg.yaml | `financial_collateral_regime` | That natural persons are within the scope of the 2005 law is an inference from the primary text ("merchant or a non-merchant" plus the over-indebtedness carve-out), not an express scope provision; the law has no scope article naming eligible persons. Must be confirmed by Luxembourg counsel. |
| luxembourg.yaml | `sources` | `[VERIFY] LU-NATPERS-01` — the corroborating article was seen in search results but never opened; `url` recorded, `verified: false`. |
| england_wales.yaml | `practical_notes` (6) | The independent-legal-advice / undue-influence practice point for a third-party non-commercial pledgor is stated from general practice and is not sourced to authority. |
| england_wales.yaml | `sources` | `[VERIFY] UK-ILA-01` — placeholder source for the above, `url: null`, `retrieved: null`, `verified: false`. |

Two further hedges are written into the text without the literal `[VERIFY]` token, because they are
qualifications of a sourced statement rather than unsourced statements, and they are the same two
points the research agent lists as its own lowest confidence items:

* `switzerland.yaml` / `governing_law_of_intermediated_securities` — the closing sentence says the
  qualifying-office condition is a real constraint and that the point has not been seen applied to a
  facility of this kind, so the operational use of it is for local counsel.
* `switzerland.yaml` / `practical_notes` (4) — the closing clause says that translating "value can be
  determined objectively" into an asset-class test (listed liquid yes; gated funds, structured
  products and unlisted no) is judgement rather than law.

All `[VERIFY]` items carried in the research but belonging to the consumer credit, suitability and
market abuse material are in `handoff/WP8.md`, not here.

---

## 4. Three lowest-confidence statements per file

### england_wales.yaml

1. **`practical_notes` (6), independent legal advice for a third-party pledgor.** Unsourced practice
   statement, marked `[VERIFY]`. It is also the one place in the file where a reader might take the
   overlay as advice on how to protect a security against undue influence, which is exactly the kind
   of conclusion the not-automated register reserves for a human.
2. **`creation`, the characterisation point.** The statement that a clause drafted as a general lien
   over intangible custody assets was analysed as a charge comes from a law-firm briefing (grade C)
   reporting a 2012 decision, not from the judgment. The briefing was read; the judgment was not.
   The decision is cited by neutral citation only, because naming the parties would put a real
   institution's name in playbook text.
3. **`registration_filing`, "register protectively wherever there is any doubt".** This is a
   commercial recommendation rather than law, and a bank with a settled policy on protective
   registration may take a different line. The underlying legal statements (the 21-day period, the
   voidness consequence and the disapplication) are all sourced at grade A.

### switzerland.yaml

1. **`enforcement_route` / `practical_notes` (3), that private realisation survives the provider's
   insolvency.** The article text was read and is unambiguous, but it sits against the general debt
   enforcement rule that pledged assets fall into the estate and private enforcement stops. The file
   presents the intermediated securities act as the specific rule overriding the general one, which
   is the orthodox reading, but the practitioner overview that was read does not spell the
   interaction out and a bank would not enforce on this analysis alone.
2. **`governing_law_of_intermediated_securities`, fixing the proprietary law by agreement.** The
   chain is sound article by article, but it has not been seen applied to a facility of this kind
   and the qualifying-office condition is stated only in summary. The structural conclusion — that
   Switzerland differs from the English and Luxembourg account-location rule — is solid; the
   operational advice to use it is not.
3. **`practical_notes` (4), the asset-class translation of "objectively determinable value".**
   Judgement dressed as a test. It matters because it decides whether appropriation or sale is the
   realistic route for gated funds, structured products and unlisted positions, which is exactly the
   collateral the illiquid-collateral rule is about.

### luxembourg.yaml

1. **`financial_collateral_regime`, natural persons in scope.** The load-bearing contrast with
   England and the whole reason the overlay is worth printing per governing law. It rests on an
   inference from two provisions rather than an express scope article, and the corroborating source
   was never opened. Highest priority of anything in WP7 for Stuart or Luxembourg counsel.
2. **`enforcement_route`, enforcement without prior notice as the default.** The article was read and
   says it, but the whole of Art. 11(1) opens with "unless otherwise provided for", so the default is
   only as good as the drafting, and the file's advice to keep a negotiated notice period out of the
   security agreement is a negotiating position, not law.
3. **`perfection_depends_on`, the custodian ranking waiver.** The statement that routes (ii) to (iv)
   are treated as a waiver by the custodian of its own pledge ranking unless otherwise agreed or
   notified is taken from the primary text, but the practical effect on a third-party custodian that
   has its own general terms lien was not tested against any custodian's actual terms, and the
   briefing that was read is silent on it.

---

## 5. Notes for the next work packages

* **Markup (WP6).** The three fields worth printing for every deal, because the three jurisdictions
  genuinely diverge on them, are `registration_filing`, `enforcement_route` and
  `financial_collateral_regime`. `perfection_depends_on` converges on "control through the custodian"
  in all three and could be summarised once.
* **Third-party custodian condition precedent (R12).** Concrete, sourced CP text exists in all three
  files: England — an account control agreement that delivers dispossession in substance;
  Switzerland — a control agreement plus a waiver or subordination of the custodian's statutory
  retention and foreclosure right; Luxembourg — the three-party or notified two-party agreement,
  noting it is treated as the custodian waiving its own ranking.
* **Do not promote any of these to `reviewed`.** Two of the three files carry a `[VERIFY]` in a
  substantive field, and the Luxembourg scope point should be confirmed by counsel before the file is
  used to support a position in a negotiation.
* **Institution names.** No real institution is named in any of the three files. Publisher names
  appear only inside `url` values, which is what `tests/test_flags_jurisdictions.py` enforces by
  stripping URLs before matching the denylist.
