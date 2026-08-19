# Crypto Training Exploit Pattern Stub: SmartSession enable-mode can be frontrun to install signed policies under a different permissionId

Source:
- https://crypto.training/hacks/42062-enable-mode-can-be-frontrun-to-add-policies-for-a-different/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, signature/insufficient-binding

Dedupe:
- id: `42062-enable-mode-can-be-frontrun-to-add-policies-for-a-different`
- fingerprint: `8e90e8ea06e38fb8ab2d7944e920e5d51cf8a1c9bff97a17e6d3ea5cae5c59d2`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
