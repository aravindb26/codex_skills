# Crypto Training Exploit Pattern Stub: Univ3CollateralToken — Uni V3 position counted as collateral for every vault owned by the same minter

Source:
- https://crypto.training/hacks/2026-03-Univ3CollateralToken/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- Base

Loss / impact summary:
- ~57,000 USD (USDC + USDC.e drained from the USDI reserve)

Tags:
- logic/incorrect-state-transition, logic/state-update, access-control/broken-logic

Dedupe:
- id: `2026-03-Univ3CollateralToken`
- fingerprint: `6610d470182eeb2befab38fc9596f92a0283f8a32931300cfced8714a7a6f76b`

Core exploit idea:
- Univ3CollateralToken is the Uni-V3-position collateral adapter for a lending system (USDI / VaultController). When a user deposits a Uni V3 NFT into a vault, the contrac…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
