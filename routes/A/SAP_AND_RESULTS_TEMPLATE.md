# Plan A — SAP candidate + results shell

> Status: analysis-plan candidate. Statistician review required before preregistration.

## Data unit
One clinician rating of one product response to one prompt.

Required identifiers:
- `pair_id`
- `prompt_id`
- `condition` = psychotic/control
- `sips_domain`
- `product_id`
- `run_id`
- `rater_id`

## Primary outcome
Ordinal appropriateness: 0 / 1 / 2.

## Candidate primary model
Cumulative-link mixed model (logit link):

`appropriateness ~ condition * product + sips_domain + (1|pair_id) + (1|prompt_id)`

Rationale:
- `pair_id` preserves the matched design
- `prompt_id` accounts for the same prompt being queried across products/runs
- `condition * product` tests whether the psychosis penalty differs by product

If all raw rater observations are modelled directly, add rater structure or use a prespecified consensus/adjudicated primary outcome plus raw-rater sensitivity analysis.

## Sensitivity analyses
1. binary fully-inappropriate vs other
2. product-specific condition effects
3. raw-rater model including rater effect
4. repeat-subset only for stability
5. bilingual subset only as secondary sensitivity

## Multiplicity
Primary confirmatory test: overall psychosis-condition effect.
Product interaction and SIPS/component analyses are secondary unless separately powered and preregistered.

## Effect reporting
Prefer estimates + uncertainty over rank-only reporting:
- common odds ratio / model-based marginal probabilities
- 95% CI
- absolute probability of score 2
- paired product/domain contrasts where prespecified

## Reliability
Report clinician agreement before adjudication, e.g. weighted kappa and/or ICC appropriate to ordinal ratings. Preserve disagreement distribution.

## Stability
For repeated items:
- exact-score agreement
- probability of any score change
- probability of clinically meaningful category change
- optional within-item entropy

## Results shell — no empirical values yet

### Table 1 — dataset and execution
| Product | Primary responses | Technical failures | Fallback/quota events | Repeat responses |
|---|---:|---:|---:|---:|
| TBD | — | — | — | — |

### Table 2 — primary outcome
| Contrast | OR | 95% CI | p | Interpretation |
|---|---:|---:|---:|---|
| Psychotic vs control | — | — | — | — |

### Table 3 — product interaction
| Product | Psychosis effect | 95% CI | Score-2 probability psychotic | Score-2 probability control |
|---|---:|---:|---:|---:|
| TBD | — | — | — | — |

### Figure 1
Model-based probabilities of appropriateness 0/1/2 by condition and product.

### Figure 2
Product × SIPS P1–P5 heatmap of inappropriate-response probability.

### Figure 3
Recognition / non-reinforcement / urgency / resources failure profile.

### Figure 4
Repeat-subset instability.

## Interpretation rules
- Do not call a product “safe” from a low average score.
- Report failure modes even if the overall effect is small.
- Separate technical refusal, appropriate refusal, safe engagement and over-refusal where available.
- Do not interpret product rankings beyond the tested dates/configurations.