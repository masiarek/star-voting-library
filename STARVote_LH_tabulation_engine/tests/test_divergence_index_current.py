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
that instead of letting it touch the repo. The throwaway goes to pytest's
`tmp_path` — i.e. the SYSTEM temp dir, never the working tree.

That used to be impossible: the generator derived each case page's `../../..`
hop from OUT_DIR.relative_to(REPO), so the throwaway had to sit inside the repo
at the real depth or every link changed (and a path outside the repo raised
outright). The generator now measures that hop from a separate LINK_BASE — where
the ledger is COMMITTED — leaving OUT_DIR as nothing but the write destination.

Worth the split, because the in-tree scratch had a nasty failure mode: an
interrupted run (Ctrl-C, a stopped background run, a crash) skipped the `finally`
and orphaned a `_divergence_staleness_*/` holding a whole `cases/**/*.md` tree of
link-bearing pages, every one of them dangling from a location no link was
computed for. Its sibling test_catalog_current.py orphaned four such directories
on 2026-08-06, producing 13 spurious broken-link failures that had to be cleared
by hand; this generator writes far more link-bearing files than that one.
"""
import importlib.util
import sys
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


def test_divergence_ledger_is_current(tmp_path):
    if not GEN.exists():
        pytest.skip("build_divergence_index.py not present")
    mod = _load_generator()

    # System temp, not the working tree — see the module docstring. Only the
    # write destination moves; mod.LINK_BASE still points at the committed
    # location, so the emitted links are the ones a real build would write. No
    # cleanup block: pytest owns tmp_path, so even a killed run leaves nothing
    # behind that the link checks can trip over.
    mod.OUT_DIR = tmp_path
    mod.main()

    problems = []
    for name in FLAT:
        expected = (tmp_path / name).read_text(encoding="utf-8-sig")
        committed = OUT_DIR / name
        actual = committed.read_text(encoding="utf-8-sig") if committed.exists() else ""
        if actual != expected:
            problems.append(f"{name} differs")

    expected_cases, actual_cases = _case_tree(tmp_path), _case_tree(OUT_DIR)
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

    assert not problems, (
        "Divergence ledger is stale:\n  " + "\n  ".join(problems) + "\n"
        "Regenerate it with:\n"
        "    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_divergence_index.py"
    )
