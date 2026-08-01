# Crypto Training Exploit Pattern Stub: DittoETH — disputing a closed Short Record permanently locks its collateral

Source:
- https://crypto.training/hacks/34176-h-06-closing-a-sr-during-a-wrong-redemption-proposal-leads-t/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- loss-of-funds/direct-drain, logic/missing-state-check, accounting/dead-credit

Dedupe:
- id: `34176-h-06-closing-a-sr-during-a-wrong-redemption-proposal-leads-t`
- fingerprint: `e32ac88112c0660cf8aac37cfd2fb8494f3b79f05321ef852ff7f01b377966dd`

Core exploit idea:
- 1. A redemption proposal removes debt (and marks pending) collateral from a Short Record, but does not lock that Short Record against ordinary closure. 2. The shorter ca…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
