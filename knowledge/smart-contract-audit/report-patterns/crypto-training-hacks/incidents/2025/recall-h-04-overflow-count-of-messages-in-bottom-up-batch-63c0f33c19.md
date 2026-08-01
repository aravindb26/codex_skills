# Crypto Training Exploit Pattern Stub: Recall — [H-04] Overflow count of messages in bottom-up batch

Source:
- https://crypto.training/hacks/65091-h-04-an-attacker-can-overflow-the-count-of-messages-in-a-bot/

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
- id: `65091-h-04-an-attacker-can-overflow-the-count-of-messages-in-a-bot`
- fingerprint: `63c0f33c19dd917afb15ccb55bbb3a1fdb9f65c39fa5e1eef293c8c42c67312f`

Core exploit idea:
- Overpopulated cut batch permanently fails ensureValidCheckpoint — bottom-up halt

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
