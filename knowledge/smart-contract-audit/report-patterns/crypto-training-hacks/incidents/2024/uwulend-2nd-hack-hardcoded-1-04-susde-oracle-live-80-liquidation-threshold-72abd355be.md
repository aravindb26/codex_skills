# Crypto Training Exploit Pattern Stub: UwuLend (2nd hack) — Hardcoded `$1.04` sUSDE Oracle + Live 80% Liquidation Threshold

Source:
- https://crypto.training/hacks/2024-06-UwuLend_Second/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jun 2024

Chain:
- Ethereum

Loss / impact summary:
- ~$3.73M — drained across 7 reserves (350.19 WETH + crvUSD + DAI + USDT + FRAX + LUSD + CR…

Tags:
- oracle/wrong-feed, logic/wrong-condition

Dedupe:
- id: `2024-06-UwuLend_Second`
- fingerprint: `72abd355bea3370baadac2804044915469f8d9ea56f6e53b0404de437487d61b`

Core exploit idea:
- This is the second UwuLend exploit, ~13 days after the first one ($19.3M, sUSDE Curve-EMA oracle manipulation). After the first hack, UwuLend tried to "patch" sUSDE pric…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
