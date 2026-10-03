# PAIR A+B manuscript blueprint v3 — formal research-article standard

Target: npj Digital Medicine (primary); JMIR Mental Health (fallback).
Manuscript role: submission-structured master with real-data placeholders. Plan C remains a separate companion benchmark paper.

## 1. Single scientific story
The manuscript must answer one primary question and one bounded extension:

- Primary question (Aim 1): Do tested consumer AI chat products respond less appropriately to psychosis-related prompts than to closely matched nonpsychotic prompts?
- Exploratory extension (Aim 2): When one clinically relevant cue changes within the same psychosis-related scenario, does the product shift its conversational intervention policy in the clinically expected direction without systematic under-response or over-response?

Aim 2 is explicitly exploratory because it contains six scenario families. It should not carry confirmatory claims that require a larger family-level sample.

## 2. Introduction: five-move structure
1. Clinical use-case and hazard: patient-facing AI may encounter unusual beliefs/perceptions; empathic validation can be unsafe when it endorses an implausible interpretation.
2. Direct empirical precedent: Shen et al. demonstrated a psychosis-specific appropriateness penalty using matched psychotic/control prompts.
3. What broader AI-psychiatry work has added: capability benchmarks, multi-turn/high-risk safety, uncertainty, refusal/over-refusal, psychosis-specific reinforcement.
4. Why a clinical boundary is needed: psychotic phenomena are multidimensional; conviction, insight/attribution, and immediate behavioral risk can change what a proportionate response should do. More escalation is not uniformly safer.
5. Study aims and hypotheses: Aim 1 confirmatory; Aim 2 prespecified exploratory. No product-ranking hypothesis.

## 3. Clinical construct grounding
- SIPS P1–P5 is a domain taxonomy, not a diagnostic instrument for this benchmark.
- Conviction is operationalized as certainty with which an unusual interpretation is held.
- Insight is operationalized narrowly as willingness/ability to consider internal, contextual, or alternative explanations; it is not treated as a single global illness-insight construct.
- Behavioral risk is operationalized as immediate planned/confrontational/risky action; the study must explicitly avoid equating psychosis with violence.
- Cultural plausibility is a validity-control consideration, not an Aim-2 axis in the current 36-item pilot.

## 4. Literature architecture
The Introduction should synthesize, not list:
A. Psychosis-specific patient-facing risk and direct parent study.
B. General psychiatry capability benchmarks.
C. Mental-health safety/calibration benchmarks.
D. Psychosis-specific multi-turn/reinforcement evidence.
E. Classical clinical literature supporting dimensionality, insight, risk assessment, and cultural formulation.

## 5. Methods: reproducibility-first order
1. Design, reporting guideline, and claim scope.
2. Objectives, hypotheses, and estimands.
3. Prompt development/provenance and AI assistance.
4. Clinical construct map and item-validation procedure.
5. Matched-control construction/audit.
6. Consumer products and exact access conditions.
7. Query strategy, randomization, retries, immutable capture.
8. Repeated-sampling subset.
9. Blinded clinical rating and adjudication.
10. Aim-2 minimal contrasts and acceptable policy intervals.
11. Sample-size rationale/execution counts.
12. Statistics and reproducibility.
13. Ethics, preregistration, Data Availability, Code Availability, AI-use disclosure.

## 6. Statistical hierarchy
Aim 1:
- Primary outcome: consensus/adjudicated 0–2 appropriateness.
- Primary model: cumulative-link mixed model with psychosis condition, product, condition×product, and SIPS domain as fixed effects; matched pair/prompt structure as random effects.
- Primary estimand: overall psychosis-vs-control common odds ratio with 95% CI.
- Secondary: product interaction, domain/failure profiles, fully inappropriate binary sensitivity.
- Rater agreement reported before adjudication; raw-rater sensitivity model adds rater structure.
- Repeated sampling: exact-score stability and clinically meaningful category changes.

Aim 2:
- No confirmatory P-value headline.
- Report CCA, URS, ORS and within-family directional concordance.
- Treat scenario family as the meaningful replication unit.
- Show individual family points/intervals; emphasize estimation and heterogeneity.
- Six-family uncertainty must be described as limited.

## 7. Results order
1. Flow, completeness, technical failures/fallbacks.
2. Aim-1 primary effect and product interaction.
3. Domain/failure profile.
4. Repeat stability.
5. Aim-2 exploratory boundary results.
6. Inter-rater reliability.
No interpretation in Results.

## 8. Discussion order
1. Three principal findings, each with an effect estimate.
2. Comparison with Shen and psychosis-specific prior work.
3. Mechanistic interpretation of under-response vs over-response.
4. Product-layer interpretation (not base-model essentialism).
5. Clinical and policy implications.
6. Strengths.
7. Limitations.
8. Conclusion with narrow claim.

## 9. Claim boundaries
Never claim:
- the tested product is generally “safe” or “unsafe”;
- base-model behavior from consumer-app results;
- causal harm to patients;
- diagnostic validity of the prompt set;
- that psychosis implies violence;
- Aim-2 benchmark validity from only six families.

## 10. Submission gates
Before submission, all must be real:
- institutional ethics/determination;
- public preregistration or transparent statement if none;
- exact product versions/dates/settings;
- clinician item validation and [L,U];
- empirical outputs only;
- final rater/adjudication rule;
- frozen statistics and software/session versions;
- data/code DOI or justified restrictions;
- CRediT, funding, COI, acknowledgements;
- AI-use disclosure reviewed against current journal policy;
- completed CHART checklist and Nature Portfolio Reporting Summary.
