# Crypto Training Exploit Pattern Stub: Autonomint odos data manipulation — AuditVault 45457

Source:
- https://crypto.training/hacks/45457-autonomint-odos-data/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- input-validation/wrong-type, logic/missing-validation

Dedupe:
- id: `45457-autonomint-odos-data`
- fingerprint: `c7e5151ac04318265aa76716d1bf9d19e9f3f6a1ebfe1c3a7e8c6637859c06a3`

Core exploit idea:
- The assembled Odos payload is trusted without checking its amount or route.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
