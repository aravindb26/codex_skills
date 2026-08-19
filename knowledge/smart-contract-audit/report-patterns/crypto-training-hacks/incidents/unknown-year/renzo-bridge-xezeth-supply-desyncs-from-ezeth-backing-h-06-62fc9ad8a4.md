# Crypto Training Exploit Pattern Stub: Renzo bridge: xezETH supply desyncs from ezETH backing (H-06)

Source:
- https://crypto.training/hacks/33493-h-06-the-amount-of-xezeth-in-circulation-will-not-represent/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `33493-h-06-the-amount-of-xezeth-in-circulation-will-not-represent`
- fingerprint: `62fc9ad8a4d577566497730c9b91ed6337a1b6e88fc19dbc8ba7d9d416e241d0`

Core exploit idea:
- Source: Code4rena 2024-04-renzo, commit b5b5b76aeafd26c3607d1f0cda6835934d9e7b9e (https://github.com/code-423n4/2024-04-renzo). Vulnerable files: contracts/Bridge/L2/xRe…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
