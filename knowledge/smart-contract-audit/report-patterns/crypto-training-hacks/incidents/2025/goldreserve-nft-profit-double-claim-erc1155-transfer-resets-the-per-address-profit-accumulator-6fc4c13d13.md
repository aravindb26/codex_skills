# Crypto Training Exploit Pattern Stub: GoldReserve NFT profit double-claim — ERC1155 transfer resets the per-address profit accumulator

Source:
- https://crypto.training/hacks/2025-02-GoldReserve/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- BNB Chain

Loss / impact summary:
- 12.74 BNB (≈ $7.3k at the time)

Tags:
- logic/state-update, logic/missing-check, access-control/missing-auth

Dedupe:
- id: `2025-02-GoldReserve`
- fingerprint: `6fc4c13d13c2f661dffbdf0ecd7c5a1b40ab269add1f9a3a7a673a628a7270d9`

Core exploit idea:
- GoldReserve is an ERC1155 NFT collection that distributes native-BNB "profit" to its holders. Anyone can call depositProfit{value} to push BNB into a profit pool; the po…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
