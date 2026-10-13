# Project Docs

Drop any context that helps the auditor understand what the protocol is supposed to do:

- Design docs and specs
- Intended invariants (what the prover must prove, what the verifier learns)
- Threat model (who's malicious, what they can do off-chain)
- Plain-English descriptions of circuit behavior
- Known limitations or accepted tradeoffs

Files can be plain text or markdown. To reference online docs, create a file containing one URL per line — they will be fetched and read automatically.

At bundle-build time, the orchestrator materializes a `docs-context` file for the `free-flow-agent`:

- Local text/markdown files are appended as-is with path headers.
- Files whose non-empty lines are all `http://` or `https://` URLs are treated as fetch lists; each URL is fetched and appended under a URL header.
- Failed fetches are noted and skipped so the audit can continue.

The `free-flow-agent` (agent #9) reads that bundled docs context to build a mental model of the protocol. A 1-page README with the threat model dramatically improves protocol-level findings.
