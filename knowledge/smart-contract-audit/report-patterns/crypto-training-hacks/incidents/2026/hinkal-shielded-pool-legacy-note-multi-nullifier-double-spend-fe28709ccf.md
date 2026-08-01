# Crypto Training Exploit Pattern Stub: Hinkal Shielded Pool — Legacy Note Multi-Nullifier Double-Spend

Source:
- https://crypto.training/hacks/2026-07-Hinkal/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Ethereum

Loss / impact summary:
- ~$800K–$822K USDC (+ other assets) drained from Hinkal privacy pool(s)

Tags:
- logic/missing-check, logic/incorrect-state-transition, auth/signature-validation, input-validation/missing-validation

Dedupe:
- id: `2026-07-Hinkal`
- fingerprint: `fe28709ccfcf895d622be2fc6e0d72a4669882c8f635016a35206e051dc781fe`

Core exploit idea:
- 1. Hinkal is a shielded pool: deposits become commitments in an on-chain Merkle tree; spends present a ZK proof plus a nullifier. The contract records each nullifier and…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
