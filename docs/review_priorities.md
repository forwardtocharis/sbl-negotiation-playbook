# Review priorities

For Stuart. One prioritised list of everything the build agents said they were least confident
about, harvested from the hand-off notes in `handoff/` (clauses WP3 A-D, rules WP5 and WP5b,
jurisdictions WP7, flags WP8, plus the schema and renderer notes from WP1 and WP6).

**Ordering.** Load-bearing first, on this test: does it fire on a golden deal, does it move a floor,
or is it only text. Band 1 items change what comes out of `python -m sbl run` on one of the six
deals in `deals/`, so a wrong answer there is a wrong answer in the demo. Band 2 items set or move
a floor but nothing in `deals/` triggers them. Band 3 is drafting and labelling, which matters for
credibility rather than for output.

Every entry is one line: what to look at, where, and why it is uncertain. The deal ids in brackets
are the golden deals the item actually reaches, taken from the run outputs rather than from the
plan.

---

## Band 1 - fires on a golden deal

### Consumer credit (D01, D04, D05, D06 - four of the six deals)

1. `playbook/flags/regulatory_flags.yaml` - `consumer_credit.description`: the four UK exemption
   threshold figures were read off live pages on one day and are not monitored, and the
   business-purpose presumption is stated without the "reasonable cause to suspect" evidential
   practice, which is where the exemption actually fails in a private bank. WP8's own third item.
2. `playbook/rules/rules.yaml` - `R03a` / `R03b` `sources`: `[VERIFY] SBL-RULE-GAP-03`, the
   continuing reach of the unfair-relationship powers to an exempt agreement and Luxembourg's
   transposition of the 2023 consumer credit directive, neither researched by any agent.
3. `playbook/rules/rules.yaml` - `R03a` vs `R03b` split: R03a escalates and R03b does not, so the
   presence or absence of a declaration in the intake decides the exit code on four deals.

### English financial-collateral safe harbour (D01, D05, D06)

4. `playbook/jurisdictions/luxembourg.yaml` - `financial_collateral_regime`: natural persons being
   in scope is an inference from Arts 2(1) and 20(4), not an express scope provision, and the
   corroborating source was never opened. WP7 calls this the highest priority of anything it wrote,
   and it is the contrast that makes the whole overlay worth printing.
5. `playbook/flags/regulatory_flags.yaml` - `fcar_safe_harbour_uncertain.description`: the gate
   itself (reg 3, both parties non-natural persons) is read and grade A, but the *consequence* of
   falling outside the regime is `[VERIFY]` in clauses 06, 07 and 09 and was deliberately not
   researched.
6. `playbook/clauses/07_security_structure_control.yaml` - `positions.fallback`: the two-party
   pledge plus custodian acknowledgement is a statutory route in Luxembourg, probably unavailable in
   England, and a different instrument in Switzerland; the tier is held together by a local-counsel
   condition rather than by being forked per jurisdiction. See design question 1.

### Concentration (D02)

7. `playbook/rules/rules.yaml` - `R06.when` and `R06b.when` values 25 and 50: no opened source
   supports either figure, and together they raise two floors and send the lending value to credit.
   WP5b's third item and the most likely thing in the file to be both wrong and noticed.
8. `playbook/clauses/04_concentration_limits.yaml` - `positions.fallback`: gives up insufficient
   diversification as a stand-alone realisation trigger, which the published Luxembourg template
   retains. If you disagree it belongs in `unacceptable` and the clause's `default_floor` moves to
   `acceptable`.
9. `playbook/clauses/04_concentration_limits.yaml` - `positions.acceptable`: carrying the excess
   over the single-name limit at a reduced lending value rather than disregarding it; no source
   supports either treatment as the norm.

### Trusts (D02)

10. `playbook/rules/rules.yaml` - `R01_trust_borrower` `rationale` and `sources`: the central
    assertion, that the trustee's indemnity is what connects the trust assets to the debt, rests on
    general practice; the rule's only verified source is a filed agreement supporting the document
    asks. WP5b's first item.
11. `playbook/clauses/10_capacity_authority.yaml` - `positions.fallback`: full limited recourse
    carved back only for fraud and wilful default. WP3 group A's least-confident position in all of
    its three files. If you merge it with `acceptable`, `default_floor` moves and R01's and R05's
    `set_floor capacity_authority=acceptable` become no-ops on every deal.
12. `playbook/clauses/10_capacity_authority.yaml` - `positions.acceptable`: subrogation to the
    trustee's right of indemnity and lien. No source that a trustee would agree it and none that it
    works as drafted; the drafter asks that it be read as a proposal.

### Insider / PDMR (D02)

13. `playbook/rules/rules.yaml` - `R07_pdmr_pledged_issuer` message: the EUR 5,000 / EUR 20,000
    figures come from a retained-EU instrument on legislation.gov.uk; whether those are the operative
    onshored figures and whether the uplift has been exercised is unconfirmed, and it is exactly the
    kind of detail an interviewer probes.
14. `playbook/clauses/09_enforcement_liquidation.yaml` - `positions.fallback` notice period `X`: the
    whole tier rests on one sub-document of one composite filing, and R07 raises this clause's floor
    on D02.
15. `playbook/clauses/09_enforcement_liquidation.yaml` - `positions.acceptable`: a commercially
    reasonable covenant paired with the full set of pre-agreed acknowledgements of what is
    commercially reasonable. No opened source has both in that combination, and a counterparty could
    argue the list guts the standard. WP3 group C calls it the position most in need of a lawyer's
    eye rather than a credit officer's.

### Third-party security and third-party custody (D04)

16. `playbook/rules/rules.yaml` - `R05_third_party_security`: the independent-advice requirement has
    no authority behind it; `[VERIFY] UK-ILA-01` has been open since WP7 and nobody has closed it.
17. `playbook/jurisdictions/england_wales.yaml` - `practical_notes` item 6: the same independent
    legal advice point, unsourced, and the one place in the overlay a reader might take it as advice
    on protecting a security against undue influence.
18. `playbook/clauses/07_security_structure_control.yaml` - `positions.fallback` substitution
    allowance `Y`: no opened source concedes uncontrolled substitution at all; the private-bank
    documents refuse it. R12 raises this clause's floor on D04.

### Swiss booking and committed term (D03)

19. `playbook/rules/rules.yaml` - `R14_swiss_booking`: asserts criminal-law consequences from a
    German-language official text, read in translation by the research agent because no English
    version was found at that identifier.
20. `playbook/jurisdictions/switzerland.yaml` - `enforcement_route` and `practical_notes` item 3:
    that private realisation survives the provider's insolvency. The orthodox reading, and the
    article text was read, but the practitioner overview does not spell out the interaction with the
    general debt-enforcement rule and a bank would not enforce on this analysis alone.
21. `playbook/clauses/12_no_advice_non_reliance.yaml` - `positions.unacceptable`: refusing any
    contractual duty to warn of an impending shortfall. Right for an execution-only relationship;
    less clearly holdable on a Swiss booking, where a notification duty may arise independently of
    the contract. Needs a Swiss reviewer before it goes in front of a Swiss client.
22. `playbook/clauses/12_no_advice_non_reliance.yaml` - `positions.fallback`: trading the
    sophisticated-investor limbs for a documented suitability file. No source concedes either ask and
    none describes the trade; the `X days` for the age of the assessment has no observed analogue.
23. `playbook/clauses/11_governing_law_jurisdiction.yaml` - `positions.fallback`: conceding mutual
    exclusive jurisdiction, which all four private-bank documents opened for this playbook refuse.
    If the asymmetry is what actually gets the bank paid, this belongs in `unacceptable`.
24. `playbook/clauses/11_governing_law_jurisdiction.yaml` - `positions.preferred`: splitting
    governing law between the facility letter and the security agreement. Legally right and sourced
    to primary text, but drafted against the observed market convention of one law for the package.
25. `playbook/jurisdictions/switzerland.yaml` - `governing_law_of_intermediated_securities`: the
    chain is sound article by article but has not been seen applied to a facility of this kind, and
    the qualifying-office condition is stated only in summary.
26. `playbook/rules/rules.yaml` - `R13_currency_mismatch`: `[VERIFY] SBL-RULE-GAP-06`, no opened
    source says which party bears a conversion shortfall on enforcement; and `derived.currency_mismatch`
    is defined broadly (any collateral currency differing from the facility currency), so R13 fires
    on most multi-currency portfolios. WP1's second open item, still open.
27. `playbook/clauses/05_lender_discretion_valuation.yaml` - `positions.fallback` notice period `X`:
    the number rests on a single observation of 15 days, which is long for this product; R13 raises
    this clause's floor on D03.
28. `playbook/clauses/05_lender_discretion_valuation.yaml` - `positions.fallback` open-margin-call
    carve-out: an explicitly observed counterparty ask that sounds reasonable in the room, kept
    deliberately in `unacceptable` and in `escalation_triggers` as well. An arguable choice, made on
    purpose.
29. `playbook/clauses/08_events_of_default.yaml` - `positions.fallback` death standstill `X`: no
    source concedes any standstill on death at all; the published template keeps death as a
    free-standing ground for realisation without notice. WP3 group D's single weakest position, and
    R11 raises this clause's floor on D03.
30. `playbook/clauses/08_events_of_default.yaml` - `positions.acceptable`: narrowing "Relevant
    Person" by function where the observed drafting defines it by status. Cleaner, but only if the
    bank can apply it at intake.

### Real estate hard stop (D05)

31. `playbook/rules/rules.yaml` - `R09_real_estate`: `[VERIFY] SBL-RULE-GAP-09`; the sources
    establish only that land lending is out of scope, not anything substantive. Also `derived.has_real_estate`
    ignores the percentage, so a `real_estate` line at `pct: 0` still trips a hard stop (WP1 item 3).
32. `playbook/flags/regulatory_flags.yaml` - `mortgage_regulation`: raised and escalated on D05, and
    the only thing the tool says about a whole asset class it declares out of scope.

### Below-floor counterparty request (D06)

33. `playbook/clauses/06_margin_maintenance_cure.yaml` - `positions.fallback`: the tier D06's first
    request lands in. The cure extension generalises a fund borrower's capital-call standstill to "a
    written cure plan with an identified, committed funding source", which in private wealth is
    usually a property sale or a bonus. If the bank would refuse and then forbear informally, this
    moves to `unacceptable`, `default_floor` moves to `acceptable`, and R06's floor tightening goes
    inert.
34. `playbook/clauses/06_margin_maintenance_cure.yaml` - `positions.acceptable` Hard Floor `Z`: one
    Luxembourg retail document is the only source with a "no notice at all below this" level, and it
    has been promoted here to an architectural feature of the clause.
35. `src/sbl/engine.py` - the built-in below-floor escalation (`R16`) uses a fixed
    `"senior lawyer"` as the escalation target rather than reading the approver off the requested
    tier's `Position.approval`. Deliberate, so that the target does not vary between a stub and a
    drafted clause, but it is a contract decision.

---

## Band 2 - sets or moves a floor, but no golden deal reaches it

36. `playbook/rules/rules.yaml` - `R08_restricted_securities` and
    `playbook/flags/regulatory_flags.yaml` - `restricted_securities.description`: both are built on a
    US resale rule, in a playbook whose jurisdictions are England, Switzerland and Luxembourg, and
    the source is a grade-C reproduction rather than the official publisher. The rule raises two
    floors when it fires. WP8's second item, inherited unchanged by WP5b.
37. `playbook/rules/rules.yaml` - `R15_illiquid_collateral`: `[VERIFY] SBL-RULE-GAP-07`, nothing
    opened addresses gating, redemption suspension or the valuation of structured products as
    collateral; the rule raises two floors.
38. `playbook/rules/rules.yaml` - `R05b_third_party_corporate_pledgor` and
    `playbook/flags/regulatory_flags.yaml` - `financial_assistance_corporate_benefit`: the English
    half is grade A and read; the statement that equivalent restrictions exist elsewhere and must be
    checked locally is a practitioner's generalisation with no primary text behind it. WP8's highest
    priority for review.
39. `playbook/clauses/01_facility_type.yaml` - `default_floor: acceptable`: a deliberate deviation
    from the uniform `fallback` used elsewhere, and the only thing setting this clause's floor since
    no rule tightens it. A reviewer could simply reverse it.
40. `playbook/clauses/03_eligible_collateral_lending_values.yaml` - `positions.fallback`: fixing
    lending value percentages for named holdings for `X` months. The concession shape is observed in
    no source at all; it was built by analogy with the one notice-period concession in the pool.
41. `playbook/clauses/03_eligible_collateral_lending_values.yaml` - `positions.fallback`
    independent-valuer mechanic: the source supports appraisal rights only for private-company
    collateral in margin loans, and it has been extended here to any asset valued off an
    issuer-reported NAV.
42. `playbook/clauses/03_eligible_collateral_lending_values.yaml` - `positions.preferred` currency
    haircut of `X` percentage points: no opened source publishes an FX haircut figure, and R13
    assumes the mechanism exists.
43. `playbook/clauses/02_conditions_precedent.yaml` - `positions.fallback`: the Part 1 / Part 2
    split with an `X` business day longstop. No source opened concedes a post-closing longstop for
    conditions precedent at all; the whole shape is the drafter's.
44. `playbook/clauses/02_conditions_precedent.yaml` - `positions.acceptable`: the undertaking to
    confirm satisfaction within `X` business days, not observed anywhere, with an operational cost
    that credit and operations rather than legal should price.
45. `playbook/clauses/07_security_structure_control.yaml` - `positions.preferred` reserving a right
    of use: no opened source shows a private bank reserving rehypothecation over private-client
    collateral, and the one filed document on point has the lender conceding the opposite.
46. `playbook/clauses/09_enforcement_liquidation.yaml` - `positions.fallback.approval:
    credit committee`, where clauses 06 and 07 use `head of credit` and `senior lawyer`. Arguable
    either way; the argument is that this tier concedes a credit cost and a legal cost at once.
47. `playbook/jurisdictions/england_wales.yaml` - `creation`: the characterisation of a clause
    drafted as a general lien over intangible custody assets as a charge comes from a grade-C
    briefing reporting a 2012 decision. The briefing was read; the judgment was not.
48. `playbook/jurisdictions/england_wales.yaml` - `registration_filing`, "register protectively
    wherever there is any doubt": a commercial recommendation rather than law. The underlying legal
    statements around it are all grade A.
49. `playbook/jurisdictions/luxembourg.yaml` - `enforcement_route`: enforcement without prior notice
    as the default. The article was read and says it, but Art. 11(1) opens with "unless otherwise
    provided for", so the default is only as good as the drafting.
50. `playbook/jurisdictions/luxembourg.yaml` - `perfection_depends_on`: the statement that the
    non-primary perfection routes are treated as a waiver by the custodian of its own pledge ranking
    unless otherwise agreed.
51. `playbook/jurisdictions/switzerland.yaml` - `practical_notes` item 4: the asset-class
    translation of "objectively determinable value", which decides whether appropriation or sale is
    the realistic route for exactly the collateral R15 is about. Judgement dressed as a test.

---

## Band 3 - text, labelling and consistency

52. `playbook/clauses/06_margin_maintenance_cure.yaml` - unit convention: levels are expressed as
    lending value as a percentage of outstandings (the cover convention), while clauses 03, 04 and 05
    talk in lending-value percentages. Both appear in the sources; the library should pick one.
53. `playbook/clauses/01_facility_type.yaml` - `positions.fallback` closed list of lender
    termination and mandatory prepayment events: the shape is sourced but two limbs are the
    drafter's, and this is where a term facility silently loses or keeps protection. Read it line by
    line against clause 08.
54. `playbook/clauses/12_no_advice_non_reliance.yaml` - `positions.acceptable`: the express saving
    for duties that cannot be excluded, and the sentence that nothing in the clause is a statement
    that the bank has not provided a service it in fact provided. Both are lender-side restraint
    rather than protection, and both are unsourced as drafting.
55. `playbook/clauses/05_lender_discretion_valuation.yaml` - `regulatory_flags` including
    `consumer_credit`: a sensitivity link with no source behind it. Drop it if you think it
    overstates.
56. `playbook/clauses/08_events_of_default.yaml` - `regulatory_flags` including
    `fcar_safe_harbour_uncertain`: the same, on the same reasoning.
57. `playbook/clauses/10_capacity_authority.yaml` - `positions.preferred` partnership limb: the
    source supports the agency analysis and nothing more; joint and several liability is drafting
    practice, and limited partnerships and LLPs are expressly out of scope and `[VERIFY]`.
58. `playbook/clauses/02_conditions_precedent.yaml` - `depends_on` including
    `reps_source_of_funds_sanctions_tax`, which is a deferred stub, so the markup prints `[STUB]`
    next to it.
59. `playbook/clauses/11_governing_law_jurisdiction.yaml` - `risk_rating: high` and `document: all`:
    both are departures from the obvious reading of a clause the plan files under boilerplate.
60. `playbook/flags/regulatory_flags.yaml` - `emir_awareness` is referenced by nothing and can never
    appear in any output; `prudential_awareness` is referenced by three clauses but is never raised
    as a flag by any rule. Either give them a trigger or say in the file that they are reference
    entries.
61. `docs/glossary.md` - third-party security and surety defences: a generic secured-lending
    statement not confirmed against case law or any jurisdiction's suretyship doctrine, and the point
    WP2 said deserves the most scrutiny of anything it wrote.
62. `src/sbl/markup.py` - the one-line ladder summary ("first sentence, else first 160 characters")
    mangles abbreviations and cuts long opening sentences mid-clause. It read well on WP6's fixtures;
    it should be re-read against the real drafting.
63. ~~`docs/source_register.md` - "Label collisions": four `LAW-EW-*` labels each name two different
    documents across clause files 02, 06, 07, 09 and 10.~~ **Resolved in WP12**: group C's sequence
    was kept and the colliding labels in clauses 02 and 10 were renamed. See "Label collisions
    (resolved in WP12)" in that file. Nothing left to review here.

---

## Design questions raised by the build agents

These are not errors. Each is a decision the plan did not settle, which an agent resolved one way
and flagged.

**1. Jurisdiction-dependent openings, and a possible `jurisdiction_overrides` field.** Clause 07's
`fallback` and clause 09's `preferred` are genuinely jurisdiction-dependent: the two-party pledge
route is statutory in Luxembourg and probably unavailable in England, and no-notice enforcement is
simply not available on a Swiss booking to a private client, because the Swiss pre-realisation
notice cannot be waived by anyone who is not a custodian or a qualified investor. The frozen schema
has one ladder per clause plus a `jurisdiction_notes` string, so group C put the constraint in the
note and in the tier's `conditions` rather than forking the ladder. **This is the one place where a
reader of the markup could take the printed opening position and be wrong on a Swiss deal.** The
fix would be a `jurisdiction_overrides` field on a position; the agent did not add one because the
schema was frozen and another agent was editing the models. Decide whether the field is worth the
schema change, or whether the jurisdiction overlay printing immediately after the clause is enough.

**2. `set_opening` is currently a no-op.** The opening starts at `preferred` and actions only
tighten, so no rule can ever move it. D02's run log shows this literally: the entry against
`margin_maintenance_cure` reads `R06b_concentration_severe (no change)`. The plan's own R06b entry
acknowledges it ("set_opening margin_maintenance_cure = preferred (already)"). Three options:
delete the action, keep it for symmetry and the log as now, or make the opening start at the
clause's `default_floor` and tighten from there - which is a one-line change in `engine.evaluate`
but changes what every markup proposes first, so it is a contract decision rather than an engine
one.

**3. What "touched" should mean for the run's not-automated list.** The markup's "Not automated on
this deal" section is the union of the `not_automated` entries of every clause the run touched, and
"touched" currently means: a rule left an entry in `rules_applied`, **or** an escalation names the
clause, **or** one of its `regulatory_flags` was raised on this run. The third limb is the wide one:
a single flag pulls in every clause that lists it as a sensitivity, which on D02 produces a list of
more than twenty items. Too wide and the section becomes wallpaper that nobody reads; too narrow and
the warning that matters is not printed. The alternatives are to drop the flag limb, or to print the
flag-derived items in a separate, quieter sub-list.

**4. The `[VERIFY]` count, and whether it is a badge or a warning.** There are **101** `[VERIFY]`
occurrences in the library as it stands - 45 in the clause files, 39 in `rules.yaml`, 10 in the
flags file and 7 in the jurisdiction files - against **20** source entries carrying
`verified: false` and 243 carrying `verified: true`. Every one of them is deliberate and every one
prints in the output. The question is where the line sits between honest and unusable: a reader who
sees `[VERIFY]` three times in a clause may read it as scrupulous, and a reader who sees it thirty
times in one run may read it as a library that is not ready to be shown. Worth deciding whether
some of the 39 in `rules.yaml` should instead be resolved by opening two or three documents, and
whether the markup should summarise the count in the header rather than only inline.

**5. Approver names are free strings in three places.** `Position.approval`, `EscalateAction.to` and
`Flag.who_decides` are all unvalidated text, and the library already contains `credit`,
`head of credit`, `senior lawyer`, `credit committee`, `senior lawyer + compliance`, `compliance`
and two informational non-answers. WP1 raised it and had no authority to fix the list. An enum would
stop the vocabulary drifting, and the approver is the single most important field in the whole
model.
