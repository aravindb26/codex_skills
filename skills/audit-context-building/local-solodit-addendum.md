# Local Solodit Addendum: Context Building Companion

## Purpose
- Use Solodit lessons to improve what gets noticed during context building without turning this skill into vulnerability reporting.

## When To Use

Use after reading `audit-context-building/SKILL.md` during first-pass line-by-line audit comprehension.

## Companion Workflow

1. Do not report findings in context mode.
2. While reading, tag snippets that resemble accepted-report patterns from local addenda.
3. Record the exact unknown/invariant/candidate lead, then continue context building.
4. Later, route the lead to the focused audit skill and local addendum for validation.

## What To Tag

- State variables updated in different lifecycle paths.
- Off-chain inputs used after state can change.
- External calls before final accounting.
- Queue/batch/state pointer movement.
- Rounding/scaling/unit conversions.
- Oracle/version/price selection.
- Access-control assumptions and trusted-role boundaries.

## False-Positive Filters

In context mode, tags are leads only. Do not call them vulnerabilities until a focused skill validates exploitability.
