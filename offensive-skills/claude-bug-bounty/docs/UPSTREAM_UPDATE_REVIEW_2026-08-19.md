# Upstream Update Review - 2026-08-19

Source: <https://github.com/shuvonsec/claude-bug-bounty>

Reviewed commit: `e363fa09f003d77a0420abcd081628cdbe7f8ed4`

## Applied

- Updated retained Web2/source-code reference skills:
  - `bb-methodology`
  - `security-arsenal`
  - `web2-recon`
  - `web2-vuln-classes`
- Kept `triage-validation` unchanged because it already matched upstream.
- Kept local `report-writing` unchanged because upstream reintroduced Immunefi/Web3 report sections and this filtered pack must remain Web2/source-code oriented.
- Added only helper scripts directly referenced by the retained Web2 skills.

## Skipped

- `web3-audit` and `meme-coin-audit`: weaker and noisier than the active Web3 audit stack.
- `credential-attack` and spray tooling: high noise and only valid under narrow explicit authorization.
- Broad runners, OOB/listener helpers, zero-day fuzzers, and miscellaneous active scanner wrappers: not needed for the filtered reference pack.
- `graphql-audit`: useful but semantically covered by existing `offensive-graphql`, `hunt-schema-enumeration`, and updated Web2 vulnerability-class references.

## Local Use Rule

Use this pack only for authorized Web2/source-code AppSec work. It remains outside `/home/dinesh/.codex/skills/` so it does not affect normal smart-contract audit skill routing.
