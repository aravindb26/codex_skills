# Crypto Training Exploit Pattern Stub: Centrifuge v3.1 — pool managers steal other pools pending deposits

Source:
- https://crypto.training/hacks/64195-h-1-pool-managers-can-steal-all-other-pools-pending-deposits/

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
- unknown

Dedupe:
- id: `64195-h-1-pool-managers-can-steal-all-other-pools-pending-deposits`
- fingerprint: `c28733f76a995ae312582c00a12b04b1a6ddb88d99c502f6a6000a9b44546c2d`

Core exploit idea:
- Spoke.requestCallback uses current requestManager without binding to the manager that created the request

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
