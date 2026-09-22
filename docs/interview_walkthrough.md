# Interview walkthrough

Written to be said out loud. The three-minute script comes first, then eight questions I expect and
the answers I would give. Everything below is checkable against the repository as it stands: the
file names, the commands and the numbers are real.

Two standing caveats, which belong in the first thirty seconds rather than the last: this is a
demonstrator built from public sources, and every substantive position in it is still `draft`. It
carries no approval from anyone and it has not been validated against any institution's credit
policy, risk appetite or local counsel advice.

---

## The three-minute script

### 1. The problem (about forty seconds)

Securities-based lending negotiation repeats the same twenty-odd decisions on every deal. Can the
facility stay uncommitted. What is the cure period. Does the bank give notice before it sells. Can
this trustee actually charge the assets. The answers are usually consistent inside an institution,
but they live in a few senior lawyers' heads, so a deal lawyer under relationship-manager pressure
either interrupts someone senior or makes the call alone. Both failure modes are expensive: the
first burns the scarcest time in the department, the second erodes the bank's protection one deal
at a time with no institutional memory of why.

What I have built is the shape of the fix. Not a drafting tool and not an AI reviewer: a library of
lender-side positions with fixed escalation points, and a deterministic engine that reads the facts
of a deal and tells you which positions you may concede and which you may not.

### 2. The structure (about sixty seconds)

Every clause carries four tiers. `preferred` is the opening. `acceptable` is a routine concession
the deal lawyer can agree alone. `fallback` costs real protection, so it carries conditions and a
named approver. `unacceptable` is the walk-away line. The distinction that matters is not the
wording, it is **who may agree it** — that is the whole reason there are four tiers and not three.

Underneath sit eighteen rules, plus one built into the engine, that read a deal intake and tighten.
A rule can raise a floor, raise an opening, add a condition precedent or a representation, raise a
regulatory flag, or escalate. What a rule cannot do is loosen anything. That is not a policy I
enforce by convention, it is the semantics of the actions: tiers only tighten, so two rules can
never disagree and the order they run in cannot change the answer.

Let me show you one run.

```
python -m sbl run deals/D02_trust_concentrated_pdmr.yaml --out runs/
```

D02 is synthetic: a Jersey discretionary trust borrowing against a portfolio that is seventy per
cent one listed holding, where the trust is a person discharging managerial responsibilities in
relation to that same issuer. English law security, lender custody, sterling, uncommitted demand.
The command prints one line — twenty-four clauses, none reviewed, twelve draft and twelve stub, one
flag, two escalations, exit code 2 — and writes a Markdown markup and a JSON result next to an
append-only audit log.

Three things on the screen. **First**, the escalations are at the top, before any drafting: the
concentration rule sends the lending value to credit, and the insider rule sends the position to a
senior lawyer and compliance before a term sheet goes out. **Second**, every clause carries its
status tag, so `[DRAFT]` is printed next to the position rather than buried in a footnote, and the
header counts them. **Third**, the trace:

```
python -m sbl explain <run_id> enforcement_liquidation
```

That prints the library hash, the intake hash, the clause's opening and floor, and the rules that
moved it. On this deal the opening is `preferred`, the floor has been raised to `acceptable`, and
the single rule responsible is the insider rule. The trace is reconstructed from the audit line
alone, which is the point: if the output cannot be derived from the log, the log is not a record of
the decision.

### 3. The judgement call (about forty seconds — the important part)

The interesting work was deciding what the tool must never do. There is a register of it,
`docs/not_automated_register.md`: fifty-nine items harvested from the clause files and eight
system-level items. Two examples.

The tool never concludes that a borrower is or is not a consumer. It raises a flag, it escalates
where no high-net-worth or business declaration is recorded, and it names senior lawyer and
compliance as the deciders — but the determination itself turns on declarations and on the lender's
own state of mind about the borrower's purpose, and the threshold figures behind the flag are still
marked `[VERIFY]`.

And the tool never agrees a concession below a clause's floor. If a counterparty asks for a tier
below the floor the engine records it, escalates it and sets the exit code to 2. The floor is the
point at which the library stops deciding and a named person starts. Take that away and the
approver field means nothing.

The register is also honest about a third category: the decisions the tool does nothing about at
all. Forbearance on a live margin call, waiver of an event of default, and the decision to enforce
are taken after signature, against a live position, on facts that never appear in an intake file.

### 4. The honest caveat (about twenty seconds)

This is built from public sources — primary legislation, regulator texts, filed agreements on
EDGAR, published bank terms, some practitioner commentary — and every source is graded and dated in
`docs/source_register.md`. Every judgement number in it is an `X` rather than a figure, because no
public source I opened publishes one. Nothing has been reviewed by a named human, so nothing is
`reviewed`. Inside a bank the substance would have to be validated against that institution's own
credit policy and its local counsel, not against anything I could read on the internet.

---

## Eight questions I expect

### 1. Why four tiers and not three?

Because `acceptable` and `fallback` differ in who can agree them, not in how much they concede. A
routine concession the deal lawyer signs off alone and a concession that costs real protection are
different events in the bank's control environment, even where the drafting change is small. So
`fallback` carries two extra fields that `acceptable` does not: `conditions`, which must hold before
the tier is available at all, and `approval`, which names the person who has to sign. Collapse them
and you lose the record of who accepted the loss of protection, which is the only thing the ladder
is actually for. In the library those approvers genuinely differ by clause — time-based concessions
go to the head of credit, form-of-security questions to a senior lawyer, and the enforcement clause
to the credit committee because its fallback concedes a credit cost and a legal cost at once.

### 2. What happens when two rules disagree?

They cannot, and that is a design property rather than luck. Every tier action in the grammar is
tighten-only: `set_floor` and `set_opening` raise, never lower, so applying the rules in any order
produces identical floors and openings. There is a property test that runs the rule set in reverse
and asserts the same result. What you do get is two rules touching the same clause, and the log
records every one of them: on D02 the concentration rules and the insider rule all reach
`enforcement_liquidation` and `eligible_collateral_lending_values`, and `sbl explain` lists them.
The engine never has to pick a winner, which means there is no arbitration logic for anyone to
argue with later.

### 3. What would you never automate?

The register has the full list, but the two I would lead with are these. The final determination
that a borrower is or is not a consumer: the tool flags it, escalates it and names the decider, but
the conclusion depends on declarations and on what the lender had reasonable cause to suspect about
the purpose of the borrowing, and getting that wrong changes the regulatory character of the whole
facility. And any concession below a clause's floor: the engine records it and escalates it, and it
will never quietly accept it, because the floor is precisely the line where the library stops being
a decision-maker. I would add a third if there were time — forbearance on a live margin call — to
make the point that a large part of what a lawyer actually does on this product happens after the
document is signed, on facts no intake file contains.

### 4. How would this be validated inside a bank?

Nothing in the library is usable until a named human promotes it. Every entry carries `status`,
`reviewed_by` and `last_reviewed`, agents may only write `stub` or `draft`, and only a reviewer sets
`reviewed` — so the current state of this repository is twelve drafted clauses and twelve stubs,
none reviewed, and the output says so on every page. Each run records a library hash over the
sorted clause, rule, jurisdiction and flag files, and an intake hash, so you can always say which
version of the library produced a given markup. The validation itself would not be against my
sources: it would be the institution's credit policy for the numbers, its compliance function for
the flags, and local counsel for each jurisdiction overlay. The architecture is built so that work
is additive — you review entries one at a time and the status counts in the header go up.

### 5. SBL versus securities lending?

A securities-based loan is credit extended to a client against their existing investment portfolio,
where the securities stay pledged rather than being sold or transferred away and the client keeps
the economic upside and downside. Securities lending is the opposite kind of transaction: the
temporary transfer of the securities themselves, typically to a short seller or market maker under
a master securities lending agreement, in exchange for a fee, and it has nothing to do with lending
against a client's own wealth. Continental private banking calls the first one a Lombard loan, UK
and US practice call it securities-based lending or a margin loan, and they are the same product.

### 6. How do you know the law in the jurisdiction overlay is right?

I do not know it in the way a bank would need to, and the files say which parts I checked. Take one
I did check: under the English Financial Collateral Arrangements Regulations, regulation 3 requires
both parties to the arrangement to be non-natural persons, so a private client pledging their own
portfolio is outside the regime. That text was opened and read, it is graded A, `verified: true`,
and a rule raises a flag whenever a natural person provides collateral under English law. Now take
one I did not: the Luxembourg file says natural-person collateral providers **are** in scope, which
is the contrast that makes the whole overlay worth printing — and that conclusion is an inference
from two provisions rather than an express scope article, so it is marked `[VERIFY]` in the file and
`[VERIFY]` prints in the output. There are around a hundred `[VERIFY]` markers in the library and
they are all there for that reason. The honest answer is that the tool cites and local counsel
confirms, and the register exists so a reviewer can see exactly which of the two any given sentence
is.

### 7. Why not just use an LLM for the whole thing?

Because reading the counterparty's draft is the easy part. The hard part is that the same facts must
produce the same answer every time, that you must be able to show afterwards why a position was
taken, and that the escalation points have to be fixed in advance by a human rather than inferred at
run time. The engine here is deterministic, has no network calls, and renders its output from the
result object alone, so the markup cannot contain anything that is not in the log. Where a model
would earn its place is at the front door — mapping a counterparty's clauses onto library ids and
proposing intake facts for a human to confirm — and the plan for that keeps the model away from the
tiers entirely: it never sees the position text and it never chooses a tier. That is an optional
extension, and it is not built.

### 8. What is the most contested clause in practice, and where is your line?

Lender discretion over valuation and lending values. It is the clause that decides whether the bank
can reprice collateral risk the same day, which on an uncommitted facility is what the bank has
instead of covenants. The opening is unilateral discretion with immediate effect, which is the
position every published bank document I opened takes. The first concession I will make is a
standard rather than a delay — good faith and commercially reasonable, and the bank shows its
calculation — because that binds the bank to a process it follows anyway and gives up the word
"absolute" while keeping the timing, which is the part with economic value. The fallback is where
the line actually sits, and the entry's rationale puts it like this: the notice period is conceded
"in the only shape that survives contact with a falling market: a period for routine repricing, and
immediate effect for the four situations in which a period would cause the loss it is meant to
prevent." Put to the counterparty, the bank is saying it will not change the rules on you in a quiet
market without warning, but it will not stand still in a loud one. The carve-out I will not give up
is the one for an open margin call — without it the borrower can hold the bank to a stale lending
value for the length of the notice period, precisely while the collateral is deteriorating — and
that is why it appears in the `unacceptable` tier and in the escalation triggers as well as in the
fallback conditions.
