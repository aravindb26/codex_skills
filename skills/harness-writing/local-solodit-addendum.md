# Local Solodit Addendum: Smart Contract PoC And Fuzz Harnesses

## Purpose

Use this companion with `harness-writing` when building smart contract PoCs, fuzz targets, invariant harnesses, or regression tests for audit findings.

The goal is to create harnesses that prove a real protocol impact with minimal artificial assumptions.

## When To Use

Use this addendum when:

- writing a Foundry, Echidna, Medusa, Hardhat, Rust, Go, Solana, Cosmos, Cairo, Substrate, TON, or Algorand security harness
- turning a Solodit pattern into a current-protocol test
- validating a high/critical candidate before report writing
- improving a fuzz harness that is too shallow or too permissive

## Companion Workflow

1. Define the exact claim the harness must prove.
2. Use real protocol contracts/modules when practical.
3. Mock only external dependencies needed to reach the path, and document what each mock replaces.
4. Model the correct actors: attacker, victim, normal user, liquidator, keeper, oracle, bridge endpoint, solver, relayer, admin, or guardian.
5. Build the protocol into a realistic pre-exploit state.
6. Execute the smallest attack sequence that breaks the invariant.
7. Assert the final impact directly: fund loss, fund lock, unauthorized state change, insolvency, replay, duplicated settlement, or rewardable liveness break.
8. Keep the command narrow and reproducible.
9. If the branch dies, remove unnecessary harness artifacts unless the user asks to preserve them.

## Solodit-Informed Harness Targets

When a matching public pattern exists, add harness support for the condition that made it exploitable:

- callback tokens, hooks, arbitrary callbacks, and receiver contracts for reentrancy paths
- fee-on-transfer, rebasing, missing return, false return, blacklisting, and decimal mismatch tokens for token integration paths
- stale, zero, outlier, paused, sequencer-down, and manipulated oracle responses for oracle paths
- dust, zero, max, boundary ratios, high precision loss, and mixed decimals for math paths
- partial fills, stale quotes, low liquidity, changed reserves, and fee deductions for slippage paths
- repeated, skipped, expired, finalized, canceled, unwound, and replayed lifecycle operations for queue/batch/bridge paths
- cross-chain domain, source chain, destination chain, nonce, and sender mismatch for message validation paths
- nonce reuse, domain mismatch, ERC-1271 behavior, malleability, and missing deadline for signature paths
- upgrade, initialize, reinitialize, storage collision, and implementation takeover paths for proxy systems

## Harness Quality Checklist

A strong audit harness should:

- prove the exploit under an unprivileged or in-scope attacker model
- avoid relying on admin setup unless the report is about in-scope configuration or initialization
- assert exact balances, shares, debt, reserves, or state transitions before and after
- include a control path when it helps triage understand expected behavior
- use labels and comments only where they clarify the exploit
- avoid broad noisy fuzzing before the invariant is understood
- produce output that can be pasted into a report without reconstruction

## False-Positive Filters

Do not treat the harness as valid evidence if:

- mocks grant impossible powers or skip mandatory real-world checks
- the setup creates an unsupported deployment state
- the attack depends on owner/admin actions outside scope
- the harness proves only revert behavior without meaningful impact
- the invariant assertion is unrelated to the program's reward bar
- the exploit only works because the test bypasses a real router, adapter, validator, or entry point that production requires

## Output Requirements

When this addendum is used, record:

- harness file path
- exact test or fuzz command
- exact observed output
- actors and assumptions
- real contracts/modules used
- mocks and what they replace
- invariant or impact asserted
- why the harness proves a submit-worthy issue or why it killed the branch
