# Local Solodit Addendum: Smart Contract Audit Augmentation

## Purpose

Use this companion with `audit-augmentation` when combining scanner findings, SARIF, weAudit notes, Trailmark graphs, and local smart-contract knowledge.

The goal is to turn tool output into prioritized manual review paths without letting scanner noise dominate.

## When To Use

Use this addendum when:

- overlaying Semgrep, CodeQL, Slither, SARIF, or manual annotations on a code graph
- cross-referencing static findings with smart-contract attack surfaces
- trying to group findings by root cause and blast radius

## Companion Workflow

1. Import tool findings and map them to graph nodes.
2. Group findings by root cause, invariant, and reachable entry point.
3. Search Solodit/local knowledge for matching accepted and rejected patterns.
4. Prioritize findings that touch assets, auth, oracle, lifecycle, signature, bridge, token, or upgrade logic.
5. Run manual verification before calling anything a vulnerability.

## False-Positive Filters

Treat augmented findings as leads only. Kill them if:

- they are scanner-only warnings
- there is no attacker-controlled path
- upstream validation protects the sink
- impact is not rewardable
- multiple findings are the same root cause and likely one submission

## Output Requirements

When this addendum is used, include:

- imported finding sources
- grouping by root cause
- graph paths selected
- Solodit/local pattern references
- verification result per group
