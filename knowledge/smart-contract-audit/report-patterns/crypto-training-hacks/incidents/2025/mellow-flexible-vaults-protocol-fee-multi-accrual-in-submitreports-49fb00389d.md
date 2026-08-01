# Crypto Training Exploit Pattern Stub: Mellow Flexible Vaults — protocol fee multi-accrual in submitReports

Source:
- https://crypto.training/hacks/62109-h-4-protocol-fee-multiple-accrual-in-oraclesubmitreports-she/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/fee-calculation

Dedupe:
- id: `62109-h-4-protocol-fee-multiple-accrual-in-oraclesubmitreports-she`
- fingerprint: `49fb00389d3a8bba9289a96e4b9e07853c7b129507713e355439b0b02e6f073f`

Core exploit idea:
- 1. Each handleReport accrues protocol fees from last timestamp → now. 2. updateState only writes the timestamp when the asset is the base asset. 3. Non-base-first batch…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
