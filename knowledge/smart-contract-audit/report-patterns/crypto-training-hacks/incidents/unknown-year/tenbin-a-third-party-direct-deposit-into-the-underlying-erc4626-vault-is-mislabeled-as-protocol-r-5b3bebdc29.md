# Crypto Training Exploit Pattern Stub: Tenbin: A third-party direct deposit into the underlying ERC4626 vault is mislabeled as protocol r

Source:
- https://crypto.training/hacks/64975-direct-vault-deposits-incorrectly-counted-as-revenue-leading/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64975-direct-vault-deposits-incorrectly-counted-as-revenue-leading`
- fingerprint: `5b3bebdc2911719387ee28713acc405be21e5e21e87417cda2da6f8c2f01961c`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
