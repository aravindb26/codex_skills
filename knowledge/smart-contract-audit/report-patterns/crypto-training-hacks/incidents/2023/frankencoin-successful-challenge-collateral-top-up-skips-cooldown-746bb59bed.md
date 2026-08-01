# Crypto Training Exploit Pattern Stub: Frankencoin — Successful challenge + collateral top-up skips cooldown

Source:
- https://crypto.training/hacks/20018-h-03-when-the-challenge-is-successful-the-user-can-send-toke/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `20018-h-03-when-the-challenge-is-successful-the-user-can-send-toke`
- fingerprint: `746bb59bed8eb39973fa63f02b475d3abc1626c0223b6e6f7ab8d064638f2960`

Core exploit idea:
- 1. On a successful challenge, internalWithdrawCollateral only extends cooldown when remaining collateral is below minimumCollateral. 2. The owner MEV-front-runs end() by…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
