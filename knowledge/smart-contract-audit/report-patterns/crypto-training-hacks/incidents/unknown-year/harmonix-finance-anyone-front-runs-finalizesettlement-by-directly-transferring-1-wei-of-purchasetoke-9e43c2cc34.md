# Crypto Training Exploit Pattern Stub: Harmonix Finance: Anyone front-runs finalizeSettlement() by directly transferring 1 wei of purchaseToken to

Source:
- https://crypto.training/hacks/63977-h-02-the-finalizesettlement-can-be-dossed-leading-to-refund/

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
- id: `63977-h-02-the-finalizesettlement-can-be-dossed-leading-to-refund`
- fingerprint: `9e43c2cc346cfdd2b1d078fb0b022421091776bbcfcfa975276fc2521ae17001`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
