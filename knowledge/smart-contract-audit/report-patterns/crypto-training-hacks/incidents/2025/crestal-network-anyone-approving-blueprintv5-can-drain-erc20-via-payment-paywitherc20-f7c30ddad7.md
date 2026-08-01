# Crypto Training Exploit Pattern Stub: Crestal Network — Anyone approving BlueprintV5 can drain ERC20 via Payment::payWithERC20

Source:
- https://crypto.training/hacks/55092-crestal-network-anyone-approving-blueprintv5-can-drain-erc20-via-payment-paywitherc20/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-auth, dependency/unsafe-external-call

Dedupe:
- id: `55092-crestal-network-anyone-approving-blueprintv5-can-drain-erc20-via-payment-paywitherc20`
- fingerprint: `f7c30ddad7a2ee75306e496942dc1b487e870506ef3e1497fc0ee7e7e2740b2a`

Core exploit idea:
- Payment::payWithERC20 trusts an arbitrary payer/spender relationship, so any account that has approved BlueprintV5 can be charged by an untrusted caller.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
