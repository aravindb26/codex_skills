# Crypto Training Exploit Pattern Stub: BMX — DoSed Voter::finalize() due to unbounded pending removals lacking a batch argument

Source:
- https://crypto.training/hacks/62810-bmx-dosed-voter-finalize-due-to-unbounded-pending-removals-lacking-a-batch-argument/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/unbounded-loop, dos/griefing

Dedupe:
- id: `62810-bmx-dosed-voter-finalize-due-to-unbounded-pending-removals-lacking-a-batch-argument`
- fingerprint: `46e86160196bb6dedd1fe7ebb76dc37916b065f61c52d34bf7117bd28bfe5aba`

Core exploit idea:
- A permissionless finalize loop processes all pending removals instead of a bounded batch, allowing an attacker to make finalization consume unbounded gas.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
