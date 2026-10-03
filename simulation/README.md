# PAIR realistic synthetic simulation v1

**Status: `SYNTHETIC_REALISTIC_SIMULATION`**

This directory records a full synthetic rehearsal of the frozen A/B/C study pipeline.

## Hard boundary
These files are **not empirical results** from DeepSeek, Doubao, Kimi, Qwen, Yuanbao, or any API endpoint. They are realistic synthetic fixtures generated with fixed random seed `202610031646`.

Permitted uses:
- pipeline validation
- statistics rehearsal
- power/precision exploration
- figure/table/manuscript dry-run
- stress-testing analysis code

Not permitted:
- reporting as observed model performance
- describing simulated clinician ratings as real clinician ratings
- replacing the preregistered real data collection

## Scale
- Plan A: 960 simulated product responses
- Plan A raw simulated ratings: 1,920 rows (2 raters)
- Plan B: 324 simulated product responses
- Plan B raw simulated policy ratings: 648 rows
- Plan C: 576 simulated API-config responses
- Plan C raw simulated policy ratings: 1,152 rows
- Total simulated model outputs: 1,860

## Simulation logic
### Plan A
Product-specific weak priors for recognition, non-reinforcement, urgency/resources, reinforcement risk, control over-pathologization, and run-to-run stability were combined with SIPS-domain difficulty and item/model latent effects.

### Plan B
The provisional `[L,U]` policy intervals were treated as assumed clinical targets. Each product received a model-specific policy bias, stochasticity and sensitivity to conviction, insight and behavioral-risk changes.

### Plan C
The four-axis pilot was simulated with model-specific policy sensitivity. Evidence/plausibility uses a **negative target direction**: stronger plausible external evidence can appropriately reduce psychiatric escalation. This tests directional calibration rather than merely high intervention intensity.

## Public-evidence constraint
Priors were intentionally weak because public 2026 evaluations are task-dependent and sometimes disagree. The simulation used current medical and mental-health evaluations only to keep the synthetic behavior within plausible ranges; no published result directly measures these exact PAIR prompts.

Key sources include:
- Huang et al., Frontiers in Public Health 2026: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2026.1850095/full
- Arnaiz-Rodriguez et al., JMIR Mental Health 2026: https://mental.jmir.org/2026/1/e88435
- Transluce Mental Health Behavior Report 2026: https://behaviors.transluce.org/mental-health
- Sterna et al., arXiv:2608.13017: https://arxiv.org/abs/2608.13017

Tencent Yuanbao lacked directly comparable psychosis/clinical evaluation in the targeted search, so its prior was deliberately neutral with larger uncertainty.

## Canonical external artifact
The full local simulation package also contains run-level responses, raw rater rows, prior tables, source tables and a formatted XLSX workbook. Keep this repo summary separate from future `REAL` results.
