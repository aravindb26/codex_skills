# Crypto Training Exploit Pattern Stub: Canto (veRWA) — undelegating back to yourself can force a 5-year lock extension

Source:
- https://crypto.training/hacks/26974-h-06-users-may-be-forced-into-long-lock-times-to-be-able-to/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-comparison-operand, governance/forced-lock-extension, access-control/missing-caller-check

Dedupe:
- id: `26974-h-06-users-may-be-forced-into-long-lock-times-to-be-able-to`
- fingerprint: `0e6dd8e3dffd1c48a87c59ae6db716500a322959ba9856c47c32b9d2c4e847f6`

Core exploit idea:
- 1. Bob locks CANTO for the (fixed) 5-year duration and, by default, self-delegates. 2. Bob delegates his voting power to Dave, whose lock happens to unlock later than Bo…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
