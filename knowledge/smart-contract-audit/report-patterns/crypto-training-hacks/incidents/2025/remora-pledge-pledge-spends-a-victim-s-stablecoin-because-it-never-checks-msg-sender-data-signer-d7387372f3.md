# Crypto Training Exploit Pattern Stub: Remora Pledge: `pledge` spends a victim's stablecoin because it never checks `msg.sender == data.signer`

Source:
- https://crypto.training/hacks/61175-attacker-can-make-pledge-on-behalf-of-users-if-those-users/

Imported:
- 2026-08-19

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `61175-attacker-can-make-pledge-on-behalf-of-users-if-those-users`
- fingerprint: `d7387372f3e759209be3e7fc3b32341a75a94be7f2ca2b89bb7b20bee93e7857`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
