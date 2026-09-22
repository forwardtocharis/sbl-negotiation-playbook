# WP3 clause drafting brief (common to all four drafting groups)

Written for: the WP3 clause-drafting sub-agents. Read this, then build_plan.md (§0, §2.1, §2.2, §3, WP3), then handoff/WP1.md and docs/schema_notes.md (the frozen schema), then docs/glossary.md, then docs/research/clause_sources.md (the shared source pool: source table, per-clause map, observed ranges, counterparty asks). If docs/research/jurisdictions_research.md exists, use it for jurisdiction_notes.

## What you produce
For each clause id assigned to you, overwrite the stub file `playbook/clauses/NN_<id>.yaml` with a full `status: draft` entry per build_plan.md §2.1. Keep the existing `id`, file name and `category` unless you have a strong reason (state it in the hand-off). All fields populated:
- `title`, `document`, `risk_rating`, `lender_objective` (one sentence), `counterparty_asks` (>= 2 realistic pushes; the source pool has an "asks observed" section).
- `positions`: preferred / acceptable / fallback with draft clause language (paraphrased, lender-side, written as if in a facility letter or security agreement, "the Bank" / "the Borrower" / "the Pledgor" / "the Custodian" as defined terms; never "we"), plus `rationale` (2-4 sentences answering "why is this the lender's line", written to be said out loud), `conditions` (list; may be empty for preferred/acceptable), `approval` for fallback (a role such as "senior lawyer", "head of credit", "credit committee"). `unacceptable` is a description of what the lender will not accept, plus rationale; no conditions/approval.
- Judgement-call numbers (days, percentages, notice periods) are written as `X` in the clause text, with a YAML comment on the line above giving the observed range and the source refs, e.g. `# observed: 2-5 business days (EDGAR-ML-01, BANK-TERMS-03); Swiss practice <=2 days (SW-NOTE-01)`. Stuart fills the number on review.
- `default_floor`: normally `fallback`; use `acceptable` only where you can argue in the rationale that conceding to fallback should always require escalation.
- `escalation_triggers`, `depends_on` (only ids that exist in playbook/clauses/), `regulatory_flags` (only ids in playbook/flags/regulatory_flags.yaml), `not_automated` (>= 1 for high risk).
- `jurisdiction_notes`: keys england_wales, switzerland, luxembourg. Only where the clause genuinely varies; otherwise exactly "No jurisdiction-specific variation identified [VERIFY]".
- `sources`: >= 3 per clause, >= 1 of reliability A or B. Copy the structured entries from the source pool (ref label, type, url, retrieved, reliability, verified, note). `verified: true` only if the pool says the source was opened AND the note says it supports the statement you are making. You may search for and open new sources (load WebSearch/WebFetch via ToolSearch); if you add one, record it in `docs/research/source_register_<your group>.md` (a fragment file; do not edit docs/source_register.md, another agent merges later) with the same columns as docs/source_register.md.
- `status: draft`, `reviewed_by: null`, `last_reviewed: null`.

## Rules you cannot break (build_plan.md §0)
- Lender side. Synthetic only: no real bank, firm, client or party names anywhere, including comments and source ref labels (URLs may contain a publisher's domain; labels and notes must be neutral, e.g. "published Lombard terms of a Luxembourg bank").
- No invented law. If a legal or market statement has no opened source, prefix the sentence `[VERIFY]` and set `verified: false` on the source entry. Never fabricate a statute section, case name, accession number or URL.
- No verbatim lifting from filed agreements or bank terms: paraphrase structure; a short defined term or phrase is fine, a sentence is not.
- `status: draft` only. Never `reviewed`.
- Known gaps from the source pool that MUST be marked [VERIFY] if you state them: numeric single-name concentration caps; a lending-value grid by asset class; trustee power to borrow/charge and limited-recourse doctrine; Swiss governing-law/jurisdiction practice; consequences of the English FCAR natural-person exclusion; incapacity (short of death) treatment; MiFID II / FinSA primary text for suitability.

## Acceptance (run and paste into your hand-off)
1. `.venv/Scripts/python -m sbl validate` exits 0 (run from F:\SBL_Legal). If the WP5 agent is mid-edit and validate fails for a reason outside your files, say so and paste the error.
2. A small script (scratchpad, not repo) that loads each of your YAML files with pyyaml and asserts: status == draft; four tiers each with non-empty text and rationale; >= 3 sources, >= 1 with reliability A or B; >= 2 counterparty_asks; all three jurisdiction_notes keys present; depends_on ids exist as files; regulatory_flags ids exist in the flags file.
3. Denylist check, word-boundary aware and ignoring URL lines (publisher domains inside `url:` are permitted): `grep -v -i "url:" playbook/clauses/<your files> | grep -n -i -w -E "societe|generale|ubs|credit suisse|julius|pictet|lombard odier|barclays|hsbc|coutts|goldman|morgan|citi|citibank|edmond|vontobel|efg|bnp|deutsche"` and paste the (empty) output. Also confirm no party names from filed agreements appear.

## Hand-off
Final message and `handoff/WP3_<group>.md`: acceptance output; per clause the two positions you are least confident about (for Stuart's review priority); every [VERIFY] you introduced; any deviation from the schema or plan.
