# Crypto Training Exploit Pattern Stub: Movie Token (MT) double-count burn — BSC Mar 2026 ~$242K

Source:
- https://crypto.training/hacks/2026-03-MovieToken/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Mar 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~$242K (~381.7 WBNB)

Tags:
- unknown

Dedupe:
- id: `2026-03-MovieToken`
- fingerprint: `f324d217e014223e2befae8fc214a2c092160ee06d6726bb64aa8f496de33fe5`

Core exploit idea:
- 1. On sells, MT._transfer delivers net tokens to the pair for the swap and adds the same net amount to pendingBurnAmount (PendingBurnRecorded). 2. Anyone can call LP_MIN…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
