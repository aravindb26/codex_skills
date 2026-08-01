# Crypto Training Exploit Pattern Stub: Ammplify — H-7: `collectFees` re-targets original `asset.liq` after `adjustMaker`

Source:
- https://crypto.training/hacks/63173-h-7-makercollectfees-re-targets-liquidity-to-original-amount/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63173-h-7-makercollectfees-re-targets-liquidity-to-original-amount`
- fingerprint: `3c876a20826f657dd19a09a0ee9b6b65e3e52c598bda747489e921f880deae3b`

Core exploit idea:
- 1. newMaker stores asset.liq = 300e18. 2. adjustMaker sets live liq to 100e18 but leaves asset.liq unchanged. 3. collectFees re-targets to asset.liq → position snaps bac…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
