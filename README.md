# A Paired-Delta QRNG Architecture for Controlling Shared Artifacts in Observer–Randomness Experiments

> **Repository updated June 2026. Earlier notebooks remain available for transparency but have been superseded by the Zen analysis notebooks listed below. Readers should use the Zen notebooks for all current analyses and reproductions.**
>
> **Note:** This repository was originally released under the working title _Beyond the Mean_. The current manuscript reflects a revised methodological framing, _A Paired-Delta QRNG Architecture for Controlling Shared Artifacts in Observer–Randomness Experiments_, while retaining the same underlying experimental architecture, datasets, and core analyses.

This repository contains the frozen datasets and analysis notebooks supporting the manuscript:

**"A Paired-Delta QRNG Architecture for Controlling Shared Artifacts in Observer–Randomness Experiments."**

The repository provides a reproducible implementation of the Paired-Delta Protocol (PDP) and all analyses reported in the paper.

---

## Project Overview

This project evaluates an experimental architecture designed to distinguish stream-specific effects from hardware- or environment-level variation in studies involving quantum random number generators (QRNGs).

Traditional QRNG experiments often rely on single-stream analyses (e.g., hit rates). When expected deviations are small relative to system noise, it can be difficult to separate potential observer-linked patterns from drift or environmental artifacts.

The Paired-Delta Protocol embeds a simultaneous control stream within each QRNG call, enabling within-call subtraction and common-mode rejection.

Temporal ordering is assessed using a single-scale Hurst exponent computed at the block level.

The primary contribution is methodological: a paired-delta architecture that embeds a matched control stream within each QRNG call, allowing common-mode influences to be controlled directly while supporting cross-condition and temporal-structure analyses.

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

### `analysis/`

### Notebook 1 — Paired Control Stream Design Validation

`Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb`

Primary design-validation notebook supporting the manuscript.

Documents QRNG labeling logic, hardware audit procedures, and design-merit diagnostics for the Paired Control Stream. Two analyses added in response to peer review are integrated directly into this notebook:

- **Cell 8 — Paired-Delta Null Distribution Validation**: tests for common-mode correlation between streams and validates the empirical null distribution of the paired-delta metric (ΔH).
- **Cell 9 — Artifact Injection Test (Positive Control)**: demonstrates that injected common-mode artifacts cancel under paired subtraction, while stream-specific artifacts survive.

### Notebook 2 — Temporal Structure Analysis

`Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb`

Primary temporal-structure analysis notebook supporting the manuscript.

Statistical analyses include:

- Bayesian hierarchical hit-rate modeling
- Single-scale Hurst exponent computation
- Permutation and shuffle testing
- Bootstrap robustness checks
- Leave-one-out analyses
- Label-swap controls
- Temporal-structure diagnostics

### Legacy and Reference Notebooks

The following notebooks are retained for transparency and historical reference but are **not part of the primary analysis workflow supporting the current manuscript**:

- `Exp4_Notebook_PairedDelta_NullValidation.ipynb`
- `Exp4_Notebook_ArtifactInjection.ipynb`
- `Exp4_Notebook_DualAnalysis.ipynb`

Readers seeking to reproduce the manuscript should use the two Zen notebooks listed above.

### `generate_manifest.py`

Recomputes SHA-256 fingerprints and summary statistics for the frozen CSVs in `data/`, producing `manifest.json`.

---

### `data/`

Frozen CSV datasets (`Frozen_Participants_*.csv`, `Frozen_Sessions_*.csv`, `Frozen_Blocks_*.csv`, `Frozen_Audits_*.csv`) and `manifest.json`, used for integrity verification.

---

### Recommended Notebooks

The Zen notebooks are the maintained and recommended analysis pipeline for this project.

- **`Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb`**
- **`Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb`**

These notebooks run standalone with no Google Drive credentials required and automatically retrieve the archived datasets when needed.

---

## Source Code

The JavaScript implementation used to collect the data is available here:

https://github.com/catboxer/QART1/tree/main/experiments/exp4

---

## Nomenclature Mapping (Code vs Manuscript)

| Manuscript Term             | Code Variable | Description                                   |
| --------------------------- | ------------- | --------------------------------------------- |
| Paired Control Stream (PCS) | `demon`       | Simultaneous hardware control stream          |
| Subject Stream              | `subject`     | Stream assigned to the experimental condition |
| Single-scale Hurst exponent | `hurstApprox` | Block-level ordering metric                   |
| Assignment Bit              | `bit 0`       | First bit used for stream labeling            |

---

## AI Assistance Statement

Large Language Models (LLMs), including systems developed by OpenAI, Anthropic, and Google, were used as research assistance tools during manuscript preparation and code refinement. These systems supported drafting, editing, statistical discussion, and documentation organization.

All experimental design decisions, analyses, interpretations, and final manuscript content were reviewed and approved by the author.

---

## Reproducibility

To reproduce the analyses:

1. Clone the repository (or download the `analysis/` and `data/` folders).
2. Install Python 3.x with `pandas`, `numpy`, `scipy`, `matplotlib`, `pymc`, and `arviz`.
3. Run **Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb** from top to bottom.
4. Run **Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb** from top to bottom.

These two notebooks constitute the authoritative analysis workflow supporting the manuscript.

### Running in Jupyter (local)

```bash
pip install pandas numpy scipy matplotlib pymc arviz jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```

Open the Zen notebooks and select **Run All Cells**.

### Running in Google Colab

1. Open `colab.research.google.com`
2. Upload one of the Zen notebooks or open directly from GitHub.
3. Select **Runtime → Run all**
4. The notebooks automatically download the archived datasets and perform integrity verification.

### Data Integrity Verification

Both Zen notebooks verify loaded datasets against `manifest.json` using SHA-256 hashes and compare row counts and summary statistics against frozen values.

Successful verification reports:

```text
✓ FULL VERIFICATION PASSED
```

To regenerate `manifest.json`, run:

```bash
python generate_manifest.py
```

---

## Data Availability

The frozen datasets and analysis notebooks are available through this repository.

The current manuscript is archived on Zenodo:

https://doi.org/10.5281/zenodo.18703829

The Zen notebooks are configured to download the archived datasets automatically and perform integrity verification using SHA-256 hashes and manifest checks.

---

## License

This project is licensed under the MIT License.
