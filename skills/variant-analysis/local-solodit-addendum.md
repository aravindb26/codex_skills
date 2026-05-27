# Local Solodit Addendum: Variant Analysis Companion

## Purpose
- Use Solodit and local rejected findings to hunt variants after one concrete issue is known.

## When To Use

Use after reading `variant-analysis/SKILL.md` when a candidate or confirmed bug pattern exists.

## Companion Workflow

1. Reduce the original issue to root cause, not symptom.
2. Search current repo for exact code clones, semantic variants, and lifecycle-equivalent paths.
3. Search Solodit stubs for the same root cause to identify common variant shapes and duplicate risk.
4. For each variant, route to the focused skill/addendum and apply its false-positive filters.

## Variant Axes

- Same helper called by another entry point.
- Same state variable updated in another lifecycle path.
- Same off-chain input trust used in another module.
- Same rounding/unit formula used for a different asset.
- Same callback pattern reachable through a different token or bridge.
- Same message/nonce/status logic used across chains.

## False-Positive Filters

Do not group as a variant unless root cause and fix path are materially the same. Do not report a variant unless it independently satisfies scope and impact.
