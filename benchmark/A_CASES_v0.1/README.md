# Plan A case bank — A-v0.1-provisional

Status: **provisional frozen case bank; AI-generated; pending clinician review**

## Contents
- 80 matched pairs
- 160 prompts total
- P1–P5: 16 pairs / 32 prompts per domain
- language: zh-CN
- intended behavioral-risk level: predominantly low

Files:
- `A_CASES_P1_32_v0.1.csv`
- `A_CASES_P2_32_v0.1.csv`
- `A_CASES_P3_32_v0.1.csv`
- `A_CASES_P4_32_v0.1.csv`
- `A_CASES_P5_32_v0.1.csv`

The combined local CSV SHA-256 at freeze was:
`053f3e03b10ea7fe137f9c08d1b0dc2e5d2bafcfa5e610e8ad083f95ff3f198e`

## Automated QA
- structural pairs: **80/80**
- very-low textual similarity (<0.35): **0**
- major length imbalance (>35%): **0**
- heuristic non-target risk mismatches after final lexical cleanup: **0**

P5 is special: discourse organization is itself the manipulated feature, so lower wording similarity is expected and is not automatically a defect.

## Provenance
These are newly synthesized fictional prompts created for PAIR. They are **not copied from SIPS interview wording, published case reports, or existing benchmark items**. SIPS P1–P5 is used only as a domain-level organizing taxonomy.

## Freeze rule
No silent edits. Any textual change after this commit requires a new version (`A-v0.2`, etc.) and a documented diff.

## Clinical gate
Before preregistration/main data collection, clinicians must still confirm:
- domain fit
- realism
- symptom severity
- matched-control appropriateness
- absence of unintended second clinical cues
- cultural appropriateness where relevant

This file makes the bank executable and versioned; it does not substitute for clinician sign-off.