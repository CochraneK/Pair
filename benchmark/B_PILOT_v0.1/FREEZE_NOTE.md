# B-v0.1 freeze note

`B_PILOT_36_v0.1.csv` is now text-frozen for engineering and pilot preparation.

- 6 scenario families
- conviction / insight / behavioral-risk axes
- 2 levels per axis
- 18 minimal pairs / 36 prompts
- automated structural QA passed

`B_POLICY_INTERVALS_ENGINEERING_DEFAULT_v0.1.csv` is deliberately marked as **engineering-only**. It allows runner/statistics smoke tests before clinician review, but it must never be cited as clinician ground truth.

Any prompt edit or policy-interval change after clinician review creates `B-v0.2`; do not overwrite v0.1.