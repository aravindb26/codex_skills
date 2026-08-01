# Crypto Training Exploit Pattern Stub: BMX — Reward tokens are lost for LPs during NFT position transfer

Source:
- https://crypto.training/hacks/62813-bmx-reward-tokens-are-lost-for-lps-during-nft-position-transfer/

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
- logic/state-update, logic/reward-calculation

Dedupe:
- id: `62813-bmx-reward-tokens-are-lost-for-lps-during-nft-position-transfer`
- fingerprint: `8ed8259e7df0126018624fd56643b2ca5bf8757a44702570113ef459d5ff0746`

Core exploit idea:
- Position transfer settles rewards for the recipient before changing ownership, leaving the earned amount assigned to the wrong LP.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
