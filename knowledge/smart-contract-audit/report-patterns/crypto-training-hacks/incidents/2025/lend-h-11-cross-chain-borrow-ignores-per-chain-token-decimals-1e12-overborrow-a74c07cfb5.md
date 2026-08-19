# Crypto Training Exploit Pattern Stub: LEND H-11: cross-chain borrow ignores per-chain token decimals (~1e12× overborrow)

Source:
- https://crypto.training/hacks/58380-h-11-users-will-lose-funds-due-to-token-decimal-mismatches/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `58380-h-11-users-will-lose-funds-due-to-token-decimal-mismatches`
- fingerprint: `a74c07cfb51a166fdd8a2397a5f3fa1bda400826a8341e80f6855ff3bde97b9a`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
