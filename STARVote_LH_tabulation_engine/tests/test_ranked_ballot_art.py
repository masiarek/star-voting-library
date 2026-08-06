"""
test_ranked_ballot_art.py
=========================
Guards the ranked ballot art drawn by
`tools_adam/scripts/build_ranked_ballot_images.py` for
`07_Concepts/scores_and_ranks/`.

These three figures are not three pictures, they are one argument, and the
argument lives entirely in which bubbles are filled:

* the **strict** ballot must actually be strict (no two candidates sharing a
  column) — otherwise the page's "you may not mark two candidates equal" is
  illustrated by a ballot doing exactly that;
* the **weak** ballot must differ from it in exactly one row — the pages say
  "one mark moved", and a second edited row would make that sentence false;
* the **overvote** ballot must carry the *same marks as the weak one*. That is
  the entire point of the third figure: the voter did nothing different, and the
  strict paper spoiled a rank anyway. Edit one and forget the other and all
  three pages keep their prose while the art quietly stops proving it.

Plus the wiring check the case art gets: a PNG nobody embeds is dead weight, and
a page embedding a PNG nobody draws is a broken image on the published site.
"""
import importlib.util
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
SCRIPTS = REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam" / "scripts"
PAGE_DIR = REPO_ROOT / "07_Concepts" / "scores_and_ranks"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


art = _load("build_ranked_ballot_images")


def test_strict_ballot_is_actually_strict():
    ranks = art.BALLOTS["ranks_strict"].ranks
    assert None not in ranks, "the strict figure is a complete ballot"
    assert len(set(ranks)) == len(ranks), "a strict ranking gives every candidate its own place"


def test_weak_ballot_shares_exactly_one_rank():
    ranks = art.BALLOTS["ranks_weak"].ranks
    assert len(set(ranks)) == len(ranks) - 1, "exactly one pair of candidates shares a rank"


def test_weak_differs_from_strict_by_one_mark():
    """The pages say "one mark moved". Keep that literally true."""
    strict = art.BALLOTS["ranks_strict"].ranks
    weak = art.BALLOTS["ranks_weak"].ranks
    moved = [i for i, (a, b) in enumerate(zip(strict, weak)) if a != b]
    assert len(moved) == 1, f"expected one changed row, got {moved}"


def test_overvote_is_the_weak_marks_on_strict_paper():
    weak = art.BALLOTS["ranks_weak"]
    over = art.BALLOTS["ranks_strict_overvote"]
    assert over.ranks == weak.ranks, (
        "the overvote figure must show the WEAK ballot's marks — that is what makes "
        "'the voter did nothing different' true"
    )
    assert over.instruction == art.BALLOTS["ranks_strict"].instruction, (
        "…on the STRICT ballot's paper, or it is not an overvote at all"
    )
    # The flagged rows are the ones actually sharing a column, not a hand-picked pair.
    shared = [i for i, r in enumerate(over.ranks) if over.ranks.count(r) > 1]
    assert sorted(over.flagged) == shared


def test_every_drawn_ballot_is_embedded_on_a_page():
    pages = "\n".join(p.read_text() for p in PAGE_DIR.glob("*.md"))
    for slug in art.BALLOTS:
        assert f"img/{slug}.png" in pages, (
            f"{slug}.png is drawn but no page in {PAGE_DIR.name}/ embeds it"
        )


def test_every_embedded_ranked_png_is_drawn():
    """A page embedding art the script doesn't write is a 404 on the built site."""
    drawn = {f"{slug}.png" for slug in art.BALLOTS}
    for page in PAGE_DIR.glob("*.md"):
        for name in drawn:
            if f"img/{name}" in page.read_text():
                assert (PAGE_DIR / "img" / name).exists(), f"{name} missing from img/"


def test_renders_without_pillow():
    """SVG is the master and must not depend on the rasterizer being installed."""
    svg = art.render_svg(art.BALLOTS["ranks_strict_overvote"])
    assert svg.startswith("<svg") and svg.endswith("</svg>")
    # Five filled bubbles, two of them flagged rust — one mark per candidate.
    assert svg.count(f'fill="{art.RUST}"/>') == 2
