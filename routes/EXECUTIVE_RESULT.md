# Parallel A/B/C execution — executive result

**Date:** 2026-10-03

This is a **design/execution result**, not a model-performance result.

## What was advanced

### Plan A — ready for final prompt/rater freeze
Now has:
- executable research question
- consumer-product SOP
- matched-pair validity rules
- primary/secondary outcomes
- candidate SAP
- results tables/figures shell
- claim boundaries
- freeze checklist

Remaining external inputs:
1. full 160-prompt set
2. clinician prompt/rubric approval
3. ethics determination
4. statistician sign-off/preregistration
5. actual APP collection and ratings

### Plan B — pilot-ready
Now has:
- Aim 1 = full Plan A
- fixed first pilot: 6 families × 3 axes × 2 variants = 36 prompts
- suggested 3 products × 3 runs = 324 responses
- clinician acceptable-policy interval `[L,U]`
- under-response / over-response separated
- relevant-sensitivity and directional-concordance metrics
- pilot go/no-go rules
- executable metric code + synthetic smoke test

Remaining external inputs:
1. clinicians validate 36 pilot items and `[L,U]`
2. team permits Aim 2 pilot
3. run pilot

### Plan C — benchmark/pilot-ready, novelty narrowed
Now has:
- new psychosis-specific response-boundary RQ
- 160 core-prompt architecture + 40 nuisance-invariance prompts
- clinician acceptable-policy interval ground truth
- CCA / URS / ORS / RS / NI / CDC metrics
- API-first + APP-secondary execution strata
- 64-prompt pilot design
- executable metric code + synthetic smoke test
- explicit novelty correction after SIM-VAIL/Nature Medicine 2026

Remaining external inputs:
1. formal narrow novelty/scoping review
2. explicit team agreement that this is a new project/question
3. contribution/authorship boundary
4. clinician ground-truth pilot

## Comparative conclusion

### Best minimum publishable route
**Plan A**

### Best current collaboration route
**Plan B**

Reason: it preserves A completely while adding a bounded new scientific question; if Aim 2 fails, Aim 1 survives.

### Highest-risk/highest-ceiling route
**Plan C**

Plan C is still interesting, but broad counterfactual mental-health auditing is no longer a credible novelty claim after 2026 work. It should be a separate benchmark-development track unless the team deliberately replaces the original project.

## What should happen next

Do **not** spend another cycle expanding concepts.

Priority order:
1. obtain/import the complete original 160-prompt set
2. run full automated + human matched-pair audit
3. in parallel, generate the 36 Plan-B pilot prompts from 6 clinician-approved base families
4. clinicians validate prompt manipulations and `[L,U]` policy intervals
5. freeze Plan A + decide whether Plan B pilot becomes part of the paper
6. leave Plan C as a prepared parallel track until novelty and ownership gates are cleared

## Current operational recommendation

Treat the project as:

> **A is the guaranteed paper; B is the active enhancement; C is the prepared next-study/benchmark track.**
