# Crypto Training Exploit Pattern Stub: Etherspot CredibleAccountModule — [H-01] no check for `userOp` / `userOpHash` mismatch nor sender validity

Source:
- https://crypto.training/hacks/61411-h-01-no-check-for-userop-and-userophash-mismatch-nor-the-val/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61411-h-01-no-check-for-userop-and-userophash-mismatch-nor-the-val`
- fingerprint: `c360899a0a5b606fa2b24e58ab90414065b79bd50eba39dab7e9e64753ade655`

Core exploit idea:
- 1. validateUserOp(userOp, userOpHash) derives sessionKeySigner from userOpHash and validates params against userOp. 2. There is no check that userOp.sender == msg.sender…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
