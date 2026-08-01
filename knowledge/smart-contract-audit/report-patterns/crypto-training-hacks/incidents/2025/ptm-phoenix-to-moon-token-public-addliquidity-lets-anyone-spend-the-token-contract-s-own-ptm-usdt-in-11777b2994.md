# Crypto Training Exploit Pattern Stub: PTM (Phoenix To Moon) token — public `addLiquidity()` lets anyone spend the token contract's own PTM/USDT into the LP

Source:
- https://crypto.training/hacks/2025-03-PTM/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2025

Chain:
- BNB Chain

Loss / impact summary:
- 552.63 USDT (≈ $553) net profit to the attacker [output.txt:1564-1565]

Tags:
- access-control/missing-auth, access-control/missing-modifier, logic/incorrect-state-transition

Dedupe:
- id: `2025-03-PTM`
- fingerprint: `11777b29942928e5a775b4ede8c05027a9b19c7b3a8a2bc028800d6e48783956`

Core exploit idea:
- PTM ("Phoenix To Moon") is a BSC reflection/dividend token whose fee machinery siphons part of every transfer into the token contract itself (address(this)): a 0.5% liqu…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
