"""
tracked_paths.py — is this file part of the COMMITTED surface?
==============================================================
Shared helper for the drift guards (`test_yaml_pages_current`,
`test_readme_index_complete`, `test_tabulated_mirrors_current`).

WHY THIS EXISTS. Those guards protect what the repo has committed: a page that
drifted from its YAML, a case missing from an index-complete README, a stale
`_tabulated` mirror. They found their targets by walking the filesystem, which
in this repo also sweeps in work that is not committed at all — and this
checkout is routinely open in more than one session at once, each mid-build. A
half-finished case sitting untracked in the shared working tree failed the
suite, and because a pre-commit hook runs that suite, ONE session's scratch
blocked EVERY session's commits until it was cleaned up or `--no-verify` was
used. (`06_Other/_demo_dropbox/processed/` did the same thing with mirrors:
3900 files on disk against 680 tracked.)

The generators are deliberately NOT filtered this way. `build_yaml_pages.py`
must still discover an untracked YAML — otherwise a brand-new case could never
get its first page. Only the *assertions* narrow to tracked paths.

WHY THIS IS STILL HONEST. The underlying set is the union of the INDEX and the
HEAD tree, so a file you have `git add`-ed already counts: the case you are
actually about to commit is checked as before. What drops out is only work
nobody has staged — someone else's, or your own not-yet-started.

The union (rather than `git ls-files` alone) is not incidental; see
`check_repo_hygiene._git_tracked_paths`, which this delegates to. During a
concurrent `git commit` the index.lock is held and the index reads back
inconsistent, so index-only membership produced six false positives in a single
run on 2026-08-05 — every one of them comfortably committed in HEAD. Consulting
HEAD too is what stops these guards crying wolf in exactly the situation they
exist to survive.

Fails OPEN — if git can't answer at all, everything counts as tracked and the
guards behave exactly as they did before.
"""

import importlib.util
import sys
from functools import lru_cache
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
_HYGIENE = ENGINE_DIR / "tools_adam" / "scripts" / "check_repo_hygiene.py"


@lru_cache(maxsize=1)
def tracked_set():
    """Repo-relative paths in the index or HEAD, or None if git can't answer."""
    try:
        if "check_repo_hygiene" in sys.modules:
            mod = sys.modules["check_repo_hygiene"]
        else:
            spec = importlib.util.spec_from_file_location(
                "check_repo_hygiene", _HYGIENE)
            mod = importlib.util.module_from_spec(spec)
            sys.modules["check_repo_hygiene"] = mod
            spec.loader.exec_module(mod)
        paths = mod._git_tracked_paths()
    except Exception:
        return None
    return frozenset(paths) if paths else None


def is_tracked(path):
    """True when `path` is in the index or HEAD. Absolute or repo-relative."""
    known = tracked_set()
    if known is None:
        return True
    p = Path(path)
    if p.is_absolute():
        try:
            p = p.resolve().relative_to(REPO_ROOT.resolve())
        except ValueError:
            return True          # outside the repo — not ours to police
    import os
    return os.path.normpath(str(p)) in known


def only_tracked(paths):
    """Filter an iterable of paths down to the committed surface."""
    return [p for p in paths if is_tracked(p)]
