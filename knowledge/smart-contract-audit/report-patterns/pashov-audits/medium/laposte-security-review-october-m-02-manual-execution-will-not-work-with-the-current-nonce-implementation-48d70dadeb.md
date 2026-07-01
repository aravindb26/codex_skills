# Pashov Audit Pattern: Manual Execution will not work with the current nonce implementation

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `LaPoste-security-review-October` (team)
- Finding ID: `M-02`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/LaPoste-security-review-October.md#L105>
- Dedupe key: `team/md/LaPoste-security-review-October.md#M-02`
- Fingerprint: `48d70dadeb7b803d930022fbee02c8b2f9fdba02ef5a4c83a7b8ae5ff3462235`

## Core Idea

A strict cross-chain nonce advances only after successful delivery, but failed CCIP messages require manual retry under nonce state that no longer matches the retry semantics, preventing recovery and blocking later ordered messages.

## Broken Invariant

A failed ordered message must remain retryable without making the lane's nonce state impossible to satisfy.

## Where To Look

- Strictly ordered bridge or CCIP lanes
- Nonce updates coupled only to success
- Manual-execution and retry entry points using original message nonces

## Attack Path

Cause one destination execution to fail, then invoke the transport's manual retry; nonce validation rejects the original message or leaves the lane unable to advance, so later messages remain blocked.

## False-Positive Checks

- Read the exact CCIP manual-execution guarantees
- Confirm retry preserves the original sequence number
- Check whether the transport, not the application, bypasses application nonce checks

## PoC Shape

Deliver message N with insufficient gas, retry N manually, and show application nonce validation prevents recovery while N+1 cannot proceed.

## Triage Note

Tie impact to locked funds or persistent lane blockage rather than a single failed message.
