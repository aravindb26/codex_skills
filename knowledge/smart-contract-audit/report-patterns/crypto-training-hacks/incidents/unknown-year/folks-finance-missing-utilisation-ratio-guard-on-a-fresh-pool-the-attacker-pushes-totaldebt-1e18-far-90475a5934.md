# Crypto Training Exploit Pattern Stub: Folks Finance: Missing utilisation-ratio guard: on a fresh pool the attacker pushes totalDebt (1e18) far

Source:
- https://crypto.training/hacks/61019-infinite-interest-rate-bug-immunefi-folks-finance-git/

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
- id: `61019-infinite-interest-rate-bug-immunefi-folks-finance-git`
- fingerprint: `90475a5934dd46d85d540e33ed39a7a1e366f0a5cbee284919ba520d30421fe2`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
