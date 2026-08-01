# Crypto Training Exploit Pattern Stub: Burve — Fee bypass in ValueFacet.removeValueSingle

Source:
- https://crypto.training/hacks/56955-burve-fee-bypass-in-valuefacet-removevaluesingle/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/fee-calculation, logic/missing-check

Dedupe:
- id: `56955-burve-fee-bypass-in-valuefacet-removevaluesingle`
- fingerprint: `5f8b4d52ec21c39a42d02befbb48cfa25eb1500dc2e2d575eacd3ebf48b9f7aa`

Core exploit idea:
- The single-sided removal path reaches the transfer without applying the configured exit fee, allowing users to bypass protocol fees.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
