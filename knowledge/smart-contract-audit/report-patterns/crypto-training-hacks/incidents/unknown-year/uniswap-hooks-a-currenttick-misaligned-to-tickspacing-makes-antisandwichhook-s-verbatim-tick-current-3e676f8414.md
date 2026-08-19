# Crypto Training Exploit Pattern Stub: Uniswap Hooks: A currentTick misaligned to tickSpacing makes AntiSandwichHook's verbatim `tick != current

Source:
- https://crypto.training/hacks/62524-infinite-loop-in-tick-iteration-due-to-misaligned-current-ti/

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
- id: `62524-infinite-loop-in-tick-iteration-due-to-misaligned-current-ti`
- fingerprint: `3e676f8414e474d01c60960b2a7870a9efe466435a18fc94e746ea6fc274df60`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
