# Selected Security Addenda

Reference-only Web2/source-code/AppSec addenda distilled from reviewed upstream skill repos. These files are not active Codex skills and must not be used during default smart-contract audits.

## Sources Reviewed

- `mukul975/Anthropic-Cybersecurity-Skills`: https://github.com/mukul975/Anthropic-Cybersecurity-Skills at `673da1f3b0b7be34ffc9624ef3858fe45f1c3bed`
- `uphiago/recon-skills`: https://github.com/uphiago/recon-skills at `1db898cec0ce8775a5c5ce12e97632fce858f6a1`

## Included

- `snyk-sca-and-scanner-triage.md`: Snyk/SCA and scanner-result triage workflow for source-code AppSec audits.
- `recon-evidence-chaining.md`: Web2 recon discipline, evidence hygiene, and attack-chain validation rules.
- `targeted-web2-hunt-notes.md`: Non-default hunt notes for source leaks, MCP/LLM surfaces, VMware/vCenter, and write-gap/business-logic paths.

## Excluded

- Full `Anthropic-Cybersecurity-Skills` import: 817 skills, heavy script/tool surface, broad SOC/DFIR/red-team coverage, too noisy for this setup.
- Full `recon-skills` import: 145 skills, strong Web2 material but substantial overlap with `claude-red` and `claude-bug-bounty`.
- Web3/meme-coin material from `recon-skills`: intentionally excluded because this machine already has stronger dedicated smart-contract skills and knowledge.
- Upstream scripts: intentionally not copied. Run tooling only from the target workspace after scope and safe harbor are understood.

## Use Rules

- Use only for authorized Web2, source-code, API, recon, or AppSec bounty work.
- Use as leads and checklists, not proof.
- Prefer the smallest matching note first; do not bulk-load this directory.
- For Web3 audits, use `/home/dinesh/.codex/skills/` and `/home/dinesh/.codex/knowledge/smart-contract-audit/` instead.
