# Crypto Training Exploit Pattern Stub: Pro Token: transfer-hook reward-swap self-dealing drains the pair

Source:
- https://crypto.training/hacks/2026-07-protoken/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~605K USDT (~$8.2M cumulative)

Tags:
- unknown

Dedupe:
- id: `2026-07-protoken`
- fingerprint: `7909d9cf0cde8d01d704653b87dcd999b39bec634d4c05207d4816c18f9f2c09`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
