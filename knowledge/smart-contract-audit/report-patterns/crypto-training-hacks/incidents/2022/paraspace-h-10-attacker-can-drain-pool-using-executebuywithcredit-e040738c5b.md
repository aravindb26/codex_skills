# Crypto Training Exploit Pattern Stub: ParaSpace — [H-10] Attacker can drain pool using executeBuyWithCredit

Source:
- https://crypto.training/hacks/15983-h-10-attacker-can-drain-pool-using-executebuywithcredit-with/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2022

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `15983-h-10-attacker-can-drain-pool-using-executebuywithcredit-with`
- fingerprint: `e040738c5b62e2792fbe5222114f3fd35cd1218b88cc8b37a4e34e1b1db2cca8`

Core exploit idea:
- 1. Pool charges the user from OrderInfo consideration built with maker price. 2. LooksRare exchange transfers taker price from the pool to the maker. 3. Attacker is both…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
