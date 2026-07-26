# Pashov Audit Pattern: Capped payout consumes the full claim cursor

- Source: Pashov private contest lesson
- Imported: 2026-07-22
- Severity: MEDIUM
- Pattern family: vesting and reward claims

## Core Idea

A reward library advances `epochsClaimed` or another claim cursor before making the payout. If payout is capped by remaining `totalDistributed`, the unpaid portion is lost because the cursor already marks it claimed.

## Broken Invariant

Claim progress must match paid entitlement. A partial or capped payout must preserve the unpaid part or advance only the paid portion.

## Where To Look

- `epochsClaimed`
- `totalClaimed`
- `totalDistributed`
- `claimable`
- `_claimReward`
- `updateReward`
- `min(claimable, remaining)`

## Attack Path

Create an over-subscribed distribution or rounding drift where earlier users consume most available funds. A late user claims, receives a capped payout, and permanently loses the remaining entitlement because the cursor is advanced.

## False-Positive Checks

- Confirm the cap does not revert.
- Confirm cursor advances before or regardless of actual payout.
- Confirm no debt/shortfall field records the unpaid amount.
- Do not confuse this with fee-on-transfer or failed-transfer cases.

## PoC Shape

Make total reconstructed entitlements exceed `totalDistributed`, claim with earlier users first, then show a late user's unpaid slice cannot be claimed later.
