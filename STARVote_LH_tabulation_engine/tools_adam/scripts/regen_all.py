#!/usr/bin/env python3
"""Regenerate every derived Markdown/CSV surface in the repo, in dependency order.

The repo has several *generators* that turn the source `.yaml` elections (and their
frozen BV exports) into reader-facing pages and indexes. Until now they were split
three ways — some run by the git pre-commit hook, some drift-guarded by pytest, some
purely manual — so "which builders do I run after adding a case?" had no single
answer. This is that single answer: run everything, in the one order that satisfies
the cross-dependencies, with one command.

    python STARVote_LH_tabulation_engine/tools_adam/scripts/regen_all.py

Order matters (each step consumes an earlier step's output):

  1. build_divergence_index  — writes method_comparisons/divergence_review/cases/*.md
  2. build_yaml_pages        — per-election pages; LINKS to the divergence case (1)
  3. build_yaml_index        — by-method index; checks each page from (2) EXISTS
  4. build_catalog           — faceted CATALOG.md + races.csv + elections.csv
  5. build_bv_registry       — BV_registry.md + bv_cases.csv (from bv_* fields)
  6. build_multirace_index   — multirace_elections.md (from frozen exports)
  7. build_paradox_index     — the voting-paradoxes tag index

Steps 4–7 only READ the `.yaml` sources, so their relative order is free; they run
after the page/index trio so any page they happen to link already exists.

`--check` additionally runs the two *checkers* after the generators:
  check_repo_hygiene  (link/anchor/terminology audit) and
  check_external_links (advisory; hits the network — off by default).
Checkers never write; a non-zero from a checker is reported but, like the pre-commit
hook, does not by itself fail the run unless a *generator* also failed.

Exit status is non-zero if any generator failed (so it's safe to chain in CI/Make).
Does NOT regenerate the `_tabulated` engine mirrors (those come from re-running each
YAML through the engine) and does NOT stage or commit anything — it only rewrites the
generated files in place, exactly as the individual builders would.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (command, one-line what-it-writes) — ORDER IS LOAD-BEARING for the first four:
# the ballot art has to be on disk before build_yaml_pages decides which pages
# show a picture. `--refresh` only redraws cases that already have art, so this
# never invents pictures for the other 300 cases.
GENERATORS = [
    ("build_style_ballot_images.py --refresh",
                                  "ballot art for cases that already have it"),
    ("build_divergence_index.py", "method_comparisons/divergence_review/ (INDEX, csv, cases/*.md)"),
    ("build_yaml_pages.py",       "per-election <set>_pages/*.md"),
    ("build_yaml_index.py",       "YAML_test_case_index/README.md (by-method index)"),
    ("build_catalog.py",          "CATALOG.md + races.csv + elections.csv"),
    ("build_bv_registry.py",      "BV_registry.md + bv_cases.csv"),
    ("build_multirace_index.py",  "multirace_elections.md"),
    ("build_paradox_index.py",    "voting_paradoxes tag index"),
]

# Checkers (read-only; run only with --check). check_external_links hits the network.
CHECKERS = [
    ("check_repo_hygiene.py",   "relative links / anchors / terminology / index completeness"),
    ("check_external_links.py", "external URLs (advisory; network)"),
]


def _run(script: str, desc: str, quiet: bool) -> tuple[str, bool, float]:
    """Run one sibling script with the SAME interpreter running us. Returns
    (script, ok, seconds). Streams the child's output unless --quiet.
    An entry may carry flags ("build_x.py --refresh"); they're passed through."""
    name, *flags = script.split()
    path = HERE / name
    if not path.is_file():
        print(f"  ! {name}: not found — skipping", file=sys.stderr)
        return (script, False, 0.0)
    t0 = time.monotonic()
    stdout = subprocess.DEVNULL if quiet else None
    proc = subprocess.run([sys.executable, str(path), *flags], stdout=stdout)
    return (script, proc.returncode == 0, time.monotonic() - t0)


def main() -> int:
    ap = argparse.ArgumentParser(description="Regenerate all derived pages/indexes in dependency order.")
    ap.add_argument("--check", action="store_true",
                    help="also run the read-only checkers (hygiene + external links) afterward")
    ap.add_argument("-q", "--quiet", action="store_true",
                    help="suppress each builder's own output; print only the summary")
    args = ap.parse_args()

    print(f"regen_all: {len(GENERATORS)} generators via {sys.executable}\n")
    results = []
    for i, (script, desc) in enumerate(GENERATORS, 1):
        if not args.quiet:
            print(f"[{i}/{len(GENERATORS)}] {script}  →  {desc}")
        results.append(_run(script, desc, args.quiet))
        if not args.quiet:
            print()

    check_results = []
    if args.check:
        print("regen_all: running read-only checkers…\n")
        for script, desc in CHECKERS:
            check_results.append(_run(script, desc, args.quiet))

    # Summary
    print("─" * 60)
    gen_failed = 0
    for script, ok, secs in results:
        flag = "ok " if ok else "FAIL"
        if not ok:
            gen_failed += 1
        print(f"  [{flag}] {script:<40} {secs:5.1f}s")
    for script, ok, secs in check_results:
        print(f"  [{'ok ' if ok else 'warn'}] {script:<28} {secs:5.1f}s  (checker)")
    print("─" * 60)

    if gen_failed:
        print(f"regen_all: {gen_failed} generator(s) FAILED — see output above.")
        return 1
    print("regen_all: all generators succeeded. "
          "Review `git status`, then commit the regenerated files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
