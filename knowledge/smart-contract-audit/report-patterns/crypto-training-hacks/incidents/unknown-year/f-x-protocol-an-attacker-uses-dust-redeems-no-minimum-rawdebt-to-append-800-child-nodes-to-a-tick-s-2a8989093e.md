# Crypto Training Exploit Pattern Stub: f(x) Protocol: An attacker uses dust redeems (no minimum rawDebt) to append 800+ child nodes to a tick's

Source:
- https://crypto.training/hacks/61788-attacker-can-lock-user-funds-through-redeem-function-openzep/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 1970

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61788-attacker-can-lock-user-funds-through-redeem-function-openzep`
- fingerprint: `2a8989093ea13344a18349588e33a8159610faa8a7859762bc0ffad6f2ad9734`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
