# PAIR Benchmark — project positioning and A/B/C rationale

## Canonical project hierarchy

PAIR is a **benchmark-building project first**.

The long-term asset is a reusable, versioned measurement framework for AI responses to psychosis-related content. A+B and PAIR-C are the first validation papers generated while building that benchmark.

Do not frame the project as three parallel experiments or as a benchmark created merely to support two papers.

## A → B → C progression

### A — real-world baseline
Question: are responses to psychosis-related prompts less appropriate than responses to tightly matched ordinary controls?

- 80 psychosis/control pairs are primarily inherited from the original protocol and balanced across SIPS P1–P5 (16 pairs/domain).
- No clinical axes are used in A.
- Approximately five consumer products balance real-world market coverage against manual collection/rating burden.
- A provides ecological validity and a stable first-paper baseline.

### B — bridge from audit to controlled clinical contrasts
Question: when one key clinical cue changes within the same scenario, does the consumer product adjust its response in the required direction?

First-pilot axes:
1. conviction
2. insight / openness to alternatives
3. immediate behavioral risk

Rationale:
- these axes support interpretable minimal contrasts;
- each has plausible clinical implications for response intensity;
- limiting the first pilot prevents Paper 1 from becoming a full benchmark-development study.

Pilot size:
- 6 scenario families × 3 axes × 2 levels = 36 prompts;
- 3 consumer products × 3 runs = 324 outputs.

These numbers are **pilot feasibility choices, not theoretically unique optima**. If successful, B can expand to 15–20 families.

The selection rule for the three B products must be frozen before inspecting A outcomes.

### C — benchmark-development pilot
Question: can a fixed model configuration move its response policy in the correct direction and magnitude when a clinically meaningful cue changes, while avoiding both under-response and over-escalation?

Core pilot axes:
1. conviction
2. insight
3. behavioral risk
4. evidence/plausibility

Evidence/plausibility is added in C because the required policy direction can be positive, negative, or unchanged; it is methodologically more complex than a simple severity escalation axis.

Pilot size:
- 8 scenario families × 4 axes × 2 levels = 64 prompts;
- 3 fixed API/model configurations × 3 runs = 576 outputs.

Again, 8 families and 3 configurations are benchmark-development compromises, not empirically proven optima.

Formal benchmark candidate:
- 20 families × 4 core axes × 2 levels = 160 core prompts;
- later expand key axes to ≥3 ordered levels for threshold calibration;
- add nuisance-invariance and cultural challenge modules only after the core is stable.

## Why two levels first

Two levels test **directional sensitivity**: does the model move appropriately when the clinical cue changes?

They do not identify a precise clinical threshold. Threshold claims require ≥3 ordered levels on the relevant axis.

## Why different system counts

- A uses ~5 consumer products because its scientific object is the real consumer-product ecology.
- B uses 3 consumer products because it is a method-testing exploratory bridge, not another market leaderboard.
- C uses 3 fixed API/model configurations because reproducibility and measurement validation matter more than breadth during benchmark development.

## Benchmark components

PAIR Benchmark should ultimately contain:
- clinical ontology;
- versioned scenario families;
- one-clinical-cue-at-a-time minimal contrasts;
- clinician-defined acceptable response intervals `[L,U]`;
- direct clinician target-direction labels;
- contraindicated-behavior flags;
- preserved raw clinician disagreement;
- calibration, directional concordance, under-response, over-response, stochastic-stability metrics;
- versioned runner/configuration contracts;
- benchmark release notes and known limitations.

## Project interpretation

A is not the benchmark endpoint.
B is where cases become controlled measurement units.
C is where the measurement framework becomes benchmark infrastructure.

The papers validate and communicate the benchmark; they do not define its ultimate scope.

## Still-to-freeze decisions

Before empirical collection:
1. prespecified selection rationale for the three B consumer products;
2. formal sampling rationale for the three C API/model configurations;
3. exact trigger for expanding key axes to ≥3 ordered levels;
4. final clinician ground-truth workflow;
5. final primary statistical model details.
