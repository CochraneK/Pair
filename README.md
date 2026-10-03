# PAIR

**PAIR = Psychosis AI Response**

A research workspace for evaluating how consumer AI chat products respond to psychosis-related content.

## Current state

PAIR supports three routes without silently changing the original student's research question:

- **Plan A** — keep the original question and make the consumer-product audit methodologically clean.
- **Plan B** — keep the original Aim 1 and add a small counterfactual clinical-boundary substudy. **Current methodological recommendation, pending team decision.**
- **Plan C** — explicitly change the research question and build a psychosis-specific response-boundary benchmark.

Start here:

1. `CANONICAL_HANDOFF.md`
2. `STATUS.md`
3. `DECISIONS_LOG.md`
4. `DECISION_TREE.md`
5. `TASKS.yaml`

## Research principles

- APP results are **consumer-product snapshots**, not stable properties of a base model.
- Hidden system prompts, safety layers, routing and product UX logic are part of the tested consumer product.
- Clinical ground truth must be approved by clinicians.
- New ideas are preserved in `IDEA_POOL.md`; they do not automatically enter the frozen study.
- Brainstorm first, preserve ideas, then falsify novelty, prioritize, freeze and execute.
- Do not commit credentials, API keys, raw account information, or personally identifying data.

## Public-repository rule

This repository may be public. Public does **not** mean everything belongs in Git.

Default exclusions:
- API keys / tokens
- account identifiers
- raw private screenshots
- private or identifiable clinical material
- non-public data under restricted licences

Use manifests/hashes for large or sensitive raw assets.

## Current blockers

- **HG1:** team selects Plan A / B / C
- full 160-prompt set is not yet present in the available v0.1 protocol
- clinician item/rubric approval
- ethics determination
- preregistration freeze
