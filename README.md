# SpaceMed 2026

Welcome to my repository dedicated to biomedical data analysis, neuroimaging pipelines, and projects developed during the Germany semster of Erasmus Mundus Joint Master in Space Medicine. 

## 👩‍🔬 About Me
Hi, I'm **Sammy (Shan-Shan) Chen** 👋 
*   **Current Role:** M.Sc. Student specializing in **Space Medicine**.
*   **Background:** Licensed Occupational Therapist (B.Sc., National Taiwan University) | Clinical Neuro-rehabilitation & Human Performance.
*   **Contact:** 📧 [shan-shan.chen@charite.de](mailto:shan-shan.chen@charite.de)

---

## Core Project: `spacemed` Python Package
`spacemed` is a custom-built Python package designed for automated processing, feature extraction, and analysis of physiological signal data (e.g., medical pulse and hemodynamic signals). 

### Pipeline & Core Functions

| Function | Input/Parameters | Description |
| :--- | :--- | :--- |
| `readPulse` | `file_name` | Efficiently parses raw physiological data (CSV) and extracts time-series matrices (`time`, `absorption`). |
| `findPeaks` | `time`, `absorption` | Applies digital signal processing (DSP) algorithms to identify local maxima (physiological peaks) and filter artifacts. |
| `calHR` | `time`, `peaks` | Quantifies instantaneous heart rate metrics based on inter-beat intervals (IBI). |
| `plotHR` | `hr` | Generates standardized, publication-ready visual plots for physiological timelines. |
| `fmriCross` | `input_sig`, `output_fmri`, `voxel_num` | Computes mathematical **cross-correlation and time lags** between peripheral physiological signals and fMRI voxel time series (crucial for BOLD signal artifact removal and coupling analysis). |

*Current Release Version: `0.0.3`*

---

## Parallel Research Projects

### Cardiorespiratory Dynamics: ECG Signal Processing
*   **Overview:** Developed a complete end-to-end processing pipeline to transform noisy, raw ECG voltage signals into clean, analyzed data structures.
*   **My Technical Contribution:** Responsible for the entire technical implementation, including pipeline engineering, digital signal processing (DSP), and the complete Python notebook development using `Neurokit2` to extract Heart Rate Variability (HRV) indices.
*   **Team Credits:** Team members contributed to the literature review and written research proposal report.

### Advanced Biostatistics & Predictive Modeling (R Framework)
*   **Overview:** A collaborative comprehensive analytics project examining multidimensional clinical datasets, patient baseline demographics, and hospital readmission risk factors. 
*   **Team Credits:** Jointly developed by Alice, Kseniia, and Me.
*   **My Specific Contribution (Task 5):** Independently designed and executed the Advanced Readmission Prediction Pipeline.
    *   Implemented a **Predictive Mean Matching (PMM)** imputation pipeline via the `mice` package to handle sparse physiological data.
    *   Engineered a step-wise hierarchical model testing framework, conducting **Likelihood Ratio Tests (LRT)** and diagnosing multicollinearity via **VIF** profiles.
    *   Deployed a **Random Forest** classifier, executed Out-Of-Bag (OOB) error convergence profiling, and tuned optimization parameters (`mtry`).
    *   Optimized clinical classification thresholds using **Youden's Index** and benchmarked final models via **ROC/AUC comparisons** (using `pROC`).
