# PAIR-C pilot freeze checklist

## Materials
- [ ] `CLINICAL_ONTOLOGY_V0_1.md` reviewed by clinicians
- [ ] all 64 candidate prompts reviewed
- [ ] every minimal pair has exactly one intended target-axis change
- [ ] no unresolved major confounds
- [ ] family/domain labels approved
- [ ] cultural challenge set remains excluded from core pilot unless separately approved

## Ground truth
- [ ] each item has raw reviewer-specific `[L,U]`
- [ ] reviewer IDs preserved
- [ ] contraindicated-behavior flags completed
- [ ] adjudication rule defined before model results are inspected
- [ ] disagreement summary produced

## Manipulation validity
Suggested pilot gate:
- [ ] ≥80% of items pass manipulation-success review
- [ ] ≤10% major-confound rate before revision
- [ ] lexical/minimal-pair QA passes
- [ ] no axis is represented only by one scenario type

## Execution
- [ ] three fixed model/API configurations selected
- [ ] exact model IDs recorded
- [ ] system prompt/config frozen and hashed
- [ ] temperature/top_p/max tokens/reasoning/tools recorded
- [ ] repetitions frozen
- [ ] randomization seed frozen
- [ ] raw outputs immutable after collection

## Analysis
- [ ] primary metrics frozen: CCA / URS / ORS / CDC / relevant sensitivity
- [ ] nuisance invariance held for later or separately piloted
- [ ] model-to-policy mapper frozen and validated before benchmark comparison
- [ ] synthetic dry-run remains clearly separated from real data

## Research governance
- [ ] team explicitly agrees C is a distinct/new research question
- [ ] contribution/authorship boundary recorded
- [ ] ethics determination obtained
- [ ] novelty search rerun immediately before preregistration/submission
