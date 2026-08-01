# Crypto Training Exploit Pattern Stub: DittoETH — Owner of a bad ShortRecord can front-run flagShort calls AND liquidateSecondary

Source:
- https://crypto.training/hacks/27454-owner-of-a-bad-shortrecord-can-front-run-flagshort-calls-and/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/insufficient-guard, logic/liquidation-manipulation, dos/liveness

Dedupe:
- id: `27454-owner-of-a-bad-shortrecord-can-front-run-flagshort-calls-and`
- fingerprint: `b0d59e2ebe14eefec13ff1cda2e6afc9d9c376f1ced984244c01576a9c14b469`

Core exploit idea:
- 1. Every DittoETH short position (a ShortRecord) can be represented as an NFT and transferred. 2. flagShort and liquidateSecondary both require their TARGET ShortRecord…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
