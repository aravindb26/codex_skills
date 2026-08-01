# Crypto Training Exploit Pattern Stub: Gondi — incorrect `_pendingWithdrawal` accounting in queueClaiming

Source:
- https://crypto.training/hacks/35211-h-09-incorrect-accounting-of-pendingwithdrawal-in-queueclai/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `35211-h-09-incorrect-accounting-of-pendingwithdrawal-in-queueclai`
- fingerprint: `6acbdfacbec3e168d21f2408fe65220e71d0291a49252ec3bbfe0c49eb3d31db`

Core exploit idea:
- 1. queueClaimAll walks each queue's getTotalReceived and distributes into newer queues. 2. Distribution writes _pendingWithdrawal[secondIdx] = pendingForQueue. 3. A seco…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
