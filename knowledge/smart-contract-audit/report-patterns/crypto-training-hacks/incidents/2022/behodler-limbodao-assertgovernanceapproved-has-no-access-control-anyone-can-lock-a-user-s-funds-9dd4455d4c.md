# Crypto Training Exploit Pattern Stub: Behodler / LimboDAO — `assertGovernanceApproved` has no access control (anyone can lock a user's funds)

Source:
- https://crypto.training/hacks/42453-h-01-lack-of-access-control-on-assertgovernanceapproved-can/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-check, dos/frozen-funds

Dedupe:
- id: `42453-h-01-lack-of-access-control-on-assertgovernanceapproved-can`
- fingerprint: `9dd4455d4cf279d42e7caf97f5e61f0efd51faeff56d7fdaac7b69d688d5670b`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
