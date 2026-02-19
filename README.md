# Beyond the Mean: A Paired-Control Architecture for QRNG Experiments

This repository contains the frozen datasets and analysis notebooks supporting the manuscript:

**“Paired QRNG Control Streams Reduce Artifactual Structure in Observer–Randomness Experiments.”**

The repository provides a reproducible implementation of the Paired-Delta Protocol (PDP) and all analyses reported in the paper.

---

## Project Overview

This project evaluates an experimental architecture designed to distinguish stream-specific effects from hardware- or environment-level variation in studies involving quantum random number generators (QRNGs).

Traditional QRNG experiments often rely on single-stream analyses (e.g., hit rates). When expected deviations are small relative to system noise, it can be difficult to separate potential observer-linked patterns from drift or environmental artifacts.

The Paired-Delta Protocol embeds a simultaneous control stream within each QRNG call, enabling within-call subtraction and common-mode rejection.

Temporal ordering is assessed using a single-scale Hurst exponent computed at the block level.

The primary contribution is methodological: an architecture in which deviations must survive hardware control, cross-condition comparison, and temporal diagnostics.

---

## The Paired-Delta Protocol (PDP)

Each QRNG call generates two simultaneous 150-bit streams derived from a single physical draw:

- **Subject Stream** – Assigned to the experimental condition  
- **Paired Control Stream (PCS)** – Simultaneous unattended hardware control  
- **Paired Difference (Δ)** – Stream-level metrics computed as Subject − PCS  

Because both streams originate from the same physical event, shared hardware or environmental fluctuations affect both equally and cancel under subtraction.

---

## Experimental Conditions

The study evaluates three conditions:

- **Human Participants** – Interactive sessions involving voluntary engagement  
- **AI Agent Condition** – An LLM-driven interface interacting with the same experimental framework  
- **Baseline Condition** – Fully automated execution without agent involvement  

These conditions allow comparison of stream-level behavior across biological, artificial, and unattended execution contexts.

---

## Repository Contents

This repository contains:

1. **Design Validation Notebook** – Documentation of QRNG labeling logic and hardware audit procedures  
2. **Analysis Notebook** – Statistical analyses including paired-delta computation, Hurst exponent calculation, permutation tests, and hierarchical modeling  
3. **data/** – Frozen CSV datasets with SHA-256 fingerprints for verification  

---

## Source Code

The JavaScript implementation used to collect the data is available here:

https://github.com/catboxer/QART1/tree/main/experiments/exp4

---

## Nomenclature Mapping (Code vs Manuscript)

| Manuscript Term | Code Variable | Description |
|-----------------|--------------|-------------|
| Paired Control Stream (PCS) | `demon` | Simultaneous hardware control stream |
| Subject Stream | `subject` | Stream assigned to the experimental condition |
| Single-scale Hurst exponent | `hurstApprox` | Block-level ordering metric |
| Assignment Bit | `bit 0` | First bit used for stream labeling |

---

## AI Assistance Statement

Large Language Models (LLMs), including systems developed by OpenAI, Anthropic, and Google, were used as research assistance tools during manuscript preparation and code refinement. These systems supported drafting, editing, statistical discussion, and documentation organization. All experimental design decisions, analyses, interpretations, and final manuscript content were reviewed and approved by the author.

---

## Reproducibility

To reproduce the analyses:

1. Clone the repository  
2. Install Python 3.x with `pandas`, `scipy`, and `pymc`  
3. Run the **Design Validation** notebook  
4. Run the **Analysis** notebook  

---

## Data Availability

All datasets and analysis code are publicly archived at:

`https://doi.org/10.5281/zenodo.18703829`

This Zenodo record represents a frozen snapshot of the repository at the time of manuscript submission and ensures full reproducibility of the reported analyses.

---

## License

This project is licensed under the **MIT License**.
