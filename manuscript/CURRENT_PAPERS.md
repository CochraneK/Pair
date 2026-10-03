# Current manuscript state

[English](CURRENT_PAPERS.md) | [简体中文](CURRENT_PAPERS.zh-CN.md)

Updated: 2026-10-03

## Paper 1 — A+B

**Canonical working version:** A+B Master v4

- English master: [`PAIR_AB_MASTER_v4_EN.md`](PAIR_AB_MASTER_v4_EN.md)
- 中文主稿: [`PAIR_AB_MASTER_v4_ZH.md`](PAIR_AB_MASTER_v4_ZH.md)
- English conversation exemplars: [`PAIR_AB_CONVERSATION_EXAMPLES_v1_EN.md`](PAIR_AB_CONVERSATION_EXAMPLES_v1_EN.md)
- 中文对话样例: [`PAIR_AB_CONVERSATION_EXAMPLES_v1_ZH.md`](PAIR_AB_CONVERSATION_EXAMPLES_v1_ZH.md)

Scientific role:
- Aim 1: confirmatory matched psychosis-related vs matched-control consumer-product audit.
- Aim 2: prespecified exploratory response-policy calibration substudy.

Reviewer-2 corrections already incorporated into the design state:
- product identity can be blinded; prompt condition is not claimed to be blinded;
- P5 disorganized-communication sensitivity analysis is prespecified;
- consumer-product sampling frame and version-break rules are required;
- brand-leakage audit is required;
- Aim 2 remains exploratory because six scenario families are the clinical replication units.

**Dialogue-exemplar rule:** the final paper must include representative prompt-response examples. Selection is frozen in advance: one Aim-1 matched pair, one Aim-2 minimal pair, and—if a failure example is shown—one predefined frequency/medoid-selected failure category rather than a narratively convenient cherry-picked case.

## Paper 2 — C

**Canonical working version:** PAIR-C Master v2

- English master: [`PAIR_C_MASTER_v2_EN.md`](PAIR_C_MASTER_v2_EN.md)
- 中文主稿: [`PAIR_C_MASTER_v2_ZH.md`](PAIR_C_MASTER_v2_ZH.md)
- English conversation exemplars: [`PAIR_C_CONVERSATION_EXAMPLES_v1_EN.md`](PAIR_C_CONVERSATION_EXAMPLES_v1_EN.md)
- 中文对话样例: [`PAIR_C_CONVERSATION_EXAMPLES_v1_ZH.md`](PAIR_C_CONVERSATION_EXAMPLES_v1_ZH.md)

Scientific role:
- development and pilot evaluation of psychosis-specific conversational response-policy calibration under one-clinical-cue-at-a-time minimal contrasts;
- clinician-defined acceptable intervention intervals `[L,U]`;
- direct clinician pair-level target direction (`-1/0/+1`);
- separate under-response and over-response;
- repeated generations used for stochasticity, not inflated clinical sample size.

Key corrections:
- the 64-item pilot does **not** claim precise threshold/boundary-location estimation;
- 0–5 is an ordinal escalation-intensity scale, not an equal-interval clinical severity scale;
- URS/ORS are ordinal step distances and must be accompanied by categorical/binary summaries;
- evidence/plausibility is clinically relevant and is not nuisance invariance;
- Nuisance Invariance is not estimated in the current 64-item pilot.

**Dialogue-exemplar rule:** the main text must contain at least one minimal clinical-contrast dialogue pair tied to the principal empirical finding; additional examples move to the Supplement. Selection must not depend on dramatic wording.

## GitHub Pages meeting interface

GitHub Pages is the intended meeting/presentation surface, not merely a repository landing page.
- `docs/index.html` is the meeting discussion handbook.
- `docs/papers.html` embeds both manuscript masters inside the Page with A+B / C and Chinese / English switching.
- The corresponding conversation-exemplar module is automatically appended beneath each embedded paper.
- `docs/dashboard.html` remains a technical project index rather than the meeting-facing page.

## Bilingual publication rule

Public README, current manuscript masters, conversation-exemplar modules, HTML meeting pages and GitHub Pages are maintained in synchronized English and Simplified Chinese versions. See [`../BILINGUAL_POLICY.md`](../BILINGUAL_POLICY.md).

## Empirical-result boundary

There are currently **no real model-performance results** in the repository. Synthetic and dry-run outputs are engineering/rehearsal artifacts only and must never be reported as empirical findings.

## Submission gate

Neither paper is submission-ready until real ethics determination, preregistration status, exact product/model manifests, real clinician review/ratings, empirical outputs, frozen statistics, Data/Code Availability, authorship/funding/COI, and final CHART review are complete.