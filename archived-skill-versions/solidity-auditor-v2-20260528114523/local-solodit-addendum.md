# Local Solodit Addendum: Solidity Auditor Companion

## Purpose
- Ensure Solidity audits use the local Solodit-derived companion mini-skills without bloating the base `solidity-auditor` workflow.

## When To Use

Use after reading `solidity-auditor/SKILL.md` when auditing Solidity code.

## Companion Workflow

1. Keep the original file discovery and source bundling workflow.
2. Before validating any candidate, load the focused skill/addendum for that bug class.
3. Search the Solodit stubs for candidate root cause and duplicate risk.
4. Prefer manual path tracing and PoC validation over scanner output.

## Routing

- External calls/callbacks: `audit-reentrancy/local-solodit-addendum.md`
- Prices: `audit-oracle/local-solodit-addendum.md`
- Math/decimals: `audit-math-precision/local-solodit-addendum.md`
- Lending/liquidation: `audit-lending` and `audit-liquidation`
- Auth signatures: `audit-signature`
- DEX swaps: `audit-slippage`
- Rewards: `audit-staking`
- Invariants/accounting: `state-invariant-detection`

## False-Positive Filters

Do not let bundled source, scanner output, or broad agent summaries replace current-code exploitability checks.
