#!/usr/bin/env python3
"""Render the repo's ballot art: the voting-style thumbnails and one-off figures.

The original eight `style_*.png` files were captured by hand from Adam's slides.
This script reproduces that design as SVG so new ballots can be added without
going back to the deck: a title, a Worst..Best header, one row per candidate,
and six bubbles (0-5) with the marked one filled in.

Three families share the drawing code:
  * the style gallery (01_STAR/01_Learn/voting_styles/), one thumbnail per style;
  * page figures, which bring their own cast and their own img/ folder — a ballot
    drawn as a ballot beats a box of ★ glyphs, which no two fonts align the same;
  * case art, drawn straight from an election YAML's `ballots:` block, one image
    per ballot row, into `<yaml dir>/img/<stem>_ballot_<n>.png`. `build_yaml_pages.py`
    embeds whatever it finds there, so a case page shows the ballots as marked
    before it shows them as CSV.

    python3 build_style_ballot_images.py            # write SVG + PNG for every ballot
    python3 build_style_ballot_images.py --svg-only # skip rasterizing
    python3 build_style_ballot_images.py --from-yaml 01_STAR/02_Examples/cases/02a_*.yaml

Two ballots are drawn, chosen by the case's `voting_method` — the 0-5 STAR grid
(six bubbles a row) and the Approval Yes/No double bubble (two). They are
different pieces of paper, so they get different drawings rather than one
drawing with a setting; a method in neither family gets no art at all.

The PNG is what the docs embed (the repo's other ballot art is PNG, and GitHub's
Markdown renderer is unreliable with relative-path SVG); the .svg is written
alongside it so the art stays editable. Rasterizing needs Pillow -- with
--svg-only, or if Pillow is missing, the .svg files are still written.
"""

from __future__ import annotations

import argparse
import math
import os
import re
import sys
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parents[3]
IMG_DIR = REPO_ROOT / "01_STAR" / "01_Learn" / "voting_styles" / "img"
LIMITS_IMG_DIR = REPO_ROOT / "01_STAR" / "01_Learn" / "properties_and_limits" / "img"

# The five-candidate cast used by every style thumbnail on the hub page.
CANDIDATES = ["Andre", "Blake", "Carmen", "David", "Ella"]

# The six-candidate cast of the Test of Balance figure.
BALANCE_CAST = ["Abby", "Ben", "Carmen", "DeAndre", "Eric", "Freya"]


class Ballot(NamedTuple):
    """One rendered ballot: who is on it, what was marked, and where it lands."""

    title: str
    cast: list[str]
    scores: list[int | None]
    out_dir: Path
    quoted: bool = True  # gallery titles are shown in quotes; figures are not
    # Which piece of paper this is. "score" = the 0–5 STAR ballot (six bubbles a
    # row); "approval" = the Yes/No double-bubble Approval ballot (two); "grade"
    # = the Majority Judgment grade ballot, one column per grade WORD. They are
    # different ballots, not settings of one — hence separate renderers.
    kind: str = "score"
    # The grade ballot's column labels, lowest first ("To Reject" … "Excellent").
    # Only the grade ballot has these, and unlike the other two its scale is a
    # property of the election rather than a constant — Balinski & Laraki's whole
    # argument is that the *words* are the ballot, so they travel with it.
    grades: tuple[str, ...] = ()
    # A *whole* ballot rather than a thumbnail: the seat count above the race
    # (technical specifications §3.c), the voter instructions above the grid
    # (§3.b), and the method explanation below it (§3.d). A style thumbnail is
    # deliberately none of this — it crops to the marks, because the marks are
    # its subject. A ballot page's subject is the paper, and on real paper the
    # instructions and the explanation are *printed on the ballot itself*
    # (§3.a requires it), so a picture without them is not a picture of a
    # ballot. Both are pre-wrapped by the author: one string per printed line,
    # so the art is deterministic and a bad line break is fixable by hand.
    subtitle: str = ""
    header: tuple[str, ...] = ()
    footer: tuple[str, ...] = ()
    # Equal Vote sets the STAR and Bloc STAR instructions as a bulleted list and
    # the Proportional STAR ones as a running paragraph. That is their choice per
    # ballot, not ours, so it is a per-ballot flag rather than a house style.
    header_bullets: bool = True


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

BALLOTS: dict[str, Ballot] = {
    slug: Ballot(title, CANDIDATES, scores, IMG_DIR)
    for slug, (title, scores) in STYLES.items()
}

# Page figures. The Test of Balance pair is one ballot and its exact opposite:
# every row sums to 5, so the two together move no score total and cancel 1-1 in
# the runoff. Keep them mirrors -- second = 5 - first, row for row.
BALLOTS.update({
    "balance_voter1": Ballot(
        "Voter 1", BALANCE_CAST, [2, 1, 0, 1, 5, 4], LIMITS_IMG_DIR, quoted=False
    ),
    "balance_voter2": Ballot(
        "Voter 2 — the exact opposite",
        BALANCE_CAST,
        [3, 4, 5, 4, 0, 1],
        LIMITS_IMG_DIR,
        quoted=False,
    ),
})

# --------------------------------------------------------------------------- #
# The whole-ballot pair: single-winner STAR and Bloc STAR, side by side
# --------------------------------------------------------------------------- #
# These two exist to be compared, so they are deliberately the same drawing with
# the same cast and the SAME MARKS — which is also how the technical
# specifications present them (Figures A and B, identical bubbles). Everything a
# voter does is identical; the differences are three lines of text, and being
# able to point at exactly those three lines is the entire lesson. Keep the marks
# in sync if either is ever redrawn.
#
# The wording is the specification's own (v1.3 §3.b instructions, §3.c seat count
# above the race, §3.d method explanation) with one deliberate departure, argued
# on the page: the method is named "Bloc STAR Voting" (§1.c) rather than the bare
# "STAR Voting" of the §3.d template, which §3.e's paraphrase licence allows
# because §1.e already defines the unqualified name to MEAN this method.
BLOC_IMG_DIR = REPO_ROOT / "02_STAR_Bloc" / "01_Learn" / "img"

# §3.b, verbatim. Shared, because the instructions are the one part that does not
# change between the two ballots — there is nothing to ration on a Bloc ballot.
SPEC_INSTRUCTIONS = (
    "Give your favorite candidate five stars.",
    "Give your last choice zero stars or leave them blank.",
    "Equal scores are allowed.",
    "Score other candidates as desired.",
)

# Figure A / Figure B marks: Andre 5, Blake 0, Carmen 1, David 4, Ella 4.
SPEC_MARKS = [5, 0, 1, 4, 4]

BALLOTS.update({
    "ballot_star_single_winner": Ballot(
        "STAR Voting",
        CANDIDATES,
        SPEC_MARKS,
        BLOC_IMG_DIR,
        quoted=False,
        header=SPEC_INSTRUCTIONS,
        footer=(
            "This election will use STAR Voting to elect one winner. In STAR",
            "Voting, the two highest scoring candidates are finalists and your",
            "vote goes to the finalist you prefer. The finalist preferred by the",
            "most voters wins.",
        ),
    ),
    "ballot_bloc_star": Ballot(
        "Bloc STAR Voting",
        CANDIDATES,
        SPEC_MARKS,
        BLOC_IMG_DIR,
        quoted=False,
        subtitle="This election will elect 3 winners.",
        header=SPEC_INSTRUCTIONS,
        footer=(
            "This election will use Bloc STAR Voting to elect 3 winners. In Bloc",
            "STAR Voting, the two highest scoring candidates are finalists and",
            "your vote goes to the finalist you prefer. The finalist preferred by",
            "the most voters wins. This process repeats until all seats have",
            "been filled.",
        ),
    ),
})

# --------------------------------------------------------------------------- #
# The third piece of paper: Proportional STAR
# --------------------------------------------------------------------------- #
# Transcribed from Equal Vote's own Proportional STAR ballot. Worth being exact
# about what does and does not change from the two above, because it is easy to
# assume "same 0–5 ballot" means "same ballot" and that is wrong:
#
#   * the GRID is identical — 0–5, one row per candidate, nothing rationed;
#   * the seat count is stated above the race, as on the Bloc ballot;
#   * the INSTRUCTIONS are reworded and set as a paragraph, not bullets;
#   * the FOOTER is a completely different method — rounds, and each round
#     designating a winner's strongest supporters as represented.
#
# So this is the same distinction the Bloc page draws (grid identical, top and
# bottom lines differ), and the reason 03_STAR_PR cannot simply reuse the
# single-winner ballot art.
#
# The title carries the same deliberate departure as the Bloc ballot: Equal
# Vote's art heads this "STAR VOTING" and names the method only in the footer,
# and we name it up front instead.
PR_IMG_DIR = REPO_ROOT / "03_STAR_PR" / "01_Learn" / "img"

PR_CAST = ["Abby", "Ben", "Carmen", "DeAndre", "Eric"]

BALLOTS.update({
    "ballot_proportional_star": Ballot(
        "Proportional STAR Voting",
        PR_CAST,
        [4, 5, 3, 5, 0],
        PR_IMG_DIR,
        quoted=False,
        subtitle="This election will elect 3 winners.",
        header=(
            "Score all candidates from 0–5 stars. Those you leave blank",
            "receive a zero. If you don't have a preference you can give",
            "candidates the same scores.",
        ),
        header_bullets=False,
        footer=(
            "Winners in Proportional STAR Voting are selected in rounds. Each",
            "round elects the candidate with the highest total score and then",
            "designates that candidate's strongest supporters as represented.",
            "Subsequent rounds include all voters who are not yet represented.",
        ),
    ),
})

# --------------------------------------------------------------------------- #
# Case art — ballots drawn from an election YAML
# --------------------------------------------------------------------------- #
# The gallery above is hand-listed because each thumbnail illustrates a *style*.
# A case file already says exactly what each voter marked, so its art is derived,
# not authored: parse the `ballots:` block the same way the engine does and draw
# one ballot per row. Blanks and markers stay blank here — the engine counts them
# as 0, but a ballot with no mark is what the voter actually handed in, and that
# distinction is half the reason to show the picture at all.
# Methods whose voters are handed the 0–5 score ballot this art draws. Bloc STAR
# and the proportional variants (allocated / sss / rrv) use the same ballot; only
# the count differs.
SCORE_METHODS = {"star", "starr", "bloc_star", "star_pr", "score", "range",
                 "allocated", "sss", "rrv", "bloc"}
# Approval voters get a *different* piece of paper — approve or don't, one bit —
# so it gets its own drawing (Yes/No bubbles) rather than a 0–5 grid with four
# columns nobody was offered. Everything still outside both sets — Plurality, any
# ranked method — has no art at all: a ballot we can't draw beats a wrong one.
APPROVAL_METHODS = {"approval", "approval_multi_winner", "approval_multiwinner",
                    "bloc_approval"}
# The grade-ballot procedures — a `grades:` file rather than a `ballots:` one, and
# a third piece of paper: columns of grade WORDS, no numerals at all. Keyed off
# `grade_method:`, which is the key those files use.
GRADE_METHODS = {"majorityjudgment", "majority_judgment", "majority_judgement",
                 "mj", "range", "rangevoting", "range_voting"}
MARKER_CHARS = set("-~&?%")
WEIGHT_RE = re.compile(r"\s*(\d+)\s*[:xX×]\s*(.*)")  # "42: 5, 4" / "9x5" / "9×5"
MAX_SCORE = 5
DEFAULT_LIMIT = 8  # rows drawn per case before we stop and say so


class CaseBallotError(ValueError):
    """The YAML can't be drawn as 0–5 ballot art (ranked ballots, bad cells…)."""


class BallotRow(NamedTuple):
    """One parsed ballot line: what it means, and what it literally said."""

    weight: int                 # a `42:` prefix = 42 identical ballots
    scores: list[int | None]    # None = blank/marker, drawn as an unmarked row
    note: str                   # the trailing `#` comment, if the author left one
    cells: list[str]            # cell text verbatim ("5", "-", "~") for display


def _find_ballots(node):
    """The `ballots:` block, top-level or nested (BV-import schemas nest it)."""
    if isinstance(node, dict):
        if node.get("ballots") is not None:
            return node["ballots"]
        for v in node.values():
            found = _find_ballots(v)
            if found is not None:
                return found
    elif isinstance(node, list):
        for v in node:
            found = _find_ballots(v)
            if found is not None:
                return found
    return None


def _cell_to_score(cell: str, max_score: int = MAX_SCORE) -> int | None:
    """0–max → int; blank or any marker → None (drawn as an unmarked row)."""
    cell = cell.strip()
    if cell == "" or cell in MARKER_CHARS:
        return None
    if not cell.isdigit() or not 0 <= int(cell) <= max_score:
        raise CaseBallotError(f"cell {cell!r} is not a 0–{max_score} score")
    return int(cell)


def parse_ballot_block(text: str, max_score: int = MAX_SCORE):
    """(cast, [BallotRow, …]) from a `ballots:` block.

    Mirrors the engine's parser: `#` starts a comment, row 1 is the candidate
    header, an optional `Count:` label rides on the first header cell, and a
    leading `N:` / `Nx` / `N×` on a row is that ballot's weight.

    `max_score` is 5 for the STAR ballot and 1 for an Approval one — an Approval
    file holding a `3` is a file the Yes/No art cannot honestly draw.
    """
    rows = []
    for raw in str(text).strip().splitlines():
        body, _, note = raw.partition("#")
        body = body.strip()
        if body:
            rows.append((body, note.strip()))
    if len(rows) < 2:
        raise CaseBallotError("need a candidate header and at least one ballot")
    if ">" in rows[0][0] or any(">" in r for r, _ in rows[1:]):
        raise CaseBallotError("ranked ballots — the 0–5 ballot art doesn't apply")

    cast = [c.strip() for c in re.split(r"[,\t]+", rows[0][0]) if c.strip()]
    if cast and re.match(r"(?i)^count\s*:", cast[0]):
        cast[0] = cast[0].split(":", 1)[1].strip()

    out = []
    for body, note in rows[1:]:
        parts = re.split(r"[,\t]", body)
        weight = 1
        wmatch = WEIGHT_RE.match(parts[0])
        if wmatch:
            weight = int(wmatch.group(1))
            parts[0] = wmatch.group(2)
        cells = [p.strip() for p in parts]
        scores = [_cell_to_score(c, max_score) for c in cells]
        if len(scores) != len(cast):
            raise CaseBallotError(
                f"row {body!r} has {len(scores)} cells, header has {len(cast)}"
            )
        out.append(BallotRow(weight, scores, note, cells))
    return cast, out


def row_title(index: int, weight: int, note: str) -> str:
    """What the drawn ballot calls itself: the author's note, after the count.

    A weighted row is one piece of paper standing for many voters, and the
    count has to survive into the title — a ballot captioned "Sofia loves
    sushi" that actually represents 21 of them is a picture telling a small
    lie. It used to: the note replaced the count outright, and the page
    restored it in a separate `Voters` column. That column is what pushed a
    weighted table past the site's content width, so the count moved here,
    where it belonged anyway.
    """
    count = f"{weight} voters" if weight > 1 else ""
    title = f"{count} — {note}" if count and note else (note or count
                                                        or f"Voter {index}")
    return (title if len(title) <= TITLE_MAX_CHARS
            else title[:TITLE_MAX_CHARS - 1].rstrip() + "…")


def grade_scale(spec) -> list[str]:
    """The grade columns, lowest first, from a `grade_scale:` string.

    Mirrors `_scale()` in `pref_voting_tabulation_engine/grade_methods_report.py`
    — the tool that *counts* these files — and adds the form that tool doesn't
    need but a picture does: a pipe-separated list of words,
    `"To Reject|Poor|Acceptable|Good|Very Good|Excellent"`. Numeric and letter
    ranges come back as strings here because a column label is text either way;
    the counting tool keeps them typed, because it has to do arithmetic.
    """
    spec = str(spec).strip()
    if "|" in spec:
        return [w.strip() for w in spec.split("|") if w.strip()]
    lo, _, hi = spec.partition("-")
    lo, hi = lo.strip(), hi.strip()
    if lo.isdigit() and hi.isdigit():
        return [str(n) for n in range(int(lo), int(hi) + 1)]
    if len(lo) == 1 and len(hi) == 1 and lo.isalpha() and hi.isalpha():
        return [chr(c) for c in range(ord(lo.upper()), ord(hi.upper()) + 1)]
    raise CaseBallotError(
        f"grade_scale {spec!r} must be '1-10', 'A-H', or 'Worst|…|Best'")


def parse_grade_block(text: str, scale: list[str], notes: dict | None = None):
    """(cast, [BallotRow, …]) from a `grades:` block — one row per VOTER.

    The block is Felsenthal's table, which is transposed relative to a ballot: its
    header names the voters and each later row is one candidate. A ballot is one
    voter's paper, so this transposes it back. A blank cell stays blank in the
    picture even though both grade procedures count it as the scale floor — the
    same rule the 0–5 art follows, and the reason the truncation examples are
    worth drawing at all.

    `notes` is the case file's optional `voter_notes:` map; a voter named there
    gets that as the title on their ballot, exactly as a `#` comment titles a
    score ballot.
    """
    rows = [l for l in str(text).strip().splitlines() if l.strip()]
    if len(rows) < 2:
        raise CaseBallotError("need a voter header and at least one candidate row")
    voters = [c.strip() for c in rows[0].split(",")][1:]
    if not voters:
        raise CaseBallotError("the header row names no voters")

    cast, by_cand = [], []
    index = {str(g).upper(): i for i, g in enumerate(scale)}
    for line in rows[1:]:
        cells = [c.strip() for c in line.split(",")]
        cand, cells = cells[0], cells[1:]
        if len(cells) != len(voters):
            raise CaseBallotError(
                f"row {cand!r} has {len(cells)} grades but the header names "
                f"{len(voters)} voters")
        marks = []
        for cell in cells:
            if not cell:
                marks.append((None, ""))
                continue
            if cell.upper() not in index:
                raise CaseBallotError(
                    f"grade {cell!r} for {cand} is not on the "
                    f"{scale[0]}…{scale[-1]} scale")
            marks.append((index[cell.upper()], scale[index[cell.upper()]]))
        cast.append(cand)
        by_cand.append(marks)

    notes = notes or {}
    out = []
    for v, voter in enumerate(voters):
        out.append(BallotRow(
            1,
            [by_cand[c][v][0] for c in range(len(cast))],
            str(notes.get(voter, "")).strip(),
            [by_cand[c][v][1] for c in range(len(cast))],
        ))
    return cast, out, voters


def grade_row_title(voter: str, note: str) -> str:
    """What a drawn grade ballot calls itself: the author's note, else the voter.

    `V1` is Felsenthal's column heading, not a name a reader recognises, so it is
    spelled out; anything else is already a name and is left alone.
    """
    if note:
        return (note if len(note) <= TITLE_MAX_CHARS
                else note[:TITLE_MAX_CHARS - 1].rstrip() + "…")
    m = re.match(r"^[Vv](\d+)$", voter.strip())
    return f"Voter {m.group(1)}" if m else voter.strip()


def ballots_from_yaml(yaml_path: Path, limit: int = DEFAULT_LIMIT):
    """[(slug, Ballot)] for a case file — one per ballot row, capped at `limit`."""
    try:
        import yaml as _yaml
    except ImportError as exc:  # pragma: no cover - environment problem
        raise CaseBallotError("PyYAML is required to read case files") from exc

    yaml_path = Path(yaml_path)
    data = _yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    block = _find_ballots(data)
    if block is None:
        if isinstance(data, dict) and data.get("grades") is not None:
            return _grade_ballots_from(yaml_path, data, limit)
        raise CaseBallotError("no `ballots:` block")
    # Allowlist, not a blocklist: each drawing IS a particular piece of paper, so
    # a method is drawn only when we know which paper its voters were handed —
    # the 0–5 grid for the score family, Yes/No bubbles for Approval. Anything
    # else (choose-one, any ranking) is refused. Drawing a Plurality race as six
    # bubbles per candidate shows a ballot nobody was given.
    method = str(_find_first_method(data) or "STAR").split("#")[0].strip().lower()
    method = method.replace("-", "_").replace(" ", "_")
    if method in APPROVAL_METHODS:
        kind, max_score = "approval", 1
    elif method in SCORE_METHODS:
        kind, max_score = "score", MAX_SCORE
    else:
        raise CaseBallotError(
            f"{method or 'this method'} is neither a 0–5 score nor an approval "
            f"ballot — drawing one would mislead")

    cast, rows = parse_ballot_block(block, max_score)
    stem = yaml_path.stem
    out_dir = yaml_path.parent / "img"
    return [
        (f"{stem}_ballot_{n}",
         Ballot(row_title(n, r.weight, r.note), cast, r.scores, out_dir,
                quoted=False, kind=kind))
        for n, r in enumerate(rows[:limit], start=1)
    ], len(rows)


def _grade_ballots_from(yaml_path: Path, data: dict, limit: int):
    """[(slug, Ballot)] for a `grades:` case file — one ballot per voter."""
    method = str(data.get("grade_method") or "").split("#")[0].strip().lower()
    method = method.replace("-", "_").replace(" ", "_")
    if method not in GRADE_METHODS:
        raise CaseBallotError(
            f"{method or 'this grade method'} is not a grade ballot this art "
            f"knows how to draw")
    scale = grade_scale(data.get("grade_scale", "1-10"))
    cast, rows, voters = parse_grade_block(
        data["grades"], scale, data.get("voter_notes"))
    stem = yaml_path.stem
    out_dir = yaml_path.parent / "img"
    return [
        (f"{stem}_ballot_{n}",
         Ballot(grade_row_title(voters[n - 1], r.note), cast, r.scores, out_dir,
                quoted=False, kind="grade", grades=tuple(scale)))
        for n, r in enumerate(rows[:limit], start=1)
    ], len(rows)


def _find_first_method(node):
    if isinstance(node, dict):
        if node.get("voting_method") is not None:
            return node["voting_method"]
        for v in node.values():
            found = _find_first_method(v)
            if found is not None:
                return found
    elif isinstance(node, list):
        for v in node:
            found = _find_first_method(v)
            if found is not None:
                return found
    return None


# Drawn art is derived from a `ballots:` block, so it can go stale the moment
# someone edits one. `--refresh` (wired into regen_all.py) redraws every case
# that ALREADY has art — never picking new cases, so "which cases get pictures"
# stays an editorial decision and only the pictures themselves are automatic.
REFRESH_SKIP_DIRS = {"site", "node_modules", "__pycache__", "venv"}


def refresh_targets(root: Path = REPO_ROOT) -> dict[Path, int]:
    """{case yaml: highest ballot index drawn} for every case with art on disk."""
    targets: dict[Path, int] = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in REFRESH_SKIP_DIRS and not d.startswith(".")]
        here = Path(dirpath)
        if here.name != "img":
            continue
        for name in filenames:
            m = re.match(r"^(.*)_ballot_(\d+)\.png$", name)
            if not m:
                continue
            src = here.parent / f"{m.group(1)}.yaml"
            if src.is_file():
                targets[src] = max(targets.get(src, 0), int(m.group(2)))
    return dict(sorted(targets.items()))


def prune_art(out_dir: Path, stem: str, keep: int) -> list[Path]:
    """Delete art for ballot rows that no longer exist (the case lost voters)."""
    gone = []
    for path in sorted(out_dir.glob(f"{stem}_ballot_*")):
        m = re.match(rf"^{re.escape(stem)}_ballot_(\d+)\.(png|svg)$", path.name)
        if m and int(m.group(1)) > keep:
            path.unlink()
            gone.append(path)
    return gone


def alt_text(ballot: Ballot) -> str:
    """Screen-reader text: the same marks, read out row by row."""
    if ballot.kind == "approval":
        marks = [
            f"{name} Yes" if mark == 1
            else f"{name} No" if mark == 0
            else f"{name} left blank (not approved)"
            for name, mark in zip(ballot.cast, ballot.scores)
        ]
        return f"A Yes/No Approval ballot — {ballot.title}: " + ", ".join(marks) + "."
    if ballot.kind == "grade":
        floor = ballot.grades[0] if ballot.grades else "the lowest grade"
        marks = [
            f"{name} {ballot.grades[i]}" if i is not None
            else f"{name} left ungraded (counts as {floor})"
            for name, i in zip(ballot.cast, ballot.scores)
        ]
        return (f"A grade ballot — {ballot.title}: " + ", ".join(marks) + ".")
    marks = [
        f"{name} {score}" if score is not None else f"{name} left blank (counts as 0)"
        for name, score in zip(ballot.cast, ballot.scores)
    ]
    return f"A 0–5 STAR ballot — {ballot.title}: " + ", ".join(marks) + "."


# Palette sampled from the existing hand-made thumbnails.
RUST = "#C0504D"          # title
ROW_TINT = "#DCE6F1"      # alternating row background
RULE = "#95B3D7"          # horizontal rules
STAR_OUTLINE = "#A9C4D9"  # the star glyphs in the header
BUBBLE_STROKE = "#595959"
INK = "#000000"

FONT = "Arial Black, Arial Bold, Helvetica, sans-serif"
# The prose blocks of a whole ballot — instructions and method explanation — are
# set in a regular weight, as they are on a real ballot. Arial Black is for the
# things you scan (names, the scale); the sentences you actually read are not.
BODY_FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"

W = 1600
TITLE_X = 30
TITLE_SIZE = 66       # gallery titles are short and all render at this size
TITLE_MIN_SIZE = 34   # …a case's title is the author's ballot note, so it shrinks
TITLE_CHAR_W = 0.66   # Arial Black advance ≈ 0.66 em — wide, so estimate wide
TITLE_Y = 78
HDR_WORST_Y = 168
STAR_ROW_Y = 292
GRID_TOP = 352
ROW_H = 158
COL0_X = 630           # centre of the "0" column
COL_DX = 174           # spacing between bubble columns
NAME_X = 118
BOTTOM_PAD = 18

# The whole-ballot blocks (see Ballot.header / .footer). Sizes are chosen so the
# instructions read as instructions -- smaller than the candidate names, larger
# than the bubble numerals -- and so a five-line footer still fits the width at
# the wrap points the author picked.
SUB_SIZE = 54          # the seat-count line, directly under the method name
SUB_GAP = 74           # title baseline -> subtitle baseline
HDR_SIZE = 46          # voter instructions
HDR_LINE_H = 62
HDR_GAP = 52           # last thing above -> first instruction line
FTR_SIZE = 44          # the method explanation
FTR_LINE_H = 58
FTR_GAP = 62           # grid bottom rule -> first footer line
BULLET_X = 44          # the "•" column; text hangs indented from BULLET_TEXT_X
BULLET_TEXT_X = 84


# The Approval ballot: two bubbles a row under Yes / No, after the Equal Vote
# "double bubble" mockup in 04_Approval/01_Learn/img/. Narrower canvas than the
# 0–5 grid because two columns don't need six columns' room — and a ballot that
# is nearly square is what an Approval ballot actually looks like.
APPROVAL_W = 1180
APPROVAL_COL0_X = 700
APPROVAL_COL_DX = 260
APPROVAL_HEADERS = ("Yes", "No")
APPROVAL_INSTRUCTION = "Vote for ALL candidates you approve of."
APPROVAL_INSTRUCTION_SIZE = 42


# The grade ballot: one column per grade WORD. Wider than either of the others
# and unavoidably so — six words need six words' room, which is why real Majority
# Judgment ballots print landscape. Nothing here is a constant width: the scale
# is per-election, so the columns are sized from the labels and the canvas from
# the columns. The name gutter is tighter than the 0–5 grid's for the same reason
# — every pixel spent left of the first column is a pixel the words don't get.
GRADE_COL0_X = 560
GRADE_NAME_X = 60
GRADE_HDR_SIZE = 44
GRADE_HDR_LINE_H = 54
GRADE_INSTRUCTION_SIZE = 42
GRADE_COL_MIN_DX = 190
GRADE_COL_PAD = 26        # blank space either side of the widest label line


def grade_label_lines(label: str) -> list[str]:
    """A column heading, split onto two lines at its last space ("Very Good")."""
    label = str(label)
    if " " not in label:
        return [label]
    head, _, tail = label.rpartition(" ")
    return [head, tail]


def grade_col_dx(labels) -> int:
    """Column spacing: wide enough for the widest heading line, at a floor."""
    widest = max((len(line) for l in labels for line in grade_label_lines(l)),
                 default=1)
    return max(GRADE_COL_MIN_DX,
               int(widest * GRADE_HDR_SIZE * TITLE_CHAR_W) + GRADE_COL_PAD)


def grade_instruction(ballot: Ballot) -> str:
    """The one printed line — and it names the convention that decides elections.

    Under both grade procedures an ungraded candidate takes the bottom of the
    scale, which is the entire mechanism of the truncation paradox. On a real
    ballot that rule would be printed on the paper, so it is printed here.
    """
    floor = ballot.grades[0] if ballot.grades else "the lowest grade"
    return f"Grade EVERY candidate. Ungraded counts as {floor}."


def col_x(i: int) -> float:
    return COL0_X + i * COL_DX


def approval_col_x(i: int) -> float:
    return APPROVAL_COL0_X + i * APPROVAL_COL_DX


def grade_col_x(i: int, dx: int) -> float:
    return GRADE_COL0_X + i * dx


def grade_width(ballot: Ballot) -> int:
    dx = grade_col_dx(ballot.grades)
    return int(grade_col_x(len(ballot.grades) - 1, dx) + dx / 2)


def canvas_width(ballot: Ballot) -> int:
    if ballot.kind == "approval":
        return APPROVAL_W
    return grade_width(ballot) if ballot.kind == "grade" else W


def title_font_size(shown: str, width: int = W) -> int:
    """Shrink a long title until it fits the canvas.

    Both renderers call this, so the SVG and the PNG stay the same drawing. A
    style name always fits at the full size; a case's title is whatever the
    author wrote next to that ballot row, which can run long. The floor scales
    with the canvas, so the narrower Approval ballot can take the same titles.
    """
    if not shown:
        return TITLE_SIZE
    floor = TITLE_MIN_SIZE * width / W
    fits = (width - 2 * TITLE_X) / (TITLE_CHAR_W * len(shown))
    return int(max(floor, min(TITLE_SIZE, fits)))


# Longest title that still fits on one line at the smallest size.
TITLE_MAX_CHARS = int((W - 2 * TITLE_X) / (TITLE_CHAR_W * TITLE_MIN_SIZE))


def top_block_h(ballot: Ballot) -> int:
    """How far the grid is pushed down by a seat count and an instruction block.

    Zero for a thumbnail, which is why every gallery ballot still renders at the
    exact pixel geometry the hand-made originals were captured at.
    """
    dy = SUB_GAP if ballot.subtitle else 0
    if ballot.header:
        dy += HDR_GAP + len(ballot.header) * HDR_LINE_H
    return dy


def bottom_block_h(ballot: Ballot) -> int:
    """Room under the grid's closing rule for the method explanation."""
    return FTR_GAP + len(ballot.footer) * FTR_LINE_H if ballot.footer else 0


def height_for(ballot: Ballot) -> int:
    """Canvas height: the grid grows a row at a time, the margins don't."""
    return (
        GRID_TOP
        + top_block_h(ballot)
        + len(ballot.cast) * ROW_H
        + bottom_block_h(ballot)
        + BOTTOM_PAD
    )


def esc(text: str) -> str:
    """XML-escape a run of author-written ballot text."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


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


def render_svg(ballot: Ballot) -> str:
    if ballot.kind == "approval":
        return render_approval_svg(ballot)
    if ballot.kind == "grade":
        return render_grade_svg(ballot)
    title, cast, scores = ballot.title, ballot.cast, ballot.scores
    H = height_for(ballot)
    dy = top_block_h(ballot)
    plain = f'"{title}"' if ballot.quoted else title
    shown = f"&quot;{title}&quot;" if ballot.quoted else title
    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
        f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
        f'<text x="{TITLE_X}" y="{TITLE_Y}" font-family="{FONT}" '
        f'font-size="{title_font_size(plain)}" font-weight="bold" '
        f'fill="{RUST}">{shown}</text>',
    ]

    # The seat count sits above the race, not inside the instructions (§3.c).
    if ballot.subtitle:
        out.append(
            f'<text x="{TITLE_X}" y="{TITLE_Y + SUB_GAP}" font-family="{FONT}" '
            f'font-size="{SUB_SIZE}" font-weight="bold" fill="{INK}">'
            f'{esc(ballot.subtitle)}</text>'
        )
    for n, line in enumerate(ballot.header):
        y = TITLE_Y + (SUB_GAP if ballot.subtitle else 0) + HDR_GAP + n * HDR_LINE_H
        if ballot.header_bullets:
            out.append(
                f'<text x="{BULLET_X}" y="{y}" font-family="{BODY_FONT}" '
                f'font-size="{HDR_SIZE}" fill="{INK}">•</text>'
            )
        x = BULLET_TEXT_X if ballot.header_bullets else TITLE_X
        out.append(
            f'<text x="{x}" y="{y}" font-family="{BODY_FONT}" '
            f'font-size="{HDR_SIZE}" fill="{INK}">{esc(line)}</text>'
        )

    out += [
        f'<text x="{col_x(0) + 40}" y="{HDR_WORST_Y + dy}" font-family="{FONT}" font-size="58" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle">Worst</text>',
        f'<text x="{col_x(5)}" y="{HDR_WORST_Y + dy}" font-family="{FONT}" font-size="58" '
        f'font-weight="bold" fill="{INK}" text-anchor="middle">Best</text>',
    ]

    # Header scale: 0 is a bare numeral, 1-5 sit inside a star outline.
    for i in range(6):
        cx = col_x(i)
        if i:
            out.append(
                f'<path d="{star_path(cx, STAR_ROW_Y + dy - 18, 62)}" fill="none" '
                f'stroke="{STAR_OUTLINE}" stroke-width="6" stroke-linejoin="round"/>'
            )
        out.append(
            f'<text x="{cx}" y="{STAR_ROW_Y + dy}" font-family="{FONT}" font-size="60" '
            f'font-weight="bold" fill="{INK}" text-anchor="middle">{i}</text>'
        )

    for r, name in enumerate(cast):
        top = GRID_TOP + dy + r * ROW_H
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
    bottom = GRID_TOP + dy + len(cast) * ROW_H
    out.append(f'<line x1="0" y1="{bottom}" x2="{W}" y2="{bottom}" stroke="{RULE}" stroke-width="7"/>')
    for n, line in enumerate(ballot.footer):
        out.append(
            f'<text x="{TITLE_X}" y="{bottom + FTR_GAP + n * FTR_LINE_H}" '
            f'font-family="{BODY_FONT}" font-size="{FTR_SIZE}" fill="{INK}">{esc(line)}</text>'
        )
    out.append("</svg>")
    return "\n".join(out)


def approval_filled(mark: int | None, col: int) -> bool:
    """Is column `col` (0 = Yes, 1 = No) filled in for this mark?

    `1` fills Yes and `0` fills No — an Approval file records "not approved" as a
    real 0, which on a double-bubble ballot is a real No. A blank or a marker
    fills neither: the tally counts it as not approved, but the voter left the
    row alone, and the picture should say so.
    """
    if mark is None:
        return False
    return (mark == 1) == (col == 0)


def render_approval_svg(ballot: Ballot) -> str:
    title, cast, marks = ballot.title, ballot.cast, ballot.scores
    width = APPROVAL_W
    H = height_for(ballot)
    plain = f'"{title}"' if ballot.quoted else title
    shown = f"&quot;{title}&quot;" if ballot.quoted else title
    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {H}" '
        f'width="{width}" height="{H}">',
        f'<rect width="{width}" height="{H}" fill="#FFFFFF"/>',
        f'<text x="{TITLE_X}" y="{TITLE_Y}" font-family="{FONT}" '
        f'font-size="{title_font_size(plain, width)}" font-weight="bold" '
        f'fill="{RUST}">{shown}</text>',
        f'<text x="{TITLE_X}" y="{HDR_WORST_Y}" font-family="{FONT}" '
        f'font-size="{APPROVAL_INSTRUCTION_SIZE}" font-weight="bold" '
        f'fill="{INK}">{APPROVAL_INSTRUCTION}</text>',
    ]

    for i, label in enumerate(APPROVAL_HEADERS):
        out.append(
            f'<text x="{approval_col_x(i)}" y="{STAR_ROW_Y}" font-family="{FONT}" '
            f'font-size="60" font-weight="bold" fill="{INK}" '
            f'text-anchor="middle">{label}</text>'
        )

    for r, name in enumerate(cast):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            out.append(f'<rect x="0" y="{top}" width="{width}" height="{ROW_H}" fill="{ROW_TINT}"/>')
        out.append(
            f'<line x1="0" y1="{top}" x2="{width}" y2="{top}" stroke="{RULE}" stroke-width="7"/>'
        )
        out.append(
            f'<text x="{NAME_X}" y="{mid + 22}" font-family="{FONT}" font-size="62" '
            f'font-weight="bold" fill="{INK}">{name}</text>'
        )
        for i in range(len(APPROVAL_HEADERS)):
            cx = approval_col_x(i)
            if approval_filled(marks[r], i):
                out.append(f'<ellipse cx="{cx}" cy="{mid}" rx="42" ry="36" fill="{INK}"/>')
            else:
                out.append(
                    f'<ellipse cx="{cx}" cy="{mid}" rx="42" ry="36" fill="#FFFFFF" '
                    f'stroke="{BUBBLE_STROKE}" stroke-width="5"/>'
                )
    bottom = GRID_TOP + len(cast) * ROW_H
    out.append(
        f'<line x1="0" y1="{bottom}" x2="{width}" y2="{bottom}" stroke="{RULE}" stroke-width="7"/>'
    )
    out.append("</svg>")
    return "\n".join(out)


def render_grade_svg(ballot: Ballot) -> str:
    """The grade ballot: a column per grade word, one filled bubble per row."""
    title, cast, marks = ballot.title, ballot.cast, ballot.scores
    width = grade_width(ballot)
    dx = grade_col_dx(ballot.grades)
    H = height_for(ballot)
    plain = f'"{title}"' if ballot.quoted else title
    shown = f"&quot;{title}&quot;" if ballot.quoted else title
    out: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {H}" '
        f'width="{width}" height="{H}">',
        f'<rect width="{width}" height="{H}" fill="#FFFFFF"/>',
        f'<text x="{TITLE_X}" y="{TITLE_Y}" font-family="{FONT}" '
        f'font-size="{title_font_size(plain, width)}" font-weight="bold" '
        f'fill="{RUST}">{shown}</text>',
        f'<text x="{TITLE_X}" y="{HDR_WORST_Y}" font-family="{FONT}" '
        f'font-size="{GRADE_INSTRUCTION_SIZE}" font-weight="bold" fill="{INK}">'
        f'{esc(grade_instruction(ballot))}</text>',
    ]

    # Headings bottom-align on one baseline, so a one-word grade sits level with
    # the second line of a two-word one instead of floating above the row.
    for i, label in enumerate(ballot.grades):
        lines = grade_label_lines(label)
        for n, line in enumerate(lines):
            y = STAR_ROW_Y - (len(lines) - 1 - n) * GRADE_HDR_LINE_H
            out.append(
                f'<text x="{grade_col_x(i, dx)}" y="{y}" font-family="{FONT}" '
                f'font-size="{GRADE_HDR_SIZE}" font-weight="bold" fill="{INK}" '
                f'text-anchor="middle">{esc(line)}</text>'
            )

    for r, name in enumerate(cast):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            out.append(f'<rect x="0" y="{top}" width="{width}" height="{ROW_H}" fill="{ROW_TINT}"/>')
        out.append(
            f'<line x1="0" y1="{top}" x2="{width}" y2="{top}" stroke="{RULE}" stroke-width="7"/>'
        )
        out.append(
            f'<text x="{GRADE_NAME_X}" y="{mid + 22}" font-family="{FONT}" font-size="62" '
            f'font-weight="bold" fill="{INK}">{esc(name)}</text>'
        )
        for i in range(len(ballot.grades)):
            cx = grade_col_x(i, dx)
            if marks[r] is not None and i == marks[r]:
                out.append(f'<ellipse cx="{cx}" cy="{mid}" rx="42" ry="36" fill="{INK}"/>')
            else:
                out.append(
                    f'<ellipse cx="{cx}" cy="{mid}" rx="42" ry="36" fill="#FFFFFF" '
                    f'stroke="{BUBBLE_STROKE}" stroke-width="5"/>'
                )
    bottom = GRID_TOP + len(cast) * ROW_H
    out.append(
        f'<line x1="0" y1="{bottom}" x2="{width}" y2="{bottom}" stroke="{RULE}" stroke-width="7"/>'
    )
    out.append("</svg>")
    return "\n".join(out)


# Heavy grotesque, to match the slide art the original eight were captured from.
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
SS = 2  # supersampling factor: draw big, downscale -> antialiased edges
PNG_MAX_W = 900  # saved PNG width; the SVG keeps the full 1600 (see rasterize)


BODY_FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def _font(size: int, body: bool = False):
    from PIL import ImageFont

    for path in BODY_FONT_CANDIDATES if body else FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def _save_png(img, width: int, height: int, png_path: Path,
              max_w: int = 0) -> None:
    """Downscale for antialiasing, then quantize, then write.

    This is flat art in a handful of colors, and the LANCZOS pass is the only
    thing that invents more. Pages show these at 220–330 px, so 900 px still
    leaves ~2.7x for retina while cutting the file to ~14 kB — which is what
    makes one image per ballot affordable across a whole teaching set. The .svg
    beside it stays the full-resolution master.
    """
    from PIL import Image

    out_w = min(width, max_w or PNG_MAX_W)
    small = img.resize((out_w, round(height * out_w / width)), Image.LANCZOS)
    small.convert("P", palette=Image.ADAPTIVE, colors=64).save(png_path, optimize=True)


def rasterize(ballot: Ballot, png_path: Path) -> None:
    """Draw the ballot straight to a bitmap, mirroring render_svg's geometry."""
    from PIL import Image, ImageDraw

    if ballot.kind == "approval":
        return rasterize_approval(ballot, png_path)
    if ballot.kind == "grade":
        return rasterize_grade(ballot, png_path)

    def s(v: float) -> float:
        return v * SS

    title, cast, scores = ballot.title, ballot.cast, ballot.scores
    H = height_for(ballot)
    img = Image.new("RGB", (W * SS, H * SS), "#FFFFFF")
    d = ImageDraw.Draw(img)
    f_hdr, f_scale = _font(58 * SS), _font(60 * SS)
    f_name, f_bubble = _font(62 * SS), _font(44 * SS)

    dy = top_block_h(ballot)
    shown = f'"{title}"' if ballot.quoted else title
    f_title = _font(title_font_size(shown) * SS)
    d.text((s(TITLE_X), s(TITLE_Y)), shown, font=f_title, fill=RUST, anchor="ls")

    if ballot.subtitle:
        d.text((s(TITLE_X), s(TITLE_Y + SUB_GAP)), ballot.subtitle,
               font=_font(SUB_SIZE * SS), fill=INK, anchor="ls")
    f_instr = _font(HDR_SIZE * SS, body=True)
    for n, line in enumerate(ballot.header):
        y = TITLE_Y + (SUB_GAP if ballot.subtitle else 0) + HDR_GAP + n * HDR_LINE_H
        if ballot.header_bullets:
            d.text((s(BULLET_X), s(y)), "•", font=f_instr, fill=INK, anchor="ls")
        d.text((s(BULLET_TEXT_X if ballot.header_bullets else TITLE_X), s(y)), line,
               font=f_instr, fill=INK, anchor="ls")

    d.text((s(col_x(0) + 40), s(HDR_WORST_Y + dy)), "Worst", font=f_hdr, fill=INK, anchor="ms")
    d.text((s(col_x(5)), s(HDR_WORST_Y + dy)), "Best", font=f_hdr, fill=INK, anchor="ms")

    for i in range(6):
        cx = col_x(i)
        if i:
            pts = [(s(x), s(y)) for x, y in star_points(cx, STAR_ROW_Y + dy - 18, 62)]
            d.polygon(pts, outline=STAR_OUTLINE, width=int(s(6)))
        d.text((s(cx), s(STAR_ROW_Y + dy)), str(i), font=f_scale, fill=INK, anchor="ms")

    for r, name in enumerate(cast):
        top = GRID_TOP + dy + r * ROW_H
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

    bottom = GRID_TOP + dy + len(cast) * ROW_H
    d.line([0, s(bottom), s(W), s(bottom)], fill=RULE, width=int(s(7)))
    f_ftr = _font(FTR_SIZE * SS, body=True)
    for n, line in enumerate(ballot.footer):
        d.text((s(TITLE_X), s(bottom + FTR_GAP + n * FTR_LINE_H)), line,
               font=f_ftr, fill=INK, anchor="ls")
    _save_png(img, W, H, png_path)


def rasterize_approval(ballot: Ballot, png_path: Path) -> None:
    """The Yes/No ballot as a bitmap — mirrors render_approval_svg exactly."""
    from PIL import Image, ImageDraw

    def s(v: float) -> float:
        return v * SS

    title, cast, marks = ballot.title, ballot.cast, ballot.scores
    width = APPROVAL_W
    H = height_for(ballot)
    img = Image.new("RGB", (width * SS, H * SS), "#FFFFFF")
    d = ImageDraw.Draw(img)
    f_instr = _font(APPROVAL_INSTRUCTION_SIZE * SS)
    f_hdr, f_name = _font(60 * SS), _font(62 * SS)

    shown = f'"{title}"' if ballot.quoted else title
    f_title = _font(title_font_size(shown, width) * SS)
    d.text((s(TITLE_X), s(TITLE_Y)), shown, font=f_title, fill=RUST, anchor="ls")
    d.text((s(TITLE_X), s(HDR_WORST_Y)), APPROVAL_INSTRUCTION,
           font=f_instr, fill=INK, anchor="ls")

    for i, label in enumerate(APPROVAL_HEADERS):
        d.text((s(approval_col_x(i)), s(STAR_ROW_Y)), label,
               font=f_hdr, fill=INK, anchor="ms")

    for r, name in enumerate(cast):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            d.rectangle([0, s(top), s(width), s(top + ROW_H)], fill=ROW_TINT)
        d.line([0, s(top), s(width), s(top)], fill=RULE, width=int(s(7)))
        d.text((s(NAME_X), s(mid + 22)), name, font=f_name, fill=INK, anchor="ls")
        for i in range(len(APPROVAL_HEADERS)):
            cx = approval_col_x(i)
            box = [s(cx - 42), s(mid - 36), s(cx + 42), s(mid + 36)]
            if approval_filled(marks[r], i):
                d.ellipse(box, fill=INK)
            else:
                d.ellipse(box, fill="#FFFFFF", outline=BUBBLE_STROKE, width=int(s(5)))

    bottom = GRID_TOP + len(cast) * ROW_H
    d.line([0, s(bottom), s(width), s(bottom)], fill=RULE, width=int(s(7)))
    _save_png(img, width, H, png_path)


# Six grade words is a much wider drawing than six numerals, and a page shows it
# at roughly twice the width to compensate — so it is saved bigger too, or the
# headings that ARE the ballot would land at a handful of pixels each.
GRADE_PNG_MAX_W = 1400


def rasterize_grade(ballot: Ballot, png_path: Path) -> None:
    """The grade ballot as a bitmap — mirrors render_grade_svg exactly."""
    from PIL import Image, ImageDraw

    def s(v: float) -> float:
        return v * SS

    title, cast, marks = ballot.title, ballot.cast, ballot.scores
    width = grade_width(ballot)
    dx = grade_col_dx(ballot.grades)
    H = height_for(ballot)
    img = Image.new("RGB", (width * SS, H * SS), "#FFFFFF")
    d = ImageDraw.Draw(img)
    f_instr = _font(GRADE_INSTRUCTION_SIZE * SS)
    f_hdr, f_name = _font(GRADE_HDR_SIZE * SS), _font(62 * SS)

    shown = f'"{title}"' if ballot.quoted else title
    f_title = _font(title_font_size(shown, width) * SS)
    d.text((s(TITLE_X), s(TITLE_Y)), shown, font=f_title, fill=RUST, anchor="ls")
    d.text((s(TITLE_X), s(HDR_WORST_Y)), grade_instruction(ballot),
           font=f_instr, fill=INK, anchor="ls")

    for i, label in enumerate(ballot.grades):
        lines = grade_label_lines(label)
        for n, line in enumerate(lines):
            y = STAR_ROW_Y - (len(lines) - 1 - n) * GRADE_HDR_LINE_H
            d.text((s(grade_col_x(i, dx)), s(y)), line,
                   font=f_hdr, fill=INK, anchor="ms")

    for r, name in enumerate(cast):
        top = GRID_TOP + r * ROW_H
        mid = top + ROW_H / 2
        if r % 2 == 0:
            d.rectangle([0, s(top), s(width), s(top + ROW_H)], fill=ROW_TINT)
        d.line([0, s(top), s(width), s(top)], fill=RULE, width=int(s(7)))
        d.text((s(GRADE_NAME_X), s(mid + 22)), name, font=f_name, fill=INK, anchor="ls")
        for i in range(len(ballot.grades)):
            cx = grade_col_x(i, dx)
            box = [s(cx - 42), s(mid - 36), s(cx + 42), s(mid + 36)]
            if marks[r] is not None and i == marks[r]:
                d.ellipse(box, fill=INK)
            else:
                d.ellipse(box, fill="#FFFFFF", outline=BUBBLE_STROKE, width=int(s(5)))

    bottom = GRID_TOP + len(cast) * ROW_H
    d.line([0, s(bottom), s(width), s(bottom)], fill=RULE, width=int(s(7)))
    _save_png(img, width, H, png_path, max_w=GRADE_PNG_MAX_W)


def _write(slug: str, ballot: Ballot, want_png: bool) -> None:
    ballot.out_dir.mkdir(parents=True, exist_ok=True)
    svg_path = ballot.out_dir / f"{slug}.svg"
    svg_path.write_text(render_svg(ballot))
    print(f"wrote {_show(svg_path)}")
    if want_png:
        png_path = ballot.out_dir / f"{slug}.png"
        rasterize(ballot, png_path)
        print(f"wrote {_show(png_path)}")


def _show(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:  # a case file outside the repo (tmp dirs, tests)
        return str(path)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--svg-only", action="store_true", help="write .svg but skip the .png")
    ap.add_argument("--only", help="render just this slug (e.g. style_null_ballot)")
    ap.add_argument("--from-yaml", nargs="+", metavar="CASE.yaml",
                    help="draw one ballot per row of these election YAMLs into "
                         "<yaml dir>/img/ (instead of the gallery)")
    ap.add_argument("--refresh", action="store_true",
                    help="redraw the art of every case that already has some "
                         "(keeps pictures in step with edited ballots)")
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                    help=f"max ballots drawn per case file (default {DEFAULT_LIMIT})")
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

    if args.from_yaml or args.refresh:
        # --refresh keeps each case's existing depth; --from-yaml takes --limit.
        jobs = {Path(p): args.limit for p in (args.from_yaml or [])}
        if args.refresh:
            for src, drawn_to in refresh_targets().items():
                jobs.setdefault(src, drawn_to)
        failed = False
        for path, limit in jobs.items():
            try:
                drawn, total = ballots_from_yaml(path, limit=limit)
            except CaseBallotError as exc:
                print(f"! {path}: {exc}", file=sys.stderr)
                failed = True
                continue
            for slug, ballot in drawn:
                _write(slug, ballot, want_png)
            for stale in prune_art(path.parent / "img", path.stem, len(drawn)):
                print(f"removed {_show(stale)} (that ballot row is gone)")
            if total > len(drawn):
                # Never cap silently: a page that shows 8 of 40 ballots reads as
                # if it showed them all.
                print(f"  ({total - len(drawn)} more ballot rows not drawn — "
                      f"limit {limit}); raise --limit to draw them")
        return 1 if failed else 0

    for slug, ballot in BALLOTS.items():
        if args.only and slug != args.only:
            continue
        _write(slug, ballot, want_png)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
