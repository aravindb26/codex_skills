# Crypto Training Exploit Pattern Stub: Drips Network DaiDripsHub `give()` — `uint128 → int128` cast flips fund flow

Source:
- https://crypto.training/hacks/2026-07-DripsDaiHub/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- Ethereum

Loss / impact summary:
- 24,882.995421947667857715 DAI (full DaiReserve balance at attack block)

Tags:
- arithmetic/overflow, input-validation/boundary, logic/missing-validation

Dedupe:
- id: `2026-07-DripsDaiHub`
- fingerprint: `693f2461baeb0a1904725cba14d811d3df0344cf76ea984da8ca3e8bd9d5da2d`

Core exploit idea:
- 1. Drips Network’s DAI hub lets any user call give(receiver, amt) to gift DAI stream collectable balance to a receiver. Accounting debits the giver via a signed _transfe…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
