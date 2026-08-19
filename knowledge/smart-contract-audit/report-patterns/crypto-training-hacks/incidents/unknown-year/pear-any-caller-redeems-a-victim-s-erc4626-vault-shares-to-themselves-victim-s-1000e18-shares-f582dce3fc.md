# Crypto Training Exploit Pattern Stub: Pear: Any caller redeems a victim's ERC4626 vault shares to themselves — victim's 1000e18 shares

Source:
- https://crypto.training/hacks/65286-c-01-missing-authorization-in-withdraw-and-redeem-allows-the/

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
- id: `65286-c-01-missing-authorization-in-withdraw-and-redeem-allows-the`
- fingerprint: `f582dce3fc60dcfc90722791f323939be94909d812f9c7b2556d5d19cc050f76`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
