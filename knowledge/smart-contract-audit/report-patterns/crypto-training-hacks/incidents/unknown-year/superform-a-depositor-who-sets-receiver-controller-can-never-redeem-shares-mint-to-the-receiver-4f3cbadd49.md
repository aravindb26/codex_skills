# Crypto Training Exploit Pattern Stub: Superform: A depositor who sets receiver != controller can never redeem: shares mint to the receiver

Source:
- https://crypto.training/hacks/63077-controller-and-receiver-cannot-redeem-shares-after-depositin/

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
- id: `63077-controller-and-receiver-cannot-redeem-shares-after-depositin`
- fingerprint: `4f3cbadd49bb3e3cfeff58646c3d7535321a365d2a29aed5d29c617da00d12b0`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
