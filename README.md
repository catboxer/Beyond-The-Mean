# Beyond the Mean: Identifying Observer-Coupled Temporal Structure in Quantum Randomness

This repository contains the frozen datasets and analysis notebooks for the paper:
**"PAIRED QRNG CONTROL STREAMS REDUCE ARTIFACTUAL STRUCTURE IN MICRO-EFFECT EXPERIMENTS"**

## The Project
Traditional micro-PK research has relied on "hit rates" (bit-frequency) to detect anomalies. This project provides the primary validation for a **Paired-Delta Architecture** which is a design refined since late 2025 that uses simultaneous hardware controls to isolate observer-dependent effects from hardware drift, timing artifacts, and environmental noise.

By analyzing the **temporal structure** (Single-scale Hurst exponent) rather than just the mean, we identify patterns in quantum randomness that are specifically coupled to human observers.

### Key Contributions
* **The Architecture:** A rigorous validation of a simultaneous, quantum-labeled paired-control stream design.
* **The Metric:** Shifting the focus from aggregate bit-counts (the Mean) to internal bit-ordering (Temporal Structure) using the Single-scale Hurst exponent.
* **The Control:** Utilizing an LLM agent as a "Temporally Decoupled Intent" control. Due to the discrete state-management of the AI interface, the agent’s intent is processed prior to the QRNG call, providing a control that lacks the sustained concurrent attention present in human sessions.

## Repository Contents
This is a "Clean Room" reproduction repository, split into two primary workflows:
1. **Design Validation Notebook:** Documentation of the Paired-Delta apparatus, quantum label assignment, and 1000-bit hardware audit protocols.
2. **Analysis of Findings Notebook:** The pipeline for Bayesian hierarchical modeling, Hurst exponent calculation, window-shuffle tests, and label-swap permutations.
3. **data/:** Frozen CSV datasets with SHA-256 fingerprints to ensure results are fixed and verifiable.

### Source Code
The original JavaScript experimental logic and environment used to collect this data can be found in the primary project repository:
[QART1 Experiment 4 Source](https://github.com/catboxer/QART1/tree/main/experiments/exp4)

## Note on Nomenclature (Code vs. Manuscript)
To maintain the integrity of the frozen data and the original analysis path, variable names in the code have not been altered to match the formal manuscript. Use this key to map the Source/Analysis code to the Paper:

| Paper Term | Source/Analysis Variable | Description |
| :--- | :--- | :--- |
| **Paired Control Stream (PCS)** | `demon` | The simultaneous, unattended hardware control stream. |
| **Subject Stream** | `subject` | The stream assigned to the observer via the quantum coin flip. |
| **Single-scale Hurst exponent** | `hurstApprox` | The temporal structure metric computed for each 150-bit block. |
| **Assignment Bit** | `bit 0` | The first bit of the 301-bit fetch used to assign labels. |

## AI Contribution Statement
This project was developed with significant collaborative input from Large Language Models (LLMs), including **Claude (Anthropic)**, **ChatGPT (OpenAI)**, and **Gemini (Google)**. These models contributed heavily to the statistical framework, experimental design, architectural logic, and documentation.

## Reproducibility
To replicate the results:
1. Clone this repository.
2. Ensure you have `Python 3.x`, `Pandas`, `SciPy`, and `PyMC` installed.
3. Run the **Design Validation** notebook first to verify hardware health, followed by the **Analysis** notebook.

## Data Availability
All data is open-access. A permanent archival record and DOI are available via Zenodo: 
`[INSERT YOUR ZENODO DOI LINK HERE]`

## License
This project is licensed under the **MIT License**.
