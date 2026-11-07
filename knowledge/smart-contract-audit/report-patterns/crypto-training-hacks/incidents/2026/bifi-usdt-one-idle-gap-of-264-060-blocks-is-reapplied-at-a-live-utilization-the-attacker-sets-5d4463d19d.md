# Crypto Training Exploit Pattern Stub: BiFi USDT — one idle gap of 264,060 blocks is reapplied at a live utilization the attacker sets

Source:
- https://crypto.training/hacks/2026-10-bifi/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2026

Chain:
- Ethereum

Loss / impact summary:
- 165,575.149730 USDT surplus after a 40,499,999.999997 USDT Morpho flash loan is repaid in…

Tags:
- logic/reward-calculation, logic/incorrect-state-transition, logic/missing-check

Dedupe:
- id: `2026-10-bifi`
- fingerprint: `5d4463d19d69ad936dd4960b054111625a4763e61e84891560a0531efdbcbcc2`

Core exploit idea:
- The BiFi USDT market had not been touched since block 25,946,196. Rolled to the profit block, that is 264,060 blocks, about 36.7 days output.txt:29–output.txt:32. BiFi a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
