# Pashov Audit Pattern: Failed cross-chain requests can drain a shared refund-fee reserve

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Ensemble Security Review` (team PDF, M-14)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Ensemble-security-review_2026-09-14.pdf>
- Dedupe decision: Distinct shared-reserve exhaustion path; not merged with ordinary fee accounting or refund rounding.

## Core Idea

An attacker can intentionally make cross-chain settlement fail after the source request is accepted, forcing the composer to pay each refund fee from a shared reserve.

## Broken Invariant

An untrusted requester must not be able to consume protocol-funded execution reserves without first funding the failure path.

## Where To Look

- Cross-chain refund and failure branches
- Response-fee payment sourced from a contract-wide reserve
- User-controlled minimum-output, destination, or callback parameters

## Attack Path

Submit requests designed to fail settlement, receive the principal refund, and repeat until the shared response-fee balance is depleted and legitimate settlements remain pending.

## False-Positive Checks

- Verify the attacker can cause failure after the fee obligation is created
- Include message fees, gas, and refund economics in the repeatability analysis
- Check whether the requester deposits a bounded failure-fee reserve

## PoC Shape

Execute repeated intentionally failing messages and reconcile reserve depletion against successful control messages.

## Triage Note

Report only when reserve exhaustion blocks a real user settlement path and is not capped by per-request funding.
