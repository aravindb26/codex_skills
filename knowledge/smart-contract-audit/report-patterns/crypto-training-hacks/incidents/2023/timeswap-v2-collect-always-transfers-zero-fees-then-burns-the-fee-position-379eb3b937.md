# Crypto Training Exploit Pattern Stub: Timeswap V2 — collect() always transfers zero fees then burns the fee position

Source:
- https://crypto.training/hacks/24903-h-03-the-collect-function-will-always-transfer-zero-fees-los/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `24903-h-03-the-collect-function-will-always-transfer-zero-fees-los`
- fingerprint: `379eb3b937e364778497e4ffdc412e9a2ad21bf389742afa0f2dad0c267ac696`

Core exploit idea:
- collect() always transfers zero fees then burns the fee position. Harm demonstrated: Fee position burned while pool transfers zero fees — permanent fee loss.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
