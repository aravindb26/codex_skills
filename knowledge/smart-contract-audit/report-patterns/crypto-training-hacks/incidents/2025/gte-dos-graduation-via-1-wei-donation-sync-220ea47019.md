# Crypto Training Exploit Pattern Stub: GTE — DOS graduation via 1-wei donation + sync

Source:
- https://crypto.training/hacks/64857-h-09-dos-of-launchpad-graduation-via-addliquidity-with-1-wei/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `64857-h-09-dos-of-launchpad-graduation-via-addliquidity-with-1-wei`
- fingerprint: `220ea47019a302c076b2bc3dd6acbd034701bdf9d7e398c188531148b34ccb2a`

Core exploit idea:
- 1. Donate 1 wei quote to empty pair and sync(). 2. Reserves become one-sided (0, >0). 3. UniswapV2Library.quote requires both reserves &gt; 0 → reverts. 4. HARM: graduat…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
