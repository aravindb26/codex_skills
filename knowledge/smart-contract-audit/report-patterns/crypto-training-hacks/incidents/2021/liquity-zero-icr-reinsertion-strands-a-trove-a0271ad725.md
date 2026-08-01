# Crypto Training Exploit Pattern Stub: Liquity — zero-ICR reinsertion strands a trove

Source:
- https://crypto.training/hacks/18030-liquity-zero-icr-trove-removal/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2021

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, logic/state-update, dos/frozen-funds

Dedupe:
- id: `18030-liquity-zero-icr-trove-removal`
- fingerprint: `a0271ad725b0e7ad0a8f5a42968d5182349c022dffe491f7a405b323ffce03e1`

Core exploit idea:
- SortedTroves removes a node and only reinserts it for a positive ICR. A zero-ICR update leaves TroveManager's existence belief inconsistent, so addCollateral and other c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
