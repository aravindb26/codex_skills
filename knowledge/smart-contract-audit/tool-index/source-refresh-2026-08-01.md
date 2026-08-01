# Tracked Source Refresh - 2026-08-01

All tracked sources were checked against upstream HEAD commits. Changed sources were cloned under `/home/dinesh/.cache/codex-source-refresh-20260801/` and reviewed by content, not only by folder names.

## Skill And Tool Sources

| Source | Checked commit | Result |
|---|---|---|
| `pashov/skills` | `c577eb7799c349de0acb187ba00ca98e14e436fd` | No upstream change; active local private V3 remains current. |
| `trailofbits/skills` | `1256982d4d925a0acfe11e26c2253c32052c6247` | Installed new bounded Trailmark/GitHub/open-source/triage skills and updated existing Trailmark skills while preserving local addenda. |
| `hackenproof-public/skills` | `0c47239cd1fbd292f5748137bfc0d90d478486b1` | No upstream change. |
| `OpenZeppelin/openzeppelin-skills` | `6f215af60eb60017ab1a933ce9d22a479cd42b26` | No upstream change. |
| `Cyfrin/solskill` | `d17bda028df073c61711a1fe156b5ca5dea91642` | No upstream change. |
| `forefy/.context` | `2d42eecd9e53cc9fa8bcdf56b181b32ada8ce5b6` | Reviewed changes; installed skill diffs were formatting-only for local needs, so no local skill update was applied. |
| `pashov/ai-web3-security` | `05c9772c135c88edafec1cf490811f5e0c4ea777` | Reviewed newly listed `melanke/defi-builder-skills` and `CertiK AI Auditor`; installed the useful open-source DeFi builder skills and tracked CertiK as paid/closed-source discovery only. |
| `quillai-network/qs_skills` | `8bdd3c058704cd855ce29b8e2385708b59152606` | No upstream change. |
| `auditmos/skills` | `c958b3abb0ce189d9f39a05caf94b5a5da655010` | No upstream change. |
| `kadenzipfel/scv-scan` | `114985581450cfed35c277831a065c6478e2c328` | No upstream change. |
| `Archethect/sc-auditor` | `942cc13111cf5b0617d9de8fa4fe9bc20f1d8cc8` | No upstream change; still omitted due conflicting user-gated orchestrator. |
| `0xiehnnkta/nemesis-auditor` | `75cecc6dbd798f82ed8928d1a906078be9c575de` | No upstream change. |
| `heavyw8t/The-Judge` | `20703caee08ffdb2736866e7d21d1df2b3e21968` | No upstream change. |
| `J4X-Security/K.I.T` | `1e18ece9cf0e7e9b73f8579e1b706a084586f47e` | No upstream change. |
| `cholakovvv/foundry-poc-mainnet-fork` | `e02ebcb75d41575eb69127039da3de85a7b72da5` | No upstream change. |
| `zzzuhaibmohd/solana-token-extensions-security` | `8147c4fb343c656f12349ccedc4d729ef7865c4b` | No upstream change. |
| `0xfirefistt/solidity-auditor-private` | `d98b387f2adcf7817b9485790abdc307672505f0` | No upstream change; active V3 remains current. |
| `DarkNavySecurity/web3-skills` | `2d00159558dd921d67fc90106a83557e963adf33` | No upstream change. |
| `SnailSploit/Claude-Red` | `aeb41eca7088a703c3a35fbcba3086d4a6c1aa4e` | No upstream change. |
| `shuvonsec/claude-bug-bounty` | `dcb6db9ab01600a03bcccafc7324b66195a15ccc` | README-only wording change; no local update needed. |
| `pashov/SCSVS` | `a0de46c9e1c37c3ee3b8bd60cb46e816c7084e03` | Reference source unchanged. |
| `pashov/weird-erc20` | `266025c555b42b2dd2517fd99f7d47032ec99abe` | Reference source unchanged. |
| `pashov/audits` | `b22301b6ed03e099842cc32dffad811f432ecebd` | No upstream change; guarded importer found 0 new importable findings. |
| `Kritt-ai/open-kritt` | `266a969eef0221075b4a182ddc2f7006eeed7509` | Reviewed but not installed; still a full Docker/orchestration platform, not a lightweight Codex skill. |
| `digger-determsec/digger` | `be8ad8368e97b5ac022eac32fe091bf2e640e4b3` | No upstream change; still tracked only. |
| `NVN404/rust-recon` | `caaaa1f42039850fe0cbfd709202e3e08baf757f` | No upstream change; still not installed due unsafe setup assumptions. |
| `NVN404/rust-recon-tool` | `eeea39ffc9c26de803e6f7eecb0ad95b837ed617` | No upstream change; still not installed due unsafe cleanup behavior. |
| `RASHMOR1/dlt-auditor` | `017d80f70ad55f95366d1dcbe8849d30eebb421a` | No upstream change; still not installed due benchmark/runtime noise. |
| `exvulsec/sui-move-skill` | `54daba3c0d3621c46bb875245539e734bc410038` | No upstream change; still not installed due overlap and broken reference. |

## Installed Or Updated

- Updated existing Trailmark-related skills: `audit-augmentation`, `diagramming-code`, `graph-evolution`, `trailmark`, `trailmark-structural`, and `trailmark-summary`.
- Installed new Trail of Bits skills: `slicing-code-context`, `trailmark-finding-triage`, `trailmark-review-gate`, `trailmark-variant-neighborhood`, `github-triage`, `open-sourcing`, and `vulnerability-triage-brocards`.
- Installed new DeFi builder skills: `defi-spec-driven` and `defi-protocol-discovery`.

## Skipped Or Tracked Only

- `forefy/.context` installed-skill changes were formatting-only; no local behavior update was needed.
- `shuvonsec/claude-bug-bounty` changed README wording only; no local behavior update was needed.
- `Kritt-ai/open-kritt` improved platform code and cleanup behavior, but remains too heavyweight and operationally noisy for default Codex skills.
- `CertiK AI Auditor` is paid/closed-source; tracked only as discovery.

## Knowledge Refresh

- Solodit: checked 300 recent High/Medium API rows; imported 0 new findings and skipped 300 duplicates or non-importable rows.
- Code4rena: checked 40 newest discovered reports; imported 0 new findings, skipped 285 duplicates or non-importable findings, and observed two upstream report fetch failures: `2025-05-blackhole` returned HTTP 404 and `2025-03-starknet-perpetual` returned HTTP 502.
- Pashov audits: checked commit `b22301b6ed03e099842cc32dffad811f432ecebd`; imported 0 new findings because all candidates were already imported, existing-title duplicates, or reviewed skips.

## Validation

- Confirmed all installed skill directories contain `SKILL.md`.
- Confirmed no duplicate `name:` frontmatter values were introduced.
- Confirmed Trailmark local addenda such as `local-solodit-addendum.md` were preserved.
- Ran Python syntax checks for `slicing-code-context` scripts.
- Ran shell syntax checks for `open-sourcing` scripts.
