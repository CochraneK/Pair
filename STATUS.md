# STATUS

**Updated:** 2026-10-03

## Overall

🟢 **Design/engineering preparation is now effectively complete. Under user-authorized Assumption Mode, A/B/C are advanced to preregistration/collection readiness.**

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
- [x] boundary metrics implemented and synthetic smoke-tested
- [x] unified blinded rater manual candidate
- [x] deterministic collection-schedule generator
- [x] blinded rating-pack generator
- [x] Plan A CLMM analysis script

## Plan A — collection-ready candidate

- [x] 80 matched pairs / 160 prompts generated
- [x] P1–P5 each contain 16 pairs / 32 prompts
- [x] structural QA passed
- [x] heuristic non-target risk mismatch after cleanup: 0
- [x] text frozen as `A-v0.1-provisional`
- [x] 5-product consumer APP set frozen candidate: DeepSeek / 豆包 / Kimi / 通义千问 / 腾讯元宝
- [x] stratified 16-item psychosis stability subset frozen
- [x] collection design fixed: 960 outputs total
- [x] preregistration draft prepared
- [x] confirmatory analysis script prepared

## Plan B — collection-ready pilot candidate

- [x] 6 families × 3 axes × 2 levels = 36 prompts
- [x] 18/18 minimal-pair structure passed
- [x] text frozen as `B-v0.1-provisional`
- [x] engineering `[L,U]` intervals available under Assumption Mode
- [x] 3-product pilot set: DeepSeek / 豆包 / 通义千问
- [x] 3 independent runs/item/product
- [x] collection design fixed: 324 outputs total
- [x] boundary analysis metrics/code ready

## Plan C — fixed-API pilot candidate

- [x] narrow novelty/scoping review
- [x] clinical ontology v0.1
- [x] 64 prompts: 8 families × 4 axes × 2 levels
- [x] structural validator passed
- [x] fixed API candidate configurations verified on 2026-10-03:
  - DeepSeek `deepseek-flash` / V4.1-Flash
  - Qwen `qwen3.8-max-0902`
  - Doubao `doubao-seed-2-1-pro-260915`
- [x] reasoning-enabled request settings candidate frozen
- [x] API runner implemented
- [x] collection design fixed: 576 outputs total
- [x] boundary metrics ready

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

## What still requires real-world execution

1. institutional ethics determination;
2. preregistration submission/freeze;
3. APP settings/account snapshot at collection time;
4. actual consumer-product querying for A/B;
5. API credentials/workspace configuration and actual Plan-C API calls;
6. actual clinician ratings/sign-off if the manuscript claims clinician validation/ground truth;
7. frozen statistical analysis on real ratings;
8. CHART audit, Reviewer-2 audit and pre-submission literature refresh.

## Immediate next step

Do **small technical smoke pilots before full collection**:
- A/B: 5–10 prompts across the selected consumer products to detect UI, quota, fallback and capture problems;
- C: 5–10 scheduled calls across all three fixed API configurations to detect provider/request incompatibilities.

If the smoke pilots pass, execute the frozen schedules without changing prompts/rubric/statistics.

## Result boundary

There are currently **no real model-performance results**. Existing outputs labelled dry-run/synthetic validate software and study structure only.
