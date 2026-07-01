# Pashov Audit Pattern: `TransferFrom` is incorrectly treated as a view function

- Source: Pashov Audit Group
- Imported: 2026-07-01
- Severity: HIGH
- Report: `Hydration-security-review-October` (team)
- Finding ID: `H-01`
- Source finding: <https://github.com/pashov/audits/blob/b60fc16f80b1291d36bd09a443e90f39bcb5d660/team/md/Hydration-security-review-October.md#L71>
- Dedupe key: `team/md/Hydration-security-review-October.md#H-01`
- Fingerprint: `a25cb819460ca98349a6f379d55f160cc76c3515cae78aba107baa6fc767e53b`

## Core Idea

A selector-to-mutability classifier omits TransferFrom, so the fallback labels a state-changing precompile call as View and the execution context can reject or mishandle it.

## Broken Invariant

Every externally callable selector must be classified with the mutability and value rules of its real state transition.

## Where To Look

- Selector or opcode match statements with a permissive default branch
- Precompile dispatch tables and static-call enforcement
- New functions added without updating metadata classifiers

## Attack Path

Invoke the omitted state-changing selector through a context whose behavior depends on the View classification, causing a valid transfer path to fail or violate call-mode assumptions.

## False-Positive Checks

- Confirm the fallback is actually View
- Trace whether the runtime enforces static/view semantics from this classification
- Check whether another layer rejects or reclassifies the selector

## PoC Shape

Compare Transfer and TransferFrom through the same precompile dispatcher and assert that both state-changing calls receive the same modifier and execute successfully.

## Triage Note

Useful beyond this report: whenever functionality and metadata are maintained in parallel tables, test selector-set equality.
