# Scripts

## pair_audit.py
Heuristic QA for matched psychotic/control prompts.

Expected input columns:
- `pair_id`
- `psychotic_prompt`
- `control_prompt`

```bash
python scripts/pair_audit.py benchmark/cases_full.csv --out results/pair_audit.csv
```

Flags:
- medication / financial / confrontation / self-harm / harm-to-others risk mismatch
- selected within-category intensity mismatches
- certainty differences for human review
- >25% character-length imbalance

This is **not** a clinical validator. Clinicians must approve final pairs.

## randomize_cases.py
Creates a reproducible presentation order.

```bash
python scripts/randomize_cases.py benchmark/cases_full.csv --out benchmark/cases_ordered.csv --seed 20261003
```

## validate_run_manifest.py
Checks required columns, duplicate `run_id`s and blank `run_id`s.

```bash
python scripts/validate_run_manifest.py data/run_manifest.csv
```
