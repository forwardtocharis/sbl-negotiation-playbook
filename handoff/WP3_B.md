# Hand-off: WP3 drafting group B

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP3 for three of the core twelve clauses.
Everything in the repository is synthetic. Nothing here is legal advice. All three entries are
`status: draft`; nothing was set to `reviewed`; no `verified` flag was changed from what the shared
source pool records.

Clauses drafted (stub files overwritten in place, file names and ids unchanged):

| # | file | id |
|---|---|---|
| 03 | `playbook/clauses/03_eligible_collateral_lending_values.yaml` | `eligible_collateral_lending_values` |
| 04 | `playbook/clauses/04_concentration_limits.yaml` | `concentration_limits` |
| 05 | `playbook/clauses/05_lender_discretion_valuation.yaml` | `lender_discretion_valuation` |

Also written: `docs/research/source_register_B.md` (fragment; records that **no new sources** were
added, and one search that was deliberately not used). No other file in the repository was touched.

---

## 1. Acceptance output (pasted verbatim)

### 1.1 `.venv/Scripts/python -m sbl validate`

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: c3e07566e59371ffc685942eba6460614cd2ef8d1427a48f3f1e71d1364830de
exit code: 0
```

Exits 0. The rule count was 0 in WP1's hand-off and is 18 here, because the WP5 agent is writing
`rules.yaml` concurrently; that is not a failure and nothing in it blocked this work package.

### 1.2 Group B assertion script

Script lives in the session scratchpad (`check_group_b.py`), not in the repository, per the brief.
It asserts per file: `status == draft`; four tiers each with non-empty `text` and `rationale`;
fallback carries an `approval`; `unacceptable` carries no `conditions`; >= 3 sources with >= 1 of
reliability A or B; >= 2 `counterparty_asks`; all three `jurisdiction_notes` keys present and
non-empty; every `depends_on` id exists as a clause file; every `regulatory_flags` id exists in
`playbook/flags/regulatory_flags.yaml`; >= 1 `not_automated` item; `reviewed_by` and `last_reviewed`
null.

```
$ .venv/Scripts/python <scratchpad>/check_group_b.py
03_eligible_collateral_lending_values.yaml: id=eligible_collateral_lending_values status=draft tiers=4 sources=8 (A=4, B=3, C=1) asks=6 depends_on=5 flags=2 not_automated=4 default_floor=fallback
04_concentration_limits.yaml: id=concentration_limits status=draft tiers=4 sources=9 (A=3, B=5, C=1) asks=5 depends_on=4 flags=3 not_automated=4 default_floor=fallback
05_lender_discretion_valuation.yaml: id=lender_discretion_valuation status=draft tiers=4 sources=9 (A=2, B=5, C=2) asks=5 depends_on=4 flags=3 not_automated=4 default_floor=fallback

All group B assertions passed.
exit code: 0
```

### 1.3 Denylist grep — **not empty; read this**

The brief asks for an empty result. The raw grep is **not** empty, for two reasons, neither of which
is a real-name leak. Raw output first:

```
$ grep -n -i -E "societe|generale|ubs|credit suisse|julius|pictet|lombard odier|barclays|hsbc|coutts|goldman|morgan|citi|edmond|vontobel|efg|bnp|deutsche" playbook/clauses/03_*.yaml playbook/clauses/04_*.yaml playbook/clauses/05_*.yaml
playbook/clauses/03_eligible_collateral_lending_values.yaml:147:  - collateral_substitution
playbook/clauses/03_eligible_collateral_lending_values.yaml:188:    url: "https://www.ubs.com/content/dam/assets/microsites/credit-suisse/static/doc/lombardkredit-factsheet-en.pdf"
playbook/clauses/04_concentration_limits.yaml:70:      eligible collateral, repay or substitute collateral within the cure period in the margin maintenance
playbook/clauses/04_concentration_limits.yaml:191:    url: "https://www.ubs.com/content/dam/assets/microsites/credit-suisse/static/doc/lombardkredit-factsheet-en.pdf"
playbook/clauses/05_lender_discretion_valuation.yaml:166:    failure to comply does not unwind an appropriation but allows the court to substitute a compliant
playbook/clauses/05_lender_discretion_valuation.yaml:239:    note: "Law-firm note on the 2022 English High Court decision ... substitute a compliant valuation ..."
```

1. **False positives.** `ubs` is a substring of `substitution`, `substitute`, `subsidiary`,
   `substantial`. Three of the six hits are ordinary English words. Any later agent running this
   check should use word boundaries.
2. **Publisher domains inside `url:` fields.** Two hits are the Swiss factsheet URL for `BANK-CH-01`,
   copied verbatim from `docs/research/clause_sources.md`. `build_plan.md` §0 rule 2 expressly permits
   a publisher's domain inside a URL while requiring labels and notes to be neutral, and the WP3
   brief instructs drafters to copy the pool's structured entries including the URL. A third URL,
   `https://www.privatebank.citibank.com/we-offer/margin-lending` (`BANK-US-01`, cited in clause 05),
   is the same situation but does not trip the raw grep because `citi` has no word boundary inside
   `citibank`.

Word-boundary grep with `url:` lines excluded — this is the check that actually answers the question
"is there a real name in the drafted content?":

```
$ grep -v -E "^\s*url:" playbook/clauses/0[345]_*.yaml | grep -n -i -E "\b(societe|generale|ubs|credit suisse|julius|pictet|lombard odier|barclays|hsbc|coutts|goldman|morgan|citi|edmond|vontobel|efg|bnp|deutsche)\b"
(no output; exit 1)
```

Clean. Every ref label used is neutral (`BANK-CH-01`, `BANK-US-01`, `EDGAR-PB-01`, ...), no bank,
firm, client or party name appears in any title, clause text, rationale, condition, comment or source
note, and the only real-world name of any kind in the drafted content is the English 2022
appropriation decision, which is referred to descriptively ("the 2022 English High Court decision on
appropriation under the financial collateral regulations") rather than by party name.

**Recommendation for the WP9/WP10 agent:** make the repo-wide denylist check word-boundary aware and
exclude `url:` lines, or it will report false failures on every clause file in the library.

---

## 2. Least-confident positions, for Stuart's review priority

Two per clause, in the order I would review them.

### 03 `eligible_collateral_lending_values`

1. **`fallback` — fixing lending value percentages for named holdings for X months.** This concession
   shape is **not observed in any source**. No document opened concedes a fixed grid at all; I built
   the shape by analogy with the one notice-period concession in the pool (`EDGAR-PB-01-B`,
   15 days with carve-outs) and applied its carve-out logic to a fixing period. It is commercially
   plausible and it is the ask counterparties actually make, but it is an invention of structure and
   should be read as a proposal, not as a market position.
2. **`fallback` — the independent-valuer mechanic for assets that are not exchange-listed.** `FIRM-01`
   supports appraisal and dispute rights only for *private-company* collateral in margin loans. I
   extended it to any asset valued off an issuer-reported NAV, which is a wider class, and I kept the
   final determination with the Bank to limit the damage. Worth checking whether a private bank would
   ever offer this at all rather than simply excluding the asset.
3. (Third, close behind.) The **currency haircut of X percentage points** in `preferred`. No opened
   source publishes an FX haircut figure. The mechanism is sound and `build_plan.md` R13 assumes it,
   but the number is pure risk appetite.

### 04 `concentration_limits`

1. **`acceptable` — carrying the excess over the single-name limit at a reduced lending value instead
   of disregarding it.** No source supports either treatment as the market norm; I chose the reduced
   percentage because it makes the portfolio behave sensibly as prices move, but the harder and
   simpler "excess is disregarded" is at least as defensible and would make the `preferred` /
   `acceptable` gap cleaner.
2. **`fallback` — giving up insufficient diversification as a stand-alone realisation trigger.** The
   published Luxembourg template retains *both* the fee lever and the liquidation trigger
   (`BANK-LU-01`), so this concession gives away something a real bank document holds. The judgement
   that it is survivable rests entirely on the margin mechanics delivering the same outcome a step
   later. If you disagree, this belongs in `unacceptable`, not `fallback`, and `default_floor` for the
   clause should move to `acceptable`.

### 05 `lender_discretion_valuation`

1. **`fallback` — the notice period of X business days.** The entire number rests on a single
   observation: one sub-part of one composite private-bank filing (`EDGAR-PB-01-B`) conceding 15 days.
   Three other published documents concede nothing. 15 days is also long for this product. I would
   expect the real institutional answer to be materially shorter, but I have no source for a shorter
   number and did not want to invent one.
2. **`fallback` — the "a margin call is outstanding and uncured" carve-out.** This is the carve-out I
   am least sure the Bank can hold, because "no change while a call is open" is an **explicitly
   observed counterparty ask** in the pool and it sounds reasonable in the room. My view is that it is
   the most important of the four carve-outs and should be the last to go, which is why it is also in
   the `unacceptable` tier and in `escalation_triggers`. That is a deliberate, arguable choice.
3. (Third, close behind.) Including `consumer_credit` in `regulatory_flags`. A unilateral variation
   right exercised against an individual borrower is obviously where a consumer regime would bite, but
   I have no source for that proposition, so the file asserts nothing about it — the flag is only a
   sensitivity link. Drop it if you think the link overstates.

---

## 3. Every `[VERIFY]` introduced

No `[VERIFY]` was added to a statement of law that a source in the pool already supports. The
`[VERIFY]` markers fall into three groups.

**(a) Numbers. Every `X` in these three files is a judgement number and is marked in the comment
above the field it appears in.**

| file | `X` | what the comment records |
|---|---|---|
| 03 | currency haircut, percentage points (`preferred`) | no opened source publishes an FX haircut figure |
| 03 | review interval (`acceptable`) | no opened source states a fixed review interval; sources say "at regular intervals" |
| 03 | fixing period in months, notice period in business days, appraisal frequency (`fallback`) | no opened source concedes a fixed grid; nearest analogue is 15 days' notice with carve-outs |
| 03 | fixing period in `escalation_triggers` | institution's own tolerance |
| 04 | single-name cap %, group/sector/currency cap % (`preferred`) | **no numeric single-name cap in any source opened** |
| 04 | single-name cap %, reduced lending value % (`acceptable`) | same |
| 04 | cap %, fixing period, notice period (`fallback`) | same |
| 04 | threshold in `escalation_triggers` | `build_plan.md` R06 (>25%) and R06b (>50%) are **uncorroborated by any opened source** |
| 05 | notice period in business days (`fallback`) | anchored on a single observation of 15 days (`EDGAR-PB-01-B`); three other documents concede none |
| 05 | notice period in `escalation_triggers` | same |

**(b) The known gap the brief names.** `04_concentration_limits.yaml` opens with a ten-line
`[VERIFY]` header comment stating in terms that no numeric single-name cap appears in any source
opened, listing what *was* found instead (regulator naming single-stock and undiversified collateral
with no cap; bank terms using diversification as an input, a fee lever and a liquidation trigger;
the institutional answer being a lower LTV plus a same-class negative pledge), and stating that
R06 / R06b's 25% and 50% are the institution's own risk appetite and must not be presented as market
observations. That instruction is repeated in the clause's `not_automated`.

**(c) In-text `[VERIFY]` prefixes.**

- `05` → `jurisdiction_notes.luxembourg`: the statement that Luxembourg practice is to specify the
  agreed valuation method in the security agreement (art. 11(1)(a) pricing on appropriation). This
  comes from the WP7 research file, not from a document this agent opened; the sentence is prefixed
  `[VERIFY]`, names its provenance, and the `LAW-LU-01` source note says explicitly which part of the
  note it does and does not support. The rest of that note rests on art. 11(1)(e)-(f), which the pool
  records as read.
- `04` → `jurisdiction_notes.england_wales` is the literal brief-mandated string
  `"No jurisdiction-specific variation identified [VERIFY]"`. It is the only one of the nine
  jurisdiction notes across the three clauses where I could not identify a genuine variation.

No source entry's `verified` value was upgraded. Every source is copied from the pool with the pool's
own grade and `verified` value, and every source `note` was rewritten to say what that source supports
**in this clause** rather than being copied blind.

---

## 4. Deviations from the plan or schema, and why

1. **Denylist grep is not empty.** §1.3 above. Two causes, both benign; recommendation included.
2. **`default_floor: fallback` on all three clauses.** The brief allows `acceptable` where conceding
   to fallback should always escalate. I used `fallback` throughout for a structural reason as well as
   a drafting one: `build_plan.md` §4 rules R06, R06b, R13 and R15 all *tighten* floors on these three
   clauses to `acceptable`, and a rule can only move a floor up. A default floor of `acceptable` would
   make those four rules no-ops on every deal. If Stuart decides `concentration_limits` should default
   to `acceptable` (see §2), R06's `set_floor concentration_limits=acceptable` becomes inert and WP5
   should be told.
3. **Clause 04's fallback approver is `credit committee`, not `senior lawyer` or `head of credit`.**
   Grandfathering a concentration breach and surrendering the diversification liquidation trigger is a
   risk-appetite decision, not a legal one. Clauses 03 and 05 use `head of credit` for the same reason.
4. **`lender_objective` rewritten on all three** (WP1 §5.5 invites this). `category` (`collateral`),
   `title`, `id` and file names are unchanged. `document: facility_letter` and `risk_rating: high` were
   assigned to all three: the eligible-collateral schedule, the concentration limit and the discretion
   right all live in the facility letter, with the security agreement only capturing the assets.
5. **`depends_on` includes deferred stubs.** Clause 03 depends on `currency_mismatch_fx` and
   `collateral_substitution`, both of which exist as `status: stub` files. The loader accepts this and
   `sbl validate` is green; flagged because the markup (WP6) will print a `[STUB]` tag next to them.
6. **Clause 05 carries an unusually long header comment.** It sets out the notice-period / threshold
   trade-off as a ladder in six lines, because the brief identifies this as an anticipated interview
   question and the comment is the fastest way to reload the argument before answering it. It is a
   comment, so it never reaches the rendered markup.
7. **No new sources added.** Everything is from the shared pool. One search for a numeric single-name
   cap was run and deliberately not used; see `docs/research/source_register_B.md` for the query, the
   result and the reasoning, so the next agent does not repeat it and reach a different conclusion.
8. **Case law is cited descriptively, never by party name** ("the 2022 English High Court decision on
   appropriation under the financial collateral regulations"), with the law-firm note's URL carrying the
   traceability. This keeps §0 rule 2 clean on its face. If Stuart would rather have the neutral
   citation in the text, it is in `FIRM-02`'s entry in `docs/research/clause_sources.md`.

---

## 5. One note for the WP5 and WP6 agents

Clause 05's `fallback` tier is the only place in group B's clauses where the *content* of the position
changes with a rule rather than just the tier: R13 (currency mismatch) sets its floor to `acceptable`,
which has the effect of withdrawing the notice period entirely on any mismatched deal. That is the
intended behaviour and the rationale text is written so it reads correctly when the markup prints the
ladder with the floor raised. No engine change is needed; recording it so nobody "fixes" it.
