# Crypto Training Exploit Pattern Stub: BeatXswap LiquidityVestingConvert — UniV3 `slot0` spot oracle

Source:
- https://crypto.training/hacks/2026-09-beatxswapvestingoracle/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- BNB Chain

Loss / impact summary:
- ~2.98M–3.07M BTX (~$63.7k–$77.5k). Live attacker net 63,704.84 USDT. Teaching PoC drains…

Tags:
- oracle/spot-price, oracle/single-source, oracle/price-manipulation, logic/price-calculation

Dedupe:
- id: `2026-09-beatxswapvestingoracle`
- fingerprint: `93d166a284807f351e713f04cfb8bee804de926562fcda43ea2aa5df41bf2dbe`

Core exploit idea:
- BeatSwap's LV Convert lets users deposit USDT. 75% goes to a treasury; 25% is paired with protocol-owned BTX and minted as a Pancake V3 LP. The BTX amount is sized by _c…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
