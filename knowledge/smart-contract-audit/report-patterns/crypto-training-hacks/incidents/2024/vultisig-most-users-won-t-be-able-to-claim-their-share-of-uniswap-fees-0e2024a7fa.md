# Crypto Training Exploit Pattern Stub: Vultisig — most users won't be able to claim their share of Uniswap fees

Source:
- https://crypto.training/hacks/35753-h-01-most-users-wont-be-able-to-claim-their-share-of-uniswap/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/shared-pool-drain, logic/max-collect-not-own-share, dos/fund-loss-cascading

Dedupe:
- id: `35753-h-01-most-users-wont-be-able-to-claim-their-share-of-uniswap`
- fingerprint: `0e2024a7fa5a40f43af072fd808c4e560826bf7b7c69362b374fd7f7bd659c0c`

Core exploit idea:
- 1. Multiple ILO investor NFT positions share ONE underlying Uniswap V3 position (same TICK_LOWER/TICK_UPPER), so they also share one pool of accrued swap fees. 2. claim(…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
