# Crypto Training Exploit Pattern Stub: ONTR Token Zero-Owner `onlyOwner` Free Mint → Pancake WETH Drain

Source:
- https://crypto.training/hacks/2026-05-ONTR/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2026

Chain:
- Ethereum

Loss / impact summary:
- 49.480100697512152261 WETH (exact wei: 49480100697512152261)

Tags:
- access-control/missing-owner-check, access-control/broken-logic, access-control/uninitialized-owner, logic/incorrect-state-transition

Dedupe:
- id: `2026-05-ONTR`
- fingerprint: `00f98433f03742c383de75eed695477e84ffe1b0f94ab7b7156004c4102546cd`

Core exploit idea:
- 1. ONTR ships a custom Ownable whose onlyOwner is: When ownership has been renounced (owner == 0), any caller is treated as owner.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
