# Crypto Training Exploit Pattern Stub: Subsquid — Gateway creator can steal all tokens from the GatewayRegistry

Source:
- https://crypto.training/hacks/58244-c-01-gateway-creator-can-steal-all-tokens-from-the-gatewayre/

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
- id: `58244-c-01-gateway-creator-can-steal-all-tokens-from-the-gatewayre`
- fingerprint: `2f424cdaaf7c060037bed6e5a2248b48231ec3062af1bf4b0fdfc0470b3a0b43`

Core exploit idea:
- 1. Stake tokens into a gateway; after unlock, unstake them. 2. Unregister the gateway — Gateway struct deleted, stakes[] kept. 3. Re-register the same peerId — totalUnst…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
