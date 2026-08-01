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
"""
import re
from pathlib import Path

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


def _composed_mirrors():
    for p in sorted(REPO_ROOT.rglob("*_tabulated.txt")):
        rel_parts = set(p.relative_to(REPO_ROOT).parts)
        if rel_parts & SKIP_PARTS:
            continue
        if not p.parent.name.endswith("_tabulated"):
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
