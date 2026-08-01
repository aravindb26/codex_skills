# Crypto Training Exploit Pattern Stub: Tapioca DAO — Unwhitelisted marketHelper returns malicious removeCollateral payload

Source:
- https://crypto.training/hacks/32313-h-02-missing-check-on-helper-contract-allows-arbitrary-actio/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `32313-h-02-missing-check-on-helper-contract-allows-arbitrary-actio`
- fingerprint: `26f9f975700aa82f9596aef568c11976ca2f3163afbf561e6c2f8a9ae311b0dc`

Core exploit idea:
- Unwhitelisted marketHelper returns malicious removeCollateral payload. Harm demonstrated: Malicious marketHelper steals victim collateral via Magnetar approval.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
