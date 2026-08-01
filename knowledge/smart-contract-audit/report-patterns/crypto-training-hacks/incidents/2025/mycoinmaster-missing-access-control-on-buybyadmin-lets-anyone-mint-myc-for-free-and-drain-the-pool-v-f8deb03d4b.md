# Crypto Training Exploit Pattern Stub: MyCoinMaster missing-access-control on `buyBYAdmin` lets anyone mint MYC for free and drain the pool via `swap` — public function lacked an `onlyAdmin` guard present on every other privileged path

Source:
- https://crypto.training/hacks/2025-08-MyCoinMaster/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~653.49 USD (653.63 USDT) — [output.txt:1594,1663,1672]

Tags:
- access-control/missing-auth, access-control/missing-modifier, logic/incorrect-state-transition

Dedupe:
- id: `2025-08-MyCoinMaster`
- fingerprint: `f8deb03d4bd0b86be5f2725243358e68a28e612ca14255fc2982f4b552d776e2`

Core exploit idea:
- MyCoinMaster is a BNB-Chain token-sale / staking protocol where users normally buy the MYC token by paying either BNB or USDT. The "buy" path locks the purchased tokens…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
