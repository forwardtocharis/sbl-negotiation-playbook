# Hand-off: WP6 (Markdown markup renderer, audit log, explain)

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP6 and §2.5.
Everything in the fixtures is synthetic. Nothing here is legal advice.
No entry was set to `reviewed`; no `verified: true` source was written.

Files owned and written by this work package:

```
src/sbl/markup.py
src/sbl/audit.py
tests/test_markup.py
tests/fixtures/runresult_clean.json
tests/fixtures/runresult_clean.expected.md
tests/fixtures/runresult_escalated.json
tests/fixtures/runresult_escalated.expected.md
handoff/WP6.md                                   (this file)
```

Nothing else was touched. `models.py`, `engine.py`, `cli.py`, `rules.yaml` and
`tests/test_engine.py` were being edited concurrently by WP5 and were left alone.
**`cli.py` still needs wiring to these functions** — see §6.

---

## 1. Acceptance output (pasted verbatim)

### The WP6 acceptance check

```
$ .venv/Scripts/python -m pytest tests/test_markup.py -q
.........................................................                [100%]
57 passed in 0.48s
```

### The full suite, for information (not the WP6 pass criterion)

Run twice, a few minutes apart, while WP5 was still landing changes.

First run:

```
$ .venv/Scripts/python -m pytest -q
FAILED tests/test_schema_validation.py::test_stub_library_loads - AssertionEr...
FAILED tests/test_schema_validation.py::test_status_counts_shape - assert 21 ...
2 failed, 221 passed in 22.75s
```

Both failures were in **WP1's** `tests/test_schema_validation.py`, not in WP6,
and neither involved any WP6 file. They were stale assertions that the library is
still an empty scaffold (`assert library.rules == []`, now 18 rules;
`assert counts["clauses"]["stub"] == 24`, now fewer, because WP3 has promoted
clauses to draft).

Second run, after WP5 updated those two assertions:

```
$ .venv/Scripts/python -m pytest -q
........................................................................ [ 64%]
........................................................................ [ 96%]
.......                                                                  [100%]
223 passed in 23.24s
```

The whole suite is green as at the time of this note. That is a moving target
while WP3, WP5, WP7 and WP8 are in flight; the WP6 pass criterion is the
`tests/test_markup.py` run above.

### Renderer sanity against the live models

After WP5 landed `LadderRung`, `JurisdictionSummary` and the `RunResult`
additions, a real model instance was checked against its own JSON round trip:

```
$ .venv/Scripts/python -c "...build a RunResult, render it, append_run it, reload it, render again..."
model instance renders identically to its JSON round trip. chars: 1945
Run abc123456789 - deal D99
```

So `render_markdown(run_result) == render_markdown(json.loads(audit_line))` holds
against the models as they now stand, which is the §6 WP6 acceptance property
("the Markdown contains no text that is not derivable from `RunResult`: render
from a JSON file alone").

---

## 2. Public function signatures

### `src/sbl/markup.py`

```python
render_markdown(result: Any) -> str
```

`result` is a `RunResult` **or** the plain dict from `json.loads` on an audit
line. The module does not import `sbl.models` at all — it duck-types via
`model_dump(mode="json")` and falls back to mapping access. Every field is read
defensively, so a run written before a model change still renders.

Output guarantees, all covered by tests:

* LF line endings, no trailing whitespace on any line, ends with exactly one `\n`;
* no two consecutive blank lines;
* no date anywhere except the result's own `timestamp`;
* stable ordering (clauses in `clauses[]` order; flags high -> medium -> low;
  ladder rungs preferred -> unacceptable regardless of the order supplied);
* pipes inside table cells escaped as `\|`.

Also exported: `DISCLAIMER` (the footer paragraph) and `STATUS_WARNING` (the
one-line header warning). Module constants worth knowing: `SEVERITY_ORDER`,
`TIER_ORDER`, `STATUS_TAGS`, `SUMMARY_LIMIT = 160`, `EMPTY_CELL = "—"`.

### `src/sbl/audit.py`

```python
append_run(result: Any, path: Path) -> None
load_runs(path: Path) -> list[dict[str, Any]]
find_run(run_id: str, runs: Iterable[Mapping]) -> dict[str, Any]
explain(run_id: str, clause_id: str, path: Path) -> str
split_rule_prefix(item: str, rules_applied: Iterable[str] = ()) -> tuple[str | None, str]
```

* `append_run` creates parent directories, writes one line with
  `sort_keys=True, ensure_ascii=False, separators=(",", ":")` and
  `newline="\n"`, so the same run is byte-identical every time. Accepts a model
  or a dict.
* `load_runs` returns `[]` for a missing file (a first run has nothing to read)
  and raises `ValueError` naming `path:lineno` on a malformed line.
* `find_run` matches an exact `run_id` first, then a unique prefix. Raises
  `LookupError` when nothing matches (listing known ids) and when a prefix is
  ambiguous (listing the candidates).
* `explain` returns the trace as a string; it does **not** print. The CLI should
  print it and map `LookupError` to a non-zero exit. Raises `LookupError` with a
  message naming what was looked for when the run or the clause is not found; an
  unknown clause id lists the clause ids that are in the run.

---

## 3. Layout produced (what WP9's snapshots will contain)

1. `# SBL negotiation markup — <deal_id>`, then bullets: Deal, Description, Run
   id, Timestamp, Library hash, Intake hash, Governing law, Review status
   (`n reviewed / n draft / n stub`), then the one-line status warning.
2. `## Escalations` — always rendered. Table `Rule id | Clause | Who decides |
   Reason`, or the single line `No escalations.` Then `Exit code: n`.
3. `## Flags` — `### High severity` / `### Medium severity` / `### Low severity`,
   each flag as id, message, who decides, triggering rule. `No flags raised.`
   when empty. `[VERIFY]` prefixes pass through untouched.
4. `## Clause-by-clause` — in `clauses[]` order. Per drafted clause:
   `### <title> [DRAFT]`, bullets for clause id / risk rating / category /
   document, `**Opening: <tier>**` with the text as a blockquote and
   `Rationale: …`, `**Floor: <tier>** — approver: …` (approver taken from the
   floor rung, omitted when null), `**Position ladder**` as a four-column table
   with the unacceptable row labelled *(description of the walk-away line, not
   drafting)*, `**Escalation triggers**`, `**Conditions precedent added by
   rules**`, `**Representations/undertakings added by rules**`, `**Drafting
   notes**` (each omitted when empty), `**Jurisdiction note (<governing law>)**`,
   and `Rules applied: … | none`. A stub clause renders only the heading, the
   identity bullets, `No drafted positions yet; status stub.`, any rule-added
   items, and the rules-applied line.
5. `## Jurisdiction overlay — <name> [STUB]` — the `JurisdictionSummary`, omitted
   when `jurisdiction` is null. **This section is an addition to the plan's §6
   list**; see §5.1 below.
6. `## Counterparty request outcomes` — table `Clause | Requested tier |
   Requested text | Floor | Outcome`. Omitted entirely when there are none.
7. `## Not automated on this deal` — always rendered; bullets, or
   `None triggered on this deal.`
8. `---` and the footer disclaimer paragraph.

---

## 4. Fixtures and snapshots

`tests/fixtures/runresult_clean.json` (deal D90) — no escalations, one medium
`consumer_credit` flag, exit code 0, twelve drafted core clauses each with a
four-rung ladder, twelve stubs, `england_wales` jurisdiction summary, no
counterparty requests.

`tests/fixtures/runresult_escalated.json` (deal D91) — two escalations, three
flags across high/medium/low (the medium one's message begins `[VERIFY]`),
rule-added CPs/reps/notes prefixed `[R07_pdmr_pledged_issuer]`-style, all three
counterparty outcome kinds, exit code 2, and a literal `|` inside one ladder rung
so the table escaping is exercised by a fixture rather than only by a unit test.

Both are **hand-written**, not engine output, so this work package's tests stay
green while WP5 and WP3 move. Content is synthetic throughout: "Borrower A",
"Aldergrove Trust", deal ids D90/D91 (outside the D01–D06 range WP9 owns).
Judgement numbers are written as `X` per §2.1. Every legal-sounding statement in
the fixture jurisdiction summary carries `[VERIFY]` and `status: stub`.

`runresult_clean.expected.md` and `runresult_escalated.expected.md` are byte
snapshots of the rendering. To refresh them after a deliberate renderer change:

```
SBL_UPDATE_SNAPSHOTS=1 .venv/Scripts/python -m pytest tests/test_markup.py -q
```

and read the diff before keeping it.

---

## 5. Assumptions about WP5's output that WP5 and WP9 must confirm

**5.1 The `## Jurisdiction overlay` section is mine, not the plan's.** §6 WP6's
numbered layout does not list a jurisdiction section, but §6 WP7's acceptance
says "markup prints the correct file for each deal's governing law", and WP5 put
a full `JurisdictionSummary` on `RunResult`. Printing it per clause only (as
`jurisdiction_note`) would leave the seven overlay answers unrendered. I render
both: the per-clause note where the clause has one, and the overlay block once,
between `## Clause-by-clause` and `## Counterparty request outcomes`.
**If Stuart wants the plan's list followed literally, delete `_jurisdiction()`
from `markup.py` and re-cut the snapshots.**

**5.2 The `[<rule_id>] ` prefix convention.** Confirmed against WP5's
`ClauseResult` docstring as landed: *"Every string in `cps`, `reps` and `notes`
is prefixed with the id of the rule that added it, in square brackets followed by
one space."* `markup.py` renders these verbatim, prefix intact. `audit.explain`
strips the prefix and reports it as "added by: `<rule_id>`". A bracketed token is
only treated as a rule id when it is one of the clause's `rules_applied` **or**
matches `^R\d` — so a `[VERIFY]` prefix, which marks an unconfirmed statement
rather than a rule, is left in the text and attributed to nothing. An unprefixed
item renders fine and explains as "originating rule not recorded on the item".
**WP5/WP9: if the prefix format ever changes (e.g. to `R07: `), `explain` degrades
to showing the raw string, not to an error — but say so in a hand-off.**

**5.3 The `escalation_triggers` heading per clause.** WP5 added
`ClauseResult.escalation_triggers`; the plan's §6 WP6 layout does not mention
rendering it. I render it, because it is derivable and it is what a reader needs
to know before conceding. Drop it if the markup is judged too long.

**5.4 Ladder rung `rationale` is not rendered for non-opening tiers.** The plan
specifies the ladder table as `tier | one-line summary | conditions | approver`,
so only the *opening* tier's rationale reaches the markup. The other three
rationales are in the run JSON and in the library file but not in the Markdown.
That is a deliberate reading of the plan; if Stuart wants the "why" for each
fallback visible in the interview demo, a fifth column or a per-rung line is a
five-line change.

**5.5 `status_summary` is assumed to count the clauses in the run**, not the
whole library. The renderer prefers `result.status_summary` and falls back to
counting `clauses[]` if it is absent, so the two agree for a normal run.

**5.6 `exit_code` is rendered in the Escalations section**, per the WP6 brief.
`markup.py` prints `Exit code: not recorded.` if the field is missing rather than
guessing 0 from an empty escalation list.

**5.7 Stub clauses still render their rule-added CPs, reps and notes.** The brief
said stubs render "just `No drafted positions yet; status stub.` and rules
applied". Several §4 rules target stub clauses (R10 notes `purpose_restrictions`,
R05 notes `third_party_security_waivers`), and dropping those items would lose
rule output. So a stub renders compactly *plus* whatever rules added to it.

---

## 6. What WP6 did **not** do (needs an owner)

`src/sbl/cli.py` is WP5's file this cycle and was not touched, so the CLI is not
yet wired to either module. Someone (WP5, or WP9 when it writes `check.ps1`)
needs to:

* `sbl run` — call `markup.render_markdown(result)` and write the `.md` to
  `--out`, and call `audit.append_run(result, root / "runs" / "audit.jsonl")`;
* `sbl explain <run_id> <clause_id>` — call `audit.explain(...)`, print it, and
  catch `LookupError` to print the message and exit non-zero.

Both are one-liners; the signatures in §2 are stable.

---

## 7. Lowest-confidence items (in priority order for review)

1. **The `## Jurisdiction overlay` section (§5.1).** The single place where I
   added something the plan's layout does not list. It is the one decision here
   most likely to be reversed, and reversing it re-cuts both snapshots and, later,
   every WP9 snapshot. Decide before WP9 cuts `tests/expected/`.

2. **One-line ladder summary rule.** "First sentence, else first 160 characters."
   Implemented as the first `.`, `!` or `?` followed by whitespace or end of
   string, if it falls within 160 characters, otherwise a hard truncation with
   `...`. This mangles an abbreviation mid-sentence (`e.g.`, `No.`), and clause
   text that opens with a long sentence gets cut mid-clause. It reads well on
   these twelve fixtures; it may read badly on WP3's real drafting. Worth a look
   once the twelve core clauses are written.

3. **Fixture legal content is mine and is illustrative only.** The four-tier
   ladders in `runresult_*.json` were written to exercise the renderer, not to be
   a playbook. They carry no sources and no `[VERIFY]` discipline beyond a few
   marked lines, because they are render fixtures rather than library entries.
   **Nobody should mine them for clause positions.** If that risk is judged too
   high, the fixture text could be reduced to lorem-style placeholders — at the
   cost of making the snapshots much less useful for eyeballing the layout.

4. **The escalated fixture's two escalations both come from R16.** That keeps the
   fixture internally consistent (two escalated counterparty requests, two
   escalations) but means it does not exercise a rule-raised escalation with a
   null `clause`. The renderer handles a null `clause` (prints `—`), and that path
   is covered by the table-cell tests, but not by a fixture.

5. **Blank-line collapsing.** `render_markdown` collapses any run of blank lines
   to one before joining. It keeps the output tidy regardless of which sections
   fire, but it means a deliberate double blank line inside a `notes` string would
   be flattened. No current producer writes one.

6. **`_cell` escapes `|` only.** Not `*`, `_`, backticks or leading `#`. A clause
   text containing `*` would render as emphasis inside a table cell. Escaping more
   would make the snapshots noisier for a problem nothing currently has; flag it
   if WP3's drafting starts using markdown-significant characters.

7. **`explain` output is plain text, not Markdown.** It is meant to be read in a
   terminal during the demo (`build_plan.md` §8 points at exactly this). If the
   demo script wants to paste it into a document, it will need reformatting.
