# Crypto Training Exploit Pattern Stub: NFTMirror — lzReceive for releaseOnEid results in OOG

Source:
- https://crypto.training/hacks/50038-h-02-lzreceive-call-for-releaseoneid-results-in-oog-error-pa/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- unknown

Dedupe:
- id: `50038-h-02-lzreceive-call-for-releaseoneid-results-in-oog-error-pa`
- fingerprint: `18c05f21fc90242b5c3c092eb06e101855b7b5ee33ab91c3725f0842ac834b21`

Core exploit idea:
- 1. releaseOnEid builds LZ options via getSendOptions(tokenIds). 2. Budget = 80_000 + 20_000 * length — too low for destination mint/transfer (and worse with transfer val…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
