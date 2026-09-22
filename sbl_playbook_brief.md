# Build Brief: Securities-Based Lending Negotiation Playbook

**Purpose:** A working demonstrator that turns a securities-based loan (SBL) negotiation into a structured, auditable, partly-automated process. Built to be walked through in an interview for a Private Wealth Management transactional lawyer role.

---

## 0. Ground rules (read first)

1. **Nothing in this file is legal advice or a verified market position.** The clause taxonomy below is a scaffold. Every substantive position — what is "market", what is a reasonable fallback — must be researched and written by Stuart. If it goes in the tool, he has to be able to defend it out loud.
2. **Synthetic data only.** No real counterparties, no real client facts, no Goldman branding, nothing that implies affiliation or access to GS materials.
3. **Frame it as a demonstrator, not production software.** Overclaiming here is worse than building nothing.
4. **The reasoning is the deliverable, not the code.** An interviewer will not read the source. They will ask why the clause library is structured the way it is. That answer is the thing being tested.

---

## 1. Why this product

The posting's first-named responsibility is drafting documentation for lending products, and it lists securities-based loans first. It separately asks for "AI tools to streamline transaction execution through automation and playbook development."

SBL is also the right scope for a short build: it is a relatively contained document set (facility letter + pledge/security agreement + account control arrangements), it has a well-defined risk spine (collateral value, margin, enforcement), and it forces engagement with exactly the issues the role is about — enforceability, perfection, and cross-border variation.

**Define the product correctly and out loud:** a securities-based loan is credit extended to a client secured against their investment portfolio. It is *not* securities lending (lending out stock itself, typically to short sellers). Do not conflate these.

---

## 2. Architecture

Five modules. Build in this order.

```
[1] Clause Library  -->  [3] Rules Engine  -->  [4] Markup Generator
        ^                      ^                       |
        |                      |                       v
   (source refs)         [2] Deal Intake        [5] Audit + Escalation Log
```

### Module 1 — Clause Library (the substantive core)

A structured file (YAML or JSON) — one entry per negotiable clause.

```yaml
- id: margin_call_cure
  title: Margin Call Cure Period
  category: collateral_maintenance
  risk_rating: high
  positions:
    preferred:    { text: "...", rationale: "..." }
    acceptable:   { text: "...", rationale: "...", conditions: [...] }
    fallback:     { text: "...", rationale: "...", conditions: [...] }
    unacceptable: { text: "...", rationale: "..." }
  escalation_trigger: "Any cure period exceeding X business days"
  jurisdiction_notes: { england: "...", switzerland: "..." }
  regulatory_flags: [ ... ]
  sources: [ ... ]
```

The four-tier structure (preferred / acceptable / fallback / unacceptable) is what makes this an actual playbook rather than a template. It encodes where the walk-away line sits, which is the part a junior lawyer cannot infer and the part that saves senior time.

### Module 2 — Deal Intake

Capture the parameters that drive everything downstream:

- Borrower type: individual / corporate / trust / partnership / fund
- Borrower domicile; is the borrower a **consumer**?
- Collateral jurisdiction(s) and custodian location
- Collateral composition: diversified portfolio / concentrated single stock / restricted or control securities / fund interests / cash
- Facility type: uncommitted and repayable on demand vs committed term
- Purpose: non-purpose vs purpose (i.e. to buy more securities)
- Size, currency, benchmark rate
- Is the borrower an insider/PDMR of any pledged issuer?

### Module 3 — Rules Engine

Deterministic. Maps intake parameters to required positions and raised flags. Keep the logic explicit and readable — the point is auditability, not cleverness.

Example rules:

- `borrower_type == trust` -> require trustee capacity and power-to-borrow diligence; pull authority representations; add CP for trust deed review
- `borrower is consumer` -> flag consumer credit regime; escalate
- `collateral includes issuer shares AND borrower is PDMR` -> flag market abuse / disclosure / closed period considerations; escalate
- `concentration > threshold in single name` -> tighten advance rate and margin triggers
- `real estate in collateral package` -> flag mortgage regulation; escalate

### Module 4 — Markup Generator

Given a deal profile, output a first-draft negotiation position: clause-by-clause, with the selected tier, the rationale, the fallback ladder, and any triggered flags.

Output as Markdown first. A redline against an uploaded counterparty draft is Phase 5, not Phase 1.

### Module 5 — Audit + Escalation Log

Every generated position traceable to a clause-library entry and a rule. Every escalation flag logged with its trigger. This is the module that makes the tool credible to a regulated institution — it is the difference between an automation tool and a black box.

---

## 3. Clause taxonomy (starting set)

Build the first twelve. The rest are later.

**Credit and facility mechanics**

1. Facility type — uncommitted/demand vs committed term
2. Interest rate, benchmark (SARON / SONIA / EURIBOR) and fallback provisions
3. Prepayment, breakage costs
4. Conditions precedent — KYC, authority documents, security perfection

**Collateral**

5. Eligible collateral and advance rates / lending values by asset class
6. Concentration limits
7. Collateral substitution rights
8. Margin maintenance, margin call mechanics, cure periods, notice
9. Security interest: pledge vs charge; control/possession; custody arrangements
10. Cross-collateralisation and set-off

**Default and enforcement**

11. Events of default — incl. insolvency, MAC, death/incapacity of an individual borrower
12. Enforcement and liquidation rights — notice vs no-notice sale, standard of conduct

**Parties and representations**

13. Capacity and authority (critical for trusts, corporates, partnerships)
14. Source of funds, sanctions, tax representations
15. Purpose restrictions

**Boilerplate that is not boilerplate here**

16. Governing law, jurisdiction, service of process
17. Transfer / assignment
18. Confidentiality and bank secrecy (a live Swiss consideration)
19. Tax gross-up / withholding

---

## 4. Jurisdictional overlay

Even stubbed, this shows you understand the actual job — the posting asks for advice on "collateral enforceability and security registration across EMEA jurisdictions."

Start with three: **England & Wales, Switzerland, Luxembourg.** For each, capture:

- How a security interest over financial collateral is created
- What (if anything) must be registered or filed, and by when
- What perfection depends on — possession, control, notice, registration
- Enforcement route: self-help sale vs court process
- Whether a financial-collateral regime disapplies general formalities

Research these properly rather than asserting them. Getting a perfection rule wrong in an interview is worse than saying "this is stubbed pending research."

---

## 5. Regulatory flag set

Map each to a trigger condition, not a general description:

- **Consumer credit regimes** — triggered by individual borrower below thresholds
- **Mortgage regulation** — triggered by residential real estate in the collateral package
- **MiFID II** — triggered where the lending conversation shades into investment advice, or where leverage affects suitability / appropriateness
- **Market abuse** — triggered where a pledgor is an insider or PDMR of a pledged issuer; disclosure and closed-period implications
- **CRD / prudential** — capital treatment of the exposure; note as awareness, do not overclaim
- **EMIR** — only if derivatives are wrapped into the structure

---

## 6. Build phases

| Phase | Scope | Rough effort |
|---|---|---|
| 1 | Clause library, 12 entries, 4 tiers each, in YAML | half day |
| 2 | Deal intake — CLI or simple form | 1–2 hours |
| 3 | Rules engine + Markdown markup output | half day |
| 4 | Jurisdiction overlay + regulatory flags | half day |
| 5 | *Optional:* LLM layer to ingest a counterparty draft and map clauses to the library | open |

**Phase 1 is the low-hanging fruit and also the highest-value part.** A well-reasoned clause library with defensible fallback ladders is more impressive than a slick UI over a thin one. If time runs out, stop after Phase 3.

The LLM layer in Phase 5 is deliberately last. The interesting claim is not "I called an API" — it is "I structured legal judgment so that it could be automated safely, with escalation points where a human must decide."

---

## 7. Research sources

- **SEC EDGAR** — full text of real securities pledge agreements filed as exhibits. The single best free source of actual drafting.
- UK Financial Collateral Arrangements regime — primary text
- Swiss pledge provisions — Code of Obligations / Federal Intermediated Securities Act
- Published bank SBL terms and disclosures from private banks
- Law firm client briefings on financial collateral and margin lending

Avoid syndicated-loan resources (LMA / LSTA) — different product, different risk profile.

---

## 8. The interview walkthrough

Three minutes, in this order:

1. **The problem.** SBL negotiation repeats the same twenty decisions across every deal, and the fallback ladder lives in senior lawyers' heads.
2. **The structure.** Four-tier positions, deterministic rules, explicit escalation.
3. **The judgment call.** Where you deliberately did *not* automate, and why. This is the most important thirty seconds — it demonstrates that you understand what automation in a regulated legal function can and cannot own.
4. **The honest caveat.** Built from public sources as a demonstrator; the substantive positions would need validation against the institution's own risk appetite.

Point 4 is not a weakness. Volunteering the limits of your own tool is exactly the disposition a bank wants in someone building automation for its legal function.
