# Local Solodit Addendum: Smart Contract Differential Review

## Purpose

Use this companion with `differential-review` when reviewing smart contract commits, PRs, patches, contest diffs, or protocol upgrades.

The goal is to catch security-relevant behavior changes that resemble accepted public bug patterns, while avoiding noisy "changed code looks risky" claims.

## When To Use

Use this addendum when a diff touches:

- asset movement, accounting, shares, debt, rewards, or reserves
- oracle, price, quote, or slippage logic
- callbacks, hooks, external calls, token integrations, or bridge messages
- access control, signatures, nonces, initialization, or upgrades
- lifecycle transitions such as queues, epochs, batches, settlement, cancellation, or liquidation

## Companion Workflow

1. Identify the exact behavioral change, not just the textual diff.
2. Map changed entry points, callers, state writes, external calls, and invariants.
3. Compare changed primitives against local Solodit stubs and knowledge-base lessons.
4. Ask whether the patch introduced, removed, reordered, or weakened a check that public reports relied on.
5. Check whether the blast radius includes unchanged functions that depend on the old behavior.
6. Validate likely exploit paths with targeted tests before reporting.

## False-Positive Filters

Do not escalate a diff finding if:

- the change is only refactoring with identical reachable behavior
- the old behavior was unsafe but the diff actually tightens the invariant
- the report depends on a pre-upgrade state that cannot exist after migration
- the path is reachable only by trusted upgrade/admin actors
- the impact is not rewardable under the current program

## Output Requirements

When this addendum is used, include:

- old behavior
- new behavior
- affected invariant
- reachable attacker path
- related Solodit/local pattern, if any
- why the change is or is not submit-worthy
