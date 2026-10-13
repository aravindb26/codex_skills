# Solodit Pattern Stub: Pi interest rate model is manipulatable due to current balances used

Source:
- https://solodit.cyfrin.io/issues/pi-interest-rate-model-is-manipulatable-due-to-current-balances-used-spearbit-none-astera-pdf

Imported:
- 2026-05-23

Status:
- distilled from the primary Astera/Spearbit report

Severity:
- MEDIUM

Protocol:
- Astera mini pools / Cod3x Pi interest-rate strategy

Source platform / firm:
- Spearbit review, December 2024

Tags:
- lending/interest-rate-manipulation
- utilization/current-balance-snapshot
- donation/available-liquidity
- stale-state/once-per-block-integral

Dedupe:
- id: `62297`
- fingerprint: `a56f3ab61504b9399a9ccc8d15102439d340260190e26773e9b092eb9df79e5b`

Core idea:
- The Pi strategy computes utilization from the current available-liquidity and debt snapshot, then updates its integral error only when the strategy is called. The report's Medium finding explains that same-block flash-loan/borrow-repay sequences can manipulate the direction of the PID rate update because the integral is not refreshed between operations.
- A separate note in the report's later comments explicitly warns that direct donations to an aToken can increase `balanceOf(aToken)`, lower minipool utilization, and affect the calculated rate. This note is related but distinct from the detailed §5.2.15 PI-integral finding.

Broken invariant:
- A rate controller should not let a transient or attacker-adjustable current-balance snapshot steer the rate-control state for an interval whose history was not represented by that snapshot.

Where to look in code:
- Utilization calculations using raw `IERC20(asset).balanceOf(...)` or current cash/debt snapshots.
- PI/PID or integral-controller state updated once per block/transaction while multiple operations can alter utilization before the next update.
- Rate changes applied to elapsed time or accumulated controller state using only the latest utilization snapshot.

Attack path:
1. Use same-block operations (the report describes flash-loan deposit/withdraw/borrow and borrow/repay ordering) to alter utilization around the rate strategy call while its integral state is not refreshed between operations.
2. Cause the next rate update to move in the attacker's preferred direction.
3. The report identifies a separate direct-donation surface: transfer assets directly to the aToken to increase its observed balance and lower utilization.

False-positive checks:
- Establish whether the manipulation changes only a future rate or also reprices previously unaccrued interest; do not conflate these temporal mechanisms.
- Trace every checkpoint and whether multiple same-block changes can reuse stale controller state.
- Distinguish raw donation effects from tracked deposits/withdrawals and verify whether the donation is reversible or permanently transferred.
- Quantify borrower savings and lender/protocol losses after the attacker's donation, repayment, and any shares/yield costs.
- In exact duplicate analysis, compare affected state, update ordering, interval semantics, attacker setup, and downstream loss; thematic use of utilization alone is not exact root-cause equality.

PoC shape:
- Compare control and attacked same-block operation sequences against the actual interest-rate strategy; record utilization, integral state, resulting borrow/supply rates, and net attacker/lender outcomes.
- For the donation note, transfer the asset directly to the aToken, then cause the actual rate calculation, and compare with a checkpointed/no-donation control.

Triage notes:
- Detailed report: Astera/Spearbit, December 2024, §5.2.15, Medium Risk; both Astera and Spearbit marked it acknowledged. Primary PDF: https://github.com/spearbit/portfolio/blob/master/pdfs/Astera-Spearbit-Security-Review-December-2024.pdf
- The report's raw-balance donation comment is a close prior-art warning, not by itself proof that another protocol's exact execution root or impact is duplicated.
