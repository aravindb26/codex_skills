# Crypto Training Exploit Pattern Stub: ArkProject NFT Bridge — The bridging process will revert if the collection is matched on the destination chain and not on the source chain

Source:
- https://crypto.training/hacks/38504-the-bridging-process-will-revert-if-the-collection-is-matche/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, dos/permanent, bridge/message-validation

Dedupe:
- id: `38504-the-bridging-process-will-revert-if-the-collection-is-matche`
- fingerprint: `a368d65956db3a3b21bf91e427cfb922a3a1d2fd1bfa8f5b838235f57440bf72`

Core exploit idea:
- 1. L1Bridge.withdrawTokens() calls _verifyRequestAddresses() to confirm the withdrawal request's L1 and L2 collection addresses match the bridge's own recorded pairing b…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
