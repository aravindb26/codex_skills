# Crypto Training Exploit Pattern Stub: FutureSwap Perpetual Drain — Fee Unit-Mismatch (`addFee` token-units interpreted as bps/share)

Source:
- https://crypto.training/hacks/2026-01-futureswap/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Arbitrum

Loss / impact summary:
- ~394,742.852305 USDC.e net attacker profit; victim drained of 197,436.748947 USDC.e of st…

Tags:
- arithmetic/decimal-mismatch, logic/fee-calculation

Dedupe:
- id: `2026-01-futureswap`
- fingerprint: `3cc5ac3118ce25cd71b6ff16cf618990dfadc7aa5f9b1207b81a444c886a91a7`

Core exploit idea:
- FutureSwap is a perpetual-swap engine. A user calls changePosition(deltaAsset, deltaStable, stableBound) to open/close/resize a position; the engine swaps the asset leg…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
