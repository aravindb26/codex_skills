# Crypto Training Exploit Pattern Stub: The Red Village — a public request forwarder is a confused deputy that upgrades a UUPS proxy to attacker code

Source:
- https://crypto.training/hacks/2026-09-theredvillage/

Imported:
- 2026-11-07

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Polygon

Loss / impact summary:
- unknown

Tags:
- access-control/confused-deputy, access-control/missing-authorization, proxy/unauthorized-upgrade

Dedupe:
- id: `2026-09-theredvillage`
- fingerprint: `16383885c8f681c38719171ad90f09378d1185d84dade0e9a761d1e47c34229a`

Core exploit idea:
- The Red Village's Polygon back end routes requests through PolygonTRVRouter.forwardRequest(zone, service, data). The function is public and forwards data verbatim to the…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
