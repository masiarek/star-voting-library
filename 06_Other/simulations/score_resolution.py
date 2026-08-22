#!/usr/bin/env python3
"""
score_resolution.py — how many rungs does a score ballot actually need?

WHY THIS EXISTS
---------------
A spatial model hands every voter a REAL NUMBER for every candidate. A ballot
gives them six bubbles. Turning the first into the second does two lossy things,
and they are separable:

  1. NORMALIZE — whose scale? one shared d_max, or your own nearest-to-furthest?
     Measured already, in score_encoding_stability.py, which fixes the scale at
     0-5 and varies this choice.
  2. QUANTIZE — how many rungs? Measured here, which fixes the normalization at
     per-voter min-max (the rule this repo's simulations use, and the one STAR's
     own voter guidance describes) and varies the number of levels.

The question this script answers is the one a ballot designer actually faces:
0-5 is a convention, not a derivation. What does it cost against a voter who
could write down any real number, and what would more rungs buy?

THE LADDER
----------
Every encoding here is the SAME rule at a different resolution: per-voter
min-max onto 0..K, half-up rounding. Your nearest candidate gets K, your
furthest gets 0, everyone else lands proportionally between.

    K=1    0/1 - this is APPROVAL, and not by analogy: min-max onto one bit
           approves exactly the candidates in the upper half of your own
           utility range. The midpoint cutoff falls out of the arithmetic.
    K=2    three levels (against / neutral / for)
    K=3    four levels
    K=5    six levels - the STAR ballot
    K=9    ten levels - a 0-9 range ballot
    K=99   a hundred levels - "write a percentage"
    cont   NO rounding: real-valued scores in [0,1]. The voter with infinite
           resolution, and the baseline everything else is scored against.

WHAT IS MEASURED
----------------
  differs      how often this resolution elects someone other than the
               continuous baseline elects, from identical positions
  VSE          voter satisfaction efficiency of the winner against the true
               spatial utilities: (E[U(winner)] - E[U(random)]) /
               (E[U(best)] - E[U(random)]). Ratio of EXPECTATIONS, not the mean
               of per-election ratios - a near-zero denominator in one election
               must not swallow the metric (the choice Caragiannis & Fehrs make
               for average distortion, and for the same reason).
  silenced     of all the strict preferences a voter genuinely holds (pairs
               whose true utilities differ), the share the ballot cannot say
               because both candidates landed on the same rung
  equal        Equal Support in the runoff: ballots with no preference between
               the two finalists

THE FIELD SIZE IS THE VARIABLE THAT MATTERS
-------------------------------------------
Six rungs against four candidates is roomy; six rungs against twelve is not.
--sweep-candidates runs the ladder across field sizes, which is where the
interesting shape is: the cost of coarse scoring is driven by how many
candidates have to share the rungs, not by the rung count alone.

WHERE THE CUTS FALL IS A SECOND CHOICE, AND AT LOW RESOLUTION IT DOMINATES
--------------------------------------------------------------------------
Rounding to the nearest of K+1 rungs does NOT divide the range into equal
bands. The end bands are half-width and every interior band is full-width, so
at K=2 the middle rung is a catch-all covering HALF the voter's range: bands
run .25 / .50 / .25. On a large field most candidates land in it, and the
tally can then only see who reached the top quarter.

Measured on 16 candidates, uniform_cube, 2000 elections: three levels placed by
round-to-nearest scores VSE 0.9120 -- WORSE than a 0/1 approval ballot (0.9756),
which has no catch-all band at all. The SAME three levels with equal-width
bands score 0.9746. Same resolution, different cut points, most of the gap
gone. --equal-bands switches the quantizer so this is reproducible either way.

The lesson is not "three levels are bad". It is that the number of rungs and
the placement of the cuts are two independent modelling choices, and a
write-up that names only the first has not specified the encoder. This is
Approval's cutoff problem (07_Concepts/topics/ ... star_vs_approval_divergence)
reappearing inside a SCORE encoder, and it is why the winner-divergence column
for 0-2 is non-monotonic in the field size while every other column is not.

It fades fast with resolution. The STAR ballot's six rungs put only 1/5 of the
range in each interior band, so on that same 16-candidate field the cut-point
choice moves VSE by 0.0021 (0.9926 nearest, 0.9947 equal) against the 0.0626 it
moves at three levels. On a four-candidate field it is 0.0014. Real: not zero,
and equal-width wins every comparison here. Decisive: only when the rungs are
few enough that one band can swallow the middle of the ballot.

A THIRD THING THE TABLE SHOWS (worth not misreading)
-----------------------------------------------------
"silenced" and VSE do not move together, and neither tracks "differs". Equal
bands SILENCE MORE preferences than round-to-nearest at every resolution (13.0%
vs 9.0% at 0-5, four candidates) while scoring the same or better on welfare,
because their wider end bands merge candidates a voter ranks at the extremes,
where the merge changes no outcome. And more rungs keep changing WHO wins long
after they stop changing HOW GOOD the winner is: 0-5 misses the infinite-
precision winner in 3.8% of elections and 0-99 in 0.5%, so the extra rungs are
still moving results, while VSE across that whole range does not improve at
all. Those elections are re-sorting near-ties between near-equally-good
candidates. A
changed winner is not by itself evidence of a defect - it has to be paired with
a yardstick that says the new winner is worse.

TIE-BREAKS (fixed, for reproducibility)
---------------------------------------
Finalists are the top two score totals, ties toward the lower candidate index;
the runoff goes to the candidate preferred on more ballots, ties likewise. Same
conventions as the other scripts in this folder, and NOT the engine's published
ladder - this is a divergence-rate measurement, not a tabulator. For a real
count, run the LH engine on a case file.

USAGE
-----
    python 06_Other/simulations/score_resolution.py
    python 06_Other/simulations/score_resolution.py --candidates 10
    python 06_Other/simulations/score_resolution.py --sweep-candidates
    python 06_Other/simulations/score_resolution.py --space uniform_sphere
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from euclidean_spaces import SPACES  # noqa: E402  (the six spaces, one source of truth)


# --------------------------------------------------------------------------- #
# The ladder: one normalization, many resolutions.                             #
# --------------------------------------------------------------------------- #
LEVELS = [1, 2, 3, 5, 9, 99]
LABELS = {1: "0-1", 2: "0-2", 3: "0-3", 5: "0-5", 9: "0-9", 99: "0-99"}


def minmax_unit(d: np.ndarray) -> np.ndarray:
    """Per-voter min-max of LINEAR utility (-d) onto the real interval [0, 1]."""
    u = -d
    mn = u.min(axis=1, keepdims=True)
    mx = u.max(axis=1, keepdims=True)
    span = np.where(mx > mn, mx - mn, 1.0)
    return (u - mn) / span


def quantize(unit: np.ndarray, k: int, equal_bands: bool = False) -> np.ndarray:
    """Put the [0,1] ballot onto 0..k.

    Default is round-to-nearest, half-up (never numpy's banker's rule), which
    gives half-width END bands and full-width interior ones. With equal_bands,
    the range is cut into k+1 equal slices instead. Both keep the endpoints:
    your nearest candidate gets k, your furthest gets 0.
    """
    if equal_bands:
        return np.minimum(np.floor(unit * (k + 1)), k)
    return np.floor(unit * k + 0.5)


# --------------------------------------------------------------------------- #
# STAR, enough of it to find a winner. Works on real or integer scores.        #
# --------------------------------------------------------------------------- #
def star(scores: np.ndarray) -> tuple[int, int]:
    """Return (winner index, number of Equal Support ballots in the runoff)."""
    totals = scores.sum(axis=0)
    a, b = np.argsort(-totals, kind="stable")[:2]
    pref_a = int((scores[:, a] > scores[:, b]).sum())
    pref_b = int((scores[:, b] > scores[:, a]).sum())
    equal = scores.shape[0] - pref_a - pref_b
    return (int(a) if pref_a >= pref_b else int(b)), equal


# --------------------------------------------------------------------------- #
# The sweep.                                                                   #
# --------------------------------------------------------------------------- #
def sweep(space, elections, voters, candidates, dims, seed, equal_bands=False):
    rng = np.random.default_rng(seed)
    sampler = SPACES[space]
    names = [LABELS[k] for k in LEVELS] + ["cont"]

    differs = {n: 0 for n in names}
    equal = {n: 0 for n in names}
    silenced_hit = {n: 0 for n in names}   # preference pairs the ballot merged
    silenced_all = 0                       # preference pairs the voter holds
    u_win = {n: 0.0 for n in names}
    u_best = 0.0
    u_rand = 0.0

    for _ in range(elections):
        vp = np.asarray(sampler(rng, voters, dims), dtype=float)
        cp = np.asarray(sampler(rng, candidates, dims), dtype=float)
        d = np.linalg.norm(vp[:, None, :] - cp[None, :, :], axis=2)

        util = -d                       # true spatial utility, per voter
        social = util.sum(axis=0)       # utilitarian total, per candidate
        u_best += float(social.max())
        u_rand += float(social.mean())

        unit = minmax_unit(d)
        # every strictly-held preference, counted once per unordered pair
        strict = util[:, :, None] != util[:, None, :]
        pairs_held = int(strict.sum()) // 2
        silenced_all += pairs_held

        base_w, _ = star(unit)

        for k in LEVELS + [None]:
            n = "cont" if k is None else LABELS[k]
            s = unit if k is None else quantize(unit, k, equal_bands)
            w, eq = star(s)
            differs[n] += int(w != base_w)
            equal[n] += eq
            same = s[:, :, None] == s[:, None, :]
            silenced_hit[n] += int((strict & same).sum()) // 2
            u_win[n] += float(social[w])

    span = u_best - u_rand
    return {
        "names": names,
        "differs": {n: 100.0 * differs[n] / elections for n in names},
        "equal": {n: 100.0 * equal[n] / (elections * voters) for n in names},
        "silenced": {n: 100.0 * silenced_hit[n] / silenced_all for n in names},
        "vse": {n: (u_win[n] - u_rand) / span if span else float("nan") for n in names},
    }


def report(space, res, elections, voters, candidates, dims, bands="round-to-nearest"):
    print(f"\n=== space: {space} ===")
    print(f"    {elections} elections x {voters} voters x {candidates} candidates, {dims}-D, "
          f"per-voter min-max, {bands}")
    print("\n    ballot    differs      VSE   silenced    equal")
    for n in res["names"]:
        diff = "  baseline" if n == "cont" else f"{res['differs'][n]:8.1f}%"
        print(f"    {n:>6}  {diff}  {res['vse'][n]:7.4f}  {res['silenced'][n]:8.1f}%  "
              f"{res['equal'][n]:6.1f}%")


def sweep_candidates(space, elections, voters, dims, seed, fields, equal_bands=False):
    print(f"\n=== space: {space} — the ladder across field sizes ===")
    print(f"    {elections} elections x {voters} voters, {dims}-D, per-voter min-max, "
          f"{'equal-width bands' if equal_bands else 'round-to-nearest'}")
    names = [LABELS[k] for k in LEVELS] + ["cont"]

    for metric, title, fmt in (
        ("differs", "winner differs from the continuous baseline", "{:>7.1f}%"),
        ("vse", "VSE against the true spatial utilities", "{:>8.4f}"),
        ("silenced", "share of genuinely-held preferences the ballot silences", "{:>7.1f}%"),
    ):
        print(f"\n  {title}")
        print("    cands " + "".join(f"{n:>9}" for n in names))
        for m in fields:
            res = sweep(space, elections, voters, m, dims, seed, equal_bands)
            cells = "".join(
                ("        —" if (metric == "differs" and n == "cont")
                 else fmt.format(res[metric][n]))
                for n in names
            )
            print(f"    {m:>5} " + cells)


def main() -> None:
    p = argparse.ArgumentParser(
        description="How many rungs does a score ballot need? Quantization, measured.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--space", default="uniform_cube", choices=sorted(SPACES))
    p.add_argument("--all-spaces", action="store_true", help="run every one of the six")
    p.add_argument("--elections", type=int, default=4000)
    p.add_argument("--voters", type=int, default=101)
    p.add_argument("--candidates", type=int, default=4)
    p.add_argument("--dims", type=int, default=2)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--sweep-candidates", action="store_true",
                   help="run the ladder across field sizes (the interesting shape)")
    p.add_argument("--fields", type=int, nargs="+", default=[3, 4, 6, 10, 16],
                   help="field sizes for --sweep-candidates")
    p.add_argument("--equal-bands", action="store_true",
                   help="cut the range into equal-width bands instead of rounding to "
                        "the nearest rung (see the docstring: at low resolution this "
                        "is the choice that dominates)")
    a = p.parse_args()

    spaces = sorted(SPACES) if a.all_spaces else [a.space]
    for space in spaces:
        if a.sweep_candidates:
            sweep_candidates(space, a.elections, a.voters, a.dims, a.seed, a.fields,
                             a.equal_bands)
        else:
            res = sweep(space, a.elections, a.voters, a.candidates, a.dims, a.seed,
                        a.equal_bands)
            report(space, res, a.elections, a.voters, a.candidates, a.dims,
                   "equal-width bands" if a.equal_bands else "round-to-nearest")
    print()


if __name__ == "__main__":
    main()
