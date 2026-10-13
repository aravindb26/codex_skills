# Eval Runner

Run the circom-auditor skill against a **sanitized copy** of each benchmark's zkbugs minimal-reproducer subdir (circuit sources only — the dataset's `README.md` / `zkbugs_config.json` / `zkbugs_*.sh` answer-key files are stripped) and compare results to ground truth. The auditor must never see those files: they name the bug class, root cause, fix, and a `Reproduced` flag, which would contaminate the audit. `Reproduced: false` is a dataset tooling status (no reproduction harness shipped), **not** a security signal.

## Usage

These examples assume you invoke `claude` from the repo root.

```
claude "read skills/circom-auditor/evals/runner.md and run all benchmarks"
claude "read skills/circom-auditor/evals/runner.md and run wormprivacy-spend"
```

## Setup

Resolve paths, create the plugin symlink, get the commit hash, and generate a timestamp.

`SKILL_DIR` is the `skills/circom-auditor/` directory (parent of `evals/`). `REPO_ROOT` is the git repo root. Both must be absolute paths.

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
SKILL_DIR="$REPO_ROOT/skills/circom-auditor"
mkdir -p /tmp/audit-plugin/skills && ln -sfn "$SKILL_DIR" /tmp/audit-plugin/skills/circom-auditor
COMMIT=$(git -C "$REPO_ROOT" rev-parse --short=7 HEAD)
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
echo "commit=$COMMIT timestamp=$TIMESTAMP"
```

## Run

Each `.md` file in `evals/benchmarks/` is a benchmark with frontmatter: `repo_url`, `repo_ref` (optional), `contracts_dir` (the path under the cloned repo to a single zkbugs minimal-reproducer subdir).

For each benchmark, clone the repo (shallow, skip if `/tmp/eval-{name}` exists), build a sanitized source tree at `/tmp/eval-clean-{name}` (see **Sanitize** below), and create `{run_dir}` at `evals/results/{name}/{timestamp}-{commit}`.

Run benchmarks **sequentially** in this fixed order: **wormprivacy-spend → selfxyz-packbytes → circomlib-decoder**. Each run gets a fresh `claude` process so context does not carry over between benchmarks.

**Sanitize (anti-contamination).** The auditor runs in `/tmp/eval-clean-{name}`, which contains only the slice's `.circom` files plus circomlib as read-on-demand peripheral context under `node_modules/circomlib/` (kept out of the in-scope scan by the skill's `node_modules/` exclude rule). The zkbugs `README.md`, `zkbugs_config.json`, `zkbugs_*.sh`, and `*_input.json` files are never copied — running the auditor in the raw slice leaks the entire answer key. A benchmark whose vulnerable template lives in a missing app-level `include` (not inlined and not circomlib) is **not self-contained**: the auditor cannot see the bug without hunting outside the tree, so it cannot be scored honestly — fix the benchmark, do not re-expose the metadata.

The `--plugin-dir /tmp/audit-plugin` flag is **required** — it makes the skill discoverable via the symlink created in Setup. Without it, `claude` will report "Unknown skill: circom-auditor".

```bash
BENCHMARKS_DIR="$SKILL_DIR/evals/benchmarks"
RESULTS_DIR="$SKILL_DIR/evals/results"

for name in wormprivacy-spend selfxyz-packbytes circomlib-decoder; do
  BENCH="$BENCHMARKS_DIR/$name.md"
  [ -f "$BENCH" ] || continue

  # Read repo_url and contracts_dir from frontmatter
  REPO_URL=$(grep '^repo_url:' "$BENCH" | sed 's/repo_url: *//')
  CONTRACTS_DIR=$(grep '^contracts_dir:' "$BENCH" | sed 's/contracts_dir: *//' || true)
  CLONE_DIR="/tmp/eval-$name"
  WORK_DIR="$CLONE_DIR${CONTRACTS_DIR:+/$CONTRACTS_DIR}"
  CLEAN_DIR="/tmp/eval-clean-$name"
  CIRCOMLIB="$CLONE_DIR/dataset/circom/dependencies/circomlib"
  RUN_DIR="$RESULTS_DIR/$name/$TIMESTAMP-$COMMIT"

  # Clone (shallow) once; reuse on subsequent runs
  [ -d "$CLONE_DIR" ] || git clone --depth 1 "$REPO_URL" "$CLONE_DIR"

  # Sanitize: copy ONLY the .circom sources into a clean tree — never the zkbugs
  # answer-key files (README.md, zkbugs_config.json, zkbugs_*.sh, *_input.json).
  # Provide circomlib under node_modules/ as read-on-demand peripheral context
  # (the skill's node_modules/ rule keeps it out of the in-scope scan, and find's
  # default no-symlink-follow keeps it out of the find sweep).
  [ -d "$CLEAN_DIR" ] && rm -r "$CLEAN_DIR"   # fresh tree each run (no stale assets/findings)
  rsync -a -m --include='*/' --include='*.circom' --exclude='*' "$WORK_DIR/" "$CLEAN_DIR/"
  mkdir -p "$CLEAN_DIR/node_modules"
  [ -d "$CIRCOMLIB" ] && ln -sfn "$CIRCOMLIB" "$CLEAN_DIR/node_modules/circomlib"

  echo "=== Starting $name ==="
  mkdir -p "$RUN_DIR" && \
  cd "$CLEAN_DIR" && mkdir -p assets/audit-logs && \
  claude --print --plugin-dir /tmp/audit-plugin --dangerously-skip-permissions \
    "run circom auditor with --file-output" 2>&1 | tee "$RUN_DIR/full-output.txt" && \
  cp -r "$(ls -dt assets/findings/*-zksec-circom-audit-report-*.md | head -1)" "$RUN_DIR/final-report.md" 2>/dev/null; \
  cp "$BENCH" "$RUN_DIR/ground-truth.md"
  echo "=== Finished $name ==="
done
echo "All benchmarks complete."
```

After all complete, for each `{run_dir}`: read `skills/circom-auditor/evals/compare.md`, compare `{run_dir}/ground-truth.md` against `{run_dir}/final-report.md`, write `summary.md` to `{run_dir}/`. Print each summary and `=== All done. {count} benchmarks. ===`
