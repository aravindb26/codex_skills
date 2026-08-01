# Crypto Training Exploit Pattern Stub: KittenSwap — Lack of `lastMintedPeriod` update allows unlimited minting of Kitten

Source:
- https://crypto.training/hacks/58066-c-02-lack-of-lastmintedperiod-update-allows-unlimited-mintin/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58066-c-02-lack-of-lastmintedperiod-update-allows-unlimited-mintin`
- fingerprint: `9df639524721730306ac0b1ad743b69af1cfd608bd1e4ad489720d5f40199cdc`

Core exploit idea:
- 1. Minter.updatePeriod() is meant to mint weekly Kitten once per epoch period. 2. The guard is if (currentPeriod > lastMintedPeriod). 3. After minting, the code never wr…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
