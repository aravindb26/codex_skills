# Crypto Training Exploit Pattern Stub: The Sandbox SAND OFT — `approveAndCall` hijacks LayerZero delegate and mints unbacked SAND

Source:
- https://crypto.training/hacks/2026-08-sandboxoft/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Aug 2026

Chain:
- Base

Loss / impact summary:
- This tx mints 10,000,000 unbacked SAND. Campaign: ~$49B face value across 400+ txs; ~$670…

Tags:
- access-control/missing-auth, bridge/message-spoofing, input-validation/missing

Dedupe:
- id: `2026-08-sandboxoft`
- fingerprint: `2fefc6fb7061c210e49bef694e4ab16117327e0b4bc68b0965341dfd15208111`

Core exploit idea:
- OFTSand.approveAndCall(target, amount, data) does target.call{value: msg.value}(data) with msg.sender == the token. Its only guard is doFirstParamEqualsAddress(data, _ms…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
