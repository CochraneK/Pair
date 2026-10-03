# Submission readiness after Reviewer #2 stress test

| Domain | A+B v4 | C v2 |
|---|---|---|
| Scientific question | strong | strong / more novel |
| Clinical grounding | strong | strong |
| Literature positioning | strong | strong, but novelty search must remain current |
| Prompt construct validity | moderate-strong; P5 sensitivity required | highest risk: axis separation and evidence/plausibility |
| Blinding | product-only, correctly stated | configuration-blinded response rating |
| Human ground truth | pending real clinician evidence | pending real clinician intervals + target directions |
| Clinical replication unit | matched pair/prompt | 8 scenario families |
| Repeated generations | stability only | stochasticity only |
| Statistical role | confirmatory primary ordinal model | estimation-focused pilot |
| Main overclaim risk | product ranking / base-model claims | exact boundary claims / ordinal-distance claims / universal benchmark claims |
| Real-data readiness | high | high after revised clinician schema |

## C clinician schema must contain before real outputs
- raw clinician `[L,U]`;
- pair-level `target_direction ∈ {-1,0,+1}`;
- `clinically_relevant_change` yes/no;
- manipulation success;
- unintended second-axis change;
- major confound;
- contraindicated behaviors.

## Both papers remain blocked from submission until
- actual ethics determination;
- public preregistration or transparent non-registration statement;
- real model/product outputs only;
- real human ratings and pre-adjudication agreement;
- exact version/configuration manifests;
- frozen analysis and software/session information;
- Data + Code Availability;
- final CHART mapping where applicable;
- Reviewer #2 rerun after empirical Results and Discussion are populated.
