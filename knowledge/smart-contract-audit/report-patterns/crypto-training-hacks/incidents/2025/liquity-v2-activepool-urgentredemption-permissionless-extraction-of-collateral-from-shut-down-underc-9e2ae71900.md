# Crypto Training Exploit Pattern Stub: Liquity V2 ActivePool `urgentRedemption` — permissionless extraction of collateral from shut-down undercollateralized troves at a +2% bonus

Source:
- https://crypto.training/hacks/2025-07-ActivePoolUrgentRedemption/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Ethereum

Loss / impact summary:
- ~2,696.49 USD (1.0385 ETH per on-chain transaction) output.txt:1562

Tags:
- logic/incorrect-state-transition, access-control/missing-auth, defi/slippage, oracle/price-calculation

Dedupe:
- id: `2025-07-ActivePoolUrgentRedemption`
- fingerprint: `9e2ae71900ccfb3d4dc4f798b166ffaf4e4bb1886f801b31c6bbf445fe2b95e9`

Core exploit idea:
- Liquity V2 lets each collateral branch (e.g. the sUSDe branch) be shut down in an emergency. When a branch is shut down the TroveManager opens a public urgentRedemption(…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
