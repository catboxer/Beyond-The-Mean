# The Paired-Delta Protocol: A Within-Call Reference Architecture for Observer–QRNG Research

> **Repository updated August 2026.** The manuscript has been substantially revised in framing and title since the June 2026 version. Readers should use the four Zen/audit notebooks listed below — together with the **Paper-to-Notebook Reader Guide** — for all current analyses and reproductions.
>
> **Note:** This repository was originally released under the working title _Beyond the Mean_, then revised to _A Paired-Delta QRNG Architecture for Controlling Shared Artifacts in Observer–Randomness Experiments_. The current manuscript title is **_The Paired-Delta Protocol: A Within-Call Reference Architecture for Observer–QRNG Research_**. All revisions retain the same underlying experimental architecture, frozen datasets, and core analyses; the framing has shifted from a claim of artifact cancellation toward a more conservative claim of **diagnostic leverage** (see below).

This repository contains the frozen datasets and analysis notebooks supporting the manuscript:

**"The Paired-Delta Protocol: A Within-Call Reference Architecture for Observer–QRNG Research"** — Andrea Rester Campbell, Independent Researcher.

The repository provides a reproducible implementation of the Paired-Delta Protocol (PDP) and all analyses reported in the paper.

---

## Project Overview

This project introduces and pilots an experimental architecture for studying whether human (or AI-agent) intention is associated with deviations in quantum random number generator (QRNG) output, while making it possible to see how any observed deviation is distributed across the components of a single acquisition.

Traditional single-stream QRNG designs (e.g., hit-rate analyses) cannot show whether an observed deviation is confined to the retained stream, shared across the acquisition, or accompanied by changes in a same-call companion stream. Small reported effects in this literature are also difficult to separate from publication bias, analytic flexibility, hardware variation, and environmental fluctuation.

The Paired-Delta Protocol (PDP) addresses this by deriving a **Subject stream** and a **Paired Control Stream (PCS)** from the same QRNG call. PDP is metric-agnostic and supports three complementary analysis families:

1. **Direct (single-stream) analysis** — the conventional comparison of one stream against an external/theoretical reference.
2. **Paired-differential analysis** — Subject minus PCS, computed within the same call, providing *conditional* common-mode control (not general protection from all artifacts).
3. **Relational analysis** — how the two streams' association, temporal alignment, and stability vary together, a property with no single-channel equivalent.

**The primary contribution is methodological, not a confirmed effect.** The pilot (Experiment 4: 11,607 blocks, 121 human participants, plus AI-agent and automated Baseline conditions) found no clear condition differences in paired mean hit rate. An exploratory, retrospectively selected subgroup (Human participants with 5+ sessions, n = 3) showed a candidate pattern in a single-scale Hurst-exponent ordering score. The paired architecture showed this candidate pattern was formed by roughly equal, opposite-direction movement in the Subject and PCS streams rather than an isolated Subject-stream effect — a configuration also compatible with selection for a large paired difference. This is presented as a **worked example of the protocol's diagnostic value**, not as an established observer-linked result, and motivates a preregistered replication (Experiment 5; see below).

---

## The Paired-Delta Protocol (PDP)

Each QRNG call generates two simultaneous 150-bit streams derived from a single physical draw:

- **Subject Stream** – Assigned to the experimental condition
- **Paired Control Stream (PCS)** – Simultaneous unattended hardware control
- **Paired Difference (Δ)** – Stream-level metrics computed as Subject − PCS

Because both streams originate from the same physical event, contributions expressed **equally** in both stream statistics cancel under subtraction. Contributions that affect the streams unequally, vary across the acquisition, or interact with the selected metric may remain — so the paired comparison provides **conditional common-mode control**, not blanket protection against all artifacts. No naturally occurring disturbance of known type and magnitude was observed in the pilot, so operational artifact cancellation was demonstrated under controlled injection but not established for real-world confounds.

---

## Experimental Conditions

The study evaluates three conditions:

- **Human Participants** – Interactive sessions involving voluntary engagement
- **AI Agent Condition** – An LLM-driven interface interacting with the same experimental framework (a constrained, API-driven procedural comparison, not a fully adaptive agent)
- **Baseline Condition** – Fully automated execution without agent involvement

These conditions allow comparison of stream-level behavior across biological, artificial, and unattended execution contexts.

---

## Repository Contents

### `analysis/`

The four notebooks below are the current, maintained analysis pipeline. NB1 and NB2 are the **primary** sources for the manuscript's reported results; the Interleaving and Exp4-vs-Exp5 notebooks are **secondary** sensitivity/consistency checks. See `paper/PDP_Paper_to_Notebook_Reader_Guide.pdf` for a full paper-section-to-notebook-header mapping.

#### Notebook 1 — Paired Control Stream Design Validation

`Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb`

Design validation, PCS calibration, Baseline relational behavior, controlled artifact-injection checks, QRNG audit reconstruction, and synthetic Baseline-offset checks. Recent additions include:

- Corrected three-subtest audit-battery reconstruction with session-aware summaries and audit-failure session-uniqueness checks
- Scheduled-audit availability/missingness diagnostics
- Alternative ordering metrics across all conditions (contributor-clustered bootstrap)
- Same-position mutual-information sampling-hierarchy and batch-clustering sensitivity checks
- Baseline-offset synthetic-pipeline check and bootstrap seed-stability check
- Shuffle-null mechanism comparison
- Composition-conditioning checks distinguishing selection-adjusted tail probability from point-estimate sensitivity (documented 2+/3+/5+ threshold search)

#### Notebook 2 — Temporal Structure Analysis

`Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb`

Hit-rate results, single-scale Hurst (H_RS) analyses, subgroup and threshold diagnostics, temporal sensitivity, local and lagged coupling, and finite-sample calibration. Recent additions include:

- Session-count pattern (descriptive): mean paired ΔH_RS by condition
- Within-session Hurst-delta drift test (Human 5+ vs. Baseline interaction)
- Hierarchy-preserving family check for lagged-correlation variance

#### Interleaving / Partitioning Audit

`Exp4_Interleaving_PhysicalHalf_AI_and_StreamLength_Audit.ipynb`

Retrospective reconstruction comparing the original contiguous Subject/PCS split against a locally interleaved (PRNG-paired) partition, a physical first-half-vs-second-half H_RS check prior to labeling, and a stream-length variance scan. Used for partitioning-sensitivity and limitations analysis; not part of the primary Pilot-4 inferential result set.

#### Exp4-vs-Exp5 Prescreen Cross-Dataset Check

`Exp4_vs_Exp5Prescreen_Baseline_CrossDataset_Check.ipynb`

Secondary, dated comparison of Pilot-4 Baseline behavior against an in-progress Exp5-prescreen snapshot, kept separate to prevent two structurally different Baseline statistics from being conflated in the manuscript.

### `generate_manifest.py`

Recomputes SHA-256 fingerprints and summary statistics for the frozen CSVs in `data/`, producing `manifest.json`.

---

### `data/`

Frozen CSV datasets (`Frozen_Participants_*.csv`, `Frozen_Sessions_*.csv`, `Frozen_Blocks_*.csv`, `Frozen_Audits_*.csv`) and `manifest.json`, used for integrity verification.

---

### `paper/`

- **`PDP-Methodology-Paper.pdf`** — the current manuscript.
- **`PDP_Paper_to_Notebook_Reader_Guide.pdf`** — a navigation companion mapping each paper section/claim to the notebook, header, method, and result that produced it, including whether that notebook is the primary or a secondary source.

---

### Recommended Notebooks

The four notebooks above are the maintained and recommended analysis pipeline for this project (NB1 and NB2 primary; Interleaving and Exp4-vs-Exp5 secondary).

These notebooks run standalone with no Google Drive credentials required and automatically retrieve the archived datasets when needed.

---

## Source Code

The JavaScript implementation used to collect the data is available here:

https://github.com/catboxer/QART1/tree/main/experiments/exp4

---

## Nomenclature Mapping (Code vs Manuscript)

| Manuscript Term              | Code Variable | Description                                   |
| ----------------------------- | ------------- | --------------------------------------------- |
| Paired Control Stream (PCS)   | `demon`       | Simultaneous hardware control stream          |
| Subject Stream                | `subject`     | Stream assigned to the experimental condition |
| Single-scale Hurst score (H_RS) | `hurstApprox` | Block-level ordering metric                   |
| Assignment Bit                | `bit 0`       | First bit used for stream labeling            |

---

## Planned Preregistered Replication (Experiment 5)

A follow-up study has been provisionally preregistered to test the paired-differential and single-stream findings as primary confirmatory analyses, with secondary, prespecified relational analyses (local Subject–PCS correlation variability and lagged cross-correlation across a fixed range of lags). It also explores individual-difference "permeability" measures as an exploratory objective.

Preregistration: https://osf.io/yseqj/overview?view_only=98fef7fec86244749d80e778424a065f

---

## Ethics and Informed Consent

This study was conducted by an independent researcher without institutional affiliation; prospective review by an institutional review board or research ethics committee was not obtained. The study was conducted with reference to the principles of respect for persons, beneficence, and justice described in the Belmont Report. Participation was voluntary, and no clinical, deceptive, or high-risk procedures were used.

---

## AI Assistance Statement

Large Language Models (LLMs) were used during the development of experimental code, data-processing pipelines, and manuscript drafting. Study design, architectural decisions, and analytic strategy were directed by the author. All generated code and analyses were reviewed and validated against the frozen dataset prior to inclusion in the manuscript.

---

## Reproducibility

To reproduce the analyses:

1. Clone the repository (or download the `analysis/`, `data/`, and `paper/` folders).
2. Install Python 3.x with `pandas`, `numpy`, `scipy`, `matplotlib`, `pymc`, and `arviz`.
3. Run **Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb** from top to bottom.
4. Run **Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb** from top to bottom.
5. For partitioning-sensitivity and cross-dataset checks, run **Exp4_Interleaving_PhysicalHalf_AI_and_StreamLength_Audit.ipynb** and **Exp4_vs_Exp5Prescreen_Baseline_CrossDataset_Check.ipynb**.

NB1 and NB2 constitute the authoritative primary-analysis workflow supporting the manuscript; the Interleaving and Exp4-vs-Exp5 notebooks support secondary sensitivity and consistency checks referenced in the Discussion and Limitations sections.

### Running in Jupyter (local)

```bash
pip install pandas numpy scipy matplotlib pymc arviz jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```

Open the notebooks and select **Run All Cells**.

### Running in Google Colab

1. Open `colab.research.google.com`
2. Upload one of the notebooks or open directly from GitHub.
3. Select **Runtime → Run all**
4. The notebooks automatically download the archived datasets and perform integrity verification.

### Data Integrity Verification

The notebooks verify loaded datasets against `manifest.json` using SHA-256 hashes and compare row counts and summary statistics against frozen values.

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

The Experiment 5 preregistration is on OSF (see above).

The notebooks are configured to download the archived datasets automatically and perform integrity verification using SHA-256 hashes and manifest checks.

---

## License

This project is licensed under the MIT License.
