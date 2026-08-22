#!/usr/bin/env python3
"""
resolvability_sweep.py — does Copeland really tie more than its Condorcet siblings?
===================================================================================
On [[Talk:Copeland's method]] in February 2021, RobLa wrote: *"I'm pretty sure that
a Monte carlo Simulation would show that Copeland's method has way more ties than
the Schulze method or with Ranked Pairs or almost any of the other Condorcet
methods (monotonic or not). It would depend on the model being used and many
other factors, though."* Nobody ran it. This does.

**What is measured.** For each sampled election, every method is asked for its
**irresolute winner set** — the answer the rule gives *before* any tie-break is
applied. A method "ties" on that election when the set has more than one member.
That is the [resolvability](https://en.wikipedia.org/wiki/Resolvability_criterion)
question Markus Schulze pointed at in the same discussion, and it is the only
comparison that is fair across methods: bolt a good enough tie-break onto
anything and it always names one winner, so comparing post-tie-break output would
measure the tie-breaks, not the methods.

**Two confounds this sweep separates, because both change the answer.**

1. **The model.** House rule in this library: never quote a paradox rate without
   naming the electorate model. Impartial culture (every ranking equally likely,
   voters independent) manufactures cycles at rates no real electorate shows and
   is a stress test, not a prediction; a spatial model is the realistic one. Both
   are run, and both are reported.
2. **Voter parity.** With complete strict rankings and an **odd** electorate, no
   pairwise matchup can be drawn, so every tie a method reports comes from the
   *shape* of the tournament. Make the electorate **even** and drawn matchups
   appear, which is a second and quite different source of ties. Pooling the two
   would hide the mechanism, so they are reported separately.

The conditional rate — ties **given that no Condorcet winner exists** — is
reported too, because it isolates the disagreement. Whenever a Condorcet winner
exists every method here returns it, uniquely, so the unconditional rate is
mostly a measure of how often cycles happen rather than of the methods.

Counts are `pref_voting` (Holliday & Pacuit), the same third-party library this
repo already uses to cross-check Ranked Robin; profiles come from its
`prefsampling` generators. Nothing here is this repo's own arithmetic, which is
the point — the claim under test is about Copeland, not about our engine.

Usage:
    python resolvability_sweep.py                    # the full sweep (~20 min)
    python resolvability_sweep.py --n 2000 --quick   # a fast smoke run
    python resolvability_sweep.py --csv out.csv      # also write tidy rows
"""

import argparse
import csv
import math
import sys
import time

import numpy as np
from prefsampling.ordinal import euclidean

from pref_voting.generate_profiles import generate_profile
from pref_voting.profiles import Profile
from pref_voting.c1_methods import copeland
from pref_voting.margin_based_methods import (
    beat_path, ranked_pairs_with_test, minimax, split_cycle,
)

# Ranked Pairs is irresolute-by-enumeration and blows up past five candidates
# (~150 ms/profile at six, against ~2 ms at five), so six-candidate cells run a
# smaller sample. That reduction is printed, never silent.
RP_SLOW_FROM = 6

# `ranked_pairs` is irresolute by enumeration: it must consider every linear
# order consistent with the margins, so tied margins make it factorial. That is
# not a rare corner — a SMALL electorate produces tied margins constantly (at 9
# voters and 5 candidates a single profile can run for minutes). pref_voting
# ships `ranked_pairs_with_test`, which returns None rather than start a
# computation it predicts will not finish; this sweep counts those separately
# and REFUSES to quote a rate for any cell that has them, because the profiles
# it gives up on are exactly the margin-tied ones — the profiles most likely to
# tie. Dropping them would bias the estimate downward, which is the one
# direction that would flatter the conclusion.
METHODS = [
    ("Copeland", copeland),          # = Ranked Robin's tally
    ("Beat Path", beat_path),        # = Schulze
    ("Ranked Pairs", ranked_pairs_with_test),
    ("Minimax", minimax),
    ("Split Cycle", split_cycle),
]

def ic_sampler(num_cands, num_voters, seed):
    return generate_profile(num_cands, num_voters, seed=seed, probmodel="IC")


def spatial_sampler(dim):
    """Voters and candidates as Gaussian points; each voter ranks by distance.

    NOT `generate_profile(probmodel="euclidean", seed=...)`, and the reason is a
    live upstream bug rather than a preference. That path routes to prefsampling
    0.1.24, whose GAUSSIAN_BALL sampler, WHEN GIVEN A SEED, returns ONE point
    repeated once per voter: 2,000 seeds produced 2,000 copies of one degenerate
    profile in which every voter sits on the same spot -- and the candidates
    collapse onto that same point, so every distance is zero and every voter
    submits the identical index-order ranking. Every
    cell reported 0.00% cycles and looked like a tidy finding about spatial
    electorates. Unseeded calls vary fine, so seeding FOR REPRODUCIBILITY is what
    breaks it. Filed as https://github.com/COMSOC-Community/prefsampling/issues/6,
    together with a second defect found alongside it: voters and candidates are
    drawn from the same seeded stream, so candidates land exactly on the first
    voters on four of the six spaces. Positions are therefore drawn here, from a
    numpy Generator this script owns — which is also what makes the run
    reproducible.
    """
    def sample(num_cands, num_voters, seed):
        rng = np.random.default_rng(seed)
        voters = rng.normal(size=(num_voters, dim))
        cands = rng.normal(size=(num_cands, dim))
        return Profile(euclidean(num_voters, num_cands, dim, voters, cands))
    return sample


MODELS = {
    "impartial culture": ic_sampler,
    "spatial (2-D)": spatial_sampler(2),
}

SHORT = {"impartial culture": "IC", "spatial (2-D)": "spatial"}


def wilson(k, n, z=1.96):
    """Wilson score interval — behaves at proportions near 0, which these are."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, centre - half), min(1.0, centre + half))


def run_cell(num_cands, num_voters, sampler, n, seed0):
    """Sample n elections; count irresolute answers per method.

    Returns per-method (tied, computed, tied_nocw, computed_nocw) so a method
    that declined some profiles gets its own honest denominator.
    """
    tied = {name: 0 for name, _ in METHODS}
    computed = {name: 0 for name, _ in METHODS}
    tied_nocw = {name: 0 for name, _ in METHODS}
    computed_nocw = {name: 0 for name, _ in METHODS}
    no_cw = 0
    for i in range(n):
        prof = sampler(num_cands, num_voters, seed0 + i)
        cw = prof.condorcet_winner()
        if cw is None:
            no_cw += 1
        for name, fn in METHODS:
            winners = fn(prof)
            if winners is None:        # the method declined this profile
                continue
            computed[name] += 1
            if cw is None:
                computed_nocw[name] += 1
            if len(winners) > 1:
                tied[name] += 1
                if cw is None:
                    tied_nocw[name] += 1
    return tied, computed, tied_nocw, computed_nocw, no_cw


def fmt(k, n):
    if n == 0:
        return "     —    "
    lo, hi = wilson(k, n)
    return f"{100*k/n:6.2f}% ±{100*(hi-lo)/2:4.2f}"


SKIP_TOLERANCE = 0.01  # quote through a <=1% intractable share, flagged with a dagger


def fmt_guarded(k, computed, attempted):
    """Rate, or a refusal when the method declined too much of the sample."""
    if attempted == 0:
        return "     —    "
    missed = (attempted - computed) / attempted
    if missed == 0:
        return fmt(k, computed)
    if missed <= SKIP_TOLERANCE:
        return fmt(k, computed).rstrip() + "\u2020"
    return f"  [skip {100*missed:4.1f}%]"


def emit(title, rows, n_label):
    print(f"\n{title}")
    head = f"{'cell':<34} {'no CW':>9}  " + "  ".join(f"{m:>14}" for m, _ in METHODS)
    print(head)
    print("-" * len(head))
    any_skip = False
    for label, tied, computed, tied_nocw, computed_nocw, no_cw, n in rows:
        cells = []
        for m, _ in METHODS:
            if computed[m] < n:
                any_skip = True
            cells.append(f"{fmt_guarded(tied[m], computed[m], n):>14}")
        print(f"{label:<34} {fmt(no_cw, n):>9}  " + "  ".join(cells))
    print(f"\n  ties GIVEN no Condorcet winner ({n_label}):")
    for label, tied, computed, tied_nocw, computed_nocw, no_cw, n in rows:
        cells = [f"{fmt_guarded(tied_nocw[m], computed_nocw[m], no_cw):>14}" for m, _ in METHODS]
        print(f"    {label:<32} {'':>9}  " + "  ".join(cells))
    if any_skip:
        print("\n  [skip N%] = Ranked Pairs declined that share of the sample as intractable;")
        print("  \u2020 = it declined <=1%, small enough that the rate is still quoted.")
        print("  No rate is quoted there on purpose: the profiles it gives up on are the")
        print("  margin-TIED ones, i.e. those likeliest to tie, so a rate over the rest")
        print("  would be biased low — the one direction that would flatter the finding.")
    sys.stdout.flush()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--n", type=int, default=20000, help="profiles per cell (default 20000)")
    ap.add_argument("--n-slow", type=int, default=2000, help="profiles per cell at 6+ candidates")
    ap.add_argument("--quick", action="store_true", help="skip the 6-candidate and parity tables")
    ap.add_argument("--csv", help="also write tidy rows to this path")
    ap.add_argument("--why", action="store_true",
                    help="only run the exhaustive mechanism check (fast, no sampling)")
    args = ap.parse_args()

    if args.why:
        why_table()
        return

    started = time.time()
    tidy = []
    print("Does Copeland tie more often than Schulze / Ranked Pairs?")
    print("Rate at which each method returns MORE THAN ONE winner, before any tie-break.")
    print(f"pref_voting {__import__('pref_voting').__version__ if hasattr(__import__('pref_voting'), '__version__') else ''}"
          f"  ·  95% Wilson intervals  ·  seeded, reproducible")

    def cell(label, cands, voters, model_name, n, seed0):
        t = time.time()
        tied, computed, tied_nocw, computed_nocw, no_cw = run_cell(
            cands, voters, MODELS[model_name], n, seed0)
        for m, _ in METHODS:
            tidy.append(dict(model=model_name, candidates=cands, voters=voters,
                             method=m, n_attempted=n, n_computed=computed[m],
                             tied=tied[m], no_cw=no_cw,
                             n_computed_no_cw=computed_nocw[m],
                             tied_given_no_cw=tied_nocw[m]))
        print(f"    [{SHORT[model_name]:>7} | {label:<34}] {n:>6} profiles, {time.time()-t:5.1f}s", file=sys.stderr)
        return (label, tied, computed, tied_nocw, computed_nocw, no_cw, n)

    # ---- Table A: field size, at a large ODD electorate (no drawn matchups) ----
    for model in MODELS:
        rows = []
        for cands in (3, 4, 5) if args.quick else (3, 4, 5, 6):
            n = args.n_slow if cands >= RP_SLOW_FROM else args.n
            rows.append(cell(f"{cands} candidates, 101 voters", cands, 101, model, n, 1_000_000 + cands * 7919))
        emit(f"A. By field size — 101 voters (ODD: no matchup can be drawn) — {model}",
             rows, "denominator = the no-CW elections in that row")
        if not args.quick:
            print(f"  Note: the 6-candidate row uses {args.n_slow:,} profiles, not {args.n:,} — "
                  f"Ranked Pairs costs ~150 ms/profile there. Its interval is correspondingly wider.")

    if args.quick:
        return finish(started, tidy, args)

    # ---- Table B: electorate size and PARITY, at 5 candidates ----
    for model in MODELS:
        rows = []
        for voters in (9, 10, 25, 26, 101, 100):
            parity = "odd" if voters % 2 else "EVEN — draws possible"
            rows.append(cell(f"5 cands, {voters:>3} voters ({parity})", 5, voters, model, args.n,
                             2_000_000 + voters * 7919))
        emit(f"B. By electorate size and parity — 5 candidates — {model}",
             rows, "denominator = the no-CW elections in that row")

    why_table()
    finish(started, tidy, args)


def finish(started, tidy, args):
    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(tidy[0].keys()))
            w.writeheader()
            w.writerows(tidy)
        print(f"\nwrote {len(tidy)} rows to {args.csv}")
    print(f"\ntotal {time.time()-started:.0f}s")


if __name__ == "__main__":
    main()
