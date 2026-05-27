# Local Solodit Addendum: X-Ray Companion

## Purpose
- Make pre-audit x-ray reports surface Solodit-informed risk areas without doing full bug validation.

## When To Use

Use after reading `x-ray/SKILL.md` when generating a pre-audit report for a smart-contract protocol.

## Companion Workflow

1. During protocol-type profiling, map modules to available local addenda.
2. In threat model output, list Solodit-informed risk surfaces only as hypotheses.
3. For each high-risk module, suggest the focused skill/addendum to use during the actual audit.
4. Do not call anything a finding from x-ray alone.

## Risk Surface Prompts

- Where do funds enter, exit, and get locked?
- Which state variables are global aggregates?
- Which functions settle queues/batches/messages?
- Which paths use oracle, off-chain, or keeper inputs?
- Which token standards and weird-token behaviors are accepted?
- Which callbacks or external integrations happen before accounting finalization?

## False-Positive Filters

X-ray output is planning context. Findings require later focused validation and PoC/source evidence.
