# Crypto Training Exploit Pattern Stub: a152 Authorized-Spender Allowance Drain — privileged spender abused to pull any user's approved tokens

Source:
- https://crypto.training/hacks/2026-04-unverified_a152/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Apr 2026

Chain:
- Ethereum

Loss / impact summary:
- 228,980.735023 USDT drained and consolidated to the attacker (PoC figure, output.txt:1565…

Tags:
- access-control/centralization, access-control/missing-auth, logic/missing-validation

Dedupe:
- id: `2026-04-unverified_a152`
- fingerprint: `6823cca24de9c1443c00b0a670f9c9aaa723f579a912e6edccf7f38eb95a44ba`

Core exploit idea:
- The victim was an aggregator/spender deployment built on the well-known "AllowanceTarget + SpenderHelper" pattern (identical addresses to 0x Exchange Proxy infra: Allowa…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
