# STATUS

**Updated:** 2026-10-03

## Overall

🟡 **A/B/C parallel preparation is complete. Plan C has now advanced from concept-ready to clinician-review-ready.**

Operational recommendation:

> **A = guaranteed paper; B = active enhancement; C = prepared next-study/benchmark track, now with a concrete 64-item clinician-review pilot.**

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
- [x] Plan C novelty narrowed after 2026 SIM-VAIL / Safe-Psych / ClinDet-Bench / K-Bench overlap
- [x] Narrow Plan C novelty/scoping review written: `routes/C/NOVELTY_SCOPING_REVIEW_2026-10-03.md`
- [x] Plan C clinical construction ontology v0.1 written
- [x] **64 candidate Plan-C pilot prompts generated:** 8 families × 4 axes × 2 levels
- [x] Clinician review schema created with raw reviewer-specific `[L,U]`
- [x] Plan C pilot freeze checklist created
- [x] Plan C structural validator created and dry-run passed: 64 rows / 8 families / 32 pairs / 0 structural errors / 0 similarity warnings
- [x] Boundary metrics implemented: CCA / URS / ORS / CDC / Relevant Sensitivity / Nuisance Invariance
- [x] Boundary-metrics synthetic smoke test passed
- [x] Plan C clinician-review gate opened: GitHub Issue #5
- [x] Parallel route executive result written: `routes/EXECUTIVE_RESULT.md`

## Current human/data gates

### Original A/B track
- [ ] **Full original prompt set:** available protocol v0.1 contains only 3 example matched pairs, not the complete 80 psychotic + 80 controls
- [ ] **HG1 formal route decision:** team records whether manuscript path is A or B
- [ ] Clinical item approval
- [ ] Clinician acceptable-policy/rubric approval
- [ ] Ethics determination / exemption confirmation
- [ ] Preregistration freeze
- [ ] Main APP collection
- [ ] Clinical rating
- [ ] Frozen statistical analysis
- [ ] Submission-target decision

### Plan C track
- [ ] **HG-C1 clinician review of ontology + 64-item pilot:** https://github.com/CochraneK/Pair/issues/5
- [ ] clinician manipulation-success check
- [ ] clinician `[L,U]` interval annotation
- [ ] revision/adjudication to C-pilot v0.2
- [ ] explicit team approval that C is a distinct research question/project
- [ ] contribution/authorship boundary
- [ ] ethics determination
- [ ] formal narrow novelty review before preregistration
- [ ] fixed-model pilot collection

## What to do next — priority order

### 1. Send Plan C pilot to clinicians now
Materials:
- `routes/C/CLINICAL_ONTOLOGY_V0_1.md`
- `routes/C/PILOT_BLUEPRINTS_64.csv`
- `routes/C/CLINICIAN_REVIEW_SCHEMA.csv`
- `routes/C/PILOT_FREEZE_CHECKLIST.md`

The 64 prompts are **AI-drafted candidates, not clinical ground truth**.

### 2. Import complete original A/B 160-prompt set when available
Then run:

```bash
python scripts/pair_audit.py benchmark/cases_full.csv --out results/pair_audit.csv
```

### 3. Freeze C-pilot only after clinician review
Suggested gate:
- ≥80% manipulation success before final revision
- ≤10% unresolved major-confound rate after revision
- usable clinician `[L,U]` on retained items
- adjudication rule frozen before model outputs are inspected

### 4. Run fixed-model C pilot after freeze
Current draft:
- 64 prompts
- 3 fixed model/API configurations
- 3 runs/item if feasible

Potential total = 576 responses.

### 5. Keep cultural formulation as a challenge set
Do not add it to the 64-item core until the four main axes are clinically stable and culturally competent reviewers are available.

## Current Plan C files

- `routes/C/BENCHMARK_AND_PILOT_READY.md`
- `routes/C/METRICS_AND_RESULTS_TEMPLATE.md`
- `routes/C/NOVELTY_SCOPING_REVIEW_2026-10-03.md`
- `routes/C/CLINICAL_ONTOLOGY_V0_1.md`
- `routes/C/PILOT_BLUEPRINTS_64.csv`
- `routes/C/CLINICIAN_REVIEW_SCHEMA.csv`
- `routes/C/PILOT_FREEZE_CHECKLIST.md`
- `scripts/validate_c_pilot.py`
- `scripts/boundary_metrics.py`
- `results/DRY_RUN_C_PILOT_STRUCTURE.md`
- `results/DRY_RUN_BOUNDARY_METRICS.md`

## Result boundary

There are currently **no real model-performance results**. Dry-run files validate software/structure only.