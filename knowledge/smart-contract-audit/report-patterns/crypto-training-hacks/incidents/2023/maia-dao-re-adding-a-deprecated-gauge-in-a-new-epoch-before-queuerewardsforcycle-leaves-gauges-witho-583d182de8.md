# Crypto Training Exploit Pattern Stub: Maia DAO — Re-adding a deprecated gauge in a new epoch before queueRewardsForCycle() leaves gauges without rewards

Source:
- https://crypto.training/hacks/26047-h-13-re-adding-a-deprecated-gauge-in-a-new-epoch-before-call/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/reward-calculation, dos/frozen-funds, timing/stale-cycle-read

Dedupe:
- id: `26047-h-13-re-adding-a-deprecated-gauge-in-a-new-epoch-before-call`
- fingerprint: `583d182de8b25034bae8a352af6f79e41c119dae8a2ae88213fc176e372324a1`

Core exploit idea:
- 1. When a gauge is deprecated (removeGauge), its weight is subtracted from _totalWeight but the gauge's own vote weight is preserved in storage. 2. Re-adding it (addGaug…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
