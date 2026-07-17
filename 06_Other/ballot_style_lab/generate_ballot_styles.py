#!/usr/bin/env python3
"""Ballot-style lab — seeded generator of random-but-HUMAN electorates.

The idea (Adam's): random ballots make good stress fixtures, but pure uniform
noise looks like no electorate on Earth. So this generator follows the repo's
own methodology page (00_start_here/topics/simulate_utilities_not_ballots.md):

    layer 1 — OPINION:    sample each voter's utilities from a faction model
                          (slants/bias + personal noise, a few true-noise voters)
    layer 2 — EXPRESSION: render those utilities through a BALLOT STYLE — the
                          legal styles from the style gallery
                          (00_start_here/STAR_Voting/STAR_ballot_voting_styles.md)
                          plus deliberately compressed ranges (all-zeros-plus-0..2
                          "harsh graders", 3..5-only "gentle souls", 0-or-3..5
                          "cliff" voters, etc.)

Same opinion, different ballot styles — rendered at electorate scale. Per the
methodology page this sits squarely in the "stress-test a tabulator" job (not a
welfare comparison), but with human-shaped ballots instead of die rolls.

Modes:
    --hunt SCEN[,SCEN,...]|all [--seeds N]   try N seeds per scenario, tabulate
        each with the real LH engine, score "interestingness" (runoff reversals,
        Condorcet cycles, center-squeeze signatures, ties, photo finishes,
        Equal-Support blowouts) and print the champions.
    --emit SCEN|all   write the frozen-seed YAML case file(s) next to this
        script (refuses if a scenario's seed is not frozen yet).
    --list   show the scenario menu.

Stdlib only. Reproducible: every emitted file records its scenario + seed.
"""

import argparse
import concurrent.futures
import random
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent
REPO_ROOT = LAB_DIR.parents[1]
ENGINE = REPO_ROOT / "STARVote_LH_tabulation_engine" / "starvote_larry_hastings.py"
VENV_PY = REPO_ROOT / ".venv" / "bin" / "python"
PYTHON = str(VENV_PY) if VENV_PY.exists() else sys.executable

MAX_SCORE = 5


# ---------------------------------------------------------------------------
# Layer 2 — expression styles: utilities (0..1 floats) -> 0..5 scores.
# Names follow the style-gallery page where a gallery style exists.
# ---------------------------------------------------------------------------

def _half_up(x):
    return int(x + 0.5)


def _norm(utils):
    lo, hi = min(utils), max(utils)
    span = hi - lo
    if span < 1e-9:
        return [0.5] * len(utils)
    return [(u - lo) / span for u in utils]


def _argmax(utils, rng):
    best = max(utils)
    return rng.choice([i for i, u in enumerate(utils) if u == best])


def _argmin(utils, rng):
    worst = min(utils)
    return rng.choice([i for i, u in enumerate(utils) if u == worst])


def st_nuanced(utils, rng):
    """Gallery 'Nuanced': honest min-max onto the full 0-5 range, ties kept."""
    return [_half_up(nu * 5) for nu in _norm(utils)]


def st_bullet(utils, rng):
    """Gallery 'Traditional (choose-one)': 5 for the favorite, nothing else."""
    scores = [0] * len(utils)
    scores[_argmax(utils, rng)] = 5
    return scores


def st_strong_backup(utils, rng):
    """Gallery 'Strong backup': favorite 5, runner-up 4, rest 0."""
    order = sorted(range(len(utils)), key=lambda i: (-utils[i], rng.random()))
    scores = [0] * len(utils)
    scores[order[0]] = 5
    if len(order) > 1:
        scores[order[1]] = 4
    return scores


def st_weak_backup(utils, rng):
    """Gallery 'Weak backup': favorite 5, a grudging 1 for the runner-up."""
    order = sorted(range(len(utils)), key=lambda i: (-utils[i], rng.random()))
    scores = [0] * len(utils)
    scores[order[0]] = 5
    if len(order) > 1:
        scores[order[1]] = 1
    return scores


def st_slate(utils, rng):
    """Gallery 'Partisan slate': 5 for everyone above the voter's bar, else 0."""
    cut = rng.uniform(0.45, 0.7)
    scores = [5 if u >= cut else 0 for u in utils]
    if 5 not in scores:
        scores[_argmax(utils, rng)] = 5
    return scores


def st_ranked_style(utils, rng):
    """Gallery 'Ranked-style': each score used once, 5 down, like a ranking."""
    order = sorted(range(len(utils)), key=lambda i: (-utils[i], rng.random()))
    scores = [0] * len(utils)
    for rank, i in enumerate(order):
        scores[i] = max(0, 5 - rank)
    return scores


def st_anyone_but(utils, rng):
    """Gallery '"Anyone but..."': 5 for everyone except the villain (0)."""
    scores = [5] * len(utils)
    scores[_argmin(utils, rng)] = 0
    return scores


def st_protest(utils, rng):
    """Gallery 'Protest / least-bad': all zeros, a lone 1 for the least bad."""
    scores = [0] * len(utils)
    scores[_argmax(utils, rng)] = 1
    return scores


def st_harsh(utils, rng):
    """Compressed LOW band: nobody deserves more than 2; zeros everywhere else."""
    return [_half_up(nu * 2) for nu in _norm(utils)]


def st_gentle(utils, rng):
    """Compressed HIGH band: can't say no — everyone gets 3..5, zeros never."""
    return [3 + _half_up(nu * 2) for nu in _norm(utils)]


def st_cliff35(utils, rng):
    """Cliff ballot: in-group rendered 3..5, everyone else 0 — nothing in 1-2."""
    cut = rng.uniform(0.45, 0.65)
    nus = _norm(utils)
    scores = [3 + _half_up(nu * 2) if u >= cut else 0
              for u, nu in zip(utils, nus)]
    if max(scores) == 0:
        scores[_argmax(utils, rng)] = 5
    return scores


def st_cliff34(utils, rng):
    """The crazy sliver: liked candidates live in 3..4 only, the rest at 0."""
    cut = rng.uniform(0.45, 0.65)
    nus = _norm(utils)
    scores = [3 + _half_up(nu * 1) if u >= cut else 0
              for u, nu in zip(utils, nus)]
    if max(scores) == 0:
        scores[_argmax(utils, rng)] = 4
    return scores


def st_flat(utils, rng):
    """Flat-liner: the same score for everyone (a legal no-preference ballot)."""
    return [rng.choice([0, 3, 3, 5])] * len(utils)


def st_chaos(utils, rng):
    """Pure noise — the fuzzing voter the methodology page blesses for
    tabulator stress; ignores utilities entirely."""
    return [rng.randint(0, 5) for _ in utils]


STYLES = {
    "nuanced": st_nuanced,
    "bullet": st_bullet,
    "strong_backup": st_strong_backup,
    "weak_backup": st_weak_backup,
    "slate": st_slate,
    "ranked_style": st_ranked_style,
    "anyone_but": st_anyone_but,
    "protest": st_protest,
    "harsh": st_harsh,
    "gentle": st_gentle,
    "cliff35": st_cliff35,
    "cliff34": st_cliff34,
    "flat": st_flat,
    "chaos": st_chaos,
}

# Styles whose zeros are often left as real-world BLANKS (a bullet voter marks
# the 5 and walks away). Blank tabulates as 0 either way; per-voter coin flip.
BLANKY_STYLES = {"bullet", "strong_backup", "weak_backup", "slate"}

STYLE_BLURB = {
    "nuanced": "full 0-5 range, honest gaps, ties allowed",
    "bullet": "choose-one transplant: favorite 5, rest 0/blank",
    "strong_backup": "5 + a strong 4 backup, rest 0/blank",
    "weak_backup": "5 + a grudging 1 backup, rest 0/blank",
    "slate": "partisan slate: equal 5s for the in-group, 0 outside",
    "ranked_style": "uses each score once, like a ranking",
    "anyone_but": "5 for everyone except the villain (0)",
    "protest": "all zeros plus a lone least-bad 1",
    "harsh": "harsh grader: everything squeezed into 0-2",
    "gentle": "gentle soul: everything squeezed into 3-5, no zeros",
    "cliff35": "cliff ballot: 0 or 3-5, nothing in between",
    "cliff34": "sliver ballot: 0 or 3-4 only",
    "flat": "flat-liner: same score for everyone",
    "chaos": "pure noise (fuzzing voter)",
}


# ---------------------------------------------------------------------------
# Layer 1 — opinion: factions -> per-voter utilities.
# ---------------------------------------------------------------------------

def sample_electorate(spec, rng):
    """Return (rows, census): rows = list of ballot cells, census = labels."""
    cast = spec["cast"]
    voters = []
    for _ in range(spec["n_ballots"] - len(spec.get("marker_rows", []))):
        r = rng.random()
        acc = 0.0
        faction = spec["factions"][-1]
        for f in spec["factions"]:
            acc += f["share"]
            if r <= acc:
                faction = f
                break
        sigma = faction.get("sigma", spec.get("sigma", 0.15))
        utils = [min(1.0, max(0.0, rng.gauss(mu, sigma))) for mu in faction["mu"]]
        style = rng.choices(list(faction["styles"]),
                            weights=list(faction["styles"].values()))[0]
        scores = STYLES[style](utils, rng)
        cells = [str(s) for s in scores]
        if style in BLANKY_STYLES and rng.random() < 0.5:
            cells = ["-" if s == 0 else str(s) for s in scores]
        if spec.get("blank_glitch") and style == "chaos":
            cells = ["-" if rng.random() < spec["blank_glitch"] else c
                     for c in cells]
        voters.append((faction["name"], style, cells))

    rng.shuffle(voters)
    rows = [cells for _, _, cells in voters]
    census = [(fname, style) for fname, style, _ in voters]

    # Marker rows (race abstention '~', spoiled '?') slip in at random spots.
    for marker in spec.get("marker_rows", []):
        pos = rng.randrange(len(rows) + 1)
        rows.insert(pos, [marker] * len(cast))
        census.insert(pos, ("markers", {"~": "race abstention",
                                        "?": "spoiled ballot"}[marker]))
    return rows, census


def format_ballots(cast, rows):
    widths = [max(len(c), 2) for c in cast]
    lines = [", ".join(cast)]
    for row in rows:
        lines.append(", ".join(cell.rjust(w) for cell, w in zip(row, widths)))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Scenarios — the electorate recipes. seed=None until a champion is frozen.
# ---------------------------------------------------------------------------

SCENARIOS = {
    "graders_divide": dict(
        seed=94,
        file_no="01", descriptor="graders-divide",
        title="The Graders' Divide — a harsh 0-2 camp meets a gentle 3-5 camp",
        cast=["Abby", "Bruno", "Clara"],
        n_ballots=31,
        factions=[
            dict(name="Abby camp", share=0.58, mu=[0.92, 0.15, 0.52],
                 sigma=0.15, styles={"harsh": 1.0}),
            dict(name="Bruno camp", share=0.42, mu=[0.12, 0.90, 0.55],
                 sigma=0.15, styles={"gentle": 1.0}),
        ],
        feature_options={"show_score_counts": True},
        intro=("Two camps, two GRADING CULTURES. The Abby camp are harsh "
               "graders: even their favorite only earns a 2, everyone else "
               "0-1. The Bruno camp are gentle souls: nobody gets less than "
               "a 3, their favorite a 5. Same kind of opinions underneath - "
               "wildly different ballots on top. The test: what do "
               "asymmetric scale habits do to the Scoring Round, and does "
               "the Automatic Runoff (which only asks WHO YOU PREFER, not "
               "how loudly you said it) keep the result sane?"),
        say=("Two departments pick a team lead. The Abby camp grades "
             "harshly - even Abby only earns a 2 from her own fans. The "
             "Bruno camp grades gently - even Abby gets a 3 from them. "
             "Watch the totals bunch together, then watch the runoff "
             "ignore the volume knob entirely."),
        why=("Scale-use asymmetry is the standard objection to score "
             "ballots; STAR's answer is the runoff. This file makes the "
             "objection concrete and lets the runoff answer it."),
    ),
    "cliff_city": dict(
        seed=123,
        file_no="02", descriptor="cliff-city",
        title="Cliff City food trucks — everyone scores 0 or 3-5, nothing between",
        cast=["Arepa", "Bao", "Churro", "Dumpling"],
        n_ballots=40,
        factions=[
            dict(name="Arepa crowd", share=0.30, mu=[0.90, 0.30, 0.55, 0.20],
                 sigma=0.15, styles={"cliff35": 0.6, "slate": 0.25, "cliff34": 0.15}),
            dict(name="Bao crowd", share=0.30, mu=[0.25, 0.90, 0.50, 0.30],
                 sigma=0.15, styles={"cliff35": 0.6, "slate": 0.25, "cliff34": 0.15}),
            dict(name="Churro crowd", share=0.25, mu=[0.30, 0.25, 0.90, 0.45],
                 sigma=0.15, styles={"cliff35": 0.6, "slate": 0.25, "cliff34": 0.15}),
            dict(name="grazers", share=0.15, mu=[0.55, 0.55, 0.55, 0.55],
                 sigma=0.25, styles={"cliff34": 0.4, "chaos": 0.2,
                                     "flat": 0.2, "anyone_but": 0.2}),
        ],
        feature_options={"show_score_counts": True},
        intro=("A whole town votes like it's Approval-with-a-volume-knob: "
               "every ballot is either 0 ('not my truck') or 3-5 ('one of "
               "mine'). Nobody uses 1 or 2 - the middle of the scale is a "
               "ghost town. Cliff ballots are the halfway house between "
               "Approval (one bit) and full STAR expressiveness; the test "
               "is what the all-or-mostly ballots do to the score "
               "distribution and how much runoff-deciding information "
               "survives the cliff."),
        say=("Four food trucks, forty voters, and not a single 1 or 2 on "
             "any ballot - you're in, or you're out. Look at the score "
             "distribution table: the middle rows are empty."),
        why=("Shows a score electorate voluntarily collapsing toward "
             "Approval - and what STAR still extracts from the 3-4-5 "
             "gradations that survive."),
    ),
    "bullet_storm": dict(
        seed=90,
        file_no="03", descriptor="bullet-storm",
        title="Bullet Storm — a bullet-voting electorate and the few who spread",
        cast=["Astrid", "Boris", "Carla", "Dolores"],
        n_ballots=33,
        factions=[
            dict(name="Astrid brigade", share=0.28, mu=[0.92, 0.20, 0.35, 0.30],
                 sigma=0.15, styles={"bullet": 0.75, "strong_backup": 0.25}),
            dict(name="Boris brigade", share=0.27, mu=[0.20, 0.92, 0.30, 0.35],
                 sigma=0.15, styles={"bullet": 0.75, "weak_backup": 0.25}),
            dict(name="Carla brigade", share=0.25, mu=[0.30, 0.25, 0.92, 0.40],
                 sigma=0.15, styles={"bullet": 0.80, "strong_backup": 0.20}),
            dict(name="the thoughtful few", share=0.20,
                 mu=[0.45, 0.40, 0.50, 0.75], sigma=0.20,
                 styles={"nuanced": 0.6, "ranked_style": 0.4}),
        ],
        feature_options={},
        intro=("Three brigades bullet-vote their champion (5 and silence - "
               "many literally leave the rest blank), while a thoughtful "
               "minority spreads honest scores. The lesson lives in the "
               "Automatic Runoff: a bullet ballot whose champion missed "
               "the top-two scored both finalists 0 - it goes EQUAL "
               "SUPPORT, silent by its own choice, and the runoff is "
               "decided by the voters who gave the count something to work "
               "with. Bullet voting is legal, counted - and self-muting."),
        say=("Everybody bullet-votes except a thoughtful few... and when "
             "the runoff comes, an entire brigade discovers their ballots "
             "say nothing about the two finalists. The nuanced folks "
             "decide it."),
        why=("The concrete answer to 'won't everyone just bullet-vote?' - "
             "STAR doesn't punish it, it just quietly hands the decision "
             "to voters who expressed more."),
    ),
    "noise_soup": dict(
        seed=217,
        file_no="04", descriptor="noise-soup",
        title="Noise Soup — weak factions, cross-winds, flat-liners and static",
        cast=["Aaron", "Beth", "Caleb", "Dana"],
        n_ballots=47,
        factions=[
            dict(name="leans A-B", share=0.30, mu=[0.75, 0.65, 0.30, 0.30],
                 sigma=0.30, styles={"nuanced": 0.5, "ranked_style": 0.2,
                                     "strong_backup": 0.3}),
            dict(name="leans C-D", share=0.30, mu=[0.30, 0.30, 0.70, 0.70],
                 sigma=0.30, styles={"nuanced": 0.5, "weak_backup": 0.2,
                                     "slate": 0.3}),
            dict(name="crosswind", share=0.20, mu=[0.60, 0.30, 0.65, 0.35],
                 sigma=0.35, styles={"nuanced": 0.4, "cliff35": 0.3,
                                     "anyone_but": 0.15, "protest": 0.15}),
            dict(name="static", share=0.20, mu=[0.50, 0.50, 0.50, 0.50],
                 sigma=0.35, styles={"chaos": 0.5, "flat": 0.3,
                                     "ranked_style": 0.2}),
        ],
        marker_rows=["~", "?"],
        blank_glitch=0.06,
        feature_options={"show_condorcet": True, "matrix_finalists_only": False},
        intro=("The messy-reality fixture: two loose leans instead of "
               "crisp camps, a crosswind bloc, pure-noise voters, "
               "flat-line no-preference ballots, one race abstention (~), "
               "one spoiled ballot (?), and stray blank cells. No clean "
               "story planted - whatever structure the count finds, it "
               "found in the noise. Watch the full pairwise matrix: weak, "
               "noisy electorates are exactly where Condorcet's neat "
               "ordering starts to wobble."),
        say=("This is what a real messy electorate looks like on paper - "
             "abstentions, a spoiled ballot, blanks, noise voters. The "
             "count stays calm: every marker tabulates as 0 and is "
             "reported honestly."),
        why=("Stress fixture: markers, blanks, flat ballots and noise all "
             "in one file - if a reporting change survives Noise Soup, it "
             "survives."),
    ),
    "squeeze_survives": dict(
        seed=51,
        file_no="05", descriptor="squeeze-survives",
        title="Does the squeeze survive noise? Two poles, one consensus middle",
        cast=["Ava", "Ben", "Cora"],
        n_ballots=38,
        factions=[
            dict(name="Ava pole", share=0.42, mu=[0.93, 0.55, 0.07],
                 sigma=0.13, styles={"nuanced": 0.45, "ranked_style": 0.20,
                                     "strong_backup": 0.20, "harsh": 0.15}),
            dict(name="Cora pole", share=0.40, mu=[0.07, 0.55, 0.93],
                 sigma=0.13, styles={"nuanced": 0.45, "ranked_style": 0.20,
                                     "weak_backup": 0.20, "slate": 0.15}),
            dict(name="Ben middle", share=0.18, mu=[0.40, 0.92, 0.40],
                 sigma=0.15, styles={"nuanced": 0.7, "gentle": 0.3}),
        ],
        feature_options={"show_irv": True},
        intro=("The center-squeeze profile - two big poles who each rate "
               "consensus-Ben an honest second - but built from NOISY "
               "utilities and mixed ballot styles instead of clean "
               "textbook blocs. The question the textbook can't answer: "
               "does the squeeze still happen once real-world mess is "
               "layered on? Tabulate and see whether RCV-IRV's "
               "first-choice tunnel vision eliminates the candidate the "
               "pairwise count says beats everyone."),
        say=("Every classroom center-squeeze uses three tidy blocs. This "
             "one uses thirty-eight noisy, differently-styled ballots - "
             "and the squeeze happens anyway. It's not an artifact of "
             "clean examples."),
        why=("Robustness check for the repo's center-squeeze teaching: "
             "the phenomenon survives noise and style mixing, so the "
             "tidy demos aren't cherry-picked."),
    ),
    "narrow_bands": dict(
        seed=239,
        file_no="06", descriptor="narrow-bands",
        title="Narrow Bands — a paint-swatch election scored in slivers of the scale",
        cast=["Azure", "Beige", "Coral", "Dune"],
        n_ballots=24,
        factions=[
            dict(name="cool tilt", share=0.35, mu=[0.85, 0.30, 0.60, 0.25],
                 sigma=0.15, styles={"cliff34": 0.5, "harsh": 0.5}),
            dict(name="warm tilt", share=0.35, mu=[0.25, 0.70, 0.35, 0.80],
                 sigma=0.15, styles={"gentle": 0.5, "cliff35": 0.5}),
            dict(name="drift", share=0.30, mu=[0.50, 0.45, 0.55, 0.50],
                 sigma=0.30, styles={"flat": 0.3, "protest": 0.25,
                                     "chaos": 0.25, "ranked_style": 0.2}),
        ],
        feature_options={"show_score_counts": True},
        intro=("The scale-abuse special: nobody here uses the 0-5 ballot "
               "as designed. One camp scores only in 0-2, one only in "
               "3-5, cliff voters jump 0-to-3, sliver voters live in "
               "3-4, plus flat-liners and a protest ballot. Totals come "
               "out compressed and bunched - photo-finish territory - "
               "and the score-distribution table turns bimodal. A "
               "stress fixture for every place the report says "
               "'distribution', 'total', or 'margin'."),
        say=("Twenty-four voters and not one uses the whole ballot. "
             "Squeezed totals mean tiny gaps - watch how the report "
             "keeps the photo finish legible."),
        why=("If a display or rounding change ever misbehaves on "
             "compressed, bunched totals, this file catches it."),
    ),
}


# ---------------------------------------------------------------------------
# YAML rendering
# ---------------------------------------------------------------------------

HOUSE_OPTIONS = [
    ("show_description", False), ("show_matrix", True),
    ("matrix_finalists_only", True), ("show_condorcet", False),
    ("show_score_counts", False), ("show_irv", False),
    ("show_runoff_percent", True), ("brief", True),
    ("collapse_ballots", True),
]

HUNT_OPTIONS = dict(HOUSE_OPTIONS, show_condorcet=True, show_score_counts=True,
                    show_irv=True, matrix_finalists_only=False)


def census_lines(spec, census):
    counts = {}
    for fname, style in census:
        counts[(fname, style)] = counts.get((fname, style), 0) + 1
    lines = []
    for f in spec["factions"]:
        total = sum(n for (fn, _), n in counts.items() if fn == f["name"])
        parts = ", ".join(
            f"{n} {style}" for (fn, style), n in sorted(
                counts.items(), key=lambda kv: -kv[1]) if fn == f["name"])
        lines.append(f"  - {f['name']}: {total} voters ({parts})")
    marker_n = sum(n for (fn, _), n in counts.items() if fn == "markers")
    if marker_n:
        parts = ", ".join(f"{n} {style}" for (fn, style), n in counts.items()
                          if fn == "markers")
        lines.append(f"  - plus {marker_n} marker row(s): {parts}")
    return lines


def styles_used(census):
    seen = []
    for _, style in census:
        if style in STYLE_BLURB and style not in seen:
            seen.append(style)
    return [f"  - {s}: {STYLE_BLURB[s]}" for s in seen]


def indent(text, pad="  "):
    return "\n".join(pad + line if line.strip() else line.rstrip()
                     for line in text.split("\n"))


def wrap(text, width=76):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    if cur:
        lines.append(cur)
    return "\n".join(lines)


def build_yaml(name, spec, seed, rows, census, options, facts=None,
               filename=None):
    cast = spec["cast"]
    opt_lines = "\n".join(f"  {k}: {str(v).lower()}" for k, v in options)
    desc = [wrap(spec["intro"]), ""]
    desc.append(f"The electorate ({len(rows)} ballots, all individual rows):")
    desc.extend(census_lines(spec, census))
    desc.append("")
    desc.append("Ballot styles in play (taxonomy: 00_start_here/STAR_Voting/")
    desc.append("STAR_ballot_voting_styles.md):")
    desc.extend(styles_used(census))
    desc.append("")
    if facts:
        desc.append(wrap("What the frozen seed produced: " + facts))
        desc.append("")
    desc.append(wrap(
        f"RANDOM-BUT-HUMAN, reproducible: generated by "
        f"06_Other/ballot_style_lab/generate_ballot_styles.py "
        f"(scenario '{name}', seed {seed}) - utilities sampled from the "
        f"faction model above, then rendered through each voter's ballot "
        f"style. Per 00_start_here/topics/simulate_utilities_not_ballots.md "
        f"this is the 'stress-test the tabulator' job (with human-shaped "
        f"renderings), not a method-welfare comparison. Regenerate "
        f"byte-identically: python generate_ballot_styles.py --emit {name}"))

    video = (f"SAY: \"{spec['say']}\"\n"
             f"WHY: {wrap(spec['why'], 71)}")

    parts = [
        f"election_title: {spec['title']}",
        "",
        "scenario_description: |-",
        indent("\n".join(desc)),
        "",
        "# Presenter notes (ignored by the engine; not shown to the audience).",
        "video_script: |-",
        indent(video),
        "",
        "options:",
        opt_lines,
        "  count_separator: \"×\"",
        "",
        "voting_method: STAR",
        "num_winners: 1",
        "ballots: |-",
        indent(format_ballots(cast, rows)),
        "",
    ]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Engine runner + report parsing
# ---------------------------------------------------------------------------

def run_engine(yaml_path):
    proc = subprocess.run([PYTHON, str(ENGINE), yaml_path.name],
                          cwd=yaml_path.parent, capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def parse_report(out):
    r = {"star": None, "scoring": [], "runoff": [], "equal_support": None,
         "condorcet": None, "condorcet_none": False, "differs": {},
         "squeeze_note": False, "lot": False, "tie": False}

    m = re.search(r"Winner — STAR Voting Method[^\n]*\n\s+(\S+)", out)
    if m:
        r["star"] = m.group(1)

    sec = re.search(r"Scoring Round\n(.*?)\n\s*\n", out, re.S)
    if sec:
        r["scoring"] = re.findall(r"^\s+(\S+)\s+--\s+(\d+)", sec.group(1),
                                  re.M)
    m = re.search(r"(\S+) and (\S+) advance", out)
    r["finalists"] = list(m.groups()) if m else []
    sec = re.search(r"Automatic Runoff Round\n(.*?)\n\s*\S+ wins", out, re.S)
    if sec:
        for name, n in re.findall(r"^\s+(\S+|Equal Support)\s+--\s+(\d+)",
                                  sec.group(1), re.M):
            if name == "Equal":
                continue
            r["runoff"].append((name, int(n)))
    m = re.search(r"Equal Support\s+--\s+(\d+)", out)
    if m:
        r["equal_support"] = int(m.group(1))

    m = re.search(r"Condorcet Winner:\s+(\S+)", out)
    if m:
        r["condorcet"] = m.group(1)
    low = out.lower()
    if "no condorcet" in low or "cycle" in low:
        r["condorcet_none"] = True

    for meth, who in re.findall(r"^\s+(.+?)\s*= (\S+)\s+\(differs from STAR\)",
                                out, re.M):
        r["differs"][meth.strip()] = who
    r["squeeze_note"] = "center-squeeze signature" in out
    r["lot"] = bool(re.search(r"\blot\b", low))
    r["tie"] = bool(re.search(r"\btie(?:d|s)?\b(?! scores)", low))
    return r


def interest(r, n_ballots):
    score, flags = 0, []
    scoring_leader = r["scoring"][0][0] if r["scoring"] else None
    if scoring_leader and r["star"] and scoring_leader != r["star"]:
        score += 6
        flags.append("RUNOFF-REVERSAL")
    if r["condorcet_none"]:
        score += 5
        flags.append("NO-CONDORCET/CYCLE")
    if "RCV-IRV" in r["differs"]:
        score += 3
        flags.append(f"IRV≠({r['differs']['RCV-IRV']})")
    if r["squeeze_note"]:
        score += 2
        flags.append("SQUEEZE-NOTE")
    if "Choose-One (Plurality)" in r["differs"]:
        score += 1
        flags.append("PLUR≠")
    es = r["equal_support"] or 0
    if n_ballots and es / n_ballots >= 0.2:
        score += 2 if es / n_ballots < 0.35 else 3
        flags.append(f"ES {es}/{n_ballots}")
    if len(r["runoff"]) >= 2:
        margin = r["runoff"][0][1] - r["runoff"][1][1]
        if margin == 0:
            score += 4
            flags.append("RUNOFF-TIE")
        elif margin <= 2:
            score += 2
            flags.append(f"margin {margin}")
    if len(r["scoring"]) >= 3:
        gap23 = int(r["scoring"][1][1]) - int(r["scoring"][2][1])
        if gap23 <= 1:
            score += 2
            flags.append(f"finalist-gap {gap23}")
    if r["lot"]:
        score += 4
        flags.append("LOT")
    return score, flags


TARGETS = {
    "graders_divide": lambda r, f: "RUNOFF-REVERSAL" in f,
    "cliff_city": lambda r, f: any(x.startswith(("finalist-gap", "ES",
                                                 "NO-CONDORCET")) for x in f),
    "bullet_storm": lambda r, f: any(x.startswith("ES") for x in f)
                                 and any(x.startswith("margin") or
                                         x == "RUNOFF-TIE" for x in f),
    "noise_soup": lambda r, f: "NO-CONDORCET/CYCLE" in f,
    "squeeze_survives": lambda r, f: r["squeeze_note"]
                                     and "RCV-IRV" in r["differs"],
    "narrow_bands": lambda r, f: any(x.startswith(("finalist-gap", "margin"))
                                     or x == "RUNOFF-TIE" for x in f),
}


# ---------------------------------------------------------------------------
# Hunt + emit
# ---------------------------------------------------------------------------

def one_seed(name, spec, seed, tmpdir):
    rng = random.Random(seed)
    rows, census = sample_electorate(spec, rng)
    ypath = tmpdir / f"{name}_{seed}.yaml"
    ypath.write_text(build_yaml(name, spec, seed, rows, census,
                                list(HUNT_OPTIONS.items()))
                     + f"\n# file: {ypath.name}\n")
    rc, out = run_engine(ypath)
    if rc != 0:
        return seed, None, None, out
    rep = parse_report(out)
    sc, flags = interest(rep, len(rows))
    return seed, rep, (sc, flags), out


def hunt(names, n_seeds, tmp_base):
    for name in names:
        spec = SCENARIOS[name]
        tmpdir = Path(tmp_base) / name
        tmpdir.mkdir(parents=True, exist_ok=True)
        results, errors = [], []
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            futs = [pool.submit(one_seed, name, spec, s, tmpdir)
                    for s in range(n_seeds)]
            for fut in concurrent.futures.as_completed(futs):
                seed, rep, scored, out = fut.result()
                if rep is None:
                    errors.append((seed, out))
                else:
                    results.append((seed, rep, scored))
        print(f"\n=== {name}  ({len(results)} seeds ok, "
              f"{len(errors)} errors) ===")
        for seed, out in errors[:2]:
            print(f"  [seed {seed} ERROR]\n{out[-600:]}")
        results.sort(key=lambda t: (-t[2][0], t[0]))
        target = TARGETS[name]
        champion = next(((s, r, sc) for s, r, sc in results
                         if target(r, sc[1]) and not r["lot"]), None)
        for seed, rep, (sc, flags) in results[:10]:
            mark = "  <== CHAMPION" if champion and seed == champion[0] else ""
            print(f"  seed {seed:>4}  score {sc:>2}  "
                  f"STAR={rep['star']:<9} {' '.join(flags)}{mark}")
        if champion:
            s, rep, (sc, flags) = champion
            print(f"  target met by seed {s} "
                  f"(freeze with: seed={s} in SCENARIOS['{name}'])")
        else:
            print("  target NOT met in this seed range")


def facts_from(rep):
    bits = []
    if rep["scoring"]:
        bits.append("Scoring Round " + ", ".join(
            f"{c} {t}" for c, t in rep["scoring"]) + ".")
        totals = [int(t) for _, t in rep["scoring"][:3]]
        if len(totals) >= 3 and totals[1] == totals[2]:
            who = " & ".join(rep["finalists"]) or "the finalists"
            bits.append(f"A scoring tie at the finalist line - {who} "
                        f"advance via STAR's official head-to-head "
                        f"tiebreaker.")
        elif len(totals) >= 2 and totals[0] == totals[1]:
            bits.append("The top two tie the Scoring Round dead even - "
                        "both advance, and the runoff decides.")
    if rep["runoff"]:
        ro = " vs ".join(f"{c} {v}" for c, v in rep["runoff"][:2])
        bits.append(f"Runoff {ro} (Equal Support {rep['equal_support']}).")
        if rep["runoff"][0][1] == rep["runoff"][1][1]:
            bits.append("The runoff itself is TIED - broken by the next "
                        "official tiebreaker (higher scoring total).")
    if rep["star"]:
        bits.append(f"STAR winner: {rep['star']}.")
    if rep["condorcet"]:
        agree = ("agrees" if rep["condorcet"] == rep["star"] else "DIFFERS")
        bits.append(f"Condorcet winner {rep['condorcet']} ({agree}).")
    if rep["condorcet_none"]:
        bits.append("No Condorcet winner - the pairwise order wobbles "
                    "(see the full matrix).")
    for meth, who in rep["differs"].items():
        bits.append(f"{meth} would elect {who}.")
    if rep["squeeze_note"]:
        bits.append("The engine flags the classic center-squeeze signature "
                    "(RCV-IRV the lone outlier).")
    return " ".join(bits)


def emit(names, outdir):
    for name in names:
        spec = SCENARIOS[name]
        seed = spec["seed"]
        if seed is None:
            print(f"  {name}: no frozen seed yet - hunt first, then set "
                  f"seed= in SCENARIOS")
            continue
        rng = random.Random(seed)
        rows, census = sample_electorate(spec, rng)

        with tempfile.TemporaryDirectory() as td:
            tp = Path(td) / "probe.yaml"
            tp.write_text(build_yaml(name, spec, seed, rows, census,
                                     list(HUNT_OPTIONS.items()))
                          + f"\n# file: {tp.name}\n")
            rc, out = run_engine(tp)
            if rc != 0:
                print(f"  {name}: engine error on frozen seed!\n{out[-400:]}")
                continue
            rep = parse_report(out)

        options = dict(HOUSE_OPTIONS)
        options.update(spec.get("feature_options", {}))
        fname = (f"{spec['file_no']}_c{len(spec['cast'])}_b{len(rows)}_"
                 f"{spec['descriptor']}.yaml")
        body = build_yaml(name, spec, seed, rows, census,
                          list(options.items()),
                          facts=facts_from(rep))
        body += ("\nexpected_winners:\n"
                 f"  - {rep['star']}\n\n# file: {fname}\n")
        (outdir / fname).write_text(body)
        print(f"  wrote {fname}  (seed {seed}, STAR winner {rep['star']})")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--hunt", metavar="SCEN|all")
    ap.add_argument("--emit", metavar="SCEN|all")
    ap.add_argument("--seeds", type=int, default=150)
    ap.add_argument("--tmp", default=None,
                    help="hunt workdir (default: a fresh temp dir)")
    ap.add_argument("--outdir", default=str(LAB_DIR))
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    def pick(arg):
        if arg == "all":
            return list(SCENARIOS)
        names = [n.strip() for n in arg.split(",")]
        unknown = [n for n in names if n not in SCENARIOS]
        if unknown:
            sys.exit(f"unknown scenario(s): {', '.join(unknown)} "
                     f"(try --list)")
        return names

    if args.list or not (args.hunt or args.emit):
        for name, spec in SCENARIOS.items():
            frozen = f"seed={spec['seed']}" if spec["seed"] is not None \
                else "no frozen seed"
            print(f"  {name:<18} {frozen:<16} {spec['title']}")
        return

    if args.hunt:
        tmp_base = args.tmp or tempfile.mkdtemp(prefix="ballot_style_hunt_")
        print(f"hunt workdir: {tmp_base}")
        hunt(pick(args.hunt), args.seeds, tmp_base)

    if args.emit:
        outdir = Path(args.outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        emit(pick(args.emit), outdir)


if __name__ == "__main__":
    main()
