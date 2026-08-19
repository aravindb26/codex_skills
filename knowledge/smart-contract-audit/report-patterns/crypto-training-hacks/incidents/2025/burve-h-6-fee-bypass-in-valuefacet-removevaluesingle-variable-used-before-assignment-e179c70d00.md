# Crypto Training Exploit Pattern Stub: Burve H-6: fee bypass in `ValueFacet.removeValueSingle` (variable used before assignment)

Source:
- https://crypto.training/hacks/56955-h-6-fee-bypass-in-valuefacetremovevaluesingle-sherlock-bur/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `56955-h-6-fee-bypass-in-valuefacetremovevaluesingle-sherlock-bur`
- fingerprint: `e179c70d00048059faab6ed474d8eea6efdf5ddbdc24e492243d9615e2584be7`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
