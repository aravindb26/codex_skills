# Crypto Training Exploit Pattern Stub: EigenLayer — impossible to slash queued withdrawals containing a malicious strategy (misplaced ++i)

Source:
- https://crypto.training/hacks/20057-h-02-it-is-impossible-to-slash-queued-withdrawals-that-conta/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/loop-increment-misplacement, dos/unslashable-withdrawal, loss-of-funds/slashing-evasion

Dedupe:
- id: `20057-h-02-it-is-impossible-to-slash-queued-withdrawals-that-conta`
- fingerprint: `b2b8a71edbdbac5ae3fae2976e8dd43840eb9cd3c8de6963bf1a95f136b9d80c`

Core exploit idea:
- 1. slashQueuedWithdrawal(recipient, queuedWithdrawal, tokens, indicesToSkip) lets the owner skip strategies in a queued withdrawal — designed so that a malicious strateg…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
