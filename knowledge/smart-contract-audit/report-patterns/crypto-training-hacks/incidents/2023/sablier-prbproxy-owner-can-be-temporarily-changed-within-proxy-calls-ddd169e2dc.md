# Crypto Training Exploit Pattern Stub: Sablier / PRBProxy — Owner can be temporarily changed within proxy calls

Source:
- https://crypto.training/hacks/54672-owner-can-be-temporarily-changed-within-proxy-calls-allowing/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `54672-owner-can-be-temporarily-changed-within-proxy-calls-allowing`
- fingerprint: `ddd169e2dc5e814d4cc0077463f5a16af081940886986ff53b09fd09239bcc78`

Core exploit idea:
- 1. execute DELEGATECALLs a target and only checks that owner is unchanged after return. 2. The target overwrites storage slot 0 (owner) mid-call to a colluding contract.…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
