# Datasets

Three datasets directly usable for training or evaluating tool-selection accuracy.

- **ToolBench**
  Source: [OpenBMB/ToolBench](https://github.com/OpenBMB/ToolBench) (companion to the ToolLLM paper, ICLR'24 Spotlight)
  Description: Instruction-tuning dataset built from 16,464 real-world RESTful APIs across 49 categories (RapidAPI Hub), with multi-step tool-use trajectories.
  Application: Fine-tuning and evaluating LLMs on realistic, large-scale multi-tool selection and invocation.

- **MetaTool / ToolE**
  Source: Released with the [MetaTool benchmark](https://doi.org/10.48550/arXiv.2310.03128) (Huang et al., 2024)
  Description: User queries annotated for (a) whether a tool is needed at all and (b) which single tool or tool-combination is correct, including deliberately confusable near-duplicate tool groups.
  Application: Testing invocation-necessity detection and fine-grained tool discrimination, isolated from argument-generation errors.

- **Berkeley Function-Calling Leaderboard (BFCL) Dataset**
  Source: [Gorilla / BFCL, ShishirPatil/gorilla](https://github.com/ShishirPatil/gorilla)
  Description: Live and non-live single-turn, parallel, and multi-turn function-calling test cases across Python, Java, JavaScript and REST APIs, evaluated via deterministic AST matching.
  Application: Standardized, reproducible benchmarking of tool/function-selection and argument accuracy across models.
