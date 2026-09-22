# Hand-off: WP3 drafting group A

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP3 for three of the core twelve clauses.
Everything in the repository is synthetic. Nothing here is legal advice. All three entries are
`status: draft`; nothing was set to `reviewed`; no `verified` flag copied from the shared source
pool was changed. Nine sources were opened by this agent and are recorded separately.

Clauses drafted (stub files overwritten in place, file names, ids and categories unchanged):

| # | file | id | category |
|---|---|---|---|
| 01 | `playbook/clauses/01_facility_type.yaml` | `facility_type` | credit |
| 02 | `playbook/clauses/02_conditions_precedent.yaml` | `conditions_precedent` | credit |
| 10 | `playbook/clauses/10_capacity_authority.yaml` | `capacity_authority` | parties_reps |

Also written: `docs/research/source_register_A.md` (fragment; nine new sources, two searches
recorded as deliberately not used). No other file in the repository was touched — in particular
nothing under `src/sbl/`, `tests/`, `playbook/rules/`, `playbook/flags/`, `playbook/jurisdictions/`
or any other clause file.

---

## 1. Acceptance output (pasted verbatim)

### 1.1 `.venv/Scripts/python -m sbl validate`

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: e60c01e49526e207af12b21b2fc8f0810137bc8805863502d84ae2ee1af189dc
exit code: 0
```

Exits 0. (One earlier failure, self-inflicted and fixed: a `counterparty_asks` item in clause 10
began `Trustee limited recourse: liability confined...`, which YAML parsed as a mapping rather than
a string. The loader caught it with a precise message — `field 'counterparty_asks.0': Input should
be a valid string` — which is the WP1 error design working. The item is now quoted.)

### 1.2 Group A assertion script

Script lives in the session scratchpad (`check_group_a.py`), not in the repository, per the brief.
It loads each file with `pyyaml` rather than with the `sbl` loader, deliberately, so the checks are
independent of the models. It asserts per file: `status == draft`; `reviewed_by` and
`last_reviewed` null; exactly four tiers, each with non-empty `text` and `rationale`; `fallback`
carries an `approval`; `unacceptable` carries no `conditions` and no `approval`; >= 3 sources with
>= 1 of reliability A or B and every source carrying a `note`; >= 2 `counterparty_asks`; exactly the
three `jurisdiction_notes` keys, all non-empty and all naming a real jurisdiction file; every
`depends_on` id exists as a clause file; every `regulatory_flags` id exists in the flags file;
>= 1 `not_automated` item; >= 1 escalation trigger; a sane `default_floor`.

```
$ .venv/Scripts/python <scratchpad>/check_group_a.py
01_facility_type.yaml: id=facility_type status=draft tiers=4 sources=9 (A=1, B=6, C=2) asks=6 depends_on=5 flags=2 not_automated=4 default_floor=acceptable
02_conditions_precedent.yaml: id=conditions_precedent status=draft tiers=4 sources=9 (A=4, B=4, C=1) asks=6 depends_on=5 flags=4 not_automated=6 default_floor=fallback
10_capacity_authority.yaml: id=capacity_authority status=draft tiers=4 sources=12 (A=8, B=3, C=1) asks=6 depends_on=5 flags=3 not_automated=6 default_floor=fallback

All group A assertions passed.
exit code: 0
```

### 1.3 Denylist check — clean

The brief's check, word-boundary aware and with `url:` lines excluded (this is the form group B
recommended; it is the check that actually answers "is there a real name in the drafted content?"):

```
$ grep -v -i "url:" playbook/clauses/01_facility_type.yaml playbook/clauses/02_conditions_precedent.yaml playbook/clauses/10_capacity_authority.yaml \
  | grep -n -i -w -E "societe|generale|ubs|credit suisse|julius|pictet|lombard odier|barclays|hsbc|coutts|goldman|morgan|citi|citibank|edmond|vontobel|efg|bnp|deutsche"
(no output; exit 1)
```

Clean. For completeness, the same grep **without** word boundaries and **without** excluding `url:`
lines returns 15 hits across the three files, every one of which is either (a) the substring `ubs`
inside an ordinary English word — `substance`, `substitute`, `substitution`, `substituting`,
`subsidiary`, `subsection` — or (b) one of two `url:` lines copied verbatim from the shared source
pool (`BANK-CH-01`'s Swiss factsheet and `BANK-US-01`'s margin lending page). `build_plan.md` §0
rule 2 expressly permits a publisher's domain inside a URL. This reproduces group B's finding
exactly and reinforces their recommendation to WP9/WP10: **make the repo-wide denylist check
word-boundary aware and exclude `url:` lines**, or it will report false failures on every clause
file in the library.

Separately confirmed by reading: no party name from any filed agreement appears anywhere in these
three files. Filed documents are referred to by what they are plus the EDGAR accession number, and
every ref label is neutral (`BANK-LU-01`, `EDGAR-PB-01`, `LAW-EW-03`, `FIRM-TR-01`, ...). No case
is cited by party name in these three clauses.

---

## 2. Least-confident positions, for Stuart's review priority

Two per clause, in the order I would review them.

### 10 `capacity_authority` — review this clause first

1. **`fallback` — full limited recourse with a carve-out only for fraud and wilful default.** This
   is the position I am least confident about in all three files. The concession itself is
   commercially normal and `FIRM-TR-01` records that nearly all professional trustees ask for it.
   What is *not* sourced is my judgement about where the line sits: I have kept personal liability
   for breach of the capacity representations in `acceptable` and given it away in `fallback`,
   because `FIRM-TR-01` says the lender cannot easily find out whether the trustee acted within its
   powers, which makes the representation the Bank's only real window. A reviewer could reasonably
   say the opposite — that a regulated institutional trustee plus a legal opinion is worth more than
   a representation, and the two tiers should be merged. If so, `default_floor` should move to
   `acceptable` and rules R01 and R05 (both of which `set_floor capacity_authority=acceptable`) would
   become no-ops on every deal, which WP5 must be told.
2. **`acceptable` — subrogation to the trustee's right of indemnity and lien.** I have drafted this
   as a term of the limitation, and it is the mechanism that makes the whole ladder coherent. I have
   **no source that a trustee will agree it** and no source that it works as drafted as a matter of
   law. `LAW-EW-04` establishes the indemnity exists; it says nothing about a lender being
   subrogated to it. Treat this sentence as a proposal, not a market position.
3. (Third, close behind.) The **partnership limb of `preferred`**, which asks for joint *and, where
   the constitution permits, several* liability. `LAW-EW-05` supports the agency analysis and nothing
   more; the liability point is drafting practice, and limited partnerships and LLPs are expressly
   out of scope and marked `[VERIFY]`.

### 01 `facility_type`

1. **`default_floor: acceptable`, and the reasoning behind it.** I have deviated from group B's
   uniform `fallback` on purpose (see §4.2). The argument is that moving from uncommitted demand to
   committed term changes the product rather than a term of it and should always escalate, and that
   no rule in `rules.yaml` tightens this clause's floor, so setting `acceptable` makes nothing inert.
   It is still a judgement, and it is the one structural decision in group A's files that a reviewer
   could simply reverse.
2. **`fallback` — the closed list of lender termination and mandatory prepayment events.** The
   *shape* is sourced (`EDGAR-ML-03`, `EDGAR-ML-04` are exactly this model) but the *contents* of my
   list are assembled by analogy, and two limbs are mine rather than the market's: "death or
   incapacity of the Borrower or any Pledgor" (borrowed from the private-bank event-of-default
   drafting at `EDGAR-PB-01-C`, which is a demand-facility document, not a term one) and "a fall in
   the price of any pledged security below the level stated in the facility letter" (the pool
   records an independent share-price trigger as a real feature but notes the intuition about its
   level is commentary only). The list is also the place where a term facility silently loses or
   keeps protection, so it deserves a line-by-line read against clause 08.

### 02 `conditions_precedent`

1. **`fallback` — the Part 1 / Part 2 split with an X business day longstop for Part 2.** **No
   source opened concedes a post-closing longstop for conditions precedent at all.** The whole shape
   is mine. I believe the test that draws the line ("can this item still be fixed the day after the
   money moves?") is right and is defensible out loud, but a reviewer should decide whether a private
   bank would offer a two-part schedule at all rather than simply waiving items case by case, which
   is what the published retail document effectively does.
2. **`acceptable` — the undertaking to confirm satisfaction within X business days.** Not observed
   anywhere. I added it because a reasonableness qualifier on its own gives the Borrower nothing it
   can plan around, and timing certainty is what the Borrower actually wants at this point in the
   deal. It is a small commitment with an operational cost that credit and operations, not legal,
   should price.
3. (Third, close behind.) Whether `reps_source_of_funds_sanctions_tax` belongs in `depends_on`. It is
   a deferred stub, so the markup will print `[STUB]` next to it; I included it because the KYC and
   source-of-funds conditions in this clause are the drafting counterpart of those representations.

---

## 3. Every `[VERIFY]` introduced

No `[VERIFY]` was added to a statement that a source in the pool, or a source this agent opened,
already supports. The markers fall into three groups.

### (a) Judgement numbers. Every `X` in these three files is commented on the line above the field.

| file | `X` | what the comment records |
|---|---|---|
| 01 | notice period in days before cancellation for convenience (`acceptable`, and in `escalation_triggers`) | 90 days in one published Luxembourg template (`BANK-LU-01`) is the **only** notice period observed; every other published document concedes none |
| 01 | term length in months (`fallback`) | up to 24 months for a Swiss fixed advance (`BANK-CH-01`); the filed term facilities state a maturity but the pool does not record the tenor |
| 01 | trading-suspension threshold in trading days (`fallback`) | named as a mandatory prepayment event but **no opened source publishes the number** (`FIRM-01`, `EDGAR-ML-04`) |
| 02 | business days for the Bank to confirm CP satisfaction (`acceptable`) | **not observed in any source**; added to make the concession administrable |
| 02 | business days to deliver Part 2 items (`fallback`) | **no source opened concedes a post-closing CP longstop at all**; nearest analogue in the pool is a 15-day notice concession on an unrelated clause |

### (b) The known gaps the brief names, and what was done about them

- **Trustee power to borrow or charge, and limited-recourse doctrine.** Rather than mark clause 10
  `[VERIFY]` throughout, I opened primary legislation and one law-firm briefing: Trustee Act 1925
  s.16 (statutory power to raise money by sale, conversion, calling in or mortgage where trustees are
  authorised to pay or apply capital money, notwithstanding anything to the contrary in the
  instrument, excluding charitable and SLA settlement trustees); Trustee Act 2000 s.31 (reimbursement
  from trust funds for expenses **properly** incurred); Partnership Act 1890 s.5; Companies Act 2006
  ss.39, 40, 172 and 678; and an offshore law-firm briefing on lending to trustees that supplies the
  lender-side treatment of the indemnity and of limited recourse. All nine are recorded in
  `docs/research/source_register_A.md` with what each supports. The head of clause 10 carries a
  20-line comment mapping each proposition to its source and naming what is still unsourced, so a
  later reader cannot mistake a sourced sentence for an unsourced one.
- **Incapacity short of death.** Not stated as law anywhere in these files. It appears only in
  `not_automated` on clause 10, which says in terms that the intake records no fact that answers it
  and that the treatment of incapacity is an identified gap in this library.
- **Swiss governing-law / jurisdiction practice, numeric concentration caps, lending-value grids,
  MiFID II / FinSA primary text, and the English FCAR natural-person exclusion consequences.** None
  of these is asserted in group A's files. The FCAR natural-person point is *used* in clause 02's
  England and Wales note, but only in the form the primary text supports (the regime requires both
  parties to be non-natural persons, per `LAW-EW-01` reg. 3, so the registration disapplication in
  `LAW-EW-02` reg. 4(4) cannot be relied on) plus a practical instruction to register protectively
  where there is doubt. No consequence beyond that is claimed.

### (c) In-text `[VERIFY]` prefixes

| file | field | what is marked and why |
|---|---|---|
| 02 | `jurisdiction_notes.switzerland` | The FISA statutory routes to a security interest over intermediated securities, the custodian's own statutory right of retention and foreclosure, and the writing/not-in-GTCs requirement for a right-of-use authorisation. These come from `docs/research/jurisdictions_research.md` (WP7), not from a document this agent opened, and no pool source covers them. The sentence names its provenance. |
| 02 | `jurisdiction_notes.luxembourg` | Only the art. 26 "no registration formalities" point. Art. 26 is **not** among the articles the sourcing agent recorded as read (arts. 3-5, 11, 12, 13, 13-1, 18-20, 22) and was not opened by this agent. The rest of that note rests on arts. 5(2)(a) and 2(3), which are inside the read range, and the `LAW-LU-01` source note says exactly which part it does and does not support. |
| 10 | `jurisdiction_notes.england_wales` | Two marks: (i) limited partnerships and limited liability partnerships, governed by statutes not opened, with an express instruction not to apply the Partnership Act analysis to them; (ii) the undue influence and independent legal advice case law behind the `unacceptable` tier — standard practice, but no case was read. |
| 10 | `jurisdiction_notes.switzerland` | Whole note. Swiss upstream and cross-stream security and capital-maintenance restrictions, and the FISA right-of-use form requirement. Neither was researched here and `playbook/flags/regulatory_flags.yaml` records the same gap for the `financial_assistance_corporate_benefit` flag. Written as an instruction to treat it as a local counsel question rather than as a statement of law. |
| 10 | `jurisdiction_notes.luxembourg` | The last sentence only: Luxembourg corporate benefit and financial assistance restrictions on a corporate pledgor were not researched. The rest of the note rests on `LAW-LU-01` art. 12 (inside the read range) and on `BANK-LU-01`. |
| 10 | header comment | Lists, in one block, everything in the clause that remains unsourced: trust law outside England and Wales except the Jersey/Guernsey limited-recourse point; LPs and LLPs; Swiss and Luxembourg corporate benefit; undue influence doctrine; incapacity short of death. |

---

## 4. Deviations from the plan or schema, and why

1. **Nine new sources opened, eight of them for clause 10.** The brief permits this and the clause
   is the designated thin-coverage entry. Seven are primary law on legislation.gov.uk and grade A;
   one is a law-firm briefing and grades C; one (FCARs reg. 4) is for clause 02. All are in
   `docs/research/source_register_A.md` with the provision actually read. Two of them — Companies Act
   2006 ss.678 and 172 — are already recorded in the flags file by the WP8 agent; the fragment flags
   that so the consolidating agent merges rather than duplicates.
2. **`default_floor: acceptable` on clause 01, against group B's uniform `fallback`.** Argued in the
   `fallback` rationale in the file itself, as the brief requires. The structural check group B
   raised holds the other way here: **no rule in `rules.yaml` performs `set_floor` on
   `facility_type`**, so raising the default floor makes no rule inert. Clauses 02 and 10 use
   `fallback`, and on clause 10 that is load-bearing — R01 and R05 both tighten it to `acceptable`,
   and a default of `acceptable` would make both no-ops.
3. **Clause 10's fallback approver is `senior lawyer + head of credit`, a compound role.** Group B
   used single roles. Giving up personal recourse against a trustee is simultaneously a validity
   question (is the route to the trust fund intact?) and a risk-appetite question (what does the
   lending value have to carry instead?), and naming only one of them would put the decision in the
   wrong place. Clause 01 uses `credit committee`; clause 02 uses `senior lawyer`. If the house
   convention is single roles, clause 10 should read `senior lawyer`, with credit consulted under the
   last of its fallback conditions.
4. **`document: all` on clause 10.** The only one of group A's three not in the facility letter
   alone: the capacity evidence is gated by conditions precedent in the facility letter and the
   representations are repeated in the security agreement, so neither value alone is honest. Clauses
   01 and 02 are `facility_letter`.
5. **Clause 02 is drafted explicitly as a base list that the rules extend, and says so in a 30-line
   header comment.** The comment names the rules that appended CPs to this clause as at drafting
   (R01, R02, R05b, R07, R08, R12) and the two that append notes rather than CPs (R03, R03b, and R05),
   says that WP5 owns that list, and warns against duplicating a rule's CP in the tier text because
   the markup would print it twice. The `preferred` text is written so the list is open — limb (i) is
   the sweeper and the text refers to conditions the Bank notifies — and the `fallback` tier's Part 1
   is defined so that no rule and no deal team can move a hard-core item into Part 2.
6. **`depends_on` includes deferred stubs.** Clause 01 depends on `prepayment_breakage`, clause 02 on
   `reps_source_of_funds_sanctions_tax`, clause 10 on `third_party_security_waivers`. All three exist
   as `status: stub` files, the loader accepts them and `sbl validate` is green; flagged because the
   markup (WP6) will print a `[STUB]` tag next to them.
7. **Clause 01 carries a long header comment.** It sets out the ladder and then answers, in six
   lines, *why demand drives enforcement* — the point `build_plan.md` §3 gives as the reason this is
   clause 1, and a likely interview question. It is a comment, so it never reaches the rendered
   markup.
8. **`lender_objective` rewritten on all three** (WP1 §5.5 invites this). `id`, `title`, `category`
   and file names are unchanged on all three.
9. **One search was blocked and one PDF was unreadable**, both while trying to close the trustee gap;
   neither is cited and no proposition rests on either. Recorded in
   `docs/research/source_register_A.md` §"Searches run and deliberately not used" so the next agent
   does not repeat them.

---

## 5. Notes for the WP5, WP6 and WP9 agents

- **WP5.** Clause 02's tier text is deliberately written to be *extended* by `require_cp`, not to
  restate rule CPs. If a rule's CP text starts duplicating a limb of the `preferred` list, change the
  rule, not the clause: the markup prints both. Also note the floor interaction in §4.2 above before
  changing any `set_floor` targeting `facility_type` or `capacity_authority`.
- **WP6.** Clause 10's `fallback` approval string contains a `+`. If the renderer formats approvers
  as a single role token, it will need to handle that, or clause 10 should be changed per §4.3.
- **WP9/WP10.** The repo-wide denylist check must use word boundaries and skip `url:` lines. Both
  group A and group B have now independently produced the same false positives (`substance`,
  `subsidiary`, `substitute`, `subsection` all contain `ubs`), and both groups' files carry publisher
  domains inside `url:` fields that `build_plan.md` §0 rule 2 expressly permits.
