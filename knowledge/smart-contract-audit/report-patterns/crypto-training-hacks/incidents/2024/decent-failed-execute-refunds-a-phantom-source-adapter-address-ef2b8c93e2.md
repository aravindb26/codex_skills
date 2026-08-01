# Crypto Training Exploit Pattern Stub: Decent — Failed `execute` refunds a phantom source-adapter address

Source:
- https://crypto.training/hacks/30561-h-03-when-decentbridgeexecutorexecute-fails-funds-will-be-se/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `30561-h-03-when-decentbridgeexecutorexecute-fails-funds-will-be-se`
- fingerprint: `ef2b8c93e216d0d002202aa8ee7ba97cefdf1b5f8f77ee820cbf4cf9a39ecdc0`

Core exploit idea:
- 1. Source DecentBridgeAdapter calls the router; _getCallParams packs msg.sender (the adapter) as from. 2. Destination onOFTReceived → executor.execute(_from, _to, ...).…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
