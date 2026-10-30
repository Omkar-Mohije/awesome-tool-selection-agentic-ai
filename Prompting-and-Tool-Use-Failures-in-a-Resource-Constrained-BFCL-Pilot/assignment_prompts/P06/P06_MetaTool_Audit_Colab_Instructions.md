# P06 follow-up — reproducible dataset and annotation pilot

Status: **NOT EXECUTED.** The notebook `P06_MetaTool_Audit_and_Annotation_Pilot.ipynb` was prepared in the associated ChatGPT conversation for the researcher to run in Google Colab; it has not been uploaded here yet. Results must not be claimed until real outputs are collected.

1. Run the notebook on Google Colab; pin the MetaTool commit shown by `git rev-parse HEAD`, capture real schema, row-count discrepancy, missing mappings, duplicates, sample and checksums.
2. Preserve `audit_summary.json`, `source_queries_for_review.csv`, and `pilot_annotation_template.csv` as execution records. Confirm dataset redistribution terms before publishing any sampled records.
3. Assess whether descriptions and schemas provide enough information to justify `SELECT`, `NO_VALID_TOOL`, and `NEEDS_CLARIFICATION`; do not infer no-valid-tool from missing documentation.
4. Arrange two independent human annotators to review eligible source query families and controlled counterfactuals. Keep model suggestions separate from ground truth; record evidence and disagreement/adjudication.
5. Verify the baseline's compatible three-way action space, model licenses and Colab environment before freezing Prompt 07.

No experimental result, dataset-derived three-way annotation, or validation score is asserted by this document.
