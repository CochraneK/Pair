# Pair-audit script QA

## Run 1
The first heuristic version flagged:
- P2 confrontation mismatch
- P4 medication mismatch

It missed:
- P3 **全部积蓄 vs 一小部分积蓄**

Reason: both prompts contained the same broad `financial` category, so presence/absence matching was insufficient.

## Revision
v2 adds within-category intensity checks:
- financial high vs low
- urgency
- certainty difference (review-only because certainty can be the intended clinical manipulation)

## Run 2
All three protocol example pairs are now flagged for human review.

## Lesson
Automated pair auditing is useful for triage, but semantic/clinical review remains mandatory.
