# Crypto Training Exploit Pattern Stub: StakeDAO: The strategy wrapper never overrides ERC20 _update

Source:
- https://crypto.training/hacks/63599-c-02-checkpoints-are-almost-always-outdated-due-to-missing/

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
- id: `63599-c-02-checkpoints-are-almost-always-outdated-due-to-missing`
- fingerprint: `5fa3ce4b38f2394a3ecbba7763b9b2045decb872a9e9259c74e632e2febcc199`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
