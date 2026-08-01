# Crypto Training Exploit Pattern Stub: LEND — Cross-chain collateral is miscalculated in borrowWithInterest

Source:
- https://crypto.training/hacks/58392-lend-cross-chain-collateral-is-miscalculated-in-borrowwithinterest/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/price-calculation, bridge/missing-validation

Dedupe:
- id: `58392-lend-cross-chain-collateral-is-miscalculated-in-borrowwithinterest`
- fingerprint: `28de6a12e4c0d98421cc1ed8dd9ee10ee8d745f4abe898e0fe5af57062254eab`

Core exploit idea:
- borrowWithInterest() counts only one side of the cross-chain collateral set, understating the required collateral and allowing excess debt.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
