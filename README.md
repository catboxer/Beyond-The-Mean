 # Beyond the Mean: A Paired-Control Architecture for QRNG Experiments                                                               
                                                                                     
  This repository contains the frozen datasets and analysis notebooks supporting the 
  manuscript:                                                                        
                                                                                     
  **“Paired QRNG Control Streams Reduce Artifactual Structure in Observer–Randomness 
  Experiments.”**                                                                    
                                                                                     
  The repository provides a reproducible implementation of the Paired-Delta Protocol 
  (PDP) and all analyses reported in the paper.                                      
                                                                                     
  ---                                                                                
                                                                                     
  ## Project Overview                                                                
                                                                                     
  This project evaluates an experimental architecture designed to distinguish        
  stream-specific effects from hardware- or environment-level variation in studies   
  involving quantum random number generators (QRNGs).                                
                                                                                     
  Traditional QRNG experiments often rely on single-stream analyses (e.g., hit       
  rates). When expected deviations are small relative to system noise, it can be     
  difficult to separate potential observer-linked patterns from drift or             
  environmental artifacts.                                                           
                                                                                     
  The Paired-Delta Protocol embeds a simultaneous control stream within each QRNG    
  call, enabling within-call subtraction and common-mode rejection.                  
                                                                                     
  Temporal ordering is assessed using a single-scale Hurst exponent computed at the  
  block level.                                                                       
                                                                                     
  The primary contribution is methodological: an architecture in which deviations    
  must survive hardware control, cross-condition comparison, and temporal            
  diagnostics.                                                                       
                                                                                     
  ---                                                                                
                                                                                     
  ## The Paired-Delta Protocol (PDP)                                                 
                                                                                     
  Each QRNG call generates two simultaneous 150-bit streams derived from a single    
  physical draw:                                                                     
                                                                                     
  - **Subject Stream** – Assigned to the experimental condition                      
  - **Paired Control Stream (PCS)** – Simultaneous unattended hardware control       
  - **Paired Difference (Δ)** – Stream-level metrics computed as Subject − PCS       
                                                                                     
  Because both streams originate from the same physical event, shared hardware or    
  environmental fluctuations affect both equally and cancel under subtraction.       
                                                                                     
  ---                                                                                
                                                                                     
  ## Experimental Conditions                                                         
                                                                                     
  The study evaluates three conditions:                                              
                                                                                     
  - **Human Participants** – Interactive sessions involving voluntary engagement     
  - **AI Agent Condition** – An LLM-driven interface interacting with the same       
  experimental framework                                                             
  - **Baseline Condition** – Fully automated execution without agent involvement     
                                                                                     
  These conditions allow comparison of stream-level behavior across biological,      
  artificial, and unattended execution contexts.                                     
                                                                                     
  ---                                                                                
                                                                                     
  ## Repository Contents                                                             
                                                                                     
  This repository contains:                                                          
                                                                                     
  1. **Design Validation Notebook** – Documentation of QRNG labeling logic and       
  hardware audit procedures                                                          
  2. **Analysis Notebook** – Statistical analyses including paired-delta             
  computation, Hurst exponent calculation, permutation tests, and hierarchical       
  modeling                                                                           
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
                                                                                     
  Large Language Models (LLMs), including systems developed by OpenAI, Anthropic,    
  and Google, were used as research assistance tools during manuscript preparation   
  and code refinement. These systems supported drafting, editing, statistical        
  discussion, and documentation organization. All experimental design decisions,     
  analyses, interpretations, and final manuscript content were reviewed and approved 
  by the author.                                                                     
                                                                                     
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
                                                                                     
  This Zenodo record represents a frozen snapshot of the repository at the time of   
  manuscript submission and ensures full reproducibility of the reported analyses.   
                                                                                     
  ---                                                                                
                                                                                     
  ## License                                                                         
                                                                                     
  This project is licensed under the **MIT License**.                                
                                                                                     

⏺ Here is the updated README with only the two sections that changed:

  # Beyond the Mean: A Paired-Control Architecture for QRNG Experiments

  This repository contains the frozen datasets and analysis notebooks supporting the
  manuscript:

  **"Paired QRNG Control Streams Reduce Artifactual Structure in Observer–Randomness 
  Experiments."**

  The repository provides a reproducible implementation of the Paired-Delta Protocol
  (PDP) and all analyses reported in the paper.

  ---

  ## Project Overview

  This project evaluates an experimental architecture designed to distinguish
  stream-specific effects from hardware- or environment-level variation in studies
  involving quantum random number generators (QRNGs).

  Traditional QRNG experiments often rely on single-stream analyses (e.g., hit
  rates). When expected deviations are small relative to system noise, it can be
  difficult to separate potential observer-linked patterns from drift or
  environmental artifacts.

  The Paired-Delta Protocol embeds a simultaneous control stream within each QRNG
  call, enabling within-call subtraction and common-mode rejection.

  Temporal ordering is assessed using a single-scale Hurst exponent computed at the
  block level.

  The primary contribution is methodological: an architecture in which deviations
  must survive hardware control, cross-condition comparison, and temporal
  diagnostics.

  ---

  ## The Paired-Delta Protocol (PDP)

  Each QRNG call generates two simultaneous 150-bit streams derived from a single
  physical draw:

  - **Subject Stream** – Assigned to the experimental condition
  - **Paired Control Stream (PCS)** – Simultaneous unattended hardware control
  - **Paired Difference (Δ)** – Stream-level metrics computed as Subject − PCS

  Because both streams originate from the same physical event, shared hardware or
  environmental fluctuations affect both equally and cancel under subtraction.

  ---

  ## Experimental Conditions

  The study evaluates three conditions:

  - **Human Participants** – Interactive sessions involving voluntary engagement
  - **AI Agent Condition** – An LLM-driven interface interacting with the same
  experimental framework
  - **Baseline Condition** – Fully automated execution without agent involvement

  These conditions allow comparison of stream-level behavior across biological,
  artificial, and unattended execution contexts.

  ---

  ## Repository Contents

  This repository contains:

  1. **Design Validation Notebook** – Documentation of QRNG labeling logic and
  hardware audit procedures
  2. **Analysis Notebook** – Statistical analyses including paired-delta computation,
  Hurst exponent calculation, permutation tests, and hierarchical modeling
  3. **Paired-Delta Null Validation Notebook** – Empirical validation of the
  paired-delta null distribution and common-mode structure test; added in response to
  peer review
  4. **Artifact Injection Notebook** – Positive control demonstrating that
  common-mode artifacts cancel under paired subtraction while stream-specific effects
  survive; added in response to peer review
  5. **Dual Analysis Notebook** – Side-by-side comparison of direct subject-stream
  analysis versus paired-delta analysis across cohorts; added in response to peer
  review
  6. **data/** – Frozen CSV datasets with SHA-256 fingerprints for verification

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

  Large Language Models (LLMs), including systems developed by OpenAI, Anthropic, and
  Google, were used as research assistance tools during manuscript preparation and
  code refinement. These systems supported drafting, editing, statistical discussion,
  and documentation organization. All experimental design decisions, analyses,
  interpretations, and final manuscript content were reviewed and approved by the
  author.

  ---

  ## Reproducibility

  To reproduce the analyses:

  1. Clone the repository
  2. Install Python 3.x with `pandas`, `scipy`, `pymc`, and `arviz`
  3. Run the **Design Validation** notebook
  4. Run the **Analysis** notebook
  5. Run the three validation notebooks: **Paired-Delta Null Validation**, **Artifact
  Injection**, and **Dual Analysis**

  **Running notebooks without Google Drive**

  The notebooks load data from Google Drive by default. To run them without a
  personal Drive setup, replace the Drive path variables at the top of each notebook
  with the following:

  ```python
  import urllib.request, os

  ZENODO_BASE = "https://zenodo.org/records/18703829/files"
  for fname in [
      "Frozen_Blocks_2026-02-10_195735.csv",
      "Frozen_Sessions_2026-02-10_195735.csv",
      "Frozen_Participants_2026-02-10_195735.csv",
      "Frozen_Audits_2026-02-10_195735.csv"
  ]:
      if not os.path.exists(fname):
          urllib.request.urlretrieve(f"{ZENODO_BASE}/{fname}", fname)

  FROZEN_BLOCKS_PATH       = "Frozen_Blocks_2026-02-10_195735.csv"
  FROZEN_SESSIONS_PATH     = "Frozen_Sessions_2026-02-10_195735.csv"
  FROZEN_PARTICIPANTS_PATH = "Frozen_Participants_2026-02-10_195735.csv"
  FROZEN_AUDITS_PATH       = "Frozen_Audits_2026-02-10_195735.csv"

  This downloads the frozen dataset directly from Zenodo into the Colab session.

  ---
  Data Availability

  All datasets and analysis code are publicly archived at:

  https://doi.org/10.5281/zenodo.18703829

  This Zenodo record represents a frozen snapshot of the repository at the time of
  manuscript submission and ensures full reproducibility of the reported analyses.

  ---
  License

  This project is licensed under the MIT License.
  ```
