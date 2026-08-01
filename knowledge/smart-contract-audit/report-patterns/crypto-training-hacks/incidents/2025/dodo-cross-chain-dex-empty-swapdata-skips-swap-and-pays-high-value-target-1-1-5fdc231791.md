# Crypto Training Exploit Pattern Stub: DODO Cross-Chain DEX — empty `swapData` skips swap and pays high-value target 1:1

Source:
- https://crypto.training/hacks/58580-h-3-attacker-can-steal-an-high-value-token-due-to-lack-of-sw/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/broken-logic, loss-of-funds/direct-drain, logic/missing-swap-enforcement

Dedupe:
- id: `58580-h-3-attacker-can-steal-an-high-value-token-due-to-lack-of-sw`
- fingerprint: `5fdc231791599385f09b8cb2789316319695e1cb71348fbf58aae52b09719722`

Core exploit idea:
- 1. _doMixSwap short-circuits when swapData is empty: return amount. 2. No check that the deposit token equals decoded.targetZRC20. 3. Attacker deposits 100 AVAX.ZRC20, e…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
