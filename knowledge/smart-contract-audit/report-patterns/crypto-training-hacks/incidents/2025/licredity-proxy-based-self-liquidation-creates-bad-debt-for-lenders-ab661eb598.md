# Crypto Training Exploit Pattern Stub: Licredity — proxy-based self-liquidation creates bad debt for lenders

Source:
- https://crypto.training/hacks/62347-proxy-based-self-liquidation-creates-bad-debt-for-lenders-cy/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/insufficient-guard, logic/liquidation-manipulation, loss-of-funds/bad-debt

Dedupe:
- id: `62347-proxy-based-self-liquidation-creates-bad-debt-for-lenders-cy`
- fingerprint: `ab661eb598c7e8a73562a4c8ebb50b34f7fa9744ebccb13c5e2784a1b6c1a12c`

Core exploit idea:
- 1. Licredity.seize tries to stop an owner from profitably self-liquidating with if (position.owner == msg.sender) revert CannotSeizeOwnPosition(). 2. This checks only th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
