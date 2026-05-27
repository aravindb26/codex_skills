# Local Solodit Addendum: Spec-To-Code Compliance Companion

## Purpose
- Extend spec-to-code review with accepted-report patterns where code violates documented rules or standard semantics.

## When To Use

Use after reading `spec-to-code-compliance/SKILL.md` when docs/specs/standards and code are both available.

## Companion Workflow

1. Extract exact spec claims and invariants before reading implementation assumptions.
2. For every mismatch, classify whether it affects funds, permissions, liveness, or accounting.
3. Search Solodit stubs by standard/spec name, invariant phrase, and affected function.
4. Route security-relevant mismatches to focused skills for exploitability validation.

## High-Value Spec Gaps

- ERC4626 maxWithdraw/maxRedeem/preview functions differ from standard.
- EIP-712 typehash/domain/digest differs from signed struct.
- Bridge message status differs from documented success/failure semantics.
- Liquidation/health-factor docs omit real collateral or fee behavior.
- Queue/batch lifecycle docs promise settlement/unwind but code can orphan requests.
- Access-control docs name one actor but code allows another.

## False-Positive Filters

Do not report documentation drift unless the spec is program-relevant and the mismatch creates a rewardable security impact.
