#!/usr/bin/env python3
"""
resignation_check.py — replay the resignation-monotonicity witnesses.

A winner resigns after the election. You re-run the count on the remaining
candidates to fill the empty seat. **Resignation monotonicity** (Oh & Peters,
*Candidate Resignation Monotonicity in Approval-Based Committee Elections*,
arXiv:2608.06156, 6 Aug 2026) demands the obvious thing: every winner who did
NOT resign must still be a winner.

Their Theorem 3.1 says plain Approval (AV) satisfies it and that among Thiele
and sequential Thiele methods AV is the ONLY one; their Theorem 3.4 says no rule
satisfying justified representation can satisfy it at all. This module encodes
the paper's own counterexamples and replays them through
`abcvoting` — Lackner's peer-reviewed implementation — so the claims on
`04_Approval/03_Criteria/resignation_monotonicity.md` are computed here rather
than transcribed.

It then asks the question the paper does not: **do this repo's SCORE-based
proportional rules fail the same way?** Allocated Score (the STAR-PR rule
BetterVoting runs), Sequentially Spent Score and Reweighted Range Voting are not
ABC rules and are not in the paper. Approval ballots are score ballots that only
use 0 and 5, so the paper's domain sits inside theirs, and the question is
well-posed. All three fail; Bloc STAR does not, on any profile searched.

What this can and cannot establish
----------------------------------
- A FAILURE is demonstrated: run the witness, watch a seated winner get evicted.
  Proof by counterexample, and complete.
- A PASS is not demonstrated and cannot be. "No profile anywhere violates this"
  is a universal claim no finite replay settles. AV's pass is CITED to the
  paper's Theorem 3.1. **Bloc STAR's pass is cited to nothing** — it is an
  exhaustive search over every 4-candidate profile up to 6 voters that found no
  violation, which is evidence and is not a theorem. `--search` extends it.

Resoluteness — the trap this module exists to avoid
---------------------------------------------------
The score rules are SEQUENTIAL, so a tie inside the count is settled by a
tie-breaking order. Run one of them once and a survivor may look evicted when a
different lot would have kept them: on the paper's own Example 3.2, all three
score rules "fail" under the engine's default tie-break and are perfectly
monotone once you enumerate the alternatives. So every score verdict here is
taken over ALL tie-breaking orders (`starvote.predefined_permutation_tiebreaker`
over every permutation of the candidates), and a violation is only reported when
the survivors appear in NO reachable committee. The flagship witnesses are
stronger still: the rule has exactly one reachable committee before and after.

Usage
-----
    python 06_Other/abcvoting_tabulation_engine/resignation_check.py
    python 06_Other/abcvoting_tabulation_engine/resignation_check.py --verbose
    python 06_Other/abcvoting_tabulation_engine/resignation_check.py --search 2000
    python 06_Other/abcvoting_tabulation_engine/resignation_check.py --sweep-bloc

Exit status is non-zero if any witness fails to reproduce, so it can be gated by
a test (`tests/test_resignation_monotonicity.py`).
"""
from __future__ import annotations

import argparse
import itertools
import random
import re
import sys

try:
    from abcvoting import abcrules
    from abcvoting.preferences import Profile
except ImportError:  # pragma: no cover
    abcrules = None

import starvote

MAX_SCORE = 5


# --------------------------------------------------------------------------
# profiles — the paper labels candidates c1, c2, ...; we keep its labels
# --------------------------------------------------------------------------

def fmt_committee(w):
    return "{" + ",".join(sorted(w, key=_key)) + "}"


def _key(name):
    """Natural sort: c2 before c10, but plain names stay alphabetical."""
    return tuple(int(t) if t.isdigit() else t.lower()
                 for t in re.split(r"(\d+)", name))


def fmt_profile(voters):
    return "  ".join(
        "v%d:{%s}" % (i + 1, ",".join(sorted(v, key=_key)))
        for i, v in enumerate(voters)
    )


def resign(voters, cands, who):
    """The instance E - {who}: strike the resigner from every ballot."""
    return [v - {who} for v in voters], [c for c in cands if c != who]


# --------------------------------------------------------------------------
# ABC rules, via abcvoting
# --------------------------------------------------------------------------

def abc_outcomes(rule_id, voters, cands, k):
    """Every winning committee, as a set of frozensets of candidate names."""
    index = {c: i for i, c in enumerate(cands)}
    profile = Profile(len(cands), cand_names=list(cands))
    for v in voters:
        profile.add_voter(sorted(index[c] for c in v))
    try:
        out = abcrules.compute(rule_id, profile, committeesize=k, resolute=False)
    except NotImplementedError:
        out = abcrules.compute(rule_id, profile, committeesize=k, resolute=True)
    return {frozenset(cands[i] for i in c) for c in out}


# --------------------------------------------------------------------------
# score rules, via starvote — always over EVERY tie-breaking order
# --------------------------------------------------------------------------

SCORE_RULES = {
    "allocated": ("Allocated Score (STAR-PR)", starvote.allocated),
    "sss":       ("Sequentially Spent Score",  starvote.sss),
    "rrv":       ("Reweighted Range Voting",   starvote.rrv),
    "bloc":      ("Bloc STAR",                 starvote.bloc),
}


def score_outcomes(rule, voters, cands, k):
    """Every committee reachable under some candidate tie-breaking order."""
    ballots = [{c: (MAX_SCORE if c in v else 0) for c in cands} for v in voters]
    out = set()
    for perm in itertools.permutations(cands):
        tb = starvote.predefined_permutation_tiebreaker(list(perm))
        try:
            w = starvote.election(rule, ballots, seats=k,
                                  maximum_score=MAX_SCORE, tiebreaker=tb)
        except Exception:                      # pragma: no cover - defensive
            continue
        out.add(frozenset(w if isinstance(w, (list, tuple, set)) else [w]))
    return out


def score_outcomes_default(rule, voters, cands, k):
    """One committee, under the engine's own default tie-break."""
    ballots = [{c: (MAX_SCORE if c in v else 0) for c in cands} for v in voters]
    w = starvote.election(rule, ballots, seats=k, maximum_score=MAX_SCORE)
    return frozenset(w if isinstance(w, (list, tuple, set)) else [w])


def survivors_retained(outcomes_after, winners, resigner):
    """The axiom: some post-resignation committee keeps every other winner."""
    keep = set(winners) - {resigner}
    return any(keep <= set(a) for a in outcomes_after)


# --------------------------------------------------------------------------
# the witnesses
# --------------------------------------------------------------------------

# Oh & Peters, Example 3.2 (n=5, k=2). Five named rules uniquely elect {c1,c2};
# c1 resigns and they uniquely elect {c3,c4}, so c2 is evicted.
EX_3_2 = dict(
    label="Example 3.2",
    cands=["c1", "c2", "c3", "c4"],
    voters=[{"c1"}, {"c1", "c3"}, {"c1", "c4"}, {"c2", "c3"}, {"c2", "c4"}],
    k=2,
    rules=["pav", "cc", "monroe", "leximaxphragmen", "minimaxav"],
    before={"c1", "c2"},
    resigner="c1",
    after={"c3", "c4"},
)

# Oh & Peters, Example 3.3 (n=5, k=5). PAV, seq-Phragmen and MES uniquely elect
# {c1,c4,c5,c6,c7}. After c1 resigns, JR demands a seat for c2 AND one for c3
# and only one is free, so none of them can return all of c4..c7.
EX_3_3 = dict(
    label="Example 3.3",
    cands=["c1", "c2", "c3", "c4", "c5", "c6", "c7"],
    voters=[{"c1", "c2"}, {"c1", "c3"},
            {"c4", "c5", "c6", "c7"}, {"c4", "c5", "c6", "c7"},
            {"c4", "c5", "c6", "c7"}],
    k=5,
    rules=["pav", "seqphragmen", "equal-shares"],
    before={"c1", "c4", "c5", "c6", "c7"},
    resigner="c1",
    after=None,          # many committees; the claim is that none retains c4..c7
)

# Oh & Peters, Proposition 3.5 (n=4, k=2). Both {c1,c2} and {c3,c4} satisfy
# perfect representation; resigning from either leaves only the other.
PROP_3_5 = dict(
    label="Proposition 3.5",
    cands=["c1", "c2", "c3", "c4"],
    voters=[{"c1", "c3"}, {"c1", "c4"}, {"c2", "c3"}, {"c2", "c4"}],
    k=2,
    expected_before=[{"c1", "c2"}, {"c3", "c4"}],
    resigner="c1",
    expected_after=[{"c3", "c4"}],
)

# AV is the paper's positive case (Theorem 3.1): on Example 3.3 it elects the
# same committee as PAV and then keeps all four survivors.
AV_CONTROL = dict(label="Example 3.3, counted by AV", rules=["av"], **{
    k: EX_3_3[k] for k in ("cands", "voters", "k", "resigner")})

# This repo's own witnesses for the score rules. Found by exhaustive search over
# every approval profile of the stated size; each has ONE reachable committee
# before and after, so no tie-breaking rescues it.
SCORE_WITNESSES = [
    dict(
        label="Allocated Score loses the lone voter's seat",
        rule="allocated",
        cands=["Ana", "Bruno", "Cleo", "Dev"],
        voters=[{"Ana"}, {"Bruno", "Cleo"}, {"Bruno", "Cleo"},
                {"Bruno", "Dev"}, {"Bruno", "Dev"}],
        k=2, before={"Ana", "Bruno"}, resigner="Bruno", after={"Cleo", "Dev"},
        case="04_Approval/03_Criteria/cases/resign_star_pr_seated_c4_b5.yaml",
    ),
    dict(
        label="Sequentially Spent Score, same profile",
        rule="sss",
        cands=["Ana", "Bruno", "Cleo", "Dev"],
        voters=[{"Ana"}, {"Bruno", "Cleo"}, {"Bruno", "Cleo"},
                {"Bruno", "Dev"}, {"Bruno", "Dev"}],
        k=2, before={"Ana", "Bruno"}, resigner="Bruno", after={"Cleo", "Dev"},
        case=None,
    ),
    dict(
        label="Reweighted Range Voting evicts a one-supporter winner",
        rule="rrv",
        cands=["Fern", "Gus", "Hana", "Ivan", "Juno"],
        voters=[{"Fern"}, {"Gus"}, {"Hana", "Ivan"}, {"Hana", "Juno"},
                {"Fern", "Hana", "Ivan", "Juno"}],
        k=3, before={"Fern", "Gus", "Hana"}, resigner="Hana",
        after={"Fern", "Ivan", "Juno"},
        case="04_Approval/03_Criteria/cases/resign_rrv_seated_c5_b5.yaml",
    ),
    # The paper's own Example 3.3, re-counted as scores. RRV agrees with PAV on
    # the committee and then fails the same way; the other three do not, which is
    # worth printing rather than hiding.
    dict(
        label="Reweighted Range Voting on the paper's Example 3.3",
        rule="rrv",
        cands=EX_3_3["cands"], voters=EX_3_3["voters"], k=5,
        before={"c1", "c4", "c5", "c6", "c7"}, resigner="c1", after=None,
        case=None,
    ),
]


def pr_committees(voters, cands, k):
    """Every size-k committee satisfying PERFECT REPRESENTATION.

    PR asks for a partition of the n voters into k groups of exactly n/k, each
    assigned a distinct committee member every member of the group approves.
    Computed directly rather than through a rule, because Proposition 3.5 is a
    claim about the axiom itself: no rule that always outputs a PR committee can
    be resignation monotone.
    """
    n = len(voters)
    if n % k:
        return set()
    size = n // k
    out = set()
    for W in itertools.combinations(sorted(cands, key=_key), k):
        for assign in itertools.permutations(range(n)):
            groups = [assign[i * size:(i + 1) * size] for i in range(k)]
            if all(all(W[g] in voters[v] for v in grp)
                   for g, grp in enumerate(groups)):
                out.add(frozenset(W))
                break
    return out


# --------------------------------------------------------------------------
# checking
# --------------------------------------------------------------------------

def check_pr(w, verbose=False):
    """Replay Proposition 3.5: the PR committees before and after a resignation."""
    lines, ok = [], True
    lines.append(f"\n{w['label']} — n={len(w['voters'])}, "
                 f"m={len(w['cands'])}, k={w['k']}  (perfect representation)")
    lines.append(f"  {fmt_profile(w['voters'])}")
    before = pr_committees(w["voters"], w["cands"], w["k"])
    after = pr_committees(*resign(w["voters"], w["cands"], w["resigner"]), w["k"])
    want_b = {frozenset(c) for c in w["expected_before"]}
    want_a = {frozenset(c) for c in w["expected_after"]}
    lines.append(f"  PR committees:            "
                 f"{sorted(map(fmt_committee, before), key=_key)}")
    lines.append(f"  after {w['resigner']} resigns:        "
                 f"{sorted(map(fmt_committee, after), key=_key)}")
    if before != want_b or after != want_a:
        ok = False
        lines.append("  MISMATCH against the paper")
    else:
        W = frozenset(w["expected_before"][0])
        held = survivors_retained(after, W, w["resigner"])
        lines.append(f"  {fmt_committee(W)} was PR; {w['resigner']} resigns; "
                     f"survivor {fmt_committee(W - {w['resigner']})}: "
                     + ("retained" if held else
                        "EVICTED — no PR committee keeps them"))
        if held:
            ok = False
    return ok, lines


def check_abc(w, verbose=False):
    """Replay one ABC witness. Returns (ok, [lines])."""
    lines, ok = [], True
    lines.append(f"\n{w['label']} — n={len(w['voters'])}, "
                 f"m={len(w['cands'])}, k={w['k']}")
    lines.append(f"  {fmt_profile(w['voters'])}")
    after_voters, after_cands = resign(w["voters"], w["cands"], w["resigner"])
    for rule_id in w["rules"]:
        before = abc_outcomes(rule_id, w["voters"], w["cands"], w["k"])
        after = abc_outcomes(rule_id, after_voters, after_cands, w["k"])
        if w.get("before") is not None:
            if before != {frozenset(w["before"])}:
                ok = False
                lines.append(f"  {rule_id:18s} MISMATCH before: "
                             f"{sorted(map(fmt_committee, before))} "
                             f"!= {{{fmt_committee(w['before'])}}}")
                continue
        if w.get("after") is not None and after != {frozenset(w["after"])}:
            ok = False
            lines.append(f"  {rule_id:18s} MISMATCH after: "
                         f"{sorted(map(fmt_committee, after))}")
            continue
        expect_fail = rule_id != "av"
        for W in sorted(before, key=lambda c: sorted(c, key=_key)):
            if w["resigner"] not in W:
                continue
            held = survivors_retained(after, W, w["resigner"])
            verdict = "retained" if held else "EVICTED"
            if held == expect_fail:
                ok = False
                verdict += "  <-- not what the paper claims"
            lines.append(
                f"  {rule_id:18s} {fmt_committee(W)} -> {w['resigner']} resigns"
                f" -> survivors {verdict}"
                + (f"   (reachable: "
                   f"{sorted(map(fmt_committee, after))})" if verbose else ""))
    return ok, lines


def check_score(w, verbose=False):
    """Replay one score witness over every tie-breaking order."""
    name, rule = SCORE_RULES[w["rule"]]
    lines, ok = [], True
    lines.append(f"\n{w['label']} — {name}, n={len(w['voters'])}, "
                 f"m={len(w['cands'])}, k={w['k']}")
    lines.append(f"  {fmt_profile(w['voters'])}")
    before = score_outcomes(rule, w["voters"], w["cands"], w["k"])
    after_voters, after_cands = resign(w["voters"], w["cands"], w["resigner"])
    after = score_outcomes(rule, after_voters, after_cands, w["k"])
    if w.get("before") is not None and before != {frozenset(w["before"])}:
        ok = False
        lines.append(f"  MISMATCH before: {sorted(map(fmt_committee, before))}")
        return ok, lines
    if w.get("after") is not None and after != {frozenset(w["after"])}:
        ok = False
        lines.append(f"  MISMATCH after: {sorted(map(fmt_committee, after))}")
        return ok, lines
    W = frozenset(w["before"])
    held = survivors_retained(after, W, w["resigner"])
    if held:
        ok = False
    lines.append(f"  before (all tie-breaks): "
                 f"{sorted(map(fmt_committee, before))}")
    lines.append(f"  {w['resigner']} resigns -> "
                 f"{sorted(map(fmt_committee, after))}")
    lines.append(f"  survivors {fmt_committee(W - {w['resigner']})}: "
                 + ("retained  <-- not a violation after all" if held
                    else "EVICTED under every tie-breaking order"))
    if w.get("case"):
        lines.append(f"  runnable case: {w['case']}")
    return ok, lines


def run_all(verbose=False):
    ok = True
    print("=" * 74)
    print("The paper's own witnesses, replayed through abcvoting")
    print("=" * 74)
    if abcrules is None:
        print("  abcvoting not installed - skipped (uv sync installs it)")
    else:
        for w in (EX_3_2, EX_3_3, AV_CONTROL):
            good, lines = check_abc(w, verbose)
            ok &= good
            print("\n".join(lines))
    good, lines = check_pr(PROP_3_5, verbose)
    ok &= good
    print("\n".join(lines))

    print("\n" + "=" * 74)
    print("This repo's question: the SCORE rules, over every tie-breaking order")
    print("=" * 74)
    for w in SCORE_WITNESSES:
        good, lines = check_score(w, verbose)
        ok &= good
        print("\n".join(lines))
    return ok


# --------------------------------------------------------------------------
# adversarial search — can only fail to refute a pass
# --------------------------------------------------------------------------

def search(rule_key, trials, seed=0, max_cand=6, max_voters=7, max_k=3):
    """Hunt for a violation on random small profiles, confirmed over all
    tie-breaks. Returns the first witness found, or None."""
    name, rule = SCORE_RULES[rule_key]
    rng = random.Random(seed)
    for i in range(trials):
        m = rng.randint(4, max_cand)
        n = rng.randint(4, max_voters)
        k = rng.randint(2, min(max_k, m - 1))
        cands = [f"c{j+1}" for j in range(m)]
        voters = [set(rng.sample(cands, rng.randint(1, max(1, m - 1))))
                  for _ in range(n)]
        if set().union(*voters) != set(cands):
            continue
        try:                        # cheap resolute pre-filter
            W = score_outcomes_default(rule, voters, cands, k)
        except Exception:           # pragma: no cover - defensive
            continue
        flagged = False
        for t in W:
            av, ac = resign(voters, cands, t)
            try:
                if not (set(W) - {t}) <= set(score_outcomes_default(rule, av, ac, k)):
                    flagged = True
                    break
            except Exception:       # pragma: no cover - defensive
                pass
        if not flagged:
            continue
        for W in score_outcomes(rule, voters, cands, k):     # confirm properly
            for t in W:
                av, ac = resign(voters, cands, t)
                if not survivors_retained(score_outcomes(rule, av, ac, k), W, t):
                    return dict(trial=i, cands=cands, voters=voters, k=k,
                                winners=W, resigner=t)
    return None


def sweep_bloc(max_voters=6):
    """Exhaustive over every 4-candidate profile up to `max_voters` voters."""
    name, rule = SCORE_RULES["bloc"]
    cands = ["c1", "c2", "c3", "c4"]
    pool = [frozenset(s) for r in range(1, 5)
            for s in itertools.combinations(cands, r)]
    total = flagged = violations = 0
    for n in range(4, max_voters + 1):
        for k in (2, 3):
            for combo in itertools.combinations_with_replacement(pool, n):
                voters = [set(s) for s in combo]
                if set().union(*voters) != set(cands):
                    continue
                total += 1
                W = score_outcomes_default(rule, voters, cands, k)
                if all((set(W) - {t}) <= set(score_outcomes_default(
                        rule, *resign(voters, cands, t), k)) for t in W):
                    continue
                flagged += 1
                for W in score_outcomes(rule, voters, cands, k):
                    for t in W:
                        if not survivors_retained(
                                score_outcomes(rule, *resign(voters, cands, t), k),
                                W, t):
                            violations += 1
                            print(f"  VIOLATION {fmt_profile(voters)} k={k} "
                                  f"W={fmt_committee(W)} {t} resigns")
    print(f"\nBloc STAR, exhaustive over 4 candidates and up to {max_voters} "
          f"voters:\n  {total} profiles, {flagged} flagged by the default "
          f"tie-break, {violations} surviving the full tie-break sweep.")
    return violations == 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--verbose", action="store_true",
                    help="print every reachable committee")
    ap.add_argument("--search", type=int, metavar="N", default=0,
                    help="hunt for fresh violations on N random profiles")
    ap.add_argument("--sweep-bloc", action="store_true",
                    help="exhaustive Bloc STAR sweep (4 candidates)")
    args = ap.parse_args(argv)

    if args.sweep_bloc:
        return 0 if sweep_bloc() else 1

    if args.search:
        rc = 0
        for key in SCORE_RULES:
            hit = search(key, args.search, seed=20260822)
            label = SCORE_RULES[key][0]
            if hit:
                print(f"\n{label}: violation after {hit['trial']} profiles")
                print(f"  {fmt_profile(hit['voters'])}  k={hit['k']}")
                print(f"  W={fmt_committee(hit['winners'])}, "
                      f"{hit['resigner']} resigns")
            else:
                print(f"\n{label}: no violation in {args.search} random "
                      f"profiles (a failure to refute, not a proof)")
        return rc

    ok = run_all(args.verbose)
    print("\n" + "=" * 74)
    print("all witnesses reproduced" if ok else "SOME WITNESS DID NOT REPRODUCE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
