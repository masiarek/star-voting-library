"""
test_catalog_current.py
=======================
Anti-staleness guard for the faceted catalog — the sibling of
test_yaml_index_current.py, for the other three generated files in
07_Concepts/YAML_test_case_index/:

    CATALOG.md      the slice-and-dice view over every election & race
    races.csv       race-grain fact table
    elections.csv   election-grain fact table

Regenerates all three (build_catalog.py) into a throwaway directory and asserts
the committed copies match. Without this nothing noticed a stale catalog: the
pre-commit hook refreshes it but never blocks on failure, and CI had no guard at
all, so drift could sit on master indefinitely — and because CATALOG.md's rows
LINK to case pages, a stale catalog turns into dangling links, a red
test_md_links, and an aborted `mkdocs --strict`.

The generator writes through the module-level IDXDIR, so the test redirects that
rather than letting it touch the repo. The throwaway lives *inside* the repo at
the same depth as the real one (07_Concepts/<tmp>) so any relative link the
generator emits comes out identical to the committed copy's.
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
GEN = REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts" / "build_catalog.py"
IDXDIR = REPO_ROOT / "07_Concepts" / "YAML_test_case_index"
OUTPUTS = ("CATALOG.md", "races.csv", "elections.csv")


def _load_generator():
    spec = importlib.util.spec_from_file_location("build_catalog", GEN)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_catalog"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_catalog_is_current():
    if not GEN.exists():
        pytest.skip("build_catalog.py not present")
    mod = _load_generator()

    # Same depth as the real output dir, so emitted relative links match.
    tmp = Path(tempfile.mkdtemp(dir=IDXDIR.parent, prefix="_catalog_staleness_"))
    try:
        mod.IDXDIR = str(tmp)
        mod.main()
        stale = []
        for name in OUTPUTS:
            expected = (tmp / name).read_text(encoding="utf-8-sig")
            committed = IDXDIR / name
            actual = committed.read_text(encoding="utf-8-sig") if committed.exists() else ""
            if actual != expected:
                stale.append(name)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    assert not stale, (
        "Catalog is stale: " + ", ".join(stale) + "\n"
        "Regenerate it with:\n"
        "    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_catalog.py\n"
        "(a YAML election or frozen _bv_export.json was added/moved/removed since "
        "it was last built)."
    )
