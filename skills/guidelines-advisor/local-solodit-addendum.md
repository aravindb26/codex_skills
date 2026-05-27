# Local Solodit Addendum: Guidelines Advisor Companion

## Purpose
- Add Solodit-informed prioritization to smart-contract best-practice guidance.
- Do not replace `SKILL.md`.

## When To Use

Use after reading `guidelines-advisor/SKILL.md` when advising on smart-contract architecture or pre-audit readiness.

## Companion Workflow

1. Separate hard security risks from general best practices.
2. Map advice to historically accepted High/Medium bug classes only when relevant.
3. Recommend focused audits/addenda for high-risk modules instead of broad generic hardening.

## High-Value Guidance Areas

- Explicit unit/decimal conventions.
- Internal accounting instead of raw token balances.
- Pull payments and per-user claims over batch pushes.
- Strict callback authentication.
- Upgrade/migration playbooks and storage layout checks.
- Program-level invariants written before implementation.
- Oracle adapter validation and failure modes.

## False-Positive Filters

Do not present guideline gaps as vulnerabilities unless a concrete exploit path exists.
