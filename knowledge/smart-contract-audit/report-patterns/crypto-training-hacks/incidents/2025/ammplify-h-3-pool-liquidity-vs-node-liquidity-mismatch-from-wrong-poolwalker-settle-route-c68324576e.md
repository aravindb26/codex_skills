# Crypto Training Exploit Pattern Stub: Ammplify — H-3: Pool liquidity vs node liquidity mismatch from wrong `PoolWalker.settle` route

Source:
- https://crypto.training/hacks/63169-h-3-mismatch-in-actual-pools-liquidity-and-pool-nodes-liquid/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/fee-calculation

Dedupe:
- id: `63169-h-3-mismatch-in-actual-pools-liquidity-and-pool-nodes-liquid`
- fingerprint: `c68324576ee90d63e619b2504e0d5a2fa22bfa847165896f62a311d1216dc521`

Core exploit idea:
- 1. WalkerLib.modify marks nodes using high index treeTick(highTick) - 1. 2. PoolWalker.settle walks high index treeTick(highTick) (one higher). 3. Settlement skips the c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
