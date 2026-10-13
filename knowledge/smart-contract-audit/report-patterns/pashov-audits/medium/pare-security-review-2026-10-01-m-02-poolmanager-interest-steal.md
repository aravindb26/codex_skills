# Pashov Audit Pattern: Permissionless interest claims can expose PoolManager-held yield

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Pare Security Review` (team PDF, M-02)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Pare-security-review_2026-10-01.pdf>
- Dedupe decision: Distinct Uniswap v4 custody path; the claim target is the PoolManager and transient settlement allows a caller to take shares credited there.

## Core Idea

Interest accrued to the Uniswap v4 `PoolManager` can be claimed by any caller, and the caller can settle and take the manager-held shares without proving ownership of the related position.

## Broken Invariant

Accrued yield must remain claimable only by the position or treasury entitled to it, even when the accounting holder is an integration manager.

## Where To Look

- `claimInterest` functions accepting arbitrary holders or pool managers
- Uniswap v4 `settle`, `take`, and delta accounting around interest claims
- Bookkeeping that credits a contract address instead of an owner-bound claim

## Attack Path

Trigger an interest claim for the PoolManager, settle the resulting delta, take the shares to the attacker, and repeat after each index increase.

## False-Positive Checks

- Trace the exact `msg.sender` and pool-key authorization checks
- Confirm the PoolManager-held balance is not intentionally public protocol surplus
- Prove the attacker receives assets rather than only moving an internal accounting entry

## PoC Shape

Accrue interest to a pool, call the claim path as an unrelated address, and assert that the attacker can withdraw the resulting balance.

## Triage Note

Use the integration's actual PoolManager settlement semantics; mocks that do not enforce transient deltas are insufficient.
