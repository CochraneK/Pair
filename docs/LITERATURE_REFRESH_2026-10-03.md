# Literature refresh — 2026-10-03

This memo updates claims that materially affect PAIR's novelty or reporting strategy.

## Direct methodological parent

### Shen et al. — JAMA Psychiatry, 2026
**Evaluation of Large Language Model Chatbot Responses to Psychotic Prompts**  
JAMA Psychiatry. 2026;83(6):655–657.  
DOI: `10.1001/jamapsychiatry.2026.0249`

Closest direct parent:
- psychotic vs matched-control prompts
- isolated chatbot sessions
- clinician-rated response appropriateness

**Implication:** the original protocol is best described as a replication/extension unless it adds a distinct scientific question.

## Psychosis-specific overlap

### psychosis-bench / The Psychogenic Machine — arXiv:2509.10970
- 16 structured 12-turn scenarios
- explicit / implicit presentations
- DCS / HES / SIS metrics

**Implication:** multi-turn psychosis escalation is not, by itself, a novelty claim.

### LLM Spirals of Delusion — arXiv:2604.06188
**Implication:** APP/interface vs API is already an active research question.

### DelusionEval — arXiv:2608.05004
**Implication:** long-context and harm-derived / naturalistic histories are already represented.

## Broader benchmark overlap

- **PsyEval**, npj Mental Health Research 2026 — DOI `10.1038/s44184-026-00227-0`
- **PsychiatryBench**, npj Digital Medicine 2026 — DOI `10.1038/s41746-026-02582-w`
- **MentalBench-100k / MentalAlign-70k**, EACL 2026 — DOI `10.18653/v1/2026.eacl-long.180`
- **Health-ORSC-Bench**, Findings ACL 2026 — DOI `10.18653/v1/2026.findings-acl.1177`
- **PsychEthicsBench**, Findings ACL 2026 — DOI `10.18653/v1/2026.findings-acl.1971`
- **Safe-Psych**, arXiv:2607.13036
- **K-Bench**, arXiv:2609.15855

**Implication:** generic mental-health benchmarking, LLM judge, over-refusal, sequential uncertainty, and generic "clinical calibration" are already occupied spaces.

## Very-close consumer-product precedent

### Xiao et al. — Frontiers in Psychiatry, 11 Sep 2026
**Large language models for late-life depression: a blinded benchmark of clinical safety, geriatric appropriateness, and triage**  
DOI: `10.3389/fpsyt.2026.1956736`

- 90 questions
- ChatGPT / Gemini / Doubao consumer products
- independent conversations
- risk strata
- repeated subset
- psychiatrist evaluation + adjudication

**Implication:** Plan A is clearly publishable as a study type, but the design family is mature. Calling a study a benchmark does not by itself increase novelty.

## Reporting standard

### CHART — BMJ, 2025
DOI: `10.1136/bmj-2024-083305`

CHART asks for:
- chatbot/model identification
- versions and query dates
- route of access
- prompt source / engineering
- query strategy
- ground truth
- sample size
- analysis
- ethics/protocol/data availability

**Action:** map PAIR to CHART before data collection.

## Benchmark interpretability

### McBain et al. — BMJ Mental Health, 28 Sep 2026
DOI: `10.1136/bmjment-2026-302921`

Calls for:
- domain composition
- subgroup/failure-mode reporting
- clinically meaningful anchors
- uncertainty
- reproducible versioned analyses

Psychosis was only 0.9% of mental-health conversations in the HealthBench subset they analysed.

**Implication:** psychosis-specific evaluation remains clinically justifiable.

## Current novelty conclusion

Do **not** use as standalone novelty:
- Chinese language
- Chinese models
- consumer APP
- API
- APP vs API
- repeated sampling
- multi-turn
- LLM judge
- refusal / over-refusal
- generic "clinical calibration"
- benchmark runner / leaderboard

Still worth formal novelty testing:
1. psychosis-specific **minimal counterfactual response-policy boundary**
2. **under-response vs over-pathologization / over-escalation**
3. **cultural formulation** as a controlled clinical factor
4. clinician **acceptable-action distributions**

Confidence:
- high for occupied-space claims
- moderate for remaining-gap claims; Plan C requires a narrower systematic search
