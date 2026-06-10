# Beyond the Mean: A Paired-Control Architecture for QRNG Experiments

  This repository contains the frozen datasets and analysis notebooks supporting the manuscript:

  **"Paired QRNG Control Streams Reduce Artifactual Structure in Observer–Randomness
  Experiments."**

  The repository provides a reproducible implementation of the Paired-Delta Protocol (PDP) and
  all analyses reported in the paper.

  ---

  ## Project Overview

  This project evaluates an experimental architecture designed to distinguish stream-specific
  effects from hardware- or environment-level variation in studies involving quantum random
  number generators (QRNGs).

  Traditional QRNG experiments often rely on single-stream analyses (e.g., hit rates). When
  expected deviations are small relative to system noise, it can be difficult to separate
  potential observer-linked patterns from drift or environmental artifacts.

  The Paired-Delta Protocol embeds a simultaneous control stream within each QRNG call, enabling
  within-call subtraction and common-mode rejection.

  Temporal ordering is assessed using a single-scale Hurst exponent computed at the block level.

  The primary contribution is methodological: an architecture in which deviations must survive
  hardware control, cross-condition comparison, and temporal diagnostics.

  ---

  ## The Paired-Delta Protocol (PDP)

  Each QRNG call generates two simultaneous 150-bit streams derived from a single physical draw:

  - **Subject Stream** – Assigned to the experimental condition
  - **Paired Control Stream (PCS)** – Simultaneous unattended hardware control
  - **Paired Difference (Δ)** – Stream-level metrics computed as Subject − PCS

  Because both streams originate from the same physical event, shared hardware or environmental
  fluctuations affect both equally and cancel under subtraction.

  ---

  ## Experimental Conditions

  The study evaluates three conditions:

  - **Human Participants** – Interactive sessions involving voluntary engagement
  - **AI Agent Condition** – An LLM-driven interface interacting with the same experimental
  framework
  - **Baseline Condition** – Fully automated execution without agent involvement

  These conditions allow comparison of stream-level behavior across biological, artificial, and
  unattended execution contexts.

  ---

  ## Repository Contents

  ### `analysis/`

  **Notebook 1 — Paired Control Stream Design Validation**
  (`Exp4_Notebook1_GD_Paired_Control_Stream_Design_Validation.ipynb` /
  `Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb`)

  Documents QRNG labeling logic, hardware audit procedures, and design-merit diagnostics for the
  Paired Control Stream. Two analyses added in response to peer review are integrated directly
  into this notebook:

  - **Cell 8 — Paired-Delta Null Distribution Validation**: tests for common-mode correlation
  between streams and validates the empirical null distribution of the paired-delta metric (ΔH).
  - **Cell 9 — Artifact Injection Test (Positive Control)**: demonstrates that injected
  common-mode artifacts cancel under paired subtraction, while stream-specific artifacts survive.

  **Notebook 2 — Temporal Structure Analysis**
  (`Exp4_Notebook2_GD_Temporal_Structure_Analysis.ipynb` /
  `Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb`)

  Statistical analyses including hit-rate modeling (Bayesian hierarchical model), single-scale
  Hurst exponent computation, permutation/shuffle tests, and robustness checks (bootstrap,
  leave-one-out, label-swap).

  **Standalone reference notebooks** — the same null-validation, artifact-injection, and a
  direct-vs-paired comparison analyses, kept as standalone notebooks for readers who want to
  inspect them independently of Notebook 1:
  - `Exp4_Notebook_PairedDelta_NullValidation.ipynb`
  - `Exp4_Notebook_ArtifactInjection.ipynb`
  - `Exp4_Notebook_DualAnalysis.ipynb`

  `generate_manifest.py` — recomputes SHA-256 fingerprints and summary statistics for the frozen
  CSVs in `data/`, producing `manifest.json`.

  ### `data/`

  Frozen CSV datasets (`Frozen_Participants_*.csv`, `Frozen_Sessions_*.csv`,
  `Frozen_Blocks_*.csv`, `Frozen_Audits_*.csv`) and `manifest.json`, used for integrity
  verification.

  ### Zen notebook variants
  
  - **`*_Zen_*`** — runs standalone, with **no Google Drive or credentials required**. On first
  run, automatically downloads the frozen CSVs and `manifest.json` from this repository's `data/`
  folder. **Recommended for reviewers and readers reproducing the analyses.**

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

  Large Language Models (LLMs), including systems developed by OpenAI, Anthropic, and Google,
  were used as research assistance tools during manuscript preparation and code refinement. These
  systems supported drafting, editing, statistical discussion, and documentation organization.
  All experimental design decisions, analyses, interpretations, and final manuscript content were
  reviewed and approved by the author.

  ---

  ## Reproducibility

  To reproduce the analyses:

  1. Clone the repository (or download just the `analysis/` and `data/` folders — the Zen
  notebooks also fetch the data automatically if needed).
  2. Install Python 3.x with `pandas`, `numpy`, `scipy`, `matplotlib`, `pymc`, and `arviz`.
  (Notebook 2 includes a setup cell that installs `pymc`/`arviz` for you when run in Colab.)
  3. Run **Notebook 1 (Zen)** top to bottom. This covers design validation, the paired-delta null
  distribution validation, and the artifact injection positive control.
  4. Run **Notebook 2 (Zen)** top to bottom. This covers the hit-rate and temporal-structure
  (Hurst) analyses.
  5. (Optional) Run the standalone notebooks (`Exp4_Notebook_PairedDelta_NullValidation.ipynb`,
  `Exp4_Notebook_ArtifactInjection.ipynb`, `Exp4_Notebook_DualAnalysis.ipynb`) for the same
  analyses in isolation.

  ### Running in Jupyter (local)

  1. Install dependencies:
     ```bash
     pip install pandas numpy scipy matplotlib pymc arviz jupyter
  2. Launch Jupyter from the analysis/ folder:
  jupyter notebook
  3. Open Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb and select Run All 
  Cells (Cell → Run All, or Kernel → Restart & Run All).
  4. Repeat for Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb.
  5. On first run, the data-loading cell downloads the frozen CSVs and manifest.json into the
  same folder as the notebook — no manual setup needed.

  ### Running in Google Colab

  1. Go to colab.research.google.com and choose File → Upload notebook, then select
  Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb (or
  Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb).

  1. Alternatively, open directly from GitHub: File → Open notebook → GitHub, search
  catboxer/Beyond-The-Mean, and select the notebook from analysis/.
  2. Select Runtime → Run all.
  3. No Google Drive permission prompt should appear — the data-loading cell fetches the frozen
  CSVs from this repository automatically.
  4. Notebook 2's first cell installs pymc and arviz; this can take a minute or two on a fresh
  Colab runtime.

  ### Data integrity verification

  Both notebooks verify the loaded CSVs against `manifest.json` using SHA-256 hashes, and check
  that row counts and summary statistics match the frozen values — this runs automatically as
  part of Cell 1/2 and will report `✓ FULL VERIFICATION PASSED` if the data is unmodified. To
  regenerate `manifest.json` independently, run `generate_manifest.py` in `analysis/`.

  ### Running without Google Drive

  The **Zen** notebooks require no Google Drive access or credentials. Their data-loading cell
  downloads the frozen dataset directly from this repository:

  ```python
  import urllib.request, os

  DATA_BASE = "https://raw.githubusercontent.com/catboxer/Beyond-The-Mean/main/data"
  for fname in [
      "Frozen_Blocks_2026-02-10_195735.csv",
      "Frozen_Sessions_2026-02-10_195735.csv",
      "Frozen_Participants_2026-02-10_195735.csv",
      "Frozen_Audits_2026-02-10_195735.csv",
      "manifest.json"
  ]:
      if not os.path.exists(fname):
          urllib.request.urlretrieve(f"{DATA_BASE}/{fname}", fname)

  FROZEN_BLOCKS_PATH       = "Frozen_Blocks_2026-02-10_195735.csv"
  FROZEN_SESSIONS_PATH     = "Frozen_Sessions_2026-02-10_195735.csv"
  FROZEN_PARTICIPANTS_PATH = "Frozen_Participants_2026-02-10_195735.csv"
  FROZEN_AUDITS_PATH       = "Frozen_Audits_2026-02-10_195735.csv"

  This code is already included in the Zen notebooks — no setup required. Just open the Zen
  notebook in Colab (or run it locally) and the data downloads automatically into the working
  directory on first run.

  ---
  Data Availability

  The frozen datasets and analysis notebooks are available in this repository, in the data/ and
  analysis/ folders.

  A snapshot of the manuscript is archived on Zenodo:

  https://doi.org/10.5281/zenodo.18703829

  ---
  License

  This project is licensed under the MIT License.
