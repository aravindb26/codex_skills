# Crypto Training Exploit Pattern Stub: Blockchain Bets ERC-1155 stake/transform inflates redeemable BCB → UniV2 dump

Source:
- https://crypto.training/hacks/2026-04-BlockchainBets/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Ethereum

Loss / impact summary:
- 17.568954659981801955 ETH (exact wei: 17568954659981801955)

Tags:
- logic/incorrect-calculation, logic/missing-check, logic/reward-calculation

Dedupe:
- id: `2026-04-BlockchainBets`
- fingerprint: `1e7650791db2d46052992c666bdce3d533b8991714ee3719e7081f70061cf6f5`

Core exploit idea:
- 1. Attacker CREATE-deploys a nested factory at nonce 0 that flash-swaps 4_000_000_000 raw BCB (9 decimals) from the UniV2 BCB/WETH pair. 2. Flash funds are split across…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
