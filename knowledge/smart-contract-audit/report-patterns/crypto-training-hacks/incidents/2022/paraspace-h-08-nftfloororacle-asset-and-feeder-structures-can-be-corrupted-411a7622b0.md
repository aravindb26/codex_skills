# Crypto Training Exploit Pattern Stub: ParaSpace — [H-08] NFTFloorOracle asset and feeder structures can be corrupted

Source:
- https://crypto.training/hacks/15981-h-08-nftfloororacles-asset-and-feeder-structures-can-be-corr/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `15981-h-08-nftfloororacles-asset-and-feeder-structures-can-be-corr`
- fingerprint: `411a7622b0f08f420b9cb95df94fd35a6d92017bbe923a518a681037b1e3b0f4`

Core exploit idea:
- 1. Asset indices stored as uint8; assets never shrinks on remove (delete only). 2. After 256 assets, the next add stores uint8(256) == 0. 3. removeAsset then zeros the w…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
