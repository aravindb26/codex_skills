# Crypto Training Exploit Pattern Stub: KittenSwap: distributing a stale zero-vote period resets a gauge's reward rate to 0

Source:
- https://crypto.training/hacks/61952-h-02-reward-rates-can-be-reset-to-0-and-future-rewards-can-b/

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
- logic/reward-calculation

Dedupe:
- id: `61952-h-02-reward-rates-can-be-reset-to-0-and-future-rewards-can-b`
- fingerprint: `9f10553ddefa9a669c68d73789917d948380df49771cffef6b83adedddb1c227`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
