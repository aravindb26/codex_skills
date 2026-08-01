# Crypto Training Exploit Pattern Stub: DittoETH — Flag can be overridden by another user

Source:
- https://crypto.training/hacks/27465-flag-can-be-overriden-by-another-user-codehawks-dittoeth-git/

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
- logic/wrong-threshold, loss-of-funds/reward-theft, access-control/shared-resource

Dedupe:
- id: `27465-flag-can-be-overriden-by-another-user-codehawks-dittoeth-git`
- fingerprint: `e7ac8179930a9cc9b24375a36674dc08ee79913a0c4175c7ba1827e87b5a7fe1`

Core exploit idea:
- 1. A flaggerId is a global, reusable slot (flagMapping[id] => address tracks who currently holds it); each ShortRecord just stores WHICH flaggerId number flags it. 2. se…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
