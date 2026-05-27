# Local Solodit Addendum: Solidity Secure Development

## Purpose

Use this companion with `solidity` when writing or modifying Solidity code that may be audited or deployed.

The goal is to bake accepted audit lessons into development so known bug classes are avoided before review.

## When To Use

Use this addendum when:

- implementing Solidity contracts
- modifying audit-target contracts
- adding tests for new Solidity logic
- writing fixes for a reported issue

## Companion Workflow

1. Identify the invariant the new code must preserve.
2. Search local knowledge and Solodit stubs for matching primitives before finalizing design.
3. Prefer balance-delta accounting for token integrations when token behavior can vary.
4. Make units, decimals, precision, and rounding direction explicit.
5. Validate oracle freshness, bounds, and failure modes before price-dependent state changes.
6. Consume nonces and update state in an order that prevents replay and reentrancy.
7. Add tests for zero, dust, max, stale, partial, repeated, and callback paths.
8. Run focused audit skills or `fp-check` on security-sensitive changes.

## False-Positive Filters

Do not over-engineer against impossible cases. Match defenses to:

- accepted token set
- deployment model
- trusted roles
- documented protocol guarantees
- real attacker capabilities

## Output Requirements

When this addendum is used, include:

- invariant protected by the code
- security assumptions
- relevant public/local bug pattern considered
- tests added or recommended
- residual audit concerns
