# Crypto Training Exploit Pattern Stub: SushiMaker — Bridgeless `convert()` Lets an Attacker Insert a Fake Pair and Steal Onsen Fee Liquidity (Badger DIGG)

Source:
- https://crypto.training/hacks/2021-01-Sushi_Badger_Digg/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2021

Chain:
- Ethereum

Loss / impact summary:
- ~81 WBTC + DIGG of accumulated Onsen LP fees siphoned from the SushiMaker (≈ low-hundreds…

Tags:
- access-control/missing-validation, logic/missing-check

Dedupe:
- id: `2021-01-Sushi_Badger_Digg`
- fingerprint: `0bfe5ba0b29fef6e75d73a96383ad4911c992b9482c879458a4343cf895da101`

Core exploit idea:
- SushiMaker.convert(token0, token1) (:85) takes the LP tokens the SushiMaker has accrued as protocol fees for a given pair, burns them to get the two underlying tokens, a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
