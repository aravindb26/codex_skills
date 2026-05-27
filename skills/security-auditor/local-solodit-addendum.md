# Local Solodit Addendum: Security Auditor Companion

## Purpose
- Add local Solodit memory to the Map-Hunt-Attack workflow.
- Do not replace `SKILL.md`.

## When To Use

Use after reading `security-auditor/SKILL.md` during Solidity Map-Hunt-Attack audits.

## Companion Workflow

1. MAP: include Solodit pattern search terms only after scope and entry-point mapping.
2. HUNT: when a surface maps to a focused skill, read that skill's local addendum.
3. ATTACK: before confirming, search Solodit stubs for root-cause duplicates and accepted variants.
4. Record killed branches with false-positive reason when Solodit pattern does not fit current code.

## Extra Checks

- If Slither/Aderyn flags a class with a local addendum, refresh that addendum before accepting/rejecting.
- If Solodit has many similar reports, identify what makes this candidate unique in root cause or impact.

## False-Positive Filters

No finding is confirmed until current code, scope, duplicate risk, and exploit path all survive falsification.
