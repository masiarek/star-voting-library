"""
test_tracked_paths.py — the committed-surface filter, and its one hard exception
===============================================================================
`tracked_paths.is_tracked()` decides what the drift guards
(`test_tabulated_mirrors_current`, `test_yaml_pages_current`,
`test_readme_index_complete`) are allowed to assert about. It deliberately fails
OPEN: when git cannot answer, everything counts as tracked and the guards behave
as they did before the filter existed.

That default is right for untracked work — a half-finished case in this shared
checkout should not block another session's commit — but it is exactly wrong for
IGNORED paths, and this file pins the difference.

The failure it guards against is not hypothetical. `06_Other/_demo_dropbox/
processed/` holds ~94 ignored `_tabulated.txt` files, several of them stale June
demo artifacts. Fail open and they are all swept back in, so the suite fails on
mirrors nobody committed and nobody can fix — and because a pre-commit hook runs
the suite, that blocks every session in the checkout. It was first blamed on a
held `.git/index.lock`, which is only one of its routes: `_git_tracked_paths()`
reports success when EITHER of its two git commands works, so a transient empty
`ls-files` (a documented behaviour of this shared tree) yields an empty set that
`tracked_set()` cannot tell apart from "no answer" and reports as None. Lock or
no lock, the guard flips open.

Ignore status is answerable without the index, so it is available precisely when
the tracked set is not — and an ignored file is never part of the committed
surface by definition.
"""

import sys
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

import tracked_paths  # noqa: E402

REPO_ROOT = tracked_paths.REPO_ROOT


def _an_ignored_file():
    ignored = tracked_paths.ignored_set()
    if not ignored:
        return None
    for rel in sorted(ignored):
        if rel.endswith("_tabulated.txt"):
            return rel
    return sorted(ignored)[0]


def test_ignored_paths_are_not_tracked():
    """The plain case: git is ignoring it, so it is not the committed surface."""
    rel = _an_ignored_file()
    if rel is None:
        return                      # nothing ignored here; nothing to assert
    assert tracked_paths.is_tracked(rel) is False, rel


def test_ignored_paths_stay_excluded_when_the_tracked_set_is_unavailable(monkeypatch):
    """The regression. Fail-open must not resurrect ignored paths.

    This is the state a transient empty `ls-files` produces, with or without a
    held index.lock — and the state in which the guards used to sweep in ~94
    ignored demo mirrors and fail the whole suite.
    """
    rel = _an_ignored_file()
    if rel is None:
        return
    monkeypatch.setattr(tracked_paths, "tracked_set", lambda: None)
    assert tracked_paths.is_tracked(rel) is False, rel
    # ...while an unknown, non-ignored path still fails OPEN, as designed.
    assert tracked_paths.is_tracked("no/such/file/anywhere.md") is True


def test_a_committed_file_is_still_tracked():
    """Guards against the opposite failure: a filter that excludes everything
    would make every drift check silently vacuous."""
    assert tracked_paths.is_tracked("CLAUDE.md") is True
    assert tracked_paths.is_tracked(REPO_ROOT / "CLAUDE.md") is True


def test_nothing_tracked_is_reported_as_ignored():
    """`--others --ignored` lists untracked-and-ignored files only, so the two
    sets cannot overlap. If they ever do, `is_tracked` would start dropping real
    committed files and the guards would go quiet on genuine drift."""
    ignored = tracked_paths.ignored_set()
    known = tracked_paths.tracked_set()
    if not ignored or not known:
        return
    overlap = sorted(ignored & known)[:5]
    assert not overlap, f"tracked files reported as ignored: {overlap}"
