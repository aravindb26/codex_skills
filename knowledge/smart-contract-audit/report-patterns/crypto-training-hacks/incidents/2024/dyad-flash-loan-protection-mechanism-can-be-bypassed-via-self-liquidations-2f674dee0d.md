# Crypto Training Exploit Pattern Stub: DYAD — Flash loan protection mechanism can be bypassed via self-liquidations

Source:
- https://crypto.training/hacks/33466-h-10-flash-loan-protection-mechanism-can-be-bypassed-via-sel/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/guard-bypass, logic/state-not-refreshed, flash-loan/protection-bypass

Dedupe:
- id: `33466-h-10-flash-loan-protection-mechanism-can-be-bypassed-via-sel`
- fingerprint: `2f674dee0d0e584cf96bef43d958669366b63ca800911b23d53804bbe7855815`

Core exploit idea:
- 1. VaultManagerV2 records idToBlockOfLastDeposit[id] = block.number on every deposit(), and withdraw() reverts if that marker equals the current block — blocking a same-…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
