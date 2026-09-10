# Crypto Training Exploit Pattern Stub: The Sandbox SAND OFT (Base) — LayerZero Delegate Hijack via `approveAndCall`

Source:
- https://crypto.training/hacks/2026-08-unknownhack/

Imported:
- 2026-09-10

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Base

Loss / impact summary:
- 10,000,000 SAND minted unbacked in this tx (10000000000000000000000000 wei, output.txt:9)…

Tags:
- access-control/missing-auth, dependency/unsafe-external-call, bridge/message-spoofing, logic/missing-validation

Dedupe:
- id: `2026-08-unknownhack`
- fingerprint: `6b2c94825f5bad38e62ad7e5584bcd32ffc94c4f6eaa32fff1b31b6f4ec5ea7f`

Core exploit idea:
- The Sandbox's SAND OFT on Base inherited an old Sand token helper, approveAndCall(target, amount, data). It approves target and then does target.call{value: msg.value}(d…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
