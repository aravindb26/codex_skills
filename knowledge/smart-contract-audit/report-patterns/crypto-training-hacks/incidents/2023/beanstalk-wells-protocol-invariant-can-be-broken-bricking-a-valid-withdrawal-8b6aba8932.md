# Crypto Training Exploit Pattern Stub: Beanstalk Wells — protocol invariant can be broken, bricking a valid withdrawal

Source:
- https://crypto.training/hacks/18431-protocols-invariants-can-be-broken-cyfrin-beanstalk-wells-ma/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- math/invariant-violation, logic/wrong-condition

Dedupe:
- id: `18431-protocols-invariants-can-be-broken-cyfrin-beanstalk-wells-ma`
- fingerprint: `8b6aba8932980fb50818343b23749e53d0aae9f3295cbf509841a9bae2bc6bc4`

Core exploit idea:
- 1. Well.removeLiquidity pays out proportionally: lpAmountIn * reserves[i] / lpTokenSupply. That is correct only if the Well function is linear — but ConstantProduct2 (b_…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
