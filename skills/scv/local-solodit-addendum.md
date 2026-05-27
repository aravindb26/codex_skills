# Local Solodit Addendum: SCV Scan Companion

## Purpose
- Add Solodit-derived pattern memory to the SCV sweep/deep-validation workflow.

## When To Use

Use after reading `scv/SKILL.md` when systematically auditing Solidity code.

## Companion Workflow

1. Load SCV cheatsheet as required by the original skill.
2. During deep validation, load the matching focused local addendum for the vulnerability class.
3. Search Solodit stubs by exact function, primitive, and root cause before escalating.
4. Use Solodit only to sharpen hypotheses and duplicate checks; current repo evidence controls.

## False-Positive Filters

Do not convert a grep hit into a finding unless the focused addendum's exploitability and false-positive filters pass.
