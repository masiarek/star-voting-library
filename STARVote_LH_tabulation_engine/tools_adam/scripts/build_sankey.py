#!/usr/bin/env python3
"""Draw an RCV-IRV round-by-round Sankey for a ranked case, into the repo.

WHY THIS EXISTS. Our engine prints rounds as columns of numbers, and a column of
numbers cannot show where a transferred vote came FROM — which is the subject of
every page here that argues about center squeeze or exhausted ballots. Third-party
visualizers draw it (RCVis, RCV Lab), but the art then lives on someone else's
domain: it disappears when they do, it cannot be committed, and RCVis is GPL-3 so
its code cannot be vendored into this MIT repo. This draws the same picture from
our own numbers, and the result is a file in the tree.

    python3 build_sankey.py 06_Other/RCV_IRV/cases/some_case.yaml
    python3 build_sankey.py --refresh          # redraw every case that has art
    python3 build_sankey.py case.yaml --svg-only

Art lands beside the case as `<yaml dir>/img/<stem>_sankey.png` (+ `.svg`), the
same convention as the ballot art: the PNG is what pages embed, the SVG is kept
so the drawing stays editable. Which cases get one is editorial — `--refresh`
only redraws cases that already have art, so nothing appears uninvited.

INPUT IS UNIVERSAL RCV TABULATOR JSON, not the YAML directly. A `.yaml` is run
through `ut_json_export.py` first (which is where the transfers are recomputed
from the ballots), so this file does no tabulating of its own and a `.json` from
RCTab — or from anywhere else speaking that format — draws just as well.

ONE GEOMETRY PASS, TWO BACKENDS. Ribbons are cubic beziers, and writing that
drawing twice (once as SVG paths, once in Pillow) is how the two renderings drift
apart. Instead the layout emits primitives — rects, polygons, texts — which a thin
SVG writer and a thin Pillow writer each consume. The bezier is flattened to a
point list ONCE and both backends draw the same polygon.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
_EXPORTER = (REPO_ROOT / "STARVote_LH_tabulation_engine" / "tools_adam"
             / "rctab_tabulation_engine" / "ut_json_export.py")

# Qualitative palette: distinguishable in common forms of colour blindness, and
# still separable when printed grey. Inactive ballots are deliberately outside it.
PALETTE = ["#4477AA", "#EE6677", "#228833", "#CCBB44", "#66CCEE",
           "#AA3377", "#BBBBBB", "#EE9944", "#009988", "#882255"]
INACTIVE = "#C8C8C8"
INK = "#222222"
MUTED = "#767676"
BG = "#FFFFFF"

# The canvas GROWS with the election. A fixed 1600x900 is right for the small
# teaching cases this library prefers, and unreadable at Minneapolis 2017's 18
# candidates over 15 rounds -- names clipped off the left edge, round labels
# printed on top of each other. Everything below is derived per case instead.
BASE_W, BASE_H = 1600, 900
PAD_R = 230                   # final tallies
PAD_T, PAD_B = 96, 54
NODE_W = 22                   # width of a round's candidate bar
GAP = 16                      # vertical gap between stacked nodes
RIBBON_STEPS = 48             # bezier flattening resolution
MIN_LABEL_H = 15              # below this a node is too thin to letter legibly


# --------------------------------------------------------------------------- #
# primitives — what the layout emits and each backend consumes
# --------------------------------------------------------------------------- #

class Scene:
    def __init__(self):
        self.items: list[tuple] = []

    def rect(self, x, y, w, h, fill):
        self.items.append(("rect", x, y, w, h, fill))

    def poly(self, pts, fill, opacity=1.0):
        self.items.append(("poly", pts, fill, opacity))

    def text(self, x, y, s, size=20, anchor="start", fill=INK, weight="normal"):
        self.items.append(("text", x, y, s, size, anchor, fill, weight))

    def line(self, pts, stroke, width=3.0):
        self.items.append(("line", pts, stroke, width))

    # ✓ and ✗ are DRAWN, not typed. As text they depend on the rasterizer finding
    # a font that carries them, and Pillow's default does not — they came out as
    # empty boxes in the PNG while looking perfect in the SVG.
    def mark_x(self, cx, cy, r=7, stroke="#CC3311"):
        self.line([(cx - r, cy - r), (cx + r, cy + r)], stroke, 3.0)
        self.line([(cx + r, cy - r), (cx - r, cy + r)], stroke, 3.0)

    def mark_check(self, cx, cy, r=8, stroke="#228833"):
        self.line([(cx - r, cy), (cx - r * 0.2, cy + r * 0.7),
                   (cx + r, cy - r * 0.8)], stroke, 3.4)


def load_ut(path: Path) -> dict:
    """Universal RCV Tabulator JSON, from a .json or via the YAML exporter."""
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    spec = importlib.util.spec_from_file_location("ut_json_export", _EXPORTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    title, ballots = mod.load_case(str(path))
    return {"config": {"contest": title}, "results": mod.tabulate(ballots)}


def build_flows(data: dict):
    """(rounds, order, flows) — rounds[r][name] = votes, flows[r] = [(a,b,v)].

    An `Inactive` pseudo-candidate accumulates exhausted ballots so every column
    sums to the same total; without it the columns shrink and the ribbons lie
    about how much of the electorate is still deciding.
    """
    res = data["results"]
    rounds = [{k: float(v) for k, v in r["tally"].items()} for r in res]

    total = sum(rounds[0].values())
    exhausted_so_far = 0.0
    flows: list[list[tuple[str, str, float]]] = []

    for r, entry in enumerate(res[:-1]):
        f: list[tuple[str, str, float]] = []
        eliminated = {t["eliminated"]: t.get("transfers", {})
                      for t in entry.get("tallyResults", []) if "eliminated" in t}
        # survivors carry their whole pile forward
        for c, v in rounds[r].items():
            if c not in eliminated and c in rounds[r + 1]:
                f.append((c, c, v))
        # eliminated candidates fan out
        newly_exhausted = 0.0
        for e, transfers in eliminated.items():
            for dest, amt in transfers.items():
                amt = float(amt)
                if not amt:
                    continue
                if dest == "exhausted":
                    newly_exhausted += amt
                    f.append((e, "Inactive", amt))
                else:
                    f.append((e, dest, amt))
        if exhausted_so_far:
            f.append(("Inactive", "Inactive", exhausted_so_far))
        exhausted_so_far += newly_exhausted
        flows.append(f)
        if exhausted_so_far:
            rounds[r + 1]["Inactive"] = exhausted_so_far

    # stable draw order: round-1 strength, Inactive pinned last
    order = sorted(rounds[0], key=lambda c: -rounds[0][c])
    for rd in rounds:
        for c in rd:
            if c not in order and c != "Inactive":
                order.append(c)
    order.append("Inactive")
    return rounds, order, flows, total


def layout(data: dict) -> tuple[Scene, int, int]:
    rounds, order, flows, total = build_flows(data)
    n = len(rounds)

    # size the canvas to the election, not the other way round
    names = [c for c in order if c != "Inactive"]
    PAD_L = max(250, int(11.2 * max((len(c) for c in names), default=10)) + 70)
    W = max(BASE_W, PAD_L + PAD_R + 118 * n)
    H = max(BASE_H, 62 * len(names) + PAD_T + PAD_B + 90)

    sc = Scene()
    sc.rect(0, 0, W, H, BG)

    contest = data.get("config", {}).get("contest", "")
    sc.text(PAD_L - 40, 44, contest[:96], size=27, weight="bold")

    colour = {c: (INACTIVE if c == "Inactive" else PALETTE[i % len(PALETTE)])
              for i, c in enumerate([c for c in order if c != "Inactive"])}
    colour["Inactive"] = INACTIVE

    plot_h = H - PAD_T - PAD_B
    span = (W - PAD_L - PAD_R - NODE_W) / max(n - 1, 1)
    scale = (plot_h - GAP * max(len([c for c in order if c in rounds[0]]) - 1, 1)) / total

    # node boxes, per round
    box: list[dict[str, tuple[float, float]]] = []   # name -> (top, height)
    for r, rd in enumerate(rounds):
        present = [c for c in order if c in rd and rd[c] > 0]
        heights = {c: rd[c] * scale for c in present}
        free = plot_h - sum(heights.values())
        gap = free / max(len(present) - 1, 1) if len(present) > 1 else 0
        gap = min(gap, GAP * 2.5)
        used = sum(heights.values()) + gap * max(len(present) - 1, 0)
        y = PAD_T + (plot_h - used) / 2
        b = {}
        for c in present:
            b[c] = (y, heights[c])
            y += heights[c] + gap
        box.append(b)

        x = PAD_L + r * span
        # with many rounds the labels collide; thin them out rather than shrink
        # them into illegibility. First and last always survive.
        every = 1 if span > 96 else (2 if span > 56 else 3)
        if r % every == 0 or r == n - 1:
            sc.text(x + NODE_W / 2, PAD_T - 30, f"Round {r + 1}",
                    size=20, anchor="middle", fill=MUTED)

    # ribbons first, so the node bars sit on top of them
    for r, f in enumerate(flows):
        x0 = PAD_L + r * span + NODE_W
        x1 = PAD_L + (r + 1) * span
        out_cur = {c: box[r][c][0] for c in box[r]}
        in_cur = {c: box[r + 1][c][0] for c in box[r + 1]}
        # draw each source's outgoing flows in the destination's draw order, so
        # ribbons from one node leave in the same order they arrive: no crossings
        # that the data does not actually contain.
        for src in [c for c in order if c in box[r]]:
            outs = [(a, b, v) for (a, b, v) in f if a == src]
            outs.sort(key=lambda t: order.index(t[1]) if t[1] in order else 99)
            for _, dst, v in outs:
                if dst not in box[r + 1] or v <= 0:
                    continue
                h = v * scale
                y0, y1 = out_cur[src], in_cur[dst]
                pts = ribbon(x0, y0, x1, y1, h)
                fade = 0.30 if src == dst else 0.55
                sc.poly(pts, colour.get(src, MUTED), fade)
                out_cur[src] += h
                in_cur[dst] += h

    # which candidates leave in which round — needed before the bars are labelled
    gone: list[set[str]] = []
    for entry in data["results"][:-1]:
        gone.append({t["eliminated"] for t in entry.get("tallyResults", [])
                     if "eliminated" in t})
    last = data["results"][-1].get("tallyResults", [])
    winner = next((t["elected"] for t in last if "elected" in t), None)

    # node bars, names and per-round tallies
    for r, rd in enumerate(rounds):
        x = PAD_L + r * span
        final = r == len(rounds) - 1
        for c, (y, h) in box[r].items():
            sc.rect(x, y, NODE_W, h, colour.get(c, MUTED))
            mid = y + h / 2
            if r == 0:
                # names clear the ✗ gutter, so an eliminated candidate's mark
                # never lands on top of their own name
                sc.text(x - 38, mid + 7, c, size=21, anchor="end")
            label = fmt(rd[c])
            if final and c == "Inactive":
                label += " inactive"
            # a hair-thin node has no room for its own number; the final column
            # is always lettered, because that is the result.
            if final or h >= MIN_LABEL_H:
                sc.text(x + NODE_W + 10, mid + (6 if final else 5), label,
                        size=21 if final else 17,
                        fill=MUTED if c == "Inactive" else INK,
                        weight="bold" if final and c != "Inactive" else "normal")
            if r < len(gone) and c in gone[r]:
                sc.mark_x(x - 17, mid)
            if final and c == winner:
                sc.mark_check(x - 17, mid)

    # NOT "N ballots": this is the round-1 active total, which excludes ballots
    # that ranked nobody. Minneapolis 2017 is 105,928 cast and 104,484 here, and
    # captioning the smaller number as turnout would be wrong on a real election.
    sc.text(PAD_L - 40, H - 18,
            f"{fmt(total)} ballots counted in round 1 · {n} rounds"
            + (f" · elected {winner}" if winner else ""),
            size=19, fill=MUTED)
    return sc, W, H


def fmt(v: float) -> str:
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v)):,}"
    return f"{v:,.2f}"


def ribbon(x0, y0, x1, y1, h):
    """Flatten the ribbon outline to a point list — shared by both backends."""
    cx = (x0 + x1) / 2

    def bez(ya, yb, steps=RIBBON_STEPS):
        pts = []
        for i in range(steps + 1):
            t = i / steps
            mt = 1 - t
            x = mt ** 3 * x0 + 3 * mt ** 2 * t * cx + 3 * mt * t ** 2 * cx + t ** 3 * x1
            y = mt ** 3 * ya + 3 * mt ** 2 * t * ya + 3 * mt * t ** 2 * yb + t ** 3 * yb
            pts.append((x, y))
        return pts

    return bez(y0, y1) + list(reversed(bez(y0 + h, y1 + h)))


# --------------------------------------------------------------------------- #
# backends
# --------------------------------------------------------------------------- #

def to_svg(sc: Scene, W: int, H: int) -> str:
    esc = lambda s: (str(s).replace("&", "&amp;").replace("<", "&lt;")
                     .replace(">", "&gt;"))
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'width="{W}" height="{H}" font-family="Helvetica,Arial,sans-serif">']
    for it in sc.items:
        if it[0] == "rect":
            _, x, y, w, h, fill = it
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" '
                       f'height="{h:.1f}" fill="{fill}"/>')
        elif it[0] == "poly":
            _, pts, fill, op = it
            d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
            out.append(f'<polygon points="{d}" fill="{fill}" fill-opacity="{op}"/>')
        elif it[0] == "line":
            _, pts, stroke, w = it
            d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
            out.append(f'<polyline points="{d}" fill="none" stroke="{stroke}" '
                       f'stroke-width="{w}" stroke-linecap="round" '
                       f'stroke-linejoin="round"/>')
        else:
            _, x, y, s, size, anchor, fill, weight = it
            out.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" '
                       f'text-anchor="{anchor}" fill="{fill}" '
                       f'font-weight="{weight}">{esc(s)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def to_png(sc: Scene, W: int, H: int, path: Path, ss: int = 2) -> bool:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    img = Image.new("RGB", (W * ss, H * ss), BG)
    d = ImageDraw.Draw(img, "RGBA")

    def font(size, bold=False):
        for name in (["Helvetica-Bold.ttc", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"]
                     if bold else ["Helvetica.ttc", "Arial.ttf", "DejaVuSans.ttf"]):
            for base in ("/System/Library/Fonts/", "/Library/Fonts/",
                         "/usr/share/fonts/truetype/dejavu/", ""):
                try:
                    return ImageFont.truetype(base + name, size * ss)
                except OSError:
                    continue
        return ImageFont.load_default()

    def rgba(hexs, op):
        hexs = hexs.lstrip("#")
        r, g, b = (int(hexs[i:i + 2], 16) for i in (0, 2, 4))
        return (r, g, b, int(round(op * 255)))

    for it in sc.items:
        if it[0] == "rect":
            _, x, y, w, h, fill = it
            d.rectangle([x * ss, y * ss, (x + w) * ss, (y + h) * ss], fill=fill)
        elif it[0] == "poly":
            _, pts, fill, op = it
            d.polygon([(x * ss, y * ss) for x, y in pts], fill=rgba(fill, op))
        elif it[0] == "line":
            _, pts, stroke, w = it
            d.line([(x * ss, y * ss) for x, y in pts], fill=stroke,
                   width=max(int(round(w * ss)), 1), joint="curve")
        else:
            _, x, y, s, size, anchor, fill, weight = it
            fnt = font(size, weight == "bold")
            anc = {"start": "ls", "middle": "ms", "end": "rs"}[anchor]
            d.text((x * ss, y * ss), str(s), font=fnt, fill=fill, anchor=anc)

    img.resize((W, H), Image.LANCZOS).save(path, optimize=True)
    return True


# --------------------------------------------------------------------------- #

def draw(src: Path, svg_only: bool = False) -> tuple[Path, bool]:
    data = load_ut(src)
    sc, W, H = layout(data)
    img_dir = src.parent / "img"
    img_dir.mkdir(exist_ok=True)
    stem = src.stem
    svg = img_dir / f"{stem}_sankey.svg"
    svg.write_text(to_svg(sc, W, H), encoding="utf-8")
    png_ok = False
    if not svg_only:
        png_ok = to_png(sc, W, H, img_dir / f"{stem}_sankey.png")
    return svg, png_ok


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cases", nargs="*", help="ranked case .yaml, or UT .json")
    ap.add_argument("--refresh", action="store_true",
                    help="redraw every case that already has sankey art")
    ap.add_argument("--svg-only", action="store_true")
    args = ap.parse_args()

    targets = [Path(c) for c in args.cases]
    if args.refresh:
        for existing in REPO_ROOT.rglob("img/*_sankey.svg"):
            stem = existing.name[: -len("_sankey.svg")]
            for cand in (existing.parent.parent / f"{stem}.yaml",):
                if cand.exists():
                    targets.append(cand)
    if not targets:
        ap.error("name a case, or pass --refresh")

    drawn = 0
    for t in sorted(set(targets)):
        try:
            svg, png_ok = draw(t, args.svg_only)
        except SystemExit as exc:            # the exporter refused it
            print(f"  skip {t.name}: {exc}", file=sys.stderr)
            continue
        drawn += 1
        print(f"  {os.path.relpath(svg, REPO_ROOT)}"
              + ("" if png_ok or args.svg_only else "   (no PNG — pip install Pillow)"))
    print(f"{drawn} sankey diagram(s) drawn.")


if __name__ == "__main__":
    main()
