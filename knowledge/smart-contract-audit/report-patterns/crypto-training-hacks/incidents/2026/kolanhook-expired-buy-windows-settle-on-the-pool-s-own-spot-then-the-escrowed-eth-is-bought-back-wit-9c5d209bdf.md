# Crypto Training Exploit Pattern Stub: KolanHook — expired buy windows settle on the pool's own spot, then the escrowed ETH is bought back with no price limit

Source:
- https://crypto.training/hacks/2026-10-kolanhook/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- Attacker ETH after the flash loan is repaid: 1.280491451506671761 output.txt:7, output.tx…

Tags:
- oracle/spot-price, oracle/price-manipulation, defi/slippage, logic/missing-check

Dedupe:
- id: `2026-10-kolanhook`
- fingerprint: `9c5d209bdf2734edb49876bcc339edf6e7655970c935a4f2cbad509d0202d0dc`

Core exploit idea:
- KolanHook escrows ETH for timed "buy windows" on a single ETH/KLN Uniswap v4 pool (fee 0, tick spacing 10, currency0 native ETH, currency1 KLN 0x2CADc4F2660Bb77a118b0e74…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
