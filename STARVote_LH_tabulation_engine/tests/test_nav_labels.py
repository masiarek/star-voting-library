"""
test_nav_labels.py
==================
The sidebar labels that `mkdocs_hooks.py` rewrites must stay honest.

WHY. Section labels in the left nav are the one title nobody authors — MkDocs
derives them from the folder name — so the hook is the only thing standing
between a reader and "Rr tiebreaks" or "IRV OUTLIER RR WITH STAR". Two ways
that goes stale:

1. The five divergence-bucket labels are COPIED from build_divergence_index.py's
   BUCKET_TITLE, because the docs build (uv sync --group docs) must not depend
   on the engine's tooling being importable. A copy drifts. This test is the
   thing that notices — rename a bucket in the generator and the sidebar keeps
   announcing the old name until someone looks.
2. The casing rules are regex-driven, and the pipeline order matters (unpad
   before acronyms, because stripping can expose a lowercase acronym at the
   front). The cases below are the ones that were actually wrong on the live
   site, kept as regressions.
"""
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(ENGINE_DIR / "tools_adam" / "scripts"))

import build_divergence_index as generator  # noqa: E402
import mkdocs_hooks as hooks  # noqa: E402


def _derived(folder_name):
    """What MkDocs makes of a folder name, for a name that carries a capital."""
    return folder_name.replace("_", " ")


def test_bucket_labels_match_the_generator():
    """Every bucket the ledger writes has the generator's own name in the nav."""
    expected = {_derived(k): v for k, v in generator.BUCKET_TITLE.items()}
    assert hooks.SECTIONS == expected


@pytest.mark.parametrize(
    "derived, expected",
    [
        # Folder was all lowercase, so MkDocs sentence-cased it and buried the
        # acronyms.
        ("Rr tiebreaks", "RR tiebreaks"),
        ("Rr vs irv plurality", "RR vs IRV plurality"),
        ("Star vs rr divergence", "STAR vs RR divergence"),
        ("Condorcet vs ranked robin", "Condorcet vs Ranked Robin"),
        ("Bv stv sole survivor crash", "BV STV sole survivor crash"),
        ("Most wins vs condorcet", "Most wins vs Condorcet"),
        ("Dark horse borda", "Dark horse Borda"),
        ("Iia cycle spoiler", "IIA cycle spoiler"),
        ("Sntv village council", "SNTV village council"),
        # Punctuation a folder name cannot carry, restored from the README H1.
        ("Split cycle", "Split Cycle"),
        ("Postit rcv example", "Post-it RCV example"),
        ("Hands on", "Hands-on"),
        # ...and not applied where the words are not that name.
        ("Split voting", "Split voting"),
        # A leading underscore becomes a leading space, and .capitalize() then
        # lands on the space and does nothing.
        (" main", "Main"),
        (" main pages", "Main pages"),
        # One capital anywhere suppresses .capitalize() for the whole label.
        ("reporting BV", "Reporting BV"),
        ("silly two cand STAR", "Silly two cand STAR"),
        # Whole-label replacements win outright.
        ("IRV OUTLIER RR WITH STAR", "RCV-IRV is the outlier (center squeeze)"),
        # Election IDs are not acronyms: bv2138 must survive intact.
        ("No condorcet bv2138", "No Condorcet bv2138"),
        # A folder that cannot be renamed (a published BV description points
        # into it), relabelled in place so it reads as a method shelf.
        ("06 Other", "06 Other methods"),
        # ...and the shelf inside it keeps its own name.
        ("Other ranked methods", "Other ranked methods"),
        # Already correct, and must stay untouched.
        ("01 STAR", "01 STAR"),
        ("Cases pages", "Cases pages"),
        ("STARVote LH tabulation engine", "STARVote LH tabulation engine"),
    ],
)
def test_clean(derived, expected):
    assert hooks.clean(derived) == expected


@pytest.mark.parametrize(
    "derived", ["Rr tiebreaks", " main", "reporting BV", "IRV OUTLIER RR WITH STAR"]
)
def test_clean_is_idempotent(derived):
    """Running the pipeline on its own output must change nothing."""
    once = hooks.clean(derived)
    assert hooks.clean(once) == once


# --- NAV_ORDER ----------------------------------------------------------
#
# The order list names files and folders by their on-disk name. Nothing at
# build time notices a name that has since been renamed or deleted — the entry
# simply stops matching and the page slides back to its alphabetical spot,
# which looks like nobody ever set an order rather than like a bug. These two
# tests are what notices.


def test_nav_order_folders_exist():
    for folder in hooks.NAV_ORDER:
        assert (REPO_ROOT / folder).is_dir(), f"NAV_ORDER key is not a folder: {folder}"


def test_nav_order_entries_exist():
    for folder, names in hooks.NAV_ORDER.items():
        for name in names:
            if name == hooks.SPINE_BREAK:
                continue
            assert (REPO_ROOT / folder / name).exists(), \
                f"NAV_ORDER lists {name!r}, which is not in {folder}"


def test_nav_order_has_no_duplicates():
    for folder, names in hooks.NAV_ORDER.items():
        listed = [n for n in names if n != hooks.SPINE_BREAK]
        assert len(listed) == len(set(listed)), f"NAV_ORDER repeats an entry in {folder}"
