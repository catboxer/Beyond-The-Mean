# The Paired-Delta Protocol: A Within-Call Reference Architecture for Observer–QRNG Research

> **Repository updated September 2026.** The manuscript has been substantially revised in framing and title since the June 2026 version. Readers should use the notebooks listed below — together with the **Paper-to-Notebook Reader Guide** — for all current analyses and reproductions.
>
> **Note:** This repository was originally released under the working title _Beyond the Mean_, then revised to _A Paired-Delta QRNG Architecture for Controlling Shared Artifacts in Observer–Randomness Experiments_. The current manuscript title is **_The Paired-Delta Protocol: A Within-Call Reference Architecture for Observer–QRNG Research_**. All revisions retain the same underlying experimental architecture, frozen datasets, and core analyses; the framing has shifted from a claim of artifact cancellation toward a more conservative claim of **diagnostic leverage** (see below).
>
> **Terminology:** the manuscript now refers to the pilot and its planned replication as **Study 1** and **Study 2**. Code, filenames, Firestore collections, and this repository's folder/notebook names still use the original **Experiment 4 (exp4)** / **Experiment 5 (exp5)** identifiers and are not being renamed, to preserve traceability with the source code repository, the OSF preregistration, and the frozen-data provenance chain. **Study 1 = Experiment 4. Study 2 = Experiment 5.**

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

**The primary contribution is methodological, not a confirmed effect.** The pilot (Study 1 / Experiment 4: 11,607 blocks, 121 human participants, plus AI-agent and automated Baseline conditions) found no clear condition differences in paired mean hit rate. An exploratory, retrospectively selected subgroup (Human participants with 5+ sessions, n = 3) showed a candidate pattern in a single-scale Hurst-exponent ordering score. The paired architecture showed this candidate pattern was formed by roughly equal, opposite-direction movement in the Subject and PCS streams rather than an isolated Subject-stream effect — a configuration also compatible with selection for a large paired difference. This is presented as a **worked example of the protocol's diagnostic value**, not as an established observer-linked result, and motivates a preregistered replication (Study 2 / Experiment 5; see below).

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

See `paper/PDP_Paper_to_Notebook_Reader_Guide.pdf` for a full paper-section-to-notebook-header mapping.

#### Notebook 1 — Paired Control Stream Design Validation

Design validation, PCS calibration, Baseline relational behavior, controlled artifact-injection checks, QRNG audit reconstruction, and synthetic Baseline-offset checks. This is a **primary** source for the manuscript's reported results. It exists as two functionally identical variants, differing only in how they locate the five required frozen input files:

- `Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb` — **local-only.** Searches the notebook's own folder, then `data/`, then recursively from the current working directory. Raises `FileNotFoundError` if a file isn't found; does not fetch anything over the network.
- `Exp4_Notebook1_Git_Paired_Control_Stream_Design_Validation.ipynb` — same local search first, but falls back to downloading any missing file directly from this repository's `data/` folder on GitHub (`raw.githubusercontent.com/catboxer/Beyond-The-Mean/main/data/...`) before failing. Recommended for Colab or a fresh clone without the data files already in hand.

Both require: `Frozen_Blocks_2026-02-10_195735.csv`, `Frozen_Sessions_2026-02-10_195735.csv`, `Frozen_Participants_2026-02-10_195735.csv`, `Frozen_Audits_2026-02-10_195735.csv`, and `Frozen_Exp4_RawBlockBits_2026-07-26.pkl` (the raw pre-split 301-bit calls, added for the whole-call reconstruction work — see `PDP_Diagnostic_Validation_Prereg.ipynb` in `preregistration/`).

Recent additions include:

- Corrected three-subtest audit-battery reconstruction with session-aware summaries and audit-failure session-uniqueness checks
- Scheduled-audit availability/missingness diagnostics
- Alternative ordering metrics across all conditions (contributor-clustered bootstrap)
- Same-position mutual-information sampling-hierarchy and batch-clustering sensitivity checks
- Baseline-offset synthetic-pipeline check and bootstrap seed-stability check
- Shuffle-null mechanism comparison
- Composition-conditioning checks distinguishing selection-adjusted tail probability from point-estimate sensitivity (documented 2+/3+/5+ threshold search)

#### Notebook 2 — Temporal Structure Analysis

Hit-rate results, single-scale Hurst (H_RS) analyses, subgroup and threshold diagnostics, temporal sensitivity, local and lagged coupling, and finite-sample calibration. Also a **primary** source, with the same Zen/Git local-vs-download split as Notebook 1:

- `Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb` — local-only.
- `Exp4_Notebook2_Git_Temporal_Structure_Analysis.ipynb` — local search with a GitHub download fallback.

Recent additions include:

- Session-count pattern (descriptive): mean paired ΔH_RS by condition
- Within-session Hurst-delta drift test (Human 5+ vs. Baseline interaction)
- Hierarchy-preserving family check for lagged-correlation variance

#### Interleaving / Partitioning Audit

`Exp4_Interleaving_PhysicalHalf_AI_and_StreamLength_Audit.ipynb`

Retrospective reconstruction comparing the original contiguous Subject/PCS split against a locally interleaved (PRNG-paired) partition, a physical first-half-vs-second-half H_RS check prior to labeling, and a stream-length variance scan. Used for partitioning-sensitivity and limitations analysis; a **secondary** sensitivity check, not part of the primary Study 1 inferential result set.

#### Exp4-vs-Exp5 Prescreen Cross-Dataset Check

`Exp4_vs_Exp5Prescreen_Baseline_CrossDataset_Check.ipynb`

Secondary, dated comparison of Study 1 Baseline behavior against an in-progress Study 2-prescreen snapshot, kept separate to prevent two structurally different Baseline statistics from being conflated in the manuscript.

#### `generate_manifest.py`

Recomputes SHA-256 fingerprints for the four original frozen CSVs in `data/` (`Frozen_Participants_*`, `Frozen_Sessions_*`, `Frozen_Blocks_*`, `Frozen_Audits_*`) and writes `data/manifest.json`. Run it as `python analysis/generate_manifest.py` (it locates `data/` relative to its own location, not the caller's working directory). **Known gap:** it does not yet hash `Frozen_Exp4_RawBlockBits_2026-07-26.pkl` or `PDP_Diagnostic_Validation_FROZEN.xlsx` — both are present in `data/` but are not covered by manifest-based integrity verification.

---

### `preregistration/`

Analyses locked *before* being run, kept separate from the ordinary exploratory notebooks in `analysis/` so a reader can see at a glance what was prospectively specified.

- **`PDP_Diagnostic_Validation_Prereg.ipynb`** — a preregistered, held-out synthetic-recovery validation of the analysis implementation itself (Registration DOI: `10.17605/OSF.IO/2KRZ3`). Applies the frozen classifier to 2,300 blinded, deliberately-constructed synthetic datasets with the ground-truth key kept separate and hash-verified, then unblinds and scores against preregistered criteria. This tests whether the *code* correctly recovers known, artificially-constructed patterns — it is an implementation/recovery check, not evidence that PDP diagnoses unknown physical-system disturbances. Reported in the manuscript as Section 3.8.
- **`PDP_HRS_IntegratedW_Association_AnalysisPlan_2026-08-25.md`** — a prospectively specified follow-up asking whether two of the paper's exploratory findings (the positive Subject-minus-PCS H_RS difference, and the separately-observed narrowing of local Subject-PCS correlation variance across window sizes) covary within participants, or are better treated as independent observations. Defines the participant-level statistics, the Baseline-matched null procedure, and states in advance that a null result is a reportable outcome distinguishing genuinely coupled findings from independently-arising ones.

---

### `data/`

- `Frozen_Participants_2026-02-10_195735.csv`, `Frozen_Sessions_2026-02-10_195735.csv`, `Frozen_Blocks_2026-02-10_195735.csv`, `Frozen_Audits_2026-02-10_195735.csv` — the core frozen session/block/participant/audit tables, covered by `manifest.json`.
- `Frozen_Exp4_RawBlockBits_2026-07-26.pkl` — raw pre-split 301-bit QRNG calls, keyed by session and block index, required by both Notebook 1 and Notebook 2's whole-call reconstruction. Not yet covered by `manifest.json` (see `generate_manifest.py` above).
- `PDP_Diagnostic_Validation_FROZEN.xlsx` — the frozen development/held-out artifacts (blinded feature table and ground-truth key) used by `preregistration/PDP_Diagnostic_Validation_Prereg.ipynb`. Not yet covered by `manifest.json`.
- `manifest.json` — SHA-256 hashes for the four core CSVs above, used for integrity verification by the Zen/Git notebook pairs.

---

### `paper/`

- **`PDP-Methodology-Paper.pdf`** — the current manuscript.
- **`PDP_Paper_to_Notebook_Reader_Guide.pdf`** — a navigation companion mapping each paper section/claim to the notebook, header, method, and result that produced it, including whether that notebook is the primary or a secondary source.

---

### Recommended Notebooks

Notebook 1 and Notebook 2 (Zen or Git variant — pick Git for a fresh clone or Colab without the data files already present, Zen if you already have `data/` populated and prefer no network access) are the primary analysis pipeline. The Interleaving and Exp4-vs-Exp5 notebooks are secondary sensitivity/consistency checks.

---

## Source Code

The JavaScript implementation used to collect the data is available here:

https://github.com/catboxer/QART1/tree/main/experiments/exp4

---

## Nomenclature Mapping (Code vs Manuscript)

| Manuscript Term                 | Code Variable | Description                                   |
| -------------------------------- | ------------- | --------------------------------------------- |
| Study 1                          | `exp4`        | The pilot study                               |
| Study 2                          | `exp5`        | The preregistered replication                 |
| Paired Control Stream (PCS)      | `demon`       | Simultaneous hardware control stream          |
| Subject Stream                   | `subject`     | Stream assigned to the experimental condition |
| Single-scale Hurst score (H_RS)  | `hurstApprox` | Block-level ordering metric                   |
| Assignment Bit                   | `bit 0`       | First bit used for stream labeling            |

---

## Planned Preregistered Replication (Study 2 / Experiment 5)

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

1. Clone the repository (or download the `analysis/`, `preregistration/`, `data/`, and `paper/` folders).
2. Install Python 3.x with `pandas`, `numpy`, `scipy`, `matplotlib`, `pymc`, and `arviz`.
3. Run **Notebook 1** (`Exp4_Notebook1_Git_...ipynb` if `data/` isn't populated locally, `Exp4_Notebook1_Zen_...ipynb` if it already is) from top to bottom.
4. Run **Notebook 2** (Git or Zen variant, same rule) from top to bottom.
5. For partitioning-sensitivity and cross-dataset checks, run **Exp4_Interleaving_PhysicalHalf_AI_and_StreamLength_Audit.ipynb** and **Exp4_vs_Exp5Prescreen_Baseline_CrossDataset_Check.ipynb**.

Notebooks 1 and 2 constitute the authoritative primary-analysis workflow supporting the manuscript; the Interleaving and Exp4-vs-Exp5 notebooks support secondary sensitivity and consistency checks referenced in the Discussion and Limitations sections.

### Running in Jupyter (local)

```bash
pip install pandas numpy scipy matplotlib pymc arviz jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```

Open the notebooks and select **Run All Cells**. If you're running the Zen (local-only) variants, make sure the five required frozen files are already in `data/` first — they will not be fetched automatically.

### Running in Google Colab

1. Open `colab.research.google.com`
2. Upload or open directly from GitHub one of the **Git**-variant notebooks (`Exp4_Notebook1_Git_...` / `Exp4_Notebook2_Git_...`) — these are the ones that fetch missing frozen files automatically from this repo's `data/` folder. The Zen variants will fail in a fresh Colab session with no local data.
3. Select **Runtime → Run all**

### Data Integrity Verification

Notebooks 1 and 2 (both variants) verify the four core frozen CSVs against `manifest.json` using SHA-256 hashes and compare row counts and summary statistics against frozen values. This check does **not** currently cover `Frozen_Exp4_RawBlockBits_2026-07-26.pkl` or `PDP_Diagnostic_Validation_FROZEN.xlsx` (see the known gap noted under `generate_manifest.py` above).

Successful verification reports:

```text
✓ FULL VERIFICATION PASSED
```

To regenerate `manifest.json` for the four covered CSVs, run:

```bash
python analysis/generate_manifest.py
```

---

## Data Availability

The frozen datasets and analysis notebooks are available through this repository.

The current manuscript is archived on Zenodo:

https://doi.org/10.5281/zenodo.18703829

The Study 2 / Experiment 5 preregistration is on OSF (see above).

The Git-variant notebooks are configured to download any missing frozen dataset files directly from this repository and perform integrity verification using SHA-256 hashes and manifest checks; the Zen-variant notebooks require the files to already be present locally.

---

## License

This project is licensed under the MIT License.
