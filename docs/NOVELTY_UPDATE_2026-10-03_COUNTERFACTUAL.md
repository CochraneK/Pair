# Novelty update — counterfactual / psychosis boundary design

**Date:** 2026-10-03

## New overlap that materially changes Plan C framing

### SIM-VAIL — Nature Medicine, 2026
Weilnhammer V, Hou KYC, Luettgau L, et al. **A clinically validated framework for auditing AI chatbot behavior in mental health interactions.** Nature Medicine. Published 7 Aug 2026. DOI `10.1038/s41591-026-04577-2`.

Relevant overlap:
- clinically grounded mental-health chatbot safety evaluation
- psychosis included among vulnerability domains
- multi-turn risk trajectories
- counterfactual interventions that changed one user/chatbot message around a risk inflection point

### Other nearby 2026 work
- Psychosis-risk assessment with open-weight LLMs: DOI `10.1038/s41746-026-02928-4`
- Clinically validated psychosis safety criteria + LLM judge/jury: arXiv `2604.02359`
- Longitudinal escalating-delusion trajectories: arXiv `2608.13017`
- Case literature on chatbot reinforcement of psychosis: DOI `10.1186/s12888-026-08137-3`

## Consequence
The following claims are now too broad:
- “first counterfactual mental-health LLM benchmark”
- “first study to test whether one changed message alters chatbot behavior”
- “first clinically grounded psychosis chatbot safety benchmark”

## Narrow signature still worth testing
PAIR-C should instead ask whether **clinically meaningful psychosis cues can be manipulated minimally and one-at-a-time, and whether the model crosses a clinician-defined response-policy boundary proportionately**.

Candidate distinguishing features:
1. psychosis-specific minimal cue contrasts rather than generic psychiatric profile/intent grids
2. explicit axes such as conviction, insight, behavioral risk and evidence/plausibility
3. clinician-defined acceptable intervention interval `[L,U]`
4. symmetric measurement of under-response and over-pathologization/over-escalation
5. nuisance-invariance controls: model should not escalate when clinically irrelevant wording changes
6. cultural formulation as an optional clinician-reviewed challenge factor

## Status of novelty
**Promising but not proven.** Before Plan C protocol freeze, run a formal systematic/scoping search targeted specifically at combinations of:
- psychosis + LLM/chatbot
- conviction / insight / risk / plausibility
- minimal pairs / counterfactual vignette / cue manipulation
- response threshold / triage threshold / intervention threshold
- over-pathologization / over-escalation

Do not write “first” until that search is documented.