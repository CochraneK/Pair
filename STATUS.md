# STATUS

**Updated:** 2026-10-03

## Overall

🟢 **Design/engineering preparation is complete, the end-to-end synthetic smoke pipeline has passed, both manuscript tracks have completed a pre-data Reviewer #2 stress test, and the public publication layer is now bilingual. Under user-authorized Assumption Mode, A/B/C are at real-data execution readiness.**

Operational framing:

> **Paper 1 = A primary product audit + B prespecified exploratory substudy.**  
> **Paper 2 = C psychosis-specific response-policy calibration benchmark pilot.**

See `ASSUMPTION_MODE_2026-10-03.md` for the evidence boundary: workflow may proceed under assumed clinical acceptance, but real clinician sign-off/ethics/preregistration/results must never be fabricated.

## Completed foundation

- [x] public collaboration-safe repository initialized
- [x] original protocol reconstructed/audited
- [x] A/B/C decision architecture + canonical handoff
- [x] APP SOP + API-ready architecture
- [x] literature/novelty refresh + CHART precheck + statistics review
- [x] pair-audit / randomization / manifest-validation tooling
- [x] boundary/calibration metrics + smoke tests
- [x] blinded rater manual candidate
- [x] deterministic collection schedules
- [x] Plan A CLMM analysis script
- [x] **end-to-end synthetic smoke run passed: 184 outputs**

## Bilingual public layer

- [x] English README: `README.md`
- [x] Chinese README: `README.zh-CN.md`
- [x] bilingual maintenance rule: `BILINGUAL_POLICY.md`
- [x] A+B Master v4 available in English + Simplified Chinese
- [x] PAIR-C Master v2 available in English + Simplified Chinese
- [x] bilingual manuscript-state page
- [x] bilingual `docs/index.html` dashboard with English/中文 switch
- [x] PAIR-C clinician review HTML rebuilt as a valid bilingual tool
- [x] clinician review HTML aligned with revised C schema: `[L,U]`, `target_direction`, `clinically_relevant_change`
- [x] GitHub Pages enabled (`has_pages: true` at latest repository check)

Public-facing README, current paper masters, HTML and Pages must remain synchronized across languages.

## Manuscript / submission layer

### Paper 1 — A+B
- [x] submission-structured master created
- [x] canonical English master: `manuscript/PAIR_AB_MASTER_v4_EN.md`
- [x] canonical Chinese master: `manuscript/PAIR_AB_MASTER_v4_ZH.md`
- [x] literature and clinical-theory narrative rebuilt
- [x] CHART map + real-data swap map created
- [x] pre-data Reviewer #2 stress test completed: `manuscript/REVIEWER2_AB_v1.md`
- [x] reviewer corrections frozen in manuscript logic as **A+B v4**: `manuscript/V4_STATUS.md`
- [x] prompt-condition blinding overclaim removed; only product identity is a valid blind
- [x] P5 disorganized-communication exclusion sensitivity analysis added
- [x] product sampling-frame / version-break / brand-leakage rules added
- [x] Aim 2 retained as exploratory because six scenario families are the clinical replication units

### Paper 2 — C
- [x] full companion manuscript master created
- [x] canonical English master: `manuscript/PAIR_C_MASTER_v2_EN.md`
- [x] canonical Chinese master: `manuscript/PAIR_C_MASTER_v2_ZH.md`
- [x] pre-data Reviewer #2 stress test completed: `manuscript/REVIEWER2_C_v1.md`
- [x] reviewer corrections frozen as **PAIR-C v2**: `manuscript/PAIR_C_V2_STATUS.md`
- [x] framing narrowed from exact “boundary location” to **response-policy calibration under minimal clinical contrasts**
- [x] 0–5 policy scale explicitly treated as ordinal escalation intensity
- [x] URS/ORS treated as ordinal step distances, not interval-scale clinical severity
- [x] CDC now requires direct clinician pair-level `target_direction ∈ {-1,0,+1}` rather than `[L,U]` midpoint arithmetic
- [x] CCA explicitly separated from total clinical appropriateness
- [x] ground-truth panel vs response-rating panel separation/freeze rule added
- [x] generic “response policy” removed as a novelty claim
- [x] benchmark-release contamination risk documented
- [x] nuisance invariance remains **not estimated** in the current 64-item pilot

Combined readiness matrix: `manuscript/SUBMISSION_READINESS_AFTER_R2.md`.

Formatted local DOCX masters have been rendered and visually QA-checked page-by-page. They are **not submission-ready until all highlighted real-world placeholders are resolved**.

## Plan A — real collection-ready candidate

- [x] 80 matched pairs / 160 prompts across P1–P5
- [x] structural QA and pair audit passed
- [x] frozen as `A-v0.1-provisional`
- [x] 5-product consumer APP set
- [x] stratified 16-item psychosis stability subset
- [x] collection design: **960 outputs**
- [x] preregistration draft + confirmatory analysis script
- [x] synthetic engineering smoke for 100-output subset passed

## Plan B — real pilot-ready candidate

- [x] 6 families × 3 axes × 2 levels = 36 prompts
- [x] 18 minimal pairs
- [x] frozen as `B-v0.1-provisional`
- [x] 3 APP products × 3 runs/item = **324 outputs**
- [x] boundary/calibration metrics ready
- [x] synthetic engineering smoke for 36-output subset passed

## Plan C — real API pilot-ready candidate

- [x] 64 prompts = 8 families × 4 axes × 2 levels
- [x] fixed API candidate configurations + runner
- [x] planned **576 outputs**
- [x] evidence/plausibility corrected as a clinically relevant axis, not nuisance
- [x] positive and negative target directions supported
- [x] NI explicitly `NA` until a true nuisance module is frozen
- [x] revised clinician schema includes raw `[L,U]`, pair-level `target_direction`, `clinically_relevant_change`, manipulation success, second-axis change, major confound, and contraindicated behaviors
- [x] bilingual clinician-review HTML exports fields aligned with the revised schema

## Execution volume

- A: 960
- B: 324
- C: 576
- **Total: 1,860 outputs**

Canonical details: `execution/EXECUTION_PLAN_v0.1.md`.

## Preregistration / ethics

- [x] A+B preregistration draft prepared
- [x] institutional ethics-determination request draft prepared
- [ ] real institutional determination obtained
- [ ] real preregistration submitted/timestamped or transparent non-registration statement finalized

## Result boundary

There are currently **no real model-performance results**. Synthetic/mock and realistic-simulation data are engineering/manuscript rehearsal only and must never be reported as empirical findings.

## Immediate next step

Run the **real technical smoke pilot** with frozen prompts/settings, then full collection if authentication/UI/quota/API checks pass:
- A: 100 real APP smoke outputs
- B: 36 real APP smoke outputs
- C: 48 real API smoke outputs after real clinician review fields are completed/frozen

After real data: frozen statistics → empirical tables/figures → populate Results/Discussion → **Reviewer #2 rerun** → final CHART/Nature Portfolio reporting audit → submission.