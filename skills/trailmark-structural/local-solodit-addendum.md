# Local Solodit Addendum: Smart Contract Structural Analysis

## Purpose

Use this companion with `trailmark-structural` to prioritize deep manual review in smart contract audits.

The goal is to find security-relevant structure: attack surface, taint, privilege boundaries, blast radius, and complex lifecycle code.

## When To Use

Use this addendum when:

- a repo is large enough that manual ordering matters
- you need hotspot, taint, blast-radius, or privilege-boundary data
- you want to choose files for second-pass review

## Companion Workflow

1. Run structural analysis on the in-scope target.
2. Cross-check generated entry points with the coverage ledger.
3. Prioritize hotspots that touch Solodit-style bug surfaces.
4. Trace privilege boundaries and external-input flows to state updates.
5. Use the output to schedule manual review, not to skip files.

## Smart Contract Priority Signals

Escalate manual review for nodes involving:

- asset accounting or value transfer
- oracle input to enforcement logic
- external callbacks or token behavior
- signature and message validation
- lifecycle finalization, cancellation, settlement, or unwind
- upgrade and initialization boundaries
- cross-chain domain, nonce, and replay protection

## False-Positive Filters

Structural risk is not a finding. Kill it unless manual review shows:

- attacker reachability
- missing validation or broken invariant
- meaningful impact
- non-duplicate root cause

## Output Requirements

When this addendum is used, include:

- top structural hotspots
- why each hotspot matters
- related Solodit/local patterns
- manual review status
- candidate paths that survived or died
