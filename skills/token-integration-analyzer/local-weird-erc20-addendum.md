# Local Weird ERC20 Addendum

## Purpose

Route `token-integration-analyzer` to the canonical Weird ERC20 pattern checklist without changing the original skill.

Canonical source:
- <https://github.com/d-xo/weird-erc20>

Reviewed snapshot:
- `781c8f039c106eb2d5c6071046b0dbb2f72c9870`

Local checklist:
- `/home/dinesh/.codex/knowledge/smart-contract-audit/bug-patterns/weird-erc20-token-integration-checklist.md`

## When To Use

Use after reading `token-integration-analyzer/SKILL.md` whenever the audited code accepts, transfers, escrows, lends, borrows, swaps, bridges, wraps, distributes, or prices ERC20 tokens.

Apply it especially when:

- the token list is arbitrary or permissionless
- the token list is allowlisted but semantics are not documented
- accounting credits requested amount instead of observed balance delta
- the code relies on `decimals`, `name`, `symbol`, `permit`, `approve`, `transfer`, `transferFrom`, or `balanceOf`
- the protocol supports native-token paths and ERC20-token paths together

## Required Use

1. Read the local checklist linked above.
2. Classify each token interaction by exact token behavior assumptions.
3. Convert only matching patterns into concrete checks against the current code.
4. Verify whether the protocol's scope/configuration can actually include the weird token behavior.
5. Reject any branch that is only a generic compatibility issue without meaningful impact.

## Output Discipline

For any token-integration candidate, state:

- affected token behavior
- exact integration assumption that breaks
- whether the token is arbitrary, allowlisted, or configured in deployment
- whether accounting uses requested amount or actual balance delta
- impact on funds, shares, debt, collateral, rewards, or liveness
- false-positive blocker if the branch dies

