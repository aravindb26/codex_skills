# Crypto Training Exploit Pattern Stub: INIT Capital — wLp tokens could be stolen

Source:
- https://crypto.training/hacks/29590-h-02-wlp-tokens-could-be-stolen-code4rena-init-capital-init/

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
- access-control/insufficient-guard, logic/liquidation-logic, loss-of-funds/direct-drain

Dedupe:
- id: `29590-h-02-wlp-tokens-could-be-stolen-code4rena-init-capital-init`
- fingerprint: `7ff32bfb2d2d5ae586295dd5d634888ff47ed847f78ac0db31cf67848d3d0ec9`

Core exploit idea:
- 1. PosManager.removeCollateralWLpTo(_posId, _wLp, _tokenId, _amt, _receiver) only checks that _posId actually holds _tokenId inside the newWLpAmt == 0 branch — i.e. only…

Audit usage:
- Use this as a searchable lead when the current code has similar tags, value-flow, function behavior, or invariant shape.
- Do not treat this card as duplicate authority. For duplicate checks, compare exact root cause, affected function/path, broken invariant, attacker setup, and impact against original program sources.
- Do not submit a finding because it resembles this exploit. Re-read the current code path and validate the candidate with source evidence and PoC/runtime evidence where feasible.
