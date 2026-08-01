# Crypto Training Exploit Pattern Stub: Shiny sRWA — blacklisted operators cannot be revoked and can steal NFTs

Source:
- https://crypto.training/hacks/64682-h-02-blacklisted-operators-can-not-be-revoked-from-being-an/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64682-h-02-blacklisted-operators-can-not-be-revoked-from-being-an`
- fingerprint: `4d6d199c35852450cf0d89019028ce040997de6f6e4f83aed9b300e3c4fec2e3`

Core exploit idea:
- setApprovalForAll reverts on blacklisted operator even for approved=false; approve still usable by blacklisted operators

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
