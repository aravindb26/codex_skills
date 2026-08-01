# Crypto Training Exploit Pattern Stub: THORWallet — Bridge path bypasses TITN transfer lock — send to any address

Source:
- https://crypto.training/hacks/55397-h-2-the-user-can-send-tokens-to-any-address-by-using-two-bri/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Feb 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `55397-h-2-the-user-can-send-tokens-to-any-address-by-using-two-bri`
- fingerprint: `6dfd13c652d20643f971051d6530f08daccccfaa1d2179ed1a371a2e2175cc5e`

Core exploit idea:
- Bridge path bypasses TITN transfer lock — send to any address. Harm demonstrated: Transfer-lock invariant broken: bridge credits tokens to arbitrary recipient.

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
