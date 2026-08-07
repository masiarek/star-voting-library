# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""condorcet_efficiency_simulation.py — how often does each method elect the Condorcet winner?

THE QUESTION. "STAR's Condorcet efficiency is very high" is asserted all over the
reform literature (and, until this script existed, in several pages of this repo)
without a number anyone can reproduce. Condorcet efficiency has a precise definition:

    Condorcet efficiency = P(method elects the Condorcet winner | a Condorcet winner exists)

The conditional matters. Elections with a CYCLE have no Condorcet winner, so no method
can elect one; folding them in would drag every method's score down by the cycle rate
and measure the electorate, not the method. Those elections are excluded from the
denominator and reported separately as "CW exists %".

WHAT IT MEASURES. One set of sampled voter utilities feeds six methods, so the
comparison is apples-to-apples — every method reads the SAME electorate, just through
its own ballot:

    Ranked Robin (Copeland)  ranking       -- must be 100.0%; it is the control
    STAR                     0-5 scores    -- top two by sum, then a pairwise runoff
    Score (Range)            0-5 scores    -- highest sum
    Approval                 0/1           -- sincere cutoff (default: score >= 4)
    RCV-IRV (Hare)           ranking       -- eliminate fewest first choices
    Plurality                one mark      -- most first choices

RANKED ROBIN IS THE CONTROL, NOT A RESULT. Copeland is Condorcet-efficient by
construction, so its column is a self-check on the harness: any cell below 100.0%
means the pairwise code and the method code disagree, and every other number in the
run is suspect. It is printed for exactly that reason.

THE STAR MECHANISM SPLIT. A Condorcet winner who REACHES STAR's runoff wins it (they
beat any opponent head-to-head), so STAR can only miss the CW two ways:
  (a) top-two miss  -- the CW never reaches the runoff, having placed third or worse
                       on score. The real mechanism: a broadly-preferred, low-intensity
                       compromise, everyone's tepid second choice.
  (b) grid loss     -- the CW reached the runoff and STILL lost. This looks impossible
                       and isn't: the CW is defined on true UTILITIES, but the runoff
                       is counted on the 0-5 SCORE ballot, and rounding to six rungs
                       can turn a real (if slim) preference into an exact tie. It is
                       the measurable cost of the ballot's resolution, not of STAR's
                       rule, and it is small -- see the README.
The two are counted separately because they say completely different things.

*** THIS SCRIPT DOES NOT DEFINE ITS OWN STAR. ***
It imports star_winner() from star_vs_rr_divergence.py, which implements the LH
engine's tie-break rungs and is held to the real engine by
STARVote_LH_tabulation_engine/tests/test_sim_star_model.py. Re-implementing STAR here
would create a second model to drift; there is deliberately only one.

Usage:  uv run 06_Other/simulations/condorcet_efficiency_simulation.py
        uv run 06_Other/simulations/condorcet_efficiency_simulation.py --selftest
        uv run 06_Other/simulations/condorcet_efficiency_simulation.py --trials 20000 --seed 7
        uv run 06_Other/simulations/condorcet_efficiency_simulation.py --approval-cutoff 3
        uv run 06_Other/simulations/condorcet_efficiency_simulation.py --chart
        uv run 06_Other/simulations/condorcet_efficiency_simulation.py --why --voters 501
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from star_vs_rr_divergence import (          # noqa: E402  - path set above
    _fill,
    _resolve,
    _totals,
    gen,
    pairwise,
    scores_from_util,
    star_winner,
)

METHODS = ["RankedRobin", "STAR", "Score", "Approval", "RCV-IRV", "Plurality"]


# --- the Condorcet winner, from true preferences -----------------------------
def condorcet_winner(util):
    """Index of the candidate who beats every other head-to-head, or -1 (a cycle).

    Computed from UTILITIES — the voters' real preferences — not from any ballot.
    That is the standard definition and the only fair one here: if the CW were read
    off the 0-5 score ballot, STAR would be graded against a target its own ballot
    had already shaped, and Approval's cruder ballot would look better than it is by
    the same trick.
    """
    W = pairwise(util)                        # W[i, j] = ballots preferring i to j
    beats = W > W.T
    won = np.where(beats.sum(1) == util.shape[1] - 1)[0]
    return int(won[0]) if len(won) else -1


# --- the methods -------------------------------------------------------------
def score_winner(scores):
    """Range/Score voting: highest 0-5 sum. Ties -> lowest column index (lot)."""
    return int(scores.sum(0).argmax())


def approval_winner(scores, cutoff):
    """Sincere approval: approve everyone you would score >= cutoff on the STAR ballot.

    The cutoff is a MODELLING CHOICE, not a fact about Approval — it is the whole
    reason Approval has no single Condorcet-efficiency number. Sweep it with
    --approval-cutoff to watch the column move.
    """
    return int((scores >= cutoff).sum(0).argmax())


def star_finalists(scores):
    """The two candidates STAR actually advances to the runoff.

    This is the first half of star_winner(), sharing its helpers, so the mechanism
    split below is keyed to the finalists STAR *really* picked. Doing it the obvious
    way instead -- argsort(-scores.sum(0))[:2] -- silently disagrees whenever the
    score round ties for second, and a tie for second is exactly the situation the
    grid-loss column is about, so the error would land squarely on the number it was
    meant to measure.
    """
    seated, tied = _fill(_totals(scores, range(scores.shape[1])), 2)
    if tied:
        seated = seated + _resolve(scores, tied, 2 - len(seated))
    return set(seated)


def plurality_winner(util):
    """Most first choices. Ties -> lowest column index (lot)."""
    return int(np.bincount(util.argmax(1), minlength=util.shape[1]).argmax())


def irv_winner(util):
    """RCV-IRV (Hare): eliminate the fewest-first-choices candidate until a majority.

    Elimination ties break to the lowest column index — arbitrary, and identically
    arbitrary for every method here, which is what keeps the comparison honest.
    """
    V, C = util.shape
    alive = np.ones(C, dtype=bool)
    while alive.sum() > 1:
        first = np.where(alive, util, -np.inf).argmax(1)      # favourite among the living
        counts = np.bincount(first, minlength=C)
        if counts.max() * 2 > V:                              # outright majority
            return int(counts.argmax())
        live = np.flatnonzero(alive)
        alive[live[counts[live].argmin()]] = False            # lot: lowest index
    return int(np.flatnonzero(alive)[0])


def winners(util, scores, cutoff):
    """Every method's winner for one election, keyed by name."""
    W = pairwise(util)
    beats = W > W.T
    ties = (W == W.T) & ~np.eye(util.shape[1], dtype=bool)
    copeland = beats.sum(1) + 0.5 * ties.sum(1)
    return {
        "RankedRobin": int(copeland.argmax()),
        "STAR": star_winner(scores),
        "Score": score_winner(scores),
        "Approval": approval_winner(scores, cutoff),
        "RCV-IRV": irv_winner(util),
        "Plurality": plurality_winner(util),
    }


# --- the sweep ---------------------------------------------------------------
def run_cell(rng, model, V, C, trials, cutoff):
    """Returns (CW-exists rate, {method: Condorcet efficiency}, STAR mechanism split)."""
    have_cw = 0
    hits = {m: 0 for m in METHODS}
    top_two_miss = grid_loss = 0
    for _ in range(trials):
        util = gen(rng, model, V, C)
        scores = scores_from_util(util)
        cw = condorcet_winner(util)
        if cw < 0:                                            # a cycle: no target to hit
            continue
        have_cw += 1
        won = winners(util, scores, cutoff)
        for m in METHODS:
            hits[m] += won[m] == cw
        if won["STAR"] != cw:                                 # why did STAR miss?
            if cw in star_finalists(scores):
                grid_loss += 1                                # reached the runoff, still lost
            else:
                top_two_miss += 1                             # never reached the runoff
    if not have_cw:
        return 0.0, {m: float("nan") for m in METHODS}, (0.0, 0.0)
    eff = {m: hits[m] / have_cw for m in METHODS}
    split = (top_two_miss / have_cw, grid_loss / have_cw)
    return have_cw / trials, eff, split


def sweep(rng, trials, cutoff, models, cands, voters):
    head = f"{'model':<10}{'C':>3}{'V':>6}  {'CW exists':>10} |"
    for m in METHODS:
        head += f"{m:>12}"
    head += f" |{'STAR: top-2 miss':>18}{'grid loss':>11}"
    print(head)
    print("-" * len(head))
    for model in models:
        for C in cands:
            for V in voters:
                cw_rate, eff, (miss, grid) = run_cell(rng, model, V, C, trials, cutoff)
                row = f"{model:<10}{C:>3}{V:>6}  {cw_rate*100:9.1f}% |"
                for m in METHODS:
                    row += f"{eff[m]*100:11.1f}%"
                row += f" |{miss*100:17.1f}%{grid*100:10.1f}%"
                print(row)
        print()


# --- the same numbers, drawn ---------------------------------------------------
BAR_WIDTH = 12                                    # characters at 100%


def _bar(pct):
    """A fixed-width bar. Deliberately plain block characters and nothing else: the
    output is pasted into Markdown pages that must render identically on GitHub, on the
    built site and in a plain text editor, so no colour and no partial glyphs."""
    filled = int(round(pct / 100 * BAR_WIDTH))
    return "█" * filled + "·" * (BAR_WIDTH - filled)


def chart(rng, trials, cutoff, models, cands, voters):
    """Condorcet efficiency as a bar chart, one block per (model, electorate size).

    Same numbers as the sweep -- this mode only draws them. The shape it exists to make
    visible is the one the table buries: EVERY method's bar shrinks as the field grows,
    and the control's does not, because Ranked Robin cannot miss. How fast the others
    shrink is the whole subject of
    07_Concepts/topics/condorcet/why_more_candidates_miss.md.
    """
    print("Condorcet efficiency = P(elects the Condorcet winner | one exists).")
    print(f"{trials} elections per bar, sincere approval cutoff score >= {cutoff}. "
          f"Ranked Robin is the CONTROL and must read 100%.\n")

    # Draw from the SAME random stream, in the same order, as sweep() -- so with the
    # same flags every bar here is the same number as the corresponding table cell in
    # 07_Concepts/topics/condorcet/condorcet_efficiency_measured.md, not a fresh sample
    # that lands a point away and makes the two pages look like they disagree.
    eff = {}
    for model in models:
        for C in cands:
            for V in voters:
                _, e, _ = run_cell(rng, model, V, C, trials, cutoff)
                eff[(model, V, C)] = e

    for model in models:
        for V in voters:
            print(f"{model} — {V} voters")
            print((" " * 12 + "  ".join(f"{str(C) + ' candidates':<{BAR_WIDTH + 6}}"
                                        for C in cands)).rstrip())
            for m in METHODS:
                print(f"{m:<12}" + "  ".join(
                    f"{_bar(eff[(model, V, C)][m] * 100)}{eff[(model, V, C)][m] * 100:4.0f}%"
                    for C in cands))
            drops = [f"{m} {(eff[(model, V, cands[0])][m] - eff[(model, V, cands[-1])][m]) * 100:.0f}"
                     for m in METHODS if m != "RankedRobin"]
            print(f"{'':12}{cands[0]} → {cands[-1]} candidates, percentage points lost: "
                  + ", ".join(drops))
            print()


# --- what actually changes when the field grows? -------------------------------
def why(rng, trials, models, cands, voters):
    """Measure the three things a bigger field does to an election, so the explanation
    on 07_Concepts/topics/condorcet/why_more_candidates_miss.md is evidence and not
    just a story. All three are properties of the ELECTORATE, not of any method:

      CW 1st %      the Condorcet winner's share of first choices. This is what
                    Choose-One counts and what RCV-IRV eliminates on, so when it falls
                    below the pack the CW goes out early -- and it falls purely because
                    more candidates stand between them and their voters.
      CW margin     the Condorcet winner's NARROWEST head-to-head win, in percentage
                    points. A wider field packs rivals closer, so the margin the ballot
                    has to preserve gets thinner.
      pairs tied    the share of candidate PAIRS an average 0-5 ballot cannot separate.
                    Six rungs hold at most 6 distinct ranks, so past 6 candidates the
                    pigeonhole makes ties compulsory -- this is the score ballot running
                    out of room, measured.

    Read the three together: the first explains the choose-one family, the third
    explains the score family, and the second explains why both get worse at once.
    """
    print("What a bigger field does to the election itself (not to any method).\n")
    print(f"{'model':<10}{'C':>3}{'V':>6} | {'CW 1st %':>10}{'CW margin':>11}"
          f"{'pairs tied':>12}")
    print("-" * 54)
    for model in models:
        for V in voters:
            for C in cands:
                first_share = margin = tied = n = 0.0
                for _ in range(trials):
                    util = gen(rng, model, V, C)
                    cw = condorcet_winner(util)
                    if cw < 0:
                        continue
                    n += 1
                    counts = np.bincount(util.argmax(1), minlength=C)
                    first_share += counts[cw] / V
                    W = pairwise(util)
                    others = [j for j in range(C) if j != cw]
                    margin += min((W[cw, j] - W[j, cw]) / V for j in others)
                    s = scores_from_util(util)
                    eq = sum(int((s[:, i] == s[:, j]).sum())
                             for i in range(C) for j in range(i + 1, C))
                    tied += eq / (V * C * (C - 1) / 2)
                if not n:
                    continue
                print(f"{model:<10}{C:>3}{V:>6} | {first_share/n*100:9.1f}%"
                      f"{margin/n*100:10.1f}%{tied/n*100:11.1f}%")
        print()
    print("Ranked Robin reads the margin column and is unaffected by the other two,\n"
          "which is exactly why its efficiency stays at 100% while everyone else's falls.")


# --- why does a grid loss happen? --------------------------------------------
def mechanism(rng, trials, cutoff, models, cands, voters):
    """Split the grid losses into 'exact tie' vs 'outright reversal' on the 0-5 ballot.

    A grid loss is an election where the Condorcet winner REACHED STAR's runoff and
    lost it, which sounds impossible. It isn't, and this mode shows why. Each voter's
    scores are a monotone transform of their utilities, so rounding can never flip an
    individual ballot -- it can only flatten a real preference into a tie. But it
    flattens DIFFERENT voters at different rates, and that is enough to move the
    aggregate: if the CW's supporters hold them by narrow margins (rounded away) while
    the opponent's supporters hold theirs by wide ones (preserved), the head-to-head
    can come out the other way on scores than it does on true preferences.

    So the two outcomes are:
      exact tie  -- the runoff tied on the score ballot and fell to a later rung
      reversal   -- the score ballot genuinely reversed the head-to-head
    'unexplained' must stay 0; anything else means this account is incomplete.
    """
    print("Grid losses — the CW reached STAR's runoff and lost. Why?\n")
    print(f"{'model':<10}{'C':>3}{'V':>6} | {'grid losses':>12}{'exact tie':>11}"
          f"{'reversal':>11}{'unexplained':>13}")
    print("-" * 68)
    for model in models:
        for C in cands:
            for V in voters:
                tie = rev = other = 0
                for _ in range(trials):
                    util = gen(rng, model, V, C)
                    scores = scores_from_util(util)
                    cw = condorcet_winner(util)
                    if cw < 0 or star_winner(scores) == cw:
                        continue
                    finalists = star_finalists(scores)
                    if cw not in finalists:
                        continue                              # a top-two miss, not a grid loss
                    opp = next(i for i in finalists if i != cw)
                    for_cw = int((scores[:, cw] > scores[:, opp]).sum())
                    for_opp = int((scores[:, opp] > scores[:, cw]).sum())
                    if for_cw == for_opp:
                        tie += 1
                    elif for_opp > for_cw:
                        rev += 1
                    else:
                        other += 1
                total = tie + rev + other
                print(f"{model:<10}{C:>3}{V:>6} | {total:>12}{tie:>11}{rev:>11}{other:>13}")
        print()
    print("Reversal dominating is the finding: most of the shortfall is preference the "
          "0-5 ballot could not carry,\nnot the top-two rule discarding a candidate. "
          "Read the README's caveat on ballot resolution before quoting it.")


# --- known-answer checks -----------------------------------------------------
def _center_squeeze():
    """The textbook squeeze: B is the Condorcet winner; IRV and Plurality miss them.

    40 voters A>B>C, 13 B>A>C, 12 B>C>A, 35 C>B>A.
      pairwise  B beats A 60-40 and beats C 65-35  -> B is the CW
      IRV       first choices A 40, B 25, C 35 -> B eliminated -> A 53, C 47 -> A
      Plurality A (40)
      STAR      score sums A 239, B 350, C 211 -> runoff B vs A -> B 60-40 -> B
    """
    rows = [(40, [1.0, 0.6, 0.0]), (13, [0.5, 1.0, 0.0]),
            (12, [0.0, 1.0, 0.5]), (35, [0.0, 0.6, 1.0])]
    return np.repeat(np.array([u for _, u in rows]), [n for n, _ in rows], axis=0)


def _clear_winner():
    """No disagreement to have: A is the CW and every method elects them."""
    rows = [(30, [1.0, 0.4, 0.0]), (25, [1.0, 0.0, 0.3]), (20, [0.9, 0.5, 0.0])]
    return np.repeat(np.array([u for _, u in rows]), [n for n, _ in rows], axis=0)


def selftest():
    """Known-answer checks. Every method's behaviour here is hand-verifiable."""
    ok = True

    util = _center_squeeze()
    scores = scores_from_util(util)
    cw = condorcet_winner(util)
    won = winners(util, scores, 4)
    expected = {"cw": 1, "RankedRobin": 1, "STAR": 1, "Score": 1,
                "RCV-IRV": 0, "Plurality": 0, "Approval": 0}
    print("center squeeze (A=0, B=1, C=2) — B is the Condorcet winner")
    print(f"  Condorcet winner : {cw}  (expect {expected['cw']})")
    ok &= cw == expected["cw"]
    for m in METHODS:
        hit = "elects CW" if won[m] == cw else "MISSES CW"
        good = won[m] == expected[m]
        ok &= good
        print(f"  {m:<12} -> {won[m]}  {hit:<10} {'ok' if good else 'UNEXPECTED'}")

    util = _clear_winner()
    scores = scores_from_util(util)
    cw = condorcet_winner(util)
    won = winners(util, scores, 4)
    print("\nclear winner — every method should elect A (=0)")
    ok &= cw == 0
    for m in METHODS:
        good = won[m] == 0
        ok &= good
        print(f"  {m:<12} -> {won[m]}  {'ok' if good else 'UNEXPECTED'}")

    # The control column must be exactly 100% on random elections, or the harness lies.
    rng = np.random.default_rng(20260727)
    _, eff, _ = run_cell(rng, "spatial2d", 25, 4, 300, 4)
    print(f"\nRanked Robin control on 300 random elections: {eff['RankedRobin']*100:.1f}%"
          "  (must be exactly 100.0%)")
    ok &= eff["RankedRobin"] == 1.0

    print("\nSELFTEST", "PASSED" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--trials", type=int, default=4000, help="elections per cell")
    ap.add_argument("--seed", type=int, default=20260727)
    ap.add_argument("--approval-cutoff", type=int, default=4, metavar="N",
                    help="sincere approval = every candidate you'd score >= N (default 4)")
    ap.add_argument("--models", nargs="+",
                    default=["noise", "spatial1d", "spatial2d", "faction2d"])
    ap.add_argument("--candidates", nargs="+", type=int, default=[3, 5, 7])
    ap.add_argument("--voters", nargs="+", type=int, default=[51, 501])
    ap.add_argument("--selftest", action="store_true",
                    help="run known-answer checks only and exit")
    ap.add_argument("--mechanism", action="store_true",
                    help="instead of the sweep, break the grid losses down into exact "
                         "ties vs outright reversals on the 0-5 ballot")
    ap.add_argument("--why", action="store_true",
                    help="instead of the sweep, measure what a bigger field does to the "
                         "election itself: the CW's first-choice share, their narrowest "
                         "head-to-head margin, and how much of the 0-5 ballot goes tied")
    ap.add_argument("--chart", action="store_true",
                    help="instead of the sweep, draw the same efficiencies as bars, "
                         "grouped by field size (what more candidates cost each method)")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if a.chart:
        chart(np.random.default_rng(a.seed), a.trials, a.approval_cutoff,
              a.models, a.candidates, a.voters)
        return 0
    if a.why:
        why(np.random.default_rng(a.seed), a.trials, a.models, a.candidates, a.voters)
        return 0
    if a.mechanism:
        mechanism(np.random.default_rng(a.seed), a.trials, a.approval_cutoff,
                  a.models, a.candidates, a.voters)
        return 0

    print(f"Condorcet efficiency = P(elects the CW | a CW exists).  "
          f"{a.trials} elections/cell, seed {a.seed}, "
          f"sincere approval cutoff score >= {a.approval_cutoff}.")
    print("Ranked Robin is the CONTROL: it must read 100.0% everywhere.\n")
    sweep(np.random.default_rng(a.seed), a.trials, a.approval_cutoff,
          a.models, a.candidates, a.voters)
    print("Cycles are EXCLUDED from the denominator (no CW to elect); "
          "'CW exists' is what is left.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
