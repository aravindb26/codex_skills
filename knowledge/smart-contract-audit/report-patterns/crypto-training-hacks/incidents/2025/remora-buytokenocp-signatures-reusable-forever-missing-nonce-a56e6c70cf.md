# Crypto Training Exploit Pattern Stub: Remora — `buyTokenOCP` signatures reusable forever (missing nonce)

Source:
- https://crypto.training/hacks/63777-signatures-on-tokenbank-and-allowlist-can-be-reused-in-perpe/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- signature/missing-nonce, auth/replay, logic/free-mint

Dedupe:
- id: `63777-signatures-on-tokenbank-and-allowlist-can-be-reused-in-perpe`
- fingerprint: `a56e6c70cff7e568b02cf3e93c4cb9cfbc520cd1b1a4edef4857bc836d388b92`

Core exploit idea:
- 1. buyTokenOCP verifies an EIP-712-style BuyToken(investor, token, amount) signature and skips on-chain payment. 2. The hash omits a nonce and nothing marks the digest a…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
