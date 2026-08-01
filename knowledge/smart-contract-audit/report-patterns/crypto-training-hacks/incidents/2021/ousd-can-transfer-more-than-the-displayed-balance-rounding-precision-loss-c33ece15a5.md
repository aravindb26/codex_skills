# Crypto Training Exploit Pattern Stub: OUSD can transfer more than the displayed balance — rounding/precision loss

Source:
- https://crypto.training/hacks/18213-ousd-allows-users-to-transfer-more-tokens-than-expected-trai/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jan 2021

Chain:
- Ethereum

Loss / impact summary:
- A holder can transfer one token more than balanceOf reports

Tags:
- arithmetic/rounding, arithmetic/precision-loss, logic/missing-check

Dedupe:
- id: `18213-ousd-allows-users-to-transfer-more-tokens-than-expected-trai`
- fingerprint: `c33ece15a5e6b4a21ab30e93b924b554f412c2adc666d104d68f3b4fa09b6fea`

Core exploit idea:
- Rebasing credits can make the token-facing balance larger than the credit deduction for a transfer. Flooring creditsDeducted before validating the token amount lets a th…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
