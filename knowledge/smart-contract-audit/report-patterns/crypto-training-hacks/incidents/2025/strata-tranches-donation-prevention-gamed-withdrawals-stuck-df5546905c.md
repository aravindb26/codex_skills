# Crypto Training Exploit Pattern Stub: Strata Tranches — donation-prevention gamed → withdrawals stuck

Source:
- https://crypto.training/hacks/63224-mechanism-to-prevent-donation-attack-can-be-gamed-to-cause-w/

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
- unknown

Dedupe:
- id: `63224-mechanism-to-prevent-donation-attack-can-be-gamed-to-cause-w`
- fingerprint: `df5546905c456a4220bad29300bde6f93ab88cbf6e5bf0a3ea50f6d1f36c862b`

Core exploit idea:
- Donate to Strategy before first deposit → first mint is 1 wei of shares. Later large deposits still leave totalSupply < MIN_SHARES. Every withdraw reverts; capital stuck.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
