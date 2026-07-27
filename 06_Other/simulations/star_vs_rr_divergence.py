# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""star_vs_rr_divergence.py — when do STAR and Ranked Robin elect DIFFERENT winners?

Same underlying voter utilities feed both methods, so the comparison is apples-to-apples:
  * STAR  reads 0-5 SCORES: top-two by score sum, then a pairwise runoff.
  * RR     reads the RANKING: Copeland (most head-to-head wins); the Condorcet winner
           when one exists.

THE MECHANISM. If the Condorcet winner is one of STAR's two score-finalists, STAR elects
them too (a Condorcet winner wins any head-to-head, so they win the runoff). So
**STAR != RR requires either (a) a Condorcet CYCLE (no CW), or (b) the Condorcet winner
MISSING the score-based top-two** — a broadly-preferred but low-intensity compromise,
everyone's tepid second choice. That second case is the preference-vs-support split:
RR rewards order, STAR rewards how much support each candidate actually has.

WHAT THE SWEEP FINDS (see the README for the full table). Two regimes:
  * RANDOM NOISE (impartial culture): divergence is high but almost all CYCLE-driven —
    cycles explode with candidate count (3->~8%, 10->~48%). Both methods are just
    resolving an electorate that has no real winner. The dark-horse mechanism is rare.
  * SPATIAL / FACTIONAL: cycles are rare (a centrist Condorcet winner usually exists);
    the divergence that occurs is the MEANINGFUL kind — the compromise CW squeezed out
    of the score top-two. Factions AMPLIFY it (polarized voters score the centrist low).

TRENDS. More candidates -> more divergence, always. More voters -> divergence FALLS
sharply under spatial/factional models (less sampling noise, structure dominates) but
stays roughly flat under pure noise. So "fewer ballots -> more divergence" holds for
structured electorates, not for random ones.

*** ANSWER KEYS: NEVER LABEL A SAMPLE WITH star_winner_approx(). ***
This module has TWO models of STAR, and they are not interchangeable:
  * star_winner_approx()  -- fast numpy. For SCREENING (the sweep below) only.
  * star_winner_engine()  -- the real LH engine. For LABELS / answer keys.
The approximation resolves ties by numpy index order; the engine has further
tie-break rungs. A sample labelled from the approximation can therefore claim a
winner the engine does not elect -- which is exactly what happened to
05_Ranked_Robin/star_vs_rr_divergence/cycle_C10_fewV29_bloc_2.yaml (labelled
"STAR A"; the engine elects C -- fixed in commit 7ddde36). Any generator that
writes election_title / scenario_description / expected_winners MUST take those
strings from star_winner_engine() (or from the case's `_tabulated` mirror), and
the result is guarded by
STARVote_LH_tabulation_engine/tools_adam/scripts/check_star_vs_rr_labels.py.

Usage:  uv run 06_Other/simulations/star_vs_rr_divergence.py [--trials N] [--seed S]
        uv run 06_Other/simulations/star_vs_rr_divergence.py --audit-model 400
"""
import argparse
import sys
from pathlib import Path

import numpy as np

ENGINE_DIR = Path(__file__).resolve().parents[2] / "STARVote_LH_tabulation_engine"


def star_winner_approx(scores):
    """FAST, APPROXIMATE STAR winner -- for divergence SCREENING, never for labels.

    Top-two by score sum, then a pairwise runoff. Where it parts company with the
    real engine is the TIE-BREAKS, and it does so silently:
      * finalist selection -- a tie on score sum is settled here by numpy's stable
        argsort (i.e. by column order); the engine goes to pairwise wins, then
        five-star count, then lot.
      * the runoff -- `va >= vb` hands a tied runoff to the higher-scored finalist;
        the engine decides it ON THE BALLOTS by five-star count, then by lot.
    Good enough to count how OFTEN STAR and RR disagree (ties are rare and the
    error is unbiased across many trials); wrong to state WHO won a given election.
    Use star_winner_engine() for that, and see --audit-model for the actual
    disagreement rate between the two.
    """
    tot = scores.sum(0)
    a, b = np.argsort(-tot, kind="stable")[:2]              # two finalists by score sum
    va = int((scores[:, a] > scores[:, b]).sum())
    vb = int((scores[:, b] > scores[:, a]).sum())
    return int(a) if va >= vb else int(b)                   # runoff; tie -> higher-scored finalist


def star_winner_engine(scores, lot_numbers=None):
    """The REAL LH-engine STAR winner for a 0-5 score matrix -- USE THIS FOR LABELS.

    Runs the same call the CLI and the test suite run (see tools_adam/scenario_eval.py):
    every tie-break rung the engine has applies, so the answer is the one a reader
    will see in the `_tabulated` mirror. Returns the winner's column INDEX, matching
    star_winner_approx()'s return type.

    Orders of magnitude slower than the approximation -- call it once per sample you
    are about to label, never inside a sweep.
    """
    if str(ENGINE_DIR) not in sys.path:
        sys.path.insert(0, str(ENGINE_DIR))
    try:
        import starvote
        from starvote_larry_hastings import LotNumberTiebreaker
    except ImportError as e:                                # pragma: no cover - env guard
        raise ImportError(
            f"star_winner_engine() needs the LH engine at {ENGINE_DIR} ({e}). "
            "Run this script from a repo checkout with the project's venv "
            "(.venv/bin/python), not a bare `uv run`."
        ) from e

    names = [chr(ord("A") + i) for i in range(scores.shape[1])]
    rows = [{n: int(v) for n, v in zip(names, row)} for row in scores]
    winners = starvote.election(
        starvote.star, rows, seats=1, maximum_score=5,
        tiebreaker=LotNumberTiebreaker(lot_numbers=lot_numbers or [], silent=True),
        verbosity=1,                                        # match the wrapper exactly
        print=lambda *a, **k: None,
    )
    won = winners[0] if isinstance(winners, (list, tuple)) else winners
    return names.index(str(won))


def pairwise(util):
    C = util.shape[1]
    return np.stack([(util[:, [i]] > util).sum(0) for i in range(C)])  # W[i,j] = #(util_i > util_j)


def rr_winner_and_cw(util):
    W = pairwise(util); C = util.shape[1]
    beats = W > W.T
    ties = (W == W.T) & ~np.eye(C, dtype=bool)
    copeland = beats.sum(1) + 0.5 * ties.sum(1)
    rr = int(np.argmax(copeland))                           # most pairwise wins (ties -> lowest idx)
    cw = np.where(beats.sum(1) == C - 1)[0]
    return rr, (int(cw[0]) if len(cw) else -1)


def scores_from_util(util):
    lo = util.min(1, keepdims=True); hi = util.max(1, keepdims=True)
    span = np.where(hi > lo, hi - lo, 1.0)
    return np.rint(5 * (util - lo) / span).astype(int)      # normalized sincere 0-5 per voter


def gen(rng, model, V, C):
    if model == "noise":
        return rng.random((V, C))
    d = 1 if model.endswith("1d") else 2
    cand = rng.normal(0, 1, (C, d))
    if model.startswith("faction"):
        K = min(C, 3)
        centers = rng.normal(0, 1.2, (K, d))
        vpos = centers[rng.integers(0, K, V)] + rng.normal(0, 0.35, (V, d))
    else:
        vpos = rng.normal(0, 1, (V, d))
    dist = np.linalg.norm(vpos[:, None, :] - cand[None, :, :], axis=2)
    return -dist + rng.normal(0, 0.15, (V, C))              # utility = -distance + noise


def run(rng, model, V, C, trials):
    diff = cyc = cw_missed = 0
    for _ in range(trials):
        u = gen(rng, model, V, C)
        s = scores_from_util(u)
        sw = star_winner_approx(s)                          # screening only -- see the docstring
        rw, cw = rr_winner_and_cw(u)
        diff += sw != rw
        if cw == -1:
            cyc += 1
        elif cw != sw and cw not in set(np.argsort(-s.sum(0))[:2].tolist()):
            cw_missed += 1
    return diff / trials, cyc / trials, cw_missed / trials


def audit_model(rng, trials):
    """How often does the fast screening model MISLABEL a winner?

    Runs both models on the same elections and reports where they part. This is the
    measured size of the answer-key hazard: the sweep's percentages tolerate it, a
    per-file label does not.
    """
    print(f"Screening model vs LH engine — {trials} elections per cell\n")
    print(f"{'model':10} {'C':>3} {'V':>5} | {'approx != engine':>16}")
    total = bad_total = 0
    for model in ["noise", "spatial2d", "faction2d"]:
        for C in [3, 5, 10]:
            for V in [15, 51]:
                bad = 0
                for _ in range(trials):
                    s = scores_from_util(gen(rng, model, V, C))
                    bad += star_winner_approx(s) != star_winner_engine(s)
                total += trials
                bad_total += bad
                print(f"{model:10} {C:>3} {V:>5} | {bad*100/trials:15.1f}%")
        print()
    print(f"overall: {bad_total}/{total} = {bad_total*100/total:.2f}% mislabelled "
          f"if the screening model were used as an answer key")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=20260721)
    ap.add_argument("--audit-model", type=int, metavar="N", default=None,
                    help="instead of the sweep, run N elections per cell through BOTH "
                         "the screening model and the real engine and report how often "
                         "they disagree (the answer-key hazard, measured)")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    if a.audit_model:
        audit_model(rng, a.audit_model)
        return
    print(f"STAR vs Ranked Robin divergence — {a.trials} trials/cell, seed {a.seed}\n")
    print(f"{'model':10} {'C':>3} {'V':>5} | {'STAR!=RR':>9} {'cycle':>7} {'CW-missed-runoff':>17}")
    for model in ["noise", "spatial2d", "faction2d"]:
        for C in [3, 4, 5, 7, 10]:
            for V in [15, 51, 501]:
                d, cy, cm = run(rng, model, V, C, a.trials)
                print(f"{model:10} {C:>3} {V:>5} | {d*100:8.1f}% {cy*100:6.1f}% {cm*100:16.1f}%")
        print()


if __name__ == "__main__":
    main()
