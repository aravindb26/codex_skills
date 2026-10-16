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

## Coverage-Feedback Loop And Crash Triage

After each fuzzing run:

1. Compare reached paths against the invariant and critical-path map; prioritize meaningful state transitions over aggregate coverage percentage.
2. For each important missed path, diagnose the blocker: missing setup or actor, action ordering/depth, boundary value, role or time precondition, oracle/sysvar state, restrictive harness constraint, or unrealistic mock.
3. Change the harness, structured/action-sequence mutator, seed corpus, or input constraints to address that specific blocker. Do not treat simply increasing runtime as a substitute for fixing reachability.
4. Re-run and check whether the intended path became reachable; preserve useful seeds and record remaining unreachable paths and their concrete reasons.
5. For every crash or failed property, reproduce and minimize the input/sequence, then distinguish a real target failure from an expected revert, harness defect, or environment failure. Map a real failure to a violated invariant and assess scope and impact before treating it as a finding.

No crash is not evidence of safety when critical paths remain unreached or the harness cannot represent the relevant states.

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
