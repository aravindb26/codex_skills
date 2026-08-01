# Crypto Training Exploit Pattern Stub: Autonomint — `ABONDToken::transferFrom` corrupts `userStates` and enables Treasury ETH theft

Source:
- https://crypto.training/hacks/45462-h-9-abondtokentransferfrom-does-not-work-as-intended-and-all/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- accounting/state-key, token/erc, logic/direct-drain

Dedupe:
- id: `45462-h-9-abondtokentransferfrom-does-not-work-as-intended-and-all`
- fingerprint: `9ebdeab3ee7abef6bfb7e5e61e358a21356a8828dbad0c06593c588b9d2f7864`

Core exploit idea:
- 1. transferFrom debits the from State, then writes it to msg.sender. 2. The true from keeps their full ethBacked State; the spender inherits a quasi-copy of the rich Sta…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
