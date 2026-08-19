# Crypto Training Exploit Pattern Stub: ManifestFinance: The first depositor into a fresh (totalSupply==0) sUSH vault receives 0 shares for a posit

Source:
- https://crypto.training/hacks/62715-c-01-first-deposit-can-result-in-zero-shares-due-to-direct-t/

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
- id: `62715-c-01-first-deposit-can-result-in-zero-shares-due-to-direct-t`
- fingerprint: `dd2c08b810c8cfb9235eaff2fe5979fb321c077926de881431091f661ecb96b0`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
