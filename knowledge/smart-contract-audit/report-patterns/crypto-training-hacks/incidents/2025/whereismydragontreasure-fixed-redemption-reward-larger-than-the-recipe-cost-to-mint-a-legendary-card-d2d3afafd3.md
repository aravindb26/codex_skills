# Crypto Training Exploit Pattern Stub: WhereIsMyDragonTreasure — fixed redemption reward larger than the recipe cost to mint a legendary card

Source:
- https://crypto.training/hacks/2025-07-WhereIsMyDragonTreasure/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- $47,461.35 (≈ 12.776 ETH, the full singleReward)

Tags:
- logic/price-calculation, logic/wrong-condition, oracle/price-manipulation

Dedupe:
- id: `2025-07-WhereIsMyDragonTreasure`
- fingerprint: `d2d3afafd30e00661e33d66dc41a9dbf7465a6fffb64f02727a232bfd7911b0b`

Core exploit idea:
- WhereIsMyDragonTreasure is a "treasure chest" side contract of the WhereIsMyDragon NFT-card game. Players who manage to obtain the game's legendary card can send it to t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
