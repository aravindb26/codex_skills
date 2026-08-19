# Crypto Training Exploit Pattern Stub: Euler HookTargetStakeDelegator double-counts the migrated stake

Source:
- https://crypto.training/hacks/55523-double-counting-of-the-migrated-stake-mixbytes-none-euler-ma/

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
- logic/accounting-error, defi/reward-accounting, dos/fund-lock

Dedupe:
- id: `55523-double-counting-of-the-migrated-stake-mixbytes-none-euler-ma`
- fingerprint: `d7bed3d27d603f4d5083b72b74d5262fa0e42ba20d061aba615ea3c3a0f7ba92`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
