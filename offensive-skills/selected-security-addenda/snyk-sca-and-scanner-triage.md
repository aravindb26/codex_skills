# Snyk SCA And Scanner Triage Addendum

Source distilled from `mukul975/Anthropic-Cybersecurity-Skills`:

- `skills/performing-sca-dependency-scanning-with-snyk/SKILL.md`
- `skills/performing-web-application-vulnerability-triage/SKILL.md`

Use this for Web2/source-code AppSec audits after program scope, safe harbor, and scanner rules are known.

## When To Use

- The target has package manifests or lockfiles such as `package-lock.json`, `pnpm-lock.yaml`, `requirements.txt`, `poetry.lock`, `pom.xml`, `go.mod`, `Cargo.lock`, `Gemfile.lock`, or container/IaC files.
- The user asks to combine Snyk with manual source-code auditing.
- Scanner output needs triage into true positive, false positive, duplicate, excluded, or report-worthy.

Do not use this as a smart-contract audit method and do not report known CVEs automatically when the program excludes dependency-only findings.

## Safe Command Pattern

Run from the target repo and save outputs under the audit workspace:

```bash
mkdir -p .context/snyk
snyk test --all-projects --severity-threshold=medium --json-file-output=.context/snyk/open-source.json || true
snyk code test --severity-threshold=medium --json-file-output=.context/snyk/code.json || true
snyk iac test --severity-threshold=medium --json-file-output=.context/snyk/iac.json || true
```

For containers, only scan images the program allows:

```bash
snyk container test <image> --severity-threshold=medium --json-file-output=.context/snyk/container.json || true
```

## Triage Gates

For every scanner lead, answer:

- Is the affected asset in scope?
- Is this finding type rewarded or explicitly excluded?
- Is the vulnerable dependency actually used in the deployed/runtime path?
- Is the vulnerable function reachable by attacker-controlled input?
- Is the installed version confirmed by lockfile, build output, image layer, or runtime evidence?
- Is there a mitigating wrapper, input validator, feature flag, sandbox, or unreachable code path?
- Can impact be demonstrated without unsafe production testing?
- Is the issue already known, patched, accepted risk, or duplicate-root-cause?

If reachability and impact are not proven, treat the scanner result as a lead only.

## False-Positive Patterns

- Package appears in a lockfile but is dev-only and absent from production build.
- Vulnerable API exists in a dependency but no application path calls it with attacker-controlled data.
- Snyk flags a transitive dependency that is bundled but not executed in the target environment.
- IaC issue applies to an example/template, not deployed infrastructure.
- Container package is vulnerable but unavailable to the application due to image stage separation or distroless runtime.
- Program excludes generic dependency CVEs without a working exploit against the product.

## Report-Worthy Upgrade

A dependency or scanner finding becomes stronger when you prove:

- exact product feature reaches the vulnerable sink
- attacker controls the relevant input
- exploit output crosses a real boundary such as auth, tenant, data, command execution, file read/write, or availability
- control vs exploit requests show different behavior
- remediation requires changing product code, config, or dependency, not only "upgrade eventually"

Record exact command output and keep raw JSON locally, but write the final report from validated product impact rather than scanner wording.
