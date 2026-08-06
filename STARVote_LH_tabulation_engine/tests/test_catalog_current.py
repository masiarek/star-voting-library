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
rather than letting it touch the repo. The throwaway goes to pytest's `tmp_path`
— i.e. the SYSTEM temp dir, never the working tree.

It used to be created at `07_Concepts/<tmp>`, on the theory that the generator
needed the real depth for its relative links. It does not: every link CATALOG.md
emits is a bare sibling name (`races.csv`, `BV_registry.md`, `README.md`,
`multirace_elections.md`), a hardcoded `../../` hop, or `_rel()` measured from
REPO — none of them read IDXDIR, and the three outputs come out byte-identical
wherever they are written. What the in-tree scratch *did* buy was a failure mode:
any interrupted run (Ctrl-C, a stopped background run, a crash) skipped the
`finally` and orphaned a `_catalog_staleness_*/` holding a CATALOG.md whose
sibling links resolve from nowhere. Four such orphans on 2026-08-06 produced 13
spurious broken-link failures in check_links()/test_md_links.py and had to be
cleared by hand; a live one also makes a concurrent link check flaky, since the
directory is in the tree while another session walks it.
"""
import importlib.util
import sys
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


def test_catalog_is_current(tmp_path):
    if not GEN.exists():
        pytest.skip("build_catalog.py not present")
    mod = _load_generator()

    # System temp, not the working tree — see the module docstring. No cleanup
    # block: pytest owns tmp_path, so even a killed run leaves nothing behind
    # that the link checks can trip over.
    mod.IDXDIR = str(tmp_path)
    mod.main()

    stale = []
    for name in OUTPUTS:
        expected = (tmp_path / name).read_text(encoding="utf-8-sig")
        committed = IDXDIR / name
        actual = committed.read_text(encoding="utf-8-sig") if committed.exists() else ""
        if actual != expected:
            stale.append(name)

    assert not stale, (
        "Catalog is stale: " + ", ".join(stale) + "\n"
        "Regenerate it with:\n"
        "    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_catalog.py\n"
        "(a YAML election or frozen _bv_export.json was added/moved/removed since "
        "it was last built)."
    )
