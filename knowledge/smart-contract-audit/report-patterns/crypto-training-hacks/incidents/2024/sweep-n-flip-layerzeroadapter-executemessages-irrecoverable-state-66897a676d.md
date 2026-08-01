# Crypto Training Exploit Pattern Stub: Sweep n Flip — LayerZeroAdapter.executeMessages irrecoverable state

Source:
- https://crypto.training/hacks/46494-layerzeroadapterexecutemessages-could-lead-to-irrecoverable/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Nov 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- dos/frozen-funds

Dedupe:
- id: `46494-layerzeroadapterexecutemessages-could-lead-to-irrecoverable`
- fingerprint: `66897a676d1570aaef6b6000c2fc82bfbfaeb1b428c40fdaecf8022cd59be0ae`

Core exploit idea:
- 1. Failed LZ deliveries are stored in s_pendingMessagesToExecute. 2. executeMessages runs pending[0] but pop() removes the last element. 3. With [msg1, msg2]: first call…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
