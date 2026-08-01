# Crypto Training Exploit Pattern Stub: Rubicon — DOS of market operations with malicious offers

Source:
- https://crypto.training/hacks/48951-h-12-dos-of-market-operations-with-malicious-offers-code4ren/

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
- id: `48951-h-12-dos-of-market-operations-with-malicious-offers-code4ren`
- fingerprint: `c14e2e56a34970eaeb5179df8d155e85279f2f4fc57f8a86be8cd3050a91d4ad`

Core exploit idea:
- offer() accepts owner/recipient=0; OZ ERC20 reverts on transfer to zero, DoSing market fills.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
