# Plan C design correction — evidence/plausibility vs nuisance invariance

**Date:** 2026-10-03  
**Triggered by:** technical smoke run v1

## Problem found
The engineering smoke fixture initially treated `evidence/plausibility` as if the model should remain policy-invariant when evidence changed.

That contradicts the scientific design. Evidence/plausibility is one of Plan C's four **clinically relevant** axes:
1. conviction
2. insight
3. behavioral risk
4. evidence/plausibility

## Correct rule
For every clinically relevant minimal pair, including evidence/plausibility:
- the expected direction is derived from the clinician-defined acceptable policy intervals `[L_low,U_low]` and `[L_high,U_high]`;
- the expected direction may be positive, negative, or no-change;
- it must never be hard-coded merely from the axis name.

In particular, stronger externally verifiable evidence can justify **less psychiatric escalation / less over-pathologisation**, so a negative policy shift is scientifically meaningful.

## Nuisance invariance
`Nuisance Invariance (NI)` is reserved for **dedicated clinically irrelevant contrasts**, such as controlled wording/style/background changes that clinicians judge policy-equivalent.

The current 64-item C pilot (`8 families × 4 clinically relevant axes × 2 levels`) contains no dedicated nuisance pairs. Therefore:

> **NI is not a valid primary estimate from the 64-item pilot itself.**

NI should be added only as a separately versioned nuisance module after the four-axis pilot is stable, or reported as `not estimable` in the first 64-item pilot.

## Consequence for metrics
For C-pilot-v0.1:
- CCA: valid
- URS: valid
- ORS: valid
- CDC: valid
- Relevant Sensitivity: valid
- Nuisance Invariance: `NA` unless dedicated nuisance pairs are explicitly added

## Consequence for benchmark v1.0
The planned larger benchmark may retain:
- 160 core clinically relevant prompts
- separate 40-prompt nuisance-invariance module

Do not conflate the two modules.

## Versioning
This is a conceptual/analysis correction, not a silent prompt rewrite. Existing 64 candidate prompt texts remain unchanged unless separate item-level clinical revision is required.
