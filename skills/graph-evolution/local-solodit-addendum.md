# Local Solodit Addendum: Smart Contract Graph Evolution

## Purpose

Use this companion with `graph-evolution` when comparing smart contract snapshots, audit commits, contest revisions, forks, or upgrades.

The goal is to catch newly introduced attack paths that text diffs can hide.

## When To Use

Use this addendum when:

- comparing pre-audit and post-audit versions
- reviewing protocol upgrades
- checking forked code against upstream
- validating whether a known public bug pattern was introduced or fixed

## Companion Workflow

1. Compare structural changes only after identifying in-scope refs.
2. Highlight new or changed paths from external entry points to state writes, value movement, or privilege checks.
3. Compare changed paths against Solodit/local accepted and rejected patterns.
4. Check whether a public fix was partially copied but missed an adjacent invariant.
5. Manually verify every candidate path before reporting.

## False-Positive Filters

Do not escalate if:

- the new graph path is unreachable in production
- unchanged validation still protects the sink
- the diff only changes architecture without security behavior
- the exploit requires a pre-migration state that cannot exist
- the issue is already fixed or known in the target version

## Output Requirements

When this addendum is used, include:

- compared refs
- new or removed attack paths
- affected invariants
- related public/local pattern
- manual verification result
