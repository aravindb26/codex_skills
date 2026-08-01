# Crypto Training Exploit Pattern Stub: Accountable — Cancelling redeem requests permanently blocks the withdrawal queue

Source:
- https://crypto.training/hacks/62968-cancelling-redeem-requests-permanently-blocks-the-withdrawal/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- liveness/queue-deadlock, logic/pointer-not-advanced

Dedupe:
- id: `62968-cancelling-redeem-requests-permanently-blocks-the-withdrawal`
- fingerprint: `a95749b63181e709a83bb0c9af22b71489c13b60d0f1efb7258e620117a22469`

Core exploit idea:
- 1. Redeem requests sit in a FIFO queue keyed by nextRequestId (head). 2. Cancelling a request fully deletes the entry (controller = address(0)) without advancing the hea…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
