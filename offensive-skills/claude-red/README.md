# Claude-Red Reference Skills For Codex

Source: https://github.com/SnailSploit/Claude-Red

Installed from commit: `aeb41eca7088a703c3a35fbcba3086d4a6c1aa4e`

This is a reference-only conversion of SnailSploit/Claude-Red into Codex-readable `SKILL.md` folders.

These skills are intentionally stored outside `/home/dinesh/.codex/skills/` so they do not auto-load during smart-contract audits.

## When To Use

Use selectively for authorized AppSec/source-code/red-team style work:

- web application bug bounty work
- API, GraphQL, REST, auth, JWT, OAuth, IDOR, SSRF, SQLi, XSS, SSTI, deserialization, file-upload, and business-logic testing
- cloud, mobile, IoT, AI-app, infrastructure, fuzzing, and vulnerability-research workflows
- pentest-style report writing

## When Not To Use

Do not use these by default for Solidity/Vyper/Solana/Cosmos/Web3 contest audits. Use the active smart-contract skills and knowledge base instead.

Do not use these for unauthorized testing. Program scope, safe harbor, and responsible testing rules always control.

## Layout

- `skills/<skill-name>/SKILL.md`: converted Codex-readable skill files
- `manifest.json`: local conversion manifest and source commit
- `docs/`: upstream README, SECURITY, LICENSE, changelog, and manifest

## Active Install Later

If one specific skill is useful later, copy only that folder into:

```text
/home/dinesh/.codex/skills/<skill-name>/
```

Do not bulk-copy this whole directory into active Codex skills unless you intentionally want all offensive skills active.
