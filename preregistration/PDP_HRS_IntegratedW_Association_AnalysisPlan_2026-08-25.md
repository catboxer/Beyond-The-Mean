# Prospectively Specified Follow-Up Analysis of Exploratory PDP Findings

**Status:** Analysis plan frozen before execution  
**Date:** 2026-08-25  
**Project:** Paired-Delta Protocol (PDP)  
**Analysis type:** Prospectively specified follow-up to exploratory findings

## 1. Purpose

Earlier exploratory analyses of the Paired-Delta Protocol identified two findings that may or may not reflect the same underlying statistical phenomenon:

1. a positive paired ordering-structure difference, defined as Subject-stream minus Paired Control Stream (PCS) single-scale H_RS; and
2. reduced variability in local Subject–PCS H_RS coupling across temporal window sizes.

The second finding was initially examined at individual window sizes. Subsequent exploratory work suggested that the more transportable quantity may be the integrated amount of Baseline-standardized relational variance narrowing across window size, rather than narrowing at one particular W.

The present analysis asks whether these two quantities covary within participants.

The central question is:

> **Do participants with a larger positive Subject-minus-PCS H_RS difference also show greater integrated relational variance narrowing across temporal scales, beyond any association expected mechanically from the same paired-stream data structure?**

This analysis is prospectively specified before examining the association itself. It does not convert the underlying exploratory findings into confirmatory evidence.

## 2. Datasets

The analysis will be performed separately in:

- **Experiment 4 Human data**, using the full eligible Human population.
- **Experiment 5 prescreen Human data**, using the full eligible pre-specified comparison population available for the exploratory cross-dataset analysis.

The two datasets will not be pooled for the primary analysis.

Baseline data from each experiment will be used to construct dataset-specific null distributions and matched pseudo-participants.

## 3. Primary participant-level variables

### 3.1 Differential H_RS

For each participant, define the participant-level paired ordering difference as:

D_H = mean(H_RS,Subject - H_RS,PCS)

where the average is taken across that participant's eligible blocks/sessions under the same aggregation rule used in the prior paired H_RS analyses.

Positive values indicate higher Subject-stream H_RS relative to PCS.

### 3.2 Integrated relational variance narrowing

For each eligible window size W, local Subject–PCS H_RS correlations will be calculated using the previously fixed relational procedure.

At each W, the Human participant's local-coupling variance will be standardized against the corresponding Baseline reference distribution to produce a standardized departure Z_W.

Negative Z_W indicates narrower local-coupling variance than expected under Baseline.

The integrated narrowing statistic is defined prospectively as:

A_W = (1/K) * sum over W in eligible set of max(0, -Z_W)

where:

- the eligible set is the complete eligible window-size set for that dataset;
- K is the number of eligible window sizes;
- only narrowing contributes positively to A_W;
- no individual W will be selected on the basis of the Human result.

Larger A_W indicates a greater total amount of Baseline-standardized relational variance suppression across temporal scales.

The same integrated-W definition used in the preceding exploratory analysis will be retained without modification.

## 4. Primary hypothesis

The primary exploratory follow-up hypothesis is:

> **Participants with larger positive Differential H_RS will tend to show greater integrated W-space relational variance narrowing.**

The primary association statistic will be **Spearman's rank correlation** between D_H and A_W.

Spearman correlation is primary because no linear relation is assumed.

## 5. Secondary association

Pearson correlation between D_H and A_W will be reported as a secondary descriptive analysis.

No transformation, threshold, subgroup boundary, polynomial term, piecewise regression, or nonlinear model will be introduced after viewing the result.

## 6. Baseline mechanical-association control

Because D_H and A_W are both derived from paired Subject/PCS H_RS values, an association between them could arise mechanically even in the absence of a condition-specific phenomenon.

To evaluate this, matched Baseline pseudo-participants will be constructed.

For each Human participant, Baseline sessions will be sampled to reproduce that participant's eligible session-count structure. The same calculations used for the Human data will then be applied to each pseudo-participant to obtain D_B and A_W,B.

A pseudo-Human group will contain the same number of pseudo-participants and the same participant-level session-count structure as the observed Human group.

For each pseudo-group, the Spearman correlation between D_B and A_W,B will be calculated.

The resulting Baseline distribution will provide the empirical null for the Human association.

The Human association will be evaluated by asking how often matched Baseline pseudo-groups produce an association at least as strong in the prespecified positive direction.

## 7. Resampling

The target number of matched Baseline pseudo-group repetitions is **5,000**.

If computational limitations prevent 5,000 repetitions, a minimum of 1,000 will be used for an initial decision analysis, with the exact number reported. Any result near a conventional decision boundary will be rerun with at least 5,000 repetitions before interpretation.

The resampling count will not be increased or decreased on the basis of whether the Human result appears favorable.

## 8. Full-population analysis

The **full eligible Human population** is primary.

Participants will receive equal weight in the participant-level association analysis regardless of the number of sessions contributed.

The analysis will not search retrospectively across minimum-session-count thresholds.

## 9. Repeat-participant / 5+ sensitivity analysis

A 5+ session subgroup analysis may be reported only as a **secondary descriptive sensitivity analysis**, because repeated-participant subgroups were already implicated in prior exploratory findings.

It will not redefine the primary result and will not be used to rescue a null full-population finding.

## 10. Cross-dataset interpretation

Experiment 4 and Experiment 5 will be analyzed independently.

The following outcomes will be distinguished:

### Pattern A: association present in both datasets and stronger than Baseline expectation

This would support the exploratory hypothesis that positive Differential H_RS and integrated relational variance narrowing may be statistically linked expressions of a common paired-stream phenomenon.

It would not establish a physical or causal mechanism.

### Pattern B: association present in one dataset only

This would indicate limited cross-dataset transport and would argue against treating the two findings as a general coupled signature.

### Pattern C: association present in Human but comparable to Baseline mechanical association

This would indicate that the relationship can be explained by the shared mathematical/data structure of the two quantities and should not be interpreted as Human-specific.

### Pattern D: no clear association

This would support treating Differential H_RS and relational variance narrowing as separate exploratory observations rather than components of one statistical signature.

## 11. No post-result modifications

After the Human association is examined, the following will not be changed for this analysis:

- the definition of Differential H_RS;
- the definition of integrated W narrowing;
- the eligible W range;
- the participant-equal weighting rule;
- Spearman correlation as the primary association;
- the Baseline pseudo-participant construction;
- the directional hypothesis;
- the full-population primary analysis;
- the status of the 5+ analysis as secondary.

Any additional analyses motivated by the observed result will be labeled explicitly as new exploratory follow-ups.

## 12. Interpretation boundary

This analysis is a **prospectively specified follow-up to exploratory findings**.

It does not constitute an independent replication because the candidate variables were identified through prior exploration of these same datasets.

A positive result would justify prospective testing of the joint pattern in a new preregistered dataset.

A null result would argue against combining positive Differential H_RS and integrated relational variance narrowing into a single PDP signature.

## 13. Planned reporting

The final report will include, for each dataset:

- number of eligible Human participants;
- participant session-count distribution;
- Spearman r_s between D_H and A_W;
- Pearson r as secondary;
- empirical Baseline-null p-value;
- Baseline pseudo-group correlation distribution summary;
- scatterplot of participant-level D_H versus A_W;
- 5+ sensitivity analysis, if reported;
- a clear statement that the analysis was prospectively specified after discovery of the component findings but before examination of their association.

## 14. Addendum — 2026-09-06: Results, Study 1 / Exp4

The participant-level Spearman correlation between D_H and A_W (Sections 3-9) was run on Study 1 / Experiment 4 data, at the Section 7 floor for an initial decision analysis (1,000 Baseline-calibration draws, 1,000 matched-pseudo-group repetitions per test). No result below is near a decision boundary, so none required escalation to the 5,000-repetition target. Only Experiment 4 is reported here; Experiment 5-prescreen has not yet been run through this analysis, so Section 10's cross-dataset Patterns A/B cannot be evaluated yet.

**Eligible population:** Human(all) = 121 participants (4,737 blocks); Human5+ = 3 participants (840 blocks); Baseline = 3 participants (3,090 blocks).

**D_H, descriptive:** Human(all) mean = +0.00034, median = +0.00137 (N=121). Human5+ mean = +0.00644, median = +0.00803 (N=3).

**A_W, descriptive:** Human(all) mean = 0.39414, median = 0.32350 (N=121). Human5+ mean = 1.13746, median = 1.11330 (N=3).

### Primary — Human(all), Section 8

| | value |
|---|---|
| Spearman r_s (D_H, A_W) | +0.0055 (N=121) |
| Baseline-matched null | mean = +0.0992, SD = 0.0907 |
| One-sided empirical p | 0.8510 |

**Pattern D** (Section 10): no clear association.

### Secondary — Human5+, Section 9

| | value |
|---|---|
| Spearman r_s (D_H, A_W) | −0.5000 (N=3) |
| Baseline-matched null | mean = +0.0651, SD = 0.7028 |
| One-sided empirical p | 0.8441 |

Wrong-signed relative to the plan's positive-direction hypothesis (Section 4). Per Section 9, this does not redefine the primary result. At N=3, this is not powered to distinguish "no coupling" from "no detectable coupling."

### Secondary — within-participant, session-level

Eligible: 6/121 participants with 3 or more sessions carrying a defined A_W_session (39 sessions pooled).

| | value |
|---|---|
| Spearman r_s (dD_H, dA_W), order-detrended | +0.0627 |
| Pearson r (secondary/descriptive) | −0.0157 |
| Within-participant permutation null | one-sided p = 0.3980 |
| Baseline-mechanical null | one-sided p = 0.5450 |

**Pattern D:** no clear within-participant association, though a null here cannot distinguish "no coupling" from insufficient within-participant variability to detect it, and N=6 is small.

An exploratory, non-confirmatory follow-up restricted to the two non-PI Human5+ participants' own sessions (N=2 participants, 10 sessions) found no relationship (Spearman ρ=−0.30, p=0.40 raw; ρ=−0.25 after order-detrending, uninterpretable at N=2) — descriptive only, not part of the registered tests.

### Reading

All sub-tests land on Pattern D: no clear association between D_H and A_W at any level tested. This bears on whether the second finding described in Section 1 (reduced local Subject-PCS H_RS coupling variability) could be a mechanical byproduct of the first (the paired ordering-structure difference, D_H) rather than an independent pattern — if that mechanism were operating, D_H and A_W should covary positively within the group carrying both effects. Instead the relationship within Human5+ is negative and indistinguishable from its own null. This does not prove the two findings are unrelated (N=3 has essentially no power) but gives no support to treating them as the same underlying artifact.

This also bears on the H_RS estimator itself: D_H and A_W are both derived from the same single-scale H_RS metric, so a positive correlation between them would also have been consistent with a shared estimator-level artifact rather than two independent findings. The null result gives no support to that explanation either.

No claim is made that either underlying finding is itself real or artifactual — this addendum only reports whether D_H and A_W covary. Per Section 12, this is a follow-up to exploratory findings, not an independent replication, since both candidate variables were identified by exploring the same dataset.
