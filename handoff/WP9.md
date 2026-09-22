# Hand-off: WP9 (golden deals, snapshots, end-to-end tests, check script)

Agent hand-off, 2026-09-21. Covers `build_plan.md` §5, §6 WP9 and §9, plus the
managing-agent flag-id rename.

Everything written here is synthetic. Nothing is legal advice. No entry was set
to `reviewed`. No new legal statement and no new source was written by this work
package: the six deals are fact patterns, not law, and the tests assert engine
behaviour, not propositions about any regime.

---

## 1. Acceptance output (pasted verbatim)

### `powershell -ExecutionPolicy Bypass -File check.ps1` — exits 0

```
=== SBL Negotiation Playbook Demonstrator: check ===
interpreter: .venv\Scripts\python

--- 1/3  sbl validate ---
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 5752d729a3dff7423c13d6b99f6021ab3662a1175ad60049c069b9bc5347247d

--- 2/3  pytest -q ---
........................................................................ [ 18%]
........................................................................ [ 36%]
........................................................................ [ 55%]
........................................................................ [ 73%]
........................................................................ [ 92%]
...............................                                      [100%]
391 passed in 40.27s

--- 3/3  sbl run (each deal into runs/) ---
D01 run 5b2b9dba5123 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 0 escalations | exit 0 | wrote D01_5b2b9dba5123.json, D01_5b2b9dba5123.md, audit.jsonl
D02 run 975ab2d753b8 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 1 flags | 2 escalations | exit 2 | wrote D02_975ab2d753b8.json, D02_975ab2d753b8.md, audit.jsonl
D03 run 36f1ae193480 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 0 escalations | exit 0 | wrote D03_36f1ae193480.json, D03_36f1ae193480.md, audit.jsonl
D04 run bf056fed8e13 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 1 flags | 1 escalations | exit 2 | wrote D04_bf056fed8e13.json, D04_bf056fed8e13.md, audit.jsonl
D05 run 6dc1888589e1 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 3 flags | 1 escalations | exit 2 | wrote D05_6dc1888589e1.json, D05_6dc1888589e1.md, audit.jsonl
D06 run c0e8c3778648 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 1 escalations | exit 2 | wrote D06_c0e8c3778648.json, D06_c0e8c3778648.md, audit.jsonl

=== summary ===

Stage                       Expected           Actual Result
-----                       --------           ------ ------
sbl validate                exit 0             exit 0 PASS
pytest -q                   exit 0             exit 0 PASS
D01_plain_vanilla           exit 0             exit 0 PASS
D02_trust_concentrated_pdmr exit 2 (escalates) exit 2 PASS
D03_swiss_corporate_purpose exit 0             exit 0 PASS
D04_third_party_pledge_lux  exit 2 (escalates) exit 2 PASS
D05_real_estate_hard_stop   exit 2 (escalates) exit 2 PASS
D06_below_floor_request     exit 2 (escalates) exit 2 PASS

OK: 8 checks passed.
Demonstrator built from public sources. Synthetic deals. Not legal advice.

SCRIPT EXIT=0
```

### `sh check.sh` — the POSIX twin, also exits 0

Same three stages, same expected table, same `exit 0`. Run under Git Bash; it
picks up `.venv/Scripts/python.exe` on Windows and `.venv/bin/python`
elsewhere, falling back to `python3` then `python` on PATH.

### `python -m sbl validate --summary` — exits 0

```
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 5752d729a3dff7423c13d6b99f6021ab3662a1175ad60049c069b9bc5347247d

kind              stub   draft  reviewed   total
------------------------------------------------
clauses             12      12         0      24
rules                0      18         0      18
flags                0      10         0      10
jurisdictions        0       3         0       3

Entries not marked 'reviewed' have not been checked by a named human reviewer.
exit=0
```

### Test counts

391 tests at the time of this run, of which WP9 adds 148: 82 in
`tests/test_golden_deals.py` and 66 in `tests/test_denylist.py`. The denylist
figure is not stable and is not meant to be — most of it is one parametrised
case per scanned file, so it moves whenever `docs/` gains or loses a file. It
was 70 an hour earlier, before WP10a consolidated four research files into
`docs/source_register.md`. The total moves with it.

---

## 2. Step 0: the flag-id rename, exactly what moved

`fca_safe_harbour_uncertain` → `fcar_safe_harbour_uncertain`. The old id read as
a point about the conduct regulator; the flag is about the Financial Collateral
Arrangements (No. 2) Regulations 2003, so the prefix is now `fcar_`. Flagged as
a naming risk in `handoff/WP7_research.md` and `handoff/WP5b.md`; decided by the
managing agent; implemented here.

### Renamed (12 occurrences, 10 files)

| file | occurrences | what |
|---|---|---|
| `playbook/flags/regulatory_flags.yaml` | 1 | the `id:` itself, plus the description rewrite below |
| `playbook/rules/rules.yaml` | 1 | R04's `flag:` value |
| `playbook/clauses/07_security_structure_control.yaml` | 1 | `regulatory_flags` entry |
| `playbook/clauses/08_events_of_default.yaml` | 2 | `regulatory_flags` entry + one prose mention in a jurisdiction note |
| `playbook/clauses/09_enforcement_liquidation.yaml` | 1 | `regulatory_flags` entry |
| `playbook/clauses/11_governing_law_jurisdiction.yaml` | 1 | `regulatory_flags` entry |
| `tests/fixtures/runresult_escalated.json` | 1 | WP6 renderer fixture |
| `tests/fixtures/runresult_escalated.expected.md` | 1 | WP6 renderer fixture |
| `tests/test_engine.py` | 2 | R04 assertions |
| `tests/test_flags_jurisdictions.py` | 1 | expected flag-id list |

The flag's `name`, `trigger_summary`, `who_decides` (senior lawyer), all four
sources and its `status: draft` are unchanged. The description's opening
sentence, which used to say the id was "a legacy label kept for compatibility …
and it is misleading", now says the id **was corrected in WP9 from an earlier
`fca_` label** and that hand-off notes written before WP9 use the superseded
label for the same flag. The substance of the description — regulation 3, the
non-natural-person scope test, what is lost and what the lender does instead —
is untouched.

### Deliberately **not** renamed

* `build_plan.md` (§4 rule table and §4 flag list, two mentions). It is the
  plan as written, not a live artefact; renaming it would rewrite the record of
  what was specified.
* `handoff/WP1.md`, `WP3_C.md`, `WP3_D.md`, `WP3_sources.md`, `WP5b.md`,
  `WP7.md`, `WP7_research.md`, `WP8.md`. History, as instructed.
* **`docs/source_register.md` (4 mentions) and
  `docs/research/jurisdictions_research.md` (1 mention).** WP9 does not own
  `docs/` and a WP10a agent was writing there concurrently. **These are now
  stale and should be updated by whoever next edits `docs/`.** They are
  "attributed to" columns and a section heading, so nothing turns on them, but
  they point at an id that no longer exists.
* `docs/schema_notes.md` does not mention the flag; checked, nothing to do.

### Effect on the library hash

The rename touches four `playbook/` files, so it changes `library_hash`, which
is a sha256 over the playbook YAML. Reverting only the id (leaving everything
else as it is now) gives `c9e7c936…`; the current value is `5752d729…`. No
pre-WP9 hash was captured before the edit, so the full delta cannot be
attributed to the rename alone — WP3/WP7/WP8 content also landed in between.

`sbl validate` and the full 243-test suite were green immediately after the
rename and before any WP9 content was written, as instructed.

---

## 3. §5 expectations vs. what the rule set actually produces

Every row below is asserted in `tests/test_golden_deals.py` **as actual
behaviour**, with the divergence named in the test's docstring. Nothing was
weakened to make a test pass.

| deal | §5 says | actual | rule responsible | verdict |
|---|---|---|---|---|
| D01 | "consumer_credit flag at medium" | `consumer_credit` at medium **and** `fcar_safe_harbour_uncertain` at medium | R03b (consumer_credit); **R04** (the second flag) | §5 undercounts. D01's borrower is a natural person and the security is English law, which is exactly R04's trigger. The extra flag is correct; §5 did not anticipate that the clean deal would still raise one. Asserted, including the exact set of two, so silencing R04 fails a test. |
| D01 | "all clauses at default floor" | true | — | Holds. Neither R03b nor R04 has a `set_floor` action; both only add notes. Asserted against the floors read from the library, not a hard-coded list. |
| D02 | "R01, R06, R06b, R07 fire" | all four fire, and nothing else | R01, R06, R06b, R07 | Holds. The test also asserts the set is *exactly* those four. |
| D02 | "escalations >= 2" | exactly 2 | R06b (to credit), R07 (to senior lawyer + compliance) | Holds. |
| D02 | (implicit) R06b tightens `margin_maintenance_cure` | recorded as `R06b_concentration_severe (no change)` on that clause | R06b | Not a divergence, but worth knowing: R06b's `set_opening margin_maintenance_cure: preferred` is a no-op because the opening is already `preferred`. The engine still logs the rule, with the `(no change)` suffix. Asserted. |
| D03 | "R02, R10, R11, R13, R14 fire" | all five, and nothing else | — | Holds. |
| D03 | no exit code given | **exit 0** | none of the five escalates | §5 is silent. Recorded here and in `check.ps1` / `check.sh`: D03 is the second clean deal. A cross-border, committed, purpose-driven deal that does not escalate is a genuine result, not an omission. |
| D04 | "R03 … fire" | **R03a** fires (R03b does not) | R03a | §5 predates WP5's split of R03 into R03a (no declaration: high, escalates) and R03b (declaration on file: medium, no escalation). D04's borrower has neither declaration, so R03a is the one. |
| D04 | "consumer_credit flag" | `consumer_credit` at **high**, and it **escalates** | R03a | §5's D04 row gives no severity and does not mention an escalation. See §4 below — this is the item the managing agent asked to be confirmed and recorded honestly. |
| D04 | "R05 … fire" | R05 fires; **R05b does not** | R05 / R05b | R05b needs `pledgor.type == corporate`; D04's pledgor is the borrower's spouse, an individual. Asserted both ways. |
| D04 | "require_cp account control" | R12 appends it to `conditions_precedent`, not to a clause called "account control" | R12 | Not a divergence in substance — the CP text is the account control agreement — but note the CP lands on `conditions_precedent`, which is where every CP lands. |
| D05 | "markup header says out of scope" | the **escalations table**, immediately under the header, carries R09's reason "Real estate collateral is outside the scope of this playbook"; R09's note "Real estate is out of scope for this playbook" appears on `eligible_collateral_lending_values` and `enforcement_liquidation` | R09 | The renderer has no separate header warning line, so "header" is read as "the top block: header plus escalations". Both wordings are asserted, and the test asserts the first appears *before* the `## Flags` heading. |
| D05 | (implicit) real estate changes the positions | R09 sets **no floor at all**; D05's floors are identical to D01's | R09 | Deliberate in R09's design: the tool stops rather than repricing a deal it was not built for. Asserted. |
| D06 | "first request accepted within floor and logged" | `margin_maintenance_cure` at `fallback` vs floor `fallback` → `accepted_within_floor`, with an R16 note naming tier, floor and approver | R16 (engine built-in) | Holds. Note the acceptance depends on nothing tightening `margin_maintenance_cure` on D06 — if a future rule raised that floor to `acceptable`, the same request would become `below_floor_escalated`. The test asserts the floor as well as the outcome, so that change would be visible. |
| D06 | "second is hard escalation" | `enforcement_liquidation` at `unacceptable` → `unacceptable_escalated`, one escalation to senior lawyer, exit 2 | R16 | Holds. |

---

## 4. D04's actual escalation state

**D04 escalates. Exit code 2. One escalation, from
`R03a_natural_person_borrower_no_declaration`, to "senior lawyer + compliance".**

The reason recorded is: *"Individual borrower with no high-net-worth or
business-purpose declaration on file. Whether this facility is consumer credit
is not a determination this tool makes."*

Why, on the facts as written: D04's borrower is a Luxembourg-resident
individual with `declared_high_net_worth: null` and
`business_purpose_declared: null`. R03a fires when the borrower is a natural
person and *neither* declaration is `true`. It raises `consumer_credit` at
**high** and escalates. R03b — medium, no escalation — needs one of the two
declarations and does not fire.

This is the rule set behaving correctly and it is the more interesting deal for
a walkthrough: it is the one case in the six where the tool refuses to reach a
conclusion about consumer status and says so. `build_plan.md` §7 lists "the
final determination that a borrower is or is not a consumer under any regime"
as the first item in the not-automated register, and D04 is that item firing.

Two choices were available and the second was taken:

1. Give D04 a high-net-worth declaration, so R03b fires at medium and the deal
   does not escalate. That would have matched §5's D04 row more literally (it
   mentions no escalation) at the cost of losing the only deal that exercises
   R03a and the consumer-determination stop.
2. Leave both declarations null, which is what the managing agent's fact
   pattern specified, let R03a fire, and record the escalation. Taken.

`check.ps1` and `check.sh` therefore expect exit 2 for D04.

---

## 5. What this work package wrote

```
deals/D01_plain_vanilla.yaml            new
deals/D02_trust_concentrated_pdmr.yaml  new
deals/D03_swiss_corporate_purpose.yaml  new
deals/D04_third_party_pledge_lux.yaml   new
deals/D05_real_estate_hard_stop.yaml    new
deals/D06_below_floor_request.yaml      new
tests/test_golden_deals.py              new, 82 tests
tests/test_denylist.py                  new, 70 tests
tests/denylist.txt                      new, 26 terms
tests/expected/D0*_*.md                 new, 6 Markdown snapshots
tests/expected/D0*_*.json               new, 6 JSON snapshots
check.ps1                               new
check.sh                                new
playbook/flags/regulatory_flags.yaml    rename + description sentence (§2)
playbook/rules/rules.yaml               rename only
playbook/clauses/07, 08, 09, 11         rename only
tests/fixtures/runresult_escalated.*    rename only
tests/test_engine.py                    rename only
tests/test_flags_jurisdictions.py       rename only
```

`src/` was not touched. No CLI bug blocked this work package; `sbl run`,
`sbl validate` and the renderer all behaved as `handoff/WP5.md` and
`handoff/WP6.md` describe.

### The six deals

All synthetic. Party names are "Borrower A", "Aldergrove Trust", "Brantwood
Holding AG" and "Borrower D" — invented for this repo. Every `description`
begins `Synthetic.` and a test enforces that. D05 and D06 are D01 with exactly
one change each (real estate added, requests added), which is what makes the
three outputs readable side by side in a demo: same borrower, one fact
different, visibly different markup.

### Snapshots

`tests/expected/<deal file stem>.md` and `.json`, named after the deal **file**
stem per `build_plan.md` §1 (`D01_plain_vanilla.md`, not `D01.md`).

Normalisation is exactly two values — `run_id` and `timestamp`, the only
non-deterministic fields in a `RunResult` — replaced by `000000000000` and
`1970-01-01T00:00:00+00:00`. A separate test asserts that those two are the
*only* fields that differ between a live run and its normalised form, so if a
third non-deterministic field ever appears the snapshots do not start flapping
silently.

Regenerate with:

```
SBL_UPDATE_SNAPSHOTS=1 .venv/Scripts/python -m pytest -q tests/test_golden_deals.py
```

`library_hash` and `intake_hash` are **not** normalised. Any change to
`playbook/` changes the snapshots, which is the point: a golden test that
ignores the library is not a golden test. `docs/` is not in the library hash,
so WP10a's work does not disturb them.

The twelve snapshot files are about 1.9 MB in total, dominated by the full
clause ladders repeated in every run. That is the cost of the WP5 decision to
make `RunResult` self-contained so the renderer needs nothing else.

### Denylist

`tests/denylist.txt` holds the 26 terms supplied, one per line; comments and
blanks are ignored, so extending it needs no code change. The sweep covers
`playbook/`, `deals/`, `docs/`, `README.md` and `tests/expected/`, over
`.md/.yaml/.yml/.json/.txt/.csv`. Before matching it drops every line containing
`url:` and every `http…` token, then flattens whitespace across the whole file
so a two-word name still matches when a folded YAML block has wrapped it over a
line break. Matching is case-insensitive on word boundaries, so `ubs` does not
fire on `suburbs`.

---

## 6. The one thing that is not clean, and why

`docs/research/jurisdictions_research.md` (WP7's raw research notes) contains
three denylisted names in prose: two law firms in source `ref:` labels and one
bank in a case name given in full. The published library already neutralises all
three — `playbook/flags/regulatory_flags.yaml` cites the same briefing as
`UK-FCL-BRIEF-01` and the same decision by neutral citation as
`[2012] EWHC 2997 (Ch)` — so the fix is to apply the existing convention to the
research file. WP9 does not own `docs/` and was blocked from editing it.

Rather than narrow the sweep, the three hits are listed by file and by term in
`KNOWN_UNFIXED` at the top of `tests/test_denylist.py`, and the test asserts
that a file's hits are **exactly** its ledger entry. So:

* a **new** denylisted name in that file fails the test;
* a denylisted name in **any other** file fails the test;
* **cleaning** the file also fails the test, with a message telling you to
  delete the ledger entry.

It cannot decay in either direction, and it cannot be forgotten. Whoever next
edits `docs/` should make the three replacements and delete the ledger entry.

---

## 7. Lowest-confidence items, in priority order

1. **D04's escalation is a design call, not a fact.** §4 above sets out both
   options. If Stuart wants D04 to demonstrate third-party security *without* the
   consumer stop, set `declared_high_net_worth: true` on the borrower and
   regenerate the snapshots; R03b then replaces R03a, the flag drops to medium,
   the escalation disappears and D04 exits 0. `check.ps1`/`check.sh` would need
   the expected code changed to 0. The current shape was chosen because it is the
   only deal that exercises R03a.

2. **D01 raises two flags, not one.** `fcar_safe_harbour_uncertain` fires on
   every English-law deal with a natural-person collateral provider, which is
   most private-wealth deals. If "the clean deal" is meant to be a deal with one
   flag, the honest fix is to reconsider R04's severity once a human has read
   WP7's England & Wales overlay against R04's message — `handoff/WP5.md` §6.1
   flags exactly this reconciliation as outstanding. Do not fix it by changing
   D01's facts to dodge the rule.

3. **The 25% and 50% concentration thresholds behind D02.** D02's 70% single
   name was chosen to clear R06b's 50% line comfortably. Both thresholds are
   `build_plan.md` placeholders, not observed figures (`handoff/WP5.md` §6.4).
   If the credit-policy numbers move, D02 may stop tripping R06b; the explicit
   test would fail and say so, which is the intended behaviour.

4. **Snapshot brittleness against `playbook/` edits.** Every clause-text edit in
   WP3's remaining review work rewrites all twelve snapshot files. That is
   correct but noisy in a diff. Regenerate deliberately and read the `.md` diff,
   which is far more legible than the `.json` one.

5. **`check.ps1` hard-codes the expected exit code per deal file name.** A
   seventh deal added to `deals/` is run, but is only checked against exit 0, and
   the summary row says so ("not in the expected table"). It does not silently
   pass. `tests/test_golden_deals.py::test_all_six_deals_exist` is what actually
   pins the set of six.

6. **`check.sh` is kept in sync with `check.ps1` by hand.** Two expected tables,
   one truth. The tests are the real specification; the scripts only decide what
   "pass" prints. Noted in both files.
