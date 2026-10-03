# Responses of Chinese consumer AI chat products to psychosis-related content: a matched-prompt study with an exploratory clinical-contrast substudy

[English](PAIR_AB_MASTER_v4_EN.md) | [简体中文](PAIR_AB_MASTER_v4_ZH.md)

**Target journal:** npj Digital Medicine  
**Fallback:** JMIR Mental Health  
**Version:** PAIR A+B Master v4  
**Internal status:** submission-structured master. Do not submit until every `[[REAL ...]]` field is resolved. Synthetic/dry-run values must never be reported as empirical findings.

## Abstract

### Background
General-purpose AI chat products may be used by people seeking advice about unusual beliefs, suspiciousness, perceptual experiences, or other psychosis-related concerns. In this setting, failure can occur in opposite directions: a chatbot may reinforce an implausible interpretation or under-triage immediate risk, but it may also over-pathologize an ambiguous or culturally plausible experience. A prior matched-prompt study of ChatGPT found substantially less appropriate responses to psychotic than control prompts [1]. Whether this psychosis-specific penalty generalizes across Chinese consumer AI products, and whether products change their response proportionately when clinically relevant cues change, remains uncertain.

### Methods
PAIR (Psychosis AI Response) is a cross-sectional, repeated-query evaluation of Chinese-language consumer AI chat products. Aim 1 uses 80 psychosis-related prompts and 80 closely matched nonpsychotic controls spanning five SIPS-informed positive-symptom domains [2]. Frozen prompts are submitted in fresh single-turn conversations to five prespecified consumer products under documented settings. Two psychiatrists, blinded to product identity, independently rate overall appropriateness (0 fully appropriate, 1 partially appropriate, 2 fully inappropriate) and prespecified component failures. A stratified subset of 16 psychosis-related prompts is repeated twice per product to quantify response instability. Aim 2 is a prespecified exploratory substudy using 36 minimal-contrast prompts that manipulate conviction, insight/alternative-explanation acceptance, or immediate behavioral risk within six scenario families. Clinicians define an acceptable intervention interval `[L,U]` for each variant, enabling separate measurement of under-response and over-response. Reporting follows CHART [19,20].

### Results
[[REAL RESULTS: report the number of analyzable responses, technical failures/fallbacks, primary cumulative-link mixed-model psychosis-vs-control effect with 95% CI, prespecified product interaction, pre-adjudication inter-rater agreement, repeat stability, and exploratory Aim-2 calibration estimates. No synthetic values.]]

### Conclusions
[[REAL CONCLUSION: state only findings supported by frozen analyses and tie claims to the tested product versions, access routes, settings, and collection dates. Avoid general model-family safety claims.]]

## Introduction

Consumer AI chat products are increasingly used as general-purpose conversational systems, yet users may bring them mental-health concerns that ordinarily require contextual clinical judgment. Psychosis-related disclosures are especially demanding. Agreement can inadvertently reinforce an implausible belief, whereas an excessively alarmed response can prematurely pathologize a benign, weakly held, or culturally meaningful experience. The relevant task is therefore not merely to “refuse” or “escalate,” but to respond proportionately to what is known, what remains uncertain, and whether there is evidence of immediate risk.

The strongest direct empirical precedent is the 2026 study by Shen and colleagues, who submitted 79 psychotic prompts and 79 matched controls to three ChatGPT product versions and found substantially higher odds of less appropriate responses to psychotic content [1]. Their study established a psychosis-specific performance gap and highlighted interpretable components such as recognition, non-reinforcement, urgency, and resources. It also left several open questions: only one product family was studied, each prompt was queried once, and consumer products change rapidly. PAIR retains the matched-prompt logic while extending it to multiple Chinese-language consumer products, repeated sampling, stricter pair auditing, and explicit version- and setting-specific claims.

AI evaluation in psychiatry has subsequently broadened in three directions. General psychiatric benchmarks such as PsychiatryBench and PsyEval assess knowledge, diagnostic reasoning, and supportive communication [7–9]. Safety-focused work evaluates vulnerability amplification, sequential uncertainty, high-risk dialogue, over-refusal, and ethics-sensitive behavior [10,13–16]. Psychosis-specific work examines delusion reinforcement, harm enablement, interface effects, and over-pathologization in psychosis-risk assessment [11,12,17]. These literatures show that psychiatric LLM evaluation is moving beyond raw accuracy, but broad benchmark scores and refusal rates do not reveal whether a system changes its response at the clinically appropriate point.

This matters because psychotic phenomena are multidimensional. Delusional experiences vary in conviction, preoccupation, distress, behavioral disruption, and attribution [3]. Insight is also multidimensional and includes awareness, attribution of experiences, and perceived need for care [4]. Immediate behavioral risk must be assessed contextually rather than inferred from psychosis alone [5,21]. Cultural formulation is likewise important because plausibility and meaning depend partly on explanatory models and social context [6]. The same unusual experience may therefore warrant different conversational responses depending on certainty, openness to alternative explanations, and intended action.

PAIR is designed around one primary question and one bounded extension. **Aim 1** tests whether psychosis-related prompts receive less appropriate responses than closely matched nonpsychotic controls across five Chinese-language consumer AI products. We hypothesize higher odds of a less appropriate rating for psychosis-related prompts. Product differences and symptom-domain patterns are prespecified secondary questions rather than rank-order hypotheses. **Aim 2** is a prespecified exploratory minimal-contrast substudy. Within six psychosis-relevant scenario families, conviction, insight/acceptance of alternative explanations, or immediate behavioral risk is changed while other information is held as constant as practicable. Clinician-defined acceptable policy intervals separate under-response from over-response and test proportionality rather than assuming that more intervention is always better.

## Methods

### Study design, reporting standard, and claim scope
PAIR is a cross-sectional, repeated-query evaluation of consumer AI chat products with an embedded exploratory minimal-contrast substudy. Aim 1 is primary; Aim 2 is exploratory. Reporting follows the Chatbot Assessment Reporting Tool (CHART) statement and explanation/elaboration guidance [19,20]. The evaluated unit is the **consumer product under the observed access route, settings, account state, and collection dates**. Findings are not interpreted as invariant properties of a base-model family.

### Objectives, hypotheses, and estimands
The primary Aim-1 hypothesis is that psychosis-related prompts have higher cumulative odds of receiving a less appropriate ordinal rating than matched nonpsychotic controls. The primary estimand is the psychosis-vs-control common odds ratio from a prespecified cumulative-link mixed model, with 95% confidence interval. Product-by-condition interaction, SIPS-domain differences, component failure profiles, and repeat instability are secondary.

Aim 2 is estimation-focused and exploratory. For each product and manipulated axis, we estimate: (1) Clinical Calibration Accuracy (CCA), the proportion of responses falling within the clinician-defined acceptable policy interval; (2) under-response severity (URS); (3) over-response severity (ORS); and (4) within-family directional concordance between clinician-required and observed policy shifts. No product ranking is hypothesized a priori.

### Prompt taxonomy and clinical constructs
Aim 1 contains 80 psychosis-related prompts organized into five SIPS-informed positive-symptom domains: unusual thought content, suspiciousness/persecutory ideas, grandiosity, perceptual abnormalities, and disorganized communication [2]. This taxonomy organizes stimuli only; PAIR is not a diagnostic or individual risk-prediction instrument.

Aim-2 axes were selected because they can change a proportionate response without changing the scenario wholesale. **Conviction** is the certainty with which an unusual interpretation is held [3]. **Insight** is operationalized narrowly as willingness to consider internal, contextual, or alternative explanations; it is not treated as a single global illness-insight construct [4]. **Behavioral risk** is immediate intention to take a consequential or potentially risky action. Risk is included because it is clinically relevant, not because psychosis is assumed to imply violence [5,21]. Cultural plausibility remains an item-validity consideration rather than a manipulated Aim-2 axis [6].

### Prompt development, provenance, and validation
All prompts are fictional and created for this study; they do not reproduce SIPS interview wording or published case narratives. Researchers first specify the clinical taxonomy, pair-matching rules, prohibited confounds, and Aim-2 manipulation axes. Generative AI may assist candidate wording and minimal-pair drafting under researcher-defined constraints. Human researchers audit candidate items for target-domain fit, naturalness, accidental risk cues, medication or financial stakes, confrontation, self-harm/harm-to-others content, and cross-condition length or tone differences.

[[REAL CLINICAL VALIDATION: report number and qualifications of psychiatrists, independent-review procedure, manipulation-success criterion, major-confound rule, adjudication procedure, and final retained/revised item counts. Do not describe assumed or simulated review as clinician validation.]]

Prompt sets are versioned and cryptographically hashed before empirical collection. Any wording change after freeze creates a new version; frozen files are never silently overwritten.

### Matched-control construction
Each psychosis-related Aim-1 prompt is paired with a nonpsychotic analogue designed to preserve scenario topic, first-person perspective, approximate length, requested action, emotional tone, and non-target behavioral risk while changing the psychosis-specific interpretation or communication feature. Pair auditing checks for differences in medication behavior, financial stakes, confrontation, self-harm/violence cues, urgency, and other features that could independently alter the appropriate response.

Because P5 disorganized communication necessarily changes linguistic organization more extensively than P1–P4 belief/perception contrasts, a P1–P4-only sensitivity analysis is prespecified.

### Consumer-product sampling frame and access conditions
The product sample is defined prospectively. Eligible products are general-purpose, publicly accessible Chinese-language chatbot products available to ordinary users during the collection window, with a stable consumer chat interface and no requirement for specialist clinical access. The five prespecified products are DeepSeek, Doubao, Kimi, Qwen, and Yuanbao.

[[REAL PRODUCT-SELECTION RECORD: document the contemporaneous sampling frame, inclusion/exclusion rationale, any major eligible product not tested and why, and confirm that the final set was frozen before outcome collection.]]

[[REAL PRODUCT MANIFEST: insert exact displayed product name, developer, access surface, displayed model/mode if available, subscription tier, locale, account state, collection timestamps/time zone, memory/history settings, reasoning state, search/tool state, and visible version/build information.]]

Dedicated research accounts are used. Memory, cross-chat history reference, and custom instructions are disabled when controllable. Unobservable or uncontrollable settings are recorded as such rather than inferred.

### Query strategy, randomization, and capture
Every frozen prompt is submitted verbatim in a fresh conversation. No follow-up question, regeneration, rating feedback, manual tool toggle, or content editing is permitted. Prompt order is independently randomized for each product using a prespecified seed. Refusals, safety banners, clarification requests, blank outputs, and other complete responses are retained as data. Retries are permitted only for prespecified technical failures, and failed attempts remain in the run manifest.

The collection window is treated as a version-controlled snapshot. If a visible model/mode/version change, forced fallback, major routing change, or other material configuration change occurs, collection for that product is paused. Remaining runs are completed only after returning to the frozen configuration or are assigned to a new configuration stratum. Materially different configurations are never pooled silently.

Raw output is archived before blinding. For each run, the study records prompt ID, product, access route, timestamp, visible settings, quota/fallback events, retry count, raw response, and screenshot or equivalent capture when feasible. Product-identifying text or formatting is removed only when this can be done without changing semantic content. A brand-leakage audit records unresolved cues such as self-identification, proprietary citations, distinctive formatting, or safety-language signatures.

### Repeated sampling
A stratified subset of 16 psychosis-related prompts (20% of the psychosis set) is fixed before collection and queried in two additional fresh conversations per product, producing three independent outputs for each repeated item. Repeats quantify instability and are not used to select a preferred response.

### Aim-1 clinical rating
Two psychiatrists independently rate each de-identified **prompt-response pair** while blinded to product identity. They are not described as blinded to prompt condition because the source prompt is required to judge response appropriateness and its clinical content may reveal condition. The primary outcome is overall appropriateness on a 0–2 ordinal scale: 0 fully appropriate, 1 partially appropriate, 2 fully inappropriate, retaining comparability with the direct parent study [1]. Prespecified component ratings cover recognition, non-reinforcement/epistemic restraint, urgency/risk handling, and resources. Exploratory flags cover inappropriate refusal/abandonment and over-pathologization.

Raters complete calibration training on a separate practice set. Raw ratings are preserved before adjudication. [[REAL RATING RULE: specify preregistered disagreement/adjudication rule and whether the primary response-level outcome is adjudicated consensus.]] Inter-rater agreement is reported before adjudication.

### Aim-2 minimal contrasts and policy scale
Aim 2 contains 36 prompts from six scenario families. Within each family, one pair is created for each axis: conviction, insight/alternative-explanation acceptance, and immediate behavioral risk. Topic, narrator, requested action, sentence structure, emotional tone, and non-target clinical dimensions are held as constant as practicable.

Clinicians independently define an acceptable intervention interval `[L,U]` for each variant on a six-level policy scale:

0. ordinary/supportive response sufficient;  
1. clarification/exploration;  
2. explicit uncertainty/non-reinforcement;  
3. risk assessment;  
4. routine professional referral;  
5. urgent escalation/emergency-oriented response.

A range is used because multiple conversational strategies can be acceptable. Separate contraindicated-behavior flags capture reinforcement of implausible interpretations, risky assistance, ridicule/confrontation, premature diagnostic labeling, dangerous under-triage, and unnecessary emergency escalation.

[[REAL AIM-2 VALIDATION: replace engineering intervals with raw clinician-specific `[L,U]`, describe disagreement/adjudication, and report any item revisions or exclusions before model outputs are inspected.]]

### Sample-size rationale and execution counts
The benchmark size is design-driven rather than a patient epidemiologic sample-size calculation. Aim 1 uses 80 matched pairs (16 per P1–P5 domain). Five products yield 800 primary responses; the repeated subset adds 160 responses, for 960 Aim-1 outputs if all runs complete. Aim 2 contains 36 prompts in three products with three runs per prompt, yielding 324 outputs.

Before empirical outcome analysis, simulation-based operating-characteristic/precision checks will document the range of condition effects and product interactions that the frozen design can estimate with useful precision; these checks will not be tuned to observed product outcomes.

[[REAL FLOW: report attempted, completed, technically failed, retried, excluded, and analyzed counts by product.]]

### Statistics and reproducibility — Aim 1
The primary response-level analysis uses the adjudicated/consensus 0–2 appropriateness rating and a cumulative-link mixed model with logit link. Fixed effects include condition, product, condition×product, and SIPS domain. Random effects preserve the paired and repeated prompt structure; final parameterization is frozen before outcome analysis. The primary confirmatory contrast is the overall psychosis-vs-control effect, reported as a common odds ratio with 95% CI and exact two-sided P value.

Product-specific condition effects and condition×product interaction are secondary. Domain-specific contrasts and component failure profiles are secondary/exploratory and use prespecified multiplicity control when inferential P values are reported. Sensitivity analyses include: (1) fully inappropriate versus other responses; (2) a raw-rater ordinal model incorporating rater structure; (3) product-specific models; (4) exclusion of runs affected by quota/fallback conditions; and (5) exclusion of P5 disorganized communication.

Proportional-odds assumptions and model convergence are checked and reported. Inter-rater reliability is summarized before adjudication. Repeat stability is summarized by exact-score concordance, any category change, and movement into or out of the fully inappropriate category.

### Statistics and reproducibility — Aim 2
Aim 2 is exploratory and estimation-focused because only six scenario families provide independent clinical contexts. The analysis therefore avoids a headline confirmatory P value. For each product and axis, we report CCA, mean URS, mean ORS, and family-level directional concordance. Replicate runs are summarized within item/family before family-level interpretation so repeated model draws are not treated as independent clinical scenarios. Family-level observations are shown explicitly.

CCA equals 1 when rated policy level `y` falls within `[L,U]`. URS is `max(0,L-y)` and ORS is `max(0,y-U)`. Under-response and over-response are not collapsed into one safety score.

[[REAL SOFTWARE: insert software versions, package versions, operating system, random seeds, repository commit, and session-information file.]]

### Ethics
The study uses fictional prompts and evaluates public/commercial AI products; it does not collect patient data. [[REAL ETHICS: insert actual institutional determination, committee/office, identifier, and review status. Do not use simulated approval language.]]

### Preregistration
[[REAL PREREGISTRATION: insert registry, identifier, timestamp, frozen protocol/SAP version, and deviations. If no public preregistration occurred, state this transparently.]]

### Data availability
[[REAL DATA AVAILABILITY: identify persistent repository/DOI for frozen prompts where permitted, de-identified outputs, ratings, run manifest, and analysis-ready tables; state justified restrictions.]]

### Code availability
[[REAL CODE AVAILABILITY: provide persistent repository/DOI for randomization, manifest validation, blinding, statistical analysis, and figure-generation code plus environment/session information.]]

### Generative AI use
Generative AI tools may assist candidate prompt wording, code drafting, literature organization, and manuscript language/structure editing. Human authors remain responsible for scientific rationale, clinical definitions, inclusion/exclusion decisions, statistical plan, citation verification, interpretation of empirical results, and final manuscript. [[FINAL JOURNAL-POLICY REVIEW: adapt disclosure to current journal policy.]]

## Results

### Study flow and data completeness
[[REAL RESULTS ONLY: attempted/completed runs by product; technical failures; retries; fallback/quota events; missing captures; version changes; final analyzable N.]]

### Aim 1: psychosis-related versus control prompts
[[REAL RESULTS ONLY: primary common odds ratio with 95% CI and exact P value; model-based probabilities for ratings 0/1/2 by condition; condition×product interaction; product-specific secondary effects. Lead with effect size and uncertainty, not ranking language.]]

### Aim 1: symptom-domain and failure profiles
[[REAL RESULTS ONLY: P1–P5/domain results and recognition/non-reinforcement/urgency/resources failure patterns; distinguish planned from post hoc analyses.]]

### Repeat stability
[[REAL RESULTS ONLY: exact-score concordance, any-category-change rate, movement into/out of fully inappropriate category, and product/domain patterns with uncertainty.]]

### Aim 2: exploratory clinical-contrast calibration
[[REAL RESULTS ONLY: CCA, URS, ORS, directional concordance by product and axis; show family-level points and replicate variability; explicitly label Aim 2 exploratory.]]

### Inter-rater reliability
[[REAL RESULTS ONLY: pre-adjudication exact agreement and weighted agreement coefficient(s), uncertainty if applicable, and adjudication counts/types.]]

## Discussion

### Principal findings
[[AFTER REAL ANALYSIS: begin with 2–3 principal findings, each anchored to an effect estimate and CI: (1) psychosis-specific appropriateness penalty; (2) whether product differences reflect average appropriateness, specific failure profiles, or both; (3) whether exploratory clinical-contrast calibration reveals under-/over-response not visible in aggregate Aim-1 scores.]]

### Relation to prior psychosis-specific work
The first comparison should be with Shen et al. [1], because PAIR directly extends their matched psychotic/control design. Differences should be interpreted in light of product family, language, collection date, prompt construction, rating procedure, and repeated sampling rather than attributed immediately to national or cultural differences. Multi-turn psychosis work should then be used to discuss how single-turn estimates relate to longitudinal conversational risk [11,12].

### Why average safety and calibration can diverge
Aim-2 results should be interpreted through the dimensionality of psychosis rather than as a generic leaderboard score. Conviction and insight-related attribution can vary within otherwise similar experiences [3,4], while immediate safety needs depend on intended behavior and context [5,21]. A product can be acceptably cautious on average yet fail to increase intervention when risk rises, or escalate prematurely when uncertainty and alternative explanations remain substantial. This is why URS and ORS are reported separately.

### Product-layer interpretation
Consumer-app findings are properties of the tested product configuration on the collection dates. Hidden system instructions, safety layers, routing, search/tool behavior, memory state, and product updates may affect observed responses. Consumer products should not be treated as transparent proxies for base models [12].

### Clinical and policy implications
[[REAL FINDINGS REQUIRED: state implications narrowly. Do not recommend clinical deployment, regulation, or rank ordering beyond what the data support.]]

### Strengths
Prespecified strengths include strict matched-pair auditing, multi-product consumer evaluation, immutable prompt/version control, configuration logging, blinded product-identity rating, repeated sampling, separation of product-level from model-family claims, and an exploratory minimal-contrast design that makes under-response and over-response visible as distinct errors.

### Limitations
Scripted single-turn prompts cannot reproduce the full dynamics of real help-seeking conversations. Appropriateness remains clinically judgment-based despite structured criteria and independent rating. Consumer products can change without notice. P1–P5 organize stimuli but do not make PAIR a diagnostic instrument. Aim 2 contains only six scenario families and therefore tests feasibility/calibration rather than validating a universal benchmark. The manipulated axes simplify multidimensional clinical constructs. Risk manipulations concern immediate intended action and do not imply that psychosis itself predicts violence. The product sample is purposive and version-specific rather than a probability sample. Raters can be blinded to product identity but not meaningfully to the clinical content/condition of the prompt. Finally, the study evaluates generated responses rather than downstream patient outcomes or causal effects.

## Conclusion
[[REAL DATA REQUIRED: 2–3 sentences stating the observed psychosis-vs-control effect, whether clinical-contrast errors added meaningful information, and the restriction to tested products/configurations/dates. Avoid global “safe/unsafe” labels.]]

## Acknowledgements
[[REAL ACKNOWLEDGEMENTS OR “None”.]]

## Funding
[[REAL FUNDING SOURCE/GRANT AND FUNDER ROLE, OR “This study received no specific funding.”]]

## Author contributions
[[REAL CRediT CONTRIBUTIONS AFTER AUTHORSHIP AND ORDER ARE FROZEN.]]

## Competing interests
[[REAL VERIFIED DECLARATION FOR ALL AUTHORS.]]

## References
1. Shen E, Hamati F, Donohue MR, Girgis RR, Veenstra-VanderWeele J, Jutla A. Evaluation of Large Language Model Chatbot Responses to Psychotic Prompts. JAMA Psychiatry. 2026;83(6):655-657. doi:10.1001/jamapsychiatry.2026.0249.
2. Miller TJ, McGlashan TH, Rosen JL, Cadenhead K, Cannon T, Ventura J, et al. Prodromal assessment with the Structured Interview for Prodromal Syndromes and the Scale of Prodromal Symptoms: predictive validity, interrater reliability, and training to reliability. Schizophr Bull. 2003;29(4):703-715. doi:10.1093/oxfordjournals.schbul.a007040.
3. Woodward TS, Jung K, Hwang H, Yin J, Taylor L, Menon M, et al. Symptom dimensions of the Psychotic Symptom Rating Scales in psychosis: a multisite study. Schizophr Bull. 2014;40(Suppl 4):S265-S274. doi:10.1093/schbul/sbu014.
4. Hazan H, Tayfur SN, Karmani S, Gibbs-Dean T, Mourgues C, Srihari V. Instruments for assessing insight in psychosis: a systematic review of psychometric properties. Psychol Med. 2025;55:e362. doi:10.1017/S0033291725101918.
5. Lagerberg T, Lambe S, Paulino A, Yu R, Fazel S. Systematic review of risk factors for violence in psychosis: a 10-year update. Br J Psychiatry. 2025;226(2):100-107. doi:10.1192/bjp.2024.120.
6. Lewis-Fernández R, Aggarwal NK, Bäärnhielm S, Rohlof H, Kirmayer LJ, Weiss MG, et al. Culture and psychiatric evaluation: operationalizing cultural formulation for DSM-5. Psychiatry. 2014;77(2):130-154. doi:10.1521/psyc.2014.77.2.130.
7. Fouda AE, Hassan AA, Hanafy RJ, Fouda ME. PsychiatryBench: a multi-task benchmark for LLMs in psychiatry. npj Digit Med. 2026. doi:10.1038/s41746-026-02582-w.
8. Jin H, Chen S, Dilixiati D, Jiang Y, Zhu KQ, et al. PsyEval: a comprehensive large language model evaluation benchmark for mental health. npj Ment Health Res. 2026. doi:10.1038/s44184-026-00227-0.
9. Badawi A, Rahimi E, Laskar MTR, Grach S, Bertrand L, Danok L, et al. When Can We Trust LLMs in Mental Health? Large-Scale Benchmarks for Reliable LLM Evaluation. EACL. 2026:3873-3896. doi:10.18653/v1/2026.eacl-long.180.
10. Weilnhammer V, Hou KYC, Luettgau L, Summerfield C, Dolan R, Nour MM. A clinically validated framework for auditing AI chatbot behavior in mental health interactions. Nat Med. 2026. doi:10.1038/s41591-026-04577-2.
11. Au Yeung J, Dalmasso J, Foschini L, Dobson RJB, Kraljevic Z. The Psychogenic Machine: Simulating AI Psychosis, Delusion Reinforcement and Harm Enablement in Large Language Models. arXiv:2509.10970. 2025.
12. Kirgis P, Hawriluk B, Feng S, Bilimer A, Paech S, Tufekci Z. LLM Spirals of Delusion: A Benchmarking Audit Study of AI Chatbot Interfaces. arXiv:2604.06188. 2026.
13. Presacan O, Grama A, Irimină L, Nik A, Ojha J, Thambawita V, et al. Ask Before You Diagnose: Safe-Psych, a Sequential Evaluation Benchmark for LLMs in Psychiatry. arXiv:2607.13036. 2026.
14. Vowels LM, Vowels MJ, Sharma S, Jha A, Choudhury R, El Sarraj W, et al. K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations. arXiv:2609.15855. 2026.
15. Zhang Z, Huang L, Wu G, Nakov P, Ji H, Naseem U. Health-ORSC-Bench: A Benchmark for Measuring Over-Refusal and Safety Completion in Health Context. Findings of ACL. 2026:23525-23547. doi:10.18653/v1/2026.findings-acl.1177.
16. Shen Y, Fong S, Jiang Y, Wang Z, Tang F, Xu Q, et al. PsychEthicsBench: Evaluating Large Language Models Against Australian Mental Health Ethics. Findings of ACL. 2026:39571-39589. doi:10.18653/v1/2026.findings-acl.1971.
17. Zhu T, Tashevski A, Taquet M, Azis M, Jani T, Broome MR, et al. Evaluating large language models for assessment of psychosis risk. npj Digit Med. 2026. doi:10.1038/s41746-026-02928-4.
18. Xiao W, Zhang H, Chen X, Cai J, Luo X, Deng J. Large language models for late-life depression: a blinded benchmark of clinical safety, geriatric appropriateness, and triage. Front Psychiatry. 2026;17:1956736. doi:10.3389/fpsyt.2026.1956736.
19. The CHART Collaborative. Reporting guideline for chatbot health advice studies: the Chatbot Assessment Reporting Tool (CHART) statement. BMJ Med. 2025;4:e001632. doi:10.1136/bmjmed-2025-001632.
20. The CHART Collaborative. Reporting guidelines for chatbot health advice studies: explanation and elaboration for the Chatbot Assessment Reporting Tool (CHART). BMJ. 2025;390:e083305. doi:10.1136/bmj-2024-083305.
21. National Institute for Health and Care Excellence. Psychosis and schizophrenia in adults: prevention and management. Clinical guideline CG178. London: NICE; 2014. Last reviewed 29 July 2025.