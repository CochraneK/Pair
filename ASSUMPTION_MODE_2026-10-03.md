# ASSUMPTION MODE — 2026-10-03

## Purpose
The user explicitly instructed the research executor to **proceed as if clinician review of A/B/C items and rubric is acceptable**, so that engineering, preregistration drafting, model/configuration freezing, collection planning, and analysis tooling can continue without waiting.

## What this DOES mean
For workflow execution only:
- A-v0.1 case bank is treated as provisionally accepted for pipeline preparation.
- B-v0.1 36-prompt pilot is treated as provisionally accepted for pipeline preparation.
- C 64-item pilot is treated as provisionally acceptable for pipeline preparation.
- B engineering `[L,U]` defaults may be used for dry-runs and software testing.
- Draft preregistration/SAP/rater manuals may be frozen for review.

## What this DOES NOT mean
This file is **not evidence that a psychiatrist actually reviewed, approved, or signed off** the materials.

Therefore do not write in a manuscript, preregistration, ethics submission, abstract, result, or public claim that:
- clinicians validated the items;
- clinician ground truth was obtained;
- ethics approval/exemption was granted;
- clinical consensus exists;
- the B engineering `[L,U]` defaults are true clinician labels.

## Evidence boundary
Any real clinical sign-off received later must be stored separately with reviewer identity/code, date, item-level judgments, and versioned revisions.

## Version rule
No silent overwrite:
- A textual/clinical revision → `A-v0.2`
- B textual/interval revision → `B-v0.2`
- C clinician-revised pilot → `C-pilot-v0.2`

## Operational consequence
Engineering gates HG2/HG3 are treated as **assumed-pass for execution only**. Formal research claims remain blocked until real evidence exists.
