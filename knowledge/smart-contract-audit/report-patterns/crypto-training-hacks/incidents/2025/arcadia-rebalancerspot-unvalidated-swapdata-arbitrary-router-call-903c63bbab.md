# Crypto Training Exploit Pattern Stub: Arcadia RebalancerSpot — Unvalidated `swapData` → Arbitrary `router.call`

Source:
- https://crypto.training/hacks/2025-07-ArcadiaRebalancer/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Base

Loss / impact summary:
- ~$2.5–3.6M total (multi-tx; ~1203 ETH bridged). This PoC primary victim ≈ 197.72 WETH

Tags:
- input-validation/missing, dependency/unsafe-external-call, access-control/broken-logic, logic/missing-validation

Dedupe:
- id: `2025-07-ArcadiaRebalancer`
- fingerprint: `903c63bbab1ca77fc697639ac0dcac9de97b514e9c4cf0f0e67accf3a888aa59`

Core exploit idea:
- Arcadia’s RebalancerSpot is an Asset Manager for user Accounts. Initiators call rebalance(account, …, swapData). When swapData is non-empty, SwapLogic._swapViaRouter dec…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
