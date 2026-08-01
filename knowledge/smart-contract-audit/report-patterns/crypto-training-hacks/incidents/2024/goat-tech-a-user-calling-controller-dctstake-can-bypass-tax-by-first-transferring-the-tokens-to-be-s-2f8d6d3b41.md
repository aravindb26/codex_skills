# Crypto Training Exploit Pattern Stub: Goat Tech — A user calling Controller::dctStake can bypass tax by first transferring the tokens to be staked

Source:
- https://crypto.training/hacks/40665-a-user-calling-controllerdctstake-can-bypass-tax-by-first-tr/

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
- logic/missing-check, accounting/tax-bypass, economic/incentive-misalignment

Dedupe:
- id: `40665-a-user-calling-controllerdctstake-can-bypass-tax-by-first-tr`
- fingerprint: `2f8d6d3b41b6ddd4618f53aa491f8c96f92ac9173b38107f7e4190d56722f698`

Core exploit idea:
- 1. When a user stakes DCT via Controller.dctStake(amount_, receiver_, lockDuration_), a 1% tax is calculated from amount_ and burned to address(0xdead). 2. But the amoun…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
