# Crypto Training Exploit Pattern Stub: ParaSpace: uint8 asset index truncates past 255 assets, colliding slots

Source:
- https://crypto.training/hacks/25724-h-08-nftfloororacles-asset-and-feeder-structures-can-be-corr/

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
- id: `25724-h-08-nftfloororacles-asset-and-feeder-structures-can-be-corr`
- fingerprint: `5227d29da973181e84316e9647b83820331756392d56ab7381118dc7870dbee4`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
