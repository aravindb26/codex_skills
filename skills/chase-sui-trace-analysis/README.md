# Chase Sui Trace Analysis

This is a conditional Codex skill for Sui/Move transaction and post-deployment
analysis. It reads executed transaction traces, applies deterministic invariant
checks, and treats every result as a lead for source review rather than proof
of a vulnerability.

Use it only when the audit involves Sui/Move runtime behavior, a transaction
digest, a deployed package, or post-incident transaction analysis. Do not load
it for ordinary Solidity/EVM source audits.

The full Chase package and MCP server are not installed here. The skill keeps
the upstream workflow, limitations, evidence examples, and a small wrapper as
reference. Install the pinned package separately only when a Sui runtime audit
actually requires live trace analysis.

Important limits:

- keyword and shape detectors have documented false-positive classes;
- public node retention can make old transactions unavailable;
- incomplete scans and skipped digests are not clean results;
- a trace has no source-level authorization or invariant proof;
- all escalated signals require manual Move-source validation and program-scope
  checks before reporting.
