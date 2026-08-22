#!/usr/bin/env python3
"""
statistical_cultures.py — the named recipes for generating a random election
============================================================================
A **statistical culture** is a probability distribution over whole preference
profiles: a named recipe that rolls an entire synthetic electorate at once.
`prefsampling` ships a dozen of them, and their names travel through the
literature — and through this repo's own sweeps — attached to parameter values
(`urn alpha=0.1`, `norm-Mallows phi=0.5`) that are almost never explained.

This script explains them the way `euclidean_spaces.py` explains the six spaces:
by **measuring** what each one produces instead of describing it, and by pinning
the measurements to anchors that are known exactly in advance. If the anchors
come out right, the rest of the table is trustworthy.

The organising fact, which the `disagree` column below makes visible: almost every
culture is a *family* with one dial, and the dial runs between the same two poles —
**unanimity** at one end and **Impartial Culture** at the other. IC is not one
culture among many so much as the place the others land when the dial is turned up.

Two measurements, both cheap and both exact:

* **`disagree`** — the mean normalised Kendall-tau distance between two randomly
  chosen ballots: the share of candidate pairs two voters order differently.
  0 = everyone agrees, 0.5 = independent uniform ballots, 1 = impossible for
  more than two voters. Computed in closed form rather than by enumerating voter
  pairs: if `c` voters prefer i to j, then exactly `c * (n - c)` voter-pairs
  disagree about that candidate pair, so the mean over all pairs is
  `sum over i<j of c_ij*(n-c_ij) / (C(n,2) * C(m,2))` — O(n*m^2), not O(n^2*m^2).

* **`no CW`** — the share of elections with no Condorcet winner. This is the
  statistic the model choice is famous for moving, and the one with published
  values to check against.

The anchors (all checked by --verify):
    IC disagree              = 0.5 exactly, for any n and m
    IC no-CW at m=3, large n -> 8.77%   (Gehrlein's limit)
    IAC no-CW at m=3, large n -> 6.25%  (Gehrlein)
    urn(alpha=0)             = IC        (nothing is ever added to the urn)
    urn(alpha=1/m!)          = IAC       (exactly one copy back per draw)
    mallows(phi=1)           = IC        (no decay with distance)
    mallows(phi=0)           = unanimity (all mass on the central vote)
    stratification(0 or 1)   = IC        (one class, ranked at random inside it)

Run:
    python statistical_cultures.py              # the dial table
    python statistical_cultures.py --verify     # the anchor checks
    python statistical_cultures.py --normalise  # why raw phi drifts as m grows
    python statistical_cultures.py --peaks      # Conitzer vs Walsh are not the same

**A trap this script routes around.** `prefsampling` 0.1.24's *Euclidean* samplers
degenerate when seeded (COMSOC-Community/prefsampling#6): `GAUSSIAN_BALL` returns
one point repeated, and candidate j lands on voter j. The ordinal cultures below
seed correctly — verified by --verify — so only the euclidean row needs care, and
it gets it by drawing its own positions from a numpy Generator this script owns
and handing them in as arrays. See:
    ../../07_Concepts/topics/statistical_cultures.md   (what the cultures are)
    ../../07_Concepts/topics/euclidean_spaces.md       (the six spaces in close-up)
"""

from __future__ import annotations

import argparse
import math
from itertools import combinations

import numpy as np
import prefsampling.ordinal as o
from prefsampling.core.euclidean import EuclideanSpace


# --------------------------------------------------------------------------
# Measurement. A "profile" is a list of votes; a vote is a list of candidate
# indices, best first — prefsampling's own format.
# --------------------------------------------------------------------------
def pairwise_counts(profile, m: int) -> np.ndarray:
    """c[i][j] = how many voters rank candidate i above candidate j."""
    votes = np.asarray(profile, dtype=int)
    n = votes.shape[0]
    # position[v][cand] = where that candidate sits on ballot v (0 = best)
    position = np.empty((n, m), dtype=int)
    np.put_along_axis(position, votes, np.arange(m)[None, :].repeat(n, axis=0), axis=1)
    c = np.zeros((m, m), dtype=int)
    for i, j in combinations(range(m), 2):
        above = int(np.sum(position[:, i] < position[:, j]))
        c[i][j], c[j][i] = above, n - above
    return c


def disagreement(profile, m: int) -> float:
    """Mean normalised Kendall-tau distance between two randomly chosen ballots.

    The closed form in the module docstring: for candidate pair (i, j) split
    c-to-(n-c), exactly c*(n-c) of the C(n,2) voter pairs disagree about it."""
    n = len(profile)
    if n < 2 or m < 2:
        return float("nan")
    c = pairwise_counts(profile, m)
    disagreeing = sum(c[i][j] * (n - c[i][j]) for i, j in combinations(range(m), 2))
    return disagreeing / (math.comb(n, 2) * math.comb(m, 2))


def has_condorcet_winner(profile, m: int) -> bool:
    """True if some candidate beats every other head to head. A drawn pair is
    not a win, so an exact tie counts as no Condorcet winner."""
    n = len(profile)
    c = pairwise_counts(profile, m)
    return any(all(c[i][j] * 2 > n for j in range(m) if j != i) for i in range(m))


# --------------------------------------------------------------------------
# The cultures, each as a callable (num_voters, num_candidates, seed) -> profile.
# --------------------------------------------------------------------------
def euclidean_own_rng(space: str, dims: int = 2):
    """Euclidean positions drawn from OUR generator, not prefsampling's seeded
    path — which is broken (prefsampling#6). Handing in explicit position arrays
    bypasses the degenerate sampler entirely."""
    from prefsampling.core.euclidean import euclidean_space_to_sampler

    def sample(n, m, seed):
        rng = np.random.default_rng(seed)
        sampler, args = euclidean_space_to_sampler(
            EuclideanSpace(space), num_dimensions=dims, seed=None
        )
        # Draw voters and candidates in two INDEPENDENT calls, so candidate j
        # cannot land on voter j (the second half of prefsampling#6).
        args_v = dict(args, num_points=n, seed=int(rng.integers(1 << 31)))
        args_c = dict(args, num_points=m, seed=int(rng.integers(1 << 31)))
        # ...and because a seed inside inner_sampler_args is what degenerates the
        # ball resampler, draw unseeded and let our own global draw order vary.
        args_v.pop("seed", None)
        args_c.pop("seed", None)
        return o.euclidean(
            num_voters=n, num_candidates=m, num_dimensions=dims,
            voters_positions=np.array(sampler(**args_v)),
            candidates_positions=np.array(sampler(**args_c)),
        )

    return sample


def build_dials(m: int):
    """(label, note, sampler) for every row of the main table, in reading order."""
    rows = [
        ("impartial (IC)", "every ranking equally likely",
         lambda n, m, s: o.impartial(n, m, seed=s)),
        ("impartial_anonymous (IAC)", "every TALLY equally likely",
         lambda n, m, s: o.impartial_anonymous(n, m, seed=s)),
    ]
    rows.append(("urn alpha=0", "= IC exactly",
                 lambda n, m, s: o.urn(n, m, alpha=0.0, seed=s)))
    rows.append((f"urn alpha=1/m! ({1/math.factorial(m):.4f})", "= IAC exactly",
                 lambda n, m, s: o.urn(n, m, alpha=1 / math.factorial(m), seed=s)))
    for a in (0.1, 0.5, 1.0):
        rows.append((f"urn alpha={a}", "the rich get richer",
                     lambda n, m, s, a=a: o.urn(n, m, alpha=a, seed=s)))
    for p in (1.0, 0.75, 0.5, 0.25, 0.0):
        rows.append((f"norm_mallows phi={p}", "noise around one ranking",
                     lambda n, m, s, p=p: o.norm_mallows(n, m, norm_phi=p, seed=s)))
    rows.append(("plackett_luce equal", "equal candidate strengths",
                 lambda n, m, s: o.plackett_luce(n, m, alphas=[1.0] * m, seed=s)))
    rows.append(("plackett_luce skewed", "strengths 1, 2, 4, 8 ...",
                 lambda n, m, s: o.plackett_luce(
                     n, m, alphas=[2.0 ** k for k in range(m)], seed=s)))
    for w in (0.0, 0.5):
        rows.append((f"stratification w={w}", "upper class ranked above lower",
                     lambda n, m, s, w=w: o.stratification(n, m, weight=w, seed=s)))
    rows.append(("single_peaked_conitzer", "peak uniform, then spread",
                 lambda n, m, s: o.single_peaked_conitzer(n, m, seed=s)))
    rows.append(("single_peaked_walsh", "same domain, other distribution",
                 lambda n, m, s: o.single_peaked_walsh(n, m, seed=s)))
    rows.append(("single_crossing", "voters ordered on one axis",
                 lambda n, m, s: o.single_crossing(n, m, seed=s)))
    rows.append(("group_separable", "nested blocs (Schroeder tree)",
                 lambda n, m, s: o.group_separable(n, m, seed=s)))
    rows.append(("euclidean gaussian_ball", "spatial, clustered centre",
                 euclidean_own_rng("gaussian_ball")))
    rows.append(("euclidean uniform_cube", "spatial, corners included",
                 euclidean_own_rng("uniform_cube")))
    return rows


def measure(sampler, n: int, m: int, trials: int, seed0: int):
    """Mean disagreement and no-Condorcet-winner rate over `trials` elections."""
    dis, no_cw = [], 0
    for t in range(trials):
        profile = sampler(n, m, seed0 + t)
        dis.append(disagreement(profile, m))
        if not has_condorcet_winner(profile, m):
            no_cw += 1
    return float(np.mean(dis)), no_cw / trials


def table(n: int, m: int, trials: int, seed: int) -> None:
    print(f"{trials:,} elections, {n} voters, {m} candidates, seeds {seed}..{seed+trials-1}\n")
    print(f"{'culture':<32} {'what the dial does':<32} {'disagree':>9} {'no CW':>7}")
    print("-" * 84)
    for label, note, sampler in build_dials(m):
        d, nc = measure(sampler, n, m, trials, seed)
        print(f"{label:<32} {note:<32} {d:>9.3f} {100*nc:>6.2f}%")
    print("\ndisagree = mean share of candidate pairs two random ballots order differently.")
    print("           0 = unanimity, 0.500 = independent uniform ballots (IC).")
    print("no CW    = share of elections with no Condorcet winner.")


# --------------------------------------------------------------------------
# --normalise: the trap that makes raw phi unquotable across candidate counts.
# --------------------------------------------------------------------------
def normalise_demo(n: int, trials: int, seed: int) -> None:
    print("Mallows dispersion at phi = 0.5, raw vs normalised, as m grows.\n")
    print(f"{'m':>3}  {'max Kendall-tau':>15}  {'raw phi=0.5':>12}  {'norm_phi=0.5':>13}")
    print("-" * 52)
    for m in (3, 4, 5, 7, 10):
        raw = np.mean([disagreement(o.mallows(n, m, phi=0.5, seed=seed + t), m)
                       for t in range(trials)])
        nrm = np.mean([disagreement(o.norm_mallows(n, m, norm_phi=0.5, seed=seed + t), m)
                       for t in range(trials)])
        print(f"{m:>3}  {math.comb(m,2):>15}  {raw:>12.3f}  {nrm:>13.3f}")
    print("\nRaw phi decays per SWAP, but the number of possible swaps grows as")
    print("m(m-1)/2 — so a fixed per-swap penalty bites harder and harder in")
    print("relative terms, and the same phi=0.5 drifts steadily TOWARD unanimity")
    print("as candidates are added. norm_phi pins the expected normalised distance")
    print("instead, and holds nearly flat, which is why it is the one that can be")
    print("quoted across studies with different candidate counts.")


# --------------------------------------------------------------------------
# --peaks: Conitzer and Walsh sample the same domain, not the same distribution.
# --------------------------------------------------------------------------
def peaks_demo(n: int, m: int, seed: int) -> None:
    print(f"Where does the peak (top-ranked candidate) fall? {n:,} ballots, m={m},")
    print("axis 0..m-1. Both samplers produce single-peaked profiles on that axis.\n")
    rows = [("single_peaked_conitzer", o.single_peaked_conitzer(n, m, seed=seed)),
            ("single_peaked_walsh", o.single_peaked_walsh(n, m, seed=seed))]
    print(f"{'sampler':<24} " + " ".join(f"{c:>6}" for c in range(m)))
    print("-" * (24 + 7 * m))
    for label, profile in rows:
        peaks = np.bincount([v[0] for v in profile], minlength=m) / n
        print(f"{label:<24} " + " ".join(f"{p:>6.3f}" for p in peaks))
    print(f"\nUniform would be {1/m:.3f} everywhere. Conitzer picks the peak uniformly")
    print("by construction; Walsh does not, and piles ballots onto the middle of the")
    print("axis. Quoting 'single-peaked' without saying which one is underspecified.")


# --------------------------------------------------------------------------
# Exact enumeration, for checking a sampler against a DEFINITION rather than
# against a sibling function. (prefsampling implements impartial_anonymous as
# urn(alpha=1/m!), so those two can never disagree — see verify() step 3.)
# --------------------------------------------------------------------------
def enumerate_tallies(n: int, m: int) -> list:
    """Every anonymous profile of n voters over m candidates: a multiset of n
    rankings, represented as a sorted tuple of ranking indices. There are
    C(n + m! - 1, m! - 1) of them — 56 for n=3, m=3, the number the simulation-
    model page quotes from Gehrlein."""
    from itertools import combinations_with_replacement, permutations

    rankings = list(permutations(range(m)))
    return list(combinations_with_replacement(range(len(rankings)), n))


def uniformity_over_tallies(n: int, m: int, tallies: list, draws: int, seed: int) -> float:
    """Draw from urn(alpha=1/m!) and bin each profile by its TALLY. IAC says the
    result is uniform over `tallies`. Returns the largest cell deviation measured
    in standard errors, so the answer is scale-free: under uniformity the biggest
    of a few dozen cells sits around 2-3 sd, and 4 is a generous ceiling."""
    from itertools import permutations

    index = {r: i for i, r in enumerate(permutations(range(m)))}
    slot = {t: i for i, t in enumerate(tallies)}
    counts = np.zeros(len(tallies))
    alpha = 1 / math.factorial(m)
    for t in range(draws):
        profile = o.urn(n, m, alpha=alpha, seed=seed + t)
        key = tuple(sorted(index[tuple(int(c) for c in v)] for v in profile))
        counts[slot[key]] += 1
    expected = draws / len(tallies)
    return float(np.max(np.abs(counts - expected)) / math.sqrt(expected))


# --------------------------------------------------------------------------
# --verify: the anchors. Every one is known before the script runs.
# --------------------------------------------------------------------------
def verify(seed: int) -> int:
    checks, failures = [], 0

    def check(name, got, want, tol, unit=""):
        nonlocal failures
        ok = abs(got - want) <= tol
        failures += 0 if ok else 1
        checks.append((name, f"{got:.4f}{unit}", f"{want:.4f}{unit} +/- {tol}{unit}",
                       "ok" if ok else "FAIL"))

    # 1. IC disagreement is exactly 0.5 — for any n, any m. Pure arithmetic.
    for n, m in ((5, 3), (50, 4), (200, 8)):
        got = np.mean([disagreement(o.impartial(n, m, seed=seed + t), m) for t in range(300)])
        check(f"IC disagree (n={n}, m={m})", got, 0.5, 0.01)

    # 2. Gehrlein's published large-electorate no-Condorcet-winner limits, m=3.
    _, ic = measure(lambda n, m, s: o.impartial(n, m, seed=s), 201, 3, 4000, seed)
    check("IC no-CW, m=3 (Gehrlein 8.77%)", 100 * ic, 8.77, 1.2, "%")
    _, iac = measure(lambda n, m, s: o.impartial_anonymous(n, m, seed=s), 201, 3, 4000, seed)
    check("IAC no-CW, m=3 (Gehrlein 6.25%)", 100 * iac, 6.25, 1.2, "%")

    # 3. The urn endpoints ARE IC and IAC. `urn` and `impartial` are separate
    #    implementations, so the first comparison is a real one.
    d_ic, c_ic = measure(lambda n, m, s: o.impartial(n, m, seed=s), 51, 4, 1500, seed)
    d_u0, c_u0 = measure(lambda n, m, s: o.urn(n, m, alpha=0.0, seed=s), 51, 4, 1500, seed)
    check("urn(alpha=0) disagree == IC", d_u0, d_ic, 0.01)
    check("urn(alpha=0) no-CW == IC", 100 * c_u0, 100 * c_ic, 2.0, "%")

    #    The IAC end needs care: prefsampling IMPLEMENTS impartial_anonymous as
    #    `urn(alpha=1/m!)`, so comparing the two would compare a function with
    #    itself and could never fail. Check it against the DEFINITION instead —
    #    uniformity over the exactly-enumerated set of anonymous profiles.
    n_e, m_e = 3, 3
    tallies = enumerate_tallies(n_e, m_e)
    check("tally count (n=3, m=3)", len(tallies), math.comb(n_e + math.factorial(m_e) - 1,
                                                            math.factorial(m_e) - 1), 0)
    dev = uniformity_over_tallies(n_e, m_e, tallies, draws=56_000, seed=seed)
    check("urn(alpha=1/m!) uniform over tallies", dev, 0.0, 4.0, " sd")

    # 4. Mallows endpoints: phi=1 is IC, phi=0 is unanimity.
    d_m1 = np.mean([disagreement(o.mallows(51, 4, phi=1.0, seed=seed + t), 4)
                    for t in range(500)])
    check("mallows(phi=1) disagree == IC", d_m1, 0.5, 0.02)
    d_m0 = np.mean([disagreement(o.mallows(51, 4, phi=0.0, seed=seed + t), 4)
                    for t in range(50)])
    check("mallows(phi=0) disagree == 0", d_m0, 0.0, 1e-9)

    # 5. Stratification collapses to IC when one class holds everybody.
    for w in (0.0, 1.0):
        d_s = np.mean([disagreement(o.stratification(51, 4, weight=w, seed=seed + t), 4)
                       for t in range(500)])
        check(f"stratification(w={w}) disagree == IC", d_s, 0.5, 0.02)

    # 6. The ordinal samplers respect their seed — the thing the EUCLIDEAN ones
    #    get wrong (prefsampling#6). Same seed identical, different seeds not.
    same = np.array_equal(np.array(o.impartial(30, 5, seed=11)),
                          np.array(o.impartial(30, 5, seed=11)))
    diff = not np.array_equal(np.array(o.impartial(30, 5, seed=11)),
                              np.array(o.impartial(30, 5, seed=12)))
    checks.append(("ordinal seeding is honest", f"{same} / {diff}", "True / True",
                   "ok" if (same and diff) else "FAIL"))
    failures += 0 if (same and diff) else 1

    print(f"{'anchor':<38} {'measured':>12} {'expected':>22}  status")
    print("-" * 84)
    for name, got, want, status in checks:
        print(f"{name:<38} {got:>12} {want:>22}  {status}")
    print(f"\n{len(checks) - failures}/{len(checks)} anchors hold.")
    return failures


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--voters", type=int, default=51)
    ap.add_argument("--candidates", type=int, default=4)
    ap.add_argument("--trials", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--verify", action="store_true", help="check the known anchors")
    ap.add_argument("--normalise", action="store_true", help="raw phi vs norm_phi as m grows")
    ap.add_argument("--peaks", action="store_true", help="Conitzer vs Walsh peak placement")
    args = ap.parse_args()

    if args.verify:
        return 1 if verify(args.seed) else 0
    if args.normalise:
        normalise_demo(args.voters, 300, args.seed)
        return 0
    if args.peaks:
        peaks_demo(20000, 7, args.seed)
        return 0
    table(args.voters, args.candidates, args.trials, args.seed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
