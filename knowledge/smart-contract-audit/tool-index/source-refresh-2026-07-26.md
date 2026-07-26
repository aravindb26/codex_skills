# Tracked Source Refresh - 2026-07-26

All tracked sources were checked against upstream HEAD commits. Changed sources were cloned under `/home/dinesh/.cache/codex-source-refresh-20260726/` and reviewed by content, not only by folder names.

## Skill And Tool Sources

| Source | Checked commit | Result |
|---|---|---|
| `pashov/skills` | `c577eb7799c349de0acb187ba00ca98e14e436fd` | Only public wording for `solidity-auditor` and `fizz` files changed; preserved local private V3 and skipped `fizz` noise. |
| `trailofbits/skills` | `cfe5d7b1619e47fb5b38b7e2561dad7e5f1e89af` | No upstream change. |
| `hackenproof-public/skills` | `0c47239cd1fbd292f5748137bfc0d90d478486b1` | No upstream change. |
| `OpenZeppelin/openzeppelin-skills` | `6f215af60eb60017ab1a933ce9d22a479cd42b26` | Installed `setup-sui-contracts`, `review-sui-contracts`, and updated `develop-secure-contracts` with Sui Move support. |
| `Cyfrin/solskill` | `d17bda028df073c61711a1fe156b5ca5dea91642` | No upstream change. |
| `forefy/.context` | `a7a8713754f1307676acb11e737cd2ee89f1daf2` | Installed `audit-scope`, `safe-hunt`, and `endpoint-threat-hunt`; patched `safe-hunt` command examples to Codex paths. |
| `pashov/ai-web3-security` | `8bf4757f39054b63584185ddb824ae253775e227` | Reviewed newly listed `digger`, `open-kritt`, and `One Dollar Audit`; did not install due tool/platform/paid-source boundaries. |
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
| `DarkNavySecurity/web3-skills` | `2d00159558dd921d67fc90106a83557e963adf33` | Updated `client-auditor` to v3.4 with stronger hunt coverage gates and Codex-friendly worker limits. |
| `SnailSploit/Claude-Red` | `aeb41eca7088a703c3a35fbcba3086d4a6c1aa4e` | No upstream change. |
| `shuvonsec/claude-bug-bounty` | `200959489fe5e0c8f70c7a72b7267cd446815617` | Added filtered Web2 `tools/lead_board.py`; skipped standalone provider/runtime changes. |
| `pashov/SCSVS` | `a0de46c9e1c37c3ee3b8bd60cb46e816c7084e03` | Reference source unchanged. |
| `pashov/weird-erc20` | `266025c555b42b2dd2517fd99f7d47032ec99abe` | Reference source unchanged. |
| `NVN404/rust-recon` | `caaaa1f42039850fe0cbfd709202e3e08baf757f` | No upstream change; still not installed due unsafe setup assumptions. |
| `NVN404/rust-recon-tool` | `eeea39ffc9c26de803e6f7eecb0ad95b837ed617` | No upstream change; still not installed due unsafe cleanup behavior. |

## Knowledge Refresh

- Solodit: checked 300 recent High/Medium API rows; imported 46 new findings and skipped 254 duplicates or non-importable rows.
- Code4rena: checked 40 newest discovered reports; imported 86 new High/Medium findings, skipped 204 duplicates or non-importable findings, and observed one stale sitemap report URL returning HTTP 404 (`2025-05-blackhole`).
- Pashov audits: checked commit `b22301b6ed03e099842cc32dffad811f432ecebd`; imported 0 new findings because all candidates were already imported, existing-title duplicates, or previously reviewed skips.

## New Install Decisions

- `setup-sui-contracts` and `review-sui-contracts` are useful for Sui Move development/review and do not disturb normal Solidity audits because their trigger surface is specific.
- `audit-scope` is useful for estimating source-code/security engagement scope and is separate from finding work.
- `safe-hunt` is useful for read-only DeFi Safe governance/admin-control review; it should be treated as a lead generator, not proof by itself.
- `endpoint-threat-hunt` is useful for endpoint IR/AppSec tasks and should not be used during smart-contract audits unless explicitly relevant.
- `client-auditor` v3.4 improves orchestration safety, coverage completeness, and Codex worker limits for blockchain client audits.
- `lead_board.py` is useful for Web2/source-code recon lead persistence and is kept under `offensive-skills`, not active Web3 skills.

## Reviewed But Not Installed

- `digger-determsec/digger`: promising beta EVM/Solana evidence-gated scanner, but it requires building and maintaining Rust binaries and overlaps as an optional lead generator. Track, do not install by default.
- `Kritt-ai/open-kritt`: full self-hosted AI audit platform with Docker/root job containers. Track, do not install into Codex skills.
- `One Dollar Audit`: paid/closed-source scanner link. Track only as a discovery item.
