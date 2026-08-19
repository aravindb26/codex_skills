# Crypto Training Exploit Pattern Stub: zkSync SSO `ERC1271Handler.isValidSignature` accepts an owner signature with no account/chain binding (replay)

Source:
- https://crypto.training/hacks/56710-potential-signature-replay-attack-in-erc1271handler-openzepp/

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
- signature/replay, account/erc

Dedupe:
- id: `56710-potential-signature-replay-attack-in-erc1271handler-openzepp`
- fingerprint: `b20e547e9786badde03366e12e8170a3dfefad0ead95eaaaa816a340762023f2`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
