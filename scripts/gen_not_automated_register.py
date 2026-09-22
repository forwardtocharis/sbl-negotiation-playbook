# -*- coding: utf-8 -*-
"""Generate docs/not_automated_register.md from the clause YAML files.

Run: .venv/Scripts/python scripts/gen_not_automated_register.py
Every `not_automated` string in playbook/clauses/*.yaml is carried verbatim.
Annotations are keyed by (clause id, leading text of the item); a missing or
non-matching key is a hard error, so a clause edit cannot silently drop an item.
"""
import yaml, glob, os, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "not_automated_register.md")

RQ = '\u201c'
LQ = '\u201d'

# clause id -> list of (item prefix, what the tool does instead, why a human owns it)
A = {
"facility_type": [
 ("Whether to exercise the demand right",
  "Nothing. The clause prints the ladder and the escalation trigger for a conversion request; no rule reads a live exposure.",
  "Calling a demand line is a relationship and credit decision taken on the day, against client conduct and market facts that no intake field records."),
 ("Whether to offer committed term at all",
  "Rule `R11_committed_term` fires only once the deal is already committed: it raises the `events_of_default` floor to `acceptable` and adds a note. The tool never recommends the product.",
  "Pricing a commitment trades lending value, fee and capital against a client relationship, and that trade belongs to credit and the business."),
 ("Whether repeated forbearance has made an uncommitted line",
  "Nothing.",
  "Course of dealing is a pattern across time and across documents, and the engine sees one deal at one moment."),
 ("Setting the notice period and the term length",
  "Prints `X` inside the fallback text and lists any longer request as an escalation trigger.",
  "One opened source states either figure, so both numbers are the institution's risk appetite and only credit can set them."),
],
"conditions_precedent": [
 ("Whether a condition has in fact been satisfied",
  "Lists the conditions, and rules `R01`, `R02`, `R05b`, `R07`, `R08` and `R12` append more. It never marks one satisfied.",
  "Satisfaction is a documentary judgement that a named person signs off, and that signature is the control."),
 ("Whether to waive a condition and advance anyway",
  "Nothing. No action in the rule grammar can remove a condition precedent.",
  "A waiver trades perfection or capacity risk for speed, and only the approver named in the clause can price that trade."),
 ("Know-your-client, sanctions and source-of-funds outcomes",
  "Prints them as conditions precedent and repeats them in the run's not-automated section.",
  "These are financial-crime determinations reserved to compliance by regulation, not drafting positions."),
 ("Whether the Borrower is a consumer",
  "`R03a` raises the `consumer_credit` flag at high severity and escalates where no declaration is recorded; `R03b` raises it at medium where one is.",
  "Build plan section 7 reserves the final consumer determination to a human, and the exemption thresholds behind the flag are themselves `[VERIFY]`."),
 ("Whether a legal opinion is required",
  "Prints the jurisdiction overlay for the deal's governing law; `R12` adds an executed account control agreement as a condition precedent.",
  "Scoping an opinion is a cross-border enforceability conclusion, and the tool cites while local counsel confirms."),
 ("Which items belong in Part 1 and which in Part 2",
  "Prints the test in the fallback rationale.",
  "Applying " + RQ + "can this still be fixed the day after the money moves?" + LQ + " is a judgement on the facts of the particular file."),
],
"eligible_collateral_lending_values": [
 ("Whether a specific holding is admitted",
  "Nothing on the individual line. `R06`, `R08`, `R13` and `R15` add notes, and `R06b` and `R15` raise the floor to `acceptable`.",
  "Eligibility and the advance rate on a named security are credit decisions, and no public source opened for this playbook publishes a grid to copy."),
 ("Setting the numeric grid itself",
  "Prints `X` placeholders in the clause text and repeats the item in the run output.",
  "Inventing a number with no source behind it is exactly what build plan section 0 rule 4 forbids."),
 ("Whether an asset that becomes illiquid or restricted after drawdown",
  "`R08` and `R15` raise floors and add notes, but only on the facts recorded at intake.",
  "Re-rating is a decision taken on a live position against a market the engine never sees."),
 ("Whether to take a concentrated but high-quality single holding",
  "`R06` and `R06b` tighten the floor and `R06b` escalates to credit.",
  "The choice between excluding the holding and discounting it is the very question the escalation exists to put in front of credit."),
],
"concentration_limits": [
 ("Setting the single-name and sector limits",
  "Uses 25 and 50 per cent as the `R06` and `R06b` triggers and prints `X` in the clause text.",
  "No opened source supports either figure, so they are credit-policy numbers wearing a rule's clothes."),
 ("Whether two issuers are correlated",
  "Nothing. The intake records a largest single-issuer percentage per asset class and no correlation fact.",
  "Collapsing two names into one exposure is a risk-modelling judgement with nothing in the intake to support it."),
 ("Whether to grandfather an existing concentrated holding",
  "`R06` raises the floor to `acceptable` and adds a lending-value haircut note.",
  "Grandfathering suspends a limit for a named client, which is a credit concession rather than a drafting tier."),
 ("Whether a concentrated position that is also restricted or PDMR-connected",
  "`R06`, `R06b`, `R07` and `R08` all fire; two of them escalate.",
  "Whether to take the position at all, rather than discount it, is the credit-and-compliance decision the escalations exist to force."),
],
"lender_discretion_valuation": [
 ("Whether a particular market move is a",
  "Prints the carve-out and the escalation trigger attached to it.",
  "The clause fixes who decides; whether today's move qualifies is a judgement on live market data the engine does not hold."),
 ("Whether to exercise the discretion at all on a live position",
  "Nothing.",
  "Forbearance is a relationship decision taken outside the document and after it is signed."),
 ("Setting the notice period itself",
  "Prints `X`; `R13` raises this clause's floor to `acceptable` where there is a currency mismatch.",
  "The only observation behind the number is a single sub-part of a single filing, so the operative figure is risk appetite."),
 ("Whether to disclose the full haircut matrix",
  "Nothing.",
  "Disclosing the Bank's own risk methodology in a negotiation is a confidentiality and strategy call, not a clause position."),
],
"margin_maintenance_cure": [
 ("Whether to grant forbearance on a live margin call",
  "Nothing. Build plan section 7 lists it, and the run output repeats it whenever this clause is touched.",
  "Forbearance is decided against a live shortfall on facts that no intake field records."),
 ("Whether a written cure plan is credible",
  "Prints the fallback tier's conditions.",
  "Judging whether a funding source will actually arrive is a credit assessment, not a document check."),
 ("Setting the Trigger Level, the Restoration Level, the Hard Floor",
  "Prints the `X`, `Y` and `Z` placeholders; `R06` raises the floor to `acceptable` on a concentrated portfolio.",
  "The opened sources give a band and one two-level retail structure, which is not an answer for this institution."),
 ("Whether a particular market move is a",
  "Prints the carve-out.",
  "The same live-market judgement as the valuation clause, and here it decides whether the borrower gets any time at all."),
 ("Whether to call at all on a relationship where the shortfall is small",
  "Nothing.",
  "Deciding not to call is a relationship decision, and repeating it is the course-of-dealing risk the facility-type clause warns about."),
],
"security_structure_control": [
 ("Whether a particular custodian's standard control agreement actually delivers control",
  "`R12` adds an executed account control agreement as a condition precedent, raises the floor to `acceptable` and prints the jurisdiction overlay for the account's law.",
  "Perfection under the law of the account's location is a local counsel conclusion; the tool prints the question and cites, and counsel answers it."),
 ("Whether to accept a client's existing custody relationship at all",
  "`R12` tightens the floor and adds a per-jurisdiction note on control.",
  "Taking on a third-party custodian is an operations and relationship decision as much as a credit one."),
 ("The classification of the client that determines whether title transfer",
  "`R04` raises `fcar_safe_harbour_uncertain` where a natural person provides collateral under English law.",
  "Classification turns on regulatory status facts the intake does not capture, and the safe-harbour point behind the flag is itself `[VERIFY]`."),
 ("Whether to register a charge protectively",
  "Prints the England and Wales jurisdiction note on registration and on the disapplication.",
  "Paying for belt-and-braces registration where reliance on the financial collateral regime is doubtful is an institutional policy choice."),
 ("Setting the substitution threshold and the acknowledgement deadline",
  "Prints the `Y` placeholder.",
  "No opened source publishes either number, so both are risk appetite stated as drafting."),
],
"events_of_default": [
 ("Whether a material adverse change or a substantial deterioration has actually occurred",
  "`R11` raises this clause's floor to `acceptable` on a committed facility and adds a material adverse change note.",
  "The clause fixes who decides and on what standard; the determination itself is made on live facts after signing."),
 ("Whether to call a default at all",
  "Nothing. Build plan section 7 reserves waiver of an event of default.",
  "Calling or waiving a default is a relationship, credit and conduct decision taken together, and it is hard to reverse."),
 ("Whether an individual has lost legal capacity",
  "Nothing. The item carries `[VERIFY]` and prints with it.",
  "No mental-capacity source was opened for this playbook, and the intake records no fact that would answer the question."),
 ("Whether to enforce against a deceased individual's collateral",
  "Nothing.",
  "It is a reputational and conduct decision as much as a legal one, and it is taken while an estate is being administered."),
 ("Setting the payment grace, covenant cure and death standstill periods",
  "Prints `X`.",
  "Only the institutional grace periods are observed in a source; the death standstill is unobserved and is a proposal, not a market position."),
],
"enforcement_liquidation": [
 ("The decision to enforce at all",
  "`R07`, `R08` and `R15` raise the floor to `acceptable` and the ladder prints; build plan section 7 reserves the decision itself.",
  "It is the most consequential judgement in the product and the tool never makes it."),
 ("Whether a particular market move is a",
  "Prints the carve-out.",
  "A live-market judgement, and here it decides whether the borrower is told before the sale."),
 ("Whether a proposed sale method is commercially reasonable",
  "Prints the standard and the pre-agreed acknowledgements of what is commercially reasonable.",
  "What is reasonable on the day depends on book depth and market conditions the engine never sees."),
 ("Whether a closed period, an issuer or underwriter consent or a volume limit",
  "`R07` raises `market_abuse` at high severity and escalates to senior lawyer and compliance; `R08` raises `restricted_securities` and adds an issuer-consent condition precedent.",
  "Build plan section 7 reserves clearing a PDMR or insider position with compliance, and the timing of a sale is where that bites."),
 ("Whether notice is required by law and unwaivable",
  "Prints the jurisdiction overlay, including the Swiss point that pre-realisation notice cannot be waived by a party who is neither a custodian nor a qualified investor.",
  "It is a cross-border enforceability conclusion, and the printed overlay is a citation rather than a confirmation."),
 ("Setting the notice period",
  "Prints `X`.",
  "Three observations across one composite filing is not a market norm, so the number is risk appetite."),
],
"capacity_authority": [
 ("Reading the trust instrument",
  "`R01` adds a trust deed review as a condition precedent, requires a trustee capacity and power representation, and raises the floor to `acceptable`.",
  "No rule can tell anyone whether a power to borrow or charge exists; a lawyer reads the deed and everything behind it."),
 ("Whether a limited recourse request is safe on the facts",
  "Prints the fallback tier's conditions and its named approver.",
  "It turns on the state of the trustee's indemnity, the standing of the trustee and the assets actually in the fund, none of which is an intake field."),
 ("Whether a corporate pledgor has corporate benefit",
  "`R05b` raises `financial_assistance_corporate_benefit` and adds a condition precedent; the non-English half of that flag is `[VERIFY]`.",
  "It is a local counsel question on every deal where the pledgor is not the borrower, and the library has no primary text outside England."),
 ("Whether independent legal advice was genuinely given",
  "`R05` requires a representation that the pledgor took independent advice.",
  "The representation records that advice was taken; whether it was real, independent and understood is a judgement about a conversation."),
 ("Whether an individual had capacity at signing",
  "Nothing.",
  "Incapacity short of death is an identified gap in this library and the intake records no fact that answers it."),
 ("Whether to accept a foreign-law legal opinion in the form offered",
  "Prints the jurisdiction overlay for the deal's governing law.",
  "Scoping and accepting an opinion is a legal judgement reserved to the deal lawyer with local counsel."),
],
"governing_law_jurisdiction": [
 ("Every cross-border perfection and enforceability conclusion",
  "Prints the jurisdiction file for the deal's governing law, with its sources, `verified` values and `[VERIFY]` markers.",
  "Build plan section 7 puts it plainly: the tool cites and local counsel confirms, and that confirmation is a condition precedent, not a drafting note."),
 ("Whether an asymmetric jurisdiction clause will be given effect",
  "Prints the tier with its `[VERIFY]` marker.",
  "Whether a forum honours a one-sided clause is unsourced for this playbook and turns on that forum's own law."),
 ("Choosing the booking centre for a new relationship",
  "`R14` switches the jurisdiction overlay and raises `bank_secrecy_data` on a Swiss booking.",
  "It is a commercial, tax and regulatory decision as well as a legal one, and it is taken before any clause is drafted."),
 ("Whether to commence proceedings in a second jurisdiction",
  "`R14` adds a note on `confidentiality_bank_secrecy`.",
  "Suing abroad discloses client information in a bank-secrecy jurisdiction, which legal and compliance in the booking centre own."),
 ("Whether the Borrower or the Pledgor is capable of claiming immunity",
  "Nothing.",
  "It turns on the counterparty's own constitution and on the law of the place of enforcement, neither of which is an intake fact."),
],
"no_advice_non_reliance": [
 ("Every suitability and appropriateness conclusion",
  "`R10` raises `mifid_suitability` and tightens this clause's floor to `acceptable`.",
  "Build plan section 7 reserves suitability conclusions, and the flag names compliance as the decider."),
 ("Whether the relationship is in fact execution-only",
  "Nothing. The intake has no relationship-type field.",
  "It is a fact about what people actually did, not a drafting choice, and the clause is only defensible if it matches that fact."),
 ("Whether a particular conversation between the relationship manager",
  "Nothing.",
  "Whether something was a personal recommendation is a conduct determination on evidence the tool never sees."),
 ("The final determination that a borrower is or is not a consumer",
  "`R03a` and `R03b` raise `consumer_credit` at high or medium severity, and `R03a` escalates where no declaration is recorded.",
  "Build plan section 7 reserves the final determination, and the thresholds behind the flag are `[VERIFY]`."),
 ("Whether to decline the facility outright",
  "Raises flags and escalations, and never declines.",
  "Turning business away is the institution's decision and no document can make it."),
],
}

SYSTEM = [
("The final determination that a borrower is or is not a consumer under any regime.",
 "`R03a` raises the `consumer_credit` flag at high severity and escalates; `R03b` raises it at medium where a high-net-worth or business declaration is recorded. The flag names senior lawyer and compliance as the deciders.",
 "The exemption logic turns on declarations, thresholds and the lender's own state of mind about the borrower's purpose, and the threshold figures in the flag are `[VERIFY]`."),
("Any concession below a clause's floor, and any request at `unacceptable`.",
 "The built-in counterparty-request check (`R16`, implemented in the engine rather than in `rules.yaml`) records the outcome as `accepted_within_floor`, `below_floor_escalated` or `unacceptable_escalated`, escalates the last two, and sets the run's exit code to 2.",
 "The floor is the point at which the library stops deciding; going below it is a named person accepting a loss of protection, which is the whole purpose of the approver field."),
("Clearing a PDMR or insider position with compliance.",
 "`R07_pdmr_pledged_issuer` raises `market_abuse` at high severity, escalates to senior lawyer and compliance, tightens `enforcement_liquidation` to `acceptable`, and adds an insider-status representation and a compliance sign-off condition precedent.",
 "Whether a pledge or an enforcement sale can proceed depends on closed periods, disclosure obligations and issuer consents that only compliance can check against live facts."),
("Suitability or appropriateness conclusions.",
 "`R10_purpose_acquire_securities` raises `mifid_suitability` and tightens `no_advice_non_reliance` to `acceptable`; the flag names compliance as the decider.",
 "Suitability is a conclusion about a client's circumstances and understanding, which is not a fact the intake carries and not a position a clause can take."),
("Any cross-border perfection or enforceability conclusion.",
 "Prints the jurisdiction file for the deal's governing law with its sources, `verified` values and `[VERIFY]` markers, and `R12` makes an executed account control agreement a condition precedent where the lender is not the custodian.",
 "The library cites public law; local counsel in the account's jurisdiction confirms it, and that confirmation is a condition precedent rather than a drafting note."),
("Sanctions, know-your-client and source-of-funds outcomes.",
 "Prints them as conditions precedent under `conditions_precedent`, and repeats them in the run's not-automated section.",
 "These are financial-crime determinations reserved to compliance by regulation, and a negative outcome ends the deal rather than moving a tier."),
("Forbearance on a live margin call, waiver of an event of default, and the decision to enforce.",
 "Nothing. The relevant clauses print their ladders, and rules `R06`, `R07`, `R08`, `R11` and `R15` tighten floors at intake only.",
 "All three are decisions taken after signature, against a live position, on facts the engine has never seen."),
("Promotion of any entry from `draft` to `reviewed`.",
 "Prints the status tag (`[REVIEWED]`, `[DRAFT]`, `[STUB]`) beside every clause, counts them in the run header, and prints a standing warning that unreviewed positions are not the lender's settled position. Agents may write `stub` or `draft` only.",
 "`reviewed` is a named human's signature on a position, with `reviewed_by` and `last_reviewed` filled, and it is the only thing that would make the library usable."),
]

INTRO = """# Not-automated register

This is the list of decisions this demonstrator deliberately does **not** make.

It is a demonstrator built from public sources. It has not been validated against any institution's
credit policy or risk appetite, it carries no regulatory approval, and nothing in it is legal
advice. The register exists for the same reason the status tags and the audit log exist: so that a
reader can tell, without reading the code, exactly where the tool stops and a person starts.

Two kinds of item are collected below.

* **Clause items** are the `not_automated` entries in `playbook/clauses/*.yaml`, carried here
  verbatim and grouped by clause. Section 1 is generated from the YAML, so it cannot drift from the
  library.
* **System-level items** are the eight in `build_plan.md` section 7. They apply on every deal
  regardless of which clauses are in play.

For each item the register records **what the tool does instead** - raise a flag, escalate, tighten
a floor, print a status or a placeholder, or nothing at all - and **why a human must own it**.
"Nothing at all" is a deliberate answer rather than a gap: several of these decisions are taken
after the document is signed, against a live position, on facts that never appear in an intake file.

At run time the markup prints a per-deal subset of the clause items under the heading
**"Not automated on this deal"**: the deduplicated union of the `not_automated` entries of every
clause the run touched, where a clause counts as touched when a rule left an entry in its
`rules_applied`, an escalation names it, or one of its `regulatory_flags` was raised on that run.
This register is the complete list; the run output is the slice that matters for that deal.
"""


def annotate(cid, item):
    best = None
    for prefix, does, why in A.get(cid, []):
        if item.startswith(prefix):
            if best is None or len(prefix) > len(best[0]):
                best = (prefix, does, why)
    if best is None:
        raise SystemExit("ANNOTATION MISSING for clause %r: %r" % (cid, item[:90]))
    return best[1], best[2]


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "playbook", "clauses", "*.yaml")))
    out = io.StringIO()
    out.write(INTRO)
    out.write("\n---\n\n## 1. Clause items\n\n")
    n = 0
    stubs = []
    drafted = 0
    for f in files:
        d = yaml.safe_load(open(f, encoding="utf-8"))
        items = d.get("not_automated") or []
        if not items:
            stubs.append((d["id"], d.get("title") or d["id"]))
            continue
        drafted += 1
        out.write("### %s\n\n" % d["title"])
        out.write("`%s` | `playbook/clauses/%s` | risk rating %s | default floor `%s` | status `%s`\n\n"
                  % (d["id"], os.path.basename(f), d.get("risk_rating"),
                     d.get("default_floor"), d.get("status")))
        for item in items:
            item = item.strip()
            does, why = annotate(d["id"], item)
            n += 1
            out.write("**%s**\n\n" % item)
            out.write("- *Tool does instead:* %s\n" % does)
            out.write("- *Why a human owns it:* %s\n\n" % why)
        out.write("\n")
    out.write("### Deferred stub clauses\n\n")
    out.write("These twelve clauses exist so that rules can reference them and so that the markup "
              "shows the shape of the full library. They are `status: stub`, carry no positions and "
              "therefore have no `not_automated` entries yet. The tool prints them with a `[STUB]` "
              "tag and nothing else, so every decision under them is, for now, entirely a human's.\n\n")
    for cid, title in stubs:
        out.write("- `%s` - %s\n" % (cid, title))
    out.write("\n---\n\n## 2. System-level items\n\n")
    out.write("From `build_plan.md` section 7. These apply on every deal, whichever clauses are in "
              "play. Several are also carried by a clause above; they are repeated here because "
              "they hold even on a deal where that clause is never touched.\n\n")
    for i, (item, does, why) in enumerate(SYSTEM, 1):
        out.write("**%d. %s**\n\n" % (i, item))
        out.write("- *Tool does instead:* %s\n" % does)
        out.write("- *Why a human owns it:* %s\n\n" % why)
    out.write("---\n\n## 3. Counts\n\n")
    out.write("- Clause items carried: **%d**, across **%d** drafted clauses.\n" % (n, drafted))
    out.write("- Deferred stub clauses with no items yet: **%d**.\n" % len(stubs))
    out.write("- System-level items: **%d**.\n\n" % len(SYSTEM))
    out.write("Section 1 is generated from `playbook/clauses/*.yaml` by "
              "`scripts/gen_not_automated_register.py`. If a clause gains or loses a "
              "`not_automated` entry, rerun that script rather than editing this file by hand: it "
              "carries every entry verbatim and fails loudly on any entry it has no annotation "
              "for, so an item cannot be dropped silently.\n")
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out.getvalue())
    print("wrote %s: %d clause items across %d clauses + %d system items, %d stubs"
          % (OUT, n, drafted, len(SYSTEM), len(stubs)))


main()
