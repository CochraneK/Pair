# STATUS

**Updated:** 2026-10-03

## Overall

🟡 **A/B/C parallel preparation is complete. The project is now waiting on real research inputs, not more conceptual expansion.**

Operational recommendation:

> **A = guaranteed paper; B = active enhancement; C = prepared next-study/benchmark track.**

## Completed

- [x] Public collaboration-safe GitHub repository initialized
- [x] Original protocol reconstructed and audited
- [x] Canonical handoff assembled
- [x] A/B/C decision tree assembled
- [x] APP consumer-product SOP assembled
- [x] API-ready architecture assembled
- [x] Evolvent/BenchRouter adapter skeleton assembled
- [x] Single-file meeting handbook added
- [x] Key 2025–2026 literature refreshed
- [x] CHART precheck completed
- [x] Protocol-diff memo completed
- [x] Statistics-method review completed
- [x] Pair-audit rules created
- [x] Pair-audit helper script created and QA-tested
- [x] Three example pairs from protocol v0.1 audited
- [x] APP environment manifest template created
- [x] Case/run/rating schemas created
- [x] Reproducible randomizer + run-manifest validator created
- [x] Public-repository sensitive-data rule established
- [x] **Plan A advanced to protocol-ready + candidate SAP + results shell**
- [x] **Plan B advanced to 36-prompt pilot-ready design + candidate SAP + results shell**
- [x] **Plan C advanced to benchmark/pilot-ready design + core metrics/results shell**
- [x] Plan C novelty narrowed after 2026 SIM-VAIL/Nature Medicine overlap
- [x] Boundary metrics implemented: CCA / URS / ORS / CDC / Relevant Sensitivity / Nuisance Invariance
- [x] Boundary-metrics synthetic smoke test passed
- [x] Parallel route executive result written: `routes/EXECUTIVE_RESULT.md`

## Current human/data gates

- [ ] **Full original prompt set:** available protocol v0.1 contains only 3 example matched pairs, not the complete 80 psychotic + 80 controls
- [ ] **HG1 formal route decision:** team records whether manuscript path is A or B; C is recommended as separate track unless project is explicitly replaced
- [ ] Clinical item approval
- [ ] Clinician acceptable-policy/rubric approval
- [ ] Ethics determination / exemption confirmation
- [ ] Preregistration freeze
- [ ] Main APP collection
- [ ] Clinical rating
- [ ] Frozen statistical analysis
- [ ] Submission-target decision

## What to do next — priority order

### 1. Import complete original 160-prompt set
Then run:

```bash
python scripts/pair_audit.py benchmark/cases_full.csv --out results/pair_audit.csv
```

Clinicians review every flagged pair.

### 2. In parallel, instantiate Plan B pilot
Use 6 clinician-approved base families:

`6 families × 3 axes × 2 variants = 36 prompts`

Axes:
- conviction
- insight
- behavioral risk

Clinicians assign acceptable policy interval `[L,U]`.

### 3. Pilot first, then freeze
If Plan-B item validation and model pilot are interpretable, include Aim 2. Otherwise continue as Plan A without damage.

### 4. Keep Plan C prepared but separate
Before Plan C becomes a real study:
- narrow formal novelty/scoping review
- explicit team approval that RQ changes
- contribution/authorship boundary
- clinician ground-truth pilot

## Current route files

- `routes/A/PROTOCOL_READY.md`
- `routes/A/SAP_AND_RESULTS_TEMPLATE.md`
- `routes/B/PROTOCOL_AND_PILOT_READY.md`
- `routes/B/SAP_AND_RESULTS_TEMPLATE.md`
- `routes/C/BENCHMARK_AND_PILOT_READY.md`
- `routes/C/METRICS_AND_RESULTS_TEMPLATE.md`
- `routes/ROUTE_COMPARISON.md`
- `routes/EXECUTIVE_RESULT.md`

## Result boundary

There are currently **no real model-performance results**. `results/DRY_RUN_BOUNDARY_METRICS.md` is synthetic pipeline validation only.