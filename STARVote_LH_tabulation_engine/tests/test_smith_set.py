"""
test_smith_set.py
=================
Guards the Smith-set analysis the engine appends to `_tabulated` mirrors.

The Smith set is the smallest non-empty group of candidates such that every
member beats every candidate OUTSIDE it head-to-head. Two jobs in the report:

  * Ranked Robin (RCV-RR / Copeland) is Smith-efficient, so the block is
    descriptive — it names the club and states the guarantee.
  * RCV-IRV is NOT Smith-efficient, so the block is a genuine PASS/FAIL: it says
    whether the eliminations walked out of the set.

House contract (same as show_runoff_percent): OFF in the on-screen echo by
default, ALWAYS ON in the `_tabulated` mirror, opt-in on screen via
`options: { show_smith_set: true }`.
"""
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import starvote_larry_hastings as lh          # noqa: E402

ENGINE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = ENGINE_DIR.parent
WRAPPER = ENGINE_DIR / "starvote_larry_hastings.py"


def _run(path):
    return subprocess.run([sys.executable, str(WRAPPER), str(path)],
                          capture_output=True, text=True, cwd=str(ENGINE_DIR))


def _matrix(candidates, beats):
    """Synthetic pairwise matrix: (for, against, no-preference) per ordered pair.
    `beats` is the set of (winner, loser) pairs; anything unlisted both ways is a
    draw."""
    m = defaultdict(lambda: defaultdict(tuple))
    for a in candidates:
        for b in candidates:
            if a == b:
                m[a][b] = (0, 0, 10)
            elif (a, b) in beats:
                m[a][b] = (6, 4, 0)
            elif (b, a) in beats:
                m[a][b] = (4, 6, 0)
            else:
                m[a][b] = (5, 5, 0)             # pairwise draw
    return m


# --------------------------------------------------------------------------
# the set itself
# --------------------------------------------------------------------------

def test_condorcet_winner_is_a_singleton_smith_set():
    """A lone Condorcet winner IS the Smith set — the one-member club."""
    cands = list("ABC")
    m = _matrix(cands, {("A", "B"), ("A", "C"), ("B", "C")})
    assert lh.smith_set(cands, m) == ["A"]


def test_top_cycle_plus_an_outsider():
    """The worked repo demo: a 3-cycle beats a universally-last candidate, so the
    club is the cycle and the outsider is provably out of contention."""
    cands = list("ABCD")
    beats = {("A", "B"), ("B", "C"), ("C", "A"),
             ("A", "D"), ("B", "D"), ("C", "D")}
    assert sorted(lh.smith_set(cands, _matrix(cands, beats))) == ["A", "B", "C"]


def test_smith_set_can_be_wider_than_the_copeland_leaders():
    """The tell the win-loss table alone cannot show: the Copeland leaders are
    always INSIDE the Smith set but need not BE it.

    A beats B,C; B beats C,D; C beats D; D beats A; everyone beats E.
    Copeland leaders are {A, B} at 3 wins, but the Smith set is {A, B, C, D}."""
    cands = list("ABCDE")
    beats = {("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"),
             ("C", "D"), ("D", "A")} | {(x, "E") for x in "ABCD"}
    m = _matrix(cands, beats)
    assert sorted(lh.smith_set(cands, m)) == ["A", "B", "C", "D"]
    block = "\n".join(lh.format_smith_set(cands, m))
    assert "Copeland leaders (A, B) are only part of the set" in block


def test_a_draw_keeps_both_candidates_in_the_club():
    """A draw is not a win, so it cannot push anyone out — that is exactly where
    Smith and Schwartz part company, and the report says so."""
    cands = list("ABC")
    beats = {("A", "C"), ("B", "C")}            # A and B draw each other
    m = _matrix(cands, beats)
    assert sorted(lh.smith_set(cands, m)) == ["A", "B"]
    block = "\n".join(lh.format_smith_set(cands, m))
    assert "pairwise DRAW" in block and "Schwartz" in block


def test_universal_cycle_puts_everyone_in_the_club():
    cands = list("ABC")
    assert sorted(lh.smith_set(cands, _matrix(
        cands, {("A", "B"), ("B", "C"), ("C", "A")}))) == ["A", "B", "C"]


# --------------------------------------------------------------------------
# the verdict line
# --------------------------------------------------------------------------

def test_inside_versus_outside_verdicts():
    cands = list("ABC")
    m = _matrix(cands, {("A", "B"), ("A", "C"), ("B", "C")})   # A is the CW
    inside = "\n".join(lh.format_smith_set(cands, m, winner="A",
                                           method_label="RCV-IRV"))
    assert "INSIDE the Smith set. ✓" in inside
    assert "Not guaranteed" in inside              # IRV earns no guarantee
    outside = "\n".join(lh.format_smith_set(cands, m, winner="B",
                                            method_label="RCV-IRV"))
    assert "OUTSIDE the Smith set. ✗" in outside
    assert "not Smith-efficient" in outside


def test_ranked_robin_verdict_states_the_guarantee():
    cands = list("ABC")
    m = _matrix(cands, {("A", "B"), ("A", "C"), ("B", "C")})
    block = "\n".join(lh.format_smith_set(
        cands, m, winner="A", method_label="Ranked Robin (RCV-RR)",
        smith_efficient=True))
    assert "Guaranteed:" in block and "Smith-efficient" in block


# --------------------------------------------------------------------------
# wiring: echo vs mirror
# --------------------------------------------------------------------------

RR_YAML = """title: Smith set echo contract
voting_method: RankedRobin
num_winners: 1
ballots: |-
  3:Ada>Ben>Cara>Dave
  2:Ben>Cara>Ada>Dave
  2:Cara>Ada>Ben>Dave
"""


def test_mirror_always_has_it_echo_does_not(tmp_path):
    """House contract: minimal echo, full mirror."""
    src = tmp_path / "rr_smith.yaml"
    src.write_text(RR_YAML, encoding="utf-8")
    r = _run(src)
    assert r.returncode == 0, r.stderr
    assert "Smith Set" not in r.stdout           # OFF on screen by default
    mirror = (tmp_path / f"{tmp_path.name}_tabulated" / "rr_smith_tabulated.txt")
    assert mirror.exists()
    text = mirror.read_text(encoding="utf-8")
    assert "--- Smith Set (the generalized Condorcet winner) ---" in text
    assert "Smith set (3 of 4): Ada, Ben, Cara" in text
    assert "Outside (1):        Dave" in text
    assert "INSIDE the Smith set. ✓" in text


def test_show_smith_set_option_opts_the_echo_in(tmp_path):
    src = tmp_path / "rr_smith_on.yaml"
    src.write_text(RR_YAML.replace(
        "ballots: |-", "options:\n  show_smith_set: true\nballots: |-"),
        encoding="utf-8")
    r = _run(src)
    assert r.returncode == 0, r.stderr
    assert "--- Smith Set (the generalized Condorcet winner) ---" in r.stdout
    # ...and it did NOT drag the full matrix along with it (separate options).
    assert "Pairwise (Round-Robin) Matrix" not in r.stdout


def test_bloc_rr_names_the_set_but_claims_no_single_winner(tmp_path):
    """With several seats, "the winner is inside the set" has no single referent,
    so the block names the club and stops."""
    src = tmp_path / "rr_bloc.yaml"
    src.write_text(RR_YAML.replace("num_winners: 1", "num_winners: 2"),
                   encoding="utf-8")
    r = _run(src)
    assert r.returncode == 0, r.stderr
    text = (tmp_path / f"{tmp_path.name}_tabulated"
            / "rr_bloc_tabulated.txt").read_text(encoding="utf-8")
    assert "Smith set (3 of 4): Ada, Ben, Cara" in text
    assert "INSIDE the Smith set" not in text
    assert "OUTSIDE the Smith set" not in text


def test_irv_mirror_flags_a_winner_outside_the_club():
    """The repo's basic RCV-IRV example is a center squeeze: C beats A 60-40 and
    B 65-35 (so the Smith set is {C}), yet C is eliminated first and A wins. The
    mirror has to say so — this is the pass/fail the block exists for."""
    src = REPO_ROOT / "06_Other" / "RCV_IRV" / "cases" / "RCV_ballot_example.yaml"
    r = _run(src)
    assert r.returncode == 0, r.stderr
    assert "Smith Set" not in r.stdout            # mirror only, not the echo
    text = (src.parent / "cases_tabulated"
            / "RCV_ballot_example_tabulated.txt").read_text(encoding="utf-8")
    assert "Smith set (1 of 3): C" in text
    assert "RCV-IRV winner A is OUTSIDE the Smith set. ✗" in text
    assert "not Smith-efficient" in text
