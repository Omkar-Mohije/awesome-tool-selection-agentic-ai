# References — Curated & Verified Research Papers

All 20 papers below were part of the AI-generated survey paper *"Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems"* or added afterward to strengthen coverage. Every entry was checked against arXiv / DOI / publisher records as part of the [Citation Integrity Audit](../citation-audit/Citation_Integrity_Audit.pdf) (Authenticity Score: 87.5/100 on the audited sample).

> ⚠️ Note on verification: 4 of the entries below (AutoTool, Tool-RoCo, MTU-Bench, TRAJECT-Bench) exist and are genuine arXiv preprints, but the AI did not surface a complete author list for them during generation. This was flagged during the audit as a "wrong/incomplete metadata" (Code B) issue rather than a fabrication — the papers themselves are real and the arXiv IDs resolve correctly.

## Table of Contents
- [Survey Papers](#survey-papers)
- [Foundational Papers](#foundational-papers)
- [Benchmarks & Evaluation Methods](#benchmarks--evaluation-methods)
- [Recent Research](#recent-research)

---

## Survey Papers

- **Tool Learning with Large Language Models: A Survey**
  Qu, C., Dai, S., Wei, X., Cai, H., Wang, S., Yin, D., Xu, J., & Wen, J.-R., 2025, *Frontiers of Computer Science*
  [Paper (DOI)](https://doi.org/10.1007/s11704-024-40678-2)
  Organizes the entire tool-learning pipeline (planning → selection → calling → response) into a single framework; used as the paper's top-level taxonomy.

- **Evaluation and Benchmarking of LLM Agents: A Survey**
  Yehudai, A., et al., 2025, arXiv:2507.21504
  [Paper](https://doi.org/10.48550/arXiv.2507.21504)
  Distinguishes "selection from a fixed candidate set" from "retrieval from a large repository" — the core distinction this repository's paper builds on.

## Foundational Papers

- **Toolformer: Language Models Can Teach Themselves to Use Tools**
  Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Hambro, E., Zettlemoyer, L., Cancedda, N., & Scialom, T., 2023, NeurIPS 2023
  [Paper](https://doi.org/10.48550/arXiv.2302.04761)
  Earliest demonstration that an LLM can learn when and which API to call in a self-supervised way.

- **ReAct: Synergizing Reasoning and Acting in Language Models**
  Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y., 2023, ICLR 2023
  [Paper](https://doi.org/10.48550/arXiv.2210.03629)
  Established the "think → act → observe" loop underlying nearly all modern tool-using agents.

- **HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face**
  Shen, Y., Song, K., Tan, X., Li, D., Lu, W., & Zhuang, Y., 2023, NeurIPS 2023
  [Paper](https://doi.org/10.48550/arXiv.2303.17580)
  Treats other ML models as "tools" dispatched by a controller LLM — an early multi-tool selection architecture.

- **Gorilla: Large Language Model Connected with Massive APIs**
  Patil, S. G., Zhang, T., Wang, X., & Gonzalez, J. E., 2023, NeurIPS 2023
  [Paper](https://doi.org/10.48550/arXiv.2305.15334)
  Introduced retriever-aware fine-tuning so a model adapts to API changes rather than memorizing a fixed tool surface.

## Benchmarks & Evaluation Methods

- **MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use**
  Huang, Y., Shi, J., Li, Y., Fan, C., Wu, S., Zhang, Q., Liu, Y., Zhou, P., Wan, Y., Gong, N. Z., & Sun, L., 2024, ICLR 2024
  [Paper](https://doi.org/10.48550/arXiv.2310.03128)
  Directly targets the selection decision with the ToolE dataset, including deliberately confusable tool groups.

- **API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs**
  Li, M., Zhao, Y., Yu, B., Song, F., Li, H., Yu, H., Li, Z., Huang, F., & Li, Y., 2023, EMNLP 2023
  [Paper](https://doi.org/10.48550/arXiv.2304.08244)
  Separates an agent's ability to *call* an API from its ability to first *retrieve and plan* which API to use.

- **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-World APIs**
  Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., Lin, Y., Cong, X., Tang, X., Qian, B., Zhao, S., Hong, L., Tian, R., Xie, R., Zhou, J., Gerstein, M., Li, D., Liu, Z., & Sun, M., 2024, ICLR 2024
  [Paper](https://doi.org/10.48550/arXiv.2307.16789)
  Constructs ToolBench from 16,464 real RESTful APIs; introduces DFS-based multi-trace decision search.

- **TaskBench: Benchmarking Large Language Models for Task Automation**
  Shen, Y., Song, K., Tan, X., Zhang, W., Ren, K., Yuan, S., Lu, W., Li, D., & Zhuang, Y., 2023, arXiv:2311.18760
  [Paper](https://doi.org/10.48550/arXiv.2311.18760)
  Reframes tool selection as graph construction, proposing Node-F1 / Edge-F1 to separate tool ID from sequencing errors.

- **The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models**
  Patil, S. G., Mao, H., Ji, C. C.-J., Yan, F., Suresh, V., Stoica, I., & Gonzalez, J. E., 2025, ICML 2025
  [Leaderboard / Paper](https://gorilla.cs.berkeley.edu/leaderboard.html)
  The standard, deterministic AST-matching leaderboard for function-calling accuracy across single- and multi-turn settings.

- **τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains**
  Yao, S., Shinn, N., Razavi, P., & Narasimhan, K., 2024, arXiv:2406.12045
  [Paper](https://doi.org/10.48550/arXiv.2406.12045)
  Evaluates tool selection inside realistic multi-turn, policy-constrained conversations (retail/airline), not isolated single-turn calls.

- **GAIA: A Benchmark for General AI Assistants**
  Mialon, G., Fourrier, C., Swift, C., Wolf, T., LeCun, Y., & Scialom, T., 2023, arXiv:2311.12983
  [Paper](https://doi.org/10.48550/arXiv.2311.12983)
  Broader agent benchmark requiring reasoning, web browsing and tool use together; shows a large human–AI performance gap (92% vs 15%).

## Recent Research

- **ToolRL: Reward is All Tool Learning Needs**
  Qian, C., Acikgoz, E. C., He, Q., Wang, H., Chen, X., Hakkani-Tür, D., Tur, G., & Ji, H., 2025, arXiv:2504.13958
  [Paper](https://doi.org/10.48550/arXiv.2504.13958)
  Proposes RL reward design specifically for tool-use learning, improving generalization to unseen tools over supervised fine-tuning.

- **Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models**
  Shi, Z., Wang, Y., Yan, L., Ren, P., Wang, S., Yin, D., & Ren, Z., 2025, ACL Findings 2025
  [Paper](https://aclanthology.org/2025.findings-acl.1258/)
  Shows standard dense/sparse retrievers are tuned for lexical similarity, not functional correctness — a key bottleneck for tool retrieval at scale.

- **MLLM-Tool: A Multimodal Large Language Model for Tool Agent Learning**
  Wang, X., et al., 2025, WACV 2025
  [Paper](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_MLLM-Tool_A_Multimodal_Large_Language_Model_for_Tool_Agent_Learning_WACV_2025_paper.pdf)
  Reports 88.19% tool-selection accuracy after fine-tuning on the multimodal ToolMMBench benchmark.

- **AutoTool: Efficient Tool Selection for Large Language Model Agents**
  (2025), arXiv:2511.14650
  [Paper](https://doi.org/10.48550/arXiv.2511.14650)
  Prunes the candidate tool space before invoking full LLM reasoning; evaluated across ALFWorld, ScienceWorld and API-query tasks.

- **Tool-RoCo: An Agent-as-Tool Self-Organization LLM Benchmark in Multi-Robot Cooperation**
  (2025), arXiv:2511.21510
  [Paper](https://doi.org/10.48550/arXiv.2511.21510)
  Extends "tool" to mean other cooperating agents; finds current LLM agents rarely invoke each other even when beneficial.

- **MTU-Bench: A Multi-Granularity Tool-Use Benchmark for Large Language Models**
  (2024), arXiv:2410.11710
  [Paper](https://doi.org/10.48550/arXiv.2410.11710)
  Unifies single-tool, multi-tool, and multi-turn tool-use evaluation in one benchmark suite.

- **TRAJECT-Bench: A Trajectory-Aware Benchmark for Evaluating Agentic Tool Use**
  (2025), arXiv:2510.04550
  [Paper](https://doi.org/10.48550/arXiv.2510.04550)
  Separately reports tool-selection accuracy, argument correctness, and dependency/order satisfaction instead of one pass/fail score.
