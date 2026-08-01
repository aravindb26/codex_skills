# Crypto Training Exploit Pattern Stub: NFTMirror — Anyone can re-mint a token that was burned by the owner

Source:
- https://crypto.training/hacks/50036-c-01-anyone-can-re-mint-a-token-that-was-burned-by-the-owner/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `50036-c-01-anyone-can-re-mint-a-token-that-was-burned-by-the-owner`
- fingerprint: `0a699a6f83210dfe7c405df71f2b3486dadf23ab48b8bfa3b51704d214964d51`

Core exploit idea:
- 1. Non-existent tokens default to locked, so only the beacon can mint them. 2. Owner can burn an unlocked token; burn does not set lock state back to locked. 3. After bu…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
