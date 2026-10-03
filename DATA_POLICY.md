# Public Repository Data Policy

`CochraneK/Pair` is a public research-methods repository.

## Allowed in Git
- protocols and derived method notes created for PAIR
- benchmark schemas and non-sensitive templates
- synthetic/example prompts approved for public release
- analysis/QA scripts
- aggregate or deliberately public example results
- meeting materials intended for project discussion
- bibliographic metadata

## Do not commit
- account credentials, API keys, tokens, cookies or session data
- personal research-account identifiers
- raw consumer-app screenshots before manual privacy review
- any real patient/participant material unless a separate ethics/data-release decision explicitly permits it
- identifiable clinician/rater data unless approved
- third-party copyrighted source files unless redistribution permission is clear
- personal-reserved research directions that are outside this collaboration

## Raw collection
Raw APP captures should live in a controlled local/approved storage location. Git should store only a manifest, hashes, derived blinded data, and release-approved materials.

## Release gate
Public release of a full benchmark case set should be a separate team decision because reproducibility, licensing, and benchmark contamination/held-out testing can conflict.
