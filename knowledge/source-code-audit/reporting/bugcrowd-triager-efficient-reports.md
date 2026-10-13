# Bugcrowd Reports: Triager-Efficient Evidence

## Source and authority

Distilled from Bugcrowd LevelUp, [How to write excellent reports, techniques that save Triager's time, and mistakes that should be avoided in reports](https://www.bugcrowd.com/resources/levelup/how-to-write-excellent-reports-techniques-that-save-triagers-time-and-mistakes-that-should-be-avoided-in-reports/).

This is general reporting guidance, not a substitute for a program's required fields, scope, character limit, or triager-specific instructions. Follow the target program first. Newer, explicit triager instructions take precedence over this note.

## Report construction

- **Title:** State the affected component or input, the vulnerability mechanism, and the demonstrated consequence. Avoid a bare category label such as "DoS" or "signature bug."
- **Description:** Explain the attacker-controlled action, the vulnerable transition, and the observable result in a few factual sentences. Keep investigation history and unsupported hypotheses out of the report.
- **Impact:** Write the concrete "As an attacker, I can..." consequence for the affected key, user, data, service, or security guarantee. Severity is context-dependent; do not paste generic impact language or claim more than the evidence proves.
- **Scope context:** If target ownership or applicability is not obvious, provide concise evidence tying the affected asset/build to the program.
- **One root cause, one report:** Consolidate instances of the same root cause across endpoints or assets. Do not split variants that share the same broken invariant and impact path; do not call different symptoms duplicates without comparing exact root causes.

## Reproduction that minimizes triager effort

Give both a short validation path and a complete clean-start path when setup is nontrivial:

1. State the exact target, supported version/revision, environment, roles, privileges, and prerequisites.
2. Explain how to obtain every required identifier and where each role acts. Do not leave unexplained placeholders in commands or requests.
3. Number actions in execution order and separate attacker and victim/co-signer roles where applicable.
4. Provide full URLs for web targets and raw HTTP requests/responses in fenced Markdown blocks. For source-library findings, provide the exact checkout, patch application, build, focused test, and control commands.
5. Include the exact observed output and the expected result. When persistence is claimed, test a fresh transaction/request and recovery path. Include a normal control where feasible.
6. Distinguish production behavior from test-fixture setup, mocks, interposers, and harness-only state. State exactly what was modified; do not imply live-service testing when only local library methods ran.
7. Make the report reproducible from its text. Treat attachments, screenshots, and video as supplemental evidence, not as the sole source of payloads, commands, or essential steps. Preserve concise logs or screenshots when they show a result that might disappear before triage.
8. Keep evidence ethical and minimal: demonstrate the claimed impact, then stop; do not collect unrelated data or expand access just to make the report look stronger.

## Source-library bounty adaptation

For a native/C/C++ library report, a triager-ready walkthrough normally identifies the pinned commit and build prerequisites, shows the attacker-controlled input being passed through the production receiver/API, records the victim-side state or result, and runs an unaffected control. A test-only patch may be necessary to assemble protocol parties, but it must not patch production behavior or manufacture the vulnerable condition without an attacker-reachable trigger. Label harness-only observations honestly.

When a triager asks for more evidence, answer the exact gap in the existing report thread unless the program directs otherwise. Put the complete numbered walkthrough and copy/paste commands in the response; do not make the reviewer infer steps from a patch, video, source references, or prior investigation notes.

## Fireblocks-specific report checklist

- Use the program's Description field and stay within its stated character limit.
- Lead with the attacker action and concrete honest-party impact.
- Give clean-checkout commands for the exact scoped revision; include patch name, build target, focused test selector, and normal-control selector.
- Include actual captured output inline, with error names/codes explained.
- Separate attacker-controlled setup from test-only fixture access, and identify which victim-side calls are production methods.
- For persistence claims, show fresh IDs/requests and whether a supported recovery path works.
- Do not repeat the prior Fireblocks rejection pattern: source-level claims, local forced conditions, or passing assertions alone do not prove that an attacker can trigger customer impact.
