#!/usr/bin/env python3
"""
euclidean_spaces.py — the six shapes a spatial electorate can be drawn from
===========================================================================
Every spatial simulation in this folder starts the same way: scatter voters and
candidates as points, and let each voter prefer whoever is nearest. *Where* those
points come from is a parameter with a name — `uniform_ball`, `gaussian_cube`,
`unbounded_gaussian` and three more — and the names show up in this repo's own
results (the Condorcet-tie sweep quotes them by name) without ever being defined.
This script defines them the only way worth trusting: it **implements each one in
a few lines from its own description**, checks that implementation against
`prefsampling`'s, and draws the picture.

The teaching claim is that these are simple. The proof is that `SPACES` below is
about forty lines of numpy for all six.

Two facts they encode, which is why the choice matters at all:

* **Shape** decides whether extreme voters exist. A cube has corners; a ball does
  not; an unbounded Gaussian has no edge at all, so a simulation on it will
  eventually draw a voter a thousand units from everyone.
* **Density** decides where the median voter is and how crowded the middle gets.
  Uniform spreads voters evenly, so a "centrist" is just another point; Gaussian
  piles them up in the middle, which is what makes centre squeeze visible.

Run:
    python euclidean_spaces.py                    # the stats table + cross-check
    python euclidean_spaces.py --gallery          # also draw img/euclidean_spaces.png
    python euclidean_spaces.py --dimensions 3     # the table in 3-D

**A trap this script deliberately does not use.** `prefsampling`'s own seeded
Euclidean path is broken — seeding it collapses `gaussian_ball` to a single
repeated point and lands candidate *j* exactly on voter *j*. Filed as
COMSOC-Community/prefsampling#6 and voting-tools/pref_voting#186. So the
cross-check below runs prefsampling **unseeded**, where it is correct, and
compares distributions rather than points. See:
    ../../07_Concepts/topics/euclidean_spaces.md   (what the six spaces are)
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

# --------------------------------------------------------------------------
# The six spaces, each from its definition. `rng` is a numpy Generator; every
# sampler returns an (n, d) array. prefsampling's defaults are width 1 (so a
# ball of radius 0.5, a cube of side 1) and sigma 0.33 inside the Gaussian ball,
# 1 elsewhere — matched here so the cross-check is meaningful.
# --------------------------------------------------------------------------
RADIUS = 0.5      # = width / 2
HALFSIDE = 0.5    # = width / 2
SIGMA_BALL = 0.33
SIGMA_PLAIN = 1.0


def uniform_cube(rng, n, d):
    """Each coordinate independent and uniform on [-0.5, 0.5]. A box, corners and all."""
    return rng.uniform(-HALFSIDE, HALFSIDE, size=(n, d))


def _directions(rng, n, d):
    """n uniformly random directions. A Gaussian vector is spherically symmetric,
    so normalising one gives a direction with no preferred axis — normalising a
    *uniform* vector would bunch points toward the corners."""
    v = rng.normal(size=(n, d))
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def uniform_sphere(rng, n, d):
    """Uniform on the SHELL: a random direction at fixed radius. Every point is
    exactly as extreme as every other — a model of pure factions, no moderates."""
    return RADIUS * _directions(rng, n, d)


def uniform_ball(rng, n, d):
    """Uniform on the SOLID ball. Direction as above, radius = R * U**(1/d).
    The 1/d power is the whole trick: volume grows like r**d, so a uniform radius
    would crowd the centre. In 2-D that means sqrt(U), not U."""
    radii = RADIUS * rng.random(n) ** (1.0 / d)
    return _directions(rng, n, d) * radii[:, None]


def unbounded_gaussian(rng, n, d):
    """Each coordinate independent Normal(0, 1). No edge: the tails run forever,
    so with enough draws you WILL get an extremist far outside every candidate."""
    return rng.normal(0.0, SIGMA_PLAIN, size=(n, d))


def _rejection(rng, n, d, sigma, accept):
    """Draw Normal points, throw away the ones outside, repeat. The standard way
    to sample a truncated distribution — and the reason both Gaussian-bounded
    spaces cost more than their unbounded sibling."""
    out = []
    while len(out) < n:
        p = rng.normal(0.0, sigma, size=d)
        if accept(p):
            out.append(p)
    return np.array(out)


def gaussian_cube(rng, n, d):
    """Normal(0, 1) per coordinate, redrawn until every coordinate is inside the
    box. Bell-shaped in the middle, hard walls at the edge. Note the mismatch in
    prefsampling's defaults: sigma 1 against a half-width of 0.5, so most draws
    are rejected (see the acceptance column)."""
    return _rejection(rng, n, d, SIGMA_PLAIN,
                      lambda p: np.all(np.abs(p) <= HALFSIDE))


def gaussian_ball(rng, n, d):
    """Normal(0, 0.33) per coordinate, redrawn until the point is inside the ball
    of radius 0.5. The narrow sigma is chosen so most draws already land inside —
    which is what makes it the realistic 'clustered electorate' of the six."""
    return _rejection(rng, n, d, SIGMA_BALL,
                      lambda p: np.linalg.norm(p) <= RADIUS)


SPACES = {
    "uniform_ball": uniform_ball,
    "uniform_sphere": uniform_sphere,
    "uniform_cube": uniform_cube,
    "gaussian_ball": gaussian_ball,
    "gaussian_cube": gaussian_cube,
    "unbounded_gaussian": unbounded_gaussian,
}

BLURB = {
    "uniform_ball": "solid ball, evenly filled",
    "uniform_sphere": "the ball's SHELL only",
    "uniform_cube": "box, corners included",
    "gaussian_ball": "clustered, clipped to a ball",
    "gaussian_cube": "clustered, clipped to a box",
    "unbounded_gaussian": "clustered, no edge at all",
}


# --------------------------------------------------------------------------
# Cross-check against prefsampling (UNSEEDED — see the docstring).
# --------------------------------------------------------------------------
def prefsampling_sample(space: str, n: int, d: int):
    """The same space, drawn by prefsampling itself. Returns None if unavailable."""
    try:
        from prefsampling.core.euclidean import EuclideanSpace, euclidean_space_to_sampler
    except ImportError:
        return None
    sampler, args = euclidean_space_to_sampler(
        EuclideanSpace(space), num_dimensions=d, seed=None
    )
    args["num_points"] = n
    return np.array(sampler(**args))


def stats(points: np.ndarray) -> dict:
    r = np.linalg.norm(points, axis=1)
    return {
        "mean_r": r.mean(),
        "max_r": r.max(),
        "sd_coord": points.std(),
        # tolerance: uniform_sphere sits exactly ON the boundary, and rounding
        # would otherwise report it as 99% inside rather than 100%.
        "in_ball": float(np.mean(r <= RADIUS + 1e-9)),
        # The column that actually separates "clustered" from "uniform": share of
        # points in the INNER HALF-radius. A uniform 2-D ball gives exactly 25%
        # (area scales as r^2); anything higher is genuine central clustering.
        "inner": float(np.mean(r <= RADIUS / 2)),
    }


def acceptance_rate(space: str, d: int) -> str:
    """Analytic share of draws a rejection sampler keeps, for the two that use one."""
    if space == "gaussian_ball":
        if d == 2:  # Rayleigh: P(||X|| <= r) = 1 - exp(-r^2 / 2s^2)
            return f"{100 * (1 - math.exp(-RADIUS**2 / (2 * SIGMA_BALL**2))):.0f}%"
        return "—"
    if space == "gaussian_cube":
        # per-dimension P(|Z| <= 0.5) with sigma 1, independent across dimensions
        per = math.erf(HALFSIDE / (SIGMA_PLAIN * math.sqrt(2)))
        return f"{100 * per**d:.0f}%"
    return "100%"


def table(n: int, d: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    print(f"{n:,} points, {d} dimension(s), seed {seed}\n")
    print(f"{'space':<20} {'what it is':<30} {'mean r':>7} {'in ball':>8} "
          f"{'inner':>6} {'kept':>6}  cross-check")
    print("-" * 103)
    for space, fn in SPACES.items():
        mine = stats(fn(rng, n, d))
        theirs_pts = prefsampling_sample(space, n, d)
        if theirs_pts is None:
            verdict = "prefsampling not installed"
        else:
            theirs = stats(theirs_pts)
            worst = max(abs(mine[k] - theirs[k]) for k in ("mean_r", "sd_coord", "in_ball"))
            verdict = f"agrees (max diff {worst:.3f})" if worst < 0.02 else \
                      f"DIFFERS by {worst:.3f}"
        print(f"{space:<20} {BLURB[space]:<30} {mine['mean_r']:>7.3f} "
              f"{mine['in_ball']:>7.0%} {mine['inner']:>5.0%} "
              f"{acceptance_rate(space, d):>6}  {verdict}")
    print(
        "\n'in ball' = share within radius 0.5 of the origin — separates the bounded\n"
        "spaces from the unbounded one. 'inner' = share within radius 0.25, which is\n"
        "the honest test of CLUSTERING: a uniform 2-D ball scores exactly 25%, so a\n"
        "space calling itself Gaussian ought to score well above that. 'kept' = share\n"
        "of draws a rejection sampler accepts; 100% means it doesn't reject at all."
    )


# --------------------------------------------------------------------------
# The picture.
# --------------------------------------------------------------------------
def gallery(n: int, seed: int, out: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    rng = np.random.default_rng(seed)
    fig, axes = plt.subplots(2, 3, figsize=(10.5, 7.2))
    for ax, (space, fn) in zip(axes.ravel(), SPACES.items()):
        pts = fn(rng, n, 2)
        ax.scatter(pts[:, 0], pts[:, 1], s=5, alpha=0.5, edgecolors="none",
                   color="#2b6cb0")
        ax.set_title(f"{space}\n{BLURB[space]}", fontsize=10)
        lim = 2.6 if space == "unbounded_gaussian" else 0.62
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for side in ax.spines.values():
            side.set_color("#cbd5e0")
    fig.suptitle(
        f"The six Euclidean spaces — {n:,} voters each, 2-D "
        "(note: unbounded_gaussian is drawn at a wider zoom)",
        fontsize=11,
    )
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=140, bbox_inches="tight")
    print(f"\nwrote {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=20000, help="points per space (default 20000)")
    ap.add_argument("--dimensions", type=int, default=2, help="default 2")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--gallery", action="store_true", help="also draw the six-panel PNG")
    args = ap.parse_args()

    table(args.n, args.dimensions, args.seed)
    if args.gallery:
        gallery(min(args.n, 3000), args.seed,
                Path(__file__).parent / "img" / "euclidean_spaces.png")


if __name__ == "__main__":
    main()
