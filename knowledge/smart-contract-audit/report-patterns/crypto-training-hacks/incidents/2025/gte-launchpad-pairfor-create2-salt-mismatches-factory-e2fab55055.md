# Crypto Training Exploit Pattern Stub: GTE — Launchpad pairFor CREATE2 salt mismatches factory

Source:
- https://crypto.training/hacks/64856-h-08-create2-address-of-the-uniswap-pair-used-by-launchpad-d/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64856-h-08-create2-address-of-the-uniswap-pair-used-by-launchpad-d`
- fingerprint: `e2fab550559ead71064c16bb4bfdf24b44d8abfa521184850cc5c968dcb1e236`

Core exploit idea:
- 1. Factory salt = keccak(token0, token1, launchpadLp, feeDistributor). 2. pairFor salt = keccak(token0, token1) only. 3. If createPair already exists, try/catch leaves t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
