# Crypto Training Exploit Pattern Stub: Elytra: Missing 1e18 scale collapses tempElyAssetPrice to 2 (far below the 18-decimal oldElyAssetP

Source:
- https://crypto.training/hacks/63546-h-03-scaling-error-in-elyasset-price-calculation-leads-to-fe/

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
- id: `63546-h-03-scaling-error-in-elyasset-price-calculation-leads-to-fe`
- fingerprint: `65c3e84ad63b50ef814b0d5f7d218f1b5f77727d4242b5b2b05991842f15ade6`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
