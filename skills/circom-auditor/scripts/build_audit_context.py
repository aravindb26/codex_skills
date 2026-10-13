#!/usr/bin/env python3
"""Build scratch context bundles for the circom-auditor skill."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import tempfile
from pathlib import Path
from typing import Iterable


EXCLUDED_DIR_PARTS = {
    "node_modules",
    "tests",
    "__tests__",
    "build",
    "dist",
    "artifacts",
    "out",
}

EXCLUDED_DIR_SUFFIXES = {
    ("circuits", "test"),
    ("dependencies", "circomlib"),
    ("lib", "circomlib"),
}

EXCLUDED_FILE_SUFFIXES = (
    ".test.circom",
    "_test.circom",
    "-test.circom",
    ".witness.json",
    ".r1cs",
    ".zkey",
)

INCLUDE_RE = re.compile(r'^\s*include\s+"([^"]+)"', re.MULTILINE)
DOC_EXTENSIONS = {".md", ".txt", ".rst", ".adoc"}
DOC_BUNDLES = {
    "agent-4-bundle.md",
    "agent-5-bundle.md",
    "agent-12-bundle.md",
    "agent-14-bundle.md",
    "agent-16-bundle.md",
}

AGENT_BUNDLES = {
    "agent-1-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/attack-vectors/signal-field.md",
        "references/hacking-agents/vector-scan-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-2-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/attack-vectors/range.md",
        "references/hacking-agents/vector-scan-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-3-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/attack-vectors/selector-accumulator.md",
        "references/hacking-agents/vector-scan-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-4-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/attack-vectors/binding-1.md",
        "references/hacking-agents/vector-scan-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-5-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/attack-vectors/binding-2.md",
        "references/hacking-agents/vector-scan-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-6-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/attack-vectors/regex-language.md",
        "references/hacking-agents/vector-scan-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-7-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/signal-flow-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-8-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/range-check-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-9-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/arithmetic-field-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-10-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/selector-mux-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-11-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/invariant-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-12-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/intent-binding-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-13-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/first-principles-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-14-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/free-flow-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-15-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/numerical-gap-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-16-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/binding-gap-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
    "agent-17-bundle.md": [
        "references/senior-auditor-sop.md",
        "references/hacking-agents/composition-gap-agent.md",
        "references/hacking-agents/shared-rules.md",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Repository root to audit")
    parser.add_argument("--skill-dir", default=None, help="circom-auditor skill directory")
    parser.add_argument("--out", default=None, help="Output directory for scratch bundles")
    parser.add_argument("--files", nargs="*", default=None, help="Specific .circom files to audit")
    return parser.parse_args()


def resolve_path(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def rel_display(path: Path, repo: Path) -> str:
    try:
        return str(path.relative_to(repo))
    except ValueError:
        return str(path)


def has_excluded_suffix(parts: tuple[str, ...]) -> bool:
    for suffix in EXCLUDED_DIR_SUFFIXES:
        if len(parts) >= len(suffix) and parts[-len(suffix) :] == suffix:
            return True
    return False


def is_excluded(path: Path, repo: Path) -> bool:
    try:
        rel = path.relative_to(repo)
    except ValueError:
        rel = path

    parts = rel.parts
    if any(part in EXCLUDED_DIR_PARTS for part in parts[:-1]):
        return True
    for idx in range(1, len(parts)):
        if has_excluded_suffix(tuple(parts[:idx])):
            return True
    return path.name.endswith(EXCLUDED_FILE_SUFFIXES)


def discover_circom_files(repo: Path, explicit_files: list[str] | None) -> list[Path]:
    if explicit_files:
        files = []
        for item in explicit_files:
            path = resolve_path(repo / item if not Path(item).is_absolute() else item)
            if path.suffix != ".circom":
                raise SystemExit(f"not a .circom file: {item}")
            if not path.exists():
                raise SystemExit(f"missing file: {item}")
            files.append(path)
        return sorted(set(files))

    files = []
    for path in repo.rglob("*.circom"):
        if path.is_file() and not is_excluded(path, repo):
            files.append(path.resolve())
    return sorted(set(files))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def include_candidates(current: Path, include: str, repo: Path) -> list[Path]:
    raw = Path(include)
    if raw.is_absolute():
        return [raw]
    return [
        current.parent / raw,
        repo / raw,
        repo / "node_modules" / raw,
        repo / "dependencies" / raw,
        repo / "dependencies" / "circomlib" / raw,
        repo / "lib" / raw,
        repo / "lib" / "circomlib" / raw,
    ]


def resolve_include(current: Path, include: str, repo: Path) -> Path | None:
    for candidate in include_candidates(current, include, repo):
        resolved = candidate.resolve()
        if resolved.exists():
            return resolved
    return None


def resolve_includes(initial_files: Iterable[Path], repo: Path) -> tuple[list[Path], list[Path], list[str]]:
    in_scope = set(initial_files)
    peripheral: set[Path] = set()
    missing: set[str] = set()
    queue = list(in_scope)

    while queue:
        current = queue.pop(0)
        for include in INCLUDE_RE.findall(read_text(current)):
            resolved = resolve_include(current, include, repo)
            if resolved is None:
                missing.add(f"{rel_display(current, repo)} -> {include}")
                continue

            if is_relative_to(resolved, repo) and resolved.suffix == ".circom" and not is_excluded(resolved, repo):
                if resolved not in in_scope:
                    in_scope.add(resolved)
                    queue.append(resolved)
            else:
                peripheral.add(resolved)

    return sorted(in_scope), sorted(peripheral), sorted(missing)


def write_source(out_dir: Path, repo: Path, in_scope: list[Path], peripheral: list[Path], missing: list[str]) -> Path:
    output = out_dir / "source.md"
    with output.open("w", encoding="utf-8") as handle:
        handle.write("# Source Bundle\n\n")
        for path in in_scope:
            text = read_text(path)
            handle.write(f"### {rel_display(path, repo)}\n\n")
            handle.write("```circom\n")
            handle.write(text)
            if not text.endswith("\n"):
                handle.write("\n")
            handle.write("```\n\n")

        handle.write("# Include Graph\n\n")
        for path in in_scope:
            includes = INCLUDE_RE.findall(read_text(path))
            if includes:
                for include in includes:
                    handle.write(f"- `{rel_display(path, repo)}` includes `{include}`\n")
            else:
                handle.write(f"- `{rel_display(path, repo)}` has no direct includes\n")

        handle.write("\n# Peripheral Files (read on demand)\n\n")
        if peripheral:
            for path in peripheral:
                handle.write(f"- `{rel_display(path, repo)}`\n")
        else:
            handle.write("- None\n")

        if missing:
            handle.write("\n# Missing Includes\n\n")
            for item in missing:
                handle.write(f"- `{item}`\n")

    return output


def write_docs_context(out_dir: Path, repo: Path) -> Path | None:
    docs_dir = repo / "assets" / "docs"
    if not docs_dir.is_dir():
        return None

    paths = sorted(path for path in docs_dir.rglob("*") if path.is_file() and path.suffix.lower() in DOC_EXTENSIONS)
    if not paths:
        return None

    output = out_dir / "docs-context.md"
    with output.open("w", encoding="utf-8") as handle:
        handle.write("# Docs Context\n\n")
        for path in paths:
            text = read_text(path)
            non_empty = [line.strip() for line in text.splitlines() if line.strip()]
            handle.write(f"### {rel_display(path, repo)}\n\n")
            if non_empty and all(line.startswith(("http://", "https://")) for line in non_empty):
                handle.write("URL list detected. Fetch manually only if the user explicitly authorizes network access.\n\n")
                for line in non_empty:
                    handle.write(f"- {line}\n")
                handle.write("\n")
            else:
                handle.write(text)
                if not text.endswith("\n"):
                    handle.write("\n")
                handle.write("\n")

    return output


def write_prior_findings(out_dir: Path, repo: Path) -> Path | None:
    findings_dir = repo / "assets" / "findings"
    if not findings_dir.is_dir():
        return None

    paths = sorted(path for path in findings_dir.rglob("*.md") if path.is_file())
    if not paths:
        return None

    output = out_dir / "prior-findings.md"
    with output.open("w", encoding="utf-8") as handle:
        handle.write("# Prior Findings\n\n")
        for path in paths:
            text = read_text(path)
            handle.write(f"### {rel_display(path, repo)}\n\n")
            handle.write(text)
            if not text.endswith("\n"):
                handle.write("\n")
            handle.write("\n")

    return output


def append_file(handle, path: Path) -> None:
    text = read_text(path)
    handle.write(f"\n\n<!-- BEGIN {path} -->\n\n")
    handle.write(text)
    if not text.endswith("\n"):
        handle.write("\n")
    handle.write(f"\n<!-- END {path} -->\n")


def write_agent_bundles(out_dir: Path, skill_dir: Path, source: Path, docs: Path | None) -> list[Path]:
    bundles = []
    source_text = read_text(source)
    for filename, references in AGENT_BUNDLES.items():
        output = out_dir / filename
        with output.open("w", encoding="utf-8") as handle:
            handle.write(source_text)
            for ref in references:
                append_file(handle, skill_dir / ref)
            if docs and filename in DOC_BUNDLES:
                append_file(handle, docs)
        bundles.append(output)
    return bundles


def line_count(path: Path) -> int:
    return len(read_text(path).splitlines())


def main() -> None:
    args = parse_args()
    repo = resolve_path(args.repo)
    skill_dir = resolve_path(args.skill_dir) if args.skill_dir else Path(__file__).resolve().parents[1]
    if args.out:
        out_dir = resolve_path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)
    else:
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        out_dir = Path(tempfile.mkdtemp(prefix=f"circom-audit-{stamp}-", dir="/tmp"))

    initial = discover_circom_files(repo, args.files)
    if not initial:
        raise SystemExit("no in-scope .circom files found")

    in_scope, peripheral, missing = resolve_includes(initial, repo)
    source = write_source(out_dir, repo, in_scope, peripheral, missing)
    docs = write_docs_context(out_dir, repo)
    prior = write_prior_findings(out_dir, repo)
    bundles = write_agent_bundles(out_dir, skill_dir, source, docs)

    print(f"bundle_dir: {out_dir}")
    print(f"repo: {repo}")
    print(f"in_scope_files: {len(in_scope)}")
    print(f"peripheral_files: {len(peripheral)}")
    print(f"missing_includes: {len(missing)}")
    print(f"source.md: {line_count(source)} lines")
    if docs:
        print(f"docs-context.md: {line_count(docs)} lines")
    if prior:
        print(f"prior-findings.md: {line_count(prior)} lines")
    for bundle in bundles:
        print(f"{bundle.name}: {line_count(bundle)} lines")


if __name__ == "__main__":
    main()
