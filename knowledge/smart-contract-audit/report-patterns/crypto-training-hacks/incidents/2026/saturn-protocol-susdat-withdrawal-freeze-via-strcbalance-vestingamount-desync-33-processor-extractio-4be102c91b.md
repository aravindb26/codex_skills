# Crypto Training Exploit Pattern Stub: Saturn Protocol (sUSDat) — Withdrawal Freeze via `strcBalance`/`vestingAmount` Desync + 33% PROCESSOR Extraction

Source:
- https://crypto.training/hacks/2026-04-SaturnProtocol/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Ethereum

Loss / impact summary:
- unknown

Tags:
- arithmetic/underflow, logic/state-update, dos/frozen-funds, logic/fee-calculation

Dedupe:
- id: `2026-04-SaturnProtocol`
- fingerprint: `4be102c91bdea123ad559059bd69df2f6a7377c46488815b8ade356151438411`

Core exploit idea:
- StakedUSDat tracks two pieces of accounting that must stay coupled but are updated by different functions:

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
