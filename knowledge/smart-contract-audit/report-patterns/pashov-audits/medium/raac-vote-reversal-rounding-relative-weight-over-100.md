# Pashov Audit Pattern: Vote reversal rounding can make relative gauge weight exceed 100 percent

- Source: Pashov private contest lesson
- Imported: 2026-07-22
- Severity: MEDIUM
- Pattern family: gauge voting math

## Core Idea

Vote removal reconstructs and subtracts scheduled bias/slope using a different rounding model than live gauge-weight projection. Clearing votes can reduce the global denominator below a surviving gauge's live weight, causing `relativeWeight` to exceed 100 percent.

## Broken Invariant

For every epoch:

```text
pointsSum[epoch].bias >= max(pointsWeight[gauge][epoch].bias)
relativeWeight(gauge, epoch) <= 1e18
```

## Where To Look

- `_reverseLockEntries`
- `pointsWeight`
- `pointsSum`
- `relativeWeight`
- vote clear, kick, or remove vote paths
- forward projection vs reverse reconstruction

## Attack Path

Create several votes with boundary-sensitive lock times, clear some votes, and observe that the remaining gauge weight is larger than the global denominator. A reward distributor that trusts the ratio can overpay the gauge.

## False-Positive Checks

- Compare exact rounding in forward and reverse paths.
- Check whether relative weights are capped before reward distribution.
- Check whether global denominator can be clamped below live gauge weight.
- Do not dismiss as generic gauge rounding unless this exact denominator-underflow-by-reversal root is known.

## PoC Shape

Construct two gauges, vote both, clear one side, then assert `relativeWeight > 1e18` or a downstream distribution drains more than the epoch deposit.
