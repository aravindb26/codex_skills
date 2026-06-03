# Pashov AI Web3 Security Tools Hub

Source: <https://github.com/pashov/ai-web3-security>

Checked: 2026-06-03

Source commit checked: `c44ad3653bece52ab0ac60a9f29e7283a78ea172`

## Classification

This repository is a curated index of Web3 AI/security tools, not an installable Codex skill package.

It contains:

- `README.md`
- `CONTRIBUTING.md`

It does not contain direct `SKILL.md` files.

## Already Covered Locally

The highest-trust/core entries were already present in this Codex setup before this review:

- `pashov/skills`
- `Cyfrin/solskill`
- `kadenzipfel/scv-scan`
- `trailofbits/skills`
- `forefy/.context` partial coverage
- `hackenproof-public/skills` partial coverage

## Installed From The Hub Review

Installed a conservative public-skill set that adds useful audit coverage without bulk-loading every listed repo.

### QuillAI Skills

Source: <https://github.com/quillai-network/qs_skills>

Commit: `8bdd3c058704cd855ce29b8e2385708b59152606`

Installed:

- `semantic-guard-analysis`
- `input-arithmetic-safety`
- `external-call-safety`
- `defender`

Reason:

- Adds guard/state consistency, input/arithmetic validation, external-call/token safety, and deployment/release gate analysis.

### Auditmos Skills

Source: <https://github.com/auditmos/skills>

Commit: `c958b3abb0ce189d9f39a05caf94b5a5da655010`

Installed:

- `audit-liquidation-dos`
- `audit-state-validation`
- `audit-auction`
- `audit-liquidation-calculation`
- `audit-clm`
- `audit-unfair-liquidation`

Reason:

- Adds focused coverage for auctions, concentrated liquidity managers, liquidation edge classes, and state validation bugs.

### OpenZeppelin Skills

Source: <https://github.com/OpenZeppelin/openzeppelin-skills>

Commit: `d72005b53b6d8c937dd1b76262a3e2ebbace2edb`

Installed:

- `develop-secure-contracts`
- `upgrade-solidity-contracts`

Reason:

- Adds official OpenZeppelin secure-development and upgradeability workflow guidance.

### Forefy Context

Source: <https://github.com/forefy/.context>

Commit: `fcf76d9b8b123073ddb8b046bbd480547e7e4718`

Installed:

- `foundry-poc`

Reason:

- Adds Foundry PoC workflow coverage complementary to local validation and report work.

### Nemesis Auditor

Source: <https://github.com/0xiehnnkta/nemesis-auditor>

Commit: `75cecc6dbd798f82ed8928d1a906078be9c575de`

Installed:

- `feynman-auditor`
- `state-inconsistency-auditor`
- `nemesis-auditor`

Reason:

- Adds deep line-by-line explanation, state inconsistency hunting, and combined deep-logic audit passes.

### The Judge

Source: <https://github.com/heavyw8t/The-Judge>

Requested pinned path in hub: `710e06a0cee1f43fc551952acce59e3c90fa2141/skill/judge`

Installed cache commit: `20703caee08ffdb2736866e7d21d1df2b3e21968`

Installed:

- `judge`

Reason:

- Adds adversarial false-positive filtering for AI-generated Web3 findings.

### Foundry Mainnet-Fork PoC

Source: <https://github.com/cholakovvv/foundry-poc-mainnet-fork>

Commit: `e02ebcb75d41575eb69127039da3de85a7b72da5`

Installed:

- `foundry-poc-mainnet-fork`

Reason:

- Adds stricter real-deployed-contract mainnet-fork PoC methodology.

### Known Issue Triager

Source: <https://github.com/J4X-Security/K.I.T>

Commit: `1e18ece9cf0e7e9b73f8579e1b706a084586f47e`

Installed:

- `known-issue-triager`

Local adaptation:

- Installed from `codex-skill-kit`.
- Renamed frontmatter from `kit` to `known-issue-triager`.
- Updated hardcoded skill path references from `~/.codex/skills/kit` to `~/.codex/skills/known-issue-triager`.

Reason:

- Adds canonical known-issues register creation and duplicate checking.

### Solana Token-2022 Security

Source: <https://github.com/zzzuhaibmohd/solana-token-extensions-security>

Commit: `8147c4fb343c656f12349ccedc4d729ef7865c4b`

Installed:

- `solana-token-extensions-security`

Reason:

- Adds focused Solana Token-2022 extension audit coverage.

## Intentionally Not Bulk Installed

Several listed repos were not installed to avoid active-skill noise or because local coverage already exists.

Skipped for now:

- broad duplicate full-auditor frameworks
- very large multi-ecosystem skill packs
- generic bug-bounty/web2 packs already partly covered by `/home/dinesh/.codex/offensive-skills/claude-red/`
- tools without `SKILL.md`
- paid/closed-source tools listed only as references

Use this hub as a discovery source, not as an authority that every listed tool should be active in Codex.
