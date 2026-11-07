# Local Codex Addendum: Audit-Safe Use

Use this workflow only for Vyper targets when stateful fuzzing materially tests an already-understood
invariant or the user asks for a Vyper fuzz harness. It supplements, and never replaces, the first-pass
manual read of every in-scope file, program rules, and manually written invariant list in `AGENTS.md`.

Before generating files or executing anything:

- Resolve the audit workspace and preserve existing test/configuration files; do not overwrite or
  create generated artifacts outside the user-approved audit workspace.
- Inspect project build configuration, runner commands, dependency hooks, and the exact commands the
  helper will execute. Treat repository-controlled scripts/configuration as untrusted input.
- Use only the project's existing local test environment or a clearly isolated local/fork harness.
  Do not target live networks or broadcast transactions.
- Keep campaigns bounded. Start with the smoke profile, inspect actual Vyper source coverage, and
  treat unsupported ABI types, setup gaps, skipped paths, and timeouts as incomplete—not clean.
- Map each implemented property to a manually established invariant and code path. A passing campaign
  is limited evidence for that harness, input model, runtime, and budget; it does not establish audit
  completeness or prove the protocol safe.
- Produce a deterministic regression reproduction for each surviving failure and distinguish a
  protocol invariant break from a faulty model, setup, or assertion.

Do not invoke the helper's `run` command until its explicit argv runner and project effects have been
reviewed. Never accept a report, generated baseline, or coverage percentage as proof without checking
the corresponding source, test wiring, and observed runtime output.
