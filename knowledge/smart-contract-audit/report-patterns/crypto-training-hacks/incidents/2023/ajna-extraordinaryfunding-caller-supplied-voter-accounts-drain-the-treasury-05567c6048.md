# Crypto Training Exploit Pattern Stub: Ajna ExtraordinaryFunding — caller-supplied voter accounts drain the treasury

Source:
- https://crypto.training/hacks/21301-extraordinary-proposal-steal-ajna/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- governance/proposal-manipulation, access-control/missing-owner-check

Dedupe:
- id: `21301-extraordinary-proposal-steal-ajna`
- fingerprint: `05567c6048613cf15916ddd5fb92231e3e51c31fdc3d5f5b06b7749188c69df3`

Core exploit idea:
- voteExtraordinary(account_, proposalId_) credits the nominated account's voting power rather than msg.sender. A contract can loop over every holder, reach the threshold,…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
