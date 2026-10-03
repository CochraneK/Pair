# PAIR publication analysis layer

This directory contains the manuscript-facing analysis pipeline.

## Real-data scripts
- `plan_a_primary_clmm.R` — preregistration-aligned cumulative-link mixed model for Plan A.
- `plan_bc_family_aware_analysis.py` — item-first / family-aware B/C calibration analysis.
- `make_publication_figures.py` — manuscript figure generation from frozen analysis tables.
- `REAL_DATA_CONTRACT.md` — required columns and merge contracts.

## Simulation rehearsal
A separate local rehearsal package was generated on 2026-10-03 using `SYNTHETIC_REALISTIC_SIMULATION` data to test the end-to-end paper pipeline. It produced:
- Plan A rating-distribution figure;
- paired binary sensitivity forest;
- repeat-stability figure;
- failure-profile heatmap;
- Plan B CCA-versus-direction and axis-level figures;
- PAIR-C CCA-versus-direction, URS-versus-ORS, axis-level CCA, and signed-residual figures.

The exact synthetic values are documented under `manuscript/simulation/` and must never be reported as empirical product/model performance.

## Statistical boundary
Repeated model generations estimate stochasticity; they do not create additional independent clinical scenarios. Plan B/C interpretation must collapse repeats at item level and retain scenario family as the meaningful clinical replication unit.
