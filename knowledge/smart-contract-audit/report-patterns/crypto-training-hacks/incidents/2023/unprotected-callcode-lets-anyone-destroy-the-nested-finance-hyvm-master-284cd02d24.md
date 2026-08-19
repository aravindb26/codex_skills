# Crypto Training Exploit Pattern Stub: Unprotected `CALLCODE` lets anyone destroy the Nested Finance HyVM master

Source:
- https://crypto.training/hacks/29663-unprotected-callcode-allows-anyone-to-destroy-the-hyvm-maste/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, access-control/missing-modifier

Dedupe:
- id: `29663-unprotected-callcode-allows-anyone-to-destroy-the-hyvm-maste`
- fingerprint: `284cd02d248e1a93db0dea7d825c215c674ace1e4d05f0138f2c336f0cc5826f`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
