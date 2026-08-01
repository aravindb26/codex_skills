# Crypto Training Exploit Pattern Stub: Phi — Exposed public _add/_removeCredIdPerAddress bricks victim sells

Source:
- https://crypto.training/hacks/41091-h-05-exposed-removecredidperaddress-addcredidperaddress-al/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-visibility, dos/state-corruption

Dedupe:
- id: `41091-h-05-exposed-removecredidperaddress-addcredidperaddress-al`
- fingerprint: `c8bc890c764248d35ab7ace67db2e1d472d90056ec37a08997b99ea5ee423277`

Core exploit idea:
- Public _removeCredIdPerAddress lets anyone strip a victim's credId list so their subsequent sell reverts and shares are frozen

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
