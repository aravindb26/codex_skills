# Crypto Training Exploit Pattern Stub: Sperax Farms: future farm-start underflows elapsed time, letting the first depositor drain the whole reward pool

Source:
- https://crypto.training/hacks/59249-underflow-in-farm-getrewardaccrualtimeelapsed-quantstamp-s/

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
- id: `59249-underflow-in-farm-getrewardaccrualtimeelapsed-quantstamp-s`
- fingerprint: `819bc0e3a3496f661aafcd94ce7a09fb0d8eedc9ef2b66c7ba5e5780d782d413`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
