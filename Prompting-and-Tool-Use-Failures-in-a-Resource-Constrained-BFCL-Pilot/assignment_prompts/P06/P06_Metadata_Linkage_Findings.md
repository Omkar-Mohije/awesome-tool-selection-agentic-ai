# P06 follow-up: metadata linkage validation (29 Oct 2026)
Status: **SOURCE-LEVEL VERIFIED; NOT ANNOTATED; NO BENCHMARK MODEL EXECUTED.**

Official MetaTool sources at commit `35e81bb7576826e980c80fed8f8c0a2b4a1e6fbb`:
- `dataset/plugin_des.json`: 199 benchmark tool IDs.
- `dataset/plugin_info.json`: 390 metadata records, 388 distinct `name_for_model` values.
- **153/199 benchmark tool IDs** match metadata exactly; **46/199 unmatched**.
- Duplicate metadata IDs: `web_scraper` and `SEO`. A first-match policy is appropriate ONLY for preliminary inspection; inspect duplicates for conflicts before scientific use.
- The earlier 50-query screening identified 21/50 records with rich metadata matches (record count, not distinct tool count).
- No full capability schemas or operational restrictions verified for every tool, and a match is not proof of a complete specification.

**Science gate:** source query + one short tool description are insufficient to assign `NO_VALID_TOOL` or `NEEDS_CLARIFICATION`. For such labels reviewers must receive a **defined inventory** and **documented capabilities/constraints for every candidate**. `not_documented` is not `unsupported`.

**Artifacts:** `P06_Rich_Metadata_Join_Colab.ipynb` creates joined 50-case and 199-tool CSVs plus a **blank, unannotated** reviewer packet. It is an execution template, not a completed experiment.

**Next steps:** run notebook; inspect metadata conflicts; select evidence-complete candidate inventories; build paired counterfactuals; independently annotate with two people; retain disagreements; calculate agreement; then decide Prompt 07 readiness.

**User-provided Colab audit already verified:** CSV 20,614 rows, columns `Query`, `Tool`, 199 unique gold labels, 0 unmatched descriptions, 51 exact duplicate records, 64 duplicate query strings, and 16-row discrepancy with the maintainer's README (cause unknown).
