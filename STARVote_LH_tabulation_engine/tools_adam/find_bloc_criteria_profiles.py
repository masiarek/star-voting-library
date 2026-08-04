#!/usr/bin/env python3
"""find_bloc_criteria_profiles.py — search for Bloc STAR profiles that break a criterion.

Stdlib only; no venv needed (`python3 find_bloc_criteria_profiles.py --help`).

WHY A SECOND IMPLEMENTATION. This file re-implements Bloc STAR (elect / remove /
re-run) in ~40 lines so the search can run millions of tabulations without engine
overhead, and so a hit is not confirmed by the same code that found it. Every hit
is meant to be re-run through the LH engine before anyone believes it — that is
how the four profiles below were checked, and BetterVoting then agreed with LH on
all of them (BV2264-BV2268).

STRICT MODE. A profile is discarded the moment ANY round needs a tie-break rung,
in the base profile and in the modified one. So a hit never depends on a lot
order, and the resulting case can be published without pinning `lot_numbers`.

The four searches, and what they returned (2026-08-04):

  participation  HITS. A voter joins, votes honestly, and their own ballot rates
                 the resulting council LOWER than the one they would have got by
                 staying home.               -> 02_STAR_Bloc/03_Criteria/participation/
  seat-order     HITS. Seat 2's winner beats seat 1's winner head to head (in the
                 shipped case, beats everyone).
                                             -> 02_STAR_Bloc/03_Criteria/seat_order/
  spoiler        HITS. An added candidate wins no seat and changes which
                 candidates do.        -> 02_STAR_Bloc/03_Criteria/committee_spoiler/
  monotonicity   NO HITS in ~377,000 tie-free profiles across 8 shapes (3-6
                 candidates, 7-11 voters, 2-3 seats), raising a seated candidate
                 by +1 on one ballot, to 5 on one ballot, and by +1 on every
                 subset of up to 5 ballots. See the argument below — for two
                 seats it looks provable, not merely unobserved.

REPRODUCING THE SHIPPED PROFILES (the ballots are the letter-named originals of
the BV cases; the candidates were renamed on promotion):

    python3 find_bloc_criteria_profiles.py participation -v 6 --seed 2 --hits 1
    python3 find_bloc_criteria_profiles.py seat-order     --seed 3  --hits 2  # it is HIT 2
    python3 find_bloc_criteria_profiles.py spoiler -c 3   --seed 11 --hits 1

The seat-order case shipped as hit 2 because hit 1 separates the two winners by
only 2-1 with four voters at Equal Support; hit 2 has every voter expressing a
preference and the winner of seat 2 beating ALL three rivals, which is the
stronger teaching profile.

WHY MONOTONICITY LOOKS SAFE (two seats). Say w wins seat 2, and raise w. Raising w
can only push w UP the scoring round, so the only way it disturbs seat 1 is by
entering the finalist pair — evicting the OTHER finalist, never the score leader X.
The new seat-1 runoff is therefore X vs w. But w won seat 2 in the original, and X
(the overall score leader) is the top scorer of any pool containing X, so X was
w's seat-2 opponent and w beat X head to head. Raising w cannot reverse that. So w
wins the new seat-1 runoff and keeps a seat. Extending this to N seats — where the
raise can disturb any earlier seat, not just the first — is the open half.
"""
import argparse
import itertools
import random

MAX_SCORE = 5


# ---------------------------------------------------------------- the method
def scores(ballots, cands):
    return {c: sum(b[c] for b in ballots) for c in cands}


def prefer(ballots, x, y):
    """(voters preferring x, preferring y, expressing no preference)."""
    fx = sum(1 for b in ballots if b[x] > b[y])
    fy = sum(1 for b in ballots if b[y] > b[x])
    return fx, fy, len(ballots) - fx - fy


def star_round(ballots, cands):
    """One STAR round. Returns (winner, needed_a_tiebreak)."""
    if len(cands) == 1:
        return cands[0], False
    sc = scores(ballots, cands)
    order = sorted(cands, key=lambda c: -sc[c])
    if len(order) > 2 and sc[order[1]] == sc[order[2]]:
        return None, True                      # tie for the last finalist slot
    a, b = order[0], order[1]
    fa, fb, _ = prefer(ballots, a, b)
    if fa == fb:
        return None, True                      # tied runoff
    return (a if fa > fb else b), False


def bloc_star(ballots, cands, seats):
    """Winners in seat order, or None if any round needed a tie-break."""
    remaining, winners = list(cands), []
    for _ in range(seats):
        w, tied = star_round(ballots, remaining)
        if tied:
            return None
        winners.append(w)
        remaining.remove(w)
    return winners


def rand_ballot(cands, rng):
    return {c: rng.randint(0, MAX_SCORE) for c in cands}


def names(n):
    return [chr(ord("A") + i) for i in range(n)]


def show(ballots, cands):
    print("    " + ",".join(cands))
    for b in ballots:
        print("    " + ",".join(str(b[c]) for c in cands))


# ---------------------------------------------------------------- searches
def search_participation(trials, ncand, nvoters, seats, rng):
    """A joiner's own ballot rates the council they voted for below the one they'd
    have got by staying home."""
    cands = names(ncand)
    for _ in range(trials):
        ballots = [rand_ballot(cands, rng) for _ in range(nvoters)]
        base = bloc_star(ballots, cands, seats)
        if base is None:
            continue
        joiner = rand_ballot(cands, rng)
        after = bloc_star(ballots + [joiner], cands, seats)
        if after is None:
            continue
        before_value = sum(joiner[c] for c in base)
        after_value = sum(joiner[c] for c in after)
        if after_value < before_value:
            yield {"ballots": ballots + [joiner], "cands": cands, "base": base,
                   "after": after, "note": f"joiner's council {after_value} < "
                                           f"no-show council {before_value}"}


def search_seat_order(trials, ncand, nvoters, seats, rng):
    """Seat 2's winner beats seat 1's winner head to head."""
    cands = names(ncand)
    for _ in range(trials):
        ballots = [rand_ballot(cands, rng) for _ in range(nvoters)]
        res = bloc_star(ballots, cands, seats)
        if res is None:
            continue
        f2, f1, eq = prefer(ballots, res[1], res[0])
        if f2 > f1:
            yield {"ballots": ballots, "cands": cands, "base": res, "after": None,
                   "note": f"{res[1]} over {res[0]} {f2}-{f1} (equal support {eq})"}


def search_spoiler(trials, ncand, nvoters, seats, rng):
    """An extra candidate wins no seat and changes who does."""
    cands = names(ncand)
    extra = chr(ord("A") + ncand)
    for _ in range(trials):
        ballots = [rand_ballot(cands, rng) for _ in range(nvoters)]
        base = bloc_star(ballots, cands, seats)
        if base is None:
            continue
        big = [dict(b) for b in ballots]
        for b in big:
            b[extra] = rng.randint(0, MAX_SCORE)
        after = bloc_star(big, cands + [extra], seats)
        if after is None or extra in after:
            continue
        if set(after) != set(base):
            yield {"ballots": big, "cands": cands + [extra], "base": base,
                   "after": after, "note": f"{extra} wins nothing and still changes "
                                           f"the council"}


def search_monotonicity(trials, ncand, nvoters, seats, rng, max_ballots=3):
    """Raise a seated candidate (+1 on up to max_ballots ballots) and see if they
    lose their seat. Returned nothing so far — see the module docstring."""
    cands = names(ncand)
    for _ in range(trials):
        ballots = [rand_ballot(cands, rng) for _ in range(nvoters)]
        base = bloc_star(ballots, cands, seats)
        if base is None:
            continue
        for w in base:
            raisable = [i for i, b in enumerate(ballots) if b[w] < MAX_SCORE]
            for k in range(1, min(max_ballots, len(raisable)) + 1):
                for combo in itertools.combinations(raisable, k):
                    mod = [dict(b) for b in ballots]
                    for i in combo:
                        mod[i][w] += 1
                    after = bloc_star(mod, cands, seats)
                    if after is None or w in after:
                        continue
                    yield {"ballots": mod, "cands": cands, "base": base,
                           "after": after,
                           "note": f"raising {w} on ballot(s) "
                                   f"{[i + 1 for i in combo]} cost {w} a seat"}


SEARCHES = {
    "participation": search_participation,
    "seat-order": search_seat_order,
    "spoiler": search_spoiler,
    "monotonicity": search_monotonicity,
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("search", choices=sorted(SEARCHES), help="which criterion to probe")
    ap.add_argument("-c", "--candidates", type=int, default=4)
    ap.add_argument("-v", "--voters", type=int, default=7)
    ap.add_argument("-s", "--seats", type=int, default=2)
    ap.add_argument("-n", "--trials", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--hits", type=int, default=3, help="stop after this many")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    fn = SEARCHES[args.search]
    print(f"{args.search}: {args.trials} profiles, {args.candidates} candidates, "
          f"{args.voters} voters, {args.seats} seats, seed {args.seed}")
    found = 0
    for hit in fn(args.trials, args.candidates, args.voters, args.seats, rng):
        found += 1
        print(f"\n--- hit {found}: {hit['note']}")
        print(f"    council: {hit['base']}"
              + (f"  ->  {hit['after']}" if hit["after"] else ""))
        show(hit["ballots"], hit["cands"])
        if found >= args.hits:
            break
    if not found:
        if args.search == "monotonicity":
            print("no hits — which IS the result here; see the module docstring for "
                  "why two seats look provably safe")
        else:
            print("no hits at this shape — try other -c/-v/-s or another --seed; the "
                  "docstring records the shapes that hit")


if __name__ == "__main__":
    main()
