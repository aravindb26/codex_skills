# Filtered Install Notes

This install intentionally keeps only the Web2/AppSec/source-code bounty pieces from `shuvonsec/claude-bug-bounty`.

## Source

- Repository: https://github.com/shuvonsec/claude-bug-bounty
- Commit reviewed for current filtered refresh: `e363fa09f003d77a0420abcd081628cdbe7f8ed4`
- Install target: `/home/dinesh/.codex/offensive-skills/claude-bug-bounty/`

## Included

- `skills/bb-methodology/`
- `skills/web2-recon/`
- `skills/web2-vuln-classes/`
- `skills/security-arsenal/`
- `skills/triage-validation/`
- `skills/report-writing/`
- `rules/hunting.md`
- `rules/reporting.md`
- selected `tools/` helpers directly referenced by retained Web2 skills
- upstream LICENSE

## Excluded To Avoid Web3 Noise

These upstream paths are intentionally not installed because this machine already has stronger Web3-specific skills and knowledge:

- `skills/web3-audit/`
- `skills/meme-coin-audit/`
- `web3/`
- `commands/web3-audit.md`
- `agents/web3-auditor.md`
- `agents/token-auditor.md`
- `docs/smart-contract-audit.md`
- upstream README, FAQ, TERMS, and CHANGELOG files that advertise mixed Web3/command-runner behavior

Use `/home/dinesh/.codex/skills/` and `/home/dinesh/.codex/knowledge/smart-contract-audit/` for serious smart-contract audits.

## Excluded To Avoid Unsafe Or Noisy Defaults

These upstream paths are intentionally not installed because they can encourage broad automation, credential attacks, or tool noise unless a specific program explicitly allows them:

- `skills/credential-attack/`
- `commands/spray.md`
- `commands/breach-check.md`
- `commands/osint-employees.md`
- `commands/recon.md`
- `commands/scan-cves.md`
- `commands/secrets-hunt.md`
- `commands/takeover.md`
- `commands/token-scan.md`
- `commands/param-discover.md`
- unreferenced `tools/` helpers, especially credential spray, broad active runners, OOB/listener, scanner wrappers, and zero-day fuzzing scripts
- `scripts/`
- `agents/`
- `mcp/`
- `.claude/`
- `hooks/`

If one of these is needed later, inspect the upstream file first and use it only under the target program's written scope and safe-harbor rules.

## Duplicate Review

No exact duplicate files were found against `/home/dinesh/.codex/offensive-skills/claude-red/`.

There is semantic overlap with Claude-Red in common web bug classes such as IDOR, XSS, SSRF, SQLi, OAuth/JWT, GraphQL, file upload, race conditions, and reporting. The reason to keep this filtered library is that it is organized as a bug-bounty workflow and triage/reporting companion, while Claude-Red is broader red-team/AppSec methodology.

Use only the smallest relevant reference for the current task. Do not load both libraries broadly.
