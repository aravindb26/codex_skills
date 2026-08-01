# Crypto Training Exploit Pattern Stub: Panoptic — cross-contract reentrancy converts phantom shares to real shares

Source:
- https://crypto.training/hacks/65026-h-02-cross-contract-reentrancy-in-liquidation-enables-conver/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65026-h-02-cross-contract-reentrancy-in-liquidation-enables-conver`
- fingerprint: `7fbba77ee5f6ff25f9d73fa165fdcc67c857111223a2c7df4330a80b7a9824df`

Core exploit idea:
- 1. Liquidation delegates type(uint248).max phantom shares on ct0 and ct1. 2. ct0.settleLiquidation refunds ETH to liquidator before ct1 is revoked. 3. Reentrant transfer…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
