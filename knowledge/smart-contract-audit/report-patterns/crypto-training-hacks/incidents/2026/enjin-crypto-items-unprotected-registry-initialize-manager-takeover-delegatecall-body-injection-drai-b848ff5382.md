# Crypto Training Exploit Pattern Stub: Enjin "Crypto Items" — unprotected registry `initialize()` → manager takeover → delegatecall-body injection drains the ERC-1155 item reserve

Source:
- https://crypto.training/hacks/2026-08-enjincryptoitems/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Ethereum

Loss / impact summary:
- 5,231,353 ENJ (≈ $142K at incident-time price), melted out of the item reserve in a singl…

Tags:
- access-control/missing-auth, access-control/uninitialized-proxy, access-control/admin-takeover, logic/arbitrary-external-call

Dedupe:
- id: `2026-08-enjincryptoitems`
- fingerprint: `b848ff5382211caba7a47d235ce8ff3c3d7192ffb6ceb70de93e8116ca4afa96`

Core exploit idea:
- 1. Every Enjin "Crypto Items" item is fronted by a logicless per-item ERC-1155 adapter clone. The clone has no logic of its own: for any selector it looks up delegates(s…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
