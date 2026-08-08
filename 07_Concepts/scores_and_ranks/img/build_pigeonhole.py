# /// script
# requires-python = ">=3.10"
# ///
"""build_pigeonhole.py — draw what nine candidates do to a six-rung ballot.

The picture for 07_Concepts/scores_and_ranks/ballot_expressiveness_measured.md. It is
NOT invented: it draws one real voter from
method_comparisons/ballot_expressiveness/cases/bv2280_37yf8x_star.yaml — the
voter standing at +0.20 on that folder's spectrum — with their true opinion on the left
and the 0-5 ballot they are actually able to fill in on the right.

That voter holds nine distinct opinions and can write down six. The six preferences the
paper cannot carry are the red brackets.

Usage:  uv run 07_Concepts/scores_and_ranks/img/build_pigeonhole.py
"""
from pathlib import Path

# --- the real voter, from the case file ------------------------------------
NAMES = ["Ada", "Ben", "Cleo", "Dev", "Emma", "Finn", "Gus", "Hugo", "Iris"]
CAND = [-0.7269, -0.3746, -0.1827, -0.1650, -0.1137, 0.2417, 0.4095, 0.8009, 0.8421]
VOTER = 0.2007

W, H = 1600, 1010
INK = "#000000"
TITLE = "#C0504D"
BAND = "#DCE6F1"
EDGE = "#95B3D7"
LOST = "#C0504D"
BLACK_FONT = "Arial Black, Arial Bold, Helvetica, sans-serif"
BODY_FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"


def utilities():
    return [-abs(VOTER - c) for c in CAND]


def scores():
    u = utilities()
    lo, hi = min(u), max(u)
    return [round(5 * (x - lo) / (hi - lo)) for x in u]


def main():
    u = utilities()
    s = scores()
    order = sorted(range(9), key=lambda i: -u[i])          # true strict ranking

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'width="{W}" height="{H}">',
           f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>']

    def text(x, y, t, size=30, font=BODY_FONT, fill=INK, anchor="start", weight=None):
        w = f' font-weight="{weight}"' if weight else ""
        out.append(f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
                   f'fill="{fill}" text-anchor="{anchor}"{w}>{t}</text>')

    text(40, 62, "Nine candidates, six rungs", 48, BLACK_FONT, TITLE, weight="bold")
    text(40, 112, "One real voter from the ballot-expressiveness case. They hold nine "
                  "distinct opinions and can write down six.", 28)

    # ---- left panel: the true ranking --------------------------------------
    LX, TOP, ROW = 40, 190, 82
    text(LX, TOP - 42, "What the voter thinks", 30, BLACK_FONT, weight="bold")
    text(LX, TOP - 12, "nine candidates, nine distinct places", 25, fill="#555555")
    for slot, i in enumerate(order):
        y = TOP + 20 + slot * ROW
        out.append(f'<rect x="{LX}" y="{y}" width="440" height="{ROW - 10}" '
                   f'fill="{BAND}" stroke="{EDGE}" stroke-width="3"/>')
        text(LX + 22, y + 48, f"{slot + 1}.", 30, BLACK_FONT, "#7F7F7F", weight="bold")
        text(LX + 95, y + 48, NAMES[i], 34, BLACK_FONT, weight="bold")

    # ---- right panel: the 0-5 ballot ---------------------------------------
    # Geometry note: the "lost" label sits to the RIGHT of the red bracket, so the
    # panel has to be wide enough for the widest rung (three names) plus the label.
    # Get this wrong and the label prints straight through the third name.
    RX, PANEL, STEP = 580, 960, 200
    text(RX, TOP - 42, "What a 0–5 ballot can hold", 30, BLACK_FONT, weight="bold")
    text(RX, TOP - 12, "six rungs, so at least three pairs must collide", 25, fill="#555555")

    rung_h = int(9 * ROW / 6)
    for k, rung in enumerate([5, 4, 3, 2, 1, 0]):
        y = TOP + 20 + k * rung_h
        here = [i for i in order if s[i] == rung]
        out.append(f'<rect x="{RX}" y="{y}" width="{PANEL}" height="{rung_h - 10}" '
                   f'fill="{BAND if here else "#F2F2F2"}" stroke="{EDGE}" '
                   f'stroke-width="3"/>')
        text(RX + 26, y + rung_h / 2 + 12, str(rung), 40, BLACK_FONT,
             INK if here else "#BFBFBF", weight="bold")
        for n, i in enumerate(here):
            text(RX + 100 + n * STEP, y + rung_h / 2 + 12, NAMES[i], 32, BLACK_FONT,
                 weight="bold")
        if len(here) > 1:
            pairs = len(here) * (len(here) - 1) // 2
            out.append(f'<rect x="{RX + 86}" y="{y + 12}" '
                       f'width="{len(here) * STEP - 30}" height="{rung_h - 34}" '
                       f'fill="none" stroke="{LOST}" stroke-width="5" rx="12"/>')
            text(RX + PANEL - 24, y + rung_h / 2 + 10, f"{pairs} pairs lost", 26,
                 BODY_FONT, LOST, anchor="end")

    lost = sum(len([i for i in order if s[i] == r]) * (len([i for i in order if s[i] == r]) - 1) // 2
               for r in range(6))
    text(40, H - 46,
         f"This voter's ballot cannot separate {lost} of the 36 candidate pairs. "
         f"The pigeonhole forces only 3 of them —", 28)
    text(40, H - 14, "the other "
         f"{lost - 3} are ordinary rounding. Neither costs this election its "
         "winner, but at a bigger field they start to.", 28)

    out.append("</svg>")
    here = Path(__file__).resolve().parent
    (here / "pigeonhole_nine_into_six.svg").write_text("\n".join(out))
    print(f"wrote {here / 'pigeonhole_nine_into_six.svg'}  ({lost} tied pairs)")


if __name__ == "__main__":
    main()
