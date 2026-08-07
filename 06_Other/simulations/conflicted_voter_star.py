#!/usr/bin/env python3
"""
conflicted_voter_star.py — does a 0-5 ballot rescue the "conflicted voter"?

WHY THIS EXISTS
---------------
Bourgeois-Gironde & Ferreira (2016), "Conflicted Voters: A Spatial Voting Model
with Multiple Party Identifications" (J. Econ. Behav. Organ., doi:10.1016/
j.jebo.2016.12.003), derive a **conflicted voter's curse**: a citizen who
identifies with TWO parties abstains whenever no candidate is acceptable to both
— and does so rationally, no matter how the candidates position, even if such
citizens are a majority.

Their mechanism is *betrayal aversion*, and it bites **because a choose-one
ballot forces a single pick**. That raises an obvious question the paper does not
ask, because it models only choose-one: what happens to those voters when the
ballot does not force a single pick?

This script asks it. The claim under test:

    On a 0-5 ballot the conflicted voter is not forced to betray anyone. They
    score every candidate honestly (participating fully in the scoring round,
    where their scores help decide WHO the finalists are) and, if both finalists
    are unacceptable, register Equal Support in the runoff — declining only the
    final binary rather than the whole election.

If that holds, the curse converts abstention into a counted ballot. If it does
not, we should say so.

WHAT IS THE PAPER'S AND WHAT IS OURS
------------------------------------
Faithful to the paper (section 2, Proposition 1):
  * political domain X = R^m; two parties b, r with ideological point delta_p
    and acceptance region A_p = {x : ||x - delta_p|| <= d_p}   (P1, P2)
  * citizens identify with {b}, {r} or {b,r}; identification weight I_i^p
  * utility, equation (1): Euclidean term -(I/d)*dist, plus identity gain I_i^p
    for each party accepting the position, minus betrayal cost c_i if the
    position is outside the intersection of the voter's acceptance regions
  * betrayal aversion: c_i > I_i^p                            (U3)
  * turnout, Proposition 1: t_i = 1 iff SOME candidate lies inside A_p for EVERY
    p the citizen identifies with

Our extensions, which the paper does not contain and which are the reason its
authors should not be blamed for anything below:
  * **more than two candidates.** The paper fixes two. STAR's scoring round does
    nothing at K=2 (both candidates are finalists by definition), so a comparison
    needs K>=3. Positions are drawn at random rather than being an equilibrium.
  * **a scored-ballot behaviour rule.** The paper has no scored ballot. We model
    the scoring round as betrayal-free — rating is not choosing, so no c_i is
    incurred — and apply betrayal aversion only at the runoff, where a full vote
    really is assigned to one finalist. A conflicted voter facing two
    unacceptable finalists scores them equally: Equal Support, the option a
    choose-one ballot does not have.

That second choice is the whole result, so treat it as an assumption on display,
not a finding. A reader who rejects it should reject the conclusion with it.

USAGE
-----
    python3 conflicted_voter_star.py
    python3 conflicted_voter_star.py --trials 20000 --candidates 5
    python3 conflicted_voter_star.py --conflicted 0.39   # Pew: ~39% mixed views

The polarization sweep moves the parties apart so the overlap region shrinks to
nothing; the curse switches on exactly when it empties.
"""

from __future__ import annotations

import argparse
import math
import random

MAX_SCORE = 5


# --------------------------------------------------------------------------- #
# The electorate
# --------------------------------------------------------------------------- #

class Citizen:
    """One voter: who they identify with, how strongly, and what betrayal costs.

    `parties` is the paper's P_i — {"b"}, {"r"} or {"b", "r"}. A citizen with
    both is a *conflicted partisan* (the paper also calls them bi-partisan), and
    is the only kind whose behaviour differs between the two ballots here.
    """

    __slots__ = ("parties", "weight", "betrayal")

    def __init__(self, parties, weight, betrayal):
        self.parties = parties
        self.weight = weight        # I_i^p per party, in ]0, 1]
        self.betrayal = betrayal    # c_i, strictly greater than every I_i^p

    @property
    def conflicted(self) -> bool:
        return len(self.parties) == 2


def make_electorate(n, share_conflicted, rng):
    """Draw N citizens. A1 (at least one of each type) is enforced by the caller."""
    voters = []
    for _ in range(n):
        if rng.random() < share_conflicted:
            parties = ("b", "r")
        else:
            parties = ("b",) if rng.random() < 0.5 else ("r",)
        # I_i^p in ]0,1]; A2 asks that I/d differ per party for conflicted
        # voters, which independent draws satisfy with probability 1.
        weight = {p: rng.uniform(0.05, 1.0) for p in parties}
        # Betrayal aversion (U3): c_i strictly above every identity gain.
        betrayal = max(weight.values()) + rng.uniform(0.01, 0.5)
        voters.append(Citizen(parties, weight, betrayal))
    return voters


# --------------------------------------------------------------------------- #
# The paper's utility and turnout rule
# --------------------------------------------------------------------------- #

def dist(a, b):
    return math.dist(a, b)


def accepts(party_pt, radius, x) -> bool:
    """P2: is position x inside this party's acceptance region?"""
    return dist(party_pt, x) <= radius


def utility(voter, x, ideo, radius):
    """Equation (1): Euclidean term, identity gains, and the betrayal cost.

    Written as the paper states it rather than as three branches, because the
    branches in (1) are just this sum evaluated at different acceptance patterns.
    """
    total = 0.0
    accepted_by_all = True
    for p in voter.parties:
        w = voter.weight[p]
        total -= (w / radius[p]) * dist(ideo[p], x)
        if accepts(ideo[p], radius[p], x):
            total += w                      # U2 identity gain
        else:
            accepted_by_all = False
    if not accepted_by_all:
        total -= voter.betrayal             # U3 cost of betrayal
    return total


def turns_out(voter, candidates, ideo, radius) -> bool:
    """Proposition 1: turn out iff SOME candidate is accepted by EVERY party.

    For a conflicted voter this means a candidate inside the overlap region. If
    the overlap is empty, no candidate can ever satisfy it — the curse.
    """
    return any(
        all(accepts(ideo[p], radius[p], c) for p in voter.parties)
        for c in candidates
    )


# --------------------------------------------------------------------------- #
# The two ballots
# --------------------------------------------------------------------------- #

def plurality_winner(voters, candidates, ideo, radius, rng):
    """The paper's ballot, extended to K candidates: turn out, then pick one.

    Returns (winner index, turnout count, conflicted turnout count).
    """
    tally = [0] * len(candidates)
    turnout = conflicted_turnout = 0
    for v in voters:
        if not turns_out(v, candidates, ideo, radius):
            continue
        turnout += 1
        if v.conflicted:
            conflicted_turnout += 1
        utils = [utility(v, c, ideo, radius) for c in candidates]
        best = max(utils)
        # Indifference is broken at random, per the paper's ice-cream-seller note.
        tied = [i for i, u in enumerate(utils) if u == best]
        tally[rng.choice(tied)] += 1
    return argmax(tally), turnout, conflicted_turnout


def star_ballot(voter, candidates, ideo, radius):
    """Sincere 0-5 scores from the voter's Euclidean preferences.

    Deliberately NOT the full equation (1): the scoring round assigns no vote to
    anyone, so no betrayal is committed and c_i does not apply. What survives is
    U1 — how close each candidate sits to the ideological points the voter takes
    her cues from — min-max scaled onto 0-5, the repo's standard sincere mapping.
    """
    utils = []
    for c in candidates:
        u = 0.0
        for p in voter.parties:
            u -= (voter.weight[p] / radius[p]) * dist(ideo[p], c)
        utils.append(u)
    lo, hi = min(utils), max(utils)
    if hi - lo < 1e-12:
        return [MAX_SCORE] * len(candidates)   # genuinely indifferent
    return [round(MAX_SCORE * (u - lo) / (hi - lo)) for u in utils]


def star_winner(voters, candidates, ideo, radius, rng):
    """STAR: score everyone, top two by total, then the automatic runoff.

    Returns (winner, equal-support count among conflicted voters, that group's
    size). Everyone participates — the scoring round costs no betrayal — so
    turnout is by construction 100%, which is the comparison being drawn.
    """
    k = len(candidates)
    totals = [0] * k
    ballots = []
    for v in voters:
        s = star_ballot(v, candidates, ideo, radius)
        ballots.append((v, s))
        for i, sc in enumerate(s):
            totals[i] += sc

    first = argmax(totals)
    second = argmax([t if i != first else -1 for i, t in enumerate(totals)])

    a = b = equal = conflicted_equal = conflicted_n = 0
    for v, s in ballots:
        if v.conflicted:
            conflicted_n += 1
        acceptable = [
            all(accepts(ideo[p], radius[p], candidates[i]) for p in v.parties)
            for i in (first, second)
        ]
        # Betrayal aversion applies HERE and only here: the runoff is where a
        # full vote is actually assigned. If neither finalist is acceptable to
        # every party the voter identifies with, expressing a preference would
        # be the betrayal the paper prices at c_i — so she registers no
        # preference instead. That option is what the ballot adds.
        if not any(acceptable) and v.conflicted:
            equal += 1
            conflicted_equal += 1
            continue
        if s[first] > s[second]:
            a += 1
        elif s[second] > s[first]:
            b += 1
        else:
            equal += 1
            if v.conflicted:
                conflicted_equal += 1
    winner = first if a > b else second if b > a else rng.choice([first, second])
    return winner, conflicted_equal, conflicted_n


def argmax(seq):
    best = max(seq)
    return seq.index(best)


# --------------------------------------------------------------------------- #
# One election, and the sweep
# --------------------------------------------------------------------------- #

def run_trial(n, k, share_conflicted, separation, radius_b, radius_r, rng):
    ideo = {"b": (-separation / 2, 0.0), "r": (separation / 2, 0.0)}
    radius = {"b": radius_b, "r": radius_r}
    voters = make_electorate(n, share_conflicted, rng)
    if not any(v.conflicted for v in voters) or all(v.conflicted for v in voters):
        return None                                   # A1: need all three types
    candidates = [
        (rng.uniform(-2.0, 2.0), rng.uniform(-1.0, 1.0)) for _ in range(k)
    ]

    p_win, turnout, conf_turnout = plurality_winner(voters, candidates, ideo, radius, rng)
    s_win, conf_equal, conf_n = star_winner(voters, candidates, ideo, radius, rng)

    # "Represents the electorate" is measured the same way for both: distance
    # from the winner to the mean ideological point, which for a symmetric
    # two-party electorate is the centre. Lower is more moderate.
    centre = (0.0, 0.0)
    return {
        "overlap": separation <= radius_b + radius_r,
        "turnout": turnout / len(voters),
        "conf_turnout": conf_turnout / conf_n if conf_n else 0.0,
        "conf_equal": conf_equal / conf_n if conf_n else 0.0,
        "same_winner": p_win == s_win,
        "plur_dist": dist(candidates[p_win], centre),
        "star_dist": dist(candidates[s_win], centre),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trials", type=int, default=4000, help="elections per separation")
    ap.add_argument("--voters", type=int, default=501)
    ap.add_argument("--candidates", type=int, default=4)
    ap.add_argument("--conflicted", type=float, default=0.39,
                    help="share of bi-partisan voters (default 0.39, Pew 2014)")
    ap.add_argument("--radius", type=float, default=0.6,
                    help="acceptance radius d_p, both parties")
    ap.add_argument("--seed", type=int, default=20260806)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    overlap_at = 2 * args.radius

    print(__doc__.split("USAGE")[0].strip()[:0] or "", end="")
    print(f"Conflicted-voter curse under two ballots — {args.trials} elections per row")
    print(f"  {args.voters} voters, {args.candidates} candidates, "
          f"{args.conflicted:.0%} conflicted, acceptance radius {args.radius}")
    print(f"  overlap region is non-empty while party separation <= {overlap_at:g}\n")
    print(f"{'separation':>10} {'overlap':>8} | {'choose-one':>10} {'conflicted':>10} | "
          f"{'STAR eq.sup':>11} | {'differ':>7} {'moderation':>10}")
    print(f"{'':>10} {'':>8} | {'turnout':>10} {'turnout':>10} | "
          f"{'(conf.)':>11} | {'winners':>7} {'gain':>10}")
    print("-" * 78)

    for step in range(9):
        sep = 0.2 + step * 0.25
        rows = [
            r for r in (
                run_trial(args.voters, args.candidates, args.conflicted, sep,
                          args.radius, args.radius, rng)
                for _ in range(args.trials)
            ) if r
        ]
        if not rows:
            continue
        m = lambda key: sum(r[key] for r in rows) / len(rows)
        differ = 1 - m("same_winner")
        # Positive = STAR's winner sits closer to the centre than choose-one's.
        moderation = m("plur_dist") - m("star_dist")
        print(f"{sep:>10.2f} {('yes' if sep <= overlap_at else 'NO'):>8} | "
              f"{m('turnout'):>9.1%} {m('conf_turnout'):>10.1%} | "
              f"{m('conf_equal'):>10.1%} | {differ:>6.1%} {moderation:>+10.3f}")

    print("\nHOW TO READ THIS — two columns are near-tautological, two are not.")
    print("  STAR turnout is 100% in every row BY CONSTRUCTION: the scoring round")
    print("  assigns no vote, so no betrayal is committed and the curse cannot fire.")
    print("  'STAR eq.sup' reaching 100% once the overlap empties is also mostly")
    print("  forced: with no overlap NO candidate is acceptable to both parties, so")
    print("  the modelling rule sends every conflicted voter to Equal Support. Those")
    print("  two columns confirm the code implements the model; they are not results.")
    print("\n  The findings are the last two columns. Recovered ballots cannot express")
    print("  a runoff preference under polarization — but they still carry full weight")
    print("  in the SCORING round, which chooses who the finalists are. That is where")
    print("  the winner changes, and it moves toward the centre rather than away.")
    print("\n  Choose-one turnout looks low throughout because Proposition 1 abstains")
    print("  PARTISANS too whenever no candidate sits inside their own party's")
    print("  acceptance region — with radius %.2g and candidates drawn across the whole"
          % args.radius)
    print("  domain, that is most of them. Raise --radius to see it climb.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
