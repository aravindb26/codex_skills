# Crypto Training Exploit Pattern Stub: Blackhole — Reward token in `GaugeFactoryCL` can be drained by anyone

Source:
- https://crypto.training/hacks/58334-h-02-reward-token-in-gaugefactorycl-can-be-drained-by-anyone/

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
- unknown

Dedupe:
- id: `58334-h-02-reward-token-in-gaugefactorycl-can-be-drained-by-anyone`
- fingerprint: `2fe6a8109dc84444f681cfff0d1ca798e85c78370afe46ca55b7f5689c878d19`

Core exploit idea:
- 1. createGauge is external with no authorization. 2. Each call seeds Algebra eternal farming with a hardcoded 1e10 of _rewardToken pulled from the factory. 3. Anyone can…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
