# Pashov Audit Pattern: CCIP receiver interface omission strands inbound funds

- Source: Pashov Audit Group
- Imported: 2026-10-13
- Severity: MEDIUM
- Report: `Ensemble Security Review` (team PDF, M-01)
- Source finding: <https://github.com/pashov/audits/blob/e615d8a5319647f95e217616d21770b3d8372f50/team/pdf/Ensemble-security-review_2026-09-14.pdf>
- Dedupe decision: Distinct CCIP receiver-interface requirement; generic ERC721 receiver findings are not the same execution branch.

## Core Idea

A CCIP composer exposes a locally defined callback but does not advertise the official receiver interface through ERC-165, so the OffRamp releases tokens and skips settlement.

## Broken Invariant

Every external messaging adapter must satisfy the exact receiver-discovery and callback contract that the transport checks before marking a message successful.

## Where To Look

- CCIP, bridge, and message receiver contracts with local interface aliases
- ERC-165 `supportsInterface` implementations and OffRamp pre-dispatch checks
- Token release occurring before callback success or message finalization

## Attack Path

An inbound deposit or redeem releases tokens to the receiver, the transport sees unsupported interface metadata, skips the callback, and marks the message successful while user settlement remains undone.

## False-Positive Checks

- Confirm the deployed transport really performs the interface check
- Confirm the callback is skipped after token release, not retried automatically
- Trace whether a separate recovery function returns the stranded assets

## PoC Shape

Run a real OffRamp message against a receiver with and without ERC-165 support; assert that the unsupported version receives tokens but never executes settlement.

## Triage Note

The pattern is integration-specific and should be reported only when the message is finalized or otherwise cannot be retried.
