# Plan C narrow novelty/scoping review — 2026-10-03

## Scope
Question searched:

> Has prior work already evaluated **psychosis-specific conversational response-policy boundaries** using one-clinical-cue-at-a-time minimal contrasts, clinician-defined acceptable action ranges, symmetric under-response/over-response penalties, and nuisance invariance?

This is a targeted scoping/novelty review, not yet a PRISMA-grade systematic review.

## Closest prior work

| Work | What it already does | Why it matters for PAIR-C | Gap relative to PAIR-C |
|---|---|---|---|
| Shen et al., JAMA Psychiatry 2026, DOI 10.1001/jamapsychiatry.2026.0249 | psychotic vs matched control prompts; clinician appropriateness rating | direct parent of Plan A | not a cue-specific response-boundary benchmark |
| The Psychogenic Machine / psychosis-bench, arXiv:2509.10970 | 16 structured 12-turn delusion scenarios; DCS/HES/SIS | psychosis-specific safety benchmark already exists | trajectory/delusion-reinforcement focus; not minimal one-cue boundary calibration |
| LLM Spirals of Delusion, arXiv:2604.06188 | 56 20-turn conversations; API vs chatbot interface; human + LLM grading | interface and longitudinal audit already occupied | not clinician-defined one-cue action thresholds |
| SIM-VAIL, Nature Medicine 2026, DOI 10.1038/s41591-026-04577-2 | clinically validated mental-health audit; counterfactual message interventions near risk-inflection points | generic counterfactual mental-health auditing is not novel | intervention changes whole message branch around observed escalation, not a psychosis-specific predefined clinical-cue grid |
| Safe-Psych, arXiv:2607.13036 | sequential psychiatric evidence; DIAGNOSE/CLARIFY/ABSTAIN; premature vs excessive abstention | bidirectional calibration under clinical uncertainty already exists conceptually | diagnostic determinability task, not patient-facing psychosis conversational response policy |
| ClinDet-Bench, ACL Industry 2026, DOI 10.18653/v1/2026.acl-industry.47 | determinable vs undeterminable clinical judgments; premature conclusion + excessive abstention | reinforces need to punish errors in both directions | general clinical decision determinability, not psychosis-specific conversational intervention |
| K-Bench, arXiv:2609.15855 | 200 multi-turn high-risk vignettes; clinician-calibrated judge; 125 configurations | clinician-calibrated mental-health benchmark is not novel | broad high-risk domains; no one-cue minimal psychosis boundary design |
| Zhu et al., npj Digital Medicine 2026, DOI 10.1038/s41746-026-02928-4 | LLM psychosis-risk assessment from PSYCHS transcripts; over-pathologisation error | over-pathologisation in psychosis-related evaluation is already documented | assessment task, not response-policy calibration |
| PsychiatryBench, npj Digital Medicine 2026, DOI 10.1038/s41746-026-02582-w | 5,188 psychiatry items across 11 tasks | psychiatry benchmark per se is not novel | diagnostic/knowledge tasks; not conversational boundary behavior |
| Zheng et al., npj Digital Medicine 2026, DOI 10.1038/s41746-026-02605-6 | AI-generated psychiatric vignettes rated by board-certified psychiatrists | validates AI-assisted vignette drafting as a method | not a response-boundary benchmark |

## Novelty claims PAIR-C must NOT make
Do not claim novelty for any of the following in isolation:
- psychosis benchmark
- multi-turn mental-health safety
- clinician ground truth
- LLM judge
- counterfactual intervention
- API vs APP
- repeated sampling
- generic "clinical calibration"
- over-pathologisation detection
- synthetic psychiatric vignette generation

## Narrow signature still not identified as an exact prior design
Current targeted search did **not identify an exact match** to the full combination below:

1. psychosis-spectrum patient-facing disclosures;
2. predefined **one-clinical-cue-at-a-time** minimal contrasts;
3. cue axes such as conviction, insight, behavioral risk, and evidence/plausibility;
4. clinician-defined **acceptable intervention interval `[L,U]`**, rather than one gold response;
5. symmetric scoring of **under-response and over-response / over-pathologisation**;
6. **relevant sensitivity** plus **nuisance invariance** in the same benchmark.

This should be written as:
> "In our current targeted search, we did not identify a benchmark combining..."

Do **not** write:
> "This is the first benchmark ever to..."

until a formal systematic/scoping search is frozen and rerun immediately before submission.

## Strongest scientific framing
PAIR-C should not be framed as another safety leaderboard.

The scientific object is:

> **the location and direction of conversational response-policy shifts when a single clinically meaningful psychosis-related cue changes, while penalising both failure to escalate and premature escalation.**

## Highest-value empirical signatures to look for
A strong paper would show one or more of:
1. models react appropriately to explicit behavioral risk but are insensitive to conviction/insight;
2. models systematically over-escalate when unusual experiences have plausible or culturally sanctioned explanations;
3. products differ not just in average safety score but in **where their intervention thresholds lie**;
4. stronger reasoning/capability does not guarantee better boundary calibration;
5. nuisance changes cause clinically unjustified policy shifts.

## Decision
Novelty status as of 2026-10-03:

- broad Plan C concept: **not novel enough**
- narrowed PAIR-C signature above: **plausibly novel / publishable, but not yet proven unique**
- formal novelty gate before preregistration/publication: **required**
