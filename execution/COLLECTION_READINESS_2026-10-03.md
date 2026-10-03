# PAIR collection readiness — 2026-10-03

## Current state
Under user-authorized **Assumption Mode**, clinical item/rubric review is treated as acceptable for workflow execution, without claiming that real clinician sign-off occurred.

## Ready now
### Plan A
- 80 matched pairs / 160 prompts frozen as A-v0.1-provisional
- APP SOP frozen candidate
- 5-product candidate set frozen
- 16-item stratified stability subset frozen
- deterministic collection schedule defined
- expected outputs: 960
- rater manual ready
- Plan-A CLMM analysis script ready

### Plan B
- 36 prompts / 18 minimal pairs frozen as B-v0.1-provisional
- 3-product pilot set frozen
- engineering `[L,U]` intervals available for pipeline execution
- deterministic collection schedule defined
- expected outputs: 324
- boundary metric code already smoke-tested

### Plan C
- 64-prompt pilot structurally validated
- 3 fixed API configurations frozen candidate
- reasoning-enabled request settings documented
- deterministic collection schedule defined
- expected outputs: 576
- OpenAI-compatible API runner implemented
- boundary metrics implemented and smoke-tested

## Total planned output volume
**1,860 model/product responses** if A+B+C are all executed exactly as currently specified.

## Still requires real-world action
1. institutional ethics determination — draft prepared, not granted;
2. preregistration submission — draft prepared, not registered;
3. consumer APP collection — requires actual product sessions/accounts;
4. Plan C API run — requires provider API keys and workspace/base URL where applicable;
5. clinician rating — rating manual/tools ready, but no real ratings have been generated;
6. any claim that clinician ground truth exists requires actual sign-off evidence.

## Result status
There are **zero real performance results** at this point. Existing results are software/structure dry-runs only.

## Recommended immediate operational order
1. submit ethics determination request;
2. submit/freeze Plan A+B preregistration;
3. snapshot APP product settings and accounts;
4. run a 5–10 item APP smoke pilot to detect UI/quota/fallback problems;
5. run a 5–10 item C API smoke pilot to detect provider/request incompatibility;
6. if both pass, execute frozen schedules;
7. build blinded rating pack;
8. obtain ratings;
9. run frozen analysis scripts;
10. CHART audit + Reviewer-2 audit + submission literature refresh.
