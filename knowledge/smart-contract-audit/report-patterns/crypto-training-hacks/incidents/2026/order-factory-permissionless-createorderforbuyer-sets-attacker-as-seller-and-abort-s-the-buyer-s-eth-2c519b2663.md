# Crypto Training Exploit Pattern Stub: Order factory — permissionless `createOrderForBuyer` sets attacker as seller and `abort`s the buyer's ETH

Source:
- https://crypto.training/hacks/2026-09-orderfactory/

Imported:
- 2026-10-13

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Sep 2026

Chain:
- Ethereum

Loss / impact summary:
- Incident ~24.7 ETH. This tx: 20.247 ETH from 5 buyers (10.05 + 5.05 + 3.05 + 1.547 + 0.55…

Tags:
- access-control/missing-auth, access-control/missing-signer, logic/missing-check

Dedupe:
- id: `2026-09-orderfactory`
- fingerprint: `2c519b26637771cb559d73199b184609c29dc761e82d345e12537e96fa41a6ad`

Core exploit idea:
- The factory's order-creation entry (selector 0xbde886fc, name unknown — factory unverified) lets any caller create an order "for" a buyer. It checks getState(buyer) == 1…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
