# Crypto Training Exploit Pattern Stub: Zaros — wrong parameter passed in TradingAccount::deductAccountMargin

Source:
- https://crypto.training/hacks/37995-wrong-parameter-passed-in-tradingaccountdeductaccountmargin/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Jul 2024

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/liquidation-logic, loss-of-funds/direct-drain, logic/wrong-argument

Dedupe:
- id: `37995-wrong-parameter-passed-in-tradingaccountdeductaccountmargin`
- fingerprint: `2b87b64a1141f1f2f1c5605d8bf8d681a67a1b98465f09e2bffb87514febd316`

Core exploit idea:
- 1. On liquidation, deductAccountMargin should realize the account's ACTUAL unrealized loss plus the liquidation fee out of its margin balance, transferring that amount t…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
