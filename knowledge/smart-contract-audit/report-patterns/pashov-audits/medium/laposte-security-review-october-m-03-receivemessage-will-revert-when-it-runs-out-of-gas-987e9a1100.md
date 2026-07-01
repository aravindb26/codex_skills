# Pashov Audit Pattern: `receiveMessage()` will revert when it runs out of gas

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: MEDIUM
- Report: `LaPoste-security-review-October` (team)
- Finding ID: `M-03`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/LaPoste-security-review-October.md#L140>
- Dedupe key: `team/md/LaPoste-security-review-October.md#M-03`
- Fingerprint: `987e9a110099a341a5eaa29c0eca6dc39c72069f079b3d30a35358afc82eeb8c`

## Core Idea

A destination callback can consume nearly all forwarded gas; Solidity try/catch cannot recover when too little gas remains, so a strict ordered cross-chain lane can be permanently blocked by one attacker message.

## Broken Invariant

Untrusted destination callbacks must not be able to consume the gas required for failure handling and ordered-lane progress.

## Where To Look

- try/catch around attacker-controlled external calls
- Forward-all-gas callbacks
- Ordered message lanes where one failure blocks subsequent messages

## Attack Path

Send a message targeting a gas-burning callback; the callback exhausts forwarded gas, catch handling cannot complete, the message remains failed, and strict ordering blocks all later lane traffic.

## False-Positive Checks

- Verify EIP-150 reserve is insufficient for the catch path
- Check transport retry and skip mechanisms
- Confirm the attacker controls callback target/data and can repeat on relevant lanes

## PoC Shape

Use a callback that burns gas, process it before a valid later message, and show repeated retries fail while the later message remains unprocessable.

## Triage Note

Strength depends on whether a permissionless sender can create a non-skippable failed message and whether funds depend on lane progress.
