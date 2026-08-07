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


@pytest.mark.parametrize("method", ["Plurality", "RankedRobin", "STV"])
def test_unknown_ballot_methods_are_refused(tmp_path, method):
    """Each drawing IS a particular piece of paper. A choose-one or ranked race
    handed its voters neither the 0–5 grid nor Yes/No bubbles, so drawing either
    would be a lie — and no picture beats a wrong one."""
    case = tmp_path / "case.yaml"
    case.write_text(f"voting_method: {method}\nballots: |-\n  Ada,Ben\n  5,0\n")
    with pytest.raises(art.CaseBallotError):
        art.ballots_from_yaml(case)


def test_star_family_is_drawn(tmp_path):
    case = tmp_path / "case.yaml"
    case.write_text("voting_method: Bloc STAR\nballots: |-\n  Ada,Ben\n  5,0\n")
    drawn, total = art.ballots_from_yaml(case)
    assert total == 1 and drawn[0][0] == "case_ballot_1"
    assert drawn[0][1].kind == "score"


@pytest.mark.parametrize("method", ["Approval", "Approval_Multi_Winner"])
def test_approval_is_drawn_as_a_yes_no_ballot(tmp_path, method):
    """Approval voters get their own paper, not a 0–5 grid with four unused
    columns — single- and multi-winner alike (bloc changes the count, not the
    ballot)."""
    case = tmp_path / "case.yaml"
    case.write_text(f"voting_method: {method}\nballots: |-\n  Ada,Ben\n  1,0\n")
    drawn, _ = art.ballots_from_yaml(case)
    ballot = drawn[0][1]
    assert ballot.kind == "approval"
    svg = art.render_svg(ballot)
    assert ">Yes<" in svg and ">No<" in svg
    assert "Worst" not in svg               # the 0–5 header has no business here


def test_approval_file_with_a_real_score_is_refused(tmp_path):
    """A `3` under `voting_method: Approval` is a file the Yes/No art cannot
    honestly draw — better to fail loudly than to round it to a bubble."""
    case = tmp_path / "case.yaml"
    case.write_text("voting_method: Approval\nballots: |-\n  Ada,Ben\n  3,0\n")
    with pytest.raises(art.CaseBallotError):
        art.ballots_from_yaml(case)


def test_approval_blanks_fill_neither_bubble():
    """`1` is a Yes and `0` is a real No, but a blank is what the voter left
    alone — the tally counts it as not approved, the picture says nothing."""
    assert art.approval_filled(1, 0) and not art.approval_filled(1, 1)
    assert art.approval_filled(0, 1) and not art.approval_filled(0, 0)
    assert not art.approval_filled(None, 0) and not art.approval_filled(None, 1)


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


def test_alt_text_reads_an_approval_ballot_as_yes_and_no():
    ballot = art.Ballot("Voter 1", ["Ada", "Ben", "Cara"], [1, 0, None], Path("."),
                        quoted=False, kind="approval")
    alt = art.alt_text(ballot)
    assert alt.startswith("A Yes/No Approval ballot")
    assert "Ada Yes" in alt and "Ben No" in alt
    assert "Cara left blank (not approved)" in alt
    assert "0–5" not in alt


# --------------------------------------------------------------------------- #
# The `<!-- ballots:<stem> -->` block on a hand-authored page
# --------------------------------------------------------------------------- #
STEM = "lone_pear_c2_b2"


def _mini_repo(tmp_path, *, with_case=True, with_art=True):
    """A miniature repo: a case in one tree, the lesson that wants it in another.

    `07_Concepts/` is deliberately NOT one of the case roots — that is the whole
    point. The lesson carries both markers so the two can be compared directly.
    """
    pages = _load("build_yaml_pages")          # fresh module: REPO is ours to set
    pages.REPO = str(tmp_path)
    pages._PAGES_BY_STEM = None                # the stem index is cached per run

    cases = tmp_path / "method_comparisons" / "set" / "cases"
    if with_case:
        cases.mkdir(parents=True)
        (cases / f"{STEM}.yaml").write_text(
            "election_title: One pear\nvoting_method: STAR\n"
            "ballots: |-\n  Ada,Ben\n  5,0  # Ada all the way\n  0,5\n",
            encoding="utf-8")
        (cases / "cases_pages").mkdir()
        (cases / "cases_pages" / f"{STEM}.md").write_text(
            "# generated\n\n" + pages.SNIPPET_START
            + "\n```text\nWinner: Ada\n```\n" + pages.SNIPPET_END + "\n",
            encoding="utf-8")
        if with_art:
            (cases / "img").mkdir()
            for n in (1, 2):                   # content is irrelevant: only paths
                (cases / "img" / f"{STEM}_ballot_{n}.png").write_bytes(b"")

    lesson = tmp_path / "07_Concepts" / "topics" / "lesson.md"
    lesson.parent.mkdir(parents=True)
    lesson.write_text(f"# Lesson\n\n<!-- ballots:{STEM} -->\n<!-- /ballots -->\n\n"
                      f"<!-- report:{STEM} -->\n<!-- /report -->\n", encoding="utf-8")
    return pages, str(lesson)


def test_both_markers_reach_the_same_pages(tmp_path):
    """`report:` walked the whole repo; `ballots:` walked the case roots only, so
    a block on a cross-method page was never even looked at — no fill, and no
    note either, because the code that writes the note never ran on that page."""
    pages, lesson = _mini_repo(tmp_path)
    assert lesson in pages.pages_with_ballot_blocks()
    assert lesson in pages.pages_with_report_blocks()


def test_a_cross_tree_ballot_block_is_filled(tmp_path):
    """Proximity runs out at the method folder, so a stem is resolved through the
    generated-page index too — the same route `report:` takes, and the reason a
    bare stem with no path is unambiguous."""
    pages, lesson = _mini_repo(tmp_path)
    filled = "".join(pages.pages_with_ballot_blocks()[lesson].values())
    assert f"{STEM}_ballot_1.png" in filled and f"{STEM}_ballot_2.png" in filled
    # paths are relative to the LESSON, which lives two levels down another tree
    assert "../../method_comparisons/set/cases/img/" in filled
    assert "| Ada | Ben |" in filled and "Ada all the way" in filled


@pytest.mark.parametrize("with_case, with_art, note", [
    (True, False, "No ballot art"),      # case found, nobody drew it
    (False, False, "No case named"),     # nothing by that stem anywhere
])
def test_an_unfillable_ballot_block_is_never_silently_empty(tmp_path, with_case,
                                                            with_art, note):
    """A lesson that asked for pictures and got none has to SAY so, and the
    staleness check has to see it — otherwise the page ships without the picture
    it asked for and nothing goes red."""
    pages, lesson = _mini_repo(tmp_path, with_case=with_case, with_art=with_art)
    filled = "".join(pages.pages_with_ballot_blocks()[lesson].values())
    assert note in filled and STEM in filled
    assert pages.check_ballot_blocks() == [lesson]


def test_a_filled_ballot_block_settles(tmp_path):
    """Writing the block back is a fixed point — otherwise every run would
    rewrite the page and `test_yaml_pages_current.py` would never be green."""
    pages, lesson = _mini_repo(tmp_path)
    blocks = pages.pages_with_ballot_blocks()[lesson]
    text = pages.apply_ballot_blocks(open(lesson, encoding="utf-8").read(), blocks)
    open(lesson, "w", encoding="utf-8").write(text)
    assert pages.check_ballot_blocks() == []


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
