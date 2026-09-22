# Hand-off: WP3 drafting group C

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP3 for three of the core twelve clauses.
Everything in the repository is synthetic. Nothing here is legal advice. All three entries are
`status: draft`; nothing was set to `reviewed`; no `verified` flag was changed from what the shared
source pool or the WP7 research file records.

Clauses drafted (stub files overwritten in place, file names, ids and categories unchanged):

| # | file | id | category |
|---|---|---|---|
| 06 | `playbook/clauses/06_margin_maintenance_cure.yaml` | `margin_maintenance_cure` | collateral |
| 07 | `playbook/clauses/07_security_structure_control.yaml` | `security_structure_control` | collateral |
| 09 | `playbook/clauses/09_enforcement_liquidation.yaml` | `enforcement_liquidation` | default_enforcement |

Also written: `docs/research/source_register_C.md` (fragment; records that **no new sources were
opened**, and maps the neutral ref labels this group assigned to sources the WP7 agent had already
opened). No other file in the repository was touched.

---

## 1. Acceptance output (pasted verbatim)

### 1.1 `.venv/Scripts/python -m sbl validate`

Final run, after the `[VERIFY]` edits described in §3 were applied:

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: c503ee43bf66ab70b6872b3097da93840941ab1fe37232eecaab2daf092335b8
validate exit code: 0
```

Exits 0. **One transient failure is worth recording**, because it was not in group C's files and a
later agent may hit it again. An intermediate run, while another agent was mid-write, produced:

```
FAIL: 1 problem found loading the playbook library:
  - playbook/clauses/10_capacity_authority.yaml [capacity_authority]: field 'counterparty_asks.0': Input should be a valid string
validate exit code: 1
```

That is clause 10, which belongs to another drafting group, and the next run of the same command was
green with no change to any group C file. It is a partially-written file caught mid-save, not a
library defect. The `library_hash` moves between runs for the same reason: other agents are writing
`playbook/` concurrently — three green runs during this work package produced three different hashes
(`f3440320…`, `e60c01e4…`, `c503ee43…`) with no change to any group C file between the second and
third. Treat the hash above as "green at the time of writing", not as a library version to pin.

### 1.2 Group C assertion script

Script lives in the session scratchpad (`check_group_c.py`), not in the repository, per the brief.
It asserts per file: `status == draft`; `reviewed_by` and `last_reviewed` null; four tiers each with
non-empty `text` and `rationale`; `fallback` carries an `approval`; `unacceptable` carries no
`conditions` and no `approval`; >= 3 sources with >= 1 of reliability A or B and every source
carrying a note; >= 2 `counterparty_asks`; >= 1 `not_automated` item; >= 1 `escalation_triggers`
item; `jurisdiction_notes` keys exactly match the jurisdiction files present and none is empty;
every `depends_on` id exists as a clause id; every `regulatory_flags` id exists in
`playbook/flags/regulatory_flags.yaml`; `default_floor` is a concedable tier. Final run, after the `[VERIFY]` edits:

```
$ .venv/Scripts/python <scratchpad>/check_group_c.py
06_margin_maintenance_cure.yaml: id=margin_maintenance_cure status=draft tiers=4 sources=16 (A=5, B=9, C=2) asks=6 depends_on=6 flags=3 not_automated=5 default_floor=fallback
07_security_structure_control.yaml: id=security_structure_control status=draft tiers=4 sources=13 (A=4, B=7, C=2) asks=6 depends_on=6 flags=3 not_automated=5 default_floor=fallback
09_enforcement_liquidation.yaml: id=enforcement_liquidation status=draft tiers=4 sources=15 (A=6, B=6, C=3) asks=6 depends_on=5 flags=3 not_automated=6 default_floor=fallback

All group C assertions passed.
script exit code: 0
```

### 1.3 Denylist check — empty, as required

Run exactly as the brief specifies (word-boundary aware, `url:` lines excluded):

```
$ grep -v -i "url:" playbook/clauses/06_margin_maintenance_cure.yaml playbook/clauses/07_security_structure_control.yaml playbook/clauses/09_enforcement_liquidation.yaml \
  | grep -n -i -w -E "societe|generale|ubs|credit suisse|julius|pictet|lombard odier|barclays|hsbc|coutts|goldman|morgan|citi|citibank|edmond|vontobel|efg|bnp|deutsche"
(no output; exit 1)
```

For completeness, without the `url:` exclusion the same grep returns two lines, both of them
publisher domains inside `url:` fields copied verbatim from `docs/research/clause_sources.md`
(`BANK-US-01` and `BANK-CH-01`, both cited in clause 06). `build_plan.md` §0 rule 2 permits a
publisher's domain inside a URL. Group B reached the same conclusion and recommended the
word-boundary-plus-url-exclusion form of the check; this hand-off supports that recommendation.

**Party and firm names from source documents.** Checked separately and clean:

```
$ grep -v -i "url:" playbook/clauses/0[679]_*.yaml \
  | grep -n -i -E "lehman|g-t-p|f2g|aapico|abt auto|clifford|chance|mayer|brown|baer|karrer|addleshaw|simpson|thacher|stblaw|delen|garanti|bbva|finma|mondaq|practical law|swissbanking"
(no output; exit 1)
```

Case law and firms are referred to descriptively throughout ("the 2022 English High Court decision on
appropriation of collateral under the financial collateral regulations"; "the 2010 and 2012 English
decisions"; "a Geneva appellate decision"; "practitioner overview of lending and taking security in
Switzerland"), with traceability carried by the URL in the `sources` block. Regulators are named by
role, not by acronym ("Swiss regulator risk monitor 2025", "CSSF-supervised", which is a supervisory
status and not a bank name).

---

## 2. Least-confident positions, for Stuart's review priority

Two per clause, in the order I would review them, plus a third where it is close behind.

### 06 `margin_maintenance_cure`

1. **`fallback` — the cure extension bought with a written cure plan.** The only observed extension in
   the entire pool is the capital-call standstill in a fund-borrower margin loan (`EDGAR-ML-02`): the
   borrower delivers a capital call confirmation package and gets extra time while the call runs. I
   generalised that into "a written cure plan with an identified, committed funding source". That is a
   real leap: in private wealth the funding source is usually a property sale, a bonus, a distribution
   or another bank, none of which is confirmable the way a capital call is. If Stuart thinks the Bank
   would in practice say no and then forbear informally rather than contract for this, the right answer
   is to move this tier to `unacceptable` and set `default_floor: acceptable` — and, if so, tell the WP5
   agent, because R06's `set_floor margin_maintenance_cure=acceptable` becomes inert.
2. **`acceptable` — the Hard Floor (`Z per cent`) as a carve-out from the cure period.** Exactly one
   source has a two-level structure with a "no notice at all below this" level: a Luxembourg private
   bank's general conditions (`BANK-LU-02`, calling at 130 per cent of outstandings and realising
   without notice below 120 per cent). The institutional documents have a *release* level below the
   maintenance level, which is a different thing — it governs getting collateral out, not enforcing.
   So the Hard Floor may be a Luxembourg retail construct that I have promoted to an architectural
   feature of the clause. It is commercially right in my view, but it rests on one document.
3. (Third, close behind.) **The unit convention.** I expressed the Trigger Level and Restoration Level
   as the Lending Value *as a percentage of outstandings* (the cover convention, following
   `BANK-LU-02` and `EDGAR-PB-01-A`), not as an LTV. Clauses 03, 04 and 05 talk in lending value
   percentages. Both conventions appear in the sources, but the library should pick one, and a reader
   comparing clause 04's caps with clause 06's levels will otherwise have to convert in their head.

### 07 `security_structure_control`

1. **`fallback` — accepting a two-party pledge plus a custodian acknowledgement instead of a tripartite
   control agreement.** This is an express statutory perfection route in Luxembourg (art. 5(2)(a)(ii)
   of the Law of 5 August 2005) and it is why I was willing to draft the tier at all. It almost
   certainly does *not* travel: the English case law requires real dispossession of the provider, and
   the Swiss route is an agreement *between the account holder and the custodian* under FISA art. 25,
   which is a different instrument from an acknowledgement given to the Bank. I handled that by
   conditioning the whole tier on a written local counsel confirmation, which is honest but may be too
   clever — the cleaner design may be a fallback that is expressly available in Luxembourg, unavailable
   in England, and re-shaped in Switzerland. That would need a jurisdiction-conditional position, which
   the frozen schema does not have (see §4.3).
2. **`fallback` — the substitution allowance of `Y per cent` of Lending Value per month without the
   Bank's consent.** No source opened concedes uncontrolled substitution; the private-bank documents
   refuse it outright and one asserts full dominion with no withdrawals permitted at all. What the
   Luxembourg statute gives (art. 2(3)) is that a retained substitution right does not *undermine* the
   pledge — which protects the Bank if it grants the right, and says nothing about whether it should.
   The shape and the number are both mine.
3. (Third, close behind.) **The `preferred` tier reserving a right of use.** I drafted the Bank as
   reserving the right to use or dispose of the collateral to the extent the law and any authorisation
   permit. No opened source shows a private bank reserving rehypothecation over private-client
   collateral, and the one filed document on point has the lender conceding the opposite
   (`EDGAR-PL-02`). It may simply be off-market for this product, in which case delete the sentence
   from `preferred` — which also makes the `acceptable` tier's no-reuse covenant a cheaper concession
   to explain.

### 09 `enforcement_liquidation`

1. **`fallback` — the notice period of `X business days` before any sale.** The whole tier rests on one
   sub-document of one composite private-bank filing (`EDGAR-PB-01-B`, five business days). Every other
   document opened concedes no notice at all for sales generally, and the two shorter observations
   (three days, three business days) apply only where notice is required by law, which is the
   `acceptable` tier. The carve-outs I am confident about; the number is a single observation.
2. **`acceptable` — pairing a "commercially reasonable manner" covenant with the full set of pre-agreed
   acknowledgements of what *is* commercially reasonable.** No source opened has both in that
   combination: the document with the acknowledgements pairs them with a discretion standard
   (`EDGAR-PL-02`), and the documents with the commercially-reasonable standard do not have the
   acknowledgements. My view is that they are complementary — the standard governs the manner, the
   acknowledgements define the manner in advance — and the English authority that only the *manner*
   need be reasonable supports that reading. But a counterparty's lawyer may reasonably argue the list
   guts the standard, and a court might read the two as inconsistent. This is the position in group C's
   three clauses most in need of a lawyer's eye rather than a credit officer's.
3. (Third, close behind.) **`approval: credit committee` on the fallback tier**, where clauses 06 and
   07 use `head of credit` and `senior lawyer`. Reasoning in §4.2; it is arguable either way.

---

## 3. Every `[VERIFY]` introduced

Two kinds. No `[VERIFY]` was added to a statement a source in the pool already supports, and no
source entry's `verified` value was upgraded.

### (a) Statements of law — five in-text `[VERIFY]` prefixes

| clause | where | what is marked and why |
|---|---|---|
| 06 | `jurisdiction_notes.england_wales` | The *consequence* of the financial collateral regulations' natural-person exclusion: that the Bank is left enforcing under an express contractual power of sale, subject to the equitable duty to obtain a proper price. The scope rule itself (reg. 3: both parties non-natural persons) is **not** marked — it was read in the primary text by the WP7 agent. The consequence comes from `docs/research/jurisdictions_research.md` and the WP3 brief names it as a known gap. |
| 07 | `jurisdiction_notes.england_wales` | The same point in its structural form: that the registration exemption, the insolvency disapplications and appropriation are all unavailable where the provider is an individual. |
| 09 | `jurisdiction_notes.england_wales` | The same point in its enforcement form: that there is no self-help appropriation in English law outside the regulations. The note says in terms that this is the single most important thing to check before the clause is promoted beyond draft, because it decides whether the appropriation route in the drafting works at all for a private client. |
| 09 | `jurisdiction_notes.switzerland` | The working conclusion that FISA art. 31(1)(b)'s "value determined objectively" means listed liquid lines qualify for appropriation while gated funds, structured products and unlisted holdings do not. The statutory words are sourced; the asset-class mapping is a practice inference drawn in the WP7 file, not in the statute. |
| 07 | `jurisdiction_notes.england_wales` (parenthetical) | Not a `[VERIFY]` but recorded here for completeness: the point that a true common-law pledge is awkward over intangible custody assets, so English custody security is drafted as mortgage or charge language, is attributed in the note to commentary (`FIRM-04`) rather than to statute. |

In each case the corresponding `LAW-EW-01` source note was rewritten to state what reg. 3 **does**
support and to say explicitly that it does **not** support the marked sentence. That is the same
treatment group B gave `LAW-LU-01` in clause 05.

### (b) Numbers — every `X`, `Y`, `Z` and `N` is a judgement number with a comment above the field

| clause | symbol | what the comment records |
|---|---|---|
| 06 | `X per cent` Trigger Level, `Y per cent` Restoration Level (`preferred`) | The four observed level architectures, with refs. Two documents give real numbers, both from one jurisdiction each; the institutional documents redact theirs into side letters. |
| 06 | `X business days` cure period, `Z per cent` Hard Floor (`acceptable`) | The full observed cure ladder (1 / 2 / 3-on-certificate / 5 business days, plus "a couple of business days" and Swiss practice of not more than two), placing `X` in a 2–5 business day band. The 1 business day written-statement deadline is **not** an `X`: it is taken from the only source that states one. |
| 06 | `N` additional business days (`fallback`) | No private-bank document opened concedes any extension; the only observed extension is the capital-call standstill. `N` is pure risk appetite. |
| 06 | `X business days` in `escalation_triggers` | Same ladder; the institution's own tolerance. |
| 07 | `X business days` for the custodian's acknowledgement, `Y per cent` monthly substitution allowance (`fallback`) | **No opened source publishes either figure.** Stated as such in the comment, in `escalation_triggers` and in `not_automated`. |
| 09 | `X business days` (`acceptable`) | Observed 3 days and 3 business days, in both cases only where notice is required by law, both with the carve-outs retained. |
| 09 | `X business days` (`fallback`) | Observed 5 business days in one sub-document, with the carve-outs retained; every other document concedes none. |
| 09 | `X business days` in `escalation_triggers` | Same, with an explicit warning that Luxembourg's 8 working days' press notice is the **public auction formality**, not a negotiated notice period, and must not be read as market evidence for a longer notice. |

### (c) Known gaps from the brief that group C did **not** state

Group C makes no statement about numeric single-name concentration caps, a lending-value grid by
asset class, trustee powers or limited recourse, Swiss governing-law/jurisdiction practice,
incapacity short of death, or MiFID II / FinSA suitability. Where clause 06 and clause 09 need a
concentration concept they refer to "the concentration limit" as a defined term in clause 04 rather
than restating a number.

---

## 4. Deviations from the plan or schema, and why

1. **`default_floor: fallback` on all three clauses.** Structural, and the same reasoning group B
   gave: `build_plan.md` §4 rules R06 (concentration), R07 (insider/PDMR), R08 (restricted
   securities), R12 (third-party custodian) and R15 (illiquid collateral) all *tighten* floors on
   these three clauses to `acceptable`. A default floor of `acceptable` would make every one of those
   rules a no-op. If Stuart moves any of these to `acceptable` on the merits, WP5 must be told which
   rule has gone inert.
2. **Three different fallback approvers.** Clause 06 uses `head of credit` (the concession is time,
   and time is priced in the lending value). Clause 07 uses `senior lawyer` (the concession is the
   form of the custodian's agreement and whether the security is effective, which is a legal
   conclusion, not a risk-appetite one). Clause 09 uses `credit committee`, because its fallback tier
   concedes two things at once — a universal notice period with a direct credit cost, and a narrowing
   of the pre-agreed standard-of-conduct acknowledgements with a direct legal cost — and neither a
   lawyer nor a credit officer owns both halves. Arguable; see §2.
3. **No jurisdiction-conditional positions, because the schema has none.** Clause 07's `fallback` and
   clause 09's `preferred` are both genuinely jurisdiction-dependent: the two-party-pledge route is a
   statutory route in Luxembourg and probably not available in England, and the no-notice enforcement
   position is simply unavailable on a Swiss booking to a private client, because FISA art. 32(1)
   notice cannot be waived by anyone who is not a custodian or a qualified investor, and a natural
   person is neither. The frozen schema (`docs/schema_notes.md` §3) has one ladder per clause and a
   `jurisdiction_notes` string per jurisdiction, so I put the constraint in the jurisdiction note and
   in the tier's `conditions` rather than forking the ladder. **This is the one place where a reader
   of the markup could take the printed opening position and be wrong on a Swiss deal**, and it is
   the strongest argument I found for a future `jurisdiction_overrides` field. I did not add one: the
   schema is frozen and another agent is editing the models.
4. **`document` assignments.** Clause 06 is `facility_letter` (the levels and the cure clock are
   commercial terms). Clauses 07 and 09 are `security_agreement`. Clause 07 arguably spans
   `account_control` as well, and `all` was available; I used `security_agreement` and made the
   control agreement a condition precedent inside the text, because that is where the obligation to
   produce it actually bites. Change it to `all` if the markup should list the clause under the
   control agreement too.
5. **`risk_rating: high` on all three**, with >= 4 `not_automated` items each, per the brief's
   requirement for high-risk clauses.
6. **`lender_objective` rewritten on all three** (WP1 §5.5 invites this). `id`, `title`, `category`
   and file names unchanged.
7. **Long header comments on all three files.** Clause 06's sets out the two-axis structure (levels
   vs cure ladder); clause 07's sets out the form-vs-control distinction and the per-jurisdiction form
   answer; clause 09's sets out the three axes and names the rules that tighten its floor. They are
   comments, so they never reach the rendered markup, and they exist because these are the three
   clauses where an interview question is most likely to require reloading the argument quickly.
8. **No new sources opened.** See `docs/research/source_register_C.md`, including the three searches
   deliberately not run and why, so a later agent does not repeat them and reach a different answer.
   That file also maps the eight neutral ref labels this group assigned to WP7's sources, and flags a
   possible `FIRM-04` / `FIRM-05` label collision for the merging agent.

---

## 5. Notes for the WP5, WP6 and WP9 agents

**5.1 The cure clock and the enforcement clock are drafted as consecutive, not cumulative.** This is
stated in the text of every tier of clause 06 and in the `fallback` of clause 09: expiry of the cure
period is an Event of Default, and any enforcement notice runs *from* that expiry. It is not
housekeeping — a counterparty reading the two clauses in isolation will add them together and believe
it has bought a much longer standstill than the Bank has sold. If the markup ever renders these two
clauses far apart, consider a `note` action linking them, or a WP6 cross-reference line. The
`depends_on` edges are already there in both directions (`margin_maintenance_cure` →
`enforcement_liquidation` and back).

**5.2 R07 and R08 tighten `enforcement_liquidation` to `acceptable`, and the clause is written so
that reads correctly.** The `acceptable` tier's rationale explains the logic explicitly: on an
insider deal or a restricted-securities deal, the sale is already slowed by closed periods, issuer or
underwriter consents and volume limits, so a universal notice period on top of that is the concession
the Bank cannot afford; and an enforcement on those facts is the one most likely to be challenged,
which is when the pre-agreed commercial-reasonableness acknowledgements matter most. R15 (illiquid
collateral) tightens the same floor for the related reason that appropriation needs an objectively
determinable value. No engine change is needed; recording it so nobody reads the tightening as
backwards and "fixes" it.

**5.3 R06 tightens `margin_maintenance_cure` to `acceptable`,** which has the effect of withdrawing
the cure extension entirely on a concentrated deal. That is the intended behaviour and the rationale
text is written to read correctly when the markup prints the ladder with the floor raised.

**5.4 For the golden deals (WP9).** D02 (trust, 70 per cent single stock, settlor PDMR, England law)
exercises the most interesting path in group C's clauses: R06 and R06b tighten clause 06, R07
tightens clause 09, and clause 09's England note prints a `[VERIFY]` about the natural-person
exclusion — but D02's pledgor is a trust, so whether that `[VERIFY]` is even in point depends on
whether the trustee is a corporate trustee. That is exactly the fact-dependence the
`fca_safe_harbour_uncertain` flag exists to surface, and it would make a good thing to point at on
screen during the walkthrough. D04 (third-party Lux custodian) is the deal that exercises clause 07's
`acceptable` tier and R12.
