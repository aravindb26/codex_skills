# Crypto Training Exploit Pattern Stub: Dhedge L2Comptroller — user can receive too few tokens when unpaused (cross-domain replay)

Source:
- https://crypto.training/hacks/18772-h-01-user-can-receive-too-few-tokens-when-l2comptroller-is-u/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- Optimism

Loss / impact summary:
- unknown

Tags:
- logic/cross-contract-state-consistency, bridge/message-replay-ordering, loss-of-funds/under-crediting

Dedupe:
- id: `18772-h-01-user-can-receive-too-few-tokens-when-l2comptroller-is-u`
- fingerprint: `cb15ffa0bdd29ea0cbd58dfce1de683b9e8c0e44f75a8e184b9e168a90fb24b3`

Core exploit idea:
- 1. When MTA is burnt on L1, a cross-domain message eventually calls L2Comptroller.buyBackFromL1(l1Depositor, receiver, totalAmountBurntOnL1) on L2, crediting the deposit…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
