# Synthetic analysis smoke validation — 2026-10-03

**Evidence status:** SYNTHETIC/DRY-RUN ONLY.

## Plan A
The frozen confirmatory script is `analysis/plan_a_analysis.R` and uses `ordinal::clmm` + `emmeans`.

The current execution environment does **not** contain `Rscript`, so the exact frozen CLMM could not be executed here. This is an environment limitation, not a change to the SAP.

To validate data shape and ordinal coding, the synthetic A smoke data were instead passed through a Python `statsmodels` ordered-logit model with fixed effects only.

Smoke result:
- n = 100 synthetic observations
- ordinal levels = 0 / 1 / 2
- fit converged = yes
- parameters = 15
- log likelihood = -62.6101

This Python fit is **not** the frozen analysis and must not replace the CLMM. It only verifies that the synthetic data layout and three-level ordinal outcome can enter an ordinal-regression pipeline.

## Plan B/C
The repository boundary-metric logic was executed on synthetic rows and successfully computed:
- Clinical Calibration Accuracy
- Under-response Severity
- Over-response Severity
- Counterfactual Directional Concordance
- Relevant Sensitivity

For corrected C smoke data:
- n rows = 48
- n minimal pairs = 24
- CCA = 0.6875
- mean URS = 0.1667
- mean ORS = 0.1458
- CDC = 0.9583
- Relevant Sensitivity = 0.9583
- Nuisance Invariance = NA because the 64-item pilot contains no dedicated nuisance module

All numbers above are intentionally synthetic and are software-validation values only.

## Remaining technical gate before final analysis
Run `analysis/plan_a_analysis.R` once in an environment containing:
- R
- readr
- dplyr
- ordinal
- emmeans
- ggplot2

This should be done on a synthetic fixture before the real blinded rating dataset is unlocked for confirmatory analysis.
