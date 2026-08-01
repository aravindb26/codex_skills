# Crypto Training Exploit Pattern Stub: Origin — listing deposit can be withdrawn repeatedly

Source:
- https://crypto.training/hacks/17095-origin-marketplace-repeated-withdraw/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/state-update, logic/missing-check, logic/wrong-condition

Dedupe:
- id: `17095-origin-marketplace-repeated-withdraw`
- fingerprint: `14ec8783252c793e7cbb7d9bdba1d7216db5d98cbb530038b109103826979655`

Core exploit idea:
- withdrawListing authorizes the deposit manager but never marks the listing withdrawn. The same deposit can be transferred six times, draining the marketplace reserve.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
