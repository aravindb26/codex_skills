# Local Solodit Addendum: Smart Contract Mutation Testing

## Purpose

Use this companion with `mutation-testing` when using mutants to assess smart contract test strength.

The goal is to learn whether tests enforce real audit invariants, not just whether they kill many mutants.

## When To Use

Use this addendum when:

- configuring mewt, muton, or similar mutation testing for Solidity, TON, or Web3 code
- checking whether invariant tests catch Solodit-style bugs
- selecting mutants for accounting, access control, oracle, lifecycle, signature, or token-integration code

## Companion Workflow

1. Start from manually identified invariants and public bug patterns.
2. Prioritize mutants that alter security meaning: check removal, comparison flip, rounding direction, stale-value use, unit scaling, nonce use, auth gate, and state-update order.
3. Run a narrow campaign on critical files before broad campaigns.
4. Inspect surviving mutants manually.
5. Treat surviving mutants as test gaps first, not confirmed bugs.
6. Convert meaningful surviving mutants into candidate hypotheses and run `fp-check`.

## High-Value Mutant Classes

Prioritize mutants that affect:

- `>=` vs `>`, `<` vs `<=`, equality checks, and zero checks
- fee, price, share, debt, reward, or reserve math
- rounding direction and precision scaling
- stale timestamps and oracle freshness
- nonce consumption and replay prevention
- role checks and caller validation
- before/after ordering of external calls and state writes
- batch, queue, epoch, settlement, and cancellation state transitions

## False-Positive Filters

Do not report a surviving mutant directly if:

- the mutant is impossible in the real source
- the changed behavior has no attacker path
- the impact is only test incompleteness
- the killed or surviving status is caused by weak mocks
- the mutant does not map to the current program's rewardable impact

## Output Requirements

When this addendum is used, include:

- target files
- mutant class
- surviving security-relevant mutants
- missing invariant or test
- candidate bug hypothesis, if any
- verification status
