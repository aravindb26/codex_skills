# Crypto Training Exploit Pattern Stub: Sablier Flow — Sender can brick a stream by forcing an overflow in the debt calculation

Source:
- https://crypto.training/hacks/42010-sender-can-brick-stream-by-forcing-overflow-in-debt-calculat/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- arithmetic/overflow, dos/permanent, logic/missing-check

Dedupe:
- id: `42010-sender-can-brick-stream-by-forcing-overflow-in-debt-calculat`
- fingerprint: `18276783a8bbede6c81c2b3a28fa9afa6e8dacc7d42790993d46714dc47be63b`

Core exploit idea:
- 1. Sablier Flow streams tokens continuously based on a per-second rate, ratePerSecond, chosen entirely by the stream's sender at creation (or via adjustRatePerSecond). 2…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
