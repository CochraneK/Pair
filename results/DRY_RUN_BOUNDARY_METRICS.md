# DRY RUN — boundary metrics

**This is not an empirical research result.**

Purpose: verify that the Plan B/C metric pipeline produces sensible outputs before any clinical/model data are collected.

Synthetic fixture: `tests/boundary_metrics_fixture.csv`

Command:

```bash
python scripts/boundary_metrics.py tests/boundary_metrics_fixture.csv --out results/boundary_metrics_fixture.json
```

Observed synthetic-test output:

```json
{
  "n_rows": 8,
  "n_pairs": 4,
  "CCA": 0.75,
  "mean_URS": 0.25,
  "mean_ORS": 0.125,
  "CDC_all_pairs": 0.75,
  "Relevant_Sensitivity": 0.6666666666666666,
  "Nuisance_Invariance_strict": 1.0
}
```

## What the fixture intentionally contains

- one correctly calibrated conviction shift
- one missed insight shift (under-response)
- one behavioral-risk shift that overshoots (over-response)
- one stable nuisance pair

The output therefore demonstrates that the code distinguishes:
- calibrated vs non-calibrated responses
- under-response vs over-response
- relevant sensitivity
- nuisance invariance

## Pass status

✅ Smoke test passed on 2026-10-03.

Next step is not to interpret these numbers. Replace the synthetic fixture with clinician-annotated pilot data after the rubric and items are approved.