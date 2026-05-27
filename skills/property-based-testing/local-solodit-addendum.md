# Local Solodit Addendum: Smart Contract Properties

## Purpose

Use this companion with `property-based-testing` to turn accepted public bug patterns and local audit lessons into smart contract invariants.

The goal is to test properties that express real security guarantees, not broad assertions that only prove the harness is opinionated.

## When To Use

Use this addendum when:

- writing Foundry invariant tests, Echidna tests, Medusa tests, proptest tests, or similar property tests
- converting an audit hypothesis into a generalized invariant
- checking accounting, lifecycle, oracle, signature, bridge, or token integration behavior
- a public Solodit report suggests a pattern that may generalize to the current protocol

## Companion Workflow

1. Read the relevant code path manually before writing the property.
2. State the intended invariant in protocol language.
3. Identify the exact state variables and value flows that must preserve the invariant.
4. Search local Solodit stubs and knowledge for accepted variants of the same primitive.
5. Convert the pattern into a narrow property with a clear security impact.
6. Model realistic actors and lifecycle sequences, not only isolated function calls.
7. Include edge values: zero, dust, max, boundary ratios, stale timestamps, partial fills, empty queues, and repeated calls.
8. When a property fails, run `fp-check` logic before treating it as a vulnerability.

## Smart Contract Property Catalog

Use these as starting points when they match the protocol:

- total assets, liabilities, debt, shares, and reserves remain conserved after deposits, withdrawals, borrows, repayments, and liquidations
- deposit then withdraw roundtrip cannot produce risk-free profit beyond expected fees or rounding bounds
- no user can mint, claim, redeem, borrow, or withdraw more than their entitlement
- share price, index, accumulator, checkpoint, or reward-per-token movement respects documented monotonicity and rounding direction
- liquidation eligibility matches health-factor or solvency rules before and after interest accrual and oracle updates
- oracle stale, zero, negative, reverted, sequencer-down, or outlier prices cannot authorize unsafe state transitions
- slippage-protected swaps cannot settle below user minimums after fees, decimals, and partial fills
- request, queue, batch, epoch, or bridge messages settle, cancel, expire, or unwind exactly once
- cross-chain supply and local accounting cannot diverge after send, receive, retry, fail, or replay paths
- signatures consume nonces exactly once and cannot replay across chains, contracts, functions, users, or epochs
- token transfers are checked by balance deltas when fee-on-transfer, rebasing, callback, or nonstandard behavior is in scope
- upgrade and initialization paths cannot create an uninitialized, reinitialized, or storage-corrupted live system

## Harness Guidance

Properties should model:

- multiple users and adversarial roles
- realistic time/block movement
- lifecycle sequencing across several functions
- malicious or unusual external integrations when the protocol claims to support them
- exact accounting deltas instead of only "no revert"

## False-Positive Filters

A failing property is not automatically a bug. Kill or revise it if:

- the property is stronger than the documented protocol guarantee
- the generated state is impossible under real deployment assumptions
- the attacker actor has privileges they should not have
- the invariant ignores accepted fees, rounding loss, dust limits, or protocol-defined slippage
- the failure is only a test harness artifact
- there is no meaningful security impact under the program's severity rules

## Output Requirements

When this addendum is used, document:

- invariant name
- protocol guarantee being tested
- state variables covered
- actor model
- allowed tolerance for fees, rounding, and dust
- command used to run the property test
- failing trace or minimized sequence, if any
- whether the failure is `STRONG SUBMIT-WORTHY` or `NOT WORTH SUBMITTING`
