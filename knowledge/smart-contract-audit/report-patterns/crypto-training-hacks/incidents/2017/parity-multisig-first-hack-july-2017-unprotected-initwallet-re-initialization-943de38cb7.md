# Crypto Training Exploit Pattern Stub: Parity Multisig First Hack (July 2017) — Unprotected `initWallet` Re-initialization

Source:
- https://crypto.training/hacks/2017-07-Parity_first_hack/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2017

Chain:
- Ethereum

Loss / impact summary:
- 82,189.93 ETH drained from a single victim wallet in the PoC

Tags:
- access-control/missing-modifier, access-control/uninitialized-owner

Dedupe:
- id: `2017-07-Parity_first_hack`
- fingerprint: `943de38cb7ef26baf9a67b0764bb2d3b74cb0a8cf5e7f71dc421eb33e53d8cae`

Core exploit idea:
- The Parity multisig wallet was a thin proxy (Wallet) that held the ETH and forwarded every unrecognized call, via delegatecall, to a single shared logic contract (Wallet…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
