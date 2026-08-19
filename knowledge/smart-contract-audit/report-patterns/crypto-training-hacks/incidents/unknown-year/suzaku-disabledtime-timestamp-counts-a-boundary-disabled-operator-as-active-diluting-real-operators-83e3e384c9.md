# Crypto Training Exploit Pattern Stub: Suzaku: `disabledTime >= timestamp` counts a boundary-disabled operator as active, diluting real operators

Source:
- https://crypto.training/hacks/61235-timestamp-boundary-condition-causes-reward-dilution-for-ac/

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
- id: `61235-timestamp-boundary-condition-causes-reward-dilution-for-ac`
- fingerprint: `83e3e384c939ea838f7f5e29da32e207bbce48b6746d94eb979797df0837e59f`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
