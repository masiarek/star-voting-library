"""
test_tabulated_mirrors_current.py
=================================
Freshness guard for the committed `_tabulated` mirrors — the one derived
surface that had no drift test.

Every composed mirror (write_composed_tabulated) embeds the ORIGINAL source
YAML verbatim between its provenance header and the TABULATION RESULTS
divider. So staleness is detectable by pure text comparison, no tabulation
needed: if someone edits a YAML's ballots and forgets to re-run the engine,
the mirror still carries the old YAML — and the regenerated page would show
new ballots beside an old count while every other test stays green.

regen_all.py deliberately does NOT regenerate mirrors (they come from
re-running each YAML through the engine), which is exactly why this guard
exists. On failure: re-run the named YAML through
STARVote_LH_tabulation_engine/starvote_larry_hastings.py and commit the
refreshed mirror.

Aux mirrors (`<stem>_<TAG>_tabulated.txt`) from the side engines don't all
embed the source, so only composed-format mirrors are checked — the count
assertion keeps the check non-vacuous.

ONLY GIT-TRACKED MIRRORS ARE CHECKED, and that matters. This guards the
*committed* surface, but the scan used to be a plain filesystem walk, which
also swept up every mirror a local run had ever dropped in an IGNORED
directory — 3900 files on disk against 680 tracked. `06_Other/_demo_dropbox/
processed/` is the usual culprit: its own .gitignore excludes it, engine runs
leave mirrors there, and their source YAMLs get moved or deleted afterwards,
so the guard reported "embedded source not found" for files that are not part
of the repo at all. That made the result depend on what junk happened to be
in someone's working tree — and since a pre-commit hook runs this suite, one
stale scratch file blocked every commit in the repo until it was deleted.
Tracked-only makes the check deterministic across machines and matches what
the guard is actually for.
"""
import re
from pathlib import Path

import tracked_paths

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent

SKIP_PARTS = {".git", ".venv", "site", "_notes", "node_modules",
              "__pycache__", "STARVote_LH_tabulation_engine"}

_COMPOSED = re.compile(
    r"^={70}\n"
    r"SOURCE FILE:\s*(?P<src>.+)\n"
    r"TABULATED FILE:.*\n"
    r"={70}\n\n"
    r"(?P<body>.*?)\n\n"
    r"={70}\n"
    r"TABULATION RESULTS\n",
    re.S,
)


def _candidate_mirrors():
    """Every git-TRACKED `*_tabulated.txt`, checkout-independent.

    Membership comes from tests/tracked_paths.py (index UNION HEAD, so a
    concurrent commit holding index.lock can't make committed files look
    untracked). Falls back to the plain walk when git can't answer at all;
    the `checked >= 300` assertion below stops either path going silently
    empty.
    """
    walked = sorted(REPO_ROOT.rglob("*_tabulated.txt"))
    if tracked_paths.tracked_set() is None:
        return walked
    return [p for p in walked if tracked_paths.is_tracked(p)]


def _composed_mirrors():
    for p in sorted(_candidate_mirrors()):
        rel_parts = set(p.relative_to(REPO_ROOT).parts)
        if rel_parts & SKIP_PARTS:
            continue
        if not p.parent.name.endswith("_tabulated"):
            continue
        if not p.is_file():          # tracked but deleted in the working tree
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        m = _COMPOSED.match(text)
        if m:
            yield p, m


def test_composed_mirrors_match_their_source_yaml():
    stale, missing, checked = [], [], 0
    for mirror, m in _composed_mirrors():
        checked += 1
        src = mirror.parent.parent / m.group("src").strip()
        rel = str(mirror.relative_to(REPO_ROOT))
        if not src.exists():
            missing.append(f"{rel}: embedded source {m.group('src')!r} not found")
            continue
        current = src.read_text(encoding="utf-8").rstrip()
        if m.group("body") != current:
            missing_cmd = str(src.relative_to(REPO_ROOT))
            stale.append(
                f"{rel} is STALE — re-run: uv run python "
                f"STARVote_LH_tabulation_engine/starvote_larry_hastings.py "
                f"{missing_cmd}"
            )
    assert checked >= 300, (
        f"only {checked} composed mirrors found — the discovery pattern broke"
    )
    assert not missing, "\n".join(missing)
    assert not stale, (
        f"{len(stale)} stale mirror(s) — the YAML changed but the engine "
        "was never re-run:\n" + "\n".join(stale)
    )
