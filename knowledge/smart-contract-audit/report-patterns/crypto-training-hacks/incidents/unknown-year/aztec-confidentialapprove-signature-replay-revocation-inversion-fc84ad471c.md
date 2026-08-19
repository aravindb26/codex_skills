# Crypto Training Exploit Pattern Stub: AZTEC `confidentialApprove` signature replay / revocation inversion

Source:
- https://crypto.training/hacks/16739-aztec-confidentialapprove-replay-status/

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
- id: `16739-aztec-confidentialapprove-replay-status`
- fingerprint: `fc84ad471c8bdab8a4da7b3f96dba7183024d3a9eb956ce04e6a99949b769c21`

Core exploit idea:
- The AZTEC ZkAssetBase.confidentialApprove lets a note owner sign an EIP-712 NoteSignature authorizing (or revoking) a third party to spend a note. In the vulnerable snap…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
