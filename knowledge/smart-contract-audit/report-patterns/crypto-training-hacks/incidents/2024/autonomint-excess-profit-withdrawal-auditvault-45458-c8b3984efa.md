# Crypto Training Exploit Pattern Stub: Autonomint excess profit withdrawal — AuditVault 45458

Source:
- https://crypto.training/hacks/45458-autonomint-excess-profit/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, access-control/missing-modifier

Dedupe:
- id: `45458-autonomint-excess-profit`
- fingerprint: `c8b3984efa842bbfa9897cbb4299e3c5b0f0b978cd3aa5cf4b56ac266bc4d637`

Core exploit idea:
- The cumulative profit value is not consumed, so CDS owners can withdraw it repeatedly.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
