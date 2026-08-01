# Crypto Training Exploit Pattern Stub: Yearn yBOLD — Steal 25% of first depositor funds via share inflation

Source:
- https://crypto.training/hacks/57686-h-1-a-malicious-attacker-can-steal-25-of-the-funds-of-the-fi/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `57686-h-1-a-malicious-attacker-can-steal-25-of-the-funds-of-the-fi`
- fingerprint: `2eb88034a01b4cf5373d29b5a883ae67d127132c64432b7986cad8a39bea6703`

Core exploit idea:
- 1. Fresh strategy has totalSupply = 0 and no burned dead shares. 2. Attacker deposits 1 wei → 1 share, then donates until totalAssets = 1 + victimDeposit/2. 3. Victim de…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
