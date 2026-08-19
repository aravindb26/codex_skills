# Crypto Training Exploit Pattern Stub: Fox Market — Flash-loan LP-bond priced from a manipulable FOX/USDT spot

Source:
- https://crypto.training/hacks/2026-08-foxmarket/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~$120k reported by TenArmor; live attacker kept ~112,976 USDT after aggregating ~482M USD…

Tags:
- oracle/spot-price, oracle/price-manipulation, logic/price-calculation, governance/flash-loan-attack

Dedupe:
- id: `2026-08-foxmarket`
- fingerprint: `099b96be63bb25cad8389e20491bdf096db54735b4bfc99bae0f783c88fac0a9`

Core exploit idea:
- 1. FoxLpBondsPool.stake() (FoxLpBondsPool.sol:136-169) is permissionless (any referred address). It quotes FOX from Pancake getAmountsOut(1e18, FOX→USDT) — a single-bloc…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
