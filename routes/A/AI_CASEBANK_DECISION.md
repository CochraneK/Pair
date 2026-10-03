# Decision: Plan A case-bank source

Date: 2026-10-03

The working Plan A prompt bank will be generated within PAIR rather than waiting for a missing external 160-prompt file.

Canonical bank: `benchmark/A_CASES_v0.1/`

Rationale:
- available protocol v0.1 contains only three examples, not the full bank;
- waiting for an unavailable bank blocks execution;
- newly synthesized fictional prompts can be designed as stricter minimal pairs;
- provenance is clearer because no prompt text is copied from scales, case reports or public benchmarks.

Boundary:
- AI generation supplies the **candidate case bank**, not clinical validity;
- clinicians still review domain fit, realism, severity, control matching and unintended cues;
- any post-review text change becomes A-v0.2.
