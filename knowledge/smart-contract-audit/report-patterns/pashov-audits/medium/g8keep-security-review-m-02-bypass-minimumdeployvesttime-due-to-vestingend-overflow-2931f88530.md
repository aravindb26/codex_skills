# Pashov Audit Pattern: Bypass `minimumDeployVestTime` due to vestingEnd overflow

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `g8keep-security-review` (team)
- Finding ID: `M-02`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/g8keep-security-review.md#L174>
- Dedupe key: `team/md/g8keep-security-review.md#M-02`
- Fingerprint: `2931f88530b09edf3e4f3f8a8f32ef4c5df71ec02b7375ec35b35f50a1726524`

## Core Idea

A minimum vesting duration is validated before the resulting end timestamp is narrowed to uint40, allowing truncation to wrap the stored end time and bypass the enforced lock.

## Broken Invariant

Values validated in a wide type must preserve the validated range when stored in a narrower type.

## Where To Look

- Explicit downcasts after validation
- start plus duration timestamp arithmetic
- Vesting, timelock, epoch, and deadline fields stored in narrow integers

## Attack Path

Choose a duration whose wide end timestamp passes the minimum check but truncates when cast to uint40, producing an earlier stored end and enabling premature claim.

## False-Positive Checks

- Confirm Solidity uses an explicit truncating cast rather than SafeCast
- Prove attacker control reaches values above uint40 max
- Check upstream caps and realistic transaction encoding limits

## PoC Shape

Select start and duration so the wide sum exceeds 2^40, store it, and show the truncated end permits claim before the intended minimum duration.

## Triage Note

Reject if an upstream cap makes overflow unreachable in the deployed configuration.
