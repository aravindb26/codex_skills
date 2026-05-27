# Local Solodit Addendum: Smart Contract Coverage Analysis

## Purpose

Use this companion with `coverage-analysis` when assessing whether a smart contract fuzz or PoC harness actually reaches security-critical paths.

Coverage is useful only if it exercises the protocol states where real bug patterns happen.

## When To Use

Use this addendum when:

- a fuzz harness is not finding useful bugs
- a PoC may be too narrow or artificial
- invariant tests miss lifecycle or edge-state paths
- mutation or fuzz results need coverage interpretation

## Companion Workflow

1. List security-critical paths from scope, architecture, and local Solodit patterns.
2. Compare coverage against those paths, not just percentage.
3. Check whether entry points, modifiers, callbacks, hooks, oracle branches, token edge cases, and revert paths are reached.
4. Identify unreachable states needed for accepted public bug classes.
5. Improve the harness before trusting a "no bug found" result.

## Smart Contract Coverage Targets

Prioritize coverage for:

- deposit, withdraw, mint, burn, borrow, repay, liquidate, claim, bridge, settle, cancel, and unwind paths
- zero, dust, max, stale, partial, expired, and boundary states
- callbacks and external integrations
- oracle failure and fallback paths
- fee, rounding, decimals, and scaling branches
- admin initialization and upgrade boundaries when in scope

## False-Positive Filters

Do not overvalue coverage if:

- high line coverage misses state combinations
- covered functions are only happy paths
- mocks remove the risky integration behavior
- the harness cannot reach attacker-controlled call paths
- failing assertions prove a harness artifact instead of protocol impact

## Output Requirements

When this addendum is used, report:

- security-critical paths covered
- security-critical paths missed
- unreachable state reasons
- harness improvements needed
- whether current coverage is enough to support or kill a candidate
