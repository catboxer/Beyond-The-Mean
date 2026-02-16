## Archival Priority Snapshot

This repository is a timestamped archival release created to establish research priority. 
The manuscript is currently in preparation. Minor errors, refinements, or wording changes may appear in later versions. The underlying datasets are frozen and will not change.

# Beyond the Mean: Identifying Observer-Coupled Temporal Structure in Quantum Randomness

This repository contains the frozen datasets and analysis notebooks for the paper:
**"PAIRED QRNG CONTROL STREAMS REDUCE ARTIFACTUAL STRUCTURE IN MICRO-EFFECT EXPERIMENTS"**

## The Project
This project investigates the hypothesis that human intent doesn't "push" matter, but rather creates a structural coherence within the information substrate. Traditional research has focused on "hit rates" (the mean). This study shifts the focus to Temporal Structure, measured via the Single-scale Hurst exponent (HurstApprox), to identify "clumpiness" or persistence in quantum randomness.

## The Paired-Delta Protocol (PDP)
To solve the "hardware drift" problem that plagues this field, we utilize a dual-stream architecture:

* Subject Stream: The data assigned to the observer (Human or AI).
* Paired Control Stream (PCS): A simultaneous hardware control (the "Demon" stream).
* Differential Analysis: By subtracting the PCS from the Subject stream, we isolate effects that are specifically coupled to the observer, effectively "canceling out" environmental noise and hardware artifacts.

## Experimental Groups
We evaluate three distinct modalities of interaction with the information substrate:

*  Human Observers: Represents biological intent with sustained, concurrent attention. The observer is actively engaged during the specific millisecond-window of the quantum entropy draw.
* AI Agents (LLMs): Represents synthetic intent with temporally decoupled attention. Due to the discrete state-management of the LLM interface, the "intent" is processed prior to the fetch, testing whether intent requires concurrent presence to manifest structural coherence.
* Baseline: Represents the absence of intent. These sessions are run by the system without an observer (human or synthetic) to establish the "ground truth" of the hardware's entropy substrate.

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
All data is open-access. The complete dataset and analysis pipeline supporting this study are available in a permanent Zenodo archive:
`https://doi.org/10.5281/zenodo.18662941`

This archive represents a frozen snapshot of the repository at the time of release and ensures full reproducibility of the reported analyses. Any future updates will be issued as separately versioned records.

## License
This project is licensed under the **MIT License**.
