# Crypto Training Exploit Pattern Stub: Recall — [H-09] Cross msg recipient can block checkpoint submission

Source:
- https://crypto.training/hacks/65096-h-09-cross-msg-recipient-can-block-checkpoint-submission-cod/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65096-h-09-cross-msg-recipient-can-block-checkpoint-submission-cod`
- fingerprint: `def5d6b02a1388c4531e4e90c1831798f9698b35eec202993456b26c63f12134`

Core exploit idea:
- Unbounded returndata from IPC recipient gas-bombs checkpoint execution under remaining gas

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
