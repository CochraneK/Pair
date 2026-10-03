# Dry-run: PAIR-C pilot structure validation

**Date:** 2026-10-03

This is a structural QA result, **not a clinical-validation result and not a model-performance result**.

Command concept:

```bash
python scripts/validate_c_pilot.py routes/C/PILOT_BLUEPRINTS_64.csv
```

Observed dry-run output:

```text
rows=64 families=8 pairs=32
errors=0 warnings=0
```

Validator checks:
- exactly 8 scenario families expected for this pilot draft
- 64 rows expected
- each family contains all 4 core axes
- every family × axis has 2 levels
- pair metadata preserves `fixed_context`
- lexical similarity threshold defaults to 0.75

What this does **not** establish:
- clinical validity
- manipulation validity
- realism
- acceptable intervention interval `[L,U]`
- absence of clinically meaningful second-axis confounding

Those require clinician review under GitHub Issue #5.
