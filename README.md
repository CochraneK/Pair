# PAIR

[English](README.md) | [简体中文](README.zh-CN.md)

**PAIR = Psychosis AI Response**

A publication-oriented research workspace for evaluating how consumer AI chat products and fixed API model configurations respond to psychosis-related content.

> **Bilingual rule:** public-facing README, manuscript masters, HTML and GitHub Pages must be maintained in synchronized English and Simplified Chinese versions. See [`BILINGUAL_POLICY.md`](BILINGUAL_POLICY.md).

## Current state

As of 2026-10-03, **design/engineering preparation is effectively complete**.

Operational structure:
- **Plan A** — main consumer-product audit; 80 matched pairs / 160 prompts; collection-ready candidate.
- **Plan B** — prespecified exploratory clinical-contrast substudy nested in Paper 1; 36 prompts / 18 minimal pairs.
- **Plan C** — separate psychosis-specific response-policy calibration paper; 64-prompt fixed-API pilot candidate.

Current paper masters:
- **Paper 1 — A+B:** [`English`](manuscript/PAIR_AB_MASTER_v4_EN.md) | [`简体中文`](manuscript/PAIR_AB_MASTER_v4_ZH.md)
- **Paper 2 — C:** [`English`](manuscript/PAIR_C_MASTER_v2_EN.md) | [`简体中文`](manuscript/PAIR_C_MASTER_v2_ZH.md)

Under [`ASSUMPTION_MODE_2026-10-03.md`](ASSUMPTION_MODE_2026-10-03.md), clinical item/rubric review is treated as acceptable **for workflow execution only**. This is not evidence that clinicians actually signed off.

## Start here

1. [`docs/index.html`](docs/index.html) — paper-like discussion handbook used as the GitHub Pages landing page
2. [`docs/dashboard.html`](docs/dashboard.html) — technical project index
3. [`STATUS.md`](STATUS.md)
4. [`CANONICAL_HANDOFF.md`](CANONICAL_HANDOFF.md)
5. [`TASKS.yaml`](TASKS.yaml)
6. [`DECISIONS_LOG.md`](DECISIONS_LOG.md)
7. [`manuscript/CURRENT_PAPERS.md`](manuscript/CURRENT_PAPERS.md)

## Papers

### Paper 1 — A+B
**Consumer-product psychosis audit + exploratory clinical-contrast substudy**

- English master: [`manuscript/PAIR_AB_MASTER_v4_EN.md`](manuscript/PAIR_AB_MASTER_v4_EN.md)
- 中文主稿: [`manuscript/PAIR_AB_MASTER_v4_ZH.md`](manuscript/PAIR_AB_MASTER_v4_ZH.md)
- Reviewer #2 audit: [`manuscript/REVIEWER2_AB_v1.md`](manuscript/REVIEWER2_AB_v1.md)
- Simulation-results rehearsal: [`English`](manuscript/simulation/PAIR_AB_REHEARSAL_RESULTS_EN.md) | [`中文`](manuscript/simulation/PAIR_AB_REHEARSAL_RESULTS_ZH.md)

### Paper 2 — C
**Psychosis-specific response-policy calibration under minimal clinical contrasts**

- English master: [`manuscript/PAIR_C_MASTER_v2_EN.md`](manuscript/PAIR_C_MASTER_v2_EN.md)
- 中文主稿: [`manuscript/PAIR_C_MASTER_v2_ZH.md`](manuscript/PAIR_C_MASTER_v2_ZH.md)
- Reviewer #2 audit: [`manuscript/REVIEWER2_C_v1.md`](manuscript/REVIEWER2_C_v1.md)
- Simulation-results rehearsal: [`English`](manuscript/simulation/PAIR_C_REHEARSAL_RESULTS_EN.md) | [`中文`](manuscript/simulation/PAIR_C_REHEARSAL_RESULTS_ZH.md)

## Publication analysis

The manuscript-facing analysis layer is in [`analysis/publication/`](analysis/publication/):
- `plan_a_primary_clmm.R` — cumulative-link mixed model for the real Plan-A primary analysis;
- `plan_bc_family_aware_analysis.py` — item-first / family-aware calibration analysis for B/C;
- `make_publication_figures.py` — figure generation from frozen analysis tables;
- `REAL_DATA_CONTRACT.md` — required real-data columns and merge contracts.

A synthetic rehearsal has already been run to test the figure/manuscript pipeline. Existing synthetic numbers and dry-run figures are **not empirical results**.

## Frozen/candidate research assets

### Plan A
- `benchmark/A_CASES_v0.1/`
- `routes/A/PROTOCOL_READY.md`
- `routes/A/SAP_AND_RESULTS_TEMPLATE.md`
- `analysis/plan_a_analysis.R`

### Plan B
- `benchmark/B_PILOT_v0.1/`
- `routes/B/PROTOCOL_AND_PILOT_READY.md`
- `routes/B/SAP_AND_RESULTS_TEMPLATE.md`
- `scripts/boundary_metrics.py`

### Plan C
- `routes/C/PILOT_BLUEPRINTS_64.csv`
- `routes/C/BENCHMARK_AND_PILOT_READY.md`
- `routes/C/METRICS_AND_RESULTS_TEMPLATE.md`
- `configs/C_API_PILOT_REQUESTS_v0.1.json`
- `scripts/api_pilot_runner.py`

## HTML / GitHub Pages

GitHub Pages is enabled for this repository.

- [`docs/index.html`](docs/index.html) is intentionally a **paper-like discussion handbook** for supervisors/students, using the earlier non-dashboard visual language.
- [`docs/dashboard.html`](docs/dashboard.html) preserves the compact technical navigation/index view.
- [`docs/PAIR_C_CLINICIAN_REVIEW.html`](docs/PAIR_C_CLINICIAN_REVIEW.html) is the bilingual clinician-review tool.

The Page must expose both English and Chinese README, papers, study state and discussion material.

## Preregistration / ethics

Prepared:
- [`preregistration/PLAN_AB_PREREGISTRATION_DRAFT_v0.1.md`](preregistration/PLAN_AB_PREREGISTRATION_DRAFT_v0.1.md)
- [`ethics/ETHICS_DETERMINATION_REQUEST_DRAFT.md`](ethics/ETHICS_DETERMINATION_REQUEST_DRAFT.md)

These are drafts. No ethics determination or preregistration status is implied until a real institution/registry provides it.

## Execution volume

Current frozen candidate schedules:
- Plan A: **960** outputs
- Plan B: **324** outputs
- Plan C: **576** outputs
- Total if all tracks run: **1,860** outputs

Schedules are generated deterministically by `scripts/build_collection_schedules.py`.

## Rating

Unified blinded rating manual:
- `rating/RATER_MANUAL_v0.1.md`

Blinded-pack generator:
- `scripts/build_blinded_rating_pack.py`

## Research principles

- APP results are **consumer-product snapshots**, not stable properties of a base model.
- APP and API are separate execution strata.
- Clinical ground truth cannot be fabricated by an AI executor.
- Brainstorm first; preserve ideas; falsify novelty; prioritize; freeze; execute.
- No silent edits after freeze: every substantive change receives a new version and diff.
- Public-facing README, papers, HTML and Pages are bilingual by default.
- Do not commit credentials, API keys, account identifiers, raw private screenshots or identifiable clinical data.

## Public-repository rule

This repository may be public, but sensitive/raw operational material does not automatically belong in Git.

Default exclusions:
- API keys / tokens
- account identifiers
- raw private screenshots
- restricted/identifiable clinical material
- third-party source documents without redistribution permission

See [`DATA_POLICY.md`](DATA_POLICY.md).

## Real-world actions still required

The project is no longer blocked by missing design work. It is blocked only by real execution steps:
1. obtain institutional ethics determination;
2. submit/timestamp preregistration;
3. snapshot consumer-product settings/accounts;
4. run A/B APP smoke pilot and then full collection;
5. supply API credentials/workspace config for C smoke/full pilot;
6. obtain real clinician ratings/sign-off if making clinician-validation claims;
7. run frozen analysis on real data;
8. regenerate empirical tables/figures, rewrite Results/Discussion, then run final CHART / Reviewer-2 / literature-refresh checks.

There are currently **no real model-performance results** in this repository; existing synthetic/dry-run artifacts are software, structure, analysis, and manuscript rehearsal only.
