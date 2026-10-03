# Reviewer #2 stress test — PAIR-C

**Simulated venue:** npj Digital Medicine  
**Decision on prior wording:** major revision; construct-overclaim risk.  
**Decision after v2 fixes:** potentially strong pilot/benchmark-development paper if real clinical validation and empirical dissociations are convincing.

## Major issues found and action taken
1. **Two-level axes cannot locate a precise boundary.** The manuscript is reframed as *response-policy calibration under minimal clinical contrasts*. Precise threshold/boundary mapping is reserved for a future ≥3-level design.
2. **The 0–5 scale is ordinal, not interval.** URS/ORS are explicitly ordinal step distances; binary under/over-response indicators and full category distributions must accompany means.
3. **CDC no longer uses `[L,U]` midpoints.** Clinicians must prospectively annotate pair-level target direction (`-1/0/+1`) and whether the change is clinically meaningful.
4. **CCA is not overall clinical appropriateness.** It measures escalation-intensity calibration only. Required/contraindicated response components remain separate.
5. **Ground-truth and response-rating roles should be separated.** Prefer distinct clinician panels; if personnel overlap, ground-truth annotations must be irreversibly frozen before outputs and raters masked to them.
6. **“Response policy” itself is not claimed as novel.** 2026 vulnerable-conversation work already audits response policies. PAIR-C's contribution is the psychosis-specific combination of one-cue minimal contrasts, acceptable intervals, direct target-direction labels, and bidirectional calibration.
7. **Eight scenario families limit inference.** Family is the clinical replication unit; 576 generations do not mean 576 clinical cases.
8. **Configuration sampling frame required.** Three models are a purposive pilot sample, not a census or universal leaderboard.
9. **Benchmark contamination risk added.** Public release can contaminate future model training; results must record model date and pre/post-release benchmark status.
10. **AI-assisted drafting artifacts acknowledged.** Naturalistic validity remains a limitation despite clinician review.

## Highest-risk remaining issues
- clinician manipulation validity, especially conviction vs insight separation;
- evidence/plausibility pairs must strengthen an ordinary explanation without changing risk/impairment/certainty;
- `[L,U]` and direct target-direction inter-clinician reliability;
- no nuisance-invariance claims until a true nuisance module exists;
- novelty search must be refreshed immediately before submission.

## Reviewer-style bottom line
C is potentially the more original paper. It will be strong only if the real pilot reveals reproducible calibration dissociations or cue-specific failure patterns. If the headline result is merely that one model has a higher average CCA, the study collapses into another leaderboard and its novelty weakens substantially.
