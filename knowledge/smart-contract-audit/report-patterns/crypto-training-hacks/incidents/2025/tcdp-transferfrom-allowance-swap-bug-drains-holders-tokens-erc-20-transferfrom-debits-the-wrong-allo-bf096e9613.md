# Crypto Training Exploit Pattern Stub: tCDP `transferFrom` allowance-swap bug drains holders' tokens — ERC-20 `transferFrom` debits the wrong allowance slot

Source:
- https://crypto.training/hacks/2025-04-tcdp/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Ethereum

Loss / impact summary:
- ~2.02 ETH (the attacker's net profit after the 0.1 ETH seed); see output.txt:1565

Tags:
- logic/incorrect-order-of-operations, access-control/broken-logic

Dedupe:
- id: `2025-04-tcdp`
- fingerprint: `bf096e9613dc0f83659caab87334dd0067d16ba4cd6bf79dd51eefc6b54f46df`

Core exploit idea:
- tCDP is an ERC-20 wrapper token for a leveraged ETH/DAI "CDP" position held on Compound — holding tCDP entitles the owner to a proportional slice of the contract's cETH…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
