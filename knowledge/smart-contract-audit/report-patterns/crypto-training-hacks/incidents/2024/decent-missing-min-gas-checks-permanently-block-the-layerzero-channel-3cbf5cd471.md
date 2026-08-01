# Crypto Training Exploit Pattern Stub: Decent — Missing min-gas checks permanently block the LayerZero channel

Source:
- https://crypto.training/hacks/30560-h-02-due-to-missing-checks-on-minimum-gas-passed-through-lay/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/unbounded-loop

Dedupe:
- id: `30560-h-02-due-to-missing-checks-on-minimum-gas-passed-through-lay`
- fingerprint: `3cbf5cd47119ccb1150311ca0beb846d9d03e11f7653df9bfe0130e65c125677`

Core exploit idea:
- 1. Adapter gas is 100_000 + _dstGasForCall with no floor on the user parameter. 2. A malicious or mistaken user can pass ~1000 → destination OOGs / fails. 3. LayerZero t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
