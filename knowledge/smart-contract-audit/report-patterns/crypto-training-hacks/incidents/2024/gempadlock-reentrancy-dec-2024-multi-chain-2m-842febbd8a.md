# Crypto Training Exploit Pattern Stub: GemPadLock reentrancy (Dec 2024) — multi-chain ~$2M

Source:
- https://crypto.training/hacks/2024-12-GemPadLock/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- ~$1.9–2.2M locked LP / ERC20 inventory

Tags:
- unknown

Dedupe:
- id: `2024-12-GemPadLock`
- fingerprint: `842febbd8ab76eb68d70514f2a9e14e26c611082506cf4d085a400ad763d0ee7`

Core exploit idea:
- 1. collectFees(lockId) snapshots GemPad balances, calls INonfungiblePositionManager.collect() on a UniV3 NFT lock, then refunds balance deltas to the lock owner. 2. coll…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
