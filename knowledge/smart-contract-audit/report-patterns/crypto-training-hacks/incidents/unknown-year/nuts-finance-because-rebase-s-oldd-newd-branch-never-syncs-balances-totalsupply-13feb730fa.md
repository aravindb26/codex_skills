# Crypto Training Exploit Pattern Stub: NUTS Finance: Because rebase()'s oldD>newD branch never syncs balances/totalSupply

Source:
- https://crypto.training/hacks/62662-buffer-drainage-through-repeated-rebase-calls-due-to-stale-s/

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
- id: `62662-buffer-drainage-through-repeated-rebase-calls-due-to-stale-s`
- fingerprint: `13feb730fa5947c78e63258e03a2511c427c47e13a99a31da291accc117c1c1b`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
