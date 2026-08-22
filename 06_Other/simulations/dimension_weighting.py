#!/usr/bin/env python3
"""
dimension_weighting.py — does a FLAT high-dimensional electorate really make the
voting methods agree, and does Zipf weighting really fix it?

WHY THIS EXISTS
---------------
07_Concepts/topics/spatial_voting_model.md repeats a claim that circulates widely
in the simulation literature: a spatial model with many EQUALLY-weighted axes
makes every method elect the same candidate, so you would wrongly conclude the
method barely matters; weight the axes by Zipf's law (later axes matter less) and
realistic disagreement comes back.

The claim is right in direction. The two explanations usually given for it are
not, and this script exists because both are checkable in twenty lines.

WHAT IS ACTUALLY MEASURED (100 dimensions, 101 voters, 5 candidates)
---------------------------------------------------------------------
                        flat      zipf(var~1/k)   zipf(sd~1/k)
  effective dimension   100.0          16.5             2.5
  all 4 methods agree    85.3%         67.0%           41.8%
  voter-pair rank corr  +0.272        +0.265          +0.252
  best-vs-2nd gap        27.7%         21.1%           16.3%
  Condorcet winner       99.7%         99.3%           99.7%

  (methods: Plurality, Approval-above-own-mean, STAR on 0-5 min-max, Copeland.
   "gap" is the utilitarian leader's lead over the runner-up as a share of the
   whole field's spread. "rank corr" is the mean Spearman correlation between
   two voters' orderings of the candidates.)

THREE CORRECTIONS THIS PRODUCES
--------------------------------
1. "Every method agrees" overstates it. Flat 100-D still disagrees 14.7% of the
   time on a five-candidate field. It is a strong tendency, not a collapse.

2. The usual MECHANISM is wrong. It is normally explained as the electorate
   becoming near-unanimous - an obvious centre everybody likes. Measured, voters
   are just as divided in both models: mean pairwise rank correlation +0.272 flat
   vs +0.252 Zipf, essentially unchanged. A flat model does not make VOTERS
   agree. It makes METHODS agree, which is a different fact and needs a different
   explanation. (The "dense ball at the centre" version of the story is also
   backwards: a high-dimensional Gaussian concentrates on a thin SHELL, and the
   centre of the cloud is nearly empty.)

3. The mechanism that IS visible here is candidate separation. In flat 100-D the
   utilitarian leader beats the runner-up by 27.7% of the field's spread; under
   Zipf it is 16.3%. Methods agree when someone is far ahead and split hairs when
   the race is close. Zipf weighting does not abolish the centre - a Condorcet
   winner still exists ~99.5% of the time in every model here, and is still the
   utilitarian optimum ~92% of the time. It just stops the centre from winning by
   a mile.

WHICH ZIPF? THE AMBIGUITY IS MATERIAL
--------------------------------------
"Scale axis k by Zipf" has two readings and they are not close:

    variance ~ 1/k   ->  sd ~ 1/sqrt(k),  effective dimension 16.5
    sd       ~ 1/k   ->  variance ~ 1/k^2, effective dimension  2.5

Effective dimension here is the participation ratio (sum L)^2 / sum(L^2) over the
per-axis variances - the number of axes that carry the variation, as opposed to
the number declared. The second reading is the one that matches the usual prose
gloss ("one dominant axis and a few minor ones"); the first still leaves sixteen
axes doing real work, and lands halfway to flat on every measure above. Say which
one a number came from.

USAGE
-----
    python 06_Other/simulations/dimension_weighting.py
    python 06_Other/simulations/dimension_weighting.py --dims 20 --candidates 8

TIE-BREAKS (fixed, for reproducibility)
---------------------------------------
argmax throughout, i.e. ties to the lower candidate index. Same convention as the
other scripts in this folder, and NOT the engine's published ladder.
"""

from __future__ import annotations

import argparse

import numpy as np


def axis_sd(model: str, d: int) -> np.ndarray:
    """Per-axis standard deviation under each weighting."""
    k = np.arange(1.0, d + 1.0)
    if model == "flat":
        return np.ones(d)
    if model == "zipf_var":      # variance ~ 1/k
        return np.sqrt(1.0 / k)
    if model == "zipf_sd":       # sd ~ 1/k
        return 1.0 / k
    raise ValueError(model)


def winners(u: np.ndarray, m: int) -> tuple[int, int, int, int]:
    """Plurality, Approval (above own mean), STAR (0-5 min-max), Copeland."""
    plur = int(np.bincount(u.argmax(1), minlength=m).argmax())
    appr = int((u > u.mean(1, keepdims=True)).sum(0).argmax())

    mn, mx = u.min(1, keepdims=True), u.max(1, keepdims=True)
    s = np.floor((u - mn) / np.where(mx > mn, mx - mn, 1.0) * 5 + 0.5)
    a, b = np.argsort(-s.sum(0), kind="stable")[:2]
    pa = int((s[:, a] > s[:, b]).sum())
    pb = int((s[:, b] > s[:, a]).sum())
    star = int(a if pa >= pb else b)

    p = (u[:, :, None] > u[:, None, :]).sum(0)
    cope = int(((p > p.T).sum(1) - (p < p.T).sum(1)).argmax())
    return plur, appr, star, cope


def run(model, dims, voters, cands, elections, seed):
    rng = np.random.default_rng(seed)
    sd = axis_sd(model, dims)
    lam = sd ** 2
    eff = lam.sum() ** 2 / (lam ** 2).sum()

    agree = cw = cw_util = 0
    corr = gap = 0.0
    iu = np.triu_indices(voters, 1)

    for _ in range(elections):
        vp = rng.normal(0, 1, (voters, dims)) * sd
        cp = rng.normal(0, 1, (cands, dims)) * sd
        u = -np.linalg.norm(vp[:, None, :] - cp[None, :, :], axis=2)

        agree += int(len(set(winners(u, cands))) == 1)

        r = u.argsort(1).argsort(1).astype(float)
        r -= r.mean(1, keepdims=True)
        norm = np.sqrt((r ** 2).sum(1))
        corr += float(((r @ r.T) / np.outer(norm, norm))[iu].mean())

        soc = u.sum(0)
        o = np.sort(soc)[::-1]
        gap += (o[0] - o[1]) / (o[0] - o[-1])

        beats = ((u[:, :, None] > u[:, None, :]).sum(0) >
                 (u[:, :, None] < u[:, None, :]).sum(0)).sum(1)
        if (beats == cands - 1).any():
            cw += 1
            cw_util += int(int(np.argmax(beats == cands - 1)) == int(soc.argmax()))

    n = elections
    return {
        "eff": eff,
        "agree": 100.0 * agree / n,
        "corr": corr / n,
        "gap": 100.0 * gap / n,
        "cw": 100.0 * cw / n,
        "cw_util": 100.0 * cw_util / max(cw, 1),
    }


def main() -> None:
    p = argparse.ArgumentParser(
        description="Flat vs Zipf-weighted axes: what the weighting actually changes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--dims", type=int, default=100)
    p.add_argument("--voters", type=int, default=101)
    p.add_argument("--candidates", type=int, default=5)
    p.add_argument("--elections", type=int, default=600)
    p.add_argument("--seed", type=int, default=42)
    a = p.parse_args()

    models = ["flat", "zipf_var", "zipf_sd"]
    res = {m: run(m, a.dims, a.voters, a.candidates, a.elections, a.seed) for m in models}

    print(f"\n=== {a.dims}-D, {a.voters} voters, {a.candidates} candidates, "
          f"{a.elections} elections, seed {a.seed} ===\n")
    print("                          " + "".join(f"{m:>14}" for m in models))
    rows = [
        ("effective dimension", "eff", "{:>14.1f}"),
        ("all 4 methods agree", "agree", "{:>13.1f}%"),
        ("voter-pair rank corr", "corr", "{:>+14.3f}"),
        ("best-vs-2nd gap", "gap", "{:>13.1f}%"),
        ("Condorcet winner exists", "cw", "{:>13.1f}%"),
        ("  ...and utilitarian best", "cw_util", "{:>13.1f}%"),
    ]
    for label, key, fmt in rows:
        print(f"  {label:<26}" + "".join(fmt.format(res[m][key]) for m in models))
    print()


if __name__ == "__main__":
    main()
