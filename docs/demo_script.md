# Demo script

Exact commands, in order, with the expected exit code, the expected one-line summary, and the
three things to put on screen for each. Everything here is synthetic. Nothing is legal advice. No
entry in the library has been reviewed by a named human.

The order is deliberate: **D01 is the clean run**, **D02 is the escalation-heavy run**, and **D06
is the counterparty-request run**. D06 is D01 with two requests added and nothing else changed, so
the third screen is a controlled comparison against the first.

Total running time is a few seconds. The talking is the slow part.

## Before you start

Working directory is the repository root. The interpreter is the project venv:

```
.venv\Scripts\python -m sbl validate --summary
```

Expected: **exit 0**, and this block, which is the slide nobody expects a tool to show:

```
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 7d8caf2f1de399852e2edfb99fdaf1e4d23aaa90da1ce56e9804611cb31d2a72

kind              stub   draft  reviewed   total
------------------------------------------------
clauses             12      12         0      24
rules                0      18         0      18
flags                0      10         0      10
jurisdictions        0       3         0       3

Entries not marked 'reviewed' have not been checked by a named human reviewer.
```

Point at the **`reviewed` column: every row is zero**. Say that out loud before anything else.

The examples below write `python` for brevity. Use `.venv\Scripts\python` unless the venv is
activated. Every `run_id` in this document is from one real run; **yours will differ**, because the
run id is derived from the timestamp as well as from the library and intake hashes. The output
filenames change with it.

Reset to a clean state at any point with:

```
Remove-Item -Recurse -Force runs
```

(POSIX: `rm -rf runs`.) `runs/` is gitignored and holds nothing that cannot be regenerated.

---

## 1. D01, the clean run

```
python -m sbl run deals/D01_plain_vanilla.yaml --out runs/
```

**Expected exit code: 0.**

Expected one-line summary (run id will differ):

```
D01 run 18088da25cb0 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 0 escalations | exit 0 | wrote D01_18088da25cb0.json, D01_18088da25cb0.md, audit.jsonl
```

Open `runs/D01_<run_id>.md`. Three things on screen:

1. **`## Escalations`**, which reads `No escalations.` and then `Exit code: 0`. This is what a deal
   the playbook can handle end to end looks like: a UK individual with a high-net-worth
   declaration on file, a diversified listed portfolio in the lender's own custody, uncommitted
   demand, sterling, general purpose. Nothing needed a human.
2. **`### Facility type: uncommitted and repayable on demand versus committed term [DRAFT]`**, the
   first clause. Point at the `[DRAFT]` tag in the heading, then at `**Opening: preferred**` with
   its drafting text and its rationale, then at `**Floor: acceptable**`, then at the
   `**Position ladder**` table underneath, which carries all four tiers with their conditions and
   their approver. Say what the floor is: the lowest tier the deal lawyer may concede to on this
   deal without asking anyone. The ladder says who to ask to go further.
3. **`## Flags`**, under `### Medium severity`: `consumer_credit`, raised by
   `R03b_natural_person_borrower_declared`, and `fcar_safe_harbour_uncertain`, raised by
   `R04_natural_person_pledgor_england`. Each carries a `Who decides` line. Point at the `[VERIFY]`
   text inside the second flag and say what it means: nobody opened a primary source that confirms
   that sentence. Then concede the known limitation before anyone asks, that R04 fires on most
   English-law private-client deals, so even the clean deal raises it.

---

## 2. D02, the escalation-heavy run

```
python -m sbl run deals/D02_trust_concentrated_pdmr.yaml --out runs/
```

**Expected exit code: 2.** Exit 2 is the designed outcome, not a failure: it means at least one
escalation.

Expected one-line summary (run id will differ):

```
D02 run 84d70a5d862b | 24 clauses (0 reviewed / 12 draft / 12 stub) | 1 flags | 2 escalations | exit 2 | wrote D02_84d70a5d862b.json, D02_84d70a5d862b.md, audit.jsonl
```

The deal: a Jersey discretionary trust, seventy per cent of the portfolio in one listed holding,
and the trust is a person discharging managerial responsibilities in relation to the pledged
issuer. Four rules fire: R01, R06, R06b and R07.

Open `runs/D02_<run_id>.md`. Three things on screen:

1. **`## Escalations`**, the table immediately under the header, before any clause text. Two rows:
   `R06b_concentration_severe` on `eligible_collateral_lending_values` to **credit**, because
   single-issuer exposure exceeds fifty per cent of lending value; and `R07_pdmr_pledged_issuer`
   to **senior lawyer + compliance**, because the insider status of the collateral provider has to
   be cleared before a term sheet is issued. Then `Exit code: 2`. The point to make: escalations
   are printed first, with the rule id and the named approver, so the reader cannot get to the
   drafting without seeing what has to be decided by a person.
2. **`### Margin maintenance, margin call mechanics and cure period [DRAFT]`**, read side by side
   with the same clause in D01. In D01 it is `**Floor: fallback** - approver: head of credit`; here
   it is `**Floor: acceptable**`. One fact about the portfolio moved the floor up a tier, and the
   `Rules applied:` line at the end of the clause says which rules touched it:
   `R06b_concentration_severe (no change), R06_concentration`. The `(no change)` suffix is worth a
   sentence: R06b named this clause and changed nothing on it, and the log records that it looked
   as well as that it did not move it. Say that rules only tighten, so two rules cannot disagree
   and the order they run in cannot change the answer.
3. **`### Enforcement and liquidation: notice, standard of conduct and self-help sale [DRAFT]`**.
   Floor `acceptable`, `Rules applied: R07_pdmr_pledged_issuer`. Point at the
   `**Jurisdiction note (england_wales)**` block under it, which is where the England and Wales
   overlay prints for this deal, and at the `[VERIFY]` sentence inside it. Then scroll to
   **`## Not automated on this deal`** at the foot and read one line out: whether a closed period,
   an issuer consent or a volume limit blocks or delays a sale, and whether compliance has cleared
   it. This tool does not decide that and says so on the face of the document.

### 2a. The audit trace

```
python -m sbl explain 84d70a5d862b enforcement_liquidation --audit runs/audit.jsonl
```

Substitute the run id printed by your own D02 run. **Expected exit code: 0.** Expected output,
with your run id, timestamp and intake hash:

```
Run 84d70a5d862b - deal D02
Timestamp:    2026-09-21T16:51:38.147480+00:00
Library hash: 7d8caf2f1de399852e2edfb99fdaf1e4d23aaa90da1ce56e9804611cb31d2a72
Intake hash:  996762f7d5a372d8688d83f50ad2f8e84b8d971112ed3d3c0898a3cb7564e0c2

Clause: enforcement_liquidation - Enforcement and liquidation: notice, standard of conduct and self-help sale
Status:  draft
Opening: preferred
Floor:   acceptable

Rules applied (1):
  - R07_pdmr_pledged_issuer

Conditions precedent added by rules: none.

Representations/undertakings added by rules: none.

Drafting notes added by rules: none.

Escalations naming this clause: none.

Counterparty requests on this clause: none.

This trace is derived entirely from the audit line for this run. Nothing here is legal advice.
```

What to say while it is on screen: the enforcement floor on this deal is `acceptable` rather than
the library default, and the single reason is `R07_pdmr_pledged_issuer`, the insider rule. The
trace is read back out of `runs/audit.jsonl`, not recomputed, so it is the record of what that run
actually did, pinned to a library hash. Change one clause file and the hash changes, and every
line written against the old library still says which library it was.

Two details worth naming because they look like gaps and are not. R07's escalation names no clause
(it is a hard stop on the deal, not on one clause), which is why "Escalations naming this clause"
is `none`. And R07's condition precedent lands on `conditions_precedent` and its representation on
`capacity_authority`, which is where every CP and every rep lands, so both are `none` here; run
the same command against `capacity_authority` and the insider representation is there, alongside
R01's trustee representation on the same clause.

---

## 3. D06, the counterparty-request run

```
python -m sbl run deals/D06_below_floor_request.yaml --out runs/
```

**Expected exit code: 2.**

Expected one-line summary (run id will differ):

```
D06 run c5227ea56800 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 1 escalations | exit 2 | wrote D06_c5227ea56800.json, D06_c5227ea56800.md, audit.jsonl
```

D06 is D01 with exactly two counterparty requests added and no other change: the `fallback` cure
period on margin maintenance, and the `unacceptable` position on enforcement and liquidation.

Open `runs/D06_<run_id>.md`. Three things on screen:

1. **`## Counterparty request outcomes`**, near the foot of the document:

   ```
   | Clause | Requested tier | Requested text | Floor | Outcome |
   | --- | --- | --- | --- | --- |
   | enforcement_liquidation | unacceptable | — | fallback | unacceptable_escalated |
   | margin_maintenance_cure | fallback | — | fallback | accepted_within_floor |
   ```

   Two requests, two different answers, and the floor is printed next to each so the reader can
   check the arithmetic. This is the engine's one built-in rule, R16: it is not in `rules.yaml`
   because it fires on the presence of a request rather than on a fact about the deal.
2. **`## Escalations`** at the top: one row, `R16` on `enforcement_liquidation`, to **senior
   lawyer**, with the reason that this is the lender's walk-away line and nobody may agree it.
   Then `Exit code: 2`. Contrast with D01, which is the same deal and exits 0.
3. **`### Margin maintenance, margin call mechanics and cure period [DRAFT]`**, the request that
   was accepted. Under `**Drafting notes**`:

   ```
   - [R16] Counterparty request accepted within floor at tier 'fallback' (floor 'fallback'); approver: head of credit.
   ```

   The concession is inside the floor, so no escalation, but it is still logged with the tier, the
   floor and the named approver for that tier. Say the line that this whole demo is for: the tool
   is not deciding whether to concede, it is making sure that whoever did decide is named, and that
   the reason is still on the file in six months.

---

## Reset

```
Remove-Item -Recurse -Force runs
```

POSIX: `rm -rf runs`. Deletes every rendered markup, every run JSON and `runs/audit.jsonl`. The
directory is gitignored and is recreated by the next `--out runs/`. Do this before a demo so the
audience sees the files appear.

## If something goes wrong

```
powershell -ExecutionPolicy Bypass -File check.ps1
```

POSIX: `sh check.sh`. It runs `sbl validate`, then the full test suite, then every deal in
`deals/`, and prints a summary table of expected against actual exit code for each stage. It
should exit 0. If a deal fails to load, that is exit 1 and the message names the file and the
field. If the summary table shows a deal at exit 0 where 2 was expected, an escalation has gone
missing, which is the failure mode that matters. Do not demo off a red check.
