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

Usage:  uv run 06_Other/simulations/star_vs_rr_divergence.py [--trials N] [--seed S]
"""
import argparse
import numpy as np


MAX_SCORE = 5

# --- STAR, with the LH engine's tie-break rungs -------------------------------
# These MUST agree with starvote's star() (STARVote_LH_tabulation_engine/starvote/
# __init__.py, ~L1837). An earlier version of this file resolved every tie by
# numpy index order, which disagrees with the engine whenever a tie is actually
# reached — that mislabelled one of the 30 dumped samples (cycle_C10_fewV29_bloc_2:
# this file said A, the engine elects C). tests/test_sim_star_model.py cross-checks
# the two on random profiles, so the drift cannot come back silently.
#   Scoring round : top two by score sum. Tie -> (1) most head-to-head wins among
#                   the tied, (2) most 5-star votes, (3) lot.
#   Runoff        : pairwise preference. Tie -> (1) higher score sum, (2) most
#                   5-star votes, (3) lot.
# "Lot" here is the lowest column index, which is what the engine falls back to
# when a file publishes no lot_numbers (its LotNumberTiebreaker defaults to CSV
# column order). A lot-decided cell is arbitrary in BOTH, just consistently so.


def _totals(scores, idx):
    return {i: int(scores[:, i].sum()) for i in idx}


def _pairwise_wins(scores, idx):
    """Ballots preferring i, summed over the other candidates in idx."""
    return {i: sum(int((scores[:, i] > scores[:, j]).sum()) for j in idx if j != i)
            for i in idx}


def _five_star(scores, idx):
    return {i: int((scores[:, i] == MAX_SCORE).sum()) for i in idx}


def _leaders(tally):
    best = max(tally.values())
    return sorted(i for i, v in tally.items() if v == best)


def _fill(tally, needed):
    """Seat `needed` candidates from ONE rung's tally, the way the engine's
    _compute_first_and_second_from_score does: take the leaders, and if they
    under-fill the slots, seat them and keep reading DOWN THE SAME TALLY. Only a
    group that over-fills the remaining slots is still tied, and only that group
    goes on to the next rung.

    Returns (seated, still_tied)."""
    seated, pool = [], dict(tally)
    while pool and len(seated) < needed:
        top = _leaders(pool)
        if len(top) > needed - len(seated):
            return seated, top
        seated += top
        for i in top:
            del pool[i]
    return seated, []


def _resolve(scores, tied, needed):
    """Cut `tied` down to `needed`, walking the engine's rungs then falling to lot."""
    seated = []
    for rung in (_pairwise_wins, _five_star):
        got, tied = _fill(rung(scores, tied), needed - len(seated))
        seated += got
        if not tied:
            return seated
    return (seated + sorted(tied))[:needed]                 # lot: lowest column index


def _runoff(scores, a, b):
    tallies = [{i: int((scores[:, i] > scores[:,
                        b if i == a else a]).sum()) for i in (a, b)},
               _totals(scores, (a, b)), _five_star(scores, (a, b))]
    for tally in tallies:
        if tally[a] != tally[b]:
            return a if tally[a] > tally[b] else b
    return min(a, b)                                        # lot: lowest column index


def star_winner(scores):
    C = scores.shape[1]
    if C < 2:
        return 0
    finalists, tied = _fill(_totals(scores, range(C)), 2)    # top two by score sum
    if tied:
        finalists += _resolve(scores, tied, 2 - len(finalists))
    return _runoff(scores, finalists[0], finalists[1])


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
        sw = star_winner(s)
        rw, cw = rr_winner_and_cw(u)
        diff += sw != rw
        if cw == -1:
            cyc += 1
        elif cw != sw and cw not in set(np.argsort(-s.sum(0))[:2].tolist()):
            cw_missed += 1
    return diff / trials, cyc / trials, cw_missed / trials


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=20260721)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
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
