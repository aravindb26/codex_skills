# Crypto Training Exploit Pattern Stub: Vultisig — whitelist index zero lets every unlisted buyer purchase

Source:
- https://crypto.training/hacks/35754-h-02-vultisig-whitelisting-can-be-bypassed-by-anyone-code4re/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/wrong-condition, access-control/missing-validation, logic/missing-check

Dedupe:
- id: `35754-h-02-vultisig-whitelisting-can-be-bypassed-by-anyone-code4re`
- fingerprint: `eec5d6d271cb9fd632d66fb16aa52f9b0ecf820d1255699f9fe8693adbd99877`

Core exploit idea:
- The whitelist map returns zero for an account that has never been added. The validation only rejects an index above the configured maximum. With a maximum of 10, index z…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
