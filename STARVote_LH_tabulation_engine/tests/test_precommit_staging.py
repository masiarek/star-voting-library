"""
test_precommit_staging.py
=========================
The pre-commit hook regenerates four index/registry surfaces and stages them, so
they always land in the same commit as the sources they describe. It must stage
**only what its own run produced** — never whatever else happens to be dirty in
those directories.

Why that matters here. This checkout is routinely open in two sessions sharing
one index and HEAD, and `git add <folder>` adopts everything dirty inside it. For
a pathspec commit (`git commit -- <paths>`) git builds a TEMPORARY index and
points GIT_INDEX_FILE at it, so anything the hook stages lands in the commit even
though the author explicitly scoped it. On 2026-08-05 that turned a 3-file commit
into 18, and later carried another session's deletions into an unrelated commit.

The two failure directions are opposite and both real, which is why this is
tested rather than eyeballed:

  * stage too much → you commit a colleague's half-finished work;
  * stage too little → the regenerated index does NOT ride along, the committed
    tree is stale, and test_yaml_index_current / test_catalog_current /
    test_divergence_index_current go red on master.

The subtle one is the second. `comm -3` puts lines unique to the second list in
column 2, i.e. prefixed with a TAB, so cutting field 1 before stripping that tab
yields an empty string for every newly created or rewritten file — the hook would
then stage deletions only, silently. That bug was written and caught during
development; this test is what keeps it caught.
"""
import re
import subprocess
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
HOOK = ENGINE_DIR / "tools_adam" / "scripts" / "git-hooks" / "pre-commit"


def _hook_functions() -> str:
    """The two staging helpers, lifted out of the hook so they can be exercised
    without running the whole thing (which needs the real repo and pytest)."""
    src = HOOK.read_text(encoding="utf-8")
    out = []
    for name in ("snapshot_paths", "stage_regenerated"):
        m = re.search(rf"^{name}\(\) \{{.*?^\}}", src, re.M | re.S)
        assert m, f"{name}() not found in {HOOK} — did the hook get restructured?"
        out.append(m.group(0))
    return "\n\n".join(out)


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True).stdout


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    _git(tmp_path, "init", "-q")
    _git(tmp_path, "config", "user.email", "t@example.com")
    _git(tmp_path, "config", "user.name", "t")
    gen = tmp_path / "gen"
    gen.mkdir()
    (gen / "INDEX.md").write_text("idx\n")
    (gen / "stale.md").write_text("stale\n")
    (gen / "foreign.md").write_text("f\n")
    (tmp_path / "mine.txt").write_text("mine\n")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-qm", "base")
    return tmp_path


def _run_staging(repo: Path, generator: str) -> None:
    """snapshot → run `generator` (shell) → stage_regenerated, as the hook does."""
    script = f"""set -u
ROOT="{repo}"
{_hook_functions()}
_snap="$(snapshot_paths "$ROOT/gen")"
{generator}
stage_regenerated "$_snap" "$ROOT/gen"
"""
    subprocess.run(["bash", "-c", script], cwd=repo, check=True,
                   capture_output=True, text=True)


def test_stages_what_it_produced_and_nothing_else(repo: Path):
    """Rewrites, deletions and creations ride along; a foreign edit does not."""
    (repo / "gen" / "foreign.md").write_text("SOMEONE ELSE'S IN-FLIGHT EDIT\n")

    _run_staging(repo, generator="\n".join([
        'printf "idx-v2\\n" > "$ROOT/gen/INDEX.md"',   # rewritten
        'rm "$ROOT/gen/stale.md"',                      # pruned
        'printf "new\\n" > "$ROOT/gen/new.md"',         # created
    ]))

    staged = dict(
        (line.split("\t")[1], line.split("\t")[0])
        for line in _git(repo, "diff", "--cached", "--name-status").splitlines() if line
    )
    assert staged == {
        "gen/INDEX.md": "M",
        "gen/stale.md": "D",
        "gen/new.md": "A",
    }, f"expected exactly this run's output staged, got {staged}"

    assert " M gen/foreign.md" in _git(repo, "status", "--porcelain"), (
        "a concurrent session's edit must be left dirty, not adopted into the commit"
    )


def test_scoped_commit_stays_scoped_but_keeps_the_index_current(repo: Path):
    """The end-to-end shape: `git commit -- mine.txt` must carry mine.txt and the
    regenerated index, and must NOT carry the foreign edit."""
    hook = repo / ".git" / "hooks" / "pre-commit"
    hook.write_text(
        "#!/usr/bin/env bash\nset -u\n"
        f'ROOT="{repo}"\n'
        f"{_hook_functions()}\n"
        '_snap="$(snapshot_paths "$ROOT/gen")"\n'
        'printf "idx-regenerated\\n" > "$ROOT/gen/INDEX.md"\n'
        'stage_regenerated "$_snap" "$ROOT/gen"\n'
        "exit 0\n"
    )
    hook.chmod(0o755)

    (repo / "gen" / "foreign.md").write_text("FOREIGN\n")
    (repo / "mine.txt").write_text("mine-v2\n")
    _git(repo, "commit", "-qm", "scoped", "--", "mine.txt")

    committed = set(_git(repo, "show", "--name-only", "--format=", "HEAD").split())
    assert "mine.txt" in committed
    assert "gen/INDEX.md" in committed, (
        "the regenerated index must ride along or the committed tree goes stale"
    )
    assert "gen/foreign.md" not in committed, (
        "a scoped commit must not sweep in another session's work"
    )


def test_missing_output_path_warns_instead_of_silently_staging_nothing(repo: Path):
    """If a generator's output moves in a reorg, that must be loud — a silent skip
    is how an index drifts stale for six commits before anyone notices."""
    script = f"""set -u
ROOT="{repo}"
{_hook_functions()}
stage_regenerated "" "$ROOT/gen/does_not_exist.md"
"""
    out = subprocess.run(["bash", "-c", script], cwd=repo, check=True,
                         capture_output=True, text=True).stdout
    assert "generated path missing" in out, out
