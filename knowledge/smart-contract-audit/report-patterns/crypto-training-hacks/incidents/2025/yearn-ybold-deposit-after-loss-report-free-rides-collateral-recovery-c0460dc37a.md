# Crypto Training Exploit Pattern Stub: Yearn yBOLD — Deposit after loss report free-rides collateral recovery

Source:
- https://crypto.training/hacks/57687-h-2-attacker-can-deposit-after-the-keeper-reports-a-loss-but/

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
- id: `57687-h-2-attacker-can-deposit-after-the-keeper-reports-a-loss-but`
- fingerprint: `c0460dc37af375534c7333001a8311b7f45355deec344c0b788d9d20213d5bf7`

Core exploit idea:
- 1. Victim deposits into the strategy. 2. Stability Pool liquidation burns BOLD; collateral gains are unrealized. 3. Keeper report() books a loss (PPS drops) because harv…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
