# Crypto Training Exploit Pattern Stub: Suzaku: Reward distribution divides by a zero historical-epoch stake, bricking the epoch forever

Source:
- https://crypto.training/hacks/61239-division-by-zero-in-rewards-distribution-can-cause-permane/

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
- id: `61239-division-by-zero-in-rewards-distribution-can-cause-permane`
- fingerprint: `fa65bd30474a9d70de747ab3bd9bdccaf84dffff05bdebfcc3a756c134dc5ce4`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
