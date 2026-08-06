"""
test_divergence_index_current.py
================================
Anti-staleness guard for the cross-method divergence ledger — the sibling of
test_yaml_index_current.py, for method_comparisons/divergence_review/:

    INDEX.md         the ledger's front page
    divergence.csv   one row per election, all winners + flags
    cases/**/*.md    one teaching page per diverging case

Regenerates the lot (build_divergence_index.py) into a throwaway directory and
asserts the committed copies match — contents AND the set of case files, so a
page for a case that no longer diverges, or a missing page for one that now
does, both fail.

That second half is the one that bit master (2026-08-05): the pre-commit hook
refreshes this ledger and stages the whole folder, but never blocks on failure,
and nothing else checked it — so a review page for an uncommitted case shipped
without its case, its two links dangled, and `mkdocs --strict` aborted. The
generator only stopped *creating* those; this is what notices one that is
already there.

Costs ~11s: it re-tabulates the curated STAR library under IRV / Ranked Robin /
Approval, which is the only honest way to know the ledger is right.

The generator writes through the module-level OUT_DIR, so the test redirects
that instead of letting it touch the repo. The throwaway must live *inside* the
repo at the same depth as the real folder (method_comparisons/<tmp>): the
generator derives each case page's `../../..` hop from
OUT_DIR.relative_to(REPO), so a different depth would silently change every
link, and a path outside the repo would raise.
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
GEN = (REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts"
       / "build_divergence_index.py")
OUT_DIR = REPO_ROOT / "method_comparisons" / "divergence_review"
FLAT = ("INDEX.md", "divergence.csv")


def _load_generator():
    spec = importlib.util.spec_from_file_location("build_divergence_index", GEN)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_divergence_index"] = mod
    spec.loader.exec_module(mod)
    return mod


def _case_tree(root):
    """{relative posix path: text} for every case page under <root>/cases."""
    cases = root / "cases"
    if not cases.is_dir():
        return {}
    return {p.relative_to(cases).as_posix(): p.read_text(encoding="utf-8")
            for p in sorted(cases.rglob("*.md"))}


def test_divergence_ledger_is_current():
    if not GEN.exists():
        pytest.skip("build_divergence_index.py not present")
    mod = _load_generator()

    # Same depth as the real output dir — see the module docstring.
    tmp = Path(tempfile.mkdtemp(dir=OUT_DIR.parent, prefix="_divergence_staleness_"))
    try:
        mod.OUT_DIR = tmp
        mod.main()

        problems = []
        for name in FLAT:
            expected = (tmp / name).read_text(encoding="utf-8-sig")
            committed = OUT_DIR / name
            actual = committed.read_text(encoding="utf-8-sig") if committed.exists() else ""
            if actual != expected:
                problems.append(f"{name} differs")

        expected_cases, actual_cases = _case_tree(tmp), _case_tree(OUT_DIR)
        missing = sorted(set(expected_cases) - set(actual_cases))
        orphaned = sorted(set(actual_cases) - set(expected_cases))
        changed = sorted(k for k in set(expected_cases) & set(actual_cases)
                         if expected_cases[k] != actual_cases[k])
        for label, items in (("missing case page(s)", missing),
                             ("orphaned case page(s)", orphaned),
                             ("stale case page(s)", changed)):
            if items:
                problems.append(f"{len(items)} {label}: "
                                + ", ".join(items[:5])
                                + (" …" if len(items) > 5 else ""))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    assert not problems, (
        "Divergence ledger is stale:\n  " + "\n  ".join(problems) + "\n"
        "Regenerate it with:\n"
        "    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_divergence_index.py"
    )
