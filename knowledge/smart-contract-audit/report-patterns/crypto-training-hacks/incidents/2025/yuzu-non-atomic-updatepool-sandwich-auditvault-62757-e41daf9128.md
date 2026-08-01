# Crypto Training Exploit Pattern Stub: Yuzu non-atomic updatePool sandwich — AuditVault 62757

Source:
- https://crypto.training/hacks/62757-yuzu-nonatomic-updatepool/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- defi/sandwich-attack, oracle/spot-price

Dedupe:
- id: `62757-yuzu-nonatomic-updatepool`
- fingerprint: `e41daf91288bfc85af9e87a9c5b525bdffa484e99918a28c5e6ea413ae3e90bf`

Core exploit idea:
- A donation can be inserted before updatePool, changing the spot-derived pool value in the same transaction sequence.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
