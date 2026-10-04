# STATUS

**Updated:** 2026-10-04

## Overall

🟢 **Design/engineering preparation is complete, the end-to-end synthetic smoke pipeline has passed, both manuscript tracks have completed a pre-data Reviewer #2 stress test, and the public meeting layer is now bilingual and public-discussion ready. Under user-authorized Assumption Mode, A/B/C remain at real-data execution readiness.**

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
- [x] end-to-end synthetic smoke run passed: 184 outputs
- [x] publication-oriented synthetic analysis/figure rehearsal pipeline
- [x] conversation-exemplar reporting rule and bilingual exemplar modules

## Bilingual public / meeting layer

- [x] English README: `README.md`
- [x] Chinese README: `README.zh-CN.md`
- [x] bilingual maintenance rule: `BILINGUAL_POLICY.md`
- [x] A+B Master v4 available in English + Simplified Chinese
- [x] PAIR-C Master v2 available in English + Simplified Chinese
- [x] bilingual manuscript-state page
- [x] GitHub Pages enabled
- [x] `docs/papers.html` embeds both manuscript tracks with English/中文 switching and conversation exemplars
- [x] `docs/PAIR_C_CLINICIAN_REVIEW.html` is a bilingual clinician-review tool aligned with `[L,U]`, `target_direction`, and `clinically_relevant_change`
- [x] technical index retained separately as `docs/dashboard.html`
- [x] **`docs/index.html` upgraded to v11 as the formal public research-group discussion interface**

### v11 meeting-page refinement

The main Page has been revised in response to three presentation issues: excessive English in the Chinese discussion text, excessive internal/meta information, and insufficient scientific detail in several high-value sections.

v11 therefore:
- uses natural Chinese as the default discussion language, with English retained mainly for proper nouns, first-use terminology, API, and metric abbreviations;
- removes public-facing meta language such as “how to persuade,” “how to open the meeting,” Agent/Git maintenance reminders, and user-specific operating notes;
- expands the scientific content on case refinement, consumer-product vs fixed-API interpretation, clinician tasks, metric interpretation, evidence boundaries, and the two-paper design;
- keeps the paper-like discussion-handbook visual style rather than returning to a dashboard aesthetic;
- preserves the bilingual paper embeds, clinician-review link, simulated figures, conversation examples, and browser-persistent decision board.

Public discussion-page rules are frozen in `MEETING_GUIDE.md` so later iterations should distinguish **public research discussion content** from **internal project-management/meta content**.

Public-facing README, current paper masters, HTML and Pages must remain synchronized across languages.

## Manuscript / submission layer

### Paper 1 — A+B
- [x] submission-structured master created
- [x] canonical English master: `manuscript/PAIR_AB_MASTER_v4_EN.md`
- [x] canonical Chinese master: `manuscript/PAIR_AB_MASTER_v4_ZH.md`
- [x] literature and clinical-theory narrative rebuilt
- [x] CHART map + real-data swap map created
- [x] pre-data Reviewer #2 stress test completed
- [x] prompt-condition blinding overclaim removed; only product identity is a valid blind
- [x] P5 disorganized-communication exclusion sensitivity analysis added
- [x] product sampling-frame / version-break / brand-leakage rules added
- [x] Aim 2 retained as exploratory because six scenario families are the clinical replication units
- [x] manuscript requires representative dialogue examples under a frozen anti-cherry-picking selection rule

### Paper 2 — C
- [x] full companion manuscript master created
- [x] canonical English master: `manuscript/PAIR_C_MASTER_v2_EN.md`
- [x] canonical Chinese master: `manuscript/PAIR_C_MASTER_v2_ZH.md`
- [x] pre-data Reviewer #2 stress test completed
- [x] framing narrowed from exact “boundary location” to response-policy calibration under minimal clinical contrasts
- [x] 0–5 policy scale explicitly treated as ordinal escalation intensity
- [x] URS/ORS treated as ordinal step distances, not interval-scale clinical severity
- [x] CDC requires direct clinician pair-level `target_direction ∈ {-1,0,+1}` rather than `[L,U]` midpoint arithmetic
- [x] CCA explicitly separated from total clinical appropriateness
- [x] ground-truth panel vs response-rating panel separation/freeze rule added
- [x] generic “response policy” removed as a novelty claim
- [x] benchmark-release contamination risk documented
- [x] nuisance invariance remains not estimated in the current 64-item pilot
- [x] manuscript requires at least one interpretable minimal-pair dialogue exemplar selected under a frozen rule

## Plan A — real collection-ready candidate

- [x] 80 matched pairs / 160 prompts across P1–P5
- [x] structural QA and pair audit passed
- [x] frozen as `A-v0.1-provisional`
- [x] 5-product consumer APP set
- [x] stratified 16-item psychosis stability subset
- [x] collection design: 960 outputs
- [x] preregistration draft + confirmatory analysis script
- [x] synthetic engineering smoke passed

## Plan B — real pilot-ready candidate

- [x] 6 families × 3 axes × 2 levels = 36 prompts
- [x] 18 minimal pairs
- [x] frozen as `B-v0.1-provisional`
- [x] 3 APP products × 3 runs/item = 324 outputs
- [x] boundary/calibration metrics ready
- [x] synthetic engineering smoke passed

## Plan C — real API pilot-ready candidate

- [x] 64 prompts = 8 families × 4 axes × 2 levels
- [x] fixed API candidate configurations + runner
- [x] planned 576 outputs
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

Current prompt banks use **fictional/synthetic research prompts**, not raw patient clinical records.

## Immediate next empirical step

Use the v11 meeting Page to finalize team decisions, then run the real technical smoke pilot with frozen prompts/settings:
- A: 100 real APP smoke outputs
- B: 36 real APP smoke outputs
- C: 48 real API smoke outputs after real clinician review fields are completed/frozen

After real data: frozen statistics → empirical tables/figures → populate Results/Discussion → Reviewer #2 rerun → final CHART/Nature Portfolio reporting audit → submission.
