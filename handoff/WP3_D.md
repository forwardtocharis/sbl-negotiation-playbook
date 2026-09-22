# Hand-off: WP3 drafting group D

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP3 for three of the core twelve clauses.
Everything in the repository is synthetic. Nothing here is legal advice. All three entries are
`status: draft`; nothing was set to `reviewed`; no `verified` flag was changed from what the
source file it came from records.

Clauses drafted (stub files overwritten in place, file names and ids unchanged):

| # | file | id |
|---|---|---|
| 08 | `playbook/clauses/08_events_of_default.yaml` | `events_of_default` |
| 11 | `playbook/clauses/11_governing_law_jurisdiction.yaml` | `governing_law_jurisdiction` |
| 12 | `playbook/clauses/12_no_advice_non_reliance.yaml` | `no_advice_non_reliance` |

Also written: `docs/research/source_register_D.md` (fragment; records that **no new sources** were
opened and **no search was run**, and gives the label mapping for nine sources carried across from
the WP7 research file). No other file in the repository was touched.

---

## 1. Acceptance output (pasted verbatim)

### 1.1 `.venv/Scripts/python -m sbl validate`

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 3a0003eaadacba98e348a3d6ca8dc4ed1b7fe71264ec8af26a8394d138a7e7d2
exit code: 0
```

Exits 0. The `library_hash` differs from the one in group B's hand-off, and moves again on every
run, because other WP3 drafting groups and the WP5 agent are writing to `rules.yaml`, `tests/` and
other clause files concurrently. That is expected, not a failure. A re-run after this hand-off was
written gave `c503ee43bf66ab70b6872b3097da93840941ab1fe37232eecaab2daf092335b8`, also exit 0, with
the same clause / rule / flag / jurisdiction counts.

### 1.2 Group D assertion script

Script lives in the session scratchpad (`check_group_d.py`), not in the repository, per the brief.
It asserts per file: `status == draft`; `reviewed_by` and `last_reviewed` null; exactly the four
tiers, each with non-empty `text` and `rationale`; `fallback` carries an `approval`; `unacceptable`
carries neither `conditions` nor `approval`; >= 3 sources with >= 1 of reliability A or B; >= 2
`counterparty_asks`; all three `jurisdiction_notes` keys present and non-empty; every `depends_on`
id exists as a clause file; every `regulatory_flags` id exists in
`playbook/flags/regulatory_flags.yaml`; >= 1 `not_automated` item; >= 1 `escalation_triggers` item.

```
$ .venv/Scripts/python <scratchpad>/check_group_d.py
08_events_of_default.yaml: id=events_of_default status=draft tiers=4 sources=10 (A=3, B=5, C=2) asks=6 depends_on=5 flags=3 not_automated=5 default_floor=fallback
11_governing_law_jurisdiction.yaml: id=governing_law_jurisdiction status=draft tiers=4 sources=10 (A=6, B=4) asks=6 depends_on=4 flags=2 not_automated=5 default_floor=fallback
12_no_advice_non_reliance.yaml: id=no_advice_non_reliance status=draft tiers=4 sources=11 (A=4, B=6, C=1) asks=6 depends_on=4 flags=2 not_automated=5 default_floor=fallback

All group D assertions passed.
exit code: 0
```

### 1.3 Denylist check — **empty, as required**

The brief's word-boundary-aware check, ignoring `url:` lines:

```
$ grep -v -i "url:" playbook/clauses/08_events_of_default.yaml playbook/clauses/11_governing_law_jurisdiction.yaml playbook/clauses/12_no_advice_non_reliance.yaml \
  | grep -n -i -w -E "societe|generale|ubs|credit suisse|julius|pictet|lombard odier|barclays|hsbc|coutts|goldman|morgan|citi|citibank|edmond|vontobel|efg|bnp|deutsche"
(no output; exit 1)
```

Clean. For completeness, the **raw** grep without word boundaries and without excluding `url:`
lines returns 13 hits across the three files, every one of which is a false positive of the kind
group B identified:

* eleven are the substring `ubs` inside ordinary English words. Counted across the three files:
  `substitute` ×5, `substantial` ×5, `substantive` ×1 — eleven occurrences on eleven distinct
  lines, plus the single genuine occurrence inside a URL below;
* two are publisher domains inside `url:` fields in clause 12 (`BANK-CH-01` and `BANK-US-01`),
  copied verbatim from `docs/research/clause_sources.md` as the brief instructs. `build_plan.md` §0
  rule 2 expressly permits a publisher's domain inside a URL. (`citi` inside `citibank` in the
  second of those URLs does not trip a word-boundary grep, which is why the raw count is 13 and not
  14.)

**No party names from filed agreements appear.** Every filed document is described by what it is
plus its EDGAR accession number; every bank-published document is described generically ("a
published Lombard loan agreement template of a Luxembourg bank", "a global private bank"). No
case is cited by party name anywhere in these three files; the one judicial reference (clause 08's
Switzerland note) is descriptive — "a Geneva appellate decision is cited for the proposition
that…" — with the practitioner note's URL carrying the traceability.

**Recommendation for the WP9 / WP10 agent** (repeating group B's, because it is still true): make
the repo-wide denylist check word-boundary aware and exclude `url:` lines, or it will fail on
almost every clause file in the library for the word "substantial".

---

## 2. Least-confident positions, for Stuart's review priority

Two per clause, in the order I would review them.

### 08 `events_of_default`

1. **`fallback` — the death standstill of X business days.** This is the single weakest position in
   group D's three files. **No source opened concedes any standstill on death at all.** The
   published Luxembourg template keeps death of the client as a free-standing ground for unilateral
   realisation *without prior notice*; the filed private-bank document accelerates without notice or
   demand on the death or incompetence of any person in its defined class. I built the standstill
   because it is the ask a private bank will actually receive from an estate-planning adviser and
   because refusing it outright reads badly, and I conditioned it hard (no open margin call, lending
   value at or above outstandings, representatives engaging). But it is an invention of structure,
   not a market position, and if Stuart disagrees it belongs in `unacceptable`, not `fallback`.
2. **`acceptable` — the functional narrowing of "Relevant Person".** The observed private-bank
   drafting defines the population by *status* and reaches any beneficial owner or settlor of the
   borrower, pledgor, guarantor or collateral provider. I narrowed it by *function* — any individual
   whose death or incapacity would affect the ability to perform or the Bank's ability to deal with
   the collateral, with a settlor with reserved powers, a sole trustee and a joint account holder
   given as examples. That is a cleaner and more defensible line, and it is also a line the Bank
   has to be able to apply at intake. If it cannot, the status-based definition is safer and this
   concession should move down a tier.
3. (Third, close behind.) Including `fca_safe_harbour_uncertain` in `regulatory_flags`. The link is
   real — the English natural-person exclusion changes what enforcement looks like after a death or
   a personal bankruptcy — but it is a sensitivity link, not an assertion, and the file asserts
   nothing beyond what `LAW-EW-01` and s.285 support. Drop it if you think it overstates.

### 11 `governing_law_jurisdiction`

1. **`fallback` — conceding mutual exclusive jurisdiction.** Every private-bank document opened for
   this playbook **refuses** this: all four reserve the lender's right to sue at the client's
   domicile or elsewhere. So this tier concedes something no document in the pool concedes. My
   argument that it is survivable rests entirely on the carve-out — the Bank can still act anywhere,
   immediately, for interim relief and to preserve or realise the collateral — and on the
   observation that in two of the three jurisdictions the proprietary law is assigned by statute and
   was never negotiable anyway. If you think the asymmetry is the thing that actually gets the Bank
   paid, this belongs in `unacceptable` and the clause's `default_floor` should move to
   `acceptable`.
2. **`preferred` — splitting the governing law between the facility letter (booking location) and
   the security agreement (account location).** This is *legally* the right answer and I am
   confident in the conflicts analysis, which is sourced to primary text. What I am not confident
   about is whether it matches what private banks actually do: the source pool's own observation is
   that the market **standardises on one law for the whole package** and handles local-law questions
   by opinion rather than by splitting. I have drafted against the observed convention on purpose
   and said so in the rationale, but a reviewer may reasonably prefer the single-law structure with
   a local-law opinion as a condition precedent.
3. (Third, close behind.) `risk_rating: high` and `document: all`. Both are departures from the
   obvious reading of a clause the plan files under `boilerplate`. See §4.

### 12 `no_advice_non_reliance`

1. **`fallback` — trading the sophisticated-investor limbs for a documented suitability file.**
   **No source opened concedes either of the two asks this tier answers**, and no source describes
   the suitability-file-as-consideration trade. The private-bank document takes all three limbs
   flat. I think the trade is right — a file the Bank can produce is worth more than a
   representation the Bank may not be able to rely on — but it is a proposal about how the Bank
   should run the relationship, not an observation about how this market documents it. The `X days`
   for the age of the assessment is pure process appetite with no observed analogue.
2. **`unacceptable` — refusing any contractual duty to warn of an impending shortfall.** I am
   confident this is the right line for an execution-only relationship and much less confident it
   can be held as drafted on a Swiss booking, where a practitioner note records that a bank acting
   as discretionary manager or adviser may owe a notification duty **independently of the
   contract**. I drafted the refusal as a refusal to *create* a contractual duty rather than as a
   denial that one can exist, and said so in `jurisdiction_notes.switzerland`, but the wording needs
   a Swiss reviewer's eye before it is put in front of a Swiss client.
3. (Third, close behind.) The `acceptable` tier's express saving for duties that cannot be excluded,
   and the sentence that nothing in the clause is to be read as a statement that the Bank has not
   provided a service it in fact provided. Both are lender-side *restraint* rather than lender-side
   protection, and both are unsourced as drafting. I believe they make the clause more useful, not
   less; a reviewer may think they give away an argument for nothing.

---

## 3. Every `[VERIFY]` introduced

No `[VERIFY]` was added to a statement that a source already supports. The markers fall into three
groups.

**(a) The three known gaps the brief names, each stated in terms.**

| gap | where it is marked | what the file says |
|---|---|---|
| Swiss governing-law / jurisdiction practice | 11: header comment (a 10-line `[VERIFY]` block) and `jurisdiction_notes.switzerland` | The shared pool contains **no** Swiss governing-law or jurisdiction clause source at all; the Swiss material is a product factsheet, the regulator's risk monitor, an industry risk booklet and a practitioner note on margin calls. The Swiss *conflicts rules* in the note are sourced to primary text (PILA, Hague Convention, HCCH status table) and are a different question from market practice; the entry says so and says nothing should be presented as observed Swiss practice. |
| Incapacity short of death | 08: header comment, `jurisdiction_notes.switzerland`, `not_automated` | Death is well sourced from three angles. Incapacity is covered only by the word "incompetent" in one filed private-bank document and by the Luxembourg statute treating death and incapacity of the collateral provider alike. No mental-capacity law and no power-of-attorney analysis was opened. **Every statement about incapacity in the file is `[VERIFY]`.** |
| MiFID II primary text for suitability | 12: header comment, `sources` entry with `verified: false` | The EU-side characterisation of such lending as an ancillary service and the EU-side suitability wording are unsourced and confined to the header comment. The substantive notes rest on the UK regulator's handbook and on FinSA, both of which the WP7 research agent read. The FinSA articles the research verified (arts. 3(c)(5), 10, 12, 13, 14) are used as verified. |

**(b) One further `[VERIFY]` I introduced on my own initiative.**

* **11 — enforceability of asymmetric jurisdiction clauses.** That private banks use them is
  observed in four documents in the pool. Whether a given forum gives effect to a clause that binds
  the client to one court while leaving the Bank free to sue anywhere was not sourced. Marked
  `[VERIFY]` in a header comment and carried onto `not_automated`. The clause text still takes the
  asymmetric position at `preferred`, because that is what the documents do; what is marked is the
  proposition that it will work.
* **08 — the English consequences of the FCAR natural-person exclusion.** The exclusion itself is
  sourced (`LAW-EW-01`); the *consequences* (bills of sale legislation, charge registration, what
  the market actually does for individual pledgors) are not, and the note says so and points at the
  `fca_safe_harbour_uncertain` flag.
* **12 — the effect of contractual non-reliance / basis-of-dealing wording under English law.** Not
  sourced; the entry asserts nothing about whether such wording operates as an estoppel.

**(c) Numbers. Every `X` is a judgement number with the observed range in a comment above the field.**

| file | `X` | what the comment records |
|---|---|---|
| 08 | payment grace on interest and fees (`acceptable`) | observed 1–2 business days (`EDGAR-ML-03`) |
| 08 | involuntary insolvency dismissal window (`acceptable`) | observed 30 days (`EDGAR-ML-03`) |
| 08 | cross-default threshold amount (`acceptable`) | **no opened source states a number** |
| 08 | general covenant cure (`fallback`) | observed 30 days (`EDGAR-ML-03`) |
| 08 | change-of-control percentage (`fallback`) | observed 50% (`EDGAR-ML-04`) |
| 08 | trading-suspension period (`fallback`) | observed only as "beyond a set number of trading days"; **no published number** (`FIRM-01`) |
| 08 | change-of-law notice before realisation (`fallback`) | observed 10 calendar days (`EDGAR-PB-01-B`) |
| 08 | **death standstill (`fallback`)** | **NOT OBSERVED IN ANY SOURCE.** The comment says so in capitals and points at this hand-off. |
| 08 | grace / cure / standstill thresholds in `escalation_triggers` | institution's own tolerance |
| 11 | process agent replacement period (`preferred`) | observed only "renewed annually" (`EDGAR-PB-01-B`); no replacement period published |
| 11 | replacement period in `escalation_triggers` | institution's own choice |
| 12 | age of the suitability assessment before first drawing (`fallback`) | no opened source states a period; the nearest adjacent observed number is a 14 calendar day withdrawal right on a distance contract (`BANK-LU-01`) |
| 12 | same period in `escalation_triggers` | institution's own process tolerance |

No source entry's `verified` value was upgraded. Every source is copied with the grade and
`verified` value recorded in the file it came from, and every `note` was rewritten to say what that
source supports **in this clause** rather than being copied blind.

---

## 4. Deviations from the plan or schema, and why

1. **Nine sources are carried across from `docs/research/jurisdictions_research.md`, not from the
   shared pool, and they carry `verified: true`.** The brief says `verified: true` only where "the
   pool" records the source as opened. These nine are not in the pool; they are in the WP7 research
   file, which the brief separately and expressly directs group D to use for `jurisdiction_notes`
   (PRIMA / Hague / PILA / FISA, and the MiFID II / FinSA notes). That file records each of them as
   read in primary text at the URL given. Marking a genuinely-opened primary text as unverified
   would be the less honest of the two options, so I carried the flag across **and** wrote the
   provenance into every affected `note`: *"Opened and read by the WP7 research agent …; not opened
   by this drafting agent, and carried across with that provenance."* All nine are already rows in
   `docs/source_register.md`; the label mapping is in `docs/research/source_register_D.md`. If
   Stuart prefers the strict reading, the fix is mechanical — flip those nine to `verified: false`
   and prefix the sentences they support with `[VERIFY]` — and it would affect the substance of
   only the Switzerland note in clause 11 and the England and Wales note in clause 12.
2. **`default_floor: fallback` on all three clauses,** for the structural reason group B gives and
   for a clause-specific one. `build_plan.md` R11 tightens `events_of_default` to `acceptable` on a
   committed term facility and R10 tightens `no_advice_non_reliance` to `acceptable` where the
   purpose is to acquire securities. A default floor of `acceptable` would make both rules no-ops on
   every deal. Both files carry a header comment saying this, so nobody "fixes" it later.
3. **The R11 interaction is argued in clause 08's `fallback` rationale, not just noted.** The
   argument is: on an uncommitted facility the events of default are not the Bank's only exit,
   because the Bank can demand repayment without a default at all — so the enumerated-MAC
   substitution and the death standstill are survivable. Once the facility is committed, that
   backstop is gone and the events of default *are* the exit, which is exactly why the rule closes
   the floor. The `fallback` conditions make "the facility is uncommitted" the first condition, so
   the clause and the rule say the same thing from two directions.
4. **Clause 11 is `document: all`, not `facility_letter`.** It is the only clause in group D where
   the choice is substantive rather than cosmetic: the whole point of the entry is that the facility
   letter's governing law and the security agreement's governing law are different questions with
   different answers, and filing the clause under one document would contradict its own content.
5. **Clause 11 is `risk_rating: high` despite `category: boilerplate`.** The category is WP1's and I
   left it (it drives grouping in the markup only). The risk rating is mine: every cross-border
   perfection and enforceability conclusion in this playbook hangs off this clause and sits on the
   not-automated register, which is not a boilerplate risk profile. If Stuart would rather the
   category matched, `default_enforcement` would be the honest home for it.
6. **Clause 12's `approval` is `senior lawyer and compliance`, not a single role.** Conceding the
   advised-relationship carve-out is a legal decision about drafting and a conduct decision about
   whether the suitability file will actually exist, and the `mifid_suitability` flag's
   `who_decides` is `compliance`. Clause 08 uses `head of credit` (the death standstill and the
   cure periods are risk appetite) and clause 11 uses `senior lawyer` (forum and immunity are legal
   judgements). If WP1's suggestion of an approver enum is ever taken up, this is the string that
   will need splitting.
7. **`lender_objective` rewritten on all three** (WP1 §5.5 invites this). `id`, `category`, `title`
   and file names are unchanged on all three.
8. **`depends_on` includes deferred stubs.** Clause 08 depends on `cross_collateral_set_off` and
   clause 12 on `purpose_restrictions`, both `status: stub`. The loader accepts this and `sbl
   validate` is green; flagged because WP6's markup will print a `[STUB]` tag next to them.
9. **Clauses 08 and 11 carry long header comments** (26 and 35 lines). Both are there because the
   clause has a single load-bearing idea that is hard to reconstruct under pressure: for 08, that
   the three fights (who is caught / what counts / how long) are separable and only the margin-call
   limb is non-negotiable; for 11, that the contractual governing law and the proprietary law of
   intermediated securities are different questions, and which of the three jurisdictions lets you
   choose the second one. They are comments, so they never reach the rendered markup.
10. **No new sources, and no search run at all.** See `docs/research/source_register_D.md` for the
    three gaps I deliberately did not try to fill and why.

---

## 5. Notes for the WP5, WP6 and WP9 agents

* **Clause 08 and rule R11.** R11 currently does `set_floor events_of_default = acceptable` plus two
  notes. The clause is drafted so that the note R11 adds ("expect the borrower to attack the MAC
  wording… check that the margin shortfall event stands on its own and is not qualified by a
  materiality test") reads correctly next to the `acceptable` tier, which is where the floor lands.
  No engine change is needed. Recording it so nobody rewrites the note.
* **Clause 12 and rule R10.** Same pattern: R10 sets this clause's floor to `acceptable`, which has
  the effect of withdrawing the advised-relationship carve-out on any acquire-securities deal. That
  is the intended behaviour — the carve-out is exactly the concession you should not be making on
  the deal where the suitability flag has fired — and the `fallback` rationale is written so it
  still reads correctly when the markup prints the ladder with the floor raised.
* **Clause 11 and the deal fixtures (WP9).** Clause 11's `escalation_triggers` include "any deal in
  which the collateral account is maintained outside England and Wales, Switzerland or Luxembourg".
  The `Intake` model has `collateral.custodian_location` as a free ISO country code and
  `collateral.governing_law` with an `other` member, so a deal booked outside the three is
  representable. There is **no rule** in §4 that fires on it. If that trigger is meant to bite
  automatically rather than being read by a human, WP5 needs a rule for it; as drafted it is a
  prompt in the markup, which I think is the right level.
* **Group D asserted nothing about the `escalation_triggers` → rules relationship** beyond that
  one. All other triggers in these three files are human-read prompts by design.
