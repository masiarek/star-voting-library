"""
test_matrix_finalists.py
========================
Locks the Runoff (Preference) Matrix `*` markers — and the
`matrix_finalists_only` filter that reuses the same set — to the pair that
ACTUALLY advanced to the Automatic Runoff.

The bug this guards against: the finalists were recomputed for the matrix as
"top two by total score, score ties broken by lot order", which is NOT how
STAR picks the second finalist. starvote's Scoring Round runs a ladder —
total score, then the head-to-head preference round, then the five-star
count, then lot — so whenever a tie for the second slot is settled by one of
the LATER rungs, ranking by score alone names the wrong candidate. The report
would say "Ana and Cora advance" while the matrix starred Ana and *Ben*, and
`matrix_finalists_only: true` would filter the grid down to Ana-vs-Ben, a
matchup that never happened.

Seven committed cases were printing the wrong pair, including the
center-squeeze teaching case (`bv2137_ywckmg_star`, which starred Reagan
though Anderson and Carter advanced) and the ice-cream tie-break ladder.

Fixture election (scores 0-5) — the tie is broken by the FIRST rung, so the
score order and the true finalists disagree:

    Ana,Ben,Cora,Dev
    5,5,4,0
    5,4,5,2
    3,3,4,3
    1,0,1,3
    1,2,0,3

  Scores: Ana 15, Ben 14, Cora 14, Dev 11 -> Ana advances, Ben/Cora tie.
  Head-to-head among the tied pair: Cora 3, Ben 2 -> CORA advances.
  So the runoff is Ana vs Cora, and Ben must NOT be starred even though he
  outranks Cora in lot/column order (the old tiebreak the matrix applied).
"""

import re
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

BALLOTS = "  Ana,Ben,Cora,Dev\n  5,5,4,0\n  5,4,5,2\n  3,3,4,3\n  1,0,1,3\n  1,2,0,3\n"

ADVANCING = {"Ana", "Cora"}
ELIMINATED_RUNNER_UP = "Ben"   # ties Cora on score, loses the head-to-head rung


def _run_cli(path):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path)],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _write(tmp_path, *, finalists_only, ballots=BALLOTS, name="case"):
    d = tmp_path / f"{name}-{'only' if finalists_only else 'full'}"
    d.mkdir()
    p = d / f"{name}.yaml"
    p.write_text(
        "voting_method: STAR\n"
        "num_winners: 1\n"
        "options:\n"
        "  show_matrix: true\n"
        f"  matrix_finalists_only: {'true' if finalists_only else 'false'}\n"
        "ballots: |-\n" + ballots
    )
    return p


def _matrix_header(text):
    """The matrix's column-header line (the one naming every column).

    Skips the optional tiebreak note, which sits between the legend and the
    grid — so this stays anchored on the columns, not on whatever prose the
    legend happens to carry.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if "indicates Top 2 Finalist" not in line:
            continue
        for candidate_line in lines[i + 1:]:
            if "|" in candidate_line:
                return candidate_line
        break
    raise AssertionError("no matrix header found:\n" + text)


def _starred(header):
    return {c.replace("*", "").strip() for c in header.split("|") if "*" in c}


def _columns(header):
    return {c.replace("*", "").strip() for c in header.split("|") if c.strip()}


def _note(text):
    """The matrix's tiebreak note, unwrapped back to one line ('' if absent)."""
    lines = text.splitlines()
    start = next((i + 1 for i, line in enumerate(lines)
                  if "indicates Top 2 Finalist" in line), None)
    assert start is not None, "no matrix legend found:\n" + text
    if start >= len(lines) or not lines[start].lstrip().startswith("Note:"):
        return ""
    out = [lines[start].strip()[len("Note:"):].strip()]
    for line in lines[start + 1:]:
        if not line.startswith(" " * 14) or not line.strip():
            break
        out.append(line.strip())
    return " ".join(out)


def _runoff_pair(text):
    """The two candidates starvote actually ran the Automatic Runoff between.

    Anchored on the round HEADING — bare on screen, bracketed in the mirror
    (`[STAR Voting: Automatic Runoff Round]`) — because the surrounding prose
    names the round too, and splitting on the first mention lands in a
    sentence rather than in the tally.
    """
    lines = text.splitlines()
    start = next(
        (i + 1 for i, line in enumerate(lines)
         if line.strip().strip("[]").endswith("Automatic Runoff Round")),
        None,
    )
    assert start is not None, "no Automatic Runoff Round heading:\n" + text
    names = set()
    for line in lines[start:]:
        if not line.strip():
            break
        m = re.match(r"^\s{3}(\S.*?)\s+--\s+\d", line)
        if m:
            names.add(m.group(1).strip())
    names.discard("Equal Support")
    return names


# --- the tiebroken fixture --------------------------------------------------

def test_report_advances_the_tiebreak_winner(tmp_path):
    # Guards the premise: the FIRST tiebreaker rung really does decide this,
    # so the rest of the file is testing what it thinks it is.
    proc = _run_cli(_write(tmp_path, finalists_only=False))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Ana and Cora advance." in proc.stdout, proc.stdout
    assert _runoff_pair(proc.stdout) == ADVANCING, proc.stdout


def test_stars_match_the_advancing_pair(tmp_path):
    proc = _run_cli(_write(tmp_path, finalists_only=False))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    starred = _starred(_matrix_header(proc.stdout))
    assert starred == ADVANCING, f"starred {sorted(starred)}\n{proc.stdout}"


def test_score_runner_up_is_not_starred(tmp_path):
    # The regression itself: Ben ties Cora on score and wins the old
    # lot/column-order tiebreak, so the buggy code starred him.
    proc = _run_cli(_write(tmp_path, finalists_only=False))
    starred = _starred(_matrix_header(proc.stdout))
    assert ELIMINATED_RUNNER_UP not in starred, proc.stdout


def test_finalists_only_filters_to_the_advancing_pair(tmp_path):
    # `matrix_finalists_only` reuses the same set, so the bug also filtered the
    # grid down to a matchup that never happened.
    proc = _run_cli(_write(tmp_path, finalists_only=True))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    header = _matrix_header(proc.stdout)
    assert _columns(header) == ADVANCING, proc.stdout
    assert _starred(header) == ADVANCING, proc.stdout


# --- the tiebreak note ------------------------------------------------------
#
# The stars alone still read as a contradiction to anyone who only has the
# scores in front of them: the higher-scoring candidate is unstarred, and
# under `matrix_finalists_only` they are gone from the grid entirely. The note
# says which rung moved them.

# Ben and Cora tie at 6; the head-to-head is 1-1; Ben holds the only five, so
# the SECOND rung settles it. Exercises a rung the main fixture never reaches.
FIVE_STAR_BALLOTS = "  Ana,Ben,Cora\n  5,5,3\n  5,1,3\n"

# Nothing ties: the note must stay off, so ordinary reports are unchanged.
NO_TIE_BALLOTS = "  Ada,Ben,Cal\n  5,3,0\n  4,2,1\n  5,1,0\n"


def test_note_names_the_tie_the_rung_and_who_advanced(tmp_path):
    proc = _run_cli(_write(tmp_path, finalists_only=False))
    note = _note(proc.stdout)
    assert "Ben and Cora tied at 14 in the Scoring Round" in note, note
    assert "the head-to-head rung advanced Cora" in note, note
    assert "The * marks who advanced, not who scored highest." in note, note


def test_note_reports_the_five_star_rung(tmp_path):
    proc = _run_cli(_write(tmp_path, finalists_only=False,
                           ballots=FIVE_STAR_BALLOTS, name="fivestar"))
    note = _note(proc.stdout)
    assert "Ben and Cora tied at 6" in note, note
    assert "the five-star rung advanced Ben" in note, note


def test_note_absent_when_no_tie_reached_the_ladder(tmp_path):
    # House "less is more": an ordinary election gains nothing on screen.
    proc = _run_cli(_write(tmp_path, finalists_only=False,
                           ballots=NO_TIE_BALLOTS, name="notie"))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "Note:" not in proc.stdout.split("Runoff (Preference) Matrix")[1], proc.stdout


def test_note_explains_the_gap_when_the_grid_is_filtered(tmp_path):
    # The case that motivated the note: `matrix_finalists_only` drops Ben, so
    # the head-to-head that settled the slot is nowhere on the page.
    proc = _run_cli(_write(tmp_path, finalists_only=True))
    note = _note(proc.stdout)
    assert "Ben is filtered out of this grid" in note, note
    assert "see the Scoring Round" in note, note


def test_note_agrees_with_the_stars(tmp_path):
    # Belt and braces: the prose and the markers come from one resolver, so a
    # future refactor cannot let them disagree.
    proc = _run_cli(_write(tmp_path, finalists_only=False))
    note = _note(proc.stdout)
    starred = _starred(_matrix_header(proc.stdout))
    advanced = re.search(r"rung advanced ([^.]+)\.", note).group(1)
    named = {n.strip() for n in advanced.replace(" and ", ", ").split(",")}
    assert named <= starred, f"note says {named}, matrix stars {starred}"


# --- the same invariant, across every committed mirror ----------------------

REPO_ROOT = ENGINE_DIR.parent


def _mirrors_with_a_star_runoff():
    for mirror in REPO_ROOT.rglob("*_tabulated.txt"):
        try:
            text = mirror.read_text(errors="replace")
        except OSError:
            continue
        if "indicates Top 2 Finalist" not in text:
            continue
        if "Automatic Runoff Round" not in text:
            continue
        yield mirror, text


def test_every_mirror_stars_its_own_runoff_pair():
    """No shipped `_tabulated` report may star a candidate it eliminated.

    The fixture above only proves the fix for one shape of tie. This walks the
    library so a future change to the finalist ladder can't quietly re-break
    the 300-odd committed reports.
    """
    wrong = []
    for mirror, text in _mirrors_with_a_star_runoff():
        starred = _starred(_matrix_header(text))
        pair = _runoff_pair(text)
        # `matrix_finalists_only` mirrors show only the finalists; either way the
        # starred set must be exactly the pair that reached the runoff.
        if starred != pair:
            wrong.append(
                f"  {mirror.relative_to(REPO_ROOT)}\n"
                f"      starred {sorted(starred)} but {sorted(pair)} advanced"
            )
    assert not wrong, (
        f"{len(wrong)} report(s) star a candidate that did not reach the runoff:\n"
        + "\n".join(wrong)
        + "\nRe-run those YAMLs through the engine to refresh their mirrors."
    )


def test_every_mirror_note_agrees_with_its_own_runoff():
    """Where a shipped report explains a tiebreak, the prose must be true.

    A note that names the wrong candidate is worse than no note: it is a
    confident sentence contradicting the tally three lines below it.
    """
    wrong = []
    checked = 0
    for mirror, text in _mirrors_with_a_star_runoff():
        note = _note(text)
        if not note:
            continue
        checked += 1
        m = re.search(r"rung(?: \([^)]*\))? advanced ([^.]+)\.", note)
        if not m:
            wrong.append(f"  {mirror.relative_to(REPO_ROOT)}\n"
                         f"      unparseable note: {note!r}")
            continue
        named = {n.strip() for n in m.group(1).replace(" and ", ", ").split(",")}
        pair = _runoff_pair(text)
        if not named <= pair:
            wrong.append(
                f"  {mirror.relative_to(REPO_ROOT)}\n"
                f"      note says {sorted(named)} advanced, but the runoff was "
                f"{sorted(pair)}"
            )
    assert checked, "no mirror carries a tiebreak note — is the note still wired up?"
    assert not wrong, (
        f"{len(wrong)} of {checked} tiebreak note(s) disagree with their own "
        f"report:\n" + "\n".join(wrong)
    )
