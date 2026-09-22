# SBL Negotiation Playbook Demonstrator

> **Disclaimer.** This is a **demonstrator built from public sources**: legislation, regulator
> material, a small number of publicly filed agreements read for structure rather than wording,
> and published commentary. Every deal, party and portfolio in this repository is **synthetic**
> and fictional. Nothing here is **legal advice**. None of it has been **validated against any
> institution's credit policy, risk appetite, house style or local counsel advice**, and it is
> not a statement of any institution's position. Every clause entry, rule, jurisdiction note and
> regulatory flag carries a `status` field: **every entry in this repository is `stub` or
> `draft`, and none has been promoted to `reviewed` by a named human**. `draft` means written
> from public sources and checked by nobody. Text carrying a `[VERIFY]` prefix has not been
> confirmed against a primary source the writer opened. Do not rely on any position in this
> repository until a named reviewer has read it and recorded themselves in the entry.

**Status: build complete, all entries draft, none reviewed.**

## What this is

Securities-based lending (SBL) is credit extended to a private client and secured against that
client's existing investment portfolio, which stays pledged rather than being sold or lent out;
Swiss and continental private banking calls the same product a **Lombard loan**, and it is not
securities lending, which is the temporary transfer of stock itself for a fee. A facility is
documented in three pieces: a **facility letter** carrying the credit terms, a **security
agreement** creating the pledge, charge or title transfer, and, where the lender is not the
custodian, an **account control agreement** with the third-party custodian. Negotiating those
documents inside a private bank means holding a line between a relationship manager who wants the
facility drawn quickly on terms the client will accept and a credit and legal function that has
to be able to price, perfect and enforce the security, which without a playbook produces ad hoc
concessions with no institutional memory and senior lawyer time spent re-deriving the same
fallback on every deal. This repository is a lender-side negotiation playbook for that product,
expressed as structured data rather than prose, so that each position carries its tier, its
conditions, its named approver and its sources, and so that the positions proposed on a given
deal can be traced back to the library entry and the rule that produced them.
`docs/product_definition.md` has the longer version.

## What the tool does

It holds a **clause library** of twenty-four clause entries, each with a four-tier position ladder
(`preferred` / `acceptable` / `fallback` / `unacceptable`) plus conditions, approvers, escalation
triggers, jurisdiction notes and sources, and it takes a structured **deal intake** describing the
borrower, the pledgor, the facility and the collateral. A **deterministic rules engine** reads the
intake, fires the rules whose conditions the facts satisfy, and records what each one did. The
result is rendered as a **negotiation markup** in Markdown and appended as one line to an **audit
log**, so every emitted position traces to a library entry, a rule and a content hash of the
library that produced it; `sbl explain` replays that trace for any clause of any past run. Rules
may only **tighten**: they can raise a clause's floor or opening but never lower either, so no two
rules can disagree and rule order cannot change the result, and anything the tool will not decide
for itself becomes an **explicit escalation** naming the rule, the clause and who has to decide,
which makes the run exit with code 2.

## How to run

Python 3.11 or later. From the repository root:

```
python -m venv .venv
.venv\Scripts\pip install -e ".[test]"
```

On Linux or macOS the second line is `.venv/bin/pip install -e ".[test]"`.

**Install caveat.** The build agent could not install into the system Python on the build machine:
`pip install -e .` against `C:\Python312` failed twice on a Windows file-permission error while
replacing a console script, which is an environment problem and not a packaging one (the wheel
built cleanly both times). Everything in this repository was therefore built and checked inside
the project-local `.venv`, which is what `check.ps1` and `check.sh` prefer. A plain
`pip install -e .` into your own Python is expected to work and **should be confirmed by you**;
if it does not, that is a real failure and not a known one.

Then:

```
python -m sbl validate --summary
python -m sbl run deals/D02_trust_concentrated_pdmr.yaml --out runs/
python -m sbl explain <run_id> enforcement_liquidation --audit runs/audit.jsonl
```

`<run_id>` is the twelve-character id printed by `sbl run` and used in the output filenames, for
example `975ab2d753b8` in `runs/D02_975ab2d753b8.md`. It changes on every run, because it is
derived from the timestamp as well as from the library and intake hashes. `--audit` defaults to
`<root>/runs/audit.jsonl`, so it can be left off when running from the repository root; the flag
is shown here because the demo script uses it explicitly.

To run everything at once:

```
powershell -ExecutionPolicy Bypass -File check.ps1
```

or, on a POSIX shell, `sh check.sh`. Both run `sbl validate`, then `pytest -q`, then every deal in
`deals/`, and check each deal's exit code against the code that deal is supposed to produce. Four
of the six deals escalate and therefore exit 2 by design; the script treats that as a pass for
those deals and as a failure if they ever exit 0.

`runs/` is gitignored. Delete it whenever you want a clean slate.

## Repository layout

```
README.md                      this file
build_plan.md                  the authoritative build plan
sbl_playbook_brief.md          the original brief
brief_review.md                the review the plan came from
pyproject.toml                 package metadata; dependencies are pyyaml and pydantic only
check.ps1  check.sh            validate, then pytest, then every deal

playbook/
  clauses/*.yaml               24 clause entries; 01 to 12 core, 13 to 24 deferred stubs
  rules/rules.yaml             18 ordered rules (R16 is built into the engine, not here)
  jurisdictions/*.yaml         england_wales, switzerland, luxembourg overlays
  flags/regulatory_flags.yaml  10 regulatory and commercial flag definitions
  schema/*.json                JSON schemas exported from the pydantic models

deals/D01..D06 *.yaml          six synthetic golden deals
runs/                          gitignored; run output and audit.jsonl land here

src/sbl/
  models.py                    pydantic models; every closed list is an enum
  loader.py                    YAML loading, cross-reference checks, library hash
  engine.py                    deterministic rule evaluation, tighten-only
  markup.py                    Markdown renderer; reads RunResult and nothing else
  audit.py                     JSONL audit log writer and the explain trace
  cli.py  __main__.py          python -m sbl validate, run, explain

tests/
  test_schema_validation.py    the frozen data contract, including ten rejection cases
  test_intake.py               intake validation and derived fields
  test_engine.py               each rule fires, and does not fire on its negation
  test_markup.py               renderer output guarantees
  test_flags_jurisdictions.py  flag and jurisdiction content checks
  test_golden_deals.py         snapshot equality plus explicit per-deal assertions
  test_denylist.py             no real institution or person names anywhere
  test_readme.py               this file quotes the current library_hash
  expected/                    the six golden Markdown and JSON snapshots
  fixtures/                    valid and deliberately invalid inputs

docs/
  product_definition.md        SBL vs securities lending, Lombard terms, the document set
  glossary.md                  tier semantics and canonical terms
  schema_notes.md              the frozen data contract in prose
  not_automated_register.md    every decision this tool refuses to make
  source_register.md           every source, graded, with retrieval date
  review_priorities.md         what a human should read first
  interview_walkthrough.md     three-minute script and anticipated questions
  demo_script.md               exact commands and what to point at on screen
  research/                    raw research notes behind the clauses and the overlays

handoff/                       one hand-off note per work package
scripts/export_schemas.py      regenerates playbook/schema/*.json from the models
```

## Status counts

Pasted from `python -m sbl validate --summary`:

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

These counts and the library hash are **regenerated by `python -m sbl validate --summary`**, and
the hash changes whenever any file under `playbook/` changes. Treat the block above as a snapshot
of one moment rather than as a maintained figure: run the command. The hash at least cannot go
stale silently: `tests/test_readme.py` recomputes it from `playbook/` and fails if this file does
not contain it. The counts are not pinned that way and can still drift.

The `reviewed` column is zero on every row, and only a named human can change that.

## Reading the output

`sbl run <deal> --out runs/` writes three things into the output directory:
`<deal_id>_<run_id>.json` (the full `RunResult`), `<deal_id>_<run_id>.md` (the negotiation
markup), and one appended line in `runs/audit.jsonl`. The Markdown is rendered from the
`RunResult` alone and from nothing else, which is what makes the trace complete: a test renders
the same document from the JSON file with the library unavailable.

**Status tags.** Every clause heading carries `[DRAFT]` or `[STUB]`, and would carry `[REVIEWED]`
if anything had been reviewed. `[DRAFT]` means the entry has drafting in all four tiers, written
from public sources, that no named human has checked. `[STUB]` means no position has been drafted
at all: the entry exists so that rules can reference it and so that the markup shows the shape of
the full library, and the engine gives it a placeholder floor of `fallback`. Twelve of the
twenty-four clauses are `[STUB]` and they print with no ladder.

**Opening and floor.** The **opening** is the tier the markup proposes first, and it is
`preferred` on every clause unless a rule tightened it. The **floor** is the lowest tier the deal
lawyer may concede to on this deal without escalating; it starts at the clause's `default_floor`
and rules can only raise it. The ladder table under each clause prints all four tiers with their
conditions and their named approver, so the floor tells you where to stop and the ladder tells you
who to ask if you want to go further. A counterparty request at or above the floor is recorded as
`accepted_within_floor`; a request below it, or at `unacceptable`, is escalated and appears in the
**Counterparty request outcomes** table.

**`[VERIFY]`.** A `[VERIFY]` prefix on any sentence means the writer did not open a primary source
that confirms it. It is used heavily: every source in `playbook/rules/rules.yaml` is
`verified: false`, because the agent that wrote the rules opened no source at all. `[VERIFY]` text
is a research target, not a finding.

**Exit code.** `sbl run` exits 0 when the deal raised no escalation, 2 when it raised at least
one, and 1 when a deal file failed to load. Exit 2 is not an error: it is the tool saying that a
named human has to decide something before the deal can proceed, and the **Escalations** table at
the top of the markup says who and why. When several deals are run in one invocation the exit code
is the worst of them.

## What is not automated

`docs/not_automated_register.md` is the consolidated list, and every run prints the subset that
applies to that deal under **Not automated on this deal**. The system-level items are the final
determination that a borrower is or is not a consumer, any concession below a clause's floor and
any request at `unacceptable`, clearing an insider position with compliance, suitability and
appropriateness conclusions, every cross-border perfection and enforceability conclusion, KYC,
sanctions and source-of-funds outcomes, forbearance on a live margin call and the decision to
enforce, and the promotion of any entry from `draft` to `reviewed`.

## Known limitations

These are the things to know before drawing any conclusion from the output. The hand-off notes
under `handoff/` carry the detail, and `docs/review_priorities.md` puts them in the order a human
should work through them.

- **Every number that is a judgement call is a placeholder.** Cure periods, notice periods,
  lending values and grace periods are written as `X` in the clause text, with the observed range
  recorded in the entry. The 25 per cent and 50 per cent concentration thresholds behind rules R06
  and R06b come from the build plan, not from any observed source; they are credit-policy numbers
  and belong to whoever owns the credit policy. If they move, D02 may stop tripping R06b, and the
  golden test will say so.
- **Jurisdiction-dependent openings are not modelled.** The overlay prints a jurisdiction note per
  clause for the deal's governing law, and rules R04 and R14 react to the governing law, but the
  opening tier and the drafting text of a clause are the same whichever law governs the security.
  A real playbook would open differently in Zurich and in London.
- **`set_opening` currently changes nothing.** The action exists, is implemented and is
  tighten-only, but the opening starts at `preferred`, which is already the tightest tier, so the
  only rule that uses it (R06b) is logged as `R06b_concentration_severe (no change)`. Until a rule
  needs to open below `preferred`, the action is inert.
- **R04 fires on most English-law private-client deals.** Its trigger is a natural-person
  collateral provider plus English-law security, which is the ordinary shape of a private-wealth
  facility, so `fcar_safe_harbour_uncertain` is raised on the clean deal D01 as well as on D06.
  That is the rule working as written, but it means the flag carries little discriminating power
  as it stands, and its severity should be reconsidered once a human has read the England and
  Wales overlay against the rule's message. The honest fix is to the rule, not to the deal facts.
- **The Luxembourg natural-person scope point is an inference.** The overlay's treatment of
  whether a natural-person collateral provider sits inside the Luxembourg financial collateral
  regime is drawn from the structure of the legislation and from commentary, not from a primary
  text opened on that specific question, and it is marked accordingly. The parallel English point,
  that the Financial Collateral Arrangements (No. 2) Regulations 2003 require both parties to be
  non-natural persons, is sourced; the consequence usually drawn from it, that there is then no
  self-help appropriation at all, is not.
- **D04 escalates, and that was a design call.** D04's borrower has neither a high-net-worth nor a
  business-purpose declaration, so rule R03a raises `consumer_credit` at high severity and stops.
  The alternative was to give the borrower a declaration so the deal runs clean, at the cost of
  losing the only deal that exercises the consumer-determination stop. The stop was kept.
  `handoff/WP9.md` section 4 sets out both options and how to switch.
- **`docs/research/jurisdictions_research.md` contains three real names** (two law firms in source
  labels and one bank inside a case name) that the published library already neutralises by
  neutral citation. The denylist test ledgers those three hits by file and by term, so a new one
  fails the test and so does cleaning the file without deleting the ledger entry. They should be
  replaced.
- **Snapshots are brittle against library edits, by design.** Any change under `playbook/` changes
  the library hash and rewrites all twelve files under `tests/expected/`. Regenerate deliberately
  with `SBL_UPDATE_SNAPSHOTS=1 python -m pytest -q tests/test_golden_deals.py`, and read the
  Markdown diff rather than the JSON one.

## Where to go next

- `docs/demo_script.md` for the exact commands to run in front of someone, in order, and what to
  point at on screen.
- `docs/interview_walkthrough.md` for the three-minute script and the questions to expect.
- `docs/review_priorities.md` for what a human reviewer should read first, and why.
- `docs/not_automated_register.md` for the boundary of the tool.
- `docs/source_register.md` for every source, graded, with its retrieval date.
- `build_plan.md` for the specification, and `handoff/` for what each work package actually did,
  including where it diverged from the plan and what it was least sure of.
