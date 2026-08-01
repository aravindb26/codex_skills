# Crypto Training Exploit Pattern Stub: Tadle — `DeliveryPlace::settleAskTaker` has incorrect access control

Source:
- https://crypto.training/hacks/38066-deliveryplacesettleasktaker-has-incorrect-access-control-cod/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/wrong-condition, access-control/role-bypass, liveness/denial-of-service

Dedupe:
- id: `38066-deliveryplacesettleasktaker-has-incorrect-access-control-cod`
- fingerprint: `c141a4111438800b8a0da0750d1e50d0799dd62d62359bd09c2a7bd3ee1f4b7a`

Core exploit idea:
- 1. settleAskTaker's own devdoc says the caller must be the stock authority — the party who actually holds the Ask-type settlement stock and is obligated to deliver point…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
