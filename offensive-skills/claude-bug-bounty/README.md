# Claude Bug Bounty Reference Skills For Codex

Source: https://github.com/shuvonsec/claude-bug-bounty

Reviewed through commit: `e363fa09f003d77a0420abcd081628cdbe7f8ed4`

This is a filtered, reference-only install for Web2/AppSec and source-code bug bounty work. It is intentionally stored outside `/home/dinesh/.codex/skills/` so it does not auto-load during smart-contract audits.

## When To Use

Use selectively for authorized Web2/AppSec/source-code bounty work:

- HackerOne, Bugcrowd, Intigriti, private web bounty, or source-code AppSec reviews
- web/API attack-surface mapping
- IDOR, auth bypass, XSS, SSRF, SQLi, XXE, GraphQL, OAuth/OIDC, JWT, file upload, race, cache, request smuggling, cloud/infra, and business-logic testing
- finding validation and report writing

## When Not To Use

Do not use this library by default for Solidity, Vyper, Solana, Cosmos, Move, or Web3 contest audits. Use the active smart-contract skills and knowledge base instead:

- `/home/dinesh/.codex/skills/`
- `/home/dinesh/.codex/knowledge/smart-contract-audit/`

Do not use this library for unauthorized testing. Program scope, safe harbor, rate limits, and responsible testing rules always control.

## Filtered Install

Included Web2/AppSec reference skills:

- `bb-methodology`
- `web2-recon`
- `web2-vuln-classes`
- `security-arsenal`
- `triage-validation`
- `report-writing`

Included helper tools:

- `tools/lead_board.py`: persistent Web2 recon lead ledger for tracking, ranking, and status-updating leads so promising surfaces are not forgotten during long hunts.
- Selected helper scripts directly referenced by the retained Web2 skills, such as `bypass_403.sh`, `graphql_audit.sh`, `multipart_mutator.py`, `param_discovery.sh`, `secrets_hunter.sh`, `takeover_scanner.sh`, and WAF helper scripts.

Inspect helper scripts before running them. They are not default audit steps and must stay within the target program's written scope and safe-harbor rules.

Excluded upstream pieces are documented in `docs/FILTERED_INSTALL_NOTES.md`.

## Layout

- `skills/<skill-name>/SKILL.md`: filtered reference skills
- `rules/`: upstream hunting/reporting rules
- `tools/`: filtered helper tools retained only when they reduce lost leads without adding noisy active scanning
- `docs/`: upstream README/FAQ/terms/changelog plus local install notes
- `manifest.json`: local install manifest

## Active Install Later

If one specific skill is useful later, copy only that folder into:

```text
/home/dinesh/.codex/skills/<skill-name>/
```

Do not bulk-copy this whole directory into active Codex skills.
