# Crypto Training Exploit Pattern Stub: DODO Cross-Chain DEX — unauthorized claim of non-EVM chain refunds

Source:
- https://crypto.training/hacks/58582-h-5-unauthorized-claim-of-non-evm-chain-refunds-in-claimrefu/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/auth-bypass, loss-of-funds/direct-drain, logic/address-encoding

Dedupe:
- id: `58582-h-5-unauthorized-claim-of-non-evm-chain-refunds-in-claimrefu`
- fingerprint: `f3a4f8a11d27efe0eab3e2a7670dd2b845bd0c3e46c72ccd36808b8ed946071d`

Core exploit idea:
- 1. Refunds store a walletAddress blob (20 bytes for EVM, longer for BTC/etc.). 2. claimRefund only decodes receiver when length is exactly 20; otherwise receiver stays m…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
