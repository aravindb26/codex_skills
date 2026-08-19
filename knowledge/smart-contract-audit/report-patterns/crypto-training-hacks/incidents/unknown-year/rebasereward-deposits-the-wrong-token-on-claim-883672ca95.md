# Crypto Training Exploit Pattern Stub: RebaseReward deposits the wrong token on claim

Source:
- https://crypto.training/hacks/58205-c-01-rebasereward-fails-because-of-incorrect-token-handling/

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
- id: `58205-c-01-rebasereward-fails-because-of-incorrect-token-handling`
- fingerprint: `883672ca95b143b0516bacc6d40480ef0b7e7613f1a63168646c81b23b667da6`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
