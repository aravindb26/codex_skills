# Tracked Source Refresh - 2026-06-30

All sources were shallow-cloned through GitHub SSH and compared against installed content, not only folder names.

| Source | Checked commit | Result |
|---|---|---|
| `pashov/skills` | `605665fe88d5afac2cf3ba208fc3edf7fbc00e1f` | Existing Solidity Auditor V3 and X-Ray content unchanged; Fizz omitted as non-audit workflow noise. |
| `trailofbits/skills` | `cfe5d7b1619e47fb5b38b7e2561dad7e5f1e89af` | Updated `c-review` and `fp-check`; installed new `rust-review`. |
| `hackenproof-public/skills` | `0c47239cd1fbd292f5748137bfc0d90d478486b1` | Installed content already current. |
| `OpenZeppelin/openzeppelin-skills` | `d72005b53b6d8c937dd1b76262a3e2ebbace2edb` | Installed content already current. |
| `Cyfrin/solskill` | `d17bda028df073c61711a1fe156b5ca5dea91642` | Installed content already current. |
| `forefy/.context` | `82236b22d0600d2e44cde5432ab284fe9c97edf5` | Relevant installed content current; broad duplicate orchestrators omitted. |
| `pashov/ai-web3-security` | `e2b4db57a24e62023af65c2cb415e9c435d7f442` | Discovery index refreshed; new Sui and DLT candidates reviewed and omitted. |
| `quillai-network/qs_skills` | `8bdd3c058704cd855ce29b8e2385708b59152606` | Installed content already current. |
| `auditmos/skills` | `c958b3abb0ce189d9f39a05caf94b5a5da655010` | Installed content already current. |
| `kadenzipfel/scv-scan` | `114985581450cfed35c277831a065c6478e2c328` | Installed local `scv` content already current. |
| `Archethect/sc-auditor` | `942cc13111cf5b0617d9de8fa4fe9bc20f1d8cc8` | Upstream mandatory user-gated orchestrator omitted; it conflicts with the autonomous local audit workflow. |
| `0xiehnnkta/nemesis-auditor` | `75cecc6dbd798f82ed8928d1a906078be9c575de` | Installed content already current. |
| `heavyw8t/The-Judge` | `20703caee08ffdb2736866e7d21d1df2b3e21968` | Installed content already current. |
| `J4X-Security/K.I.T` | `1e18ece9cf0e7e9b73f8579e1b706a084586f47e` | Locally adapted known-issue triager already current. |
| `cholakovvv/foundry-poc-mainnet-fork` | `e02ebcb75d41575eb69127039da3de85a7b72da5` | Installed content already current. |
| `zzzuhaibmohd/solana-token-extensions-security` | `8147c4fb343c656f12349ccedc4d729ef7865c4b` | Installed content already current. |
| `0xfirefistt/solidity-auditor-private` | `d98b387f2adcf7817b9485790abdc307672505f0` | Active V3 content already current. |
| `SnailSploit/Claude-Red` | `aeb41eca7088a703c3a35fbcba3086d4a6c1aa4e` | Reference-only install already current. |
| `shuvonsec/claude-bug-bounty` | `b2e9eb7a8e1c7a2e470b3c66069b72fedc60baa2` | Only excluded active scanner scripts changed; filtered reference install unchanged. |

## New Skill Decisions

- `rust-review` is distinct, narrowly triggered for non-smart-contract Rust crates/services, and adds unsafe-boundary, FFI, concurrency, panic-DoS, async, and SARIF workflows.
- `c-review` was repaired into a complete Codex-readable installation by adding its missing prompts, planner, validators, SARIF generator, and updated agents.
- `fp-check` retained local addenda while upstream verification instructions and references were refreshed.
- `exvulsec/sui-move-skill` was not retained because existing Move coverage is richer and the candidate would weaken the local reporting gate.
- `RASHMOR1/dlt-auditor` was not installed because its large benchmark runtime would add overlap and noise rather than a focused reusable skill.

## Knowledge Refresh

- Solodit: checked the 300 most recent High/Medium API rows; retained 22 genuinely new findings after canonical-URL deduplication.
- Solodit cleanup: removed 242 duplicate URL aliases caused by the API returning the same issue with and without a trailing underscore, and updated the importer to prevent recurrence.
- Code4rena: checked the 30 newest discovered reports and retained 5 new Medium findings.
