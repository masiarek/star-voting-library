#!/usr/bin/env python3
"""Render the voting-style ballot thumbnails used by 01_STAR/01_Learn/voting_styles/.

The original eight `style_*.png` files were captured by hand from Adam's slides.
This script reproduces that design as SVG so new styles can be added without
going back to the deck: a title, a Worst..Best header, one row per candidate,
and six bubbles (0-5) with the marked one filled in.

    python3 build_style_ballot_images.py            # write SVG + PNG for every style
    python3 build_style_ballot_images.py --svg-only # skip rasterizing

The PNG is what the docs embed (the repo's other ballot art is PNG, and GitHub's
Markdown renderer is unreliable with relative-path SVG); the .svg is written
alongside it so the art stays editable. Rasterizing needs Pillow -- with
--svg-only, or if Pillow is missing, the .svg files are still written.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
IMG_DIR = REPO_ROOT / "01_STAR" / "01_Learn" / "voting_styles" / "img"

# The five-candidate cast used by every style thumbnail on the hub page.
CANDIDATES = ["Andre", "Blake", "Carmen", "David", "Ella"]

# Scores are 0-5; None means the row was left blank (which STAR counts as 0, but
# the ballot shows no mark at all -- that distinction is the whole point of the
# partial-ballot and null-ballot styles).
# Listed in the hub page's gallery order. Titles match the style names in that
# table on purpose: the original hand-made art disagreed with itself (some
# titles rust and left-aligned, some black and centred; "Not much of a backup"
# in sentence case against "Decent Backup" in title case), and the marks below
# are transcribed from those originals.
STYLES: dict[str, tuple[str, list[int | None]]] = {
    # slug: (title shown on the ballot, scores in CANDIDATES order)
    "style_traditional": ("Traditional", [None, None, 5, None, None]),
    "style_partial_ballot": ("Partial Ballot", [None, None, 5, 3, None]),
    "style_decent_backup": ("Decent Backup", [None, None, 5, None, 4]),
    "style_not_much_of_a_backup": ("Not Much of a Backup", [None, None, 5, None, 1]),
    "style_exaggerated_compromise": ("Exaggerated Compromise", [5, 1, 5, 2, 0]),
    "style_partisan": ("Partisan", [5, None, 5, 5, None]),
    "style_approval_style": ("Approval-style", [5, 0, 5, 5, 0]),
    "style_ranked": ("Ranked", [2, 4, 5, 3, 1]),
    "style_nuanced": ("Nuanced", [1, 4, 5, None, 4]),
    "style_compressed_middle": ("Compressed Middle", [3, 2, 3, 3, 2]),
    "style_null_ballot": ("Null Ballot", [3, 3, 3, 3, 3]),
    "style_anyone_but": ("Anyone But…", [5, None, 5, 5, 5]),
    "style_protest_vote": ("Protest Vote", [None, 1, None, None, None]),
}

# Palette sampled from the existing hand-made thumbnails.
RUST = "#C0504D"          # title
ROW_TINT = "#DCE6F1"      # alternating row background
RULE = "#95B3D7"          # horizontal rules
STAR_OUTLINE = "#A9C4D9"  # the star glyphs in the header
BUBBLE_STROKE = "#595959"
INK = "#000000"

FONT = "Arial Black, Arial Bold, Helvetica, sans-serif"

W, H = 1600, 1160
TITLE_Y = 78
HDR_WORST_Y = 168
STAR_ROW_Y = 292
GRID_TOP = 352
ROW_H = 158
COL0_X = 630           # centre of the "0" column
COL_DX = 174           # spacing between bubble columns
NAME_X = 118


def col_x(i: int) -> float:
    return COL0_X + i * COL_DX


def star_points(cx: float, cy: float, r: float) -> list[tuple[float, float]]:
    """Five-pointed star outline, point up."""
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rad = r if k % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return pts


def star_path(cx: float, cy: float, r: float) -> str:
    pts = [f"{x:.1f},{y:.1f}" for x, y in star_points(cx, cy, r)]
    return "M" + "L".join(pts) + "Z"


def render_svg(title: str, scores: list[int | None]) -> str:
    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
        f'<text x="30" y="{TITLE_Y}" font-family="{FONT}" font-size="66" font-weight="bold" '
        f'fill="{RUST}">&quot;{title}&quot;</text>',
        f'<text x="{col_x(0) + 40}" y="{HDR_WORST_Y}" font-family="{FONT}" font-size="58" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle">Worst</text>',
        f'<text x="{col_x(5)}" y="{HDR_WORST_Y}" font-family="{FONT}" font-size="58" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle">Best</text>',
    ]

    # Header scale: 0 is a bare numeral, 1-5 sit inside a star outline.
    for i in range(6):
        cx = col_x(i)
        if i:
            out.append(
                f'<path d="{star_path(cx, STAR_ROW_Y - 18, 62)}" fill="none" '
                f'stroke="{STAR_OUTLINE}" stroke-width="6" stroke-linejoin="round"/>'
            )
        out.append(
            f'<text x="{cx}" y="{STAR_ROW_Y}" font-family="{FONT}" font-size="60" '
            f'font-weight="bold" fill="{INK}" text-anchor="middle">{i}</text>'
        )

    for r, name in enumerate(CANDIDATES):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            out.append(f'<rect x="0" y="{top}" width="{W}" height="{ROW_H}" fill="{ROW_TINT}"/>')
        out.append(
            f'<line x1="0" y1="{top}" x2="{W}" y2="{top}" stroke="{RULE}" stroke-width="7"/>'
        )
        out.append(
            f'<text x="{NAME_X}" y="{mid + 22}" font-family="{FONT}" font-size="62" '
            f'font-weight="bold" fill="{INK}">{name}</text>'
        )
        marked = scores[r]
        for i in range(6):
            cx = col_x(i)
            if marked is not None and i == marked:
                out.append(f'<ellipse cx="{cx}" cy="{mid}" rx="42" ry="36" fill="{INK}"/>')
            else:
                out.append(
                    f'<ellipse cx="{cx}" cy="{mid}" rx="42" ry="36" fill="#FFFFFF" '
                    f'stroke="{BUBBLE_STROKE}" stroke-width="5"/>'
                )
                out.append(
                    f'<text x="{cx}" y="{mid + 16}" font-family="{FONT}" font-size="44" '
                    f'font-weight="bold" fill="{INK}" text-anchor="middle">{i}</text>'
                )
    bottom = GRID_TOP + len(CANDIDATES) * ROW_H
    out.append(f'<line x1="0" y1="{bottom}" x2="{W}" y2="{bottom}" stroke="{RULE}" stroke-width="7"/>')
    out.append("</svg>")
    return "\n".join(out)


# Heavy grotesque, to match the slide art the original eight were captured from.
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
SS = 2  # supersampling factor: draw big, downscale -> antialiased edges


def _font(size: int):
    from PIL import ImageFont

    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def rasterize(title: str, scores: list[int | None], png_path: Path) -> None:
    """Draw the ballot straight to a bitmap, mirroring render_svg's geometry."""
    from PIL import Image, ImageDraw

    def s(v: float) -> float:
        return v * SS

    img = Image.new("RGB", (W * SS, H * SS), "#FFFFFF")
    d = ImageDraw.Draw(img)
    f_title, f_hdr, f_scale = _font(66 * SS), _font(58 * SS), _font(60 * SS)
    f_name, f_bubble = _font(62 * SS), _font(44 * SS)

    d.text((s(30), s(TITLE_Y)), f'"{title}"', font=f_title, fill=RUST, anchor="ls")
    d.text((s(col_x(0) + 40), s(HDR_WORST_Y)), "Worst", font=f_hdr, fill=INK, anchor="ms")
    d.text((s(col_x(5)), s(HDR_WORST_Y)), "Best", font=f_hdr, fill=INK, anchor="ms")

    for i in range(6):
        cx = col_x(i)
        if i:
            pts = [(s(x), s(y)) for x, y in star_points(cx, STAR_ROW_Y - 18, 62)]
            d.polygon(pts, outline=STAR_OUTLINE, width=int(s(6)))
        d.text((s(cx), s(STAR_ROW_Y)), str(i), font=f_scale, fill=INK, anchor="ms")

    for r, name in enumerate(CANDIDATES):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            d.rectangle([0, s(top), s(W), s(top + ROW_H)], fill=ROW_TINT)
        d.line([0, s(top), s(W), s(top)], fill=RULE, width=int(s(7)))
        d.text((s(NAME_X), s(mid + 22)), name, font=f_name, fill=INK, anchor="ls")
        marked = scores[r]
        for i in range(6):
            cx = col_x(i)
            box = [s(cx - 42), s(mid - 36), s(cx + 42), s(mid + 36)]
            if marked is not None and i == marked:
                d.ellipse(box, fill=INK)
            else:
                d.ellipse(box, fill="#FFFFFF", outline=BUBBLE_STROKE, width=int(s(5)))
                d.text((s(cx), s(mid + 16)), str(i), font=f_bubble, fill=INK, anchor="ms")

    bottom = GRID_TOP + len(CANDIDATES) * ROW_H
    d.line([0, s(bottom), s(W), s(bottom)], fill=RULE, width=int(s(7)))

    img.resize((W, H), Image.LANCZOS).save(png_path, optimize=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--svg-only", action="store_true", help="write .svg but skip the .png")
    ap.add_argument("--only", help="render just this slug (e.g. style_null_ballot)")
    args = ap.parse_args()

    want_png = not args.svg_only
    if want_png:
        try:
            import PIL  # noqa: F401
        except ImportError:
            print("! Pillow not installed -- writing SVG only", file=sys.stderr)
            want_png = False

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    for slug, (title, scores) in STYLES.items():
        if args.only and slug != args.only:
            continue
        svg_path = IMG_DIR / f"{slug}.svg"
        svg_path.write_text(render_svg(title, scores))
        print(f"wrote {svg_path.relative_to(REPO_ROOT)}")
        if want_png:
            png_path = IMG_DIR / f"{slug}.png"
            rasterize(title, scores, png_path)
            print(f"wrote {png_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
