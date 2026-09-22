# Hand-off: WP8 (regulatory flags)

Agent hand-off, 2026-09-21. Covers `build_plan.md` §6 WP8 and §4's flag list.

Everything in the repository is synthetic. Nothing here is legal advice. All ten flags are
`status: draft`; `reviewed_by` and `last_reviewed` are null throughout. A flag is a prompt to a
named human, not a conclusion.

---

## 1. Acceptance output (pasted verbatim)

```
$ .venv/Scripts/python -m sbl validate
OK: 24 clauses, 18 rules, 10 flags, 3 jurisdictions validated.
library_hash: 8aaa41bfe806aba151feaef9308c125d76881ffb2760ab665490e07875874ee8
validate exit=0
```

```
$ .venv/Scripts/python -m pytest tests/test_flags_jurisdictions.py -q
....................                                                     [100%]
20 passed in 2.26s
```

Plan acceptance for WP8 is "every flag referenced by a rule or clause exists; every flag has
`who_decides`". Both are asserted by tests in `tests/test_flags_jurisdictions.py`
(`test_every_flag_id_used_by_a_rule_exists`, `test_every_flag_id_used_by_a_clause_exists`,
`test_every_flag_has_a_non_empty_who_decides`). At the time of the run `rules.yaml` held 18 rules,
so the rule test ran for real rather than skipping.

Flags referenced by rules at the time of writing: `consumer_credit` (high where no declaration,
medium where declared), `fca_safe_harbour_uncertain` (medium), `financial_assistance_corporate_benefit`
(medium), `market_abuse` (high), `restricted_securities` (high), `mortgage_regulation` (high),
`mifid_suitability` (medium), `bank_secrecy_data` (low). Referenced by clauses: `prudential_awareness`
(eligible collateral, concentration, lender discretion), plus `restricted_securities`,
`market_abuse` and `consumer_credit`. `emir_awareness` is referenced by nothing and its
`trigger_summary` says so.

---

## 2. The naming issue on `fca_safe_harbour_uncertain` — managing-agent decision, implemented

The id reads as a point about the conduct regulator. It is not: it is about the **Financial
Collateral Arrangements (No. 2) Regulations 2003**, and "FCAR" is not "FCA". The research agent
raised this as a risk that the markup would mislead an interviewer.

The managing-agent decision was to keep the id for compatibility with the existing rules, outputs and
clause references, and to fix the problem in the two fields a reader actually sees. That is what is
in the file:

* `name` now reads **"Financial Collateral Arrangements Regulations (FCARs) safe harbour
  uncertain"**.
* `description` opens by saying, in terms, that the id is a legacy label kept for compatibility, that
  it is misleading, that this is not a point about the conduct regulator, and that the regime is the
  FCARs 2003.

`who_decides` is `senior lawyer`, as the research suggests, because the question is whether the
statutory self-help package is available on these facts and what the enforcement clause should say
instead — a drafting and analysis call, not a compliance sign-off.

**If anyone is willing to take the rename**, `fcar_safe_harbour_uncertain` would be better, and the
change is mechanical: the flag id here, the `flag:` value in `R04_natural_person_pledgor_england`,
and any clause `regulatory_flags` entry. It was not done unilaterally because three other agents were
writing those files at the same time.

---

## 3. What was written

`playbook/flags/regulatory_flags.yaml`, overwritten, the same ten ids in the same order. Each flag
has `name`, `description` (lender-side, what the risk actually is), `trigger_summary` (plain English,
aligned with §4), `who_decides`, `sources` (structured, same shape as clauses) and `status: draft`.

| id | who_decides | sources | verified sources |
|---|---|---|---|
| consumer_credit | senior lawyer + compliance | 6 | 6 |
| mortgage_regulation | senior lawyer + compliance | 3 | 3 |
| mifid_suitability | compliance | 3 | 2 |
| market_abuse | senior lawyer + compliance | 1 | 1 |
| restricted_securities | compliance, with head of credit on lending value | 2 | 2 |
| fca_safe_harbour_uncertain | senior lawyer | 4 | 4 |
| financial_assistance_corporate_benefit | senior lawyer + local counsel | 3 | 2 |
| bank_secrecy_data | legal + compliance for the booking centre | 2 | 2 |
| prudential_awareness | not a deal-level decision; informational | 1 | 1 |
| emir_awareness | not a deal-level decision; informational | 1 | 1 |

Five sources were opened by this agent rather than lifted from the research, for the four flags the
research did not cover: the Regulated Activities Order article on regulated mortgage contracts;
Companies Act 2006 ss.678 and 172; the retained capital requirements regulation article on eligible
financial collateral; and the retained EMIR article on risk mitigation for uncleared OTC derivatives.
Rule 144 was read at a university reproduction of the regulation because the official code reader
redirected to a block page, and it is graded **C** for that reason with the reason stated in the
source note. All are in `docs/source_register.md`.

`WP1.md` §5 item 7 flagged that `who_decides` is a free string and that WP8 should propose an
approver vocabulary if the strings drift. They have: the file now uses five distinct values plus two
"informational" strings. A suggested closed list, if Stuart wants one:
`deal lawyer`, `senior lawyer`, `compliance`, `senior lawyer + compliance`, `head of credit`,
`local counsel`, `informational`. That would need an enum in `models.py` and is a post-freeze schema
change, so it was not done here.

---

## 4. Every `[VERIFY]` in the flags file

| flag | field | the statement carrying `[VERIFY]` |
|---|---|---|
| consumer_credit | `description` | Whether any of the four UK figures (GBP 25,000; GBP 60,260; GBP 150,000; GBP 500,000) has been amended since the versions read on 2026-09-21; whether the 1974 Act's own high net worth exemption is likewise omitted (only s.16B was confirmed omitted); and whether the unfair relationship powers continue to apply to an exempt agreement. |
| consumer_credit | `description` | The Luxembourg consolidated consumption code still cross-refers to the pre-MiFID II directive in the margin-lending carve-out, read across but not confirmed; and the effect of the 2023 consumer credit directive on the EUR 200 / EUR 75,000 bounds once transposed was not researched. |
| mifid_suitability | `description` and `sources` | The EU-side characterisation of such lending as an ancillary service and the EU-side suitability wording are unsourced: the directive fetch returned no usable article text, so it is recorded with `url` and `verified: false`. The UK points are sourced to the regulator's handbook, which was read. |
| market_abuse | `description` | The exact retained-UK monetary threshold figure (the text read gives EUR 5,000 with a permitted uplift to EUR 20,000) and whether the regulator has exercised the uplift. |
| financial_assistance_corporate_benefit | `sources` | The Swiss and Luxembourg equivalents of the financial assistance and corporate benefit restrictions were not researched; the description's statement that equivalent restrictions exist elsewhere is unsourced, recorded with `url: null` and `verified: false`. |
| prudential_awareness | `description` | Nothing in this library computes a capital number; no institution's own approach, permissions, haircuts or internal model was considered; no statement is a capital conclusion. |
| emir_awareness | `description` | The intake captures no facts about derivative overlays at all, the clearing thresholds and client-classification analysis were not researched, and no regime other than the retained UK one was looked at. |

Note that `consumer_credit`'s Swiss thresholds (CHF 500 / CHF 80,000) and the collateral exclusion
are **not** `[VERIFY]`: the German official text was read in the research and the article is cited.
The same is true of the Luxembourg EUR 200 / EUR 75,000 bounds.

---

## 5. Three lowest-confidence statements in the flags file

1. **`financial_assistance_corporate_benefit`: "equivalent restrictions exist in other jurisdictions
   and must be checked locally".** The English law in the description is sourced at grade A and was
   read, but the cross-border half is a practitioner's generalisation with no primary text behind it.
   Upstream security and corporate benefit constraints in Switzerland and Luxembourg are real and are
   routinely the reason a third-party corporate pledge gets restructured, but this agent did not open
   a single article on either. Highest priority in WP8 for review.
2. **`restricted_securities`: the whole description is built on a US rule.** The playbook's three
   jurisdictions are England, Switzerland and Luxembourg, and the holding period, volume cap,
   manner-of-sale and notice-filing conditions described are those of the US resale rule, because
   that is the regime most often behind an issuer-restricted line in a private-wealth portfolio. The
   description is written generically enough to be honest, but a reader could take it as a statement
   of English or Swiss law, which it is not. The source is also grade C, being a university
   reproduction rather than the official publisher. Either narrow the description to say it describes
   a US-listed restricted position, or add English and Swiss lock-up and consent material.
3. **`consumer_credit`: the UK exemption logic is stated confidently and the thresholds are the
   brittle part.** The four figures were read in the versions live on 2026-09-21 and are not
   independently monitored; the business-purpose presumption is also stated without the underlying
   evidential practice around "reasonable cause to suspect", which is where the exemption actually
   fails in a private bank. The flag says the final determination stays with a human, and it should
   stay that way.

Honourable mention, because it is a design risk rather than a legal one: **`prudential_awareness` and
`emir_awareness` never fire.** `prudential_awareness` is referenced by three clauses so it will print
where those clauses print; `emir_awareness` is referenced by nothing at all and will never appear in
any output. If it should appear, it needs either a clause reference or a rule, and the intake would
need a derivative-overlay fact to hang a rule on.

---

## 6. Test file

`tests/test_flags_jurisdictions.py` is shared between WP7 and WP8: 20 tests covering library load,
the three jurisdiction ids, flag ids used by rules and by clauses, the ten agreed flag ids,
non-empty `who_decides`, the seven jurisdiction fields answered and not left as the literal "stub",
at least one source per jurisdiction and per flag, no `reviewed` status anywhere in flags or
jurisdictions, and a denylist grep over `playbook/jurisdictions` and `playbook/flags`.

The denylist test strips `http\S+` before matching and matches on **word boundaries**,
case-insensitively. Word boundaries matter: without them, `ubs` trips on "substitution", `allen`
trips on "challenge" and `citi` trips on "citizen", all of which appear or could appear in ordinary
legal prose. With them, only the institution names themselves match.

The rule-reference test skips itself if `rules.yaml` is empty, so it cannot pass vacuously while
another agent is still writing that file. It did not skip on the run above.
