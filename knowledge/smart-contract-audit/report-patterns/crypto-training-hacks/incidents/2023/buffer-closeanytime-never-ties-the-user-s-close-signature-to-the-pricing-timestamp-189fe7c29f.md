# Crypto Training Exploit Pattern Stub: Buffer `closeAnytime` never ties the user's close signature to the pricing timestamp

Source:
- https://crypto.training/hacks/55637-h-05-closeanytime-timestamp-is-never-validated-against-prici/

Imported:
- 2026-08-19

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
- id: `55637-h-05-closeanytime-timestamp-is-never-validated-against-prici`
- fingerprint: `189fe7c29fcb444b5e544031067f495ca3a2a527b5818d3b49fbef2bb56d32a1`

Core exploit idea:
- Open the source link and distill the reusable exploit mechanism before applying this to a live audit.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
