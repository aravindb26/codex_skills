# Local Solodit Addendum: Smart Contract Structural Summary

## Purpose

Use this companion with `trailmark-summary` for fast orientation on smart contract and Web3 repositories.

The summary should help choose audit surfaces, not replace reading.

## When To Use

Use this addendum when:

- starting a new smart contract audit
- orienting in an unfamiliar Web3 repo
- choosing which detailed Trailmark or manual pass to run next

## Companion Workflow

1. Run summary only after identifying the repo root and likely scope.
2. Compare detected languages and entry points against the program scope.
3. Highlight smart-contract modules, offchain adapters, tests, scripts, and generated code separately.
4. Search local knowledge and Solodit stubs for detected protocol primitives.
5. Recommend the next manual and skill-based passes.

## False-Positive Filters

Do not treat summary output as coverage. It does not prove:

- all in-scope files were read
- entry points are exploitable
- graph paths are security bugs
- scanner output is accurate

## Output Requirements

When this addendum is used, include:

- detected languages
- likely in-scope modules
- high-risk module categories
- relevant Solodit/local pattern searches
- next manual reading priorities
