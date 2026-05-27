# Local Solodit Addendum: Full Audit Orchestrator Companion

## Purpose
- Make full smart-contract audits use the local Solodit-derived addenda and knowledge base deliberately.
- Do not replace `SKILL.md` or its references.

## When To Use

Use after reading `smart-contract-audit/SKILL.md` during full Solidity, Anchor, Vyper, TON/FunC/Tact, Sui/Move, or broad Web3 audits.

## Companion Workflow

1. Complete Program Lock and coverage ledger first.
2. Before hunting a bug class, load the matching focused skill and its `local-solodit-addendum.md` if present.
3. For candidates, search `/home/dinesh/.codex/knowledge/smart-contract-audit/report-patterns/solodit/` by protocol primitive, function name, error text, and bug class.
4. Use Solodit matches as duplicate-risk and pattern-memory leads, not proof.
5. Re-anchor before report writing: Program Memory, relevant skills, local addenda, knowledge base, candidate verification card, PoC output.

## Focus Routing

- Oracle / flash loan: `audit-oracle`, `oracle-flashloan-analysis`
- Math / units / rounding: `audit-math-precision`, `dimensional-analysis`
- Lending / liquidation: `audit-lending`, `audit-liquidation`
- Reentrancy / callbacks: `audit-reentrancy`, `reentrancy-pattern-analysis`
- Signatures / replay: `audit-signature`, `signature-replay-analysis`
- Slippage / DEX: `audit-slippage`
- Staking / rewards: `audit-staking`
- DoS / queues / liveness: `dos-griefing-analysis`
- State accounting: `state-invariant-detection`
- Upgradeability: `proxy-upgrade-safety`
- Token integrations: `token-integration-analyzer`

## False-Positive Filters

Do not report from pattern memory alone. A candidate must survive current code tracing, scope/known-issue checks, duplicate-risk checks, and PoC or strong source evidence.
