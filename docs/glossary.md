# Glossary

Synthetic demonstrator. Drafted from the lender's (private bank's) side. Terms below define usage within this playbook; they are not legal advice. `[VERIFY]` marks a statement not confirmed against a primary source the drafting agent actually opened.

## Tier semantics

| Tier | Meaning | Who may agree it |
|---|---|---|
| preferred | Lender's opening position | Deal lawyer, by default |
| acceptable | Routine concession; no loss of core protection | Deal lawyer, no escalation |
| fallback | Concession that costs real protection; only with the listed conditions satisfied | Named approver in the entry; concession logged |
| unacceptable | Walk-away line | Nobody. Any request here is a hard escalation |

The **floor** for a clause on a deal is the lowest tier the deal lawyer may concede to without escalation. Rules can only move the floor up (tighten). The **opening** is the tier the markup proposes first; rules can only move it up.

---

## Facility type

**Synonyms:** uncommitted demand facility / committed term facility / evergreen line.

An SBL facility is structured either as **uncommitted and repayable on demand** (the lender can call the loan and stop further advances at any time, at its discretion, with no default required) or as a **committed term facility** (the lender is obliged to make agreed advances for a fixed period, subject to conditions precedent, and can only accelerate on an event of default). Most private-bank Lombard facilities are uncommitted demand facilities; committed term is the exception, typically for larger or purpose-specific loans. This distinction is set out in the facility letter and drives almost everything downstream, including how enforcement is framed, because a demand facility gives the lender a contractual "on-demand" route that does not require proving default `[VERIFY: exact drafting mechanics vary by bank and were not confirmed against a specific filed facility letter]`.

## Conditions precedent

**Synonyms:** CPs, drawdown conditions.

Conditions precedent are the list of items (KYC/AML clearance, constitutional and authority documents, executed security documents, perfection steps, valuations) that must be satisfied before the lender is obliged to advance any money. They appear in the facility letter, cross-referring to the security agreement and account control agreement for perfection-related items. CPs are the principal gate through which capacity, insider status and jurisdictional issues get cleared before money moves, which is why several rules in this playbook append CP items rather than blocking the deal outright.

## Eligible collateral and lending values

**Synonyms:** advance rate, LTV / loan-to-value, collateral value, haircut, lending value percentage.

**Lending value** (also called advance rate, LTV or collateral value after haircut) is the percentage of an asset's market value that the lender will advance against, set by asset class and often tightened for single-name concentration, restricted status, or currency mismatch; the discount from 100% is the **haircut**. Eligible collateral is the defined universe of asset classes the lender will accept at all (e.g. listed equity, listed bonds, daily-dealt funds, cash), set out in the facility letter or a schedule to the security agreement, with the security agreement itself covering how each eligible asset is captured by the security interest. Swiss/continental Lombard practice and UK SBL practice use these terms interchangeably; this playbook standardises on "lending value" in clause text.

## Concentration limits

**Synonyms:** single-name limit, single-issuer cap.

A concentration limit caps how much of the lending value attributable to a single issuer, asset class, or correlated group of assets can count toward the facility, to stop the collateral pool being effectively a bet on one name. It is set out in the facility letter (as a formula or percentage) and enforced operationally through the margin maintenance mechanics in the security agreement. Breach of a concentration limit typically triggers a tightened margin call trigger or a forced top-up/substitution rather than an immediate default.

## Lender discretion over valuation and eligibility

**Synonyms:** lender discretion, unilateral variation right.

This is the clause giving the lender the contractual right to change lending values, add or remove eligible asset classes, or revalue collateral, unilaterally and (subject to any agreed notice period) without the borrower's consent. It sits in the facility letter. Brief review flags this as arguably the most contested clause in practice: borrowers push for advance notice and objective triggers (e.g. only on a market event), while lenders resist because the ability to reprice risk in real time is the core protection behind an uncommitted facility `[VERIFY: specific notice-period market practice not confirmed against a primary filed document]`.

## Margin maintenance, margin call mechanics and cure period

**Synonyms:** margin call (shortfall, top-up, collateral call); cure period (grace period, remedy period).

A **margin call** (or shortfall/top-up/collateral call) arises when the lending value of the collateral pool falls below the amount drawn, and requires the borrower to post additional eligible collateral or repay part of the loan. The **cure period** (grace period, remedy period) is the window the borrower has to satisfy a margin call before the lender may treat it as unremedied and move to enforcement. Mechanics (how the call is calculated, how it is notified, and the length of the cure period) sit in the security agreement, cross-referenced from the facility letter. This is one of the risk-spine clauses: a longer cure period is the single most common borrower ask and the one most likely to be tightened by concentration or PDMR-related rules in this playbook.

## Security structure and control

**Synonyms:** pledge / charge / title transfer; security interest vs title-transfer collateral arrangement; possession; control.

The lender can take collateral either as a **security interest** (a pledge or charge, where legal title stays with the borrower/pledgor and the lender has a proprietary right that must be perfected — typically by possession, control, or registration) or by **title transfer** (full legal and beneficial ownership passes to the lender, subject to a contractual obligation to transfer back equivalent assets on repayment). Title transfer changes the insolvency analysis substantially compared with a security interest, because the collateral is the lender's own asset rather than an asset of an insolvent borrower's estate. **Control** is the mechanism (an account control agreement with the custodian) by which a pledgee lender who is not itself the custodian can direct dealings in the pledged account without the pledgor's further cooperation; it is what "perfects" a pledge over intermediated securities in most of the target jurisdictions. This clause lives in the security agreement, with control mechanics also appearing in the account control agreement where the custodian is a third party.

## Events of default

Events of default are the defined triggers (non-payment, breach of undertaking, insolvency, material adverse change, and — distinctively for individual borrowers — death or incapacity) that entitle the lender to accelerate the facility and move to enforcement. They sit in the facility letter, cross-referenced by the security agreement's enforcement trigger. On an uncommitted demand facility, events of default matter less for the decision to stop lending (which needs no default) and more for whether enforcement against collateral is available without further notice.

## Enforcement and liquidation

**Synonyms:** self-help sale, appropriation, realisation.

Enforcement is the process by which the lender realises the collateral to satisfy the secured debt after an event of default (or, on a demand facility, after a call is not met). Mechanics differ by legal structure: a security interest is typically enforced by sale (with or without prior notice, depending on the governing law and the agreement) or, in jurisdictions that permit it, by **appropriation** (the lender takes ownership of the collateral itself at a fair value, offsetting the debt) `[VERIFY: appropriation availability and preconditions vary by jurisdiction and asset type; only partially confirmed against a primary source for England & Wales]`; a title-transfer arrangement is enforced simply by netting/close-out, since the lender already owns the assets. This clause sits in the security agreement.

## Capacity and authority

Capacity and authority is the set of representations and diligence items confirming that the borrower (and, if different, the pledgor) has the legal power to enter into the facility and grant security — critical for trusts (trustee power to borrow/charge, beneficiary interests), corporates (board authority, corporate benefit), and partnerships. It is documented through conditions precedent in the facility letter (constitutional documents, resolutions, trust deed extracts) and through representations repeated in the security agreement.

## Governing law and jurisdiction

This clause fixes which country's law governs the facility letter and security documents and which courts (or arbitral seat) have jurisdiction over disputes. For SBL it also determines which financial-collateral regime and perfection rules apply to the security, which is why it is treated as a core clause rather than boilerplate in this playbook — the cross-border overlay (England & Wales, Switzerland, Luxembourg) hangs directly off this choice.

## No advice and non-reliance

**Synonyms:** no-advice, non-reliance, risk acknowledgement.

A representation, usually in the facility letter, that the lender is not giving investment, tax, or legal advice in connection with the facility and that the borrower is relying on its own judgement (and advisers) in deciding to borrow against its portfolio and in selecting or retaining pledged assets. It is closely linked to the MiFID II / FinSA suitability and appropriateness regime, because a Lombard facility that shades into a recommendation about which securities to hold or acquire risks being treated as investment advice rather than pure lending.

---

## Additional canonical terms

### PDMR / insider / closed period

**Synonyms:** person discharging managerial responsibilities, insider, closed period.

A **PDMR** (person discharging managerial responsibilities) or **insider** is someone who, by virtue of their role or access, holds inside information about an issuer; a **closed period** is a defined window (commonly ahead of results announcements) during which such persons are restricted from dealing in that issuer's securities. This matters in SBL because pledging shares, and especially any enforcement sale of pledged shares, can itself constitute "dealing" for market-abuse purposes if the pledgor is a PDMR or insider of the pledged issuer, and closed periods can restrict both the initial pledge and any enforcement sale. Captured via a representation in the facility letter/security agreement plus a market-abuse regulatory flag in this playbook.

### Lombard loan / SBL / securities-backed lending / margin loan

A **Lombard loan** is the Swiss and continental European term for credit extended against a pledge of a client's securities portfolio; **SBL** (securities-based lending), **securities-backed lending**, and (in a US idiom) **margin loan** describe the same underlying product in UK/US usage. All are credit secured against an investment portfolio, structurally distinct from securities lending (see below). Documented via the facility letter, security agreement, and (where relevant) account control agreement.

### Securities lending (what SBL is NOT)

**Securities lending** is the temporary transfer of securities themselves (typically to a borrower such as a short seller or market-maker) in exchange for a fee and collateral, governed by instruments such as a Global Master Securities Lending Agreement. It is a different product with a different risk profile from SBL/Lombard lending, where securities are pledged as collateral for a cash loan and are not themselves lent out. This playbook deliberately excludes securities-lending drafting conventions (LMA/LSTA syndicated-loan and GMSLA precedent are also out of scope per the brief).

### Uncommitted demand facility vs committed term facility

See "Facility type" above.

### Account control agreement / control

See "Security structure and control" above. The **account control agreement** is the tripartite document (pledgor/borrower, lender as secured party, third-party custodian) under which the custodian agrees to act on the lender's instructions regarding the pledged account, used whenever the lender is not itself the custodian.

### Custodian

The institution holding the pledged securities in custody. Where the lender is also the custodian, perfection of the security interest and enforcement are operationally simpler; where a third-party custodian holds the assets, an account control agreement is required and adds a layer of counterparty and operational risk.

### MAC clause

**Synonyms:** material adverse change.

A MAC (material adverse change) clause is an event of default triggered by a significant deterioration in the borrower's (or, less commonly, the collateral's) financial condition or ability to perform, assessed qualitatively rather than by a fixed metric. It is one of the harder-edged events of default to invoke because it is inherently judgement-based, which is why this playbook flags it as an area with limited automation.

### Cross-collateralisation and set-off

**Cross-collateralisation** is using collateral pledged for one facility to secure other facilities with the same lender; **set-off** is the lender's right to apply credit balances the borrower holds with it against amounts owed under the facility. Both increase the lender's effective security but raise complexity where other facilities, other pledgors, or other jurisdictions are involved; captured in the security agreement and flagged by the intake field for other facilities with the lender.

### Benchmark (SONIA, SARON, EURIBOR)

The reference interest rate used to calculate interest on the facility: **SONIA** (Sterling Overnight Index Average) for GBP facilities, **SARON** (Swiss Average Rate Overnight) for CHF, and **EURIBOR** (Euro Interbank Offered Rate) for EUR. Set out in the facility letter along with any fallback provisions if the benchmark is discontinued or unavailable.

### Currency mismatch

A currency mismatch arises where the facility currency differs from the currency (or currencies) of the pledged collateral, introducing FX risk that can erode lending value independent of the securities' own price movement. This playbook applies an FX haircut note and a tightened lender-discretion floor wherever the intake shows a currency mismatch.

### Financial collateral arrangement (regime overview)

A **financial collateral arrangement** is a category of security or title-transfer arrangement over cash or financial instruments that qualifies for a simplified statutory regime disapplying certain general-law formalities (for example, registration or written-form requirements) in exchange for meeting defined scope conditions. Three regimes are relevant to this playbook:
- **England & Wales — Financial Collateral Arrangements (No. 2) Regulations 2003** (SI 2003/3226, implementing EU Directive 2002/47/EC): confirmed by primary-text review to require both the collateral-provider and collateral-taker to be non-natural persons for the regime to apply, and to disapply Companies Act 2006 charge-registration requirements (sections 859A/859H) for qualifying security arrangements. Appropriation as an enforcement method was not clearly confirmed from the primary text reviewed `[VERIFY]`.
- **Luxembourg — Law of 5 August 2005 on financial collateral arrangements**, as amended: widely reported (law-firm commentary reviewed, primary consolidated text not read in full) as one of the most creditor-friendly EU regimes, permitting enforcement on any contractually agreed trigger event and offering broad insolvency-remoteness. Treatment of natural-person collateral providers `[VERIFY]`.
- **Switzerland — Federal Intermediated Securities Act (FISA/BEG)**: governs security interests over intermediated securities, created either by pledge (via an account control agreement with the intermediary) or by security transfer of title; permits private enforcement (Privatverwertung), including appropriation (Selbsteintritt) of intermediated securities, per secondary commentary reviewed. Interaction with the Swiss Code of Obligations general pledge provisions and the Debt Enforcement and Bankruptcy Act `[VERIFY]`.

### Eligible collateral

See "Eligible collateral and lending values" above.

### Lender discretion

See "Lender discretion over valuation and eligibility" above.

### No-advice / non-reliance

See "No advice and non-reliance" above.

### Third-party security / pledgor / surety defences

**Third-party security** arises where the person granting the pledge (the **pledgor**) is not the borrower — for example a spouse, family trust, or holding company securing a relative's or affiliate's facility. Because the pledgor receives no direct benefit from the loan, many legal systems give third-party guarantors and security providers **surety-type defences** (for example, discharge if the lender varies the facility terms without the pledgor's consent, or a requirement that the pledgor receive independent legal advice before signing). This playbook requires a representation that independent advice was taken and tightens the capacity/authority floor whenever the intake shows a third-party pledgor. `[VERIFY: the precise content and availability of surety defences is highly jurisdiction- and fact-specific and was not confirmed against primary case law]`.
