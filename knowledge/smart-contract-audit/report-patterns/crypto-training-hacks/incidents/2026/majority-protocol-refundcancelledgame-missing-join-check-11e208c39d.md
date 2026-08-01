# Crypto Training Exploit Pattern Stub: Majority Protocol — refundCancelledGame missing join check

Source:
- https://crypto.training/hacks/65373-attacker-can-drain-all-tokens-from-cancelled-game-since-sess/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2026

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `65373-attacker-can-drain-all-tokens-from-cancelled-game-since-sess`
- fingerprint: `11e208c39d7f3f2fa256bd0914a75bd70b70f5696e5188bd550970e145c95e7d`

Core exploit idea:
- SessionManager.refundCancelledGame only checks that the game is Cancelled, then refunds ticketPrice to msg.sender without verifying contestants[gameId][msg.sender]. An a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
