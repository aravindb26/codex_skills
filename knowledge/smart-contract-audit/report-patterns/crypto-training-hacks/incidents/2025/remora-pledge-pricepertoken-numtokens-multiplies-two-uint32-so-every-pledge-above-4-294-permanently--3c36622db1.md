# Crypto Training Exploit Pattern Stub: Remora Pledge: `pricePerToken * numTokens` multiplies two `uint32`, so every pledge above ~$4,294 permanently reverts

Source:
- https://crypto.training/hacks/61172-pledgemanagerpledge-refundtokens-will-revert-due-to-overfl/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61172-pledgemanagerpledge-refundtokens-will-revert-due-to-overfl`
- fingerprint: `3c36622db15470dd462dd02a2dadb369878734af8d34fd02d72b44abcbedd18f`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
