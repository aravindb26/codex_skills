# Upstream Tool And Skill Refresh: 2026-10-13 Follow-up

This is the full follow-up refresh after the public Solodit importer was made the default. The
comparison was content-based, not name-based. Existing local customizations and addenda were
preserved.

## Active Upstream Heads Checked

| Source | Checked commit | Result |
|---|---|---|
| `pashov/skills` | `92b0ea6786e6c210bc9a839e4813d50876c1c550` | V4.1 reviewed; local V3 retained with the existing Codex V4 addendum |
| `trailofbits/skills` | `442fc9d6c89b1e937e6f7a477e7071ea75fcbea4` | Semgrep merged; Trailmark/Rust guidance merged; three conditional skills installed |
| `hackenproof-public/skills` | `60d88130e42a24d4678b636efdcd7af846c990db` | Existing local triage skills match; no duplicate update |
| `OpenZeppelin/openzeppelin-skills` | `6f215af60eb60017ab1a933ce9d22a479cd42b26` | Existing secure-development/upgrade/Sui coverage retained |
| `Cyfrin/solskill` | `d17bda028df073c61711a1fe156b5ca5dea91642` | BattleChain-specific update not added to the general audit path |
| `forefy/.context` | `c8ff161fccdeef9a0416df6230636eb2dfde4a8b` | Existing selected skills retained; no distinct low-noise replacement |
| `quillai-network/qs_skills` | `8bdd3c058704cd855ce29b8e2385708b59152606` | Existing selected skills retained |
| `auditmos/skills` | `c958b3abb0ce189d9f39a05caf94b5a5da655010` | Existing selected skills retained |
| `kadenzipfel/scv-scan` | `114985581450cfed35c277831a065c6478e2c328` | Existing adapted `scv` skill retained |
| `0xiehnnkta/nemesis-auditor` | `75cecc6dbd798f82ed8928d1a906078be9c575de` | Existing selected skills retained |
| `heavyw8t/The-Judge` | `20703caee08ffdb2736866e7d21d1df2b3e21968` | Existing judge skill retained |
| `J4X-Security/K.I.T` | `1e18ece9cf0e7e9b73f8579e1b706a084586f47e` | Existing adapted known-issue skill retained |
| `cholakovvv/foundry-poc-mainnet-fork` | `e02ebcb75d41575eb69127039da3de85a7b72da5` | Existing PoC skill retained |
| `zzzuhaibmohd/solana-token-extensions-security` | `3e56671dd55c15465cbb55c91675597bf6fd54de` | No useful audit-content delta; existing skill retained |
| `0xCyrildev/Chase` | `c8c4f18999024119ddb6cbf7f29dbf9e996f9016` | Conditional Sui/Move skill retained |
| `DarkNavySecurity/web3-skills` | `2d00159558dd921d67fc90106a83557e963adf33` | Existing client/incident skills retained |
| `melanke/defi-builder-skills` | `fa24571dba27768d73f9c52a95ebfbf26acb894c` | README-only change; no update |
| `0xsimao/0xsimao-ai` | `3f81e5803174182a7db07eca87849d2b3d571113` | Existing Arsen attack-lens reference retained |
| `pantheraudits/move-auditor` | `21610f0db7982dc991b356e09d38e06e149f7331` | Move-only reference; not default active routing |
| `SnailSploit/Claude-Red` | `a8de813edc9f66f60d44cfe42d47750e89d9930b` | Curated offensive reference retained; no bulk import |
| `shuvonsec/claude-bug-bounty` | `40b03eeea639ef930123924aa316a89566d5180b` | Existing Web2 reference retained; Web3 overlap excluded |
| `uphiago/recon-skills` | `1260244136edc6ae698d76d3d526f503e322778d` | Existing filtered Web2 recon reference retained |
| `mukul975/Anthropic-Cybersecurity-Skills` | `54a798831d2266a3ca61ce68a7acb80b81160d57` | Existing filtered Web2/source reference retained |
| `openai/codex-security` | `296abe7319affdcebaf8e5def53e5f36a21426b2` | Existing local reference is more complete; no overwrite |
| `pashov/audits` | `e615d8a5319647f95e217616d21770b3d8372f50` | Dry-run: 0 new High/Medium, 16 reviewed skips, no content duplicates |
| `Auditware/AuditVault` | `392eb3eee1cb99b9ba227b9c182cdaa1dab40abe` | Checklists byte-identical to local; no update |
| `zksecurity/zk-skills` | `f56ed630f15b7782885342cc55dacbe5692a7b9d` | Installed conditional `circom-auditor` skill |
| `0xfirefistt/solidity-auditor-private` | unavailable unauthenticated | Private V3 preserved; no overwrite or unauthorised access attempt |

## Installed Or Merged

- Installed Trail of Bits `modern-cpp` for C++ security/source-code review.
- Installed Trail of Bits `post-patch-validation` for pinned baseline-versus-patch validation,
  exploit variants, regressions, and evidence gaps.
- Installed `zksecurity/zk-skills` `circom-auditor` only for Circom/ZK targets, with a local
  Codex addendum that keeps AGENTS.md, scope, evidence, and final-gate rules authoritative.
- Merged current Trail of Bits Semgrep coverage improvements: partial-scan recording, invalid
  YAML/join-rule pruning, broader language/config detection, `--no-project` execution, and
  explicit coverage-gap reporting. Existing local oversized-file safeguards were preserved.
- Updated Trailmark installation/import/diff guidance and Rust-review helper execution to use
  reproducible `uv` commands while preserving the local Codex path-resolution logic.
- Made public Solodit retrieval the default; API retrieval remains explicit and is not required
  for the public report pages.

## Reviewed But Not Installed

- Pashov Solidity Auditor V4.1: useful mechanisms are already represented in
  `solidity-auditor/local-pashov-v4-addendum.md`; replacing local V3 would lose Codex adaptations.
- `monad-developers/ultrafuzz`: isolated-VM skip-permissions orchestrator; unsafe/noisy as a
  workstation skill.
- `TarasBrilian/gebug-audit`: strong EVM doctrine but Claude-specific full orchestrator that
  overlaps local Pashov/Arsen/AGENTS workflows.
- `aeonfun/aeon`, `Gabson0x/bountyforge`, and `itsdarktoday/auditcode`: full agent platforms with
  overlapping orchestration, providers, scanners, and persistent state.
- `adshao/flounder`: full sandbox/daemon/dashboard audit system, not a portable Codex skill.
- `CDSecurity/cdsecurity-skills`: audit-preparation guidance already covered locally.
- `Frankcastleauditor/safe-solana-builder`: secure-development guidance, not a distinct hunting
  workflow.
- `GPTScan/GPTScan`: scanner/tool without a Codex `SKILL.md`; retain only as a lead-generator
  reference under existing evidence rules.
- Current Trail `review-walkthrough`, `writing-lean-proofs`, and internal review fixtures were
  not installed: they are explicit visualization/proof/development utilities, not default
  vulnerability-finding skills.

## Feed And Dedupe Results

- Solodit public page recheck was idempotent: page 1 imported `0`, skipped `10`; the local exact
  ID/fingerprint/canonical-URL indexes remain duplicate-free.
- Crypto Training hacks dry-run: `parsed=1665`, `would import=0`, `skipped_existing=1665`.
- Pashov audits dry-run: `total=1289`, `imported_high=0`, `imported_medium=0`,
  `duplicate_content=0`, `duplicate_semantic=0`.
- Code4rena discovery dry-run: `reports=30`, `imported=0`, `skipped=263`, `failed=0`; the
  existing content/root-cause index already covers the discovered High/Medium material.
- The existing report-pattern importers remain deduplicating; no report body is copied when the
  local root-cause/content index already covers it.

## Routing Rule

Web3 contract, Move, Solana, Cosmos, and Circom skills remain separate from Web2/offensive
reference libraries. Full external platforms and scanners are never silently invoked as default
auditors; they require an explicit task and still produce leads only until manually validated.
