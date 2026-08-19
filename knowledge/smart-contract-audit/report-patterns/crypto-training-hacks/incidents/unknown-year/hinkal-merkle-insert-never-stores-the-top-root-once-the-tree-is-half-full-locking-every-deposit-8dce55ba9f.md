# Crypto Training Exploit Pattern Stub: Hinkal: Merkle insert never stores the top root once the tree is half-full, locking every deposit

Source:
- https://crypto.training/hacks/60149-all-funds-become-irredeemable-when-the-tree-is-halfway-pop/

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
- id: `60149-all-funds-become-irredeemable-when-the-tree-is-halfway-pop`
- fingerprint: `8dce55ba9fe3813c7c953a27f4d70678a47db0c5030019b032faf22c51110787`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
