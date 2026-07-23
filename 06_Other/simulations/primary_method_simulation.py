#!/usr/bin/env python3
"""
primary_method_simulation.py — does the QUALIFYING ROUND throw away the consensus winner?

WHY THIS EXISTS
---------------
Several reform packages are two-stage: an **open qualifying election** narrows a
crowded field to the top N (usually 4), then a good method runs the general.
Better Choices for Democracy's *Consensus Choice* is the current example — step 1
is "an open qualifying election ... [that] determines at least four of the
strongest candidates," and their published materials do NOT say which method that
round uses. (See 00_start_here/RCV_Ranked_Robin/ranked_robin_vs_consensus_choice.md.)

That gap provoked a real disagreement among people who know this field well:

  (a) It matters a lot. If the primary doesn't eliminate vote-splitting, the
      general's accuracy is capped by whatever the primary already distorted.
      Pair a top-4/5 open primary with a good method or don't bother.
  (b) It matters little. With FOUR candidates advancing, it's unlikely the
      consensus candidate fails to advance even under Plurality — four slots is
      a lot of slack.

Both are plausible; neither side has published numbers. This script measures it.

THE KEY STRUCTURAL FACT (why "dropped" is the whole story)
----------------------------------------------------------
If the general election is a Condorcet method (Ranked Robin / Consensus Choice),
then a full-field Condorcet winner who ADVANCES always wins: they beat every
candidate head-to-head, so they beat every survivor, so they are the Condorcet
winner of the surviving subset too. Therefore with a Condorcet general, **the
qualifying round is the ONLY place the consensus winner can be lost.** That makes
"how often does the primary drop the CW?" the entire accuracy question — which is
exactly why the unspecified primary method is not a footnote.

(With --general star that stops holding: a CW can advance and still lose the
runoff by missing the score-based top two. Run both to see the difference.)

WHAT WE MEASURE
---------------
Per (electorate model, primary method, N advancing):
  - CW exists %      : how often the full field has a Condorcet winner at all
  - CW dropped %     : of those, how often the primary fails to advance them
  - accuracy %       : end-to-end, final winner == full-field CW (of CW-exists)
  - VSE              : utility efficiency of the final winner
                       (U(winner) - U(avg candidate)) / (U(best) - U(avg candidate))

QUALIFYING METHODS
------------------
  plurality   : top N by first choices (argmax utility). The vote-splitting case.
  approval_ge3: top N by sincere approvals, approve everyone you'd score >= 3
  approval_ge4: same, tighter cutoff (closer to bullet voting)
  score       : top N by 0-5 score sum — i.e. STAR's scoring round
  rr          : top N by Copeland record (a Condorcet qualifying round)
  none        : no primary; the whole field goes to the general (the ceiling)

ELECTORATE MODELS (same family as star_vs_rr_divergence.py)
-----------------------------------------------------------
  noise     : each utility uniform[0,1], independent. Adversarial stress test;
              manufactures far more cycles and paradoxes than reality.
  spatial2d : voters & candidates are points in 2-D issue space; utility =
              -distance + noise. The realistic model (what VSE uses).
  faction2d : spatial, but voters cluster around 3 faction centers. The polarized
              case — and the one where a crowded co-partisan field splits.

HOUSE RULES OBSERVED
--------------------
Utilities are sampled and every ballot is DERIVED from them — never draw random
ballots (00_start_here/topics/simulate_utilities_not_ballots.md). Everything is
seeded. Tie-breaks are fixed and documented. Never quote a rate without the model.

USAGE
-----
  uv run 06_Other/simulations/primary_method_simulation.py --selftest
  uv run 06_Other/simulations/primary_method_simulation.py
  uv run 06_Other/simulations/primary_method_simulation.py --candidates 12 --advance 3 4 5
  uv run 06_Other/simulations/primary_method_simulation.py --general star
"""

import argparse
import sys

import numpy as np

METHODS = ["plurality", "approval_ge4", "approval_ge3", "score", "rr", "none"]
MODELS = ["noise", "spatial2d", "faction2d"]


# ---------------------------------------------------------------- ballots

def scores_from_util(util):
    """Sincere 0-5 STAR scores: per-voter min-max normalization of utilities."""
    lo = util.min(1, keepdims=True)
    hi = util.max(1, keepdims=True)
    span = np.where(hi > lo, hi - lo, 1.0)
    return np.rint(5 * (util - lo) / span).astype(int)


def pairwise(util):
    """W[i, j] = number of voters preferring candidate i to candidate j."""
    C = util.shape[1]
    return np.stack([(util[:, [i]] > util).sum(0) for i in range(C)])


def copeland_record(util):
    """Wins + 1/2 ties per candidate, and the Condorcet winner (-1 if a cycle)."""
    W = pairwise(util)
    C = util.shape[1]
    beats = W > W.T
    ties = (W == W.T) & ~np.eye(C, dtype=bool)
    record = beats.sum(1) + 0.5 * ties.sum(1)
    cw = np.where(beats.sum(1) == C - 1)[0]
    return record, (int(cw[0]) if len(cw) else -1)


# ---------------------------------------------------------------- qualifying round

def qualify(util, method, N):
    """Return the indices of the top-N candidates under `method`.

    Tie-break is fixed for reproducibility: stable argsort, so ties resolve
    toward the lower candidate index. Real rules use a lot draw; the bias is
    arbitrary but consistent across methods, so cross-method comparison is fair.
    """
    C = util.shape[1]
    if method == "none" or N >= C:
        return np.arange(C)

    if method == "plurality":
        firsts = np.argmax(util, axis=1)
        key = np.bincount(firsts, minlength=C).astype(float)
    elif method.startswith("approval_ge"):
        cutoff = int(method[-1])
        key = (scores_from_util(util) >= cutoff).sum(0).astype(float)
    elif method == "score":
        key = scores_from_util(util).sum(0).astype(float)
    elif method == "rr":
        key, _ = copeland_record(util)
        key = key.astype(float)
    else:
        raise ValueError(f"unknown qualifying method: {method}")

    return np.argsort(-key, kind="stable")[:N]


# ---------------------------------------------------------------- general election

def general_winner(util, survivors, general):
    """Winner among `survivors`, as a full-field candidate index."""
    sub = util[:, survivors]
    if general == "rr":
        record, _ = copeland_record(sub)
        local = int(np.argmax(record))                       # ties -> lowest index
    elif general == "star":
        s = scores_from_util(sub)
        tot = s.sum(0)
        a, b = (np.argsort(-tot, kind="stable")[:2] if sub.shape[1] > 1 else (0, 0))
        va = int((s[:, a] > s[:, b]).sum())
        vb = int((s[:, b] > s[:, a]).sum())
        local = int(a) if va >= vb else int(b)               # tie -> higher-scored
    else:
        raise ValueError(f"unknown general method: {general}")
    return int(survivors[local])


# ---------------------------------------------------------------- electorate

def gen(rng, model, V, C):
    if model == "noise":
        return rng.random((V, C))
    d = 2
    cand = rng.normal(0, 1, (C, d))
    if model.startswith("faction"):
        K = min(C, 3)
        centers = rng.normal(0, 1.2, (K, d))
        vpos = centers[rng.integers(0, K, V)] + rng.normal(0, 0.35, (V, d))
    else:
        vpos = rng.normal(0, 1, (V, d))
    dist = np.linalg.norm(vpos[:, None, :] - cand[None, :, :], axis=2)
    return -dist + rng.normal(0, 0.15, (V, C))


def vse(util, winner):
    """Utility efficiency: 1.0 = the utilitarian best, 0.0 = an average candidate."""
    mean_u = util.mean(0)
    best, avg = mean_u.max(), mean_u.mean()
    return 1.0 if best == avg else float((mean_u[winner] - avg) / (best - avg))


# ---------------------------------------------------------------- the run

def run(rng, model, method, N, V, C, trials, general):
    cw_exists = dropped = accurate = 0
    vse_total = 0.0
    for _ in range(trials):
        u = gen(rng, model, V, C)
        _, cw = copeland_record(u)
        survivors = qualify(u, method, N)
        w = general_winner(u, survivors, general)
        vse_total += vse(u, w)
        if cw >= 0:
            cw_exists += 1
            if cw not in set(survivors.tolist()):
                dropped += 1
            if w == cw:
                accurate += 1
    e = max(cw_exists, 1)
    return {
        "cw_exists": cw_exists / trials,
        "dropped": dropped / e,
        "accuracy": accurate / e,
        "vse": vse_total / trials,
    }


# ---------------------------------------------------------------- self-test

def selftest():
    """Known-answer checks. These are invariants, not sampled estimates."""
    ok = True
    rng = np.random.default_rng(7)

    # 1. A Condorcet qualifying round can NEVER drop the Condorcet winner:
    #    the CW has the strictly maximal Copeland record, so they are always #1.
    for model in MODELS:
        for _ in range(300):
            u = gen(rng, model, 51, 9)
            _, cw = copeland_record(u)
            if cw >= 0 and cw not in set(qualify(u, "rr", 4).tolist()):
                print("FAIL: rr primary dropped the Condorcet winner"); ok = False
                break

    # 2. If N >= C, no method drops anyone.
    for method in METHODS:
        u = gen(rng, "spatial2d", 51, 4)
        if len(qualify(u, method, 4)) != 4:
            print(f"FAIL: {method} with N>=C did not advance the whole field"); ok = False

    # 3. With a Condorcet general, an advanced CW always wins (the structural fact
    #    the script's headline claim rests on).
    for _ in range(300):
        u = gen(rng, "faction2d", 51, 9)
        _, cw = copeland_record(u)
        surv = qualify(u, "plurality", 4)
        if cw >= 0 and cw in set(surv.tolist()):
            if general_winner(u, surv, "rr") != cw:
                print("FAIL: advanced CW lost a Condorcet general"); ok = False
                break

    # 4. Hand-built center squeeze: 5 voters, 3 candidates, B is the CW but has
    #    only one first choice, so a Plurality top-2 primary drops B.
    #       2 x A>B>C , 2 x C>B>A , 1 x B>A>C
    u = np.array([
        [1.0, 0.6, 0.0],
        [1.0, 0.6, 0.0],
        [0.0, 0.6, 1.0],
        [0.0, 0.6, 1.0],
        [0.6, 1.0, 0.0],
    ])
    _, cw = copeland_record(u)
    if cw != 1:
        print(f"FAIL: expected B (index 1) as Condorcet winner, got {cw}"); ok = False
    if 1 in set(qualify(u, "plurality", 2).tolist()):
        print("FAIL: plurality top-2 should have dropped the squeezed centrist"); ok = False
    if 1 not in set(qualify(u, "plurality", 3).tolist()):
        print("FAIL: top-3 of a 3-candidate field must advance everyone"); ok = False

    print("selftest: PASS" if ok else "selftest: FAIL")
    return 0 if ok else 1


# ---------------------------------------------------------------- cli

def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trials", type=int, default=2000)
    ap.add_argument("--voters", type=int, default=501)
    ap.add_argument("--candidates", type=int, default=9,
                    help="size of the crowded open field the primary must narrow")
    ap.add_argument("--advance", type=int, nargs="+", default=[2, 3, 4, 5],
                    help="how many candidates the qualifying round sends forward")
    ap.add_argument("--methods", nargs="+", default=METHODS, choices=METHODS)
    ap.add_argument("--models", nargs="+", default=MODELS, choices=MODELS)
    ap.add_argument("--general", default="rr", choices=["rr", "star"],
                    help="method for the general election (default: Ranked Robin / Consensus Choice)")
    ap.add_argument("--seed", type=int, default=20260723)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    rng = np.random.default_rng(a.seed)
    print(f"Qualifying-round accuracy — {a.trials} trials/cell, seed {a.seed}")
    print(f"field of {a.candidates} candidates, {a.voters} voters, "
          f"general = {a.general.upper()}\n")

    for model in a.models:
        print(f"--- {model} ---")
        print(f"{'primary':13} {'N':>2} | {'CW exists':>9} {'CW dropped':>11} "
              f"{'accuracy':>9} {'VSE':>6}")
        for method in a.methods:
            for N in a.advance:
                if method == "none" and N != a.advance[0]:
                    continue                                  # baseline is N-independent
                r = run(rng, model, method, N, a.voters, a.candidates, a.trials, a.general)
                label = "—" if method == "none" else str(N)
                print(f"{method:13} {label:>2} | {r['cw_exists']*100:8.1f}% "
                      f"{r['dropped']*100:10.1f}% {r['accuracy']*100:8.1f}% "
                      f"{r['vse']:6.3f}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
