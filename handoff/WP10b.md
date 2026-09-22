# Hand-off: WP10b (README and demo script)

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP10, the README and demo-script half.

Everything in this repository is synthetic. Nothing here is legal advice. No entry was set to
`reviewed`; no new legal statement and no new source was written by this work package. Nothing
under `playbook/`, `src/`, `deals/` or `tests/` was touched, so `library_hash` is unchanged at
`5752d729a3dff7423c13d6b99f6021ab3662a1175ad60049c069b9bc5347247d`.

Files owned and written:

```
README.md              rewritten in full (the WP0 scaffold is gone)
docs/demo_script.md    new
handoff/WP10b.md       this file
```

`docs/not_automated_register.md`, `docs/source_register.md`, `docs/interview_walkthrough.md`,
`docs/review_priorities.md` and `docs/research/*` belong to the concurrent WP10a agent and were
read but not edited.

---

## 1. Acceptance output (pasted verbatim)

### 1.1 Following the README from a clean state, timed

Clean state established with `Remove-Item -Recurse -Force runs`, then the README's documented
commands run in order in a fresh PowerShell 5.1 session. The venv was created at a scratchpad path
rather than at `F:\SBL_Legal\.venv`, so that the repository's working venv was not destroyed while
another agent was live in the repo; the two commands run are otherwise exactly the README's, and
they installed from `F:\SBL_Legal` in editable mode. This is the stronger test of the two available:
it proves `pip install -e ".[test]"` works into a venv built from scratch, rather than reusing the
environment the build already happened in.

```
--- 0. clean state: Remove-Item -Recurse runs ---
runs/ exists after delete: False

--- 1. python -m venv .venv   (fresh venv, see note) ---
exit=0   elapsed=6.8s

--- 2. .venv\Scripts\pip install -e ".[test]" ---
Obtaining file:///F:/SBL_Legal
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Checking if build backend supports build_editable: started
  Checking if build backend supports build_editable: finished with status 'done'
  Getting requirements to build editable: started
  Getting requirements to build editable: finished with status 'done'
  Preparing editable metadata (pyproject.toml): started
  Preparing editable metadata (pyproject.toml): finished with status 'done'
Collecting pyyaml (from sbl==0.1.0)
  Using cached pyyaml-6.0.3-cp312-cp312-win_amd64.whl.metadata (2.4 kB)
Collecting pydantic>=2 (from sbl==0.1.0)
  Using cached pydantic-2.13.5-py3-none-any.whl.metadata (110 kB)
Collecting pytest (from sbl==0.1.0)
  Using cached pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2->sbl==0.1.0)
  Using cached annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.46.5 (from pydantic>=2->sbl==0.1.0)
  Using cached pydantic_core-2.46.5-cp312-cp312-win_amd64.whl.metadata (6.7 kB)
Collecting typing-extensions>=4.14.1 (from pydantic>=2->sbl==0.1.0)
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting typing-inspection>=0.4.2 (from pydantic>=2->sbl==0.1.0)
  Using cached typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)
Collecting colorama>=0.4 (from pytest->sbl==0.1.0)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting iniconfig>=1.0.1 (from pytest->sbl==0.1.0)
  Using cached iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting packaging>=22 (from pytest->sbl==0.1.0)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.5 (from pytest->sbl==0.1.0)
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting pygments>=2.7.2 (from pytest->sbl==0.1.0)
  Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Using cached pydantic-2.13.5-py3-none-any.whl (472 kB)
Using cached pydantic_core-2.46.5-cp312-cp312-win_amd64.whl (2.0 MB)
Using cached pytest-9.1.1-py3-none-any.whl (386 kB)
Using cached pyyaml-6.0.3-cp312-cp312-win_amd64.whl (154 kB)
Using cached annotated_types-0.8.0-py3-none-any.whl (13 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pluggy-1.6.0-py3-none-any.whl (20 kB)
Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Using cached typing_inspection-0.4.4-py3-none-any.whl (14 kB)
Checking if build backend supports build_editable: started
Checking if build backend supports build_editable: finished with status 'done'
Building wheels for collected packages: sbl
  Building editable for sbl (pyproject.toml): started
  Building editable for sbl (pyproject.toml): finished with status 'done'
  Created wheel for sbl: filename=sbl-0.1.0-0.editable-py3-none-any.whl size=1463 sha256=bb573307a0c77f95ed8cc52d0e31e2ae39050601d39bca8e1a7eecdbea40a8e0
  Stored in directory: C:\Users\forwa\AppData\Local\Temp\pip-ephem-wheel-cache-7dshhtfg\wheels\de\67\d1\e3647e11a286893b28e64dc30eda670882496f4e47e192b788
Successfully built sbl
Installing collected packages: typing-extensions, pyyaml, pygments, pluggy, packaging, iniconfig, colorama, annotated-types, typing-inspection, pytest, pydantic-core, pydantic, sbl
Successfully installed annotated-types-0.8.0 colorama-0.4.6 iniconfig-2.3.0 packaging-26.3 pluggy-1.6.0 pydantic-2.13.5 pydantic-core-2.46.5 pygments-2.21.0 pytest-9.1.1 pyyaml-6.0.3 sbl-0.1.0 typing-extensions-4.16.0 typing-inspection-0.4.4
exit=0   elapsed=22.0s

--- 3. python -m sbl validate --summary ---
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 5752d729a3dff7423c13d6b99f6021ab3662a1175ad60049c069b9bc5347247d

kind              stub   draft  reviewed   total
------------------------------------------------
clauses             12      12         0      24
rules                0      18         0      18
flags                0      10         0      10
jurisdictions        0       3         0       3

Entries not marked 'reviewed' have not been checked by a named human reviewer.
exit=0   elapsed=25.0s

--- 4. python -m sbl run deals/D02_trust_concentrated_pdmr.yaml --out runs/ ---
D02 run 84d70a5d862b | 24 clauses (0 reviewed / 12 draft / 12 stub) | 1 flags | 2 escalations | exit 2 | wrote D02_84d70a5d862b.json, D02_84d70a5d862b.md, audit.jsonl
exit=2   elapsed=27.9s
rendered markup: D02_84d70a5d862b.md   run_id: 84d70a5d862b

--- 5. python -m sbl explain 84d70a5d862b enforcement_liquidation --audit runs/audit.jsonl ---
Run 84d70a5d862b - deal D02
Timestamp:    2026-09-21T16:51:38.147480+00:00
Library hash: 5752d729a3dff7423c13d6b99f6021ab3662a1175ad60049c069b9bc5347247d
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

exit=0   elapsed=28.2s

=== clone-to-rendered-D02 total: 28.2s (0.5 min) ===
```

**Time from a clean state to a rendered D02 markup, including building the virtual environment
and installing the package: 28.2 seconds.** `build_plan.md` §6 WP10 asks for under ten minutes.
Every documented command worked as documented and produced the documented exit code (0, 0, 0, 2,
0 in order; the 2 is D02's escalation, which is the designed result).

### 1.2 `powershell -ExecutionPolicy Bypass -File check.ps1` — exits 0

```
=== SBL Negotiation Playbook Demonstrator: check ===
interpreter: .venv\Scripts\python

--- 1/3  sbl validate ---
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 5752d729a3dff7423c13d6b99f6021ab3662a1175ad60049c069b9bc5347247d

--- 2/3  pytest -q ---
........................................................................ [ 18%]
........................................................................ [ 36%]
........................................................................ [ 54%]
........................................................................ [ 73%]
........................................................................ [ 91%]
..................................                                       [100%]
394 passed in 38.66s

--- 3/3  sbl run (each deal into runs/) ---
D01 run a5fe85079ebe | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 0 escalations | exit 0 | wrote D01_a5fe85079ebe.json, D01_a5fe85079ebe.md, audit.jsonl
D02 run d65414228dc3 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 1 flags | 2 escalations | exit 2 | wrote D02_d65414228dc3.json, D02_d65414228dc3.md, audit.jsonl
D03 run de2ae2904c07 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 0 escalations | exit 0 | wrote D03_de2ae2904c07.json, D03_de2ae2904c07.md, audit.jsonl
D04 run d7f6f51417dd | 24 clauses (0 reviewed / 12 draft / 12 stub) | 1 flags | 1 escalations | exit 2 | wrote D04_d7f6f51417dd.json, D04_d7f6f51417dd.md, audit.jsonl
D05 run 858b08d96c60 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 3 flags | 1 escalations | exit 2 | wrote D05_858b08d96c60.json, D05_858b08d96c60.md, audit.jsonl
D06 run 0a60b723ea6b | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 1 escalations | exit 2 | wrote D06_0a60b723ea6b.json, D06_0a60b723ea6b.md, audit.jsonl

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

394 tests, up from the 391 WP9 recorded, because `tests/test_denylist.py` runs one parametrised
case per scanned file and `docs/` has gained files since. The denylist sweep covers `README.md`,
so the rewritten README is confirmed free of every denylisted name.

### 1.3 The demo script's own commands

Every command in `docs/demo_script.md` was run before it was written down, and the one-line
summaries and the `explain` output in it are copied from those runs, not composed:

```
D01 run 18088da25cb0 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 0 escalations | exit 0 | wrote D01_18088da25cb0.json, D01_18088da25cb0.md, audit.jsonl
exit=0
D06 run c5227ea56800 | 24 clauses (0 reviewed / 12 draft / 12 stub) | 2 flags | 1 escalations | exit 2 | wrote D06_c5227ea56800.json, D06_c5227ea56800.md, audit.jsonl
exit=2
```

Every section heading, clause title, floor value, `Rules applied` line, flag id, escalation row
and drafting note quoted in the demo script was read out of a rendered `runs/*.md` from those
runs. The `Counterparty request outcomes` table and the R16 drafting note in step 3 are verbatim
from `runs/D06_c5227ea56800.md`.

---

## 2. What is in the README, and where each part came from

| Section | Source |
|---|---|
| Disclaimer block | `build_plan.md` §0 rules 2, 3, 8; the markup footer in `src/sbl/markup.py` |
| "What this is" | one-paragraph compression of `docs/product_definition.md` |
| "What the tool does" | four sentences: library and intake, deterministic engine, markup and audit log, tighten-only plus explicit escalation |
| "How to run" | commands verified by running them; flag names read off `src/sbl/cli.py` |
| Install caveat | `handoff/WP1.md` §4.1, plus the fresh-venv result in §1.1 above |
| Repository layout | the actual tree, listed on disk |
| Status counts | pasted from a real `python -m sbl validate --summary` |
| "Reading the output" | `src/sbl/markup.py` guarantees, `handoff/WP5.md` §2 and §4, `handoff/WP6.md` |
| "What is not automated" | `build_plan.md` §7, pointing at `docs/not_automated_register.md` |
| "Known limitations" | `handoff/WP9.md` §3, §4, §6, §7; `handoff/WP5.md` §6 |

The CLI flags in the README were confirmed against `src/sbl/cli.py`, not assumed: `validate`
takes `--summary`; `run` takes one or more deal paths plus `--out` and `--echo`; `explain` takes
`run_id` and `clause_id` positionally plus `--audit`, which defaults to `<root>/runs/audit.jsonl`.
There is also a global `--root`, which the README does not mention because nothing in the
documented walkthrough needs it.

No em-dash or en-dash appears anywhere in `README.md` (checked by grep). No real institution,
firm or person is named in either file.

## 3. Deviations

**3.1 The acceptance venv was built at a scratchpad path, not at `F:\SBL_Legal\.venv`.** A WP10a
agent was editing `docs/` concurrently and `check.ps1` prefers `.venv`, so destroying and
rebuilding the repository venv mid-flight would have been reckless for no gain. The two install
commands run are the README's, executed against `F:\SBL_Legal` in editable mode, and the
subsequent `validate`, `run` and `explain` all ran on that fresh interpreter from the repository
root. The repository's own `.venv` was left alone and `check.ps1` used it afterwards.

**3.2 `runs/` was deleted as part of the acceptance run.** It is gitignored and regenerable. It
has since been repopulated by the demo-script runs and by `check.ps1`, so it now holds one run per
deal plus the D01, D02 and D06 runs quoted above, and an `audit.jsonl` containing all of them.

**3.3 The README points at `docs/review_priorities.md`.** That file is WP10a's and exists on disk,
but this work package did not read it and cannot vouch for what is in it.

## 4. What could not be verified

1. **`pip install -e .` into the system Python.** `handoff/WP1.md` §4.1 records that this failed on
   a Windows file-permission error while replacing a console script under `C:\Python312\Scripts`.
   This work package did not retry it, because the failure is a write-permission problem with the
   machine's system Python rather than anything about the package, and retrying it from the same
   sandbox would fail the same way. What §1.1 above does prove is that `pip install -e ".[test]"`
   works cleanly into a venv created from nothing, which is the part that was in doubt about the
   packaging. **The README says in terms that a plain `pip install -e .` into your own Python
   should be confirmed by the user and that a failure there is a real failure, not a known one.**
   That sentence is still live and is the one thing in the README a reader should test first.
2. **`check.sh` on a POSIX shell.** The README and the demo script both offer it as the non-Windows
   twin of `check.ps1`. Only `check.ps1` was run here. `handoff/WP9.md` §1 records `sh check.sh`
   passing under Git Bash at the time WP9 landed, and §7 item 6 records that the two scripts are
   kept in step by hand, so a drift between them would not be caught by anything.
3. **The Linux and macOS install line** (`.venv/bin/pip install -e ".[test]"`) is given in the
   README by construction from the Windows one. No POSIX machine was available.
4. **Everything the README says about the law.** The README asserts no legal proposition of its
   own. Where it characterises one, for example the Financial Collateral Arrangements (No. 2)
   Regulations 2003 requiring both parties to be non-natural persons, it is reporting what
   `playbook/jurisdictions/england_wales.yaml` says and attributing it there. The Luxembourg
   natural-person point is described in the README as an inference because that is how
   `handoff/WP7_research.md` and the overlay present it; this work package did not open any
   primary text to check either.
5. **Whether `docs/not_automated_register.md` still matches the README's summary of the
   system-level items.** The README's list is taken from `build_plan.md` §7, which is the
   specification for that register, not from the register itself, because WP10a was rewriting it
   concurrently. If WP10a's register diverges from §7, the README's paragraph should be
   re-checked against it.

## 5. Lowest-confidence items, in priority order

1. **The status-count block in the README goes stale on any `playbook/` edit.** It is pasted
   output, and the library hash inside it moves whenever a clause, rule, flag or jurisdiction file
   changes. The README says so in terms immediately underneath, and says to run the command, but
   there is no test that the pasted block matches reality. If anyone wants one, the cheapest
   version is a test that greps the README for the current `library_hash` and fails when it has
   moved.
2. **Run ids in `docs/demo_script.md` will never match what the presenter sees.** `run_id` is
   derived from the timestamp, so every run is different. Each expected-summary block in the demo
   script says "run id will differ" and the `explain` step tells the reader to substitute their
   own, but somebody reading quickly under demo pressure could still be tripped by it. The
   alternative, leaving the id out, loses the point that the id is what ties the markup to the
   audit line.
3. **The README describes `set_opening` as inert.** That is true of the current rule set: the only
   rule using it is R06b, and it sets an opening to `preferred`, which is already where openings
   start. If a future rule sets an opening to `acceptable` or lower, the sentence becomes wrong and
   nothing will catch it, because no test asserts that openings never move.
4. **"Twelve of the twenty-four clauses are `[STUB]`"** in the README's "Reading the output"
   section is a count as at this hand-off. It is also in the pasted `validate --summary` block a
   few lines above, so the two go stale together, but the prose sentence is the one a reader will
   trust without re-running anything.
5. **The demo script's clause-by-clause pointers assume the current clause text.** Floors, the
   `Rules applied` lines and the exact wording of the R16 drafting note are quoted from live runs,
   so any WP3 review that changes a clause's `default_floor`, or any rule change, can silently
   falsify a pointer. The golden tests will catch the underlying change; nothing connects that
   back to this document. Re-read the demo script after any `playbook/` edit before demoing off
   it.
