# PAIR

**PAIR = Psychosis AI Response**

A publication-oriented research workspace for evaluating how consumer AI chat products and fixed API model configurations respond to psychosis-related content.

## Current state

As of 2026-10-03, **design/engineering preparation is effectively complete**.

Operational structure:
- **Plan A** — main consumer-product audit; 80 matched pairs / 160 prompts; collection-ready candidate.
- **Plan B** — nested clinical-boundary enhancement; 36 prompts / 18 minimal pairs; collection-ready pilot candidate.
- **Plan C** — separate psychosis response-boundary benchmark track; 64-prompt fixed-API pilot candidate.

Under [`ASSUMPTION_MODE_2026-10-03.md`](ASSUMPTION_MODE_2026-10-03.md), clinical item/rubric review is treated as acceptable **for workflow execution only**. This is not evidence that clinicians actually signed off.

## Start here

1. [`STATUS.md`](STATUS.md)
2. [`CANONICAL_HANDOFF.md`](CANONICAL_HANDOFF.md)
3. [`TASKS.yaml`](TASKS.yaml)
4. [`DECISIONS_LOG.md`](DECISIONS_LOG.md)
5. [`execution/COLLECTION_READINESS_2026-10-03.md`](execution/COLLECTION_READINESS_2026-10-03.md)
6. [`execution/EXECUTION_PLAN_v0.1.md`](execution/EXECUTION_PLAN_v0.1.md)

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
8. final CHART / Reviewer-2 / literature-refresh checks.

There are currently **no real model-performance results** in this repository; existing dry-runs are software/structure validation only.
