# Crypto Training Exploit Pattern Stub: Terplayer: A staker's legitimate withdraw() reverts on arithmetic underflow: ceiling-division delegat

Source:
- https://crypto.training/hacks/62638-c-01-withdrawal-calculation-causes-underflow-locking-all-use/

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
- id: `62638-c-01-withdrawal-calculation-causes-underflow-locking-all-use`
- fingerprint: `8640e3a8b0d82c79b54a10cc23158bf423bca79cf872438f907f133368fccd74`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
