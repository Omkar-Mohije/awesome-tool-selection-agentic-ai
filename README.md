# Awesome Tool-Selection Accuracy in Agentic AI

A curated, verified collection of research papers, datasets, tools, implementations, and learning resources on **tool-selection accuracy in multi-tool agentic AI systems** — the problem of an LLM agent choosing the correct tool (or set of tools) from a candidate pool to complete a task.

This repository accompanies an AI-assisted research paper on the topic and a systematic citation-integrity audit of that paper's references.

## Contents
- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Survey Papers](#survey-papers)
- [Foundational Papers](#foundational-papers)
- [Benchmarks & Evaluation Methods](#benchmarks--evaluation-methods)
- [Recent Research](#recent-research)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [License](#license)

## Overview

As large language models are deployed as autonomous agents, they must increasingly choose among many external functions, APIs, and plug-ins to satisfy a user instruction. **Tool-selection accuracy** — whether an agent picks the correct tool from a candidate set, independent of whether it later fills in correct arguments or achieves a correct final outcome — has become a first-order determinant of end-to-end agent reliability.

The field decomposes this problem into several sub-tasks: deciding whether a tool is needed at all (invocation necessity), discriminating between functionally similar tools, retrieving candidates from large repositories, grounding arguments once a tool is chosen, and correctly sequencing tools in multi-step trajectories. Benchmarks such as MetaTool, ToolLLM/ToolBench, API-Bank, TaskBench, τ-bench, and the Berkeley Function-Calling Leaderboard (BFCL) each target different slices of this problem, using metrics ranging from simple top-1 accuracy to set-based F1, ranked-retrieval metrics, and graph-based Node-F1/Edge-F1 scores.

Key open challenges include: persistent confusion between semantically overlapping tools, degraded accuracy as candidate/repository size grows, inconsistent evaluation protocols across benchmarks, and the difficulty of isolating selection error from downstream execution error. This repository organizes verified literature, datasets, and tools around these themes, and separately documents a hands-on audit of how reliable AI-generated citations on this topic actually are.

## AI-Assisted Research Paper

**Title:** Evaluating Tool-Selection Accuracy in Multi-Tool Agentic AI Systems — *A Survey of Metrics, Benchmarks, and Open Challenges*

A ~10-page, AI-assisted survey covering the taxonomy of tool-selection sub-problems, the metrics used to evaluate each, current benchmarks and approaches (prompting/reasoning, fine-tuning + retrieval, reinforcement learning), open research challenges, and future directions.

[View Paper](paper/AI_Assisted_Research_Paper.pdf)

## Citation Integrity Audit

Before adding any reference to this repository, every citation in the original AI-generated paper was checked against arXiv, DOI/Crossref, and publisher records rather than trusted at face value. A systematically sampled set of 10 references (first 3, last 3, and 4 spread through the middle of the bibliography) was audited in full for authenticity, correct metadata, and whether the paper genuinely supports the claim it was cited for.

**Result:** 18 total references, 10 deep-audited → 5 fully verified, 5 with minor metadata issues (mainly missing author lists in the most recently published entries), 0 fabricated, 0 identifier mismatches. **Authenticity Score: 87.5/100.** Pre-verification plausibility predictions were correct 100% of the time — meaning citations that *looked* professional were, in this sample, genuinely real, though not always fully accurate in their details.

[View Audit](citation-audit/Citation_Integrity_Audit.pdf)

## Survey Papers
- **Tool Learning with Large Language Models: A Survey** — Qu et al., 2025. [DOI](https://doi.org/10.1007/s11704-024-40678-2)
- **Evaluation and Benchmarking of LLM Agents: A Survey** — Yehudai et al., 2025. [arXiv:2507.21504](https://doi.org/10.48550/arXiv.2507.21504)

*(Full list with descriptions: [references/references.md](references/references.md))*

## Foundational Papers
- **Toolformer** — Schick et al., 2023. [arXiv:2302.04761](https://doi.org/10.48550/arXiv.2302.04761)
- **ReAct** — Yao et al., 2023. [arXiv:2210.03629](https://doi.org/10.48550/arXiv.2210.03629)
- **HuggingGPT** — Shen et al., 2023. [arXiv:2303.17580](https://doi.org/10.48550/arXiv.2303.17580)
- **Gorilla** — Patil et al., 2023. [arXiv:2305.15334](https://doi.org/10.48550/arXiv.2305.15334)

## Benchmarks & Evaluation Methods
- **MetaTool** — Huang et al., 2024. [arXiv:2310.03128](https://doi.org/10.48550/arXiv.2310.03128)
- **API-Bank** — Li et al., 2023. [arXiv:2304.08244](https://doi.org/10.48550/arXiv.2304.08244)
- **ToolLLM / ToolBench** — Qin et al., 2024. [arXiv:2307.16789](https://doi.org/10.48550/arXiv.2307.16789)
- **TaskBench** — Shen et al., 2023. [arXiv:2311.18760](https://doi.org/10.48550/arXiv.2311.18760)
- **Berkeley Function-Calling Leaderboard (BFCL)** — Patil et al., 2025. [Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- **τ-bench** — Yao et al., 2024. [arXiv:2406.12045](https://doi.org/10.48550/arXiv.2406.12045)
- **GAIA** — Mialon et al., 2023. [arXiv:2311.12983](https://doi.org/10.48550/arXiv.2311.12983)

## Recent Research
- **ToolRL** — Qian et al., 2025. [arXiv:2504.13958](https://doi.org/10.48550/arXiv.2504.13958)
- **Retrieval Models Aren't Tool-Savvy** — Shi et al., 2025. [ACL Findings 2025](https://aclanthology.org/2025.findings-acl.1258/)
- **MLLM-Tool** — Wang et al., 2025 (WACV). [Paper](https://openaccess.thecvf.com/content/WACV2025/papers/Wang_MLLM-Tool_A_Multimodal_Large_Language_Model_for_Tool_Agent_Learning_WACV_2025_paper.pdf)
- **AutoTool** — 2025. [arXiv:2511.14650](https://doi.org/10.48550/arXiv.2511.14650)
- **Tool-RoCo** — 2025. [arXiv:2511.21510](https://doi.org/10.48550/arXiv.2511.21510)
- **MTU-Bench** — 2024. [arXiv:2410.11710](https://doi.org/10.48550/arXiv.2410.11710)
- **TRAJECT-Bench** — 2025. [arXiv:2510.04550](https://doi.org/10.48550/arXiv.2510.04550)

*(Full list with one-line descriptions for every paper: [references/references.md](references/references.md))*

## Datasets
See [datasets/datasets.md](datasets/datasets.md) for full details.
- ToolBench (16k+ real-world APIs)
- MetaTool / ToolE (tool-necessity and discrimination annotations)
- BFCL Dataset (single/multi-turn function-calling test cases)

## Tools and Libraries
See [tools/tools.md](tools/tools.md) for full details.
- LangChain
- LlamaIndex
- CrewAI
- Hugging Face smolagents
- OpenBMB BMTools

## GitHub Implementations
See [implementations/github-repositories.md](implementations/github-repositories.md) for full details.
- OpenBMB/ToolBench
- ShishirPatil/gorilla
- sierra-research/tau-bench
- microsoft/JARVIS
- philschmid/ai-agent-benchmark-compendium

## Tutorials and Learning Resources
- **[Hugging Face Agents Course](https://github.com/huggingface/agents-course)** — Free, hands-on course covering agent fundamentals, frameworks, and tool use.
- **[LangChain — Agents documentation](https://docs.langchain.com/oss/javascript/langchain/agents)** — Official guide to building agents that select and call tools in a loop.
- **[LangChain-OpenTutorial — Tools notebook](https://github.com/LangChain-OpenTutorial/LangChain-OpenTutorial/blob/main/15-Agent/01-Tools.ipynb)** — Worked notebook on defining and binding tools for agent use.
- **[AI Agent Benchmark Compendium (blog)](https://www.philschmid.de/benchmark-compedium)** — Accessible written overview of 50+ agent/tool-use benchmarks and what each measures.
- **[LlamaIndex vs LangChain for Agentic Workflows (ZenML blog)](https://www.zenml.io/blog/llamaindex-vs-langchain)** — Practical comparison of the two most common frameworks for building tool-using agents.

## License

Content in this repository (README, curation, descriptions) is released under the [MIT License](LICENSE). The AI-assisted paper and citation audit are the author's own work. Linked external papers, datasets, and repositories remain under their own respective licenses — see each source for details.
