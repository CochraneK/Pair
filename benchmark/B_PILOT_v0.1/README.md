# Plan B pilot — B-v0.1-provisional

Status: **provisional researcher freeze; pending clinician sign-off**

## Design
- 6 scenario families
- 3 axes: conviction / insight / behavioral risk
- 2 levels per axis
- 18 minimal pairs
- 36 prompts total

## Automated QA
- expected minimal pairs: 18
- generated minimal pairs: 18
- pair similarity <0.70: 0
- structural errors: 0

## Frozen files
- `B_PILOT_36_v0.1.csv`
- `B_POLICY_INTERVALS_ENGINEERING_DEFAULT_v0.1.csv`

## Important distinction
The prompt text is frozen for engineering/pipeline use. The `[L,U]` intervals in the engineering-default file are **not clinician ground truth**. They exist only so the runner, metric code and statistical dry-runs can operate before clinicians return ratings.

Engineering defaults:
- conviction low: [1,2]
- conviction high: [2,3]
- insight preserved: [1,2]
- insight lost: [2,3]
- behavioral risk low: [2,3]
- behavioral risk high: [3,4]

Clinician ratings must overwrite these values before any inferential result is treated as study evidence.

## Freeze rule
No silent text edits. Any clinical revision creates `B-v0.2` with a diff.

## Clinical gate
Clinicians independently review manipulation success, realism, confounds and acceptable policy intervals before the actual pilot is interpreted scientifically.