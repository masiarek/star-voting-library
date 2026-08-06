#!/usr/bin/env python3
"""Render the repo's RANKED ballot art — the third piece of paper.

`build_style_ballot_images.py` draws two ballots and refuses everything else: the
0–5 STAR grid and the Approval Yes/No double bubble. A ranked ballot is neither.
It is a grid of *places* — one column per rank, one row per candidate — and the
rule that matters is not what a mark means but how many marks a column may hold.
That rule is the whole subject of `07_Concepts/scores_and_ranks/`, and it is
invisible in prose: "you may not mark two candidates equal" is a sentence, while
two filled bubbles in one column is a picture.

So these are drawn here, in the same visual language as the rest of the repo's
ballot art (same palette, same geometry, same cast, same PNG pipeline — all
imported from the style script, so there is one source of truth for the look).
They are deliberately NOT wired into the case-art pipeline: that draws ballots
from an election YAML's tally, and these three are one voter's paper with no
election behind them. `--from-yaml` refusing ranked files stays correct.

    python3 build_ranked_ballot_images.py            # write SVG + PNG for all
    python3 build_ranked_ballot_images.py --svg-only # skip rasterizing
    python3 build_ranked_ballot_images.py --only ranks_weak

The three ballots are one voter marked three ways, and they only teach anything
as a set — see the STRICT/WEAK/OVERVOTE comment below before editing any of them.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from typing import NamedTuple

# Import the style script by path, not by name: it is a CLI script in a scripts/
# folder, not an installed module, so a plain `import` only works when the cwd
# happens to be that folder. Every other tool here that reaches across does the
# same (see tests/test_ballot_art.py::_load).
_SCRIPTS = Path(__file__).resolve().parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, _SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


art = _load("build_style_ballot_images")

# The look, borrowed wholesale. Anything that changes in the style script — the
# palette, the row height, the antialiasing pass — changes here too, which is the
# point of importing rather than copying.
REPO_ROOT = art.REPO_ROOT
RUST, ROW_TINT, RULE = art.RUST, art.ROW_TINT, art.RULE
BUBBLE_STROKE, INK = art.BUBBLE_STROKE, art.INK
FONT, BODY_FONT = art.FONT, art.BODY_FONT
TITLE_X, TITLE_Y = art.TITLE_X, art.TITLE_Y
INSTRUCTION_Y = art.HDR_WORST_Y      # where the Approval ballot puts its one line
COLUMN_HDR_Y = art.STAR_ROW_Y        # where the 0–5 ballot puts its scale
GRID_TOP, ROW_H, NAME_X = art.GRID_TOP, art.ROW_H, art.NAME_X
BOTTOM_PAD = art.BOTTOM_PAD
FTR_SIZE, FTR_LINE_H, FTR_GAP = art.FTR_SIZE, art.FTR_LINE_H, art.FTR_GAP
SS = art.SS
esc, title_font_size = art.esc, art.title_font_size

IMG_DIR = REPO_ROOT / "07_Concepts" / "scores_and_ranks" / "img"

# The same five candidates as every other ballot picture in this repo (the style
# gallery, `07_Concepts/img/ballot_panel_ranking.png`, the whole-ballot pair).
# House style asks for a fresh cast per *scenario* — but a ballot figure is not a
# scenario, it is a picture of paper, and a reader who has already met this cast
# on the ranking panel should recognise the same ballot here rather than wonder
# what changed.
CANDIDATES = ["Andre", "Blake", "Carmen", "David", "Ella"]

# --------------------------------------------------------------------------- #
# STRICT / WEAK / OVERVOTE — one voter, three ballots, one bubble of difference
# --------------------------------------------------------------------------- #
# This voter's honest opinion: Andre best, then Carmen, then David — and Blake
# and Ella are equally last. That last "equally" is the only thing under test, so
# everything else is held fixed across all three drawings.
#
#   ranks_strict   Blake 4th, Ella 5th        — the order the paper made them invent
#   ranks_weak     Blake 4th, Ella 4th        — the opinion they actually hold
#   ranks_strict_overvote                     — the WEAK marks on the STRICT paper
#
# The third is not a third opinion. It is drawing #2's marks under drawing #1's
# rule, which is what makes the pages' claim concrete: the voter did nothing
# different, and the ballot spoiled a rank anyway. So `ranks_weak` and
# `ranks_strict_overvote` MUST keep identical `ranks` — if you move a mark in one,
# move it in the other, or the figure stops proving anything.
#
# The strict marks are also, deliberately, the marks already on
# `07_Concepts/img/ballot_panel_ranking.png`. Same cast, same paper, same
# bubbles — so the strict ballot is the ranked ballot the reader has already
# seen, and the weak one differs from it by exactly one mark (Ella, 5th -> 4th).
STRICT_RANKS = [0, 3, 1, 2, 4]   # Andre 1st, Blake 4th, Carmen 2nd, David 3rd, Ella 5th
WEAK_RANKS = [0, 3, 1, 2, 3]     # …Ella joins Blake at 4th; the 5th column empties

STRICT_INSTRUCTION = "Rank the candidates. One candidate per column — no ties."
WEAK_INSTRUCTION = "Rank the candidates. Two candidates may share a rank."


class RankedBallot(NamedTuple):
    """One ranked ballot: who is on it, where they were marked, and where it lands."""

    title: str
    cast: list[str]
    # Column index per candidate, 0-based (0 = 1st place). None = row left blank,
    # which is a truncated ballot, not a last place — so it draws as no mark.
    ranks: list[int | None]
    out_dir: Path
    instruction: str = ""
    # Pre-wrapped by the author, one string per printed line, so the art is
    # deterministic and a bad line break is fixable by hand.
    footer: tuple[str, ...] = ()
    # Rows whose mark is drawn in rust rather than black: the ballot's own way of
    # saying "these two are the problem". Used only by the overvote figure — an
    # ordinary ballot has no opinion about its own marks.
    flagged: tuple[int, ...] = ()


BALLOTS: dict[str, RankedBallot] = {
    "ranks_strict": RankedBallot(
        "Strict ranks — every candidate a different place",
        CANDIDATES,
        STRICT_RANKS,
        IMG_DIR,
        instruction=STRICT_INSTRUCTION,
        footer=(
            "This voter thinks Blake and Ella are equally last. The ballot made",
            "them pick an order anyway — “is she my 4th or my 5th?”",
        ),
    ),
    "ranks_weak": RankedBallot(
        "Weak ranks — equal ranks allowed",
        CANDIDATES,
        WEAK_RANKS,
        IMG_DIR,
        instruction=WEAK_INSTRUCTION,
        footer=(
            "Blake and Ella share 4th, so nobody is 5th. One mark moved, and the",
            "ballot now says what the voter actually thinks.",
        ),
    ),
    "ranks_strict_overvote": RankedBallot(
        "The same marks on a strict ballot — an overvote",
        CANDIDATES,
        WEAK_RANKS,
        IMG_DIR,
        instruction=STRICT_INSTRUCTION,
        footer=(
            "Two candidates marked 4th. A strict ballot has no way to read that,",
            "so the rank is an overvote — and may spoil the ballot from there on.",
        ),
        flagged=(1, 4),  # Blake and Ella, the two sharing 4th
    ),
}


# --------------------------------------------------------------------------- #
# Geometry
# --------------------------------------------------------------------------- #
# Wider than the Approval ballot, narrower than the 0–5 grid: five rank columns
# sit between two and six. Column spacing and the 58 px right margin are the 0–5
# ballot's, so the two pieces of paper look like they came off the same press.
RANK_COL_DX = 210
RANK_RIGHT_PAD = 100
BUBBLE_RX, BUBBLE_RY = 42, 36
COLUMN_HDR_SIZE = 54
NAME_SIZE = 62
NUMERAL_SIZE = 44
INSTRUCTION_SIZE = 42

# Ordinal labels, one per rank column. Five candidates is as wide as this art
# goes; beyond that a ballot wants a different drawing, not a longer list.
ORDINALS = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")


def columns_for(ballot: RankedBallot) -> int:
    """How many rank columns the paper prints — one per candidate.

    A real ranked ballot sometimes prints fewer columns than candidates (that is
    truncation-by-design, e.g. "rank up to 3"), but none of these figures do, and
    a column count that quietly disagreed with the cast would make the empty 5th
    column of the weak ballot ambiguous — the reader could not tell a tie from a
    column that was never offered.
    """
    return len(ballot.cast)


def canvas_width(ballot: RankedBallot) -> int:
    return NAME_X + RANK_RIGHT_PAD + RANK_COL_DX * columns_for(ballot) + 340


def col0_x(ballot: RankedBallot) -> float:
    return canvas_width(ballot) - RANK_RIGHT_PAD - RANK_COL_DX * (columns_for(ballot) - 1)


def col_x(ballot: RankedBallot, i: int) -> float:
    return col0_x(ballot) + i * RANK_COL_DX


def height_for(ballot: RankedBallot) -> int:
    footer_h = FTR_GAP + len(ballot.footer) * FTR_LINE_H if ballot.footer else 0
    return GRID_TOP + len(ballot.cast) * ROW_H + footer_h + BOTTOM_PAD


def alt_text(ballot: RankedBallot) -> str:
    """Describe the marks for a screen reader — pasted into the page's <img alt>."""
    marks = [
        f"{name} {ORDINALS[rank]}" if rank is not None else f"{name} left unranked"
        for name, rank in zip(ballot.cast, ballot.ranks)
    ]
    shared = [
        ORDINALS[r]
        for r in sorted({x for x in ballot.ranks if x is not None})
        if ballot.ranks.count(r) > 1
    ]
    tail = f" {' and '.join(shared)} is marked twice." if shared else ""
    return (
        f"A ranked ballot with columns 1st through {ORDINALS[columns_for(ballot) - 1]} "
        f"— {ballot.title}: " + ", ".join(marks) + f".{tail}"
    )


def render_svg(ballot: RankedBallot) -> str:
    width, H = canvas_width(ballot), height_for(ballot)
    n_cols = columns_for(ballot)
    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {H}" '
        f'width="{width}" height="{H}">',
        f'<rect width="{width}" height="{H}" fill="#FFFFFF"/>',
        f'<text x="{TITLE_X}" y="{TITLE_Y}" font-family="{FONT}" '
        f'font-size="{title_font_size(ballot.title, width)}" font-weight="bold" '
        f'fill="{RUST}">{esc(ballot.title)}</text>',
    ]
    if ballot.instruction:
        out.append(
            f'<text x="{TITLE_X}" y="{INSTRUCTION_Y}" font-family="{BODY_FONT}" '
            f'font-size="{INSTRUCTION_SIZE}" fill="{INK}">'
            f'{esc(ballot.instruction)}</text>'
        )

    for i in range(n_cols):
        out.append(
            f'<text x="{col_x(ballot, i)}" y="{COLUMN_HDR_Y}" font-family="{FONT}" '
            f'font-size="{COLUMN_HDR_SIZE}" font-weight="bold" fill="{INK}" '
            f'text-anchor="middle">{ORDINALS[i]}</text>'
        )

    for r, name in enumerate(ballot.cast):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            out.append(
                f'<rect x="0" y="{top}" width="{width}" height="{ROW_H}" fill="{ROW_TINT}"/>'
            )
        out.append(
            f'<line x1="0" y1="{top}" x2="{width}" y2="{top}" stroke="{RULE}" stroke-width="7"/>'
        )
        out.append(
            f'<text x="{NAME_X}" y="{mid + 22}" font-family="{FONT}" '
            f'font-size="{NAME_SIZE}" font-weight="bold" fill="{INK}">{esc(name)}</text>'
        )
        marked = ballot.ranks[r]
        fill = RUST if r in ballot.flagged else INK
        for i in range(n_cols):
            cx = col_x(ballot, i)
            if marked is not None and i == marked:
                out.append(
                    f'<ellipse cx="{cx}" cy="{mid}" rx="{BUBBLE_RX}" ry="{BUBBLE_RY}" '
                    f'fill="{fill}"/>'
                )
            else:
                out.append(
                    f'<ellipse cx="{cx}" cy="{mid}" rx="{BUBBLE_RX}" ry="{BUBBLE_RY}" '
                    f'fill="#FFFFFF" stroke="{BUBBLE_STROKE}" stroke-width="5"/>'
                )
                out.append(
                    f'<text x="{cx}" y="{mid + 16}" font-family="{FONT}" '
                    f'font-size="{NUMERAL_SIZE}" font-weight="bold" fill="{INK}" '
                    f'text-anchor="middle">{i + 1}</text>'
                )

    bottom = GRID_TOP + len(ballot.cast) * ROW_H
    out.append(
        f'<line x1="0" y1="{bottom}" x2="{width}" y2="{bottom}" stroke="{RULE}" stroke-width="7"/>'
    )
    for n, line in enumerate(ballot.footer):
        out.append(
            f'<text x="{TITLE_X}" y="{bottom + FTR_GAP + n * FTR_LINE_H}" '
            f'font-family="{BODY_FONT}" font-size="{FTR_SIZE}" '
            f'fill="{INK}">{esc(line)}</text>'
        )
    out.append("</svg>")
    return "\n".join(out)


def rasterize(ballot: RankedBallot, png_path: Path) -> None:
    """Draw the ballot straight to a bitmap, mirroring render_svg's geometry."""
    from PIL import Image, ImageDraw

    def s(v: float) -> float:
        return v * SS

    width, H = canvas_width(ballot), height_for(ballot)
    n_cols = columns_for(ballot)
    img = Image.new("RGB", (width * SS, H * SS), "#FFFFFF")
    d = ImageDraw.Draw(img)
    f_title = art._font(title_font_size(ballot.title, width) * SS)
    f_hdr, f_name = art._font(COLUMN_HDR_SIZE * SS), art._font(NAME_SIZE * SS)
    f_numeral = art._font(NUMERAL_SIZE * SS)

    d.text((s(TITLE_X), s(TITLE_Y)), ballot.title, font=f_title, fill=RUST, anchor="ls")
    if ballot.instruction:
        d.text((s(TITLE_X), s(INSTRUCTION_Y)), ballot.instruction,
               font=art._font(INSTRUCTION_SIZE * SS, body=True), fill=INK, anchor="ls")

    for i in range(n_cols):
        d.text((s(col_x(ballot, i)), s(COLUMN_HDR_Y)), ORDINALS[i],
               font=f_hdr, fill=INK, anchor="ms")

    for r, name in enumerate(ballot.cast):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            d.rectangle([0, s(top), s(width), s(top + ROW_H)], fill=ROW_TINT)
        d.line([0, s(top), s(width), s(top)], fill=RULE, width=int(s(7)))
        d.text((s(NAME_X), s(mid + 22)), name, font=f_name, fill=INK, anchor="ls")
        marked = ballot.ranks[r]
        fill = RUST if r in ballot.flagged else INK
        for i in range(n_cols):
            cx = col_x(ballot, i)
            box = [s(cx - BUBBLE_RX), s(mid - BUBBLE_RY),
                   s(cx + BUBBLE_RX), s(mid + BUBBLE_RY)]
            if marked is not None and i == marked:
                d.ellipse(box, fill=fill)
            else:
                d.ellipse(box, fill="#FFFFFF", outline=BUBBLE_STROKE, width=int(s(5)))
                d.text((s(cx), s(mid + 16)), str(i + 1),
                       font=f_numeral, fill=INK, anchor="ms")

    bottom = GRID_TOP + len(ballot.cast) * ROW_H
    d.line([0, s(bottom), s(width), s(bottom)], fill=RULE, width=int(s(7)))
    f_ftr = art._font(FTR_SIZE * SS, body=True)
    for n, line in enumerate(ballot.footer):
        d.text((s(TITLE_X), s(bottom + FTR_GAP + n * FTR_LINE_H)), line,
               font=f_ftr, fill=INK, anchor="ls")
    art._save_png(img, width, H, png_path)


def _write(slug: str, ballot: RankedBallot, want_png: bool) -> None:
    ballot.out_dir.mkdir(parents=True, exist_ok=True)
    svg_path = ballot.out_dir / f"{slug}.svg"
    svg_path.write_text(render_svg(ballot))
    print(f"wrote {art._show(svg_path)}")
    if want_png:
        png_path = ballot.out_dir / f"{slug}.png"
        rasterize(ballot, png_path)
        print(f"wrote {art._show(png_path)}")
    print(f"  alt: {alt_text(ballot)}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--svg-only", action="store_true", help="write .svg but skip the .png")
    ap.add_argument("--only", help="render just this slug (e.g. ranks_weak)")
    args = ap.parse_args()

    if args.only and args.only not in BALLOTS:
        print(f"! unknown slug {args.only!r}; known: {', '.join(BALLOTS)}", file=sys.stderr)
        return 2

    want_png = not args.svg_only
    if want_png:
        try:
            import PIL  # noqa: F401
        except ImportError:
            print("! Pillow not installed -- writing SVG only", file=sys.stderr)
            want_png = False

    for slug, ballot in BALLOTS.items():
        if args.only and slug != args.only:
            continue
        _write(slug, ballot, want_png)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
