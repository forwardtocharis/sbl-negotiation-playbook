# WP7 research: jurisdiction overlay (England & Wales, Switzerland, Luxembourg)

Researched 2026-09-21. Status: `draft`. Written from the lender's (private bank's) side, for a
facility secured on a portfolio of intermediated securities and cash held with a custodian.

**Method and honesty note.** Everything marked `verified: true` below was read by me in the primary
text at the URL given (statute text on legislation.gov.uk, fedlex.admin.ch PDF-A official
translations, legilux.public.lu consolidated code, the CSSF-published consolidated text of the
Luxembourg collateral law, the HCCH status table and Convention text, or the FCA Handbook).
Anything I could not open, or could not confirm word for word, is marked `[VERIFY]` and
`verified: false`. Nothing here is a substitute for local counsel: cross-border perfection and
enforceability conclusions are on the not-automated register.

Reliability grades: **A** primary law / regulator; **B** filed agreement / published bank terms;
**C** commentary (law-firm briefing, practitioner guide, textbook).

This file is research input for `playbook/jurisdictions/*.yaml`. It deliberately does **not**
create YAML — the schema is being frozen elsewhere.

---

## england_wales

### creation

For a portfolio of intermediated securities and cash held with a custodian, English practice takes a
**security interest** — normally an equitable mortgage or a fixed charge over the securities account,
the securities credited to it, the cash balances and all proceeds, with a floating charge fallback —
or, less commonly in Lombard lending, a **title transfer** collateral arrangement under which legal
and beneficial ownership passes and the taker owes an obligation to deliver equivalent assets back.
A true common-law pledge is awkward here because it depends on delivery of possession of a tangible
thing, which is why English custody security is drafted as mortgage/charge language rather than as a
pledge. The FCARs treat pledge, mortgage, fixed charge, floating charge and lien alike as "security
interests", so the financial collateral benefits can attach to a charge if the other conditions are
met. Lender-side: take a fixed charge or mortgage **plus** an express contractual power of sale
**and** an express power of appropriation, and do not rely on a label — in the 2012 English decision
[2012] EWHC 2997 (Ch) the court treated a clause drafted as a "general lien" over intangible
custody assets as a charge.

Sources:
- ref: "FCARs reg 3 (current)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/3"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Definitions of security interest (pledge, mortgage, fixed charge, floating charge, lien), financial collateral, possession, and the two arrangement types."
- ref: "[2012] EWHC 2997 (Ch) — via UK-FCL-BRIEF-01 (law-firm briefing, Nov 2012)"
  type: law_firm_briefing
  url: "https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2012/11/financial-collateral-remains-a-gray-area.pdf"
  retrieved: 2026-09-21
  reliability: C
  verified: true
  note: "Briefing states the court analysed a clause labelled general lien over intangible custody assets as a charge; also cites [2010] EWHC 1772 (Ch)."

### registration_filing

For a **corporate** chargor, Companies Act 2006 s.859A would normally require a statement of
particulars to reach the registrar within 21 days beginning with the day after creation, and s.859H
makes an unregistered registrable charge void against a liquidator, administrator or creditor.
FCARs reg 4(4), as amended in 2013, disapplies **both** s.859A and s.859H in relation to a security
financial collateral arrangement and any charge created or arising under one — so a qualifying
arrangement over a securities account needs no Companies House filing. The weak link is that the
exemption is only as good as the qualification: if the arrangement turns out not to be a security
FCA (individual party, or insufficient possession/control), the registration duty was live all along
and the 21 days have gone. Lender-side line: **register protectively wherever there is any doubt**
— a needless registration costs nothing, a missed one is fatal. There is no public filing regime for
security granted by an individual over intangible investments in England, so registration is simply
not a live question for a natural-person pledgor.

Sources:
- ref: "Companies Act 2006 s.859A"
  type: primary_law
  url: "https://www.legislation.gov.uk/ukpga/2006/46/section/859A"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Registrable charges created by a company; 21-day period from the day after creation; delivery by the company or any person interested; limited exceptions in subsection (6)."
- ref: "FCARs reg 4 (current)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/4"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Reg 4(4) disapplies CA 2006 ss.859A and 859H for a security financial collateral arrangement and any charge under one; section references substituted with effect from 6 April 2013."

### perfection_depends_on

England has no filing-based perfection for this collateral, so two things do the work commercially.
First, whether the charge is **fixed** rather than floating, which turns on how far the client is free
to deal with the collateral without the lender's consent. Second, whether the collateral-taker has
**possession or control** for FCARs purposes: reg 3 treats collateral as in the taker's possession
where it is credited to an account in the taker's name and the provider's rights are limited to
substituting collateral of the same or greater value or withdrawing excess. The case law requires
real dispossession of the provider — [2010] EWHC
1772 (Ch) and [2012] EWHC 2997 (Ch) — so a lender holding
assets as a pure nominee with no more dominion than a custodian does not have control. Where the
lender is also the custodian, control is straightforward and should be documented in the security
agreement and reflected in the account terms. Where a third-party custodian holds, take an **account
control agreement** that switches off the client's dealing and withdrawal rights on a default notice
and obliges the custodian to act on the lender's instructions alone.

Sources:
- ref: "FCARs reg 3 (current)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/3"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Possession includes crediting to an account in the taker's name where provider rights are limited to substitution of equal-or-greater value collateral or withdrawal of excess."
- ref: "UK-FCL-BRIEF-01: law-firm briefing on financial collateral possession and control (Nov 2012)"
  type: law_firm_briefing
  url: "https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2012/11/financial-collateral-remains-a-gray-area.pdf"
  retrieved: 2026-09-21
  reliability: C
  verified: true
  note: "Both possession and control require more than mere custody; dispossession of the collateral-provider is the key; the 2011 amendment added an inclusive possession definition; case citations as above."

### enforcement_route

Two routes, and a good facility keeps both open. **Sale**: under an express contractual power of
sale, or the Law of Property Act 1925 s.101 power where the security is made by deed. Section 101
is cut down by s.103, which stops the power being exercised until notice requiring payment has been
served and three months' default has run, or two months' interest is in arrear, or another provision
of the mortgage deed has been breached — so lenders routinely contract out of s.103 and rely on
express drafting, and remain subject to the mortgagee's equitable duty to take reasonable care to
obtain a proper price. **Appropriation**: FCARs reg 17 lets a collateral-taker whose security
financial collateral arrangement contains an appropriation power appropriate the collateral in
accordance with its terms **without any order for foreclosure from the court**, and reg 18 requires
the taker to value the collateral in accordance with the arrangement and in any event **in a
commercially reasonable manner**, accounting to the provider for any excess and leaving the provider
liable for any shortfall. Outside the FCARs there is no self-help appropriation in English law —
foreclosure needs the court — which is why the FCAR qualification matters so much. Reg 8 disapplies
the administration moratorium and the related Insolvency Act 1986 restrictions on enforcing security
for financial collateral arrangements; for an individual chargor there is no equivalent need, because
IA 1986 s.285(4) already preserves the secured creditor's right to enforce notwithstanding the
restrictions on creditors' remedies after a bankruptcy order.

Sources:
- ref: "FCARs reg 17 (as made)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/17/made"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Appropriation under an express power in a security FCA, without any court order for foreclosure."
- ref: "FCARs reg 18 (as made)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/18/made"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Duty to value per the arrangement and in any event in a commercially reasonable manner, and to account for the difference."
- ref: "FCARs reg 8 (as made)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/8/made"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Disapplies IA 1986 Sch B1 paras 43(2), 44, 70, 71, 41(2), ss.10(1)(b), 11(2), 11(3)(c), 15(1)-(2) and Sch A1 moratorium provisions for FCAs."
- ref: "Law of Property Act 1925 s.101"
  type: primary_law
  url: "https://www.legislation.gov.uk/ukpga/Geo5/15-16/20/section/101"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Mortgagee's powers where the mortgage is by deed: sale by auction or private contract, insurance, appointment of a receiver; sale and receiver powers arise once the mortgage money is due."
- ref: "Law of Property Act 1925 s.103"
  type: primary_law
  url: "https://www.legislation.gov.uk/ukpga/Geo5/15-16/20/section/103"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Three alternative pre-conditions to the s.101 power of sale: notice plus three months' default, two months' interest in arrear, or breach of another provision."
- ref: "Insolvency Act 1986 s.285"
  type: primary_law
  url: "https://www.legislation.gov.uk/ukpga/1986/45/section/285"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Restrictions on creditors' remedies after a bankruptcy order; subsection (4) preserves the right of a secured creditor to enforce its security."

### financial_collateral_regime

The instrument is the **Financial Collateral Arrangements (No. 2) Regulations 2003 (SI 2003/3226)**,
implementing Directive 2002/47/EC and retained after EU exit. It recognises two arrangement types,
the **security financial collateral arrangement** and the **title transfer financial collateral
arrangement**. Both require written evidence, collateral consisting of cash, financial instruments or
credit claims, delivery/transfer so that the collateral is in the possession or under the control of
the taker, and — the decisive point for private wealth — that **both parties are non-natural
persons**, a "non-natural person" being any corporate body, unincorporated firm, partnership or body
with legal personality **except an individual**, including bodies formed under foreign or
international law. The benefits are: no Companies Act registration (reg 4), disapplication of
insolvency restrictions on enforcement and of certain avoidance provisions (regs 8 and 10), close-out
netting effective in accordance with its terms (reg 12), protection where the taker was unaware of a
winding-up or reorganisation (reg 13), right of use (reg 16), and appropriation without a court order
(reg 17) subject to commercially reasonable valuation (reg 18). So for an individual client or an
individual third-party pledgor the whole package is off the table — see "Inputs for rules R04 and
R14" below.

Sources:
- ref: "FCARs reg 3 (current)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/3"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Both parties to a security FCA and to a title transfer FCA must be non-natural persons; non-natural person excludes an individual."
- ref: "FCARs table of contents (as made)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/contents/made"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Structure of the Regulations: Part 2 formalities, Part 3 modification of insolvency law (regs 8-15), Part 4 right of use and appropriation (regs 16-18), Part 5 conflict of laws (reg 19)."

### governing_law_of_intermediated_securities

FCARs reg 19 applies a **PRIMA**-style rule to "book entry securities collateral": the listed
questions are governed by the **domestic law of the country in which the relevant account is
maintained**, with renvoi excluded. The questions covered are the legal nature and proprietary
effects of the collateral, the requirements for provision and for third-party effectiveness, whether
title is extinguished or subordinated by a competing interest or a good-faith acquisition, priority,
and the steps required to realise the collateral after an enforcement event. The UK is **not** a
contracting party to the 2006 Hague Securities Convention — the contracting parties are Mauritius,
Switzerland and the United States, and it entered into force on 1 April 2017 — so you cannot select
the proprietary law by agreement in the account agreement the way a Swiss-booked structure can.
Practical consequence for a deal lawyer: the governing law clause in the facility and security
documents does **not** settle the proprietary analysis; the **booking location of the account** does.
If the facility is English law but the account is in Zurich or Luxembourg, get local counsel on
creation, third-party effectiveness and realisation.

Sources:
- ref: "FCARs reg 19 (as made)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/19/made"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Applicable law for book entry securities collateral is the domestic law of the country where the relevant account is maintained; lists the five matters governed."
- ref: "HCCH status table, Convention #36 (2006 Securities Convention)"
  type: primary_law
  url: "https://www.hcch.net/en/instruments/conventions/status-table/?cid=72"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Three contracting parties: Mauritius (ratified 15-X-2009), Switzerland (14-IX-2009), USA (15-XII-2016); entry into force 1-IV-2017. UK, Luxembourg and the EU are not parties."

### practical_notes

Do these things in order. (1) Establish at intake whether **every party to the collateral
arrangement** is a non-natural person; if not, delete or condition any reliance on appropriation and
on the insolvency disapplications, and say so in the security agreement's enforcement clause rather
than leaving boilerplate that does not work. (2) Establish where the **account is maintained**,
because reg 19 makes that the proprietary law, and take local counsel if it is not England. (3) If
the lender is not the custodian, make an executed **account control agreement** a condition
precedent, and make sure it delivers dispossession in substance, not just a notice of charge. (4) For
a corporate chargor, decide the registration question deliberately and record the decision; if you
are relying on reg 4, you are betting the security on the FCAR qualification. (5) Draft both a sale
power and an appropriation power, contract out of LPA 1925 s.103, and specify the valuation method
you will use so that the reg 18 "commercially reasonable" standard is evidenced by a process, not
argued about after the event. (6) **Third-party pledgor**: take separate independent legal advice
confirmations and consider undue influence and misrepresentation risk where the pledgor is a spouse
or family member of the borrower; corporate pledgors raise corporate benefit and financial assistance
questions. (7) **Natural-person pledgor**: on bankruptcy, s.285(4) protects the right to enforce but
gives you none of the FCAR self-help; plan for a sale under a contractual power, not appropriation.

Sources:
- ref: "FCARs reg 3 (current)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/3"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Non-natural person requirement and possession/control definition drive steps (1) and (3)."
- ref: "Insolvency Act 1986 s.285"
  type: primary_law
  url: "https://www.legislation.gov.uk/ukpga/1986/45/section/285"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Secured creditor's enforcement rights preserved on personal bankruptcy."
- ref: "[VERIFY] English law on independent legal advice for third-party security (undue influence line of authority)"
  type: textbook
  url: ""
  retrieved: 2026-09-21
  reliability: C
  verified: false
  note: "Not researched in this work package. The practice point (independent advice for a non-commercial third-party pledgor) is stated from general practice and must be sourced before promotion beyond draft."

---

## switzerland

### creation

Security over **intermediated securities** (book-entry securities credited to a securities account
with a custodian — a bank, a securities firm, a fund management company for unit accounts, a CSD or
the SNB) is governed **exclusively** by the Federal Intermediated Securities Act (FISA / BEG,
SR 957.1); the Civil Code says so expressly. FISA gives three ways to make the disposal effective
against third parties: **credit** of the securities to the collateral taker's own securities account
on the account holder's instruction (Art. 24, which transfers full legal rights if the disposition is
framed that way); an irrevocable **control agreement** between the account holder and the custodian
under which the custodian must carry out the acquirer's instructions without any further consent or
cooperation from the account holder (Art. 25), which may cover specific securities, the whole account,
or a proportion of the account up to a stated value; and, where the collateral taker **is** the
custodian, a simple **agreement with the custodian**, effective against third parties on conclusion
(Art. 26). Cash balances are claims against the bank and sit outside FISA: they are pledged under
Civil Code Art. 899-900, which require a written pledge agreement, with the bank's own general terms
lien and set-off usually doing the heavy lifting. Lender-side: if you are the custodian, Art. 26 is
the cleanest and fastest route; if you are not, an Art. 25 control agreement is a condition precedent,
not a post-closing item.

Sources:
- ref: "FISA (SR 957.1) Arts 2, 4, 24, 25, 26"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/450/20230101/en/pdf-a/fedlex-data-admin-ch-eli-cc-2009-450-20230101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Official English translation. Art. 2(1) scope; Art. 4 who is a custodian; Art. 24 credit; Art. 25 irrevocable control agreement covering specific securities, a whole account or a value proportion; Art. 26 agreement with the custodian effective on conclusion."
- ref: "Swiss Civil Code (SR 210) Arts 899, 900, 901"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/24/233_245_233/20260101/en/pdf-a/fedlex-data-admin-ch-eli-cc-24-233_245_233-20260101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 899 pledge of assignable debts and rights; Art. 900 written pledge agreement for claims and other rights; Art. 901(3) pledging of intermediated securities is governed exclusively by FISA."
- ref: "CH-PRACT-01: practitioner overview, lending and taking security in Switzerland (law stated 1 May 2025)"
  type: law_firm_briefing
  url: "https://www.baerkarrer.ch/userdata/lending-and-taking-security-in-switzerland-overview.pdf"
  retrieved: 2026-09-21
  reliability: C
  verified: true
  note: "Confirms the two practical routes: pledge with an account control agreement under which the intermediary irrevocably agrees to follow the secured party's instructions, or security transfer of legal title by crediting the secured party's account."

### registration_filing

There is **no registration, filing or public register** for a pledge or a security transfer over
intermediated securities or over cash claims in Switzerland. Third-party effectiveness comes from the
FISA act of disposal itself — the credit under Art. 24, the control agreement under Art. 25, or the
Art. 26 agreement — and priority is determined by the time of the disposition (Art. 30(1)), with a
specific rule subordinating a custodian's own earlier rights where it enters into an Art. 25
agreement without expressly notifying the acquirer of them (Art. 30(2)). That makes Swiss collateral
quick to take, but it also means there is nothing to search: your diligence is documentary. Get a
custodian confirmation of the account holdings, an express waiver or subordination of the custodian's
own statutory right of retention and foreclosure and of any general terms lien and set-off, and a
confirmation that no earlier control agreement exists.

Sources:
- ref: "FISA (SR 957.1) Arts 21, 30"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/450/20230101/en/pdf-a/fedlex-data-admin-ch-eli-cc-2009-450-20230101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 21 custodian's right of retention and foreclosure for due debts arising from custody or acquisition financing; Art. 30(1) first-in-time priority; Art. 30(2) custodian's undisclosed earlier right subordinated to the acquirer."

### perfection_depends_on

**Control, exercised through the custodian.** There is nothing to file and nothing to notify beyond
the custodian: either the securities are credited to the lender's account (Art. 24), or the custodian
is irrevocably bound to follow the lender's instructions without the client's further consent
(Art. 25), or the lender is itself the custodian and the agreement alone does it (Art. 26). Two
traps to close in the documents. First, the custodian has its **own** statutory right of retention
and foreclosure over securities credited to the account for debts arising from the custody or the
financing of their acquisition (Art. 21), so where a third-party custodian holds, deal with its
ranking expressly. Second, a **right of use** in favour of the custodian requires the account
holder's authorisation and, unless the account holder is a qualified investor, that authorisation
must be **in writing and may not be included in general terms and conditions** (Art. 22) — which
matters directly for a private individual client.

Sources:
- ref: "FISA (SR 957.1) Arts 21, 22, 23, 24, 25, 26"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/450/20230101/en/pdf-a/fedlex-data-admin-ch-eli-cc-2009-450-20230101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 22(2): right-of-use authorisation must be in writing and not in GTCs unless the account holder is a qualified investor; Art. 23 return of collateral and the option to realise under Art. 31 instead."

### enforcement_route

FISA Art. 31 gives the secured party a **statutory private realisation power**: it may realise the
intermediated securities in accordance with the terms of the security agreement either by **selling**
them and offsetting the proceeds against the secured debt, or by **appropriating** securities whose
value can be determined objectively and offsetting that value. Critically, Art. 31(2) says that power
is **not affected by the commencement of debt enforcement, reorganisation or protective proceedings**
against the collateral provider, and Art. 31(3) says the custodian is neither bound nor entitled to
check whether the realisation conditions are met (Art. 31(4) preserves the secured party's liability
if they were not). Art. 32(1) requires the secured party to **give notice to the provider before
realisation**, and that notice may be waived only by a provider that is a custodian or a **qualified
investor**; Art. 32(2) requires an account and remittance of surplus proceeds. This is a real
departure from the ordinary Swiss default, where a pledge-secured claim is enforced through debt
enforcement proceedings to realise the pledge under the Debt Enforcement and Bankruptcy Act (DEBA
Art. 41, Arts 151-158), where private enforcement of a pledge generally stops once bankruptcy is
declared because pledged assets fall into the estate (DEBA Art. 198), and where the Civil Code
invalidates any agreement that the pledged chattel becomes the pledgee's property on default (Art. 894,
the *lex commissoria* prohibition). Note also the extraterritorial reach: FISA Art. 2(1bis) applies
Art. 31(2) to intermediated securities held with a custodian in Switzerland **or abroad**, even where
that custody is subject to foreign law.

Sources:
- ref: "FISA (SR 957.1) Arts 2(1bis), 31, 32"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/450/20230101/en/pdf-a/fedlex-data-admin-ch-eli-cc-2009-450-20230101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 31(1) sale or appropriation where value objectively determinable; 31(2) power unaffected by debt enforcement, reorganisation or protective proceedings; 31(3) custodian need not verify; Art. 32(1) pre-realisation notice waivable only by a custodian or qualified investor; 32(2) account and surplus; Art. 2(1bis) reach to foreign-held intermediated securities."
- ref: "DEBA (SR 281.1) Arts 41, 198, 219"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/11/529_488_529/20260101/en/pdf-a/fedlex-data-admin-ch-eli-cc-11-529_488_529-20260101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 41 pledge-secured claims are continued by proceedings to realise a pledge (Arts 151-158), with the debtor able to demand the pledge be realised first; Art. 198 pledged assets fall into the bankruptcy estate subject to the pledgee's preferential rights; Art. 219(1) pledge-secured claims are paid in advance from the proceeds of sale of the pledges."
- ref: "Swiss Civil Code (SR 210) Arts 891, 894"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/24/233_245_233/20260101/en/pdf-a/fedlex-data-admin-ch-eli-cc-24-233_245_233-20260101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 891 creditor may satisfy its claim from the proceeds of the pledge on default; Art. 894 any agreement that the pledged chattel becomes the pledgee's property on default is invalid."
- ref: "CH-PRACT-01: practitioner overview, lending and taking security in Switzerland"
  type: law_firm_briefing
  url: "https://www.baerkarrer.ch/userdata/lending-and-taking-security-in-switzerland-overview.pdf"
  retrieved: 2026-09-21
  reliability: C
  verified: true
  note: "Private enforcement must be organised and documented to obtain the best price obtainable in the circumstances; assets with an objectively determinable market value may be bought in by the secured party at market value with set-off and surplus returned; once bankruptcy is declared, private enforcement of pledges generally stops but security transferred by title transfer before opening stays outside the estate."

### financial_collateral_regime

Switzerland has **no** equivalent of Directive 2002/47/EC and no instrument called a financial
collateral regime; **FISA Chapters 5 and 6 do the same work** for intermediated securities. The
practical scope difference that matters in private wealth is that FISA contains **no requirement that
either party be a non-natural person**: a private individual can be the collateral provider and the
Art. 31 realisation power, including the insolvency override in Art. 31(2), still applies. The
trade-off runs the other way on process: an individual is **not** a "qualified investor" — Art. 5(d)
limits that to a custodian, a prudentially supervised insurance company, a public-law entity, a
pension fund, or a company with professional treasury management — so the pre-realisation notice in
Art. 32(1) **cannot be waived** for a private client, and the Art. 22 right-of-use authorisation
cannot be buried in general terms. Benefits of the regime, in lender terms: self-help sale or
appropriation without court involvement, survival of that power through the provider's insolvency or
moratorium, and no obligation on the custodian to second-guess the enforcement.

Sources:
- ref: "FISA (SR 957.1) Arts 5(d), 22, 31, 32"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/450/20230101/en/pdf-a/fedlex-data-admin-ch-eli-cc-2009-450-20230101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 5(d) closed definition of qualified investor, which does not include a natural person; Art. 32(1) notice waiver limited to custodians and qualified investors; no non-natural-person restriction anywhere in the security-interest provisions."

### governing_law_of_intermediated_securities

Switzerland is the outlier of the three and it works in the lender's favour. It **ratified the 2006
Hague Securities Convention on 14 September 2009**, and the Convention entered into force on
1 April 2017. Swiss private international law channels the question straight to it: PILA Art. 108a
defines intermediated securities by reference to the Convention and Art. 108c states that the law
applicable to intermediated securities is governed by the Convention. Under the Convention the
primary rule (Art. 4(1)) is the **law expressly agreed in the account agreement** as governing the
Convention issues, or another law expressly designated there, provided the relevant intermediary has
a qualifying office in that State; Art. 5 supplies sequential fall-backs (the office through which the
account agreement was entered into, then incorporation/organisation, then principal place of
business), and Art. 2 lists the issues governed (proprietary nature and effects, perfection, priority,
intermediary duties to competing claimants, realisation requirements, and extension to
distributions and proceeds). For claims and rights that are **not** intermediated securities — cash
claims, for example — PILA Art. 105 applies: the parties may choose the law governing the pledge but
that choice cannot be asserted against third parties; failing a choice, the pledge of claims is
governed by the law of the **pledgee's habitual residence**, and a law other than the one governing
the pledged right cannot be asserted against the debtor. So for a Swiss-booked account you can, in
principle, fix the proprietary law by agreement — something reg 19 in England and Art. 23 in
Luxembourg do not allow.

Sources:
- ref: "PILA (SR 291) Arts 105, 108a, 108b, 108c, 108d"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1988/1776_1776_1776/20260101/en/pdf-a/fedlex-data-admin-ch-eli-cc-1988-1776_1776_1776-20260101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 105 choice of law for the pledging of claims, securities and other rights, not assertable against third parties, with the pledgee's habitual residence as the default; Arts 108a and 108c route intermediated securities to the 2006 Hague Convention."
- ref: "HCCH 2006 Securities Convention, Arts 2, 4, 5 (full text)"
  type: primary_law
  url: "https://www.hcch.net/en/instruments/conventions/full-text/?cid=72"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 2 the seven issues governed; Art. 4(1) primary rule of the law expressly agreed in the account agreement subject to the qualifying office test; Art. 5 the three sequential fall-backs."
- ref: "HCCH status table, Convention #36"
  type: primary_law
  url: "https://www.hcch.net/en/instruments/conventions/status-table/?cid=72"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Switzerland ratified 14-IX-2009; entry into force 1-IV-2017."

### practical_notes

(1) If the bank is the Swiss custodian, use the Art. 26 route and make sure the security agreement
and the custody terms agree with each other; if a third-party custodian holds, an executed Art. 25
control agreement plus a waiver or subordination of the custodian's Art. 21 rights is a condition
precedent. (2) Build the **Art. 32(1) notice** into the enforcement clause and into the operational
runbook: for a private individual pledgor it cannot be waived, so a facility that assumes instant
liquidation without notice is wrong for that client type. Define the notice period, the delivery
method and the trigger, and keep evidence. (3) Rely on **Art. 31(2)** as the answer to the DEBA
problem, and say so in the enforcement clause; without FISA, a pledge would otherwise be dragged into
DEBA pledge-realisation proceedings, and on bankruptcy the pledged assets fall into the estate under
DEBA Art. 198 with the pledgee taking priority in the proceeds under Art. 219(1). (4) Appropriation
is available only where the value can be **determined objectively** (Art. 31(1)(b)) — so listed
liquid securities yes; gated funds, structured products and unlisted positions probably not, and
those should be enforced by sale with a documented process. (5) **Third-party pledgor**: the Art. 32
notice goes to the *provider* of the security interest, not the borrower, so identify the notice
recipient correctly. (6) Bank secrecy and data protection are live on every Swiss booking — see
"Inputs for rules R04 and R14". (7) FinSA Art. 3(c)(5) makes the granting of loans to finance
transactions with financial instruments a **financial service** in its own right, which pulls a
purpose-to-invest Lombard facility into the FinSA conduct perimeter.

Sources:
- ref: "FISA (SR 957.1) Arts 21, 26, 31, 32"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/450/20230101/en/pdf-a/fedlex-data-admin-ch-eli-cc-2009-450-20230101-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Basis for the CP list, the non-waivable notice for private clients, and the objective-value limit on appropriation."
- ref: "FinSA (SR 950.1) Art. 3(c)"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2019/758/20240301/en/pdf-a/fedlex-data-admin-ch-eli-cc-2019-758-20240301-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 3(c)(5): granting of loans to finance transactions with financial instruments is a financial service."

---

## luxembourg

### creation

The **Law of 5 August 2005 on financial collateral arrangements**, as amended (most recently by the
laws of 20 July 2022 and 15 July 2024), governs the whole field. "Collateral" means financial
instruments and claims, and "financial instruments" is given the broadest possible meaning, expressly
including shares, units in collective investment undertakings, bonds and certificates of deposit. A
pledge is created by agreement; the provision of collateral must be capable of being evidenced in
writing, in electronic or other durable form, and must allow the collateral to be identified — and
for book-entry financial instruments and cash claims it is enough to show that they have been credited
to, or form a credit in, a designated account. Article 4 allows the parties to agree an
**all-present-and-future pledge** without needing to designate the collateral specifically, which is
exactly what a revolving Lombard portfolio needs. Article 2(4) allows collateral to be provided to a
person acting for the account of beneficiaries, a fiduciary or a trustee for determined or
determinable third-party beneficiaries, who then enjoy the same rights as direct beneficiaries. The
Law also covers **title transfer for security purposes and fiduciary transfer** (Art. 13 — if
fiduciary, the fiduciary must be a financial sector professional) and repurchase agreements (Arts 15-17).

Sources:
- ref: "Luxembourg Law of 5 August 2005 on financial collateral arrangements (CSSF consolidated text, updated 15 July 2024), Arts 1, 2, 3, 4, 13"
  type: primary_law
  url: "https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "CSSF consolidation, stated to be for information only with the Journal officiel texts authoritative. Art. 1(1) and 1(8) definitions; Art. 2(2) written evidence and identification, account credit sufficient for book-entry instruments and cash claims; Art. 2(4) collateral to a fiduciary, trustee or person acting for beneficiaries; Art. 4 all-assets pledge without specific designation; Art. 13 title transfer and fiduciary transfer."

### registration_filing

**None.** Article 26 states that instruments evidencing a financial collateral arrangement are not
subject to registration formalities, and are registered at the fixed rate if voluntarily submitted to
the registration formality. There is no equivalent of the Companies Act 2006 charge register for a
financial collateral arrangement, and no notice filing, which is one of the reasons Luxembourg
collateral is quick to take. As in Switzerland, the corollary is that there is nothing to search:
priority is determined by the date on which each pledge became enforceable against third parties
(Art. 5(6)), so the diligence is documentary — custodian confirmations, and express treatment of the
custodian's own ranking.

Sources:
- ref: "Luxembourg Law of 5 August 2005, Arts 5(6), 26"
  type: primary_law
  url: "https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 26 no registration formalities; Art. 5(6) priority by date of enforceability against third parties."

### perfection_depends_on

**Possession, defined functionally through the custodian.** Article 5(1) says the privilege only
remains on the pledged collateral if it has been and remains (or is deemed to have remained) in the
possession of the pledgee or an agreed third party. For **book-entry financial instruments**,
Art. 5(2)(a) gives four alternatives: (i) simply concluding the pledge agreement, where the pledgee
**is** the custodian; (ii) a three-party agreement between provider, pledgee and custodian, or a
two-party agreement notified to the custodian, under which the custodian will act on the pledgee's
instructions **without any further agreement of the provider**; (iii) booking the instruments to an
account of the pledgee; or (iv) earmarking them, without number specification, in the custodian's
books on an account in the provider's or an agreed third-party custodian's name. Routes (ii)-(iv)
are treated as a **waiver by the custodian of its own pledge ranking** unless otherwise agreed or
notified. For other financial instruments, Art. 5(3) requires notification to or acknowledgement by
the issuer or the third-party custodian. For a pledge over **claims** — including cash balances —
Art. 5(4) makes it effective against the debtor and third parties on the mere conclusion of the
pledge contract, though the account debtor can still validly pay the provider until it learns of the
pledge. Article 2(3) confirms that a right of substitution, a right to withdraw excess collateral, a
right to collect proceeds until further notice, and a reserved right of the provider to give
instructions **do not** prejudice the collateral having been provided — a materially more
collateral-taker-friendly position than the English "dispossession" case law.

Sources:
- ref: "Luxembourg Law of 5 August 2005, Arts 2(3), 5"
  type: primary_law
  url: "https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 2(3) substitution, withdrawal of excess, collection of proceeds and instruction rights do not prejudice provision; Art. 5(1)-(4) the possession routes for book-entry instruments, other instruments and claims, and the custodian ranking waiver."

### enforcement_route

Article 11(1) is the centrepiece: on an enforcement event the pledgee may, **unless otherwise
provided for, without prior notice**, (a) appropriate the pledged collateral, or have a third party
appropriate it, at a price determined before or after appropriation by the agreed valuation method;
(b) assign or cause it to be assigned **by private sale in a commercially reasonable manner**, on a
trading venue on which it is admitted to trading, or by public auction; (c) obtain a judgment
attributing the collateral in payment on an expert valuation; (d) net under Part V; (e) appropriate
listed financial instruments at the market price, or units in a collective investment undertaking at
that price or at the last published net asset value provided it is not more than a year old;
(f) request redemption of pledged fund units at the redemption price; or (g) exercise the rights under
a pledged insurance contract, including surrender. Article 11(3) obliges a third-party custodian to
transfer the instruments to the pledgee on notice of an enforcement event **without the provider's
consent and without informing it in advance**, and allows the pledgee to demand payment directly from
the debtor of a pledged monetary claim. Article 11(2) sets out the public-auction machinery in detail
(a Luxembourg bailiff or notary as auctioneer, at least eight working days' press notice with
prescribed content, sale to the highest bidder with payment permitted by set-off against the secured
obligations, and minutes within three working days). "Enforcement event" is whatever the parties
agree (Art. 1(6)). Lender-side: choose and specify the route and the valuation method in the security
agreement, because Art. 11 is a menu, and "unless otherwise provided for" means your drafting can
narrow it as well as widen it.

Sources:
- ref: "Luxembourg Law of 5 August 2005, Arts 1(6), 11"
  type: primary_law
  url: "https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 1(6) enforcement event as agreed; Art. 11(1) the seven enforcement routes without prior notice; Art. 11(2) public auction procedure; Art. 11(3) third-party custodian must transfer on notice without the provider's consent or prior information."
- ref: "LU-FCL-BRIEF-01: law-firm briefing on the Luxembourg financial collateral law (2022)"
  type: law_firm_briefing
  url: "https://www.addleshawgoddard.com/en/insights/insights-briefings/2022/finance/luxembourg-financial-collateral-law/"
  retrieved: 2026-09-21
  reliability: C
  verified: true
  note: "Confirms the 2022 amendments broadened enforcement to sale on a trading venue (regulated market, MTF or OTF) and added enforcement of pledged insurance contracts. Does not address natural persons, prior notice or insolvency remoteness."

### financial_collateral_regime

The instrument is the **Law of 5 August 2005 on financial collateral arrangements**, transposing
Directive 2002/47/EC and repealing the earlier repo and transfer-of-ownership-for-security laws. On
**scope of persons**, the Law contains **no** requirement equivalent to FCARs reg 3 that both parties
be non-natural persons: Article 2(1) expressly contemplates financial collateral arrangements and
netting agreements "entered into either by a merchant or a non-merchant", and Article 20(4) carves
the **Law of 8 December 2000 on over-indebtedness** out of the general disapplication of insolvency
law — a carve-out that only makes sense if private individuals are within scope. (That last step is
my inference from the primary text, not a quotation; treat it as a drafting assumption to be
confirmed by Luxembourg counsel.) The core benefits are in Articles 20 and 21: financial collateral
arrangements, the agreed enforcement events, netting agreements and the agreed valuation and
enforcement measures are valid and enforceable against third parties, commissioners, receivers and
liquidators **notwithstanding reorganisation measures, winding-up proceedings or any other similar
national or foreign proceedings** (Art. 20(1)); termination, valuation, enforcement and netting
triggered by an enforcement procedure or protective measure are deemed to have occurred before it
(Art. 20(2)); the listed Civil Code, Commercial Code and national or foreign insolvency, attachment
and similar provisions simply do not apply, with the over-indebtedness law the sole carve-out
(Art. 20(4)); **the same rules apply on the death or incapacity of the collateral provider or the
debtor** (Art. 20(4), final paragraph); arrangements made on the day of opening but before the court
decision are valid, and arrangements made after it are valid if the taker proves it neither knew nor
should have known (Art. 21). Article 24 confirms that the disapplied national provisions remain
disapplied where the collateral provider is established or resident in Luxembourg.

Sources:
- ref: "Luxembourg Law of 5 August 2005, Arts 2(1), 20, 21, 24"
  type: primary_law
  url: "https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 2(1) merchant or non-merchant; Art. 20(1)-(4) insolvency remoteness and the over-indebtedness (Law of 8 December 2000) carve-out, plus the death-or-incapacity rule; Art. 21 day-of-opening and good-faith protection; Art. 24 territorial confirmation."
- ref: "[VERIFY] Luxembourg exercise of the Directive 2002/47/EC Art. 1(3) option on natural persons"
  type: law_firm_briefing
  url: "https://www.luxembourgforfinance.com/portfolio/luxembourgs-collateral-law-particularly-favourable-to-beneficiaries/"
  retrieved: 2026-09-21
  reliability: C
  verified: false
  note: "URL seen in search results but NOT opened. Search snippet indicated that, except for over-indebtedness proceedings concerning private individuals, financial collateral arrangements are safe-harboured. Needs to be opened and confirmed, or replaced with a Luxembourg counsel confirmation, before this point moves past draft."

### governing_law_of_intermediated_securities

Article 23 is Luxembourg's **PRIMA** rule and it mirrors FCARs reg 19 almost exactly: any question on
the listed matters arising in relation to financial collateral over financial instruments transferable
by book entry is governed by the **law of the country in which the relevant account is maintained**,
meaning its domestic law with renvoi excluded. The matters covered are the legal nature and
proprietary effects, the requirements for provision and for third-party effectiveness, extinction or
subordination by a competing interest or a good-faith acquisition, the custodian's obligations to a
competing claimant, the conditions for realisation after an enforcement event, and the extent of the
arrangement over dividends, income, distributions, reimbursements and proceeds. "Relevant account"
is defined in Art. 1(3) as the register or account in which the entries providing the collateral are
made, **which may be maintained by the collateral taker itself**. Luxembourg is **not** a contracting
party to the 2006 Hague Securities Convention, so there is no choice-of-law route to displace the
account-location rule. Practical consequence is the same as England's: the account booking location,
not the governing law of the pledge agreement, drives the proprietary analysis.

Sources:
- ref: "Luxembourg Law of 5 August 2005, Arts 1(3), 23"
  type: primary_law
  url: "https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 1(3) relevant account, which may be maintained by the collateral taker; Art. 23(1)-(2) the account-location rule, exclusion of renvoi, and the six matters governed."
- ref: "HCCH status table, Convention #36"
  type: primary_law
  url: "https://www.hcch.net/en/instruments/conventions/status-table/?cid=72"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Luxembourg and the EU are not contracting parties."

### practical_notes

(1) If the bank is the Luxembourg custodian, Art. 5(2)(a)(i) means the pledge agreement alone
perfects — the cheapest structure of the three jurisdictions. If a third-party custodian holds, use
the Art. 5(2)(a)(ii) route and take the custodian's acknowledgement in writing, remembering that
route (ii) is treated as the custodian waiving its own ranking unless it says otherwise. (2) Use the
Art. 4 all-present-and-future formulation so that substitutions in a revolving portfolio do not need
new security, and rely on Art. 2(3) so that the client's right to trade the portfolio until a default
notice does not undermine the pledge — this is a genuine structural advantage over English law. (3)
**Specify the valuation method** in the security agreement: Art. 11(1)(a) appropriation is priced by
"the agreed valuation method", so if you do not agree one you are pushed toward private sale in a
commercially reasonable manner or auction. (4) Enforcement **without prior notice** is the statutory
default, but Art. 11(1) opens with "unless otherwise provided for" — so do not let a negotiated notice
period creep into the security agreement unless you mean it, and if the client insists, put it in the
facility letter as a courtesy undertaking rather than a condition of the enforcement power. (5)
**Natural-person pledgor**: the Law applies, but the over-indebtedness carve-out in Art. 20(4) means
you cannot assume full insolvency remoteness against a Luxembourg-resident individual; get Luxembourg
counsel to scope the over-indebtedness procedure for the specific client. (6) **Third-party
pledgor**: the Law is comfortable with security for a third party's obligations and with fiduciary or
agent structures under Art. 2(4), and Art. 2(6) even allows the provider to waive its recourse claims
against the principal debtor, valid against third parties — but corporate benefit and, for an
individual, independent advice remain ordinary diligence items. (7) The death or incapacity rule in
Art. 20(4) is directly useful for a private-client pledgor and worth citing in the events-of-default
rationale.

Sources:
- ref: "Luxembourg Law of 5 August 2005, Arts 2(3), 2(4), 2(6), 4, 5(2), 11, 20(4)"
  type: primary_law
  url: "https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Supports each of the seven practice points; Art. 2(6) waiver by the provider of its claims against the debtor, valid between parties and against third parties."

---

## Inputs for rules R04 and R14

### R04 — `fcar_safe_harbour_uncertain` (natural-person pledgor + England & Wales)

**What the point actually is.** It is not an FCA (regulator) point at all — it is the
**FCARs** point, and the flag id risks being misread. Regulation 3 of the Financial Collateral
Arrangements (No. 2) Regulations 2003 defines both a *security* financial collateral arrangement and a
*title transfer* financial collateral arrangement so that **both parties must be non-natural
persons**, a non-natural person being any corporate body, unincorporated firm, partnership or body
with legal personality **except an individual** (including entities formed under foreign or
international law). So where the collateral **provider** is an individual — the classic private-wealth
case, and equally the classic third-party spouse or family pledgor — the arrangement is not a
financial collateral arrangement and none of the FCAR machinery is available: no appropriation without
a court order (reg 17), no commercially-reasonable-valuation appropriation framework (reg 18), no
disapplication of insolvency restrictions on enforcement (regs 8 and 10), no statutory close-out
netting protection (reg 12), no registration exemption (reg 4 — academic for an individual, who has no
registrable charge anyway).

**Why the flag should say "uncertain" rather than "unavailable".** Three reasons, all of which are
deal facts the tool holds: (a) the test is on the **parties to the collateral arrangement**, so an
individual *borrower* with a corporate or trustee-company *pledgor* can still be inside the regime;
(b) a trust structure may have a corporate trustee, which is a non-natural person; (c) even with two
non-natural persons, the arrangement still has to satisfy **possession or control**, which the English
courts read as requiring real dispossession of the provider ([2010] EWHC 1772 (Ch); [2012] EWHC 2997 (Ch)). So the honest output is: *safe-harbour availability is
fact-dependent and must be confirmed, and the drafting must not assume appropriation.*

**Suggested flag text (paraphrase, lender-side):** "Collateral provider is an individual and the
collateral is governed by English law. The Financial Collateral Arrangements (No. 2) Regulations 2003
require both parties to a financial collateral arrangement to be non-natural persons, so the statutory
appropriation right and the insolvency disapplications may not be available. Do not rely on
appropriation in the enforcement clause; rely on an express power of sale with LPA 1925 s.103
disapplied, and confirm the analysis with counsel." `who_decides`: senior lawyer.

**What the lender does instead.** Express contractual power of sale; contract out of LPA 1925 s.103;
retain the equitable duty to take reasonable care to obtain a proper price and evidence it with a
documented valuation and sale process; and note that on personal bankruptcy IA 1986 s.285(4) preserves
the secured creditor's enforcement rights, so the loss is the self-help package, not the security.

Sources:
- ref: "FCARs reg 3 (current)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/regulation/3"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Both parties to a security FCA and to a title transfer FCA must be non-natural persons; non-natural person excludes an individual."
- ref: "FCARs regs 4, 8, 17, 18 (as made / current)"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2003/3226/contents/made"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "The benefits that are lost: registration exemption, insolvency disapplications, appropriation without court order, valuation duty."
- ref: "UK-FCL-BRIEF-01: law-firm briefing on financial collateral possession and control (Nov 2012)"
  type: law_firm_briefing
  url: "https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2012/11/financial-collateral-remains-a-gray-area.pdf"
  retrieved: 2026-09-21
  reliability: C
  verified: true
  note: "Possession/control requires dispossession of the provider; source of the two case citations."
- ref: "Insolvency Act 1986 s.285"
  type: primary_law
  url: "https://www.legislation.gov.uk/ukpga/1986/45/section/285"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "s.285(4) preserves secured creditors' enforcement rights on personal bankruptcy."

### R14 — `bank_secrecy_data` (Swiss booking centre)

**What the point actually is.** Two overlapping duties, one criminal and one data-protection.
(1) **Banking Act (SR 952.0) Art. 47** makes it a criminal offence, punishable by up to three years'
imprisonment or a monetary penalty, intentionally to disclose a secret entrusted to a person in their
capacity as a body member, employee, agent or liquidator of a bank (or of a person under Art. 1b), or
perceived in that capacity; to attempt to induce such a breach; or, for a recipient, to pass on or
exploit a secret disclosed to them that way. The penalty rises to up to five years where the offender
obtains a pecuniary advantage; negligent breach is punishable by a fine of up to CHF 250,000; the duty
**survives** the end of the employment or professional relationship; and federal and cantonal
provisions on the duty to testify and to inform an authority are reserved. (2) **Federal Act on Data
Protection (SR 235.1) Arts 16-17**: personal data may be disclosed abroad only where the Federal
Council has found the destination adequate, or where adequacy is guaranteed by a treaty, by
contractual data protection clauses notified to the FDPIC beforehand, by specific guarantees notified
by the competent federal body, by FDPIC-approved standard clauses, or by approved binding corporate
rules; Art. 17 then provides exceptions, including explicit consent, disclosure directly connected with
the conclusion or performance of a contract with the data subject, and disclosure necessary to
establish, exercise or enforce legal rights before a court or competent foreign authority.

**Why it fires on a Lombard deal.** Any of: a non-Swiss custodian holding part of the collateral; a
non-Swiss guarantor, pledgor or their counsel; a credit committee, servicing function or group
function outside Switzerland; an enforcement sale routed through a foreign broker; a foreign court or
arbitral tribunal under the governing-law/jurisdiction clause; or a foreign counsel opinion on the
security. Severity is properly **low** for the flag itself — this is a routine, solvable issue — but
it is not a no-op, because the criminal duty is not cured by a data-protection consent alone.

**Suggested flag text (paraphrase, lender-side):** "Swiss booking centre. Client information is
protected by Banking Act Art. 47 and personal data transfers abroad are restricted by FADP Arts 16-17.
Confirm the disclosure route before sharing client information with any non-Swiss custodian, adviser,
committee, court or purchaser, and take an express client consent and waiver in the facility and
security documents." `who_decides`: legal + compliance (Swiss booking centre).

Sources:
- ref: "Swiss Banking Act (SR 952.0) Art. 47"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/51/117_121_129/20240101/de/pdf-a/fedlex-data-admin-ch-eli-cc-51-117_121_129-20240101-de-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "German official text (no English PDF located at this ELI). Art. 47(1) intentional disclosure, inducement and onward disclosure/exploitation; (1bis) up to five years where a pecuniary advantage is obtained; (2) negligence, fine up to CHF 250,000; (4) duty survives the end of the relationship; (5) duties to testify or inform an authority reserved."
- ref: "Swiss FADP (SR 235.1) Arts 16, 17"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20230901/en/pdf-a/fedlex-data-admin-ch-eli-cc-2022-491-20230901-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 16 adequacy decision or listed safeguards for disclosure abroad; Art. 17 exceptions including explicit consent, contract performance, and establishing or enforcing legal rights before a foreign court or authority."

---

## Consumer credit inputs for WP8

### United Kingdom — the exemption logic in plain English

Since 1 April 2014, consumer credit regulation sits in FSMA and the **Financial Services and Markets
Act 2000 (Regulated Activities) Order 2001** ("RAO"), not in the Consumer Credit Act 1974 exemptions:
CCA 1974 s.16B was **omitted** with effect from 1 April 2014 (26 July 2013 for specified purposes).
Two exemptions matter for private-wealth lending, and both work the same way — an objective test plus
a prescribed **declaration** by the borrower that shifts the evidential burden.

**1. Business purpose (RAO art. 60C).** An agreement is exempt if the lender provides credit
**exceeding £25,000** and the borrower enters into it **wholly or predominantly** for the purposes of
a business carried on, or intended to be carried on, by the borrower. (For credit of £25,000 or less
there is only a narrow green-deal route requiring a **wholly** business purpose.) Where the agreement
includes a declaration in the FCA-prescribed form, the agreement is **presumed** to be for business
purposes **unless** the lender, or anyone acting on its behalf, **knows or has reasonable cause to
suspect** otherwise. That "reasonable cause to suspect" carve-out is the live risk: a relationship
manager's file note describing a personal purpose defeats the declaration.

**2. High net worth (RAO art. 60H).** An agreement is exempt if the borrower is an **individual**,
the agreement is secured on land **or** is for credit **exceeding £60,260** for a purpose other than
renovating residential property, the borrower makes a prescribed **declaration** agreeing to forgo the
protections of a regulated credit agreement, a **statement of high net worth** relating to the
borrower's income or assets has been made in compliance with FCA rules, the statement is connected to
the agreement in accordance with FCA rules, and a copy of the statement is given to the lender before
the agreement is made. The FCA thresholds are in **CONC App 1.4**: net income of at least **£150,000**
in the previous financial year, **or** net assets of at least **£500,000** throughout that year,
excluding the borrower's primary residence, rights under a contract of insurance and pension benefits.
The statement must be signed by the lender/owner or by a qualified accountant from the listed bodies,
and where the person making it is an employee, agent or associate of the lender, the lender must be
authorised to accept deposits. The borrower's declaration must be in the agreement, no less prominent
than the other information and clearly distinguishable, signed by the borrower, confirm receipt of the
statement, state that the borrower is giving up consumer credit protections, note that the court
retains powers in relation to unfair relationships, and recommend independent legal advice.

**Intake facts the tool should capture (not the conclusion).** Borrower is a natural person; borrower
domicile/residence; facility amount and currency; declared business purpose (yes/no) and whether a
compliant declaration is in the agreement; declared high net worth (yes/no) and whether a compliant
statement exists and was given to the lender before execution; and anything on file suggesting a
personal purpose. The **final determination that the borrower is or is not a consumer stays on the
not-automated register**.

`[VERIFY]` items for this section: (a) whether **CCA 1974 s.16A** (the high net worth exemption under
the old Act) is likewise omitted — I confirmed only s.16B; (b) whether the CCA 1974 **unfair
relationship** powers in ss.140A-140C continue to apply to an exempt agreement — the CONC App 1.4
declaration wording refers to the court's unfair-relationship powers, which strongly implies they do,
but I did not read s.140A; (c) whether either monetary figure has been amended after the version I
read.

Sources:
- ref: "RAO 2001 art. 60C"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2001/544/article/60C"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 60C(3) credit exceeding £25,000 and a wholly or predominantly business purpose; 60C(4) the £25,000-or-less green deal route requiring a wholly business purpose; 60C(5)-(6) the declaration and the presumption defeated by knowledge or reasonable cause to suspect."
- ref: "RAO 2001 art. 60H"
  type: primary_law
  url: "https://www.legislation.gov.uk/uksi/2001/544/article/60H"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "High net worth exemption: individual borrower; secured on land or credit exceeding £60,260 other than for residential renovation; borrower declaration forgoing protections; statement of high net worth complying with FCA rules, connected per FCA rules, copy to the lender before the agreement is made."
- ref: "FCA Handbook CONC App 1.4"
  type: regulator
  url: "https://www.handbook.fca.org.uk/handbook/CONC/App/1/4.html"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Net income at least £150,000 in the previous financial year or net assets at least £500,000 throughout it, excluding primary residence, insurance contract rights and pension benefits; who may sign the statement; required content and prominence of the borrower's declaration."
- ref: "CCA 1974 s.16B (omitted)"
  type: primary_law
  url: "https://www.legislation.gov.uk/ukpga/1974/39/section/16B"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Section omitted 26 July 2013 for specified purposes and 1 April 2014 otherwise, by the FSMA 2000 (Regulated Activities) (Amendment) (No. 2) Order 2013 — confirming the exemption logic now lives in the RAO."

### Switzerland — Consumer Credit Act (KKG, SR 221.214.1) scope exclusions

A **consumer** is a natural person entering a consumer credit contract for a purpose that cannot be
attributed to their professional or commercial activity (Art. 3); a **consumer credit contract** is one
granting or promising credit as deferred payment, a loan or a similar financing assistance (Art. 1);
a **lender** is any natural or legal person granting consumer credit on a commercial basis (Art. 2).
For a Lombard loan the KKG normally drops out **twice over** under Art. 7(1):

- **Art. 7(1)(b)** — the Act does not apply to credit agreements or credit promises that are covered
  by **deposited customary bank collateral** (*hinterlegte bankübliche Sicherheiten*) or by
  **sufficient assets which the consumer holds with the lender**. A pledged portfolio held with the
  lending bank is exactly this case. This is the single most important exclusion for the product.
- **Art. 7(1)(e)** — the Act does not apply to contracts for credit of **less than CHF 500 or more
  than CHF 80,000**, aggregating consumer credits arranged in a coordinated way for the same consumer.
  Art. 7(2) lets the Federal Council adjust these figures.

Also excluded: credit directly or indirectly secured by a **real estate charge** (Art. 7(1)(a));
interest- and fee-free credit (c); credit with no interest charged where the consumer agrees to repay
in one instalment (d); credit repayable within at most **three months** (f); and continuing
supply-of-services contracts with instalment payment (g).

**Intake facts to capture:** whether the pledged portfolio is held **with the lender** (this alone
usually disapplies the KKG), the total facility amount in CHF equivalent, whether the borrower is a
natural person acting outside a professional or commercial activity, and whether any real estate
charge is in the structure.

Sources:
- ref: "Swiss Consumer Credit Act (KKG, SR 221.214.1) Arts 1, 2, 3, 7"
  type: primary_law
  url: "https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2002/593/20230901/de/pdf-a/fedlex-data-admin-ch-eli-cc-2002-593-20230901-de-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "German official text (status 1 September 2023). Art. 3 consumer as a natural person acting outside professional or commercial activity; Art. 7(1)(a)-(g) exclusions, with (b) deposited customary bank collateral or sufficient assets held with the lender and (e) below CHF 500 or above CHF 80,000; Art. 7(2) Federal Council power to adjust."

### Luxembourg — consumer credit

The consumer credit chapter of the **Code de la consommation** (Arts L.224-1 ff) sets out its
exclusions in **Art. L.224-3(1)**, and three of them matter here:

- **L.224-3(1)(c)** — the chapter does **not** apply to credit agreements where the total amount of
  credit is **below EUR 200 or above EUR 75,000**. (Art. L.224-3(5) adds an exception: it does apply
  to **unsecured** credit above EUR 75,000 intended to fund the renovation of residential property.)
- **L.224-3(1)(h)** — the chapter does **not** apply to credit agreements concluded with an
  investment firm or a credit institution **to allow an investor to carry out a transaction in one or
  more of the instruments listed in Section C of Annex I to the markets-in-financial-instruments
  directive**, where the lender is involved in that transaction. This is a direct margin/Lombard
  carve-out and is the cleanest basis for a purpose-to-invest facility. Note the consolidated text
  still cross-refers to Directive **2004/39/EC** (the pre-MiFID II directive) — read across to MiFID
  II Annex I Section C. `[VERIFY]` that cross-reference has been updated.
- **L.224-3(1)(a)** — credit secured by a mortgage or comparable security over immovable property, or
  by a right relating to immovable property, is excluded; and **(k)** excludes pawn-type contracts
  where the consumer must hand a good into the lender's possession as security and the consumer's
  liability is strictly limited to that pledged good.

`[VERIFY]`: the effect of Directive (EU) 2023/2225 (the new Consumer Credit Directive) on these
thresholds and exclusions once transposed in Luxembourg — not researched in this work package.

Sources:
- ref: "Luxembourg Code de la consommation, Art. L.224-3 (consolidated version 31 December 2024)"
  type: primary_law
  url: "https://legilux.public.lu/eli/etat/leg/code/consommation/20241231"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Read from the Legilux consolidated PDF at https://legilux.public.lu/filestore/eli/etat/leg/code/consommation/20241231/fr/pdf/eli-etat-leg-code-consommation-20241231-fr-pdf.pdf. Art. L.224-3(1)(a), (c), (h), (k) and L.224-3(5) as described."

### MiFID II / FinSA suitability on leverage

In the UK and EU, lending to an investor so they can carry out a transaction in financial instruments
is an **ancillary service** under MiFID II, and where the bank also advises or manages, the suitability
obligation bites on the **whole arrangement**: FCA COBS 9A.2.1R requires a personal recommendation to
be suitable and in accordance with the client's **risk tolerance and ability to bear losses**;
COBS 9A.2.7R requires information on the source and extent of regular income, assets including liquid
assets, investments and real property, and regular financial commitments; COBS 9A.2.8R requires the
holding period, risk preferences, risk profile and the purpose of the investment; and COBS 9A.2.17G
tells a firm to consider the suitability of the **overall transaction** where an instrument is linked
directly or indirectly to any form of loan or mortgage. In Switzerland, FinSA Art. 3(c)(5) makes the
**granting of loans to finance transactions with financial instruments** a financial service in its own
right, Art. 10 requires an appropriateness or suitability review where investment advice or portfolio
management is provided, Art. 12 requires enquiry into the client's financial situation and investment
objectives as well as knowledge and experience where advice takes the portfolio into account, Art. 13
exempts pure execution/transmission subject to notifying the client, and Art. 14 requires the firm to
**advise the client against** an instrument it thinks unsuitable. The practical consequence for the
playbook: a facility whose declared purpose is to acquire securities pulls the bank into the suitability
perimeter in both regimes, so the no-advice / non-reliance clause has to be consistent with what the
relationship manager actually did, and the leverage must be assessed together with the investment, not
separately.

Sources:
- ref: "FCA Handbook COBS 9A.2"
  type: regulator
  url: "https://www.handbook.fca.org.uk/handbook/COBS/9A/2.html"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "COBS 9A.2.1R suitability including risk tolerance and ability to bear losses; 9A.2.7R financial situation information; 9A.2.8R investment objectives; 9A.2.17G suitability of the overall transaction where the instrument is linked directly or indirectly to a loan, mortgage or home reversion plan."
- ref: "FinSA (SR 950.1) Arts 3(c), 10, 11, 12, 13, 14"
  type: primary_law
  url: "https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2019/758/20240301/en/pdf-a/fedlex-data-admin-ch-eli-cc-2019-758-20240301-en-pdf-a.pdf"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 3(c)(5) loans to finance transactions with financial instruments are a financial service; Arts 10-14 the appropriateness and suitability duties, the execution-only exemption and the duty to advise against an unsuitable instrument."
- ref: "[VERIFY] MiFID II Directive 2014/65/EU Art. 25(2) and Annex I Section B(2)"
  type: primary_law
  url: "https://eur-lex.europa.eu/eli/dir/2014/65/oj/eng"
  retrieved: 2026-09-21
  reliability: A
  verified: false
  note: "EUR-Lex fetch did not return usable article text; the summary returned only restated the question. The UK-side points above are instead sourced to the FCA Handbook, which I did read. Confirm the Annex I Section B(2) ancillary-service wording and the Art. 25(2) suitability wording against EUR-Lex before this leaves draft."

### UK Market Abuse Regulation Article 19 — PDMR pledges and closed periods

Article 19 of the Market Abuse Regulation (Regulation (EU) 596/2014, as retained in UK law) does two
things that matter to a securities-backed facility. **Notification**: persons discharging managerial
responsibilities and persons closely associated with them must notify the issuer and the competent
authority of transactions conducted on their own account relating to the issuer's shares or debt
instruments, or to derivatives or other linked financial instruments, **promptly and no later than
three working days** after the transaction, once the aggregate of their transactions in a calendar year
reaches **EUR 5,000** (the competent authority may raise the threshold to EUR 20,000). Article 19(7)
expressly brings **the pledging or lending of financial instruments** by or on behalf of a PDMR or
closely associated person within the notifiable transactions — but with a carve-out that is the
practically important bit for a private bank: a pledge or similar security interest given in connection
with **depositing the instruments in a custody account** does not have to be notified **unless and
until it is designated to secure a specific credit facility**. **Closed periods**: Article 19(11)
prohibits a PDMR from conducting transactions on their own account or for the account of a third party
relating to the issuer's shares, debt instruments or linked derivatives during a **closed period of 30
calendar days before the announcement of an interim financial report or a year-end report**, subject to
the limited exceptions in Article 19(12).

**Lender-side translation.** The act of designating an existing custody pledge to secure a named
facility is itself the notifiable event, so the timing of the security documents drives the client's
notification clock. The Article 19(11) prohibition is addressed to the PDMR's own dealing, not in terms
to the secured creditor's enforcement, but an enforcement sale in a closed period, or while the client
holds inside information, is a live market-abuse and reputational problem for both sides. Playbook
consequences: a condition precedent requiring compliance sign-off on insider status and any issuer
consent or lock-up; a representation that the pledgor is not in possession of inside information and
will notify the lender on becoming subject to a closed period; and an enforcement clause that preserves
the lender's discretion while flagging the need for compliance input before a sale.
`[VERIFY]`: the exact retained-UK monetary threshold figure (the page I read gives EUR 5,000 /
EUR 20,000) and whether the FCA has exercised the uplift.

Sources:
- ref: "Market Abuse Regulation (EU) 596/2014 Art. 19 (retained UK law)"
  type: primary_law
  url: "https://www.legislation.gov.uk/eur/2014/596/article/19"
  retrieved: 2026-09-21
  reliability: A
  verified: true
  note: "Art. 19(1) notification of PDMR and closely associated persons' own-account transactions, promptly and no later than three working days; 19(8)-(9) EUR 5,000 threshold, uplift to EUR 20,000; 19(7) pledging and lending are notifiable, with the custody-account pledge carve-out until designated to secure a specific credit facility; 19(11) 30-calendar-day closed period before interim and year-end reports, with 19(12) exceptions."

---

## Source register rows

Rows for appending to `docs/source_register.md`. Every source appears once.

| ref | type | url | retrieved | reliability | verified | note |
|---|---|---|---|---|---|---|
| FCARs 2003 (SI 2003/3226) reg 3 (current) | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/regulation/3 | 2026-09-21 | A | true | Definitions: security/title transfer FCA, both parties must be non-natural persons, possession including substitution and excess-withdrawal rights, financial collateral, security interest. |
| FCARs 2003 reg 4 (current) | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/regulation/4 | 2026-09-21 | A | true | Reg 4(4) disapplies CA 2006 ss.859A and 859H for a security FCA and charges under it (section references substituted from 6 April 2013). |
| FCARs 2003 table of contents (as made) | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/contents/made | 2026-09-21 | A | true | Structure of the Regulations: formalities, insolvency modifications, right of use and appropriation, conflict of laws. |
| FCARs 2003 reg 8 (as made) | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/regulation/8/made | 2026-09-21 | A | true | Insolvency Act 1986 provisions restricting enforcement of security disapplied for FCAs (Sch B1 paras 43(2), 44, 70, 71, 41(2); ss.10, 11, 15; Sch A1 moratorium). |
| FCARs 2003 reg 17 (as made) | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/regulation/17/made | 2026-09-21 | A | true | Appropriation under an express power without any court order for foreclosure. |
| FCARs 2003 reg 18 (as made) | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/regulation/18/made | 2026-09-21 | A | true | Duty to value per the arrangement and in any event in a commercially reasonable manner; account for the difference. |
| FCARs 2003 reg 19 (as made) | primary_law | https://www.legislation.gov.uk/uksi/2003/3226/regulation/19/made | 2026-09-21 | A | true | PRIMA rule for book entry securities collateral: domestic law of the country where the relevant account is maintained; five matters governed. |
| Companies Act 2006 s.859A | primary_law | https://www.legislation.gov.uk/ukpga/2006/46/section/859A | 2026-09-21 | A | true | Registrable company charges; 21 days from the day after creation; delivery by the company or any person interested; s.859H voidness consequence. |
| Law of Property Act 1925 s.101 | primary_law | https://www.legislation.gov.uk/ukpga/Geo5/15-16/20/section/101 | 2026-09-21 | A | true | Mortgagee's statutory powers where the mortgage is by deed; sale and receiver powers arise once the mortgage money is due. |
| Law of Property Act 1925 s.103 | primary_law | https://www.legislation.gov.uk/ukpga/Geo5/15-16/20/section/103 | 2026-09-21 | A | true | Three alternative pre-conditions to exercising the s.101 power of sale; routinely contracted out of. |
| Insolvency Act 1986 s.285 | primary_law | https://www.legislation.gov.uk/ukpga/1986/45/section/285 | 2026-09-21 | A | true | Restrictions on creditors' remedies on personal bankruptcy; s.285(4) preserves secured creditors' enforcement rights. |
| Consumer Credit Act 1974 s.16B (omitted) | primary_law | https://www.legislation.gov.uk/ukpga/1974/39/section/16B | 2026-09-21 | A | true | Business-purpose exemption omitted with effect from 1 April 2014; the exemption logic now lives in the RAO. |
| FSMA 2000 (Regulated Activities) Order 2001 art. 60C | primary_law | https://www.legislation.gov.uk/uksi/2001/544/article/60C | 2026-09-21 | A | true | Business-purpose exemption: credit exceeding GBP 25,000, wholly or predominantly business purpose, prescribed declaration and the presumption defeated by knowledge or reasonable cause to suspect. |
| FSMA 2000 (Regulated Activities) Order 2001 art. 60H | primary_law | https://www.legislation.gov.uk/uksi/2001/544/article/60H | 2026-09-21 | A | true | High net worth exemption: individual borrower, secured on land or credit exceeding GBP 60,260, borrower declaration, statement of high net worth per FCA rules, copy to lender before execution. |
| FCA Handbook CONC App 1.4 | regulator | https://www.handbook.fca.org.uk/handbook/CONC/App/1/4.html | 2026-09-21 | A | true | High net worth thresholds: net income at least GBP 150,000 or net assets at least GBP 500,000 (excluding primary residence, insurance rights, pensions); who signs; declaration content and prominence. |
| FCA Handbook COBS 9A.2 | regulator | https://www.handbook.fca.org.uk/handbook/COBS/9A/2.html | 2026-09-21 | A | true | Suitability: risk tolerance and ability to bear losses; financial situation and investment objectives information; 9A.2.17G suitability of the overall transaction for loan-linked instruments. |
| Market Abuse Regulation (EU) 596/2014 Art. 19 (retained UK law) | primary_law | https://www.legislation.gov.uk/eur/2014/596/article/19 | 2026-09-21 | A | true | PDMR notification within three working days above the EUR 5,000 threshold; pledging and lending notifiable; custody-pledge carve-out until designated to secure a specific facility; 30-day closed period. |
| UK-FCL-BRIEF-01: law-firm briefing on financial collateral possession and control (Nov 2012) | law_firm_briefing | https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2012/11/financial-collateral-remains-a-gray-area.pdf | 2026-09-21 | C | true | Possession and control require more than mere custody; dispossession is key; source of the citations for [2010] EWHC 1772 (Ch) and [2012] EWHC 2997 (Ch). |
| Swiss FISA / BEG (SR 957.1), official English translation | primary_law | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/450/20230101/en/pdf-a/fedlex-data-admin-ch-eli-cc-2009-450-20230101-en-pdf-a.pdf | 2026-09-21 | A | true | Arts 2, 4, 5(d), 21-26, 30, 31, 32: scope, custodians, qualified investor, custodian rights, creation by credit / control agreement / agreement with the custodian, priorities, realisation and notice. |
| Swiss Civil Code (SR 210), official English translation | primary_law | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/24/233_245_233/20260101/en/pdf-a/fedlex-data-admin-ch-eli-cc-24-233_245_233-20260101-en-pdf-a.pdf | 2026-09-21 | A | true | Arts 884, 891, 894, 899, 900, 901: pledge of chattels by transfer of possession, satisfaction from proceeds, invalidity of forfeiture agreements, pledge of claims and rights in writing, and Art. 901(3) routing intermediated securities to FISA. |
| Swiss PILA / IPRG (SR 291), official English translation | primary_law | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1988/1776_1776_1776/20260101/en/pdf-a/fedlex-data-admin-ch-eli-cc-1988-1776_1776_1776-20260101-en-pdf-a.pdf | 2026-09-21 | A | true | Art. 105 choice of law for pledges of claims and securities and the pledgee's-habitual-residence default; Arts 108a-108d intermediated securities, jurisdiction, and the Hague Convention as the applicable-law rule. |
| Swiss DEBA / SchKG (SR 281.1), official English translation | primary_law | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/11/529_488_529/20260101/en/pdf-a/fedlex-data-admin-ch-eli-cc-11-529_488_529-20260101-en-pdf-a.pdf | 2026-09-21 | A | true | Art. 41 pledge-realisation proceedings and the debtor's right to require the pledge be realised first; Art. 198 pledged assets in the bankruptcy estate; Art. 219(1) pledge-secured claims paid in advance from the proceeds. |
| Swiss Banking Act (SR 952.0), German official text | primary_law | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/51/117_121_129/20240101/de/pdf-a/fedlex-data-admin-ch-eli-cc-51-117_121_129-20240101-de-pdf-a.pdf | 2026-09-21 | A | true | Art. 47 banking secrecy: intentional disclosure, inducement and onward disclosure; up to three years, five where a pecuniary advantage is obtained; negligence fine up to CHF 250,000; duty survives the relationship. No English PDF located at this ELI. |
| Swiss FADP (SR 235.1), official English translation | primary_law | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20230901/en/pdf-a/fedlex-data-admin-ch-eli-cc-2022-491-20230901-en-pdf-a.pdf | 2026-09-21 | A | true | Arts 16-17: adequacy decision or listed safeguards for cross-border disclosure of personal data, and the exceptions including consent, contract performance and enforcement of legal rights abroad. |
| Swiss FinSA / FIDLEG (SR 950.1), official English translation | primary_law | https://fedlex.data.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2019/758/20240301/en/pdf-a/fedlex-data-admin-ch-eli-cc-2019-758-20240301-en-pdf-a.pdf | 2026-09-21 | A | true | Art. 3(c)(5) granting loans to finance transactions in financial instruments is a financial service; Arts 10-14 appropriateness and suitability duties, execution-only exemption, duty to advise against. |
| Swiss Consumer Credit Act (KKG, SR 221.214.1), German official text | primary_law | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2002/593/20230901/de/pdf-a/fedlex-data-admin-ch-eli-cc-2002-593-20230901-de-pdf-a.pdf | 2026-09-21 | A | true | Arts 1, 2, 3 and 7: consumer as natural person outside professional activity; Art. 7(1)(b) exclusion for credit covered by deposited customary bank collateral or sufficient assets held with the lender; Art. 7(1)(e) below CHF 500 or above CHF 80,000. |
| HCCH status table, Convention #36 (2006 Securities Convention) | primary_law | https://www.hcch.net/en/instruments/conventions/status-table/?cid=72 | 2026-09-21 | A | true | Contracting parties Mauritius (15-X-2009), Switzerland (14-IX-2009), USA (15-XII-2016); entry into force 1-IV-2017; UK, Luxembourg and the EU are not parties. |
| HCCH 2006 Securities Convention, full text (Arts 2, 4, 5) | primary_law | https://www.hcch.net/en/instruments/conventions/full-text/?cid=72 | 2026-09-21 | A | true | Art. 2 issues governed; Art. 4(1) primary rule of the law expressly agreed in the account agreement subject to the qualifying office test; Art. 5 sequential fall-backs. |
| CH-PRACT-01: practitioner overview, lending and taking security in Switzerland (law stated 1 May 2025) | law_firm_briefing | https://www.baerkarrer.ch/userdata/lending-and-taking-security-in-switzerland-overview.pdf | 2026-09-21 | C | true | Pledge with account control agreement vs security transfer of title; private enforcement must be documented to obtain the best price; effect of bankruptcy on private enforcement of pledges; title-transferred assets stay outside the estate. |
| Luxembourg Law of 5 August 2005 on financial collateral arrangements, CSSF consolidated text updated 15 July 2024 | primary_law | https://www.cssf.lu/wp-content/uploads/L_050805_fin_coll_upd_15072024.pdf | 2026-09-21 | A | true | Arts 1-5, 10-13, 20, 21, 23, 24, 26: definitions, merchant or non-merchant, provision and possession routes, all-assets pledge, right of use, enforcement without prior notice, insolvency remoteness with the over-indebtedness carve-out, PRIMA rule, no registration formalities. CSSF consolidation, authoritative text is the Journal officiel version. |
| Luxembourg Code de la consommation, consolidated version 31 December 2024 | primary_law | https://legilux.public.lu/eli/etat/leg/code/consommation/20241231 | 2026-09-21 | A | true | Art. L.224-3(1)(a), (c), (h), (k) and (5): consumer credit exclusions including below EUR 200 / above EUR 75,000, and credit from an investment firm or credit institution to let an investor carry out a transaction in MiFID Annex I Section C instruments. |
| LU-FCL-BRIEF-01: law-firm briefing on the Luxembourg financial collateral law (2022) | law_firm_briefing | https://www.addleshawgoddard.com/en/insights/insights-briefings/2022/finance/luxembourg-financial-collateral-law/ | 2026-09-21 | C | true | 2022 amendments: enforcement by sale on a trading venue (regulated market, MTF, OTF) and new enforcement route for pledged insurance contracts. Silent on natural persons, prior notice and insolvency remoteness. |
| [VERIFY] LU-NATPERS-01: promotional-body article on the Luxembourg collateral law and its beneficiaries | law_firm_briefing | https://www.luxembourgforfinance.com/portfolio/luxembourgs-collateral-law-particularly-favourable-to-beneficiaries/ | 2026-09-21 | C | false | URL seen in search results but not opened. Would corroborate that private individuals are in scope subject to the over-indebtedness carve-out. |
| [VERIFY] MiFID II Directive 2014/65/EU, Art. 25(2) and Annex I Section B(2) | primary_law | https://eur-lex.europa.eu/eli/dir/2014/65/oj/eng | 2026-09-21 | A | false | Fetch did not return usable article text. Needed to source the ancillary-service characterisation of lending for financial instrument transactions and the EU-side suitability wording. |
| [VERIFY] English law on independent legal advice for third-party (non-commercial) security | textbook |  | 2026-09-21 | C | false | Not researched in this work package. The undue-influence / independent-advice practice point must be sourced before promotion beyond draft. |
