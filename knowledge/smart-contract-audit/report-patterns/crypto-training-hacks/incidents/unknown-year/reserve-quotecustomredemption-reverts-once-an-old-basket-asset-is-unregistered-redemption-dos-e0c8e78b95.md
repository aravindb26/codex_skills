# Crypto Training Exploit Pattern Stub: Reserve `quoteCustomRedemption` reverts once an old basket asset is unregistered (redemption DoS)

Source:
- https://crypto.training/hacks/27331-h-01-custom-redemption-might-revert-if-old-assets-were-unreg/

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
- logic/array-out-of-bounds, defi/denial-of-service

Dedupe:
- id: `27331-h-01-custom-redemption-might-revert-if-old-assets-were-unreg`
- fingerprint: `e0c8e78b95d7de4a493192f51cbe2e862de2575e33ad48098f44ef87c18052f4`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
