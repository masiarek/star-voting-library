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


def star_winner(scores):
    tot = scores.sum(0)
    a, b = np.argsort(-tot, kind="stable")[:2]              # two finalists by score sum
    va = int((scores[:, a] > scores[:, b]).sum())
    vb = int((scores[:, b] > scores[:, a]).sum())
    return int(a) if va >= vb else int(b)                   # runoff; tie -> higher-scored finalist


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
