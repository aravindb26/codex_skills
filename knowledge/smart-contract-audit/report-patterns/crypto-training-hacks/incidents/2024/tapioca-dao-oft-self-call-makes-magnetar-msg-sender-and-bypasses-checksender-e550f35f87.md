# Crypto Training Exploit Pattern Stub: Tapioca DAO — OFT self-call makes Magnetar msg.sender and bypasses _checkSender

Source:
- https://crypto.training/hacks/32317-h-06-attacker-can-use-magnetaractionoft-action-of-the-magnet/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `32317-h-06-attacker-can-use-magnetaractionoft-action-of-the-magnet`
- fingerprint: `e550f35f875c98bc17568bf3b295560a1afc2e6ede605f5e5e85b7c5a27aaac0`

Core exploit idea:
- OFT self-call makes Magnetar msg.sender and bypasses _checkSender. Harm demonstrated: Nested OFT self-call drains victim collateral approved to Magnetar.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
