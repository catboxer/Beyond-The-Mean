# Changelog

All notable changes to this repository's paper, notebooks, and data documentation are listed here.

## [2026-08-18]

### Paper

- **Title changed**: "A Paired-Delta QRNG Architecture for Controlling Shared Artifacts in Observer–Randomness Experiments" → **"The Paired-Delta Protocol: A Within-Call Reference Architecture for Observer–QRNG Research."**
- **Framing revised** from a general artifact-cancellation claim to **diagnostic leverage**: paired subtraction is now described as *conditional* common-mode control (removes contributions expressed equally in both stream statistics; does not by itself guard against unequal, position-dependent, or unmodeled contributions). No naturally occurring disturbance was observed in the pilot, so cancellation was demonstrated under controlled injection but not established for real-world confounds.
- Formalized the **three analysis families** (direct/single-stream, paired-differential, relational) as the paper's organizing structure, including a new architectural-contribution discussion.
- **Human 5+ subgroup result reframed**: presented as an exploratory worked example of the protocol's diagnostic value rather than a candidate observer-linked finding. New analysis shows the effect was formed by roughly equal, opposite-direction movement in Subject vs. PCS (not an isolated Subject-stream shift) — a configuration also compatible with retrospective selection for a large paired difference.
- Added **Section 4.4, Planned Preregistered Replication (Experiment 5)**, with OSF preregistration link and a secondary "permeability" individual-differences sub-study.
- Added an explicit **Ethics and Informed Consent** section: discloses that no IRB/ethics-committee review was obtained (independent researcher, no institutional affiliation) and states the study was conducted with reference to Belmont Report principles.
- Expanded **Limitations** (§5) from a shorter list to 11 subsections, adding QRNG provider heterogeneity/execution environment, finite-sample H_RS behavior, and contiguous stream-partitioning items.
- `paper/A-paired-delta-qrng-architecture.pdf` removed, replaced by `paper/PDP-Methodology-Paper.pdf`.
- Added `paper/PDP_Paper_to_Notebook_Reader_Guide.pdf`, mapping each paper section/claim to its source notebook, header, method, and result.

### Notebooks

**`Exp4_Notebook1_Zen_Paired_Control_Stream_Design_Validation.ipynb`** (66 → 87 cells):
- Corrected three-subtest audit-battery reconstruction with session-aware summaries and audit-failure session-uniqueness checks
- Scheduled-audit availability/missingness diagnostics
- Alternative ordering metrics across all conditions (contributor-clustered bootstrap)
- Same-position mutual-information sampling-hierarchy and batch-clustering sensitivity checks
- Baseline-offset synthetic-pipeline check and bootstrap seed-stability check
- Shuffle-null mechanism comparison
- Composition-conditioning checks split into two explicit tests: selection-adjusted tail probability vs. point-estimate sensitivity (documented 2+/3+/5+ threshold search)

**`Exp4_Notebook2_Zen_Temporal_Structure_Analysis.ipynb`** (76 → 78 cells):
- Added session-count descriptive pattern (mean paired ΔH_RS by condition)
- Added within-session Hurst-delta drift test (Human 5+ vs. Baseline interaction)
- Added hierarchy-preserving lagged-correlation-variance family check
- Removed standalone "PCS Randomness Validation" section; renamed "Single-Scale Hurst — Power Users (5+ Sessions)" → "Single-Scale Hurst — 5+ Sessions"

**New notebooks** (secondary/supporting analyses, per the Reader Guide):
- `Exp4_Interleaving_PhysicalHalf_AI_and_StreamLength_Audit.ipynb` — retrospective contiguous-vs-interleaved partition comparison, physical first-half-vs-second-half check prior to labeling, stream-length variance scan
- `Exp4_vs_Exp5Prescreen_Baseline_CrossDataset_Check.ipynb` — dated cross-dataset Baseline consistency check against the in-progress Exp5-prescreen data, kept separate to avoid conflating two structurally different Baseline statistics

### Repository

- `README.md` rewritten to match the revised manuscript title, framing, and section structure; adds the Exp5 preregistration link, the Ethics and Informed Consent statement, and documents all four analysis notebooks plus the Reader Guide.
