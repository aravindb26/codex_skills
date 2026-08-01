# Crypto Training Exploit Pattern Stub: DODO Cross-Chain DEX — missing `msg.value` check on ETH placeholder drains ZRC20

Source:
- https://crypto.training/hacks/58579-h-2-any-attacker-will-steal-accumulated-zrc20-tokens-from-ga/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- May 2025

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- access-control/missing-auth, bridge/message-spoofing, loss-of-funds/direct-drain

Dedupe:
- id: `58579-h-2-any-attacker-will-steal-accumulated-zrc20-tokens-from-ga`
- fingerprint: `1b0a1e531325acf10a81c9296d96d306dea568a76cbd6604ae18d06717218cd2`

Core exploit idea:
- 1. For non-ETH inputs, the gateway pulls tokens via transferFrom. 2. For zrc20 == _ETH_ADDRESS_, that pull is skipped — but msg.value is never checked. 3. Attacker claim…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
