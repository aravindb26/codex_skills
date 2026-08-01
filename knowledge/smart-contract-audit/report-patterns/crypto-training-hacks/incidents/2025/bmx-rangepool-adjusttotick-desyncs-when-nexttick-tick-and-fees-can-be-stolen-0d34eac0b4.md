# Crypto Training Exploit Pattern Stub: BMX — RangePool::adjustToTick() desyncs when nextTick == tick and fees can be stolen

Source:
- https://crypto.training/hacks/62812-bmx-rangepool-adjusttotick-desyncs-when-nexttick-tick-and-fees-can-be-stolen/

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
- logic/incorrect-state-transition, logic/fee-calculation

Dedupe:
- id: `62812-bmx-rangepool-adjusttotick-desyncs-when-nexttick-tick-and-fees-can-be-stolen`
- fingerprint: `0d34eac0b4441578a1c2ff0ab6133d3f66b0f278c08acacb53dbbd01354ad675`

Core exploit idea:
- The equal-tick branch skips the reserve update, so the accounting view and the actual range pool diverge and the stale fee balance can be taken.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
