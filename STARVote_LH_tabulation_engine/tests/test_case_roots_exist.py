"""Every case-root a test module names must exist on disk.

The failure this catches is SILENT, which is why it needs its own test. Most
suites here collect their cases by globbing a directory constant:

    CASE_DIRS = [REPO_ROOT / "01_STAR" / "02_Examples", ...]

If a folder is renamed and that constant isn't updated, the glob simply yields
nothing. No error, no skip — the parameterized cases just stop existing and the
suite still reports all green, with a smaller number nobody reads. The
2026-08-02 folder reorganization did exactly this: 953 passed quietly became
724 passed while only two tests failed loudly.

So: import every sibling test module, walk its module-level constants, and
assert that anything pointing under the repo root actually resolves. Renaming a
folder now breaks the build at the rename instead of hollowing out the suite.
"""
from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent

TEST_MODULES = sorted(
    m.name for m in pkgutil.iter_modules([str(HERE)])
    if m.name.startswith("test_") and m.name != Path(__file__).stem
)


def _candidate_paths(value):
    """Yield every Path-like leaf in `value` (scalars, lists, tuples, sets)."""
    if isinstance(value, Path):
        yield value
    elif isinstance(value, str):
        # Only strings that were clearly built as repo paths — a bare word like
        # "star" is not a path claim, an absolute path under the repo is.
        if value.startswith(str(REPO_ROOT)):
            yield Path(value)
    elif isinstance(value, (list, tuple, set, frozenset)):
        for item in value:
            yield from _candidate_paths(item)


@pytest.mark.parametrize("modname", TEST_MODULES)
def test_module_case_roots_exist(modname):
    mod = importlib.import_module(modname)
    missing = []
    for name, value in vars(mod).items():
        if name.startswith("_"):
            continue
        for path in _candidate_paths(value):
            try:
                rel = path.resolve().relative_to(REPO_ROOT.resolve())
            except ValueError:
                continue  # outside the repo (tmp dirs, site-packages)
            if not path.exists():
                missing.append(f"{name} -> {rel}")
    assert not missing, (
        f"{modname} names {len(missing)} repo path(s) that do not exist. A "
        f"renamed folder silently empties the glob that uses them:\n  "
        + "\n  ".join(sorted(missing))
    )
