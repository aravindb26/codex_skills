# Local Solodit Addendum: Secure Workflow Companion

## Purpose
- Keep secure-development workflow focused on bug classes that historically lead to accepted smart-contract findings.
- Do not replace `SKILL.md`.

## When To Use

Use after reading `secure-workflow-guide/SKILL.md` for smart-contract secure development or audit preparation.

## Companion Workflow

1. Use scanners as setup, not final judgment.
2. Require manual review of high-risk modules using the matching focused local addenda.
3. Convert each scanner result into a hypothesis and run false-positive checks.
4. Capture rejected and accepted lessons into the knowledge base.

## Priority Workflow Additions

- Add invariant tests for accounting, shares, debt, rewards, and cross-chain supply.
- Add weird-token tests if arbitrary tokens are accepted.
- Add oracle failure/stale/depeg tests.
- Add upgrade migration tests from every deployed version.
- Add callback/reentrancy tests for all external transfers and hooks.

## False-Positive Filters

Do not treat a clean scanner result as proof of safety. Do not treat a scanner warning as reportable without exploitability evidence.
