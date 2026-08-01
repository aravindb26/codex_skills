# Crypto Training Exploit Pattern Stub: Securitize DSToken — unapproved `transferFrom` theft

Source:
- https://crypto.training/hacks/64373-investors-can-steal-tokens-from-other-investors-since-standa/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Oct 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/missing-check, access-control/broken-logic

Dedupe:
- id: `64373-investors-can-steal-tokens-from-other-investors-since-standa`
- fingerprint: `5690fd6ea4e01181e6f7fabd4a0491bc450a22decc293e4fd3eddae3ec0aa3b8`

Core exploit idea:
- StandardToken.transferFrom calls its transfer primitive directly and never checks the owner's allowance for msg.sender. An arbitrary investor can therefore debit any oth…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
