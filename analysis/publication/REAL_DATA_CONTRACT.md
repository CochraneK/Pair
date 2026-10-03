# PAIR real-data analysis contract

## Plan A
Required run-level columns:
`run_id, product_id, phase, replicate, case_id, pair_id, sips_domain, condition`

Required adjudicated outcome columns:
`run_id, appropriateness_0_2`

Required raw-rater columns for reliability/sensitivity:
`run_id, rater_id, appropriateness_0_2`

Primary model:
- cumulative-link mixed model;
- psychosis condition is the primary effect;
- product interaction is secondary;
- P5 exclusion sensitivity is prespecified.

## Plans B/C
Required run-level columns:
`run_id, model_or_product, family_id, case_id, axis, level, replicate, policy_level_y`

Clinician item annotations:
`case_id, acceptable_L, acceptable_U`

Clinician pair annotations:
`pair_id, family_id, axis, low_case_id, high_case_id, target_direction, clinically_relevant_change`

Core metrics:
- CCA;
- URS and ORS as ordinal-step distances;
- direct-clinician-direction CDC;
- Relevant Sensitivity;
- violation rates.

Repeated generations estimate stochasticity and must be collapsed within item before clinical family-level interpretation.
