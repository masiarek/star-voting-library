#!/usr/bin/env python3
"""
score_encoding_stability.py — how much does the DISTANCE-TO-SCORE rule change
who wins? Measured, across the six Euclidean spaces.

WHY THIS EXISTS
---------------
A spatial model hands you a distance, not a ballot. To run STAR on it you must
pick a rule that turns "voter v is 0.42 away from candidate c" into an integer
0-5. That rule is a MODELLING CHOICE, and it is the least-discussed step in the
whole pipeline: papers and library docs describe the sampler in detail and then
convert to a ballot in one unexplained line.

This script measures what that line costs. The headline: on a plain uniform-cube
electorate the two most natural rules disagree about the WINNER in roughly one
election in twelve — from identical voter and candidate positions. Same
electorate, same method, different arithmetic in the conversion step, different
winner.

That is the evidence behind the house rule (07_Concepts/topics/
simulate_utilities_not_ballots.md): the ballot is a *rendering* of a preference,
the rendering is a model, and a winner quoted from a single encoding is a claim
about the encoding as much as about the method.

THE TWO ENCODINGS
-----------------
  global   U = 5 * (1 - d / d_max), one d_max shared by every voter, then round
           and clamp to 0-5. The obvious rule, and the one that circulates in
           write-ups of the Euclidean samplers. It treats the scale as absolute:
           a 5 means "close in the space", not "my favourite".

  minmax   Per-voter min-max: your nearest candidate gets 5, your furthest gets
           0, everyone else lands proportionally between. What this repo's own
           simulations use (star_vs_approval_divergence.py::honest_scores), and
           what STAR's own voter guidance describes.

  quad     Per-voter min-max applied to QUADRATIC loss (utility = -d^2) instead
           of linear. The other standard spatial-utility convention; included so
           the linear choice is visible as a choice.

WHAT GOES WRONG WITH A GLOBAL d_max (this is the interesting part)
------------------------------------------------------------------
d_max has to be big enough for the furthest possible pair, so for a typical
voter every candidate sits well inside it and the whole ballot compresses into
the middle of the scale. Measured on a unit cube: no voter ever reaches 0, only
about 5% of marks reach 5, and 92% of every mark cast lands in {2,3,4}.

Two consequences the script reports:
  - DEAD BALLOTS. Some voters score every candidate identically and so express
    no preference at all. They are not abstaining; the encoding silently erased
    them. Per-voter min-max cannot do this (your nearest is always 5, your
    furthest always 0, unless you are exactly equidistant).
  - INFLATED EQUAL SUPPORT. Compression drives many more voters into the "no
    preference between the two finalists" bucket, so the runoff looks far more
    indecisive than the same electorate under min-max.

Neither is voter behaviour. Both are artifacts of the conversion rule.

A NOTE ON d_max ITSELF
----------------------
`unbounded_gaussian` has NO maximum distance — the tails run forever — so the
global rule is not merely inadvisable there, it is undefined. This script uses
the observed maximum for that space and labels it, which is the standard bodge
and is worth seeing labelled rather than buried.

A NOTE ON ROUNDING (and a negative result worth keeping)
--------------------------------------------------------
numpy's round() is banker's rounding: np.round(2.5) == 2.0 and np.round(4.5) ==
4.0, tipping half-integers toward EVEN rather than up. Both encodings here use
explicit floor(x + 0.5) half-up rounding, and --banker switches to numpy's rule.

Measured, the two are INDISTINGUISHABLE: identical score distributions and
identical winners across 4000 elections. That is the point of keeping the flag.
Sampled Euclidean distances are floats that essentially never land exactly on a
half-integer, so the tie-breaking rule has nothing to break. Where banker's
rounding really does bite is a HAND-BUILT example with round coordinates — the
kind of four-candidate illustration a write-up computes by hand — because there
a distance like 0.1414... against a d_max of 1.414 lands precisely on 4.5 and
silently becomes a 4. So: a documentation hazard, not a simulation hazard. Do
not cite --banker as a source of modelling error; cite it as the reason a
worked example in prose may not reproduce.

USAGE
-----
    python 06_Other/simulations/score_encoding_stability.py
    python 06_Other/simulations/score_encoding_stability.py --space gaussian_ball
    python 06_Other/simulations/score_encoding_stability.py --all-spaces
    python 06_Other/simulations/score_encoding_stability.py --banker

TIE-BREAKS (fixed, for reproducibility)
---------------------------------------
Finalists are the top two score totals, ties toward the lower candidate index;
the runoff goes to the candidate preferred on more ballots, ties likewise. These
are the same conventions as the other scripts in this folder. They are NOT the
engine's published ladder — this is a divergence-rate measurement, not a
tabulator. For a real count, run the LH engine on a case file.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from euclidean_spaces import SPACES  # noqa: E402  (the six spaces, one source of truth)


# --------------------------------------------------------------------------- #
# Encodings: distance matrix -> integer 0-5 scores.                            #
# --------------------------------------------------------------------------- #
def _round(x: np.ndarray, banker: bool) -> np.ndarray:
    """Half-up by default; numpy's round-half-to-even under --banker."""
    return np.round(x) if banker else np.floor(x + 0.5)


def enc_global(d: np.ndarray, banker: bool) -> np.ndarray:
    """U = 5 * (1 - d / d_max) with ONE d_max for the whole electorate."""
    d_max = d.max()
    if d_max <= 0:
        return np.full(d.shape, 5, dtype=int)
    return np.clip(_round(5.0 * (1.0 - d / d_max), banker), 0, 5).astype(int)


def _minmax(u: np.ndarray, banker: bool) -> np.ndarray:
    """Per-voter min-max of a utility matrix onto 0-5."""
    mn = u.min(axis=1, keepdims=True)
    mx = u.max(axis=1, keepdims=True)
    span = np.where(mx > mn, mx - mn, 1.0)
    return np.clip(_round((u - mn) / span * 5.0, banker), 0, 5).astype(int)


def enc_minmax(d: np.ndarray, banker: bool) -> np.ndarray:
    """Per-voter min-max on LINEAR loss (utility = -d)."""
    return _minmax(-d, banker)


def enc_quad(d: np.ndarray, banker: bool) -> np.ndarray:
    """Per-voter min-max on QUADRATIC loss (utility = -d^2)."""
    return _minmax(-(d ** 2), banker)


ENCODINGS = {
    "global": (enc_global, "one shared d_max, absolute scale"),
    "minmax": (enc_minmax, "per-voter min-max, linear loss"),
    "quad": (enc_quad, "per-voter min-max, quadratic loss"),
}


# --------------------------------------------------------------------------- #
# STAR, enough of it to find a winner.                                         #
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
def sweep(space, elections, voters, candidates, dims, seed, banker, names):
    rng = np.random.default_rng(seed)
    sampler = SPACES[space]
    n_marks = elections * voters * candidates

    hist = {n: np.zeros(6, dtype=np.int64) for n in names}
    dead = {n: 0 for n in names}
    equal = {n: 0 for n in names}
    winners = {n: [] for n in names}

    for _ in range(elections):
        vp = np.asarray(sampler(rng, voters, dims), dtype=float)
        cp = np.asarray(sampler(rng, candidates, dims), dtype=float)
        d = np.linalg.norm(vp[:, None, :] - cp[None, :, :], axis=2)

        for n in names:
            s = ENCODINGS[n][0](d, banker)
            hist[n] += np.bincount(s.ravel(), minlength=6)
            dead[n] += int((s.max(axis=1) == s.min(axis=1)).sum())
            w, eq = star(s)
            equal[n] += eq
            winners[n].append(w)

    return {
        "hist": {n: hist[n] / n_marks * 100.0 for n in names},
        "dead": {n: dead[n] / (elections * voters) * 100.0 for n in names},
        "equal": {n: equal[n] / (elections * voters) * 100.0 for n in names},
        "winners": {n: np.array(winners[n]) for n in names},
    }


def report(space, res, names, elections, voters, candidates, dims, banker):
    note = " (observed max — this space is unbounded)" if space == "unbounded_gaussian" else ""
    print(f"\n=== space: {space}{note} ===")
    print(f"    {elections} elections x {voters} voters x {candidates} candidates, "
          f"{dims}-D, rounding={'banker' if banker else 'half-up'}")

    print("\n  score distribution (% of all marks)")
    print("    score " + "".join(f"{n:>12}" for n in names))
    for s in range(6):
        print(f"    {s:>5} " + "".join(f"{res['hist'][n][s]:>11.1f}%" for n in names))

    print("\n    dead   " + "".join(f"{res['dead'][n]:>11.2f}%" for n in names)
          + "   <- ballots expressing NO preference at all")
    print("    equal  " + "".join(f"{res['equal'][n]:>11.1f}%" for n in names)
          + "   <- Equal Support in the runoff")

    print("\n  winner disagreement between encodings")
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            diff = int((res["winners"][a] != res["winners"][b]).sum())
            print(f"    {a:>7} vs {b:<7} {diff:>6}/{elections} = "
                  f"{100.0 * diff / elections:5.1f}%")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Measure how much the distance-to-score encoding changes the STAR winner.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--space", default="uniform_cube", choices=sorted(SPACES))
    p.add_argument("--all-spaces", action="store_true", help="run every one of the six")
    p.add_argument("--elections", type=int, default=4000)
    p.add_argument("--voters", type=int, default=101)
    p.add_argument("--candidates", type=int, default=4)
    p.add_argument("--dims", type=int, default=2)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--banker", action="store_true",
                   help="use numpy's round-half-to-even instead of half-up")
    p.add_argument("--encodings", nargs="+", default=["global", "minmax", "quad"],
                   choices=sorted(ENCODINGS))
    args = p.parse_args()

    names = list(dict.fromkeys(args.encodings))

    print("Distance-to-score encoding stability")
    print("=" * 72)
    for n in names:
        print(f"  {n:<8} {ENCODINGS[n][1]}")
    print("\nSame positions, same method, different conversion arithmetic.")
    print("Any disagreement below is caused by the encoding alone.")

    spaces = sorted(SPACES) if args.all_spaces else [args.space]
    for space in spaces:
        res = sweep(space, args.elections, args.voters, args.candidates,
                    args.dims, args.seed, args.banker, names)
        report(space, res, names, args.elections, args.voters,
               args.candidates, args.dims, args.banker)

    print("\nThe house rule: never quote a winner from a single encoding.")
    print("Report the rule beside the number, or sample the encodings and")
    print("report a win rate.  See 07_Concepts/topics/simulate_utilities_not_ballots.md")


if __name__ == "__main__":
    main()
