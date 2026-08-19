# Crypto Training Exploit Pattern Stub: Zero Staking: full-exit unstake `delete`s the Staker struct and wipes non-zero `owedRewards`

Source:
- https://crypto.training/hacks/59358-loss-of-pending-reward-when-unstaking-quantstamp-zero-stak/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `59358-loss-of-pending-reward-when-unstaking-quantstamp-zero-stak`
- fingerprint: `7e104ce5be1b857c86aa7d3b65dbc1888ec70fa87d608e14aaec0285176842bd`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
