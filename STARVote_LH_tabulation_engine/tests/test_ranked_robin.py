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
    assert "tie for the top Copeland score" in r.stdout
    assert "dead heat" in r.stdout
    assert "Condorcet cycle" not in r.stdout
    assert "Ranked Robin (RCV-RR): Ada" in r.stdout


def test_copeland_score_decides_not_raw_wins(tmp_path):
    """The `Copeland` column must be the column that DECIDES.

    Regression for a real bug: the report printed `wins + ½·ties` but sorted by
    RAW `len(wins)`, so the two disagreed the moment any matchup was drawn. On
    this profile the pairwise results are

        A beats B 36–20 · A ties C 36–36 · A beats D 37–20
        C beats B 57–0  · D beats B 56–16 · D beats C 35–16

    which gives A a Copeland score of 2.5 (2 wins + 1 draw) against D's 2. Sorted
    by raw wins the two both showed "2" and D's bigger margin (+42 vs +33) put D
    on top — so the engine crowned D while printing A at the head of the Copeland
    column, and D had *lost to A head-to-head 37–20*.

    Three things are asserted, one per symptom:
      1. A is ranked #1 and wins (the printed score decides).
      2. A — undefeated — is not passed over for a candidate it beat.
      3. NO "Condorcet cycle" is claimed: the strict edges A→B, A→D, C→B, D→B,
         D→C are acyclic, and A's draw with C is a draw, not a loop.

    Cross-checks: BetterVoting's RankedRobin.ts scores "win +1, tie +0.5" and
    pref_voting's Copeland (wins − losses) induces the same order, so half-credit
    is what keeps LH agreeing with both.
    """
    f = tmp_path / "cope_decides.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [A, B, C, D]\nballots: |-\n"
        "  Count:A,B,C,D\n"
        "  16:3,3,5,2\n"
        "  20:1,2,3,5\n"
        "  21:4,1,2,2\n"
        "  15:5,1,1,5\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    # the tally itself, so a future ballot-parsing change can't silently move the
    # goalposts and leave the assertions below passing for the wrong reason
    assert "A  ties  C" in out and "A  beats D" in out and "D  beats C" in out
    # 1 + 2 — highest Copeland (2.5), undefeated, and it WINS
    assert "Winner — Ranked Robin (RCV-RR): A" in out
    assert "weak Condorcet winner" in out
    rows = [ln for ln in out.splitlines() if ln.strip().startswith(("1 ", "2 "))]
    assert rows[0].split()[1] == "A" and "2.5" in rows[0], rows
    assert rows[1].split()[1] == "D", rows
    # 3 — acyclic profile: no cycle may be claimed
    assert "Condorcet cycle" not in out
    assert "dead heat" not in out


def test_unbeaten_but_outscored_is_disclosed(tmp_path):
    """Copeland does NOT guarantee electing an unbeaten candidate — half-credit
    means a record full of draws can be tied or out-scored by someone who lost a
    matchup. LH keeps the Copeland rule (so it still agrees with BetterVoting and
    pref_voting) but must SAY SO rather than pass the unbeaten candidate over in
    silence. Here Dev is 1–0–2 (never beaten) and ties Ada on Copeland 2; Ada
    takes it on the published lot, and the report has to disclose Dev."""
    f = tmp_path / "unbeaten_outscored.yaml"
    f.write_text(
        "voting_method: RankedRobin\nnum_winners: 1\n"
        "lot_numbers: [Ada, Ben, Cara, Dev]\nballots: |-\n"
        "  Ada,Ben,Cara,Dev\n  3,0,0,5\n  0,0,0,0\n  5,5,5,0\n  5,3,3,5\n  0,5,3,2\n"
    )
    r = _run(f)
    assert r.returncode == 0, r.stderr
    out = r.stdout
    assert "Winner — Ranked Robin (RCV-RR): Ada" in out
    assert "Dev is never beaten head-to-head" in out
    assert "weak Condorcet winner" in out
    assert "Condorcet cycle" not in out          # Ada→Ben→Cara etc. has no loop


def test_copeland_winner_helper_matches_the_rr_report():
    """`copeland_winner()` feeds the [Divergence from STAR] block, so it must use
    the SAME key as `run_ranked_robin` — half-credit for draws included. When it
    used raw wins, a STAR file could name one RCV-RR winner in its divergence
    block while the very same ballots as a RankedRobin file elected another.

    Checked on the profile above (A undefeated, Copeland 2.5, but only as many raw
    wins as D) plus the co-top dead heat, where the two must also agree."""
    sys.path.insert(0, str(ENGINE_DIR))
    import starvote_larry_hastings as LH

    cands = ["A", "B", "C", "D"]
    rows = [(16, [3, 3, 5, 2]), (20, [1, 2, 3, 5]),
            (21, [4, 1, 2, 2]), (15, [5, 1, 1, 5])]
    ballots = [dict(zip(cands, scores)) for n, scores in rows for _ in range(n)]
    assert LH.copeland_winner(cands, ballots, cands) == "A"

    # dead heat: Ada and Ben both 1–0–1 (Copeland 1.5); the lot breaks it to Ada,
    # exactly as the RR report does.
    dc = ["Ada", "Ben", "Cara"]
    db = [dict(zip(dc, s)) for s in ([5, 5, 0], [5, 5, 0], [4, 3, 1], [3, 4, 1])]
    assert LH.copeland_winner(dc, db, dc) == "Ada"


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
