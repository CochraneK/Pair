# Script smoke test — 2026-10-03

Executed locally against the repository artefacts.

## pair_audit.py
Input: `benchmark/pair_audit_input_examples.csv`

Result:
- 3 pairs audited
- 3/3 flagged for human review after intensity-aware QA revision

## randomize_cases.py
Command:
```bash
python scripts/randomize_cases.py benchmark/pair_audit_input_examples.csv --out /tmp/randomized.csv --seed 20261003
```

Result:
- 3 rows written
- reproducible presentation order generated

## validate_run_manifest.py
Command:
```bash
python scripts/validate_run_manifest.py schemas/run_manifest_template.csv
```

Result:
- template parsed successfully
- 0 rows
- 0 duplicate run IDs
- 0 blank run IDs

## Syntax
`python -m py_compile` passed for:
- `scripts/pair_audit.py`
- `scripts/randomize_cases.py`
- `scripts/validate_run_manifest.py`

These checks confirm the current helper scripts start and operate on the example/template artefacts. They do not validate clinical correctness or the future full dataset.
