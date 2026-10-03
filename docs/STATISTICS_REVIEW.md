# Statistics-method review — pre-freeze

## Current v0.1

Proposes proportional-odds regression + GEE clustered by prompt + Brant test, plus mixed-model sensitivity analyses.

## Main concern

These components do not automatically form one coherent inferential framework. A conventional Brant test belongs to a standard proportional-odds model, while ordinal GEE may require different assumption/robustness diagnostics.

## Pre-registration recommendation

A statistician should choose **one** primary clustered ordinal framework, e.g.:

1. cumulative-link mixed model with prompt/pair random effects; or
2. ordinal GEE with robust SE and prespecified working correlation.

Choice must reflect:
- paired psychotic/control observations
- multiple products on the same prompts
- repeated-response subset
- possible rater-level modelling

## Raters

Do not automatically collapse two clinician ratings using "median then floor" before the estimand is clear.

Preserve:
- raw rating
- rater ID
- adjudication record

Predefine whether primary analysis uses adjudicated consensus or raw ratings with rater effects.

## Power

The original OR≥2.5 calculation may support the primary replication effect, but interactions, language effects, SIPS subgroups and Plan B/C need separate precision/power simulation if made confirmatory.

**Human/statistician gate required before preregistration.**
