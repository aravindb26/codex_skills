# Crypto Training Exploit Pattern Stub: INIT Capital — MoneyMarketHook#_handleRepay can leave user tokens stuck

Source:
- https://crypto.training/hacks/29591-h-03-handlerepay-of-moneymarkethook-does-not-consider-the-a/

Imported:
- 2026-08-01

Status:
- compact index-derived exploit-pattern lead

Incident date:
- Dec 2023

Chain:
- Other

Loss / impact summary:
- unknown

Tags:
- logic/accounting

Dedupe:
- id: `29591-h-03-handlerepay-of-moneymarkethook-does-not-consider-the-a`
- fingerprint: `ce1101fcb81df59c4ce8c265e396cb3be2663926c6493573a1fda50e6d5d6fce`

Core exploit idea:
- 1. MoneyMarketHook._handleRepay converts the caller-supplied _params[i].shares into repayAmt via debtShareToAmtCurrent and transferFroms that full amount from the user i…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
