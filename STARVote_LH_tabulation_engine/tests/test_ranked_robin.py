"""
test_ranked_robin.py
====================
Guards the first-class Ranked Robin (RCV-RR / Copeland) path in the LH engine.

A file with `voting_method: RankedRobin` (alias RCV_RR / Copeland / Consensus)
and ranked ballots must dispatch to `run_ranked_robin` — printing the round-robin
(ballots + pairwise table + win-loss record), NOT the RCV-IRV elimination rounds —
exit 0, elect the round-robin winner, and write its `_tabulated` sibling.

Also checks the cycle path: a Rock/Paper/Scissors profile must be reported as a
Condorcet cycle (3-way tie on wins), not silently resolved without a flag.
"""
import subprocess
import sys
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"
CANON = REPO_ROOT / "05_Ranked_Robin" / "_main" / "cases" / "ranked_robin_consensus_center.yaml"


def _run(path):
    return subprocess.run([sys.executable, str(WRAPPER), str(path)],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


def test_canonical_ranked_robin_file():
    """The repo's worked RR example dispatches to the round-robin and elects Ben."""
    r = _run(CANON)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert "Ranked Robin (RCV-RR / Copeland) Method" in out
    assert "Instant-Runoff" not in out and "Elimination" not in out
    assert "Round-Robin — every pair" in out          # the pairwise table
    assert "Ballots:" in out                            # ballots are shown
    assert "Winner — Ranked Robin (RCV-RR): Ben" in out
    # This file sets options: { show_matrix: true }, so the echo opts INTO the
    # full pairwise matrix. The _tabulated mirror always has it regardless.
    assert "Pairwise (Round-Robin) Matrix" in out
    tab = (REPO_ROOT / "05_Ranked_Robin" / "_main" / "cases" / "cases_tabulated"
           / "ranked_robin_consensus_center_tabulated.txt")
    assert tab.exists()
    mirror = tab.read_text()
    assert "Pairwise (Round-Robin) Matrix" in mirror
    assert "Legend: For - Equal Support - Against" in mirror


def test_echo_matrix_is_opt_in(tmp_path):
    """Default echo is compact (no matrix); show_matrix opts it in. The mirror
    always has the matrix either way."""
    base = ("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
            "  3:Ada>Ben>Cara\n  2:Ben>Cara>Ada\n  2:Cara>Ben>Ada\n")
    # default (no options) → compact echo, no matrix
    f1 = tmp_path / "compact.yaml"
    f1.write_text(base)
    r1 = _run(f1)
    assert r1.returncode == 0, r1.stderr
    assert "Pairwise (Round-Robin) Matrix" not in r1.stdout
    hits = list(tmp_path.parent.rglob("compact_tabulated.txt"))
    assert hits, "no _tabulated mirror was written"
    assert "Pairwise (Round-Robin) Matrix" in hits[0].read_text()
    # options: { show_matrix: true } → echo includes the matrix
    f2 = tmp_path / "full.yaml"
    f2.write_text(base + "options:\n  show_matrix: true\n")
    r2 = _run(f2)
    assert r2.returncode == 0, r2.stderr
    assert "Pairwise (Round-Robin) Matrix" in r2.stdout


def test_collapse_and_separator_options(tmp_path):
    """collapse_ballots and count_separator are honored by the RR echo."""
    base = ("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
            "  3:Ada>Ben>Cara\n  2:Ben>Cara>Ada\n  2:Cara>Ben>Ada\n")
    # custom separator
    fs = tmp_path / "sep.yaml"
    fs.write_text(base + 'options:\n  count_separator: ":"\n')
    rs = _run(fs)
    assert rs.returncode == 0, rs.stderr
    assert "3 : Ada > Ben > Cara" in rs.stdout
    assert "×" not in rs.stdout
    # collapse off → one row per voter (7 ballot rows, no count prefix)
    fc = tmp_path / "nocollapse.yaml"
    fc.write_text(base + "options:\n  collapse_ballots: false\n")
    rc = _run(fc)
    assert rc.returncode == 0, rc.stderr
    assert rc.stdout.count("Ada > Ben > Cara") == 3
    assert "3 ×" not in rc.stdout


def test_ranked_robin_aliases_and_cycle(tmp_path):
    """rcv_rr alias works, and a Condorcet cycle is flagged (not hidden)."""
    f = tmp_path / "rps.yaml"
    f.write_text(
        "voting_method: rcv_rr\nnum_winners: 1\nballots: |-\n"
        "  1:Rock>Scissors>Paper\n"
        "  1:Paper>Rock>Scissors\n"
        "  1:Scissors>Paper>Rock\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "Ranked Robin (RCV-RR / Copeland) Method" in r.stdout
    assert "Condorcet cycle" in r.stdout


def test_ranked_robin_bloc_multiwinner(tmp_path):
    """RankedRobin with num_winners>1 elects the top-N by record (Bloc RR) — it
    must NOT silently downgrade to a single winner (the old bug)."""
    f = tmp_path / "bloc_rr.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 3\n"
        "lot_numbers: [Dog, Cat, Fish, Bird, Rabbit, Hamster]\nballots: |-\n"
        "  13:Dog>Cat>Fish>Bird>Rabbit>Hamster\n"
        "  9:Bird>Rabbit>Hamster>Fish>Cat>Dog\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "3 winners" in r.stdout and "Winners — Ranked Robin" in r.stdout
    assert "single winner" not in r.stdout
    for name in ("Dog", "Cat", "Fish"):
        assert name in r.stdout


def test_plurality_multiwinner_sntv(tmp_path):
    """Multi-winner Plurality = SNTV: top-N by first-choice count. It must NOT
    error (the old missing-feature behavior) and must elect the two most-marked."""
    f = tmp_path / "sntv.yaml"
    f.write_text(
        "voting_method: Plurality\nnum_winners: 2\n"
        "lot_numbers: [Dog, Cat, Fish, Bird]\nballots: |-\n"
        "  Dog,Cat,Fish,Bird\n  13: 1,0,0,0\n  9: 0,0,0,1\n  4: 0,1,0,0\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "SNTV" in r.stdout and "2 winners" in r.stdout
    assert "Dog" in r.stdout and "Bird" in r.stdout


def test_ranked_robin_dead_heat_is_not_called_a_cycle(tmp_path):
    """A co-top DEAD HEAT (tied leaders that draw each other and both beat the
    rest) must be labelled 'dead heat', NOT 'Condorcet cycle' — cycle is reserved
    for a genuine directed loop. Two indifferent voters (Ada=Ben) create the
    head-to-head tie; the pre-published lot breaks it to Ada."""
    f = tmp_path / "dead_heat.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [Ada, Ben, Cara]\nballots: |-\n"
        "  Ada,Ben,Cara\n  5,5,0\n  5,5,0\n  4,3,1\n  3,4,1\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "tie for the most wins" in r.stdout
    assert "dead heat" in r.stdout
    assert "Condorcet cycle" not in r.stdout
    assert "Ranked Robin (RCV-RR): Ada" in r.stdout


def test_equal_rankings_are_ties(tmp_path):
    """Ranked Robin reads an equal-rank level (A=B>C) as a TIE between A and B,
    not as one phantom candidate literally named 'A=B'. Regression for the
    parser that split ballots only on '>' (see README_larry_hastings.md change
    log). Every ballot ties two candidates at some level; the winner and the
    pairwise field must contain only the three real candidates."""
    f = tmp_path / "equal_ranks.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "options:\n  show_matrix: true\nballots: |-\n"
        "  4:Ada>Ben=Cara\n  3:Ben>Ada=Cara\n  2:Cara>Ada=Ben\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    # Ada beats Ben 4-3 and Cara 4-2 -> 2-0, the round-robin winner.
    assert "Ranked Robin (RCV-RR): Ada" in out
    # No phantom candidate: the '=' groups must never appear as a matrix ROW
    # label or a round-robin competitor ("Name >" / "Name beats"). (They DO
    # legitimately appear in the ballot echo, e.g. "Ada > Ben=Cara".)
    for phantom in ("Ben=Cara >", "Ada=Cara >", "Ada=Ben >",
                    "Ben=Cara beats", "Ada=Ben beats", "Ada=Cara beats"):
        assert phantom not in out, f"phantom equal-rank candidate leaked: {phantom!r}"
    # The tie is scored as Equal Support in the matrix (middle column).
    assert "Equal Support" in out


# --- Weak vs strict Condorcet winner in the RR verdict line -------------------
# The report used to test only "no losses", so an UNDEFEATED-BUT-TIED winner was
# announced as "beats every opponent head-to-head — the Condorcet winner" —
# contradicting the pairwise table printed a few lines above it, and (because
# engine output gets pasted verbatim into teaching pages) propagating a false
# claim into published material. Both branches are locked below; the strings
# must be changed here and in run_ranked_robin() together.

STRICT_WHY = "beats every opponent head-to-head — the Condorcet winner."
WEAK_WHY = ("undefeated, but ties Ben — a weak Condorcet winner "
            "(beats or ties every opponent), not the strict Condorcet winner.")

# Ben ties Cal 2-2 and ties Ada 2-2; Cal beats Ada 4-0. Cal is therefore 1-0-1:
# undefeated, but NOT a strict Condorcet winner — a weak one.
WEAK_BALLOTS = ("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
                "  2:Ben>Cal>Ada\n  2:Cal>Ada>Ben\n")


def test_weak_condorcet_winner_is_not_called_the_condorcet_winner(tmp_path):
    """Undefeated + at least one DRAW = a *weak* Condorcet winner. Saying it
    'beats every opponent head-to-head' contradicts the report's own table:
    a tie is not a win (cf. the weak-Condorcet-loser footnote in
    00_start_here/topics/criteria_at_a_glance.md)."""
    f = tmp_path / "weak_cw.yaml"
    f.write_text(WEAK_BALLOTS)
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert "Winner — Ranked Robin (RCV-RR): Cal" in out
    # The table itself says Cal is 1-0-1 and ties Ben — the premise of the test.
    assert "Cal        1–0–1" in out
    assert "Ben  ties  Cal" in out
    assert WEAK_WHY in out
    assert STRICT_WHY not in out, "weak Condorcet winner announced as the strict one"
    # The _tabulated mirror is what gets pasted into teaching pages — it must
    # carry the corrected verdict too, not just the on-screen echo.
    hits = list(tmp_path.parent.rglob("weak_cw_tabulated.txt"))
    assert hits, "no _tabulated mirror was written"
    mirror = hits[0].read_text()
    assert WEAK_WHY in mirror
    assert STRICT_WHY not in mirror


def test_strict_condorcet_winner_keeps_its_wording(tmp_path):
    """The other branch is unchanged: a winner who actually beats everyone
    head-to-head (no losses AND no ties) is still the Condorcet winner."""
    f = tmp_path / "strict_cw.yaml"
    f.write_text("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
                 "  3:Ada>Ben>Cara\n  2:Ben>Cara>Ada\n  2:Cara>Ben>Ada\n")
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    # Ben beats Cara and Ada: 2-0-0, a strict Condorcet winner.
    assert "Winner — Ranked Robin (RCV-RR): Ben" in out
    assert "Ben        2–0–0" in out
    assert STRICT_WHY in out
    assert "weak Condorcet winner" not in out


def test_winner_with_losses_still_reports_most_wins(tmp_path):
    """Third branch, unchanged: a winner who LOSES a matchup claims neither the
    strict nor the weak Condorcet title — just the most head-to-head wins."""
    # Ben is 2-1-0 — the unique leader on raw wins AND on Copeland (2.0 vs 1.5,
    # 1.5, 1.0), so this fixture stays valid whichever of the two the sort key
    # ends up using.
    f = tmp_path / "most_wins.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [Ada, Ben, Cara, Dan]\nballots: |-\n"
        "  2:Ada>Ben>Cara>Dan\n  1:Ben>Cara>Ada>Dan\n  1:Ben>Dan>Cara>Ada\n"
        "  2:Dan>Cara>Ada>Ben\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert "Winner — Ranked Robin (RCV-RR): Ben" in out
    assert "Ben        2–1–0" in out
    assert "the most head-to-head wins (2)." in out
    assert STRICT_WHY not in out
    assert "weak Condorcet winner" not in out
