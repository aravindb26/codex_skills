# Crypto Training Exploit Pattern Stub: Beanstalk Wells — read-only reentrancy in `Well.removeLiquidity`

Source:
- https://crypto.training/hacks/18434-read-only-reentrancy-cyfrin-beanstalk-wells-markdown/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- reentrancy/read-only, logic/cei-violation

Dedupe:
- id: `18434-read-only-reentrancy-cyfrin-beanstalk-wells-markdown`
- fingerprint: `8d0f8193d01f26735c1995baae59b389d300aab1d8cba3c8f4728e2fe3d0f177`

Core exploit idea:
- 1. Well.removeLiquidity burns the caller's LP first, then transfers each underlying token out, and only after the loop calls _setReserves. 2. If one token has a transfer…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
