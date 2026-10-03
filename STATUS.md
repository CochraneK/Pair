# STATUS

**Updated:** 2026-10-03

## Overall

🟢 **Design/engineering preparation is complete and the end-to-end synthetic smoke pipeline has passed. Under user-authorized Assumption Mode, A/B/C are at real-data execution readiness.**

Operational framing:

> **A = main product-audit paper; B = nested active enhancement; C = separate fixed-API high-ceiling benchmark track.**

See `ASSUMPTION_MODE_2026-10-03.md` for the evidence boundary: clinical review is treated as acceptable for workflow execution only; this does **not** fabricate real clinician sign-off.

## Completed foundation

- [x] Public collaboration-safe GitHub repository initialized
- [x] Original protocol reconstructed and audited
- [x] Canonical handoff + A/B/C decision architecture
- [x] APP SOP + API-ready architecture
- [x] literature/novelty refresh + CHART precheck + statistics review
- [x] pair-audit / randomization / manifest-validation tooling
- [x] boundary metrics implemented and smoke-tested
- [x] unified blinded rater manual candidate
- [x] deterministic collection-schedule generator
- [x] blinded rating-pack generator
- [x] Plan A CLMM analysis script
- [x] **end-to-end synthetic smoke run passed: 184 outputs**
- [x] synthetic run → blind pack → rating schema → boundary metrics chain validated

## Plan A — real collection-ready candidate

- [x] 80 matched pairs / 160 prompts generated
- [x] P1–P5 each contain 16 pairs / 32 prompts
- [x] structural QA passed
- [x] heuristic non-target risk mismatch after cleanup: 0
- [x] text frozen as `A-v0.1-provisional`
- [x] 5-product consumer APP set: DeepSeek / 豆包 / Kimi / 通义千问 / 腾讯元宝
- [x] stratified 16-item psychosis stability subset frozen
- [x] collection design fixed: **960 outputs**
- [x] preregistration draft prepared
- [x] confirmatory analysis script prepared
- [x] smoke subset fixed: 20 prompts × 5 products = 100 outputs; engineering chain passed on synthetic fixture

## Plan B — real pilot-ready candidate

- [x] 6 families × 3 axes × 2 levels = 36 prompts
- [x] 18/18 minimal-pair structure passed
- [x] text frozen as `B-v0.1-provisional`
- [x] engineering `[L,U]` intervals available under Assumption Mode
- [x] 3-product pilot set: DeepSeek / 豆包 / 通义千问
- [x] 3 independent runs/item/product
- [x] collection design fixed: **324 outputs**
- [x] boundary analysis metrics/code ready
- [x] smoke subset fixed: 12 prompts × 3 products = 36 outputs; engineering chain passed on synthetic fixture

## Plan C — real API pilot-ready candidate

- [x] narrow novelty/scoping review
- [x] clinical ontology v0.1
- [x] 64 prompts: 8 families × 4 axes × 2 levels
- [x] structural validator passed
- [x] fixed API candidate configurations verified on 2026-10-03
- [x] API runner implemented
- [x] collection design fixed: **576 outputs**
- [x] boundary metrics ready
- [x] smoke subset fixed: 16 prompts × 3 configs = 48 outputs
- [x] smoke run exposed and corrected one design bug: `evidence/plausibility` is a clinically relevant axis, **not** a nuisance-invariance axis
- [x] corrected metric dry-run handles positive and negative expected policy shifts
- [x] NI is now explicitly `NA` for the 64-item pilot unless a separate nuisance module is frozen

Correction record: `routes/C/DESIGN_CORRECTION_EVIDENCE_AXIS_2026-10-03.md`.

## Execution volume

- A: 960 outputs
- B: 324 outputs
- C: 576 outputs
- **Total if all executed: 1,860 outputs**

Canonical details: `execution/EXECUTION_PLAN_v0.1.md`.

## Preregistration / ethics

- [x] Plan A+B preregistration draft prepared: `preregistration/PLAN_AB_PREREGISTRATION_DRAFT_v0.1.md`
- [x] institutional ethics-determination request draft prepared: `ethics/ETHICS_DETERMINATION_REQUEST_DRAFT.md`
- [ ] real institutional determination obtained
- [ ] real preregistration submitted/timestamped

## Smoke result

Engineering smoke report: `results/SMOKE_RUN_V1_2026-10-03.md`.

This run used **synthetic/mock responses only**. It validates plumbing, not model quality.

## What still requires real-world execution

1. real institutional ethics determination if required by local policy;
2. real preregistration submission/timestamp;
3. APP settings/account snapshot at collection time;
4. actual consumer-product querying for A/B;
5. API credentials and actual C API calls;
6. real clinician ratings/sign-off if manuscript claims clinical validation/ground truth;
7. frozen statistics on real ratings;
8. CHART audit, Reviewer-2 audit and pre-submission literature refresh.

## Immediate next step

**Run the real technical smoke pilot using the already frozen 184-output subset.**

- A: 100 real APP outputs
- B: 36 real APP outputs
- C: 48 real API outputs

If real authentication/UI/quota/API compatibility passes, execute the full frozen 1,860-output schedules without changing prompts, rubric or primary analyses.

## Result boundary

There are currently **no real model-performance results**. All existing smoke/dry-run values are synthetic engineering validation only.