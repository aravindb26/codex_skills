# Crypto Training Exploit Pattern Stub: Majority Protocol — re-join after leave permanently locks second entry fee

Source:
- https://crypto.training/hacks/65375-impossible-for-user-to-get-refund-after-re-joining-a-resched/

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
- id: `65375-impossible-for-user-to-get-refund-after-re-joining-a-resched`
- fingerprint: `4cd51c43aa8ead3a147254246627177fb38665c9361ed8289ffc61d587ce7d6b`

Core exploit idea:
- After leaveRescheduledGame sets hasRefunded[gameId][player]=true, _payEntryFee on re-join never clears that flag. When the game is later cancelled, refundCancelledGame r…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
