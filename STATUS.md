# STATUS

**Updated:** 2026-10-03

## Overall

🟡 **A/B/C are now all instantiated as concrete versioned research assets. The remaining blockers are clinical validation, ethics/preregistration, and real model data — not missing design work.**

Operational recommendation:

> **A = guaranteed paper track with a complete AI-generated 160-prompt provisional bank; B = active enhancement with a frozen 36-prompt provisional pilot; C = separate high-ceiling benchmark track with a 64-item clinician-review pilot.**

## Completed

- [x] Public collaboration-safe GitHub repository initialized
- [x] Original protocol reconstructed and audited
- [x] Canonical handoff + A/B/C decision architecture
- [x] APP SOP + API-ready benchmark architecture
- [x] Literature/novelty refresh + CHART precheck + statistics review
- [x] Pair-audit / randomization / manifest-validation tooling
- [x] Boundary metrics implemented and synthetic smoke-tested

### Plan A
- [x] protocol-ready + candidate SAP + results shell
- [x] decision recorded to create the missing full bank inside PAIR
- [x] **80 matched pairs / 160 prompts generated**
- [x] P1–P5 each contain 16 pairs / 32 prompts
- [x] structural QA: 80/80 pairs
- [x] very-low pair similarity (<0.35): 0
- [x] major length imbalance (>35%): 0
- [x] heuristic non-target risk mismatch after cleanup: 0
- [x] text frozen as `A-v0.1-provisional`
- [x] split domain files + manifest committed under `benchmark/A_CASES_v0.1/`

### Plan B
- [x] protocol/SAP/results shell
- [x] **6 families × 3 axes × 2 levels = 36 prompts generated**
- [x] 18/18 minimal-pair structure passed
- [x] text frozen as `B-v0.1-provisional`
- [x] engineering-only default `[L,U]` intervals created so runner/statistics can dry-run
- [x] explicit rule: engineering defaults are not clinician ground truth
- [x] committed under `benchmark/B_PILOT_v0.1/`

### Plan C
- [x] narrow novelty/scoping review
- [x] clinical ontology v0.1
- [x] 64 candidate prompts: 8 families × 4 axes × 2 levels
- [x] clinician review schema + freeze checklist
- [x] structural validator passed: 64 rows / 32 pairs / 0 structural errors / 0 similarity warnings
- [x] clinician-review gate: Issue #5
- [x] clinician-review HTML tool

## Current human/research gates

### Plan A
- [ ] clinician review of A-v0.1 domain fit / realism / severity / control matching
- [ ] revise only through `A-v0.2` if needed
- [ ] final rubric approval
- [ ] ethics determination / exemption confirmation
- [ ] preregistration freeze
- [ ] actual consumer-APP collection
- [ ] blinded clinician rating
- [ ] frozen statistical analysis

### Plan B
- [ ] clinician manipulation check on B-v0.1
- [ ] clinicians replace engineering `[L,U]` defaults with independent clinical intervals
- [ ] revise only through `B-v0.2` if needed
- [ ] run 36-prompt pilot after sign-off

### Plan C
- [ ] HG-C1 clinician review of ontology + 64-item pilot: https://github.com/CochraneK/Pair/issues/5
- [ ] clinician `[L,U]` annotations + revision/adjudication
- [ ] explicit team approval that C is a distinct new research question/project
- [ ] contribution/authorship boundary
- [ ] ethics determination + preregistration + fixed-model pilot

## What to do next

### 1. Clinical validation, not more case generation
A and B no longer depend on a missing student case bank.

Review these canonical assets:
- `benchmark/A_CASES_v0.1/`
- `benchmark/B_PILOT_v0.1/`
- `routes/C/PILOT_BLUEPRINTS_64.csv`

### 2. Keep all version boundaries strict
- A text edits → `A-v0.2`
- B text/clinical interval edits → `B-v0.2`
- C clinician-revised pilot → `C-pilot-v0.2`

Never overwrite the frozen v0.1 evidence trail.

### 3. After clinician approval
- A: preregister and run APP product audit
- B: run the 36-prompt boundary pilot in parallel
- C: run separately only after project/ownership/novelty gate

## Result boundary

There are currently **no real model-performance results**. Existing dry-runs validate data structure and metric software only.