# Crypto Training Exploit Pattern Stub: LoopVaults: inverted `_vestingInterest()` enables an MEV sandwich

Source:
- https://crypto.training/hacks/58543-h-01-incorrect-vesting-interest-calculation-enables-mev-atta/

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
- id: `58543-h-01-incorrect-vesting-interest-calculation-enables-mev-atta`
- fingerprint: `41da5e2833bcfd693991786921bbbfb3bbdbd7b1a17c94d1009a85880e294e77`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
