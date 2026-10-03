# PAIR-C manuscript v2 status

**Date:** 2026-10-03

Current canonical writing state for Paper 2:

> **PAIR-C = psychosis-specific benchmark of conversational response-policy calibration under minimal clinical contrasts.**

The current 64-item pilot does **not** claim precise threshold/boundary-location estimation. With two levels per axis, it tests directional cue sensitivity and calibration; true threshold mapping is reserved for a later ≥3-level design.

## Reviewer-driven corrections now required
- 0–5 is an ordinal escalation-intensity scale, not an interval-quality scale;
- CCA measures escalation-intensity calibration, not total clinical appropriateness;
- URS/ORS are ordinal step distances and must be accompanied by binary/category distributions;
- clinicians directly annotate pair-level `target_direction ∈ {-1,0,+1}` before model outputs;
- clinicians also annotate `clinically_relevant_change` for Relevant Sensitivity;
- CDC uses direct clinician target direction, not `[L,U]` midpoint arithmetic;
- ground-truth panel and model-output raters should be distinct where feasible, otherwise annotations are frozen before outputs and masked during rating;
- eight families are the clinical replication units; repeated generations only estimate stochasticity;
- model/configuration sample is purposive and prespecified, not a universal leaderboard;
- nuisance invariance remains **not estimated** until a dedicated nuisance module exists;
- public benchmark release creates future contamination risk and must be versioned by release/model date;
- generic “response policy” is not claimed as novel.

## Mandatory clinician schema before real C outputs
- raw `[L,U]` per clinician;
- pair-level `target_direction`;
- `clinically_relevant_change`;
- manipulation success;
- unintended second-axis change;
- major confound;
- contraindicated behaviors.

## Canonical review documents
- `manuscript/REVIEWER2_C_v1.md`
- `manuscript/SUBMISSION_READINESS_AFTER_R2.md`

The local DOCX/Markdown artifact is `PAIR_C_MASTER_v2`; later drafting should not revert to the older “exact boundary benchmark” wording.
