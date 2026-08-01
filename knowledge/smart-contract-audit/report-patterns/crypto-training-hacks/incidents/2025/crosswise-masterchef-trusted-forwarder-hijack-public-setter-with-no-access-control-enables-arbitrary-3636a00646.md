# Crypto Training Exploit Pattern Stub: Crosswise MasterChef trusted-forwarder hijack — public setter with no access control enables arbitrary `_msgSender()` spoofing

Source:
- https://crypto.training/hacks/2025-05-crosswise/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- BNB Chain

Loss / impact summary:
- ~4.16 WBNB (the public PoC drains this from the CRSS/WBNB pair; the on-chain attack drain…

Tags:
- access-control/missing-auth, access-control/broken-logic, access-control/centralization

Dedupe:
- id: `2025-05-crosswise`
- fingerprint: `3636a00646319395175c17bdbec3480f54af09e1bc374b393c53aa6fcbe50a81`

Core exploit idea:
- Crosswise's MasterChef inherits OpenGSN's BaseRelayRecipient, which overrides _msgSender() so that when the caller is the trustedForwarder, the real sender is read from…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
