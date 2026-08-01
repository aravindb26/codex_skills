# Tracked Upstream Sources

Last reviewed: 2026-08-01

This is the canonical URL registry for Codex audit tooling, knowledge feeds, and reference libraries maintained in this workspace. It intentionally excludes incidental article/report links already stored with their individual knowledge cards.

## Private Backup

| Source | URL | Purpose |
|---|---|---|
| Codex audit backup | <https://github.com/aravindb26/codex_skills> | Private backup of the curated local audit configuration, skills, knowledge, and reference libraries. |

## Core Skill Sources

| Source | URL | Local policy |
|---|---|---|
| Pashov skills | <https://github.com/pashov/skills> | Track useful Solidity and audit workflow changes; preserve local V3 and addenda. |
| Trail of Bits skills | <https://github.com/trailofbits/skills> | Track security review, fuzzing, static analysis, and language-specific skills. |
| HackenProof public skills | <https://github.com/hackenproof-public/skills> | Track bounty triage, PoC grading, comments, handoff, and fix-verification workflows. |
| OpenZeppelin skills | <https://github.com/OpenZeppelin/openzeppelin-skills> | Track secure smart-contract development and upgrade workflows. |
| Cyfrin Solskill | <https://github.com/Cyfrin/solskill> | Track useful Solidity security guidance; omit BattleChain-only noise unless needed. |
| Forefy context skills | <https://github.com/forefy/.context> | Track distinct multi-language and audit skills after content comparison. |

## Web3 Audit Skill Sources

| Source | URL | Local policy |
|---|---|---|
| Pashov AI Web3 Security | <https://github.com/pashov/ai-web3-security> | Discovery hub; review linked tools individually rather than bulk-installing. |
| QuillAI skills | <https://github.com/quillai-network/qs_skills> | Track distinct Solidity audit patterns. |
| Auditmos skills | <https://github.com/auditmos/skills> | Track distinct security-audit skills after deduplication. |
| SCV Scan | <https://github.com/kadenzipfel/scv-scan> | Source for the locally adapted `scv` workflow. |
| Archethect auditor | <https://github.com/Archethect/sc-auditor> | Monitor only; do not install its conflicting user-gated orchestrator unchanged. |
| Nemesis auditor | <https://github.com/0xiehnnkta/nemesis-auditor> | Track deep business-logic and state-consistency workflows. |
| The Judge | <https://github.com/heavyw8t/The-Judge> | Track false-positive and finding-quality review workflow. |
| K.I.T | <https://github.com/J4X-Security/K.I.T> | Track known-issue deduplication and triage workflow. |
| Foundry mainnet-fork PoC | <https://github.com/cholakovvv/foundry-poc-mainnet-fork> | Track focused Foundry exploit-reproduction guidance. |
| Solana Token Extensions Security | <https://github.com/zzzuhaibmohd/solana-token-extensions-security> | Track Token-2022-specific Solana audit patterns. |
| Solidity Auditor Private V3 | <https://github.com/0xfirefistt/solidity-auditor-private> | Private upstream for the active V3 Solidity auditor. |
| Dark Navy Web3 Skills | <https://github.com/DarkNavySecurity/web3-skills> | Source for `client-auditor`; use for blockchain nodes and clients, not ordinary contract audits. |
| DeFi Builder Skills | <https://github.com/melanke/defi-builder-skills> | Track greenfield DeFi protocol discovery and spec-driven development workflows; not default audit hunting. |

## Pinned Review Snapshots

| Source | URL | Purpose |
|---|---|---|
| Dark Navy client-auditor reviewed snapshot | <https://github.com/DarkNavySecurity/web3-skills/tree/96b485e7229fdb260fa74c29d4d123661a466927/client-auditor> | Exact snapshot reviewed before installing the local `client-auditor` skill. |
| Rust Recon reviewed snapshot | <https://github.com/NVN404/rust-recon/tree/caaaa1f42039850fe0cbfd709202e3e08baf757f> | Exact snapshot reviewed and rejected until upstream setup safety improves. |
| Rust Recon extractor reviewed snapshot | <https://github.com/NVN404/rust-recon-tool/tree/eeea39ffc9c26de803e6f7eecb0ad95b837ed617> | Exact extractor snapshot reviewed and rejected due unsafe cleanup behavior. |

## Offensive And AppSec Sources

| Source | URL | Local policy |
|---|---|---|
| Claude-Red | <https://github.com/SnailSploit/Claude-Red> | Reference-only Web2/AppSec library under `offensive-skills`; never bulk-load for Web3 audits. |
| Claude Bug Bounty | <https://github.com/shuvonsec/claude-bug-bounty> | Filtered Web2/source-code bounty reference; exclude overlapping Web3 and noisy scanner wrappers. |
| Recon Skills | <https://github.com/uphiago/recon-skills> | Filtered reference-only Web2/AppSec recon pack under `offensive-skills/recon-skills-filtered`; exclude generic Web3 and mass-recon noise. |
| Anthropic Cybersecurity Skills | <https://github.com/mukul975/Anthropic-Cybersecurity-Skills> | Filtered reference-only Web2/source-code/SCA/API/mobile/supply-chain pack under `offensive-skills/anthropic-cybersecurity-filtered`; exclude SOC/DFIR/generic cyber and weaker smart-contract overlap. |
| Snyk | <https://snyk.io/> | Web2/source-code scanner and lead generator, never proof by itself. |
| OpenAI Codex Security | <https://github.com/openai/codex-security> | Official OpenAI CLI/SDK for authorized source-code security scans, validation, exports, patch suggestions, scan comparison, and false-positive tracking; keep as a Web2/source-code lead generator, not default Web3 audit context. |

## Knowledge And Report Feeds

| Source | URL | Local policy |
|---|---|---|
| Solodit | <https://solodit.cyfrin.io/> | Import High/Medium findings with the local deduplicating importer. |
| Code4rena reports | <https://code4rena.com/reports> | Import useful Medium/High report patterns without copying duplicate report bodies. |
| Code4rena report sitemap | <https://code4rena.com/sitemap.xml> | Discovery feed used by the local Code4rena importer. |
| Pashov audits | <https://github.com/pashov/audits> | Import distinct public audit patterns and retain original report links. |

## Discovery And Reference Sources

| Source | URL | Local policy |
|---|---|---|
| Forefy skills registry | <https://forefy.com/skills> | Discover candidates; install only after source, safety, quality, and overlap review. |
| Forefy benchmarks | <https://forefy.com/benchmarks> | Treat benchmark scores as leads, not proof that a workflow is safe or superior. |
| Pashov repository index | <https://github.com/pashov?tab=repositories> | Discover new Pashov repositories for manual review. |
| SCSVS | <https://github.com/pashov/SCSVS> | Reference checklist; use selectively rather than duplicating active skills. |
| Weird ERC20 | <https://github.com/pashov/weird-erc20> | Reference for nonstandard token behavior and integration assumptions. |

## Reviewed But Not Installed

| Source | URL | Reason |
|---|---|---|
| Rust Recon skill | <https://github.com/NVN404/rust-recon> | Runbook currently references the wrong installer repository and performs unsafe setup assumptions. |
| Rust Recon extractor | <https://github.com/NVN404/rust-recon-tool> | Cleanup can remove user-owned root files; revisit only after upstream safety fixes. |
| Digger | <https://github.com/digger-determsec/digger> | Beta EVM/Solana scanner and MCP skill; reviewed but not installed because it requires maintaining Rust binaries and overlaps as a lead generator. |
| Open Kritt | <https://github.com/Kritt-ai/open-kritt> | Full self-hosted AI audit platform; reviewed but not installed because Docker/root job containers and orchestration overlap would add operational noise. |
| One Dollar Audit | <https://www.onedollaraudit.com/> | Paid/closed-source scanner link from pashov hub; tracked only as discovery, not installed. |
| CertiK AI Auditor | <https://aiauditor.certik.com/> | Paid/closed-source scanner link from pashov hub; tracked only as discovery, not installed. |
| Pashov Solidity examples | <https://github.com/pashov/solidity> | Educational Solidity examples; not useful enough to track as an active audit skill source. |
| Pashov data-structures coursework | <https://github.com/pashov/Data-Structures-And-Algorithms> | Low relevance to audit workflow; retained only as reviewed source inventory. |
| Pashov virtual-machines coursework | <https://github.com/pashov/Virtual-machines> | Low relevance to audit workflow; retained only as reviewed source inventory. |
| Pashov OOP 2019 coursework | <https://github.com/pashov/FMI-IS-OOP-2019> | Low relevance to audit workflow; retained only as reviewed source inventory. |
| Pashov UP 2018 coursework | <https://github.com/pashov/FMI-IS-UP-2018> | Low relevance to audit workflow; retained only as reviewed source inventory. |
| Pashov data-structures 2018 coursework | <https://github.com/pashov/FMI-IS-DS-2018> | Low relevance to audit workflow; retained only as reviewed source inventory. |
| Pashov OOP 2018 coursework | <https://github.com/pashov/FMI-IS-OOP-2018> | Low relevance to audit workflow; retained only as reviewed source inventory. |

## Refresh Rule

When the user asks for updates:

1. Check every active source and relevant feed above.
2. Compare actual content, not only names or folder structure.
3. Install or merge only useful, distinct, low-noise improvements.
4. Preserve local addenda, private V3 improvements, and user customizations.
5. Keep Web3 skills separate from Web2/offensive reference libraries.
6. Update this registry when a source is added, replaced, retired, or changes status.
7. Sync approved local changes to the private backup and push them.
