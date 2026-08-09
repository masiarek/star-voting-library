"""
test_default_render.py
======================
Locks the GLOBAL display defaults (`DEFAULT_OPTIONS`) and their auto-gates,
introduced 2026-08-09 when the teaching case files dropped their per-file
`options:` blocks — the engine's own defaults ARE the house style now.

Behaviour locked here:
  * a single-winner score race (3+ candidates) shows the finalists matrix and
    hides the scenario_description and [Score Distribution] by default;
  * a TWO-candidate race auto-suppresses the matrix (it would just echo the
    runoff);
  * a MULTI-WINNER race auto-suppresses the matrix (a "Top 2 Finalist" grid is
    a single-winner concept) — but a file's `show_matrix: true` still wins;
  * whenever a MULTI-WINNER race DOES render the grid (a file override, the
    always-full `_tabulated` mirror, `--full`), it renders as plain
    head-to-head data: retitled "Preference Matrix", no Top-2 finalist
    markers (they come from a silent seats=1 STAR analysis), and an
    "Informational only" legend line in their place;
  * `--full` puts the everything-on mirror render on screen (full grid, score
    distribution, description, and the "Runoff math" funnel).

The runoff-summary default (on by default, opt-out honored) is locked by
test_runoff_percent.py; the Ranked Robin matrix default by
test_ranked_robin.py.
"""

import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"

MATRIX_HEADER = "--- Runoff (Preference) Matrix ---"
FINALIST_LEGEND = "* indicates Top 2 Finalist"
MW_MATRIX_HEADER = "--- Preference Matrix ---"
MW_MATRIX_NOTE = "so no Top-2 finalists are marked"
SCORE_DIST = "[Score Distribution]"
FUNNEL = "Runoff math:"
DESC_MARKER = "UNIQUE-DESC-MARKER"

# Decided runoff (no tie): scores Ada=19 Ben=16 Cara=5; runoff Ada 3, Ben 1,
# Equal Support 1 — same shape as the test_runoff_percent fixture.
SW3 = (
    f"election_title: Default render\n"
    f"scenario_description: A {DESC_MARKER} sentence.\n"
    "voting_method: STAR\nnum_winners: 1\nballots: |-\n"
    "  Ada,Ben,Cara\n  5,4,0\n  5,4,0\n  2,5,0\n  3,3,0\n  4,0,5\n"
)

SW2 = (
    "voting_method: STAR\nnum_winners: 1\nballots: |-\n"
    "  Ada,Ben\n  5,2\n  1,4\n  5,0\n"
)

MW4 = (
    "voting_method: bloc\nnum_winners: 2\nballots: |-\n"
    "  Ada,Ben,Cara,Dave\n  5,4,1,0\n  5,4,0,1\n  4,5,2,0\n  0,3,5,4\n  1,2,4,5\n"
)


def _run(path, *extra):
    return subprocess.run(
        [sys.executable, str(WRAPPER), str(path), *extra],
        cwd=str(ENGINE_DIR), capture_output=True, text=True,
    )


def _write(tmp_path, text, name="case.yaml"):
    d = tmp_path / "d"
    d.mkdir(exist_ok=True)
    p = d / name
    p.write_text(text, encoding="utf-8")
    return p


def test_single_winner_default_render(tmp_path):
    r = _run(_write(tmp_path, SW3))
    assert r.returncode == 0, r.stdout + r.stderr
    out = r.stdout
    assert MATRIX_HEADER in out, out          # finalists matrix ON by default
    assert FINALIST_LEGEND in out, out
    assert DESC_MARKER not in out, out        # description hidden by default
    assert SCORE_DIST not in out, out         # score distribution stays opt-in
    assert "Voters with a preference:" in out, out  # runoff summary ON


def test_two_candidate_race_suppresses_matrix(tmp_path):
    # With two candidates the matrix would just echo the runoff — auto-off.
    r = _run(_write(tmp_path, SW2))
    assert r.returncode == 0, r.stdout + r.stderr
    assert MATRIX_HEADER not in r.stdout, r.stdout


def test_multiwinner_suppresses_matrix(tmp_path):
    # A "Top 2 Finalist" grid is a single-winner concept — auto-off for Bloc/PR.
    r = _run(_write(tmp_path, MW4))
    assert r.returncode == 0, r.stdout + r.stderr
    assert MATRIX_HEADER not in r.stdout, r.stdout


def test_multiwinner_file_override_wins(tmp_path):
    # The auto-gate is a DEFAULT, not a gag: a file's own options still win —
    # but the grid a multi-winner file forces on is the UNMARKED one (plain
    # head-to-head data, no seats=1 "Top 2 Finalist" markers).
    text = MW4.replace("ballots: |-", "options:\n  show_matrix: true\nballots: |-")
    r = _run(_write(tmp_path, text))
    assert r.returncode == 0, r.stdout + r.stderr
    assert MW_MATRIX_HEADER in r.stdout, r.stdout
    assert MW_MATRIX_NOTE in r.stdout, r.stdout
    assert MATRIX_HEADER not in r.stdout, r.stdout
    assert "Top 2 Finalist" not in r.stdout, r.stdout


def test_multiwinner_mirror_grid_is_unmarked(tmp_path):
    # The always-full `_tabulated` mirror keeps the pairwise grid for a
    # multi-winner race (maximum info), but as plain head-to-head data:
    # retitled, no finalist markers, and the "Informational only" legend
    # naming the reason. Nothing locked this before 2026-08-09 — the mirror
    # carried a "Top 2 Finalist" grid from the silent seats=1 STAR analysis.
    p = _write(tmp_path, MW4)
    r = _run(p)
    assert r.returncode == 0, r.stdout + r.stderr
    mirror = p.parent / f"{p.parent.name}_tabulated" / f"{p.stem}_tabulated.txt"
    assert mirror.exists(), f"mirror not written: {mirror}"
    out = mirror.read_text(encoding="utf-8")
    assert MW_MATRIX_HEADER in out, out
    assert MW_MATRIX_NOTE in out, out
    assert "2-winner count" in out, out        # the note names the seat count
    assert MATRIX_HEADER not in out, out
    assert "Top 2 Finalist" not in out, out
    assert "Ada >" in out, out                 # the grid itself is present


def test_full_flag_shows_everything(tmp_path):
    # --full = the mirror's render on screen: full grid, score distribution,
    # description, and the expanded "Runoff math" funnel.
    r = _run(_write(tmp_path, SW3), "--full")
    assert r.returncode == 0, r.stdout + r.stderr
    out = r.stdout
    assert MATRIX_HEADER in out, out
    assert SCORE_DIST in out, out
    assert DESC_MARKER in out, out
    assert FUNNEL in out, out
