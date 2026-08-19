# Crypto Training Exploit Pattern Stub: Kinetiq: `reportSlashingEvent` reverts when the stale balance is below the slash amount

Source:
- https://crypto.training/hacks/58612-h-04-reportslashingevent-reverts-if-outdated-balance-is-belo/

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
- id: `58612-h-04-reportslashingevent-reverts-if-outdated-balance-is-belo`
- fingerprint: `a4ef663103106511712c0cf7eec10dbe1087dad6a47f77c3d15238ce0c160c9f`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
