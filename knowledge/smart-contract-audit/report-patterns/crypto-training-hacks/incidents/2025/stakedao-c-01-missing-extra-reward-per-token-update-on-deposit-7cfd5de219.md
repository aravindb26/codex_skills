# Crypto Training Exploit Pattern Stub: StakeDAO — [C-01] Missing extra reward per token update on deposit

Source:
- https://crypto.training/hacks/63598-c-01-missing-update-of-extra-reward-per-token-during-deposit/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `63598-c-01-missing-update-of-extra-reward-per-token-during-deposit`
- fingerprint: `7cfd5de2198ff4af71949036285d34d5d6d85252f91c27b64ff326d44881236d`

Core exploit idea:
- First user deposits and extra rewards are funded. Second user deposits a huge amount without the index updating first, then withdraws/claims — receives ~100k/100001 of r…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
