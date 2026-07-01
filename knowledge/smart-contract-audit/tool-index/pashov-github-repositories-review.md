# Pashov GitHub Repository Review

Source: <https://github.com/pashov?tab=repositories>

Checked: 2026-06-30

## Account-Level Result

The `pashov` account has 12 public repositories. Only the following are useful for the local audit setup:

- `pashov/skills`
- `pashov/audits`
- `pashov/ai-web3-security`
- `pashov/SCSVS`
- `pashov/weird-erc20`

The other repositories are old coursework, sample projects, or a Solidity compiler fork and should not be installed as audit skills.

## Useful Repositories

### `pashov/skills`

URL: <https://github.com/pashov/skills>

Checked commit: `605665fe88d5afac2cf3ba208fc3edf7fbc00e1f`

Decision:

- Keep tracking.
- Active local coverage already exists through `solidity-auditor` and `x-ray`.
- `fizz` is not installed because it does not improve the local smart-contract bounty workflow enough to justify active-skill noise.

Use:

- Source for Pashov Audit Group Solidity audit workflow updates.

### `pashov/audits`

URL: <https://github.com/pashov/audits>

Checked commit: `b60fc16f80b1291d36bd09a443e90f39bcb5d660`

Observed structure:

- 298 markdown audit reports.
- 248 team reports under `team/md/`.
- 50 solo reports under `solo/md/`.
- PDFs exist too, but should not be bulk stored locally unless needed.

Decision:

- Useful as a knowledge source, not as an active Codex skill.
- A guarded importer now extracts only manually reviewed, non-duplicate High/Medium findings into `/home/dinesh/.codex/knowledge/smart-contract-audit/report-patterns/pashov-audits/`.
- Initial import at the checked commit parsed 1,289 High/Medium findings: 1,260 were already present by normalized title in Solodit, 16 more were rejected as semantic duplicates or low-signal noise, and 13 distinct patterns were imported (4 High, 9 Medium).
- The importer refuses to add new upstream findings until each has an explicit reviewed decision, and it deduplicates report content and distilled core ideas.
- Do not clone/store the full PDF-heavy repository permanently by default because it is large and would add storage cost.

Importer:

- `/home/dinesh/.codex/knowledge/smart-contract-audit/scripts/pashov_audits_ingest.py`
- `/home/dinesh/.codex/knowledge/smart-contract-audit/report-patterns/pashov-audits/indexes/reviewed-decisions.jsonl`

Use:

- Public audit-report pattern mining.
- Duplicate-risk and known-pattern comparison.
- High/Medium examples across lending, DEX, stablecoin, yield, bridge, RWA, staking, NFT, and wallet systems.

### `pashov/ai-web3-security`

URL: <https://github.com/pashov/ai-web3-security>

Checked commit: `e2b4db57a24e62023af65c2cb415e9c435d7f442`

Decision:

- Keep tracking as a discovery index.
- It is not an installable skill repo because it only contains a curated tool list.
- See `pashov-ai-web3-security-tools.md` for installed and skipped entries.

Use:

- Discover new Web3 AI/security tools and skill repos.

### `pashov/SCSVS`

URL: <https://github.com/pashov/SCSVS>

Checked commit: `a0de46c9e1c37c3ee3b8bd60cb46e816c7084e03`

Decision:

- Useful as a checklist/reference source.
- Do not install as an active skill because the local audit workflow and installed skills already cover the same categories more directly.
- Consider targeted reference use for coverage completeness, especially token, governance, oracle, vault, bridge, NFT, liquid staking, liquidity pool, integration, arithmetic, access-control, upgradeability, and DoS categories.

Use:

- Audit coverage cross-check.
- Scoping and completeness checklist.

### `pashov/weird-erc20`

URL: <https://github.com/pashov/weird-erc20>

Checked commit: `266025c555b42b2dd2517fd99f7d47032ec99abe`

Decision:

- Useful as a token-integration reference corpus.
- Do not install as a separate active skill because local skills already include token-integration and external-call/token-safety guidance.
- Good for test-case ideas when auditing ERC20 integrations.

Useful token behaviors:

- reentrant transfer hooks
- missing return values
- false return values
- fee-on-transfer
- rebasing or external balance changes
- upgradeable tokens
- flash minting
- blocklists
- pausable tokens
- approval race protections
- revert on zero transfer
- multiple token addresses/proxies
- low decimals
- high decimals
- `transferFrom(src == msg.sender)` semantic differences

Use:

- ERC20 integration edge-case checklist.
- Mock token ideas for PoCs and invariant tests.

## Not Useful For Active Audit Setup

### `pashov/solidity`

URL: <https://github.com/pashov/solidity>

Decision:

- Do not install.
- It is a fork of the Solidity compiler/language repo, not a Codex audit skill or finding-pattern source.

### Old Coursework / Sample Repositories

URLs:

- <https://github.com/pashov/Data-Structures-And-Algorithms>
- <https://github.com/pashov/Virtual-machines>
- <https://github.com/pashov/FMI-IS-OOP-2019>
- <https://github.com/pashov/FMI-IS-UP-2018>
- <https://github.com/pashov/FMI-IS-DS-2018>
- <https://github.com/pashov/FMI-IS-OOP-2018>

Decision:

- Do not install.
- Not relevant to smart-contract audits, source-code bounty hunting, or local Codex audit skills.

## Future Update Rule

When the user asks for updates, check:

- `pashov/skills` for skill updates.
- `pashov/ai-web3-security` for newly listed tool repos.
- `pashov/audits` for new markdown audit reports that can be imported as High/Medium report-pattern stubs.

Use `pashov/SCSVS` and `pashov/weird-erc20` as references only when a target audit needs checklist or token-integration edge-case coverage.
