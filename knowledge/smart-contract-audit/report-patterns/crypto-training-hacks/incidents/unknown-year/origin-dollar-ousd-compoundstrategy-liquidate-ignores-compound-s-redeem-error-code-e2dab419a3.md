# Crypto Training Exploit Pattern Stub: Origin Dollar (OUSD): `CompoundStrategy.liquidate()` ignores Compound's redeem error code

Source:
- https://crypto.training/hacks/18210-lack-of-return-value-checks-can-lead-to-unexpected-results-t/

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
- id: `18210-lack-of-return-value-checks-can-lead-to-unexpected-results-t`
- fingerprint: `e2dab419a31bd4b92bfd6dce10fef24a81e976341cdebb5636142cea17027e78`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
