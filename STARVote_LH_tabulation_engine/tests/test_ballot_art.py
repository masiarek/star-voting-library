"""
test_ballot_art.py
==================
Guards the 0–5 ballot art drawn from a case file by
`tools_adam/scripts/build_style_ballot_images.py --from-yaml <case.yaml>` and
embedded by `build_yaml_pages.py`.

Two halves:

* the parser — it has to read a `ballots:` block the way the ENGINE does
  (weights, `Count:` header, markers, comments), or the picture would show
  something the tally never saw;
* the wiring — every `<stem>_ballot_<n>.png` sitting in a case folder's `img/`
  must actually appear on that case's generated page. Without this, deleting the
  figure block from the generator would leave `test_yaml_pages_current.py` green
  (it compares the generator against its own output) while every ballot picture
  silently vanished from the site.
"""
import importlib.util
import re
import sys
from pathlib import Path

import pytest

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
SCRIPTS = REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


art = _load("build_style_ballot_images")


def test_parses_notes_weights_and_markers():
    cast, rows = art.parse_ballot_block(
        "Ada,Ben,Cara\n"
        "5, 3, 0  # Caroline loves Ada\n"
        "42: 5, 4, 3\n"
        "-, ~, 2\n"
    )
    assert cast == ["Ada", "Ben", "Cara"]
    assert rows[0] == art.BallotRow(1, [5, 3, 0], "Caroline loves Ada", ["5", "3", "0"])
    assert rows[1] == art.BallotRow(42, [5, 4, 3], "", ["5", "4", "3"])  # weight, not a score
    # Markers draw as no mark at all, but the page still prints what the file said.
    assert rows[2] == art.BallotRow(1, [None, None, 2], "", ["-", "~", "2"])


def test_count_label_is_not_a_candidate():
    cast, rows = art.parse_ballot_block("Count:Ada,Ben\n15:5,2\n")
    assert cast == ["Ada", "Ben"]
    assert rows == [art.BallotRow(15, [5, 2], "", ["5", "2"])]


@pytest.mark.parametrize("block, why", [
    ("Ada,Ben,Cara\nAda>Cara>Ben\n", "ranked ballots have no 0–5 bubbles"),
    ("Ada,Ben\n5,9\n", "9 is off the 0–5 scale"),
    ("Ada,Ben\n5,3,0\n", "row is wider than the header"),
    ("Ada,Ben\n", "no ballot rows"),
])
def test_unrenderable_blocks_raise(block, why):
    with pytest.raises(art.CaseBallotError):
        art.parse_ballot_block(block)


def test_row_title_prefers_the_authors_note():
    assert art.row_title(1, 1, "Caroline loves Choco") == "Caroline loves Choco"
    assert art.row_title(1, 42, "") == "42 voters"
    assert art.row_title(3, 1, "") == "Voter 3"
    long_note = "x" * 200
    assert len(art.row_title(1, 1, long_note)) <= art.TITLE_MAX_CHARS


def test_titles_shrink_to_fit_the_canvas():
    """A style name renders full size; a long ballot note shrinks instead of
    running off the right edge (both renderers read this one number)."""
    assert art.title_font_size('"Exaggerated Compromise"') == art.TITLE_SIZE
    long_title = "x" * art.TITLE_MAX_CHARS
    size = art.title_font_size(long_title)
    assert size >= art.TITLE_MIN_SIZE
    assert len(long_title) * art.TITLE_CHAR_W * size <= art.W - 2 * art.TITLE_X


def test_alt_text_names_every_row():
    ballot = art.Ballot("Voter 1", ["Ada", "Ben"], [5, None], Path("."), quoted=False)
    alt = art.alt_text(ballot)
    assert "Ada 5" in alt
    assert "Ben left blank (counts as 0)" in alt


def _art_files():
    pages = _load("build_yaml_pages")
    for root in pages.ROOTS:
        yield from sorted((REPO_ROOT / root).rglob("img/*_ballot_[0-9]*.png"))


def test_every_drawn_ballot_is_embedded_on_its_page():
    missing = []
    for png in _art_files():
        stem = re.sub(r"_ballot_\d+$", "", png.stem)
        case_dir = png.parent.parent
        page = case_dir / f"{case_dir.name}_pages" / f"{stem}.md"
        if not page.exists() or png.name not in page.read_text(encoding="utf-8"):
            missing.append(f"{png.relative_to(REPO_ROOT)} → {page.relative_to(REPO_ROOT)}")
    assert not missing, (
        "ballot art exists but its case page doesn't show it:\n  "
        + "\n  ".join(missing)
        + "\nRegenerate with: python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py"
    )
