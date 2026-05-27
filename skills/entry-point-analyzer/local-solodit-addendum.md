# Local Solodit Addendum: Entry Point Analyzer Companion

## Purpose
- Extend entry-point mapping with Solodit-derived high-risk entry-point categories.

## When To Use

Use after reading `entry-point-analyzer/SKILL.md` at the start of smart-contract audits.

## Companion Workflow

1. Enumerate state-changing entry points as the original skill requires.
2. Add a Solodit-risk label to each entry point where applicable.
3. Prioritize permissionless high-risk entry points for first deep review.
4. Search Solodit stubs by entry-point name and risk label for duplicate/pattern awareness.

## Risk Labels

- `value-entry`: deposit, stake, mint, lock, bridge in.
- `value-exit`: withdraw, redeem, unstake, burn, bridge out.
- `debt`: borrow, repay, refinance, clear debt.
- `liquidation`: liquidate, auction, seize, bad debt.
- `oracle-settlement`: settle, execute order, keeper update, price publish.
- `callback`: token receiver, DEX callback, bridge callback, flash action.
- `admin-lifecycle`: pause, deprecate, upgrade, configure market.
- `batch-queue`: finalize, process, unwind, retry, claim batch.
- `signature`: permit, executeWithSig, metaTx, delegated action.

## False-Positive Filters

Entry-point risk labels are prioritization hints, not findings. Escalate only after code-path validation.
