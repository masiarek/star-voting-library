#!/usr/bin/env python3
"""
star_vs_approval_divergence.py — measure how often single-winner STAR and Approval
elect DIFFERENT winners, by brute force over many random elections.

WHY THIS EXISTS
---------------
"How often do STAR and Approval disagree?" has no single answer — and the reason
is the whole lesson. STAR has a canonical sincere ballot (min-max your utilities
onto 0-5). APPROVAL DOES NOT: the voter must pick a 0/1 cutoff, and *where they
draw it* changes the winner. So the divergence rate depends on BOTH the electorate
model AND the approval-cutoff rule. This script reports it across both, so the
number always comes with its assumptions (the house rule: never quote a rate
without the model — see 06_Other/simulations/README.md and Curriculum 301.6/301.9).

WHAT WE MEASURE
---------------
For each random election we derive every voter's utilities, then:
  - STAR winner: from the sincere 0-5 scores (per-voter min-max scaling of utilities).
  - Approval winner: from sincere approvals under a chosen CUTOFF rule.
Divergence = the two winners differ. We report the % of elections that diverge,
per (electorate model, approval cutoff).

APPROVAL CUTOFF RULES (sincere; no polling/strategy)
----------------------------------------------------
The key knob: Approval has NO canonical sincere ballot, so *where a voter draws
the 0/1 line* is a modelling choice — and it moves the winner. Two families:
- Score cutoffs (default): geN = approve every candidate you'd SCORE >= N on the
  0-5 STAR ballot. ge5 = only your top (near-Plurality) .. ge1 = anyone but your
  worst (near-universal). This is the intuitive "read the STAR ballot as approvals
  at threshold N" family — sweep it to see the cutoff's impact directly.
- Utility cutoffs: mean (above your average utility), midpoint (above your midrange).
Run `--cutoffs ge5 ge4 ge3 ge2 ge1` (the default) to see divergence rise as the
cutoff tightens toward bullet voting.

ELECTORATE MODELS (same as fbc_simulation.py)
---------------------------------------------
- spatial   : voters & candidates are points in --dims-D issue space; utility =
              -distance. The realistic model (what VSE uses).
- impartial : each utility ~ uniform[0,1], independent. An adversarial stress test
              that manufactures far more disagreement; treat as a rough upper bound.

TIE-BREAKS (fixed, for reproducibility)
---------------------------------------
- STAR finalists: top two totals, ties toward the lower candidate index; runoff
  tie -> the higher-total finalist. (Identical to fbc_simulation.py.)
- Approval: most approvals; tie -> lower candidate index.
A tie-broken STAR winner that equals a tie-broken Approval winner counts as
agreement; the tie rule is fixed and seeded, so results reproduce exactly.

USAGE
-----
    python3 star_vs_approval_divergence.py                 # default sweep
    python3 star_vs_approval_divergence.py --candidates 4 --voters 51
    python3 star_vs_approval_divergence.py --selftest      # known-answer checks only
"""

import argparse

import numpy as np


# --------------------------------------------------------------------------- #
# Tabulators.                                                                  #
# --------------------------------------------------------------------------- #
def star_winner(scores):
    """scores: (V, C) int 0..5. Finalists = two highest totals (tie -> lower
    index); runoff -> more-preferred finalist (tie -> higher-total finalist)."""
    totals = scores.sum(axis=0)
    order = sorted(range(len(totals)), key=lambda c: (-int(totals[c]), c))
    a, b = order[0], order[1]
    pa = int((scores[:, a] > scores[:, b]).sum())
    pb = int((scores[:, b] > scores[:, a]).sum())
    if pa > pb:
        return a
    if pb > pa:
        return b
    return a  # runoff tie -> higher-total finalist


def approval_winner(approvals):
    """approvals: (V, C) 0/1. Most approvals wins; tie -> lower candidate index."""
    totals = approvals.sum(axis=0)
    return int(max(range(len(totals)), key=lambda c: (int(totals[c]), -c)))


# --------------------------------------------------------------------------- #
# Sincere ballots from utilities.                                             #
# --------------------------------------------------------------------------- #
def honest_scores(U):
    """U: (V, C) utilities -> (V, C) int STAR scores 0..5 (per-voter min-max)."""
    mn = U.min(axis=1, keepdims=True)
    mx = U.max(axis=1, keepdims=True)
    rng = np.where(mx > mn, mx - mn, 1.0)
    return np.clip(np.rint((U - mn) / rng * 5).astype(int), 0, 5)


def honest_approvals(U, cutoff):
    """U: (V, C) utilities -> (V, C) 0/1 approvals under a sincere cutoff rule.

    Utility cutoffs:
      mean      approve every candidate rated above your average utility.
      midpoint  approve every candidate above the midpoint of your utility range.
    Score cutoffs (the intuitive "read the STAR ballot as approvals" family) —
    approve every candidate you'd SCORE >= N on the 0-5 STAR ballot:
      ge5  only your top-scored candidate(s)   (most restrictive, ~bullet vote)
      ge4  scored 4 or 5
      ge3  scored 3-5   (top half of the scale; ~= midpoint)
      ge2  scored 2-5
      ge1  scored 1-5   (anyone but your worst; most generous)
    Because STAR's min-max scaling puts each voter's favorite at 5 and worst at 0,
    ge5 approves >=1 candidate and ge1 approves all-but-worst — a full spectrum
    from near-Plurality to near-universal-approval.
    """
    if cutoff == "mean":
        return (U > U.mean(axis=1, keepdims=True)).astype(int)
    if cutoff == "midpoint":
        mid = (U.min(axis=1, keepdims=True) + U.max(axis=1, keepdims=True)) / 2.0
        return (U > mid).astype(int)
    if cutoff.startswith("ge") and cutoff[2:].isdigit():
        return (honest_scores(U) >= int(cutoff[2:])).astype(int)
    raise ValueError(f"unknown cutoff: {cutoff}")


# --------------------------------------------------------------------------- #
# Electorate models (identical to fbc_simulation.py).                          #
# --------------------------------------------------------------------------- #
def sample_utilities(rng, V, C, model, dims):
    if model == "spatial":
        vp = rng.normal(size=(V, dims))
        cp = rng.normal(size=(C, dims))
        d = np.linalg.norm(vp[:, None, :] - cp[None, :, :], axis=2)
        return -d
    if model == "impartial":
        return rng.random((V, C))
    raise ValueError(f"unknown model: {model}")


# --------------------------------------------------------------------------- #
# Driver.                                                                      #
# --------------------------------------------------------------------------- #
def run_model(rng, model, elections, V, C, dims, cutoffs):
    diverge = {c: 0 for c in cutoffs}
    for _ in range(elections):
        U = sample_utilities(rng, V, C, model, dims)
        sw = star_winner(honest_scores(U))
        for c in cutoffs:
            aw = approval_winner(honest_approvals(U, c))
            if aw != sw:
                diverge[c] += 1
    return diverge


def report(model, diverge, elections):
    print(f"\n=== model: {model}   ({elections} elections) ===")
    print(f"{'approval cutoff':<14}{'STAR vs Approval diverge'}")
    for c, n in diverge.items():
        print(f"{c:<14}{n}/{elections} = {100.0 * n / elections:5.1f}%")


# --------------------------------------------------------------------------- #
# Known-answer self-tests.                                                     #
# --------------------------------------------------------------------------- #
def selftest():
    ok = True

    # Approval tabulator: candidate 1 has the most approvals.
    ap = np.array([[1, 1, 0],
                   [0, 1, 1],
                   [1, 1, 0],
                   [0, 1, 0]])
    w = approval_winner(ap)
    ok &= (w == 1)
    print(f"[selftest] approval_winner -> {w} (expect 1) {'OK' if w == 1 else 'FAIL'}")

    # A constructed divergence: an intense majority favorite (STAR) vs a broadly
    # approved consensus (Approval). 3 candidates 0,1,2.
    #   6 voters: 0=5, 1=3, 2=0   -> approve {0,1} at midpoint; STAR-score 0 high
    #   5 voters: 2=5, 1=4, 0=0   -> approve {2,1}
    # STAR: totals 0=30, 1=38, 2=25 -> finalists 1,0; runoff 0>1 on 6 ballots vs
    #   1>0 on 5 -> STAR winner 0. Approval(midpoint): 1 approved by all 11, wins.
    U = np.array([[5, 3, 0]] * 6 + [[0, 4, 5]] * 5, dtype=float)
    sw = star_winner(honest_scores(U))
    aw = approval_winner(honest_approvals(U, "midpoint"))
    ok &= (sw != aw)
    print(f"[selftest] constructed divergence -> STAR {sw}, Approval {aw} "
          f"(expect different) {'OK' if sw != aw else 'FAIL'}")

    print(f"[selftest] {'ALL PASS' if ok else 'FAILURES PRESENT'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--elections", type=int, default=20000)
    ap.add_argument("--voters", type=int, default=51)
    ap.add_argument("--candidates", type=int, default=3)
    ap.add_argument("--dims", type=int, default=2, help="issue-space dimensions (spatial)")
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--models", nargs="+", default=["spatial", "impartial"],
                    choices=["spatial", "impartial"])
    ap.add_argument("--cutoffs", nargs="+",
                    default=["ge5", "ge4", "ge3", "ge2", "ge1"],
                    choices=["mean", "midpoint", "ge1", "ge2", "ge3", "ge4", "ge5"],
                    help="approval cutoff rule(s): geN = approve scores >= N (ge5 "
                         "restrictive .. ge1 generous); mean/midpoint = utility cutoffs")
    ap.add_argument("--selftest", action="store_true", help="run known-answer checks only")
    args = ap.parse_args()

    if args.selftest:
        raise SystemExit(0 if selftest() else 1)

    print("STAR vs Approval divergence simulation")
    print(f"  candidates={args.candidates}  voters={args.voters}  "
          f"elections/model={args.elections}  dims={args.dims}  seed={args.seed}")
    if not selftest():
        raise SystemExit("self-tests failed; aborting.")

    for model in args.models:
        rng = np.random.default_rng(args.seed)  # same seed per model -> comparable
        diverge = run_model(rng, model, args.elections, args.voters,
                            args.candidates, args.dims, args.cutoffs)
        report(model, diverge, args.elections)

    print("\nReminder: divergence depends on BOTH the electorate model AND the "
          "approval cutoff. Quote the number only with both — Approval has no "
          "single sincere ballot, so 'the' rate does not exist.")


if __name__ == "__main__":
    main()
