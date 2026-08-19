# Crypto Training Exploit Pattern Stub: Entangle Trillion DexWrapper accepts `amountOutMin = 0` — MEV sandwich

Source:
- https://crypto.training/hacks/51371-exploiting-zero-amountoutmin-in-dexwrappers-for-mev-attacks/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- defi/mev-sandwich, defi/missing-slippage-bound

Dedupe:
- id: `51371-exploiting-zero-amountoutmin-in-dexwrappers-for-mev-attacks`
- fingerprint: `4450948a8305299dd9879d319dd60810654bbb8b8b17b10b17828e71140a01dd`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
