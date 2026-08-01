# Crypto Training Exploit Pattern Stub: Rubicon — First depositor bug on unmodified Compound fork

Source:
- https://crypto.training/hacks/48956-h-17-first-depositor-bug-on-unmodified-compound-fork-code4re/

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
- id: `48956-h-17-first-depositor-bug-on-unmodified-compound-fork-code4re`
- fingerprint: `7f3bbebd10ecb993ef740827720824cd630209b801a4bfc88b6cb8e7a5a43571`

Core exploit idea:
- 1. Fresh CToken has totalSupply == 0 and exchangeRate = 2e26. 2. Attacker mints the minimum (2e8 underlying → 1 share), then donates a large underlying amount to the CTo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
