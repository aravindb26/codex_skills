# Crypto Training Exploit Pattern Stub: Forte Float128 `Ln.ln` silently accepts non-positive inputs (mispriced settlement / stolen collateral)

Source:
- https://crypto.training/hacks/55705-h-03-natural-logarithm-function-silently-accepts-invalid-non/

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
- math/missing-input-validation, defi/mispricing

Dedupe:
- id: `55705-h-03-natural-logarithm-function-silently-accepts-invalid-non`
- fingerprint: `665c01fd53ec1a4390eb48c5e34975d103610cf95ebe17a758847b90ea76e54f`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
