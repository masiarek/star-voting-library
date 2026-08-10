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
CANON = REPO_ROOT / "05_Ranked_Robin" / "02_Examples" / "cases" / "ranked_robin_consensus_center.yaml"


def _run(path):
    return subprocess.run([sys.executable, str(WRAPPER), str(path)],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


# The exact strict-Condorcet claim. Named because it is asserted from BOTH sides:
# present when the winner really beats everyone, absent otherwise. A one-sided
# `not in` check would stay green if the phrase were dropped from the engine.
STRICT_WHY = "beats every opponent head-to-head — the Condorcet winner."


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
    # The full pairwise matrix is ON by default (flipped 2026-08-09 — the
    # round-robin table IS the method). The _tabulated mirror always has it.
    assert "Pairwise (Round-Robin) Matrix" in out
    tab = (REPO_ROOT / "05_Ranked_Robin" / "02_Examples" / "cases" / "cases_tabulated"
           / "ranked_robin_consensus_center_tabulated.txt")
    assert tab.exists()
    mirror = tab.read_text()
    assert "Pairwise (Round-Robin) Matrix" in mirror
    assert "Legend: For - Equal Support - Against" in mirror


def test_echo_matrix_default_on_with_opt_out(tmp_path):
    """The pairwise matrix is ON by default (flipped 2026-08-09 — the table IS
    the method, and case files carry no options); show_matrix: false still
    gives the compact echo. The mirror has the matrix either way."""
    base = ("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
            "  3:Ada>Ben>Cara\n  2:Ben>Cara>Ada\n  2:Cara>Ben>Ada\n")
    # default (no options) → the echo includes the matrix
    f1 = tmp_path / "default.yaml"
    f1.write_text(base)
    r1 = _run(f1)
    assert r1.returncode == 0, r1.stderr
    assert "Pairwise (Round-Robin) Matrix" in r1.stdout
    # options: { show_matrix: false } → compact echo, no matrix on screen —
    # but the always-full mirror still carries it.
    f2 = tmp_path / "compact.yaml"
    f2.write_text(base + "options:\n  show_matrix: false\n")
    r2 = _run(f2)
    assert r2.returncode == 0, r2.stderr
    assert "Pairwise (Round-Robin) Matrix" not in r2.stdout
    hits = list(tmp_path.parent.rglob("compact_tabulated.txt"))
    assert hits, "no _tabulated mirror was written"
    assert "Pairwise (Round-Robin) Matrix" in hits[0].read_text()


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
    # No DRAWS anywhere in a clean RPS loop, so tying on Copeland is tying on wins
    # and the report keeps the plainer phrasing. It switches to naming the Copeland
    # score only when a draw makes "most wins" untrue — see the dead-heat test.
    assert "tie for the most wins (Rock, Scissors, Paper)" in r.stdout, r.stdout
    assert "Copeland score" not in r.stdout.split("***")[1]


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
    assert "tie on the highest Copeland score" in r.stdout
    assert "dead heat" in r.stdout
    assert "Condorcet cycle" not in r.stdout
    assert "Ranked Robin (RCV-RR): Ada" in r.stdout


def test_ranked_robin_ranks_by_copeland_not_raw_wins(tmp_path):
    """The ranking key must be the Copeland score (wins + ½·ties), i.e. the very
    column the report prints — NOT the raw win count.

    Regression for a bug where `order` sorted on `len(wins[c])` while the table
    printed wins + ½·ties, so the two disagreed as soon as a pairwise DRAW existed.
    On this profile B holds 1 win / 2 losses (Copeland 1) while A and D are each
    unbeaten at 1–0–2 (Copeland 2); the raw-wins key tied all three at one win,
    then handed the election to B on margin — a candidate its own table ranked
    third, and one that loses two of its three matchups. A must win, and the
    printed order must be non-increasing in the Copeland column."""
    f = tmp_path / "copeland_key.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [A, B, C, D]\nballots: |-\n"
        "  6:A=B=D>C\n  7:A=C=D>B\n  6:B>C>A=D\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "Ranked Robin (RCV-RR): A" in r.stdout, r.stdout
    assert "Ranked Robin (RCV-RR): B" not in r.stdout
    # Only A and D share the top Copeland score, and they DRAW — a dead heat.
    assert "tie on the highest Copeland score (2): A, D" in r.stdout, r.stdout
    # The table must never rank a lower Copeland score above a higher one.
    rows = [ln.split() for ln in r.stdout.splitlines()
            if ln.strip().startswith(("1  ", "2  ", "3  ", "4  "))]
    scores = [float(cols[3]) for cols in rows if len(cols) > 3]
    assert scores == sorted(scores, reverse=True), scores


def test_weak_condorcet_winner_is_not_called_the_condorcet_winner(tmp_path):
    """An unbeaten candidate who DRAWS someone is a *weak* Condorcet winner, and the
    report must not claim they "beat every opponent head-to-head".

    Regression for a guard that tested only `not losses[winner]`. Cal goes 1–0–1 —
    beating Ada, drawing Ben — and was announced as "the Condorcet winner", which is
    false: a draw is not a win. Smith vs Schwartz turns on exactly this distinction."""
    f = tmp_path / "weak_condorcet.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [Ada, Ben, Cal]\nballots: |-\n"
        "  2:Ben>Cal>Ada\n  2:Cal>Ada>Ben\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "Ranked Robin (RCV-RR): Cal" in r.stdout, r.stdout
    assert STRICT_WHY not in r.stdout, r.stdout
    assert "weak" in r.stdout and "not a strict one" in r.stdout, r.stdout
    assert "draws Ben" in r.stdout, r.stdout
    # The _tabulated mirror is what gets pasted verbatim into teaching pages, so
    # the corrected verdict has to reach it too — not just the on-screen echo.
    hits = list(tmp_path.parent.rglob("weak_condorcet_tabulated.txt"))
    assert hits, "no _tabulated mirror was written"
    mirror = hits[0].read_text()
    assert STRICT_WHY not in mirror
    assert "not a strict one" in mirror


def test_strict_condorcet_winner_keeps_its_wording(tmp_path):
    """The other side of the weak-Condorcet guard: a winner who really does beat
    everyone head-to-head (no losses AND no draws) must still be announced as the
    Condorcet winner.

    Without this, the weak-winner test above is one-sided — deleting the strict
    claim from the engine outright would leave the suite green."""
    f = tmp_path / "strict_cw.yaml"
    f.write_text("voting_method: RankedRobin\nnum_winners: 1\nballots: |-\n"
                 "  3:Ada>Ben>Cara\n  2:Ben>Cara>Ada\n  2:Cara>Ben>Ada\n")
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    # Ben beats Cara and Ada outright: 2-0-0, a strict Condorcet winner.
    assert "Ranked Robin (RCV-RR): Ben" in out, out
    assert "Ben        2–0–0" in out, out
    assert STRICT_WHY in out, out
    assert "weak" not in out.split("Winner —")[1], out


def test_winner_with_losses_still_reports_most_wins(tmp_path):
    """Third verdict branch: a winner who LOSES a matchup claims neither the strict
    nor the weak Condorcet title — just the most head-to-head wins."""
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
    assert "Ranked Robin (RCV-RR): Ben" in out, out
    assert "Ben        2–1–0" in out, out
    assert "the most head-to-head wins (2)." in out, out
    assert STRICT_WHY not in out, out
    assert "weak" not in out.split("Winner —")[1], out


def test_copeland_verdict_when_winner_has_both_a_loss_and_a_draw(tmp_path):
    """Fourth verdict branch: losses AND draws together, where neither the
    Condorcet wording nor the raw win count is exact.

    Ada goes 2-1-1 — she LOSES to Cara — yet wins on Copeland 2.5, because the
    half-credit for her draw edges her past three rivals sitting on 2.0. So the
    report must fall through to naming the Copeland score and its formula, and
    must not imply she beat everyone or led on raw wins (Cara and Dan match her
    two wins)."""
    f = tmp_path / "cope_verdict.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [Ada, Ben, Cara, Dan, Eve]\nballots: |-\n"
        "  9:Ada>Eve>Dan>Ben>Cara\n  8:Cara>Ben>Ada>Eve>Dan\n"
        "  7:Dan>Ben>Cara>Ada>Eve\n  6:Cara>Ada>Dan>Eve>Ben\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert "Ranked Robin (RCV-RR): Ada" in out, out
    assert "Ada        2–1–1" in out, out
    # The premise: she lost a matchup, and rivals tie her on raw wins.
    assert "Cara       2–2–0" in out, out
    assert "the highest Copeland score (2.5 = wins + ½·ties)." in out, out
    assert STRICT_WHY not in out, out
    assert "the most head-to-head wins" not in out, out


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


def test_ranked_robin_decided_leaders_are_not_called_a_cycle(tmp_path):
    """The THIRD shape of a tie, and the one that read worst: Cara and Dan tie on
    the Copeland tally, and Cara BEATS Dan head-to-head (2-1). That is not a dead
    heat (there is a win in it) and it cannot be a Condorcet cycle (a 2-cycle would
    need each to beat the other), yet the line used to announce "a Condorcet cycle
    (no candidate beats all others)" — about two candidates one of whom beat the
    other. Tying on the overall tally says nothing about the shape underneath."""
    f = tmp_path / "mixed_leaders.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [Ada, Ben, Cara, Dan]\nballots: |-\n"
        "  Ada,Ben,Cara,Dan\n  0,0,0,1\n  0,0,3,1\n  3,3,1,0\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    assert "tie on the highest Copeland score" in r.stdout
    assert "tied on the tally, not a cycle" in r.stdout
    assert "Condorcet cycle" not in r.stdout
    assert "dead heat" not in r.stdout
    assert "Ranked Robin (RCV-RR): Cara" in r.stdout


def test_copeland_winner_helper_matches_the_rr_report():
    """`copeland_winner()` feeds the [Divergence from STAR] block, so it must use
    the SAME key as `run_ranked_robin` — half-credit for draws included. When it
    used raw wins, a STAR file could name one RCV-RR winner in its divergence
    block while the very same ballots as a RankedRobin file elected another.

    Profile: A ties C and beats B and D (Copeland 2.5); D holds as many RAW wins
    (2, over B and C) with a bigger margin — so a raw-wins ranking crowned D even
    though D had LOST to A head-to-head 37-20."""
    sys.path.insert(0, str(ENGINE_DIR))
    import starvote_larry_hastings as LH

    cands = ["A", "B", "C", "D"]
    rows = [(16, [3, 3, 5, 2]), (20, [1, 2, 3, 5]),
            (21, [4, 1, 2, 2]), (15, [5, 1, 1, 5])]
    ballots = [dict(zip(cands, scores)) for n, scores in rows for _ in range(n)]
    assert LH.copeland_winner(cands, ballots, cands) == "A"

    # ...and on a dead heat: Ada and Ben both 1–0–1 (Copeland 1.5, equal margin);
    # the priority order breaks it to Ada, exactly as the RR report's lot does.
    dc = ["Ada", "Ben", "Cara"]
    db = [dict(zip(dc, s)) for s in ([5, 5, 0], [5, 5, 0], [4, 3, 1], [3, 4, 1])]
    assert LH.copeland_winner(dc, db, dc) == "Ada"
