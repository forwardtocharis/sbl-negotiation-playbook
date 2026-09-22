# Hand-off: WP4 (intake CLI) and WP5 (rules engine, rules.yaml)

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP4 and WP5.

Everything written here is synthetic. Nothing is legal advice. No entry has been
set to `reviewed`; no `verified: true` source has been written by this work
package. **Every source in `playbook/rules/rules.yaml` is `verified: false` with
a `[VERIFY]` ref, because this agent opened no source at all.** See §6.

---

## 1. Acceptance output (pasted verbatim)

### `pytest -q` — all test files green

```
$ .venv/Scripts/python -m pytest -q
........................................................................ [ 32%]
........................................................................ [ 64%]
........................................................................ [ 96%]
.......                                                                  [100%]
223 passed in 25.18s
```

(223 = 29 WP1 schema tests, as amended in §4.1, plus 48 in `tests/test_intake.py`,
89 in `tests/test_engine.py`, and the tests WP3/WP6/WP7/WP8 landed concurrently.)

### `python -m sbl validate` — exits 0, 18 rules

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 8821e3840fea2de6a51c3f3cd3facbced375fa6c9d8b972c73326a8d313bb165
exit code: 0

$ .venv/Scripts/python -m sbl validate --summary
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 8821e3840fea2de6a51c3f3cd3facbced375fa6c9d8b972c73326a8d313bb165

kind              stub   draft  reviewed   total
------------------------------------------------
clauses             21       3         0      24
rules                0      18         0      18
flags                0      10         0      10
jurisdictions        0       3         0       3

Entries not marked 'reviewed' have not been checked by a named human reviewer.
exit code: 0
```

The library hash and the clause/flag/jurisdiction status counts move as WP3, WP7
and WP8 land content; the rule line is this work package's.

### `python -m sbl run <test intake> --out runs/` — writes JSON

```
$ .venv/Scripts/python -m sbl run tests/fixtures/wp5_demo_intake.yaml --out runs/
T99 run 93c2e9d51d3a | 24 clauses (0 reviewed / 3 draft / 21 stub) | 4 flags | 4 escalations | exit 2 | wrote T99_93c2e9d51d3a.json, T99_93c2e9d51d3a.md, audit.jsonl
exit code: 2

$ ls runs/
T99_93c2e9d51d3a.json
T99_93c2e9d51d3a.md
audit.jsonl
```

Exit 2 is correct: the test intake is built to trip four escalations. The `.md`
and `audit.jsonl` appear because WP6 landed while this was being written; the CLI
imports `sbl.markup` and `sbl.audit` lazily inside `try/except ImportError`, so
it degrades to JSON only if they are absent.

### `sbl explain` round-trips through WP6

```
$ .venv/Scripts/python -m sbl explain 93c2e9d51d3a margin_maintenance_cure --audit runs/audit.jsonl
Run 93c2e9d51d3a - deal T99
...
Rules applied (3):
  - R06b_concentration_severe (no change)
  - R06_concentration
  - R16
...
Drafting notes added by rules (1):
  - Counterparty request accepted within floor at tier 'acceptable' (floor 'acceptable'); approver: ...
      added by: R16
```

WP6's `explain` parses the `[rule_id] ` prefix correctly, so the two halves of the
convention agree.

### A 110% portfolio is rejected (WP4 acceptance)

```
$ .venv/Scripts/python -m sbl run tests/fixtures/invalid_intake_composition_over_100.yaml
FAIL: tests/fixtures/invalid_intake_composition_over_100.yaml is not a valid intake:
  - tests/fixtures/invalid_intake_composition_over_100.yaml [D98]: field 'collateral': Value error, collateral composition percentages sum to 110, which exceeds 100
exit=1
```

---

## 2. Model additions (the exact list — this is a post-WP1-freeze change)

`src/sbl/models.py` only. Nothing was removed or renamed; every WP1 field keeps
its name and meaning. `python scripts/export_schemas.py` has been rerun and all
tests pass.

### 2.1 `Derived`

| change | field | definition |
|---|---|---|
| **added** | `any_issuer_restricted: bool` | any composition item with `issuer_restricted: true`. Percentage is not considered. Used by R08. |
| **added** | `has_illiquid_collateral: bool` | any composition item with `pct > 0` whose `asset_class` is in `fund_gated`, `unlisted`, `structured_product`. Used by R15. |
| **changed** | `has_real_estate: bool` | now requires `pct > 0` (was: any real-estate line whatever its percentage). |
| unchanged | `currency_mismatch` | still "any collateral currency differs from the facility currency", exactly as WP1 defined it. |

New module constant: `models.ILLIQUID_ASSET_CLASSES` — the frozenset of the three
asset classes above, so the rule and the test cannot drift apart.

Both new fields are addressable as `derived.any_issuer_restricted` and
`derived.has_illiquid_collateral` (tested). They resolve WP1's lowest-confidence
item 1 (projection over `collateral.composition`) the way WP1 recommended.

### 2.2 New models

* **`LadderRung`**: `tier`, `text`, `rationale`, `conditions: list[str]`,
  `approval: str | None`. The `unacceptable` rung always carries `conditions: []`
  and `approval: null`.
* **`JurisdictionSummary`**: `id`, `name`, `creation`, `registration_filing`,
  `perfection_depends_on`, `enforcement_route`, `financial_collateral_regime`,
  `governing_law_of_intermediated_securities`, `practical_notes`, `status`.
  `sources` is deliberately **not** copied.

### 2.3 `ClauseResult` — fields added

`title`, `category`, `document?`, `risk_rating?`, `opening_text?`,
`opening_rationale?`, `ladder: list[LadderRung]`, `jurisdiction_note?`,
`escalation_triggers: list[str]`, `not_automated: list[str]`.

Existing fields unchanged: `id`, `opening`, `floor`, `status`, `rules_applied[]`,
`cps[]`, `reps[]`, `notes[]`.

For a stub clause `ladder` is `[]`, `opening_text` and `opening_rationale` are
`null`, floor is `fallback` and opening is `preferred`, and `status` carries
`stub`.

### 2.4 `RunResult` — fields added

`deal_id`, `description`, `governing_law`, `status_summary: dict[str, int]`
(keys `reviewed` / `draft` / `stub`), `jurisdiction: JurisdictionSummary | None`
(None when `governing_law` is `other`), `not_automated: list[str]`,
`exit_code: int`.

`FlagResult.who_decides` is now populated by the engine from the flag definition
in `playbook/flags/regulatory_flags.yaml`.

`run_id` and `timestamp` remain the only non-deterministic fields.
`run_id` = first 12 hex characters of
`sha256(library_hash + intake_hash + timestamp)`.
`intake_hash` = `sha256(Intake.model_dump_json())`, derived fields included, so
comments and formatting in a deal file do not change it.

`RunResult.not_automated` is the deduplicated, sorted union of the
`not_automated` items of every clause the run touched. **A clause counts as
touched when** any rule left an entry in its `rules_applied` (including a
`(no change)` entry), **or** an escalation names it, **or** one of its
`regulatory_flags` was raised on this run. That last limb is how "flag-related"
is made concrete, since a `flag` action names no clause.

### 2.5 Also re-exported

`scripts/export_schemas.py` now also writes
`playbook/schema/run_result.schema.json`. The renderer's whole contract is that
object, so it is worth being readable without running Python. `playbook/schema/`
holds JSON, not YAML, so this does not affect `library_hash`.

---

## 3. The two conventions WP6 parses

### 3.1 `cps` / `reps` / `notes` carry their rule id

Every string the engine appends is prefixed with the id of the rule that produced
it, in square brackets followed by one space:

```
[R07_pdmr_pledged_issuer] Compliance sign-off on the pledgor's insider status...
[R16] Counterparty request accepted within floor at tier 'acceptable' (floor 'acceptable'); approver: senior lawyer.
```

**The id is the rule's full id exactly as it appears in `rules.yaml`**, not a
short form — so `R07_pdmr_pledged_issuer`, not `R07`. The one exception is the
built-in rule, whose id is the literal `R16`. A parser should take everything
between the leading `[` and the first `] `; WP6's `explain` already does, and it
works against the current ids.

### 3.2 `rules_applied` entries

* A **bare rule id** (`R06_concentration`) means the rule changed something on
  that clause: it tightened the floor or the opening, added a CP, a rep or a
  note, or raised an escalation naming the clause.
* The suffix **` (no change)`** (`engine.NO_CHANGE_SUFFIX`) means the rule named
  the clause but changed nothing on it — typically a `set_floor` to a tier
  another rule had already reached, or a duplicate note. Example from the test
  deal: `R06b_concentration_severe (no change)` on `margin_maintenance_cure`,
  because R06b sets that clause's opening to `preferred`, which it already is.
* A rule appears **at most once** per clause. If any one of its actions changed
  something, the entry is the bare id.

Both forms are recorded so the log answers "did this rule look at this clause?"
as well as "did it move it?".

---

## 4. Other decisions, and the reasons

### 4.1 Two WP1 assertions relaxed (`tests/test_schema_validation.py`)

`test_stub_library_loads` asserted `library.rules == []` and that every clause is
`stub`; `test_status_counts_shape` asserted `counts["clauses"]["stub"] == 24`.
Both were snapshots of the library at the end of WP1 and both now fail because
WP5 writes rules and WP3 promotes clauses. They are now
`len(library.rules) >= 15`, `status in (stub, draft)`, and
`sum(counts["clauses"].values()) == 24`, plus a new assertion that **no** kind has
any `reviewed` entry. The tests now assert the shape of the library rather than
how far the content work has got. Nothing else in that file was touched.

### 4.2 R03 is split into two rules, not one with a conditional severity

`R03a_natural_person_borrower_no_declaration` (severity `high`, escalates) and
`R03b_natural_person_borrower_declared` (severity `medium`, no escalation). A
`flag` action has no way to vary its own severity, and two rules read more
honestly in the log than one rule whose meaning depends on a branch nobody can
see. Their conditions are mutually exclusive, so exactly one fires for any
individual borrower.

### 4.3 R05 is split the same way, giving R05b

`R05_third_party_security` covers third-party security generally.
`R05b_third_party_corporate_pledgor` adds the
`financial_assistance_corporate_benefit` flag and the corporate-benefit CP, and
fires only when the pledgor is a company. Same reason: the condition is narrower
than R05's, and §2.4's grammar attaches conditions to rules, not to actions.

With those two splits the file has **18 rules**, not 15: R01, R02, R03a, R03b,
R04, R05, R05b, R06, R06b, R07, R08, R09, R10, R11, R12, R13, R14, R15. R16 is
built into `engine.py` and deliberately absent from the YAML: it fires on the
presence of a counterparty request, not on a fact about the deal.

### 4.4 R16, and the free-text convention

Per counterparty request, in clause-id order:

| case | outcome | escalation |
|---|---|---|
| requested tier is `unacceptable` | `unacceptable_escalated` | `rule_id=R16`, `to="senior lawyer"`, clause named, reason says walk-away line |
| requested tier is looser than the computed floor | `below_floor_escalated` | `rule_id=R16`, `to="senior lawyer"`, clause named, reason names both tiers |
| requested tier is at or tighter than the floor | `accepted_within_floor` | none; a note records the tier, the floor and the approver for that tier |
| **free text with no tier** | `below_floor_escalated` | `rule_id=R16`, `to="deal lawyer"`, reason exactly `unmapped counterparty request text requires manual classification` |

The free-text case is the decided convention: the engine does not guess what
prose maps to, and "I could not classify this" is not the same as "this is fine",
so it lands on the escalating side and a note quotes the request text back for
the lawyer who has to classify it. Where a request carries **both** a tier and
text, the tier governs and the text is quoted at the end of the note.

A request naming a clause id that is not in the library raises `EngineError`
rather than being ignored. The loader does not check intake request keys (they
are a `dict[str, …]`), so the engine is the only place that can catch a typo.

### 4.5 Order independence is achieved by sorting, not by commutativity

`evaluate()` sorts by `(priority, id)` whatever order the rules arrive in.
Feeding `library.rules` reversed therefore gives a byte-identical `RunResult`
(tested by comparing `model_dump_json(indent=2)`), and the order of `cps` /
`reps` / `notes` inside a clause is the canonical rule order rather than an
accident of file layout. Tier assignments are separately tighten-only
(`tighter(current, proposed)`), which is what makes the sort safe to rely on.

The `opening ≤ floor` invariant is asserted per clause before the result is
returned and raises `EngineError` if it is ever violated. In practice `opening`
starts at `preferred` and can only tighten, so it stays at `preferred`; the
assertion is there to catch a future loosening action rather than a live bug.

### 4.6 Null handling, and projection

A null on the left of a leaf condition makes **every** operator `False` except
`is_null` — including `neq`. "We do not know" must not read as "the rule fires",
and must not read as an error either, because most intake fields are legitimately
null on most deals. `True == 1` is explicitly defused: a boolean field only ever
equals a boolean value.

A dotted path that crosses a list of models projects across it, so
`collateral.composition.asset_class` evaluates to the list of that field over
every line and `{op: contains, value: fund_gated}` means "any line is gated".
That is tested, but no rule in `rules.yaml` uses it: the two derived booleans are
clearer in a YAML condition and easier to test.

### 4.7 Stub clauses still get tiers

A clause with no `default_floor` gets floor `fallback` and opening `preferred`
(`engine.STUB_DEFAULT_FLOOR`), and its `status: stub` travels into the result so
the markup can label the tiers as placeholders.

### 4.8 CLI

* `sbl run <deal.yaml> [...] [--out DIR] [--echo]`. Multiple paths; a `*` in an
  argument is expanded by `glob` as well as by the shell, because the Windows
  shell does not glob. A wildcard matching nothing is passed through unchanged so
  the error names it.
* `--echo` prints the validated intake as YAML, derived fields included, to
  stdout before the run.
* With `--out`, writes `<DIR>/<deal_id>_<run_id>.json`
  (`model_dump_json(indent=2)`), plus `<DIR>/<deal_id>_<run_id>.md` if
  `sbl.markup.render_markdown` imports, and calls `sbl.audit.append_run` with
  `<DIR>/audit.jsonl` if it imports. Both imports are lazy and wrapped in
  `try/except ImportError`. **Without `--out` nothing is written** — the run still
  evaluates and prints its summary line.
* Exit code is the worst over the deals run: `result.exit_code` (0 or 2), or 1 if
  a deal file failed to load.
* `sbl explain <run_id> <clause_id> [--audit PATH]` delegates to
  `sbl.audit.explain`, defaulting the path to `<root>/runs/audit.jsonl`. If
  `sbl.audit` is not importable it prints "not implemented" and exits 1.
* `sbl intake --interactive` was skipped, as instructed (`build_plan.md` §6 WP4
  makes it lowest priority).

### 4.9 Test intake

`tests/fixtures/wp5_demo_intake.yaml` (deal id `T99`), **not** in `deals/` —
`deals/` is WP9's. Entirely synthetic: a fictional discretionary trust borrower
with a concentrated, partly restricted, partly illiquid portfolio at a
third-party Swiss custodian, plus one counterparty request of each of the three
kinds. It is shaped to exercise the engine, not to be a realistic deal.

---

## 5. Files this work package owns

```
src/sbl/engine.py                    new
src/sbl/cli.py                       rewritten (run + explain implemented)
src/sbl/models.py                    additions only (§2)
playbook/rules/rules.yaml            18 rules, all status: draft
tests/test_intake.py                 new, 48 tests
tests/test_engine.py                 new, 89 tests
tests/fixtures/wp5_demo_intake.yaml  new
docs/schema_notes.md                 §3 Derived / RunResult / new §3.1 engine conventions
playbook/schema/*.json               re-exported, plus run_result.schema.json
scripts/export_schemas.py            one target added
tests/test_schema_validation.py      two stale assertions relaxed (§4.1)
```

`src/sbl/markup.py`, `src/sbl/audit.py` and `tests/test_markup.py` were **not**
touched: they belong to WP6.

---

## 6. Lowest-confidence items, in priority order for review

**Everything in §6.1 is the big one.** The rest are design choices.

### 6.1 No source in `rules.yaml` has been opened. Every one is `[VERIFY]`.

This agent did not open a single primary text, regulator page, filed agreement or
briefing. `docs/research/jurisdictions_research.md` and
`docs/research/clause_sources.md` did not exist when the rules were written.
Accordingly, in `playbook/rules/rules.yaml`:

* every `sources` entry has `verified: false`, `url: null`, `retrieved: null`,
  and a `ref` that begins `[VERIFY]` and describes a **research target**, not a
  checked citation;
* **no section, article, regulation number, case name, date or URL is asserted
  anywhere** — only instrument names that already appear in `build_plan.md` or
  that are common knowledge, and even those are framed as "research target";
* every `flag` message begins `[VERIFY]`, because every one of them asserts that
  a regulatory regime may apply. A test enforces the `[VERIFY]` prefix and
  `verified: false` on all rule sources, so this cannot silently decay.

The single least certain statement in the rule set is **R04**'s: whether the
English financial collateral regime's protections (appropriation, relief from
registration and sale formalities) are available where the collateral provider is
a natural person. The rule is written so the lender does not rely on the answer
either way, but a reviewer should treat this as the first thing to check. *(WP7's
England & Wales overlay landed after these rules were written and appears to
answer this point; R04's message and note should be reconciled against it, and
the flag's severity reconsidered, once a human has read both.)*

The other rule-source items a reviewer should take in order:

1. **R03a / R03b** — the consumer credit regime, its high-net-worth and
   business-purpose exemptions, the required form and timing of a declaration,
   and every threshold figure. Nothing here is confirmed for either the UK or
   Switzerland.
2. **R07** — whether a pledge, and whether an enforcement sale, is a notifiable
   or restricted transaction for a PDMR. Framed as "may be"; unconfirmed.
3. **R08** — the resale restrictions on control and affiliate securities and
   typical lock-up terms. No filed lock-up agreement was read.
4. **R06 / R06b thresholds** — 25% and 50% are placeholders taken straight from
   `build_plan.md` §4, not figures observed in any published source. They are
   credit-policy numbers and belong to whoever owns the credit policy.
5. **R14** — Swiss banking confidentiality and Swiss law on intermediated
   securities. WP7's Switzerland overlay is the right place to resolve both.
6. **R09** is a scope boundary rather than a legal statement, and should be read
   that way: it says "this tool was not built for land", not "here is the law on
   land".

### 6.2 Rule ids in the `[...]` prefix are the **full** ids

The interface note gave `[R07]` as its example. The engine writes
`[R07_pdmr_pledged_issuer]`, because that is the id in `rules.yaml` and a reader
can look it up. A parser matching `^\[([^\]]+)\] ` is unaffected, and WP6's
`explain` works today. If WP6 ever hard-codes a short form, this is where it will
break.

### 6.3 "Touched" for `RunResult.not_automated`

The definition in §2.4 is mine: `rules_applied` non-empty, **or** named by an
escalation, **or** one of the clause's `regulatory_flags` was raised. A
`(no change)` entry counts as touched, which is slightly generous. `build_plan.md`
§6 WP6 says "clauses touched by escalations or flags", which is narrower; the
managing agent's instruction was broader. If the not-automated section of the
markup reads as noise on a quiet deal, tighten this first.

### 6.4 `to="senior lawyer"` on a below-floor R16 escalation

The instruction fixed `to` for the `unacceptable` case and for the free-text
case but not for below-floor. I used `"senior lawyer"` for consistency with the
`unacceptable` case rather than reading the approver off the requested tier's
`Position.approval`, which would make the escalation target depend on clause
content and vary between a stub and a drafted clause. The approver **is** recorded
in the note on the accepted path.

### 6.5 The `opening` tier is always `preferred` in practice

`set_opening` can only tighten and the opening starts at `preferred`, so no rule
can ever move it. That follows directly from §2.2 ("rules can only move it up"),
and R06b's own plan entry acknowledges it ("set_opening margin_maintenance_cure =
preferred (already)"). It means `set_opening` is currently a no-op action that
exists for symmetry and for the log. If the intention was that the opening should
start at the clause's `default_floor` and be tightened from there, that is a
one-line change in `engine.evaluate` — but it is a contract decision, not mine.

### 6.6 `currency_mismatch` stays broad

Per instruction, unchanged from WP1: a GBP facility against `[GBP, USD]`
collateral **is** a mismatch, so R13 fires on most multi-currency portfolios and
adds two notes and one floor tightening. R13 does not escalate, so a "quiet" deal
stays at exit 0 — but WP9 should expect the notes when cutting D01's snapshot
(this is WP1's lowest-confidence item 2, still open).

### 6.7 Rationale wording

Every rule's `rationale` is two to four sentences, lender-side, written to be
said out loud. They are commercial explanations, not statements of law, and they
carry no citations. They are the part of this work package a human can review
fastest and should probably rewrite most freely.
