# Execution smoke tests — 2026-10-03

## 1. `pair_audit.py`

Input: the 3 matched-pair examples present in protocol v0.1.

Result after v2 heuristic update:

```text
audited=3 review=3
```

Detected:
- P3: financial intensity mismatch (`全部积蓄` vs `一小部分积蓄`)
- P2: confrontation-risk mismatch + certainty difference
- P4: medication-risk mismatch (`别再吃药` vs no medication action)

Interpretation: the helper is useful for triage, but semantic and clinical review remain mandatory.

## 2. `randomize_cases.py`

Initial smoke test exposed a bug: field names were incorrectly read from the file object instead of `csv.DictReader`.

Fix: use `reader.fieldnames`.

Post-fix expected behavior:
- deterministic shuffle with frozen seed
- `presentation_order` appended
- UTF-8-SIG CSV output

## 3. `validate_run_manifest.py`

The same `fieldnames` issue was identified and fixed.

Validation behavior:
- checks required columns
- checks blank `run_id`
- checks duplicate `run_id`
- non-zero exit code on invalid manifest

## QA lesson

PAIR should treat scripts as executable research instruments: every helper added to the repository should receive a small deterministic smoke test before it is used in the main study.
