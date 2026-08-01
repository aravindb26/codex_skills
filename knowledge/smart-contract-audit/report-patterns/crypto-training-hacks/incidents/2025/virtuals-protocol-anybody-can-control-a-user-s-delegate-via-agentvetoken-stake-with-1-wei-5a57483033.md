# Crypto Training Exploit Pattern Stub: Virtuals Protocol — anybody can control a user's delegate via `AgentVeToken.stake()` with 1 wei

Source:
- https://crypto.training/hacks/61823-h-02-anybody-can-control-a-users-delegate-by-calling-agentve/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-caller-check, governance/vote-delegation-hijack, logic/unconditional-state-write

Dedupe:
- id: `61823-h-02-anybody-can-control-a-users-delegate-by-calling-agentve`
- fingerprint: `5a5748303391a05f348d68695622dd1a82b0fb9146f3826f1018754a668fb8aa`

Core exploit idea:
- 1. AgentVeToken.stake(amount, receiver, delegatee) mints amount veToken to receiver, then unconditionally calls _delegate(receiver, delegatee). 2. Only the caller's own…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
