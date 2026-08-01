# Crypto Training Exploit Pattern Stub: Nouns Builder — when reservedUntilTokenId > 100, first founder loses 1% NFT

Source:
- https://crypto.training/hacks/29423-h-1-when-reserveduntiltokenid-100-first-funder-loss-1-nft-sh/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, state/unreachable-storage-slot, loss-of-funds/direct-drain

Dedupe:
- id: `29423-h-1-when-reserveduntiltokenid-100-first-funder-loss-1-nft-sh`
- fingerprint: `e8344a1a98aed05002f40fca9879d0bea0a2b3dcc2caa755c8b77c18592a0708`

Core exploit idea:
- 1. _addFounders schedules a founder's NFT allocation slots by seeding a cursor: uint256 baseTokenId = reservedUntilTokenId;. 2. Every REAL ERC-721 token id that will eve…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
