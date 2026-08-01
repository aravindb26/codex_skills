# Crypto Training Exploit Pattern Stub: Autonomint cross-chain price desync — AuditVault 45459

Source:
- https://crypto.training/hacks/45459-autonomint-cross-chain-price/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- oracle/stale-price, logic/state-update

Dedupe:
- id: `45459-autonomint-cross-chain-price`
- fingerprint: `e17c99676bc658c65f3020931c92add46f3e122c52110875277d8481101f0eb9`

Core exploit idea:
- lastEthPrice is updated on one chain without synchronizing the other chain.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
