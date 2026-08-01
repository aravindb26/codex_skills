# Crypto Training Exploit Pattern Stub: FlyLong (FLG) — public balance-forger lets any caller fake the LP's token balance and drain the WBNB side of the pair — access-control/missing-auth

Source:
- https://crypto.training/hacks/2025-04-flylong/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~1.73 BNB (PoC extracts 1.7258625 BNB; ~1 BNB of dust remains in the pair as 0.0001726035…

Tags:
- access-control/missing-auth, access-control/broken-logic, logic/state-update, oracle/price-manipulation

Dedupe:
- id: `2025-04-flylong`
- fingerprint: `7d416b77661f5104c8bf7149f089c95753281b10997446825bf5f3f13c07b073`

Core exploit idea:
- FlyLong is an obfuscated BSC ERC-20 whose code keeps a custom liquiditySwapFrom mapping as its "real" balance ledger (balanceOf just reads it). Two of its functions are…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
