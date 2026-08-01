# Crypto Training Exploit Pattern Stub: Ajna Protocol — PositionManager's `moveLiquidity` freezes residual LP on partial moves

Source:
- https://crypto.training/hacks/20069-h-01-positionmanagers-moveliquidity-can-freeze-funds-by-remo/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds

Dedupe:
- id: `20069-h-01-positionmanagers-moveliquidity-can-freeze-funds-by-remo`
- fingerprint: `4ba79a9e7fd7a290da38818f2ccbeff7a0bffe751621c8d68e95e43a9a336c35`

Core exploit idea:
- 1. moveLiquidity removes fromIndex from positionIndexes before calling pool.moveQuoteToken. 2. moveQuoteToken can move only part of the requested quote when deposit is t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
