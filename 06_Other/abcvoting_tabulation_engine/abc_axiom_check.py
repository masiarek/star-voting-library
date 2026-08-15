#!/usr/bin/env python3
"""
abc_axiom_check.py — verify Table 3.1 of Lackner & Skowron against `abcvoting`.

Chapter 3 of *Multi-Winner Voting with Approval Preferences* (Lackner & Skowron,
SpringerBriefs 2023, open access, doi:10.1007/978-3-031-09016-5) prints one grid —
Table 3.1 — giving, for thirteen approval-based committee (ABC) rules, whether each
satisfies Pareto efficiency, committee monotonicity, support monotonicity (with and
without additional voters), consistency, and inclusion-strategyproofness.

A grid of ticks and crosses is exactly the kind of claim this repo does not copy.
Every `x` in that table is a THEOREM WITH A WITNESS: a specific tiny approval
profile on which the rule visibly misbehaves. Appendix A prints those witnesses.
This module encodes them and REPLAYS each one through `abcvoting` — Lackner's own
peer-reviewed implementation — so the table on
`04_Approval/03_Criteria/README.md` is a computed result, not a transcription.

What it can and cannot establish
--------------------------------
- An `x` cell is DEMONSTRATED: run the witness, watch the axiom break. That is a
  proof by counterexample and it is complete.
- A tick is NOT demonstrated here and cannot be — "no profile anywhere violates
  this" is a universal claim, and no finite replay settles it. Ticks are CITED to
  the book's propositions. `--search` will hunt for a violation on random small
  profiles, which can only ever *fail to refute* a tick; that is worth something
  (it catches a mis-transcribed cell) and it is not a proof.

Usage
-----
    python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py
    python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --verbose
    python 06_Other/abcvoting_tabulation_engine/abc_axiom_check.py --search 2000

Exit status is non-zero if any witness fails to reproduce, so it can be gated by
a test (`tests/test_abc_axioms.py`).

Resoluteness convention
-----------------------
Several axioms are defined for RESOLUTE rules only (committee monotonicity,
inclusion-strategyproofness), and the book resolves ties "lexicographically
between committees, alphabetically between candidates". Two kinds of rule need
two different treatments, and conflating them silently changes answers:

- Rules defined by OPTIMISATION (AV, SAV, PAV, CC, Monroe, leximax-Phragmen,
  MAV) genuinely tie. We take all optimal committees and pick the
  lexicographically smallest — the book's stated convention, and independent of
  which solver `abcvoting` happens to use.
- Rules defined SEQUENTIALLY (seq-PAV, seq-CC, rev-seq-PAV, seq-Phragmen, Greedy
  Monroe, Method of Equal Shares) are resolute by construction once candidate
  ties are broken alphabetically, which is what `abcvoting`'s `resolute=True`
  does. Asking those for their irresolute set instead would return every
  committee reachable under SOME tiebreaking and lose the counterexample.
"""
from __future__ import annotations

import argparse
import itertools
import random
import sys

try:
    from abcvoting import abcrules
    from abcvoting.preferences import Profile
    ABCVOTING_AVAILABLE = True
except ImportError:  # pragma: no cover - guarded for bare-pip environments
    ABCVOTING_AVAILABLE = False

#: Table 3.1's thirteen rules, in the book's printed order, mapped to abcvoting ids.
TABLE_RULES = [
    ("AV", "av"),
    ("CC", "cc"),
    ("PAV", "pav"),
    ("seq-PAV", "seqpav"),
    ("seq-CC", "seqcc"),
    ("rev-seq-PAV", "revseqpav"),
    ("Monroe", "monroe"),
    ("Greedy Monroe", "greedy-monroe"),
    ("seq-Phragmen", "seqphragmen"),
    ("leximax-Phragmen", "leximaxphragmen"),
    ("Method of Eq. Shares", "equal-shares"),
    ("MAV", "minimaxav"),
    ("SAV", "sav"),
]

#: Rules whose definition is already sequential/resolute (see module docstring).
SEQUENTIAL_RULES = {
    "seqpav", "seqcc", "revseqpav", "seqphragmen",
    "greedy-monroe", "equal-shares", "maximin-support",
}


# --------------------------------------------------------------------------
# profiles
# --------------------------------------------------------------------------

def parse_profile(spec, num_cand=None):
    """Build an abcvoting Profile from a compact ``[(count, "abc"), ...]`` spec.

    Candidate letters are a, b, c, ... and map to indices 0, 1, 2, ...  The
    candidate set is the letters used, unless `num_cand` widens it (some of the
    book's examples name candidates that nobody approves).
    """
    letters = sorted({ch for _, approvals in spec for ch in approvals})
    n = max(num_cand or 0, (ord(letters[-1]) - ord("a") + 1) if letters else 0)
    names = [chr(ord("a") + i) for i in range(n)]
    profile = Profile(n, cand_names=names)
    for count, approvals in spec:
        voter = [ord(ch) - ord("a") for ch in approvals]
        for _ in range(count):
            profile.add_voter(voter)
    return profile, names


def fmt(committee, names):
    """Render a committee as ``{a,b,c}``."""
    return "{" + ",".join(names[c] for c in sorted(committee)) + "}"


def fmt_profile(spec):
    """Render a profile spec the way the book prints it."""
    return "  ".join(
        f"{count} x " + "{" + ",".join(approvals) + "}" for count, approvals in spec
    )


# --------------------------------------------------------------------------
# rule evaluation
# --------------------------------------------------------------------------

def winners(rule_id, profile, k):
    """All winning committees, as a list of sorted tuples.

    Greedy Monroe is the one rule with no irresolute form at all — it is
    *defined* by a tiebreaking order over voters, which is also why it is the
    single rule in Chapter 2 that fails anonymity. `abcvoting` refuses
    `resolute=False` for it rather than inventing a set, and so do we: its one
    committee is returned.
    """
    try:
        committees = abcrules.compute(rule_id, profile, committeesize=k, resolute=False)
    except NotImplementedError:
        committees = abcrules.compute(rule_id, profile, committeesize=k, resolute=True)
    return sorted(tuple(sorted(c)) for c in committees)


def resolute_winner(rule_id, profile, k):
    """The single winning committee under the book's tiebreaking convention."""
    if rule_id in SEQUENTIAL_RULES:
        committees = abcrules.compute(rule_id, profile, committeesize=k, resolute=True)
        return tuple(sorted(next(iter(committees))))
    return min(winners(rule_id, profile, k))


# --------------------------------------------------------------------------
# the axioms (Definitions 3.1-3.7)
# --------------------------------------------------------------------------

def dominates(w1, w2, profile):
    """Definition 3.1: w1 dominates w2 (weakly better for all, strictly for one)."""
    strict = False
    for voter in profile:
        a, b = len(set(voter.approved) & set(w1)), len(set(voter.approved) & set(w2))
        if a < b:
            return False
        if a > b:
            strict = True
    return strict


def _strict_gainers(w1, w2, profile):
    """How many voters are STRICTLY better off under w1 than under w2."""
    return sum(1 for voter in profile
               if len(set(voter.approved) & set(w1)) > len(set(voter.approved) & set(w2)))


def pareto_violation(rule_id, profile, k):
    """Return (winning, dominator) if the rule outputs a dominated committee.

    A dominated committee usually has SEVERAL dominators, and they are not
    equally instructive: on the book's CC witness both {a,c} and {c,d} dominate
    {a,b}, but only {c,d} makes *every* voter better off, which is the point
    being made. So report the dominator that leaves the most voters strictly
    better off (ties broken lexicographically, to stay deterministic).
    """
    all_committees = list(itertools.combinations(range(profile.num_cand), k))
    for w in winners(rule_id, profile, k):
        doms = [c for c in all_committees if dominates(c, w, profile)]
        if doms:
            return w, max(doms, key=lambda c: (_strict_gainers(c, w, profile),
                                               tuple(-x for x in c)))
    return None


def committee_monotonicity_violation(rule_id, profile, k):
    """Definition 3.2: the size-k winner must be a subset of the size-(k+1) winner."""
    small = resolute_winner(rule_id, profile, k)
    large = resolute_winner(rule_id, profile, k + 1)
    return None if set(small) <= set(large) else (small, large)


def _profile_plus_voter(spec, approvals, num_cand=None):
    return parse_profile(spec + [(1, approvals)], num_cand=num_cand)


def _profile_voter_adds(spec, voter_index, approvals, num_cand=None):
    """Expand a weighted spec to one row per voter, then widen voter `voter_index`."""
    rows = [set(a) for count, a in spec for _ in range(count)]
    rows[voter_index] |= set(approvals)
    return parse_profile([(1, "".join(sorted(r))) for r in rows], num_cand=num_cand)


def support_monotonicity_violation(rule_id, spec, k, added, *, with_voter,
                                   voter_index=0, num_cand=None):
    """Definition 3.3, resolute reading.

    `added` is the candidate set X whose support grows — either because a NEW
    voter approving exactly X joins (`with_voter=True`), or because an existing
    voter additionally approves X (`with_voter=False`). If X was in the winning
    committee before, it must still be after.
    """
    before_profile, names = parse_profile(spec, num_cand=num_cand)
    before = resolute_winner(rule_id, before_profile, k)
    x = {ord(ch) - ord("a") for ch in added}
    if not x <= set(before):
        return ("precondition", before, None)
    if with_voter:
        after_profile, _ = _profile_plus_voter(spec, added, num_cand=num_cand)
    else:
        after_profile, _ = _profile_voter_adds(spec, voter_index, added, num_cand=num_cand)
    after = resolute_winner(rule_id, after_profile, k)
    return None if x <= set(after) else ("violation", before, after)


def inclusion_sp_tiebreak_dependence(rule_id, spec, k, voter_index, new_ballot,
                                     num_cand=None):
    """Does the manipulation pay off under EVERY tiebreak, or only some?

    This resolves what looks at first like a contradiction inside the book.
    Table 3.1 marks CC and leximax-Phragmen `?` (open) for
    inclusion-strategyproofness, while the prose of Proposition A.4 lists both
    among the rules that fail it and hands each a counterexample. Both are
    right, and the distinction is here: for those two rules the MANIPULATED
    profile ends in a TIE, and the misreport pays only if the tiebreak lands on
    the right committee. The proposition's "without loss of generality we assume
    a tie ... is resolved in favour of {a,b}" is carrying that weight. Whether
    the rule fails for *every* tiebreaking order is the open part.

    Returns (paying, non_paying) committees among the manipulated winners, or
    None when the honest outcome is itself tied (nothing to compare against).
    """
    honest_profile, names = parse_profile(spec, num_cand=num_cand)
    honest_set = winners(rule_id, honest_profile, k)
    if len(honest_set) > 1:
        return None
    rows = [set(a) for count, a in spec for _ in range(count)]
    true_prefs = {ord(ch) - ord("a") for ch in "".join(sorted(rows[voter_index]))}
    manipulated = [(1, "".join(sorted(r))) for r in rows]
    manipulated[voter_index] = (1, "".join(sorted(set(new_ballot))))
    manip_profile, _ = parse_profile(manipulated, num_cand=num_cand)

    held = true_prefs & set(honest_set[0])
    paying, non_paying = [], []
    for w in winners(rule_id, manip_profile, k):
        (paying if held < (true_prefs & set(w)) else non_paying).append(w)
    return paying, non_paying


def inclusion_sp_violation(rule_id, spec, k, voter_index, new_ballot, num_cand=None):
    """Definition 3.7: R(A,k) & A(i) must not be a STRICT SUBSET of R(A',k) & A(i)."""
    honest_profile, names = parse_profile(spec, num_cand=num_cand)
    rows = [set(a) for count, a in spec for _ in range(count)]
    true_prefs = {ord(ch) - ord("a") for ch in "".join(sorted(rows[voter_index]))}
    manipulated = [(1, "".join(sorted(r))) for r in rows]
    manipulated[voter_index] = (1, "".join(sorted(set(new_ballot))))
    manip_profile, _ = parse_profile(manipulated, num_cand=num_cand)

    honest = resolute_winner(rule_id, honest_profile, k)
    manip = resolute_winner(rule_id, manip_profile, k)
    got_honest = true_prefs & set(honest)
    got_manip = true_prefs & set(manip)
    if got_honest < got_manip:  # strict subset — the manipulation paid off
        return (honest, manip, got_honest, got_manip)
    return None


def consistency_violation(rule_id, spec_a, spec_b, k, num_cand=None):
    """Definition 3.4: agreeing electorates must keep their agreement when merged."""
    pa, names = parse_profile(spec_a, num_cand=num_cand)
    pb, _ = parse_profile(spec_b, num_cand=num_cand)
    pj, _ = parse_profile(spec_a + spec_b, num_cand=num_cand)
    wa, wb = set(winners(rule_id, pa, k)), set(winners(rule_id, pb, k))
    shared = wa & wb
    if not shared:
        return ("precondition", sorted(wa), sorted(wb), None)
    joint = set(winners(rule_id, pj, k))
    return None if joint == shared else ("violation", sorted(shared), sorted(joint), names)


# --------------------------------------------------------------------------
# the book's witnesses (Chapter 3 + Appendix A, Propositions A.1-A.4)
# --------------------------------------------------------------------------

#: Every one of these reproduces an `x` (or a "cand") cell of Table 3.1.
WITNESSES = []


def witness(axiom, rule, cite, **kwargs):
    WITNESSES.append(dict(axiom=axiom, rule=rule, cite=cite, **kwargs))


# --- Pareto efficiency (Example 3.1, Proposition A.1) ---
witness("pareto", "monroe", "Example 3.1", k=2,
        spec=[(2, "a"), (1, "ac"), (1, "ad"), (10, "bc"), (10, "bd")],
        note="Monroe seats {c,d}; {a,b} gives every voter a representative.")
witness("pareto", "cc", "Proposition A.1", k=2,
        spec=[(1, "acd"), (1, "bcd")],
        note="CC ties {a,b} with {c,d} on coverage; {c,d} gives everyone TWO.")
witness("pareto", "minimaxav", "Proposition A.1", k=1,
        spec=[(1, "ac"), (1, "bc"), (1, "de")],
        note="Every size-1 committee has worst-case Hamming distance 3, so MAV "
             "ties them all — including {a}, which {c} dominates.")

# --- committee monotonicity (Proposition A.2) ---
for _rule in ("cc", "pav", "monroe", "leximaxphragmen", "minimaxav"):
    witness("committee_monotonicity", _rule, "Proposition A.2", k=1,
            spec=[(2, "a"), (3, "ac"), (3, "bc"), (2, "b")],
            note="k=1 elects {c}; k=2 elects {a,b} and drops the sole winner.")
witness("committee_monotonicity", "equal-shares", "Proposition A.2", k=3,
        spec=[(1, "ade"), (1, "ac"), (1, "be"), (1, "cdf")],
        note="k=3 elects {a,c,e}; k=4 elects {a,b,c,d} and drops e.")
witness("committee_monotonicity", "greedy-monroe", "Proposition A.2", k=2,
        spec=[(6, "a"), (4, "ac"), (2, "abc"), (2, "a"), (1, "ad"), (3, "bd")],
        note="k=2 elects {a,b}; k=3 elects {a,c,d} and drops b.")

# --- support monotonicity WITH additional voters (Proposition A.3) ---
witness("support_mono_with", "seqcc", "Proposition A.3", k=3, added="ad",
        spec=[(3, "a"), (1, "acd"), (1, "b"), (2, "bc"), (1, "bd"), (2, "c"), (2, "d")],
        note="seq-CC elects {a,c,d}; one more voter approving {a,d} drops d.")
witness("support_mono_with", "greedy-monroe", "Proposition A.3", k=3, added="e",
        spec=[(1, "bcd"), (1, "acf"), (1, "ade"), (1, "ce"), (1, "ab"),
              (2, "df"), (1, "be"), (1, "bf")],
        note="Greedy Monroe elects {b,e,f}; one more voter approving {e} drops e.")
witness("support_mono_with", "equal-shares", "Proposition A.3", k=3, added="a",
        spec=[(1, "bd"), (1, "ab"), (1, "bde"), (1, "ae"), (2, "cde"),
              (1, "ce"), (1, "ace"), (1, "bcd")],
        note="Equal Shares elects {a,d,e}; one more voter approving {a} drops a.")

# --- support monotonicity WITHOUT additional voters (Proposition A.3) ---
witness("support_mono_without", "seqpav", "Proposition A.3", k=3, added="af",
        voter_index=0,
        spec=[(1, "cd"), (1, "ac"), (1, "ad"), (1, "af"), (1, "bc"), (2, "bf"), (1, "ce")],
        note="seq-PAV elects {a,c,f}; voter 1 widening {c,d} to {a,c,d,f} drops f.")
witness("support_mono_without", "seqcc", "Proposition A.3", k=3, added="bd",
        voter_index=0,
        spec=[(1, "e"), (1, "a"), (1, "ad"), (3, "b"), (2, "ac"), (1, "bcd"),
              (2, "c"), (2, "d")],
        note="seq-CC elects {b,c,d}; voter 1 widening {e} to {b,d,e} drops d.")
witness("support_mono_without", "equal-shares", "Proposition A.3", k=3, added="ae",
        voter_index=0,
        spec=[(1, "b"), (1, "abe"), (2, "be"), (1, "c"), (1, "ac"), (1, "a")],
        note="Equal Shares elects {a,b,e}; voter 1 widening {b} to {a,b,e} drops e.")
witness("support_mono_without", "greedy-monroe", "Proposition A.3", k=2, added="bc",
        voter_index=0,
        spec=[(1, "d"), (1, "c"), (1, "b"), (1, "ac")],
        note="Greedy Monroe elects {b,c}; voter 1 widening {d} to {b,c,d} drops b.")

# --- consistency (Example 3.2) ---
witness("consistency", "monroe", "Example 3.2", k=2,
        spec=[(2, "ay"), (2, "by")],
        spec_b=[(1, "y"), (1, "a"), (4, "ax"), (1, "y"), (1, "by"), (4, "bx")],
        num_cand=25,
        note="Both electorates can elect {a,b}; merged, Monroe prefers {x,y}.")

# --- inclusion-strategyproofness (Proposition A.4) ---
witness("inclusion_sp", "cc", "Proposition A.4", k=2, voter_index=0, new_ballot="b",
        spec=[(1, "ab"), (3, "a"), (1, "c")], tiebreak_dependent=True,
        note="Dropping a from her ballot swaps {a,c} for {a,b} — she gains b. "
             "Pays only under a tiebreak favouring {a,b}, which is why Table 3.1 "
             "leaves CC's cell OPEN rather than marking it a failure.")
witness("inclusion_sp", "pav", "Proposition A.4", k=3, voter_index=0, new_ballot="e",
        spec=[(1, "cde"), (1, "ab"), (1, "bf"), (1, "acd"), (1, "bcf"), (1, "cef")],
        note="Reporting {e} instead of {c,d,e} swaps {b,c,f} for {b,c,e}.")
witness("inclusion_sp", "seqpav", "Proposition A.4", k=3, voter_index=0, new_ballot="a",
        spec=[(1, "ab"), (1, "bd"), (1, "cf"), (1, "abf"), (1, "bf"), (1, "bc")],
        note="Reporting {a} instead of {a,b} swaps {b,c,f} for {a,b,f}.")
witness("inclusion_sp", "seqcc", "Proposition A.4", k=3, voter_index=0, new_ballot="c",
        spec=[(1, "bef"), (1, "ab"), (1, "def"), (1, "de"), (1, "bf"), (2, "cd"),
              (1, "abc"), (1, "ac"), (1, "abe"), (1, "aef"), (1, "bcd")],
        note="Reporting {c} instead of {b,e,f} swaps {a,b,d} for {b,c,e}.")
witness("inclusion_sp", "revseqpav", "Proposition A.4", k=2, voter_index=0,
        new_ballot="a",
        spec=[(1, "abc"), (1, "bd"), (1, "bc"), (1, "ade"), (1, "be")],
        note="Reporting {a} instead of {a,b,c} swaps {b,d} for {a,b}.")
witness("inclusion_sp", "monroe", "Proposition A.4", k=3, voter_index=0, new_ballot="f",
        spec=[(1, "bd"), (1, "abc"), (1, "be"), (1, "de"), (1, "ef"), (1, "bce"),
              (1, "cde"), (1, "bc"), (2, "af"), (1, "bcd"), (1, "ad")],
        note="Reporting {f} instead of {b,d} swaps {a,b,e} for {b,d,f}.")
witness("inclusion_sp", "greedy-monroe", "Proposition A.4", k=2, voter_index=0,
        new_ballot="b",
        spec=[(1, "ab"), (1, "acf"), (1, "acd"), (1, "ef")],
        note="Reporting {b} instead of {a,b} swaps {a,c} for {a,b}.")
witness("inclusion_sp", "seqphragmen", "Proposition A.4", k=2, voter_index=0,
        new_ballot="c",
        spec=[(1, "abc"), (1, "ab"), (1, "bf"), (1, "ce"), (1, "bef"), (1, "bdf")],
        note="Reporting {c} instead of {a,b,c} swaps {b,f} for {b,c}.")
witness("inclusion_sp", "leximaxphragmen", "Proposition A.4", k=3, voter_index=0,
        new_ballot="a",
        spec=[(1, "ab"), (3, "bcd")], tiebreak_dependent=True,
        note="Reporting {a} instead of {a,b} swaps {b,c,d} for {a,b,c}. Pays "
             "under two of the three tied committees, so Table 3.1 leaves "
             "leximax-Phragmen's cell OPEN too.")
witness("inclusion_sp", "equal-shares", "Proposition A.4", k=3, voter_index=0,
        new_ballot="c",
        spec=[(1, "bcd"), (1, "ab"), (1, "bd"), (1, "cd"), (2, "de")],
        note="Reporting {c} instead of {b,c,d} swaps {b,d,e} for {b,c,d}.")
witness("inclusion_sp", "minimaxav", "Proposition A.4", k=3, voter_index=0,
        new_ballot="c",
        spec=[(1, "abc"), (1, "bd"), (2, "abe"), (1, "abd"), (1, "ab")],
        note="Reporting {c} instead of {a,b,c} swaps {a,b,d} for {a,b,c}.")
witness("inclusion_sp", "sav", "Proposition A.4", k=1, voter_index=0, new_ballot="a",
        spec=[(1, "abc"), (1, "de")],
        note="SAV splits one vote across a ballot's marks, so the two-voter "
             "profile elects {d}; approving ONLY a wins the seat outright.")


# --------------------------------------------------------------------------
# replay
# --------------------------------------------------------------------------

def check_witness(w, verbose=False):
    """Replay one witness. Returns (ok, message)."""
    rule, axiom, k = w["rule"], w["axiom"], w["k"]
    spec, num_cand = w["spec"], w.get("num_cand")
    profile, names = parse_profile(spec, num_cand=num_cand)

    if axiom == "pareto":
        got = pareto_violation(rule, profile, k)
        if got is None:
            return False, "no dominated committee found — the cell did NOT reproduce"
        w_, dom = got
        return True, f"{fmt(w_, names)} wins but is dominated by {fmt(dom, names)}"

    if axiom == "committee_monotonicity":
        got = committee_monotonicity_violation(rule, profile, k)
        if got is None:
            return False, f"k={k} winner IS a subset of the k={k + 1} winner"
        small, large = got
        return True, f"k={k} -> {fmt(small, names)}, k={k + 1} -> {fmt(large, names)}"

    if axiom in ("support_mono_with", "support_mono_without"):
        got = support_monotonicity_violation(
            rule, spec, k, w["added"], with_voter=(axiom == "support_mono_with"),
            voter_index=w.get("voter_index", 0), num_cand=num_cand)
        if got is None:
            return False, "support grew and the committee held — no violation"
        kind, before, after = got
        if kind == "precondition":
            return False, (f"precondition failed: {w['added']} not inside the "
                           f"winner {fmt(before, names)}")
        return True, f"{fmt(before, names)} -> {fmt(after, names)} (lost {w['added']})"

    if axiom == "consistency":
        got = consistency_violation(rule, spec, w["spec_b"], k, num_cand=num_cand)
        if got is None:
            return False, "merged electorate kept the shared winner — no violation"
        kind, shared, joint, _ = got
        if kind == "precondition":
            return False, "the two electorates share no winning committee"
        shared_s = ", ".join(fmt(c, names) for c in shared)
        joint_s = ", ".join(fmt(c, names) for c in joint)
        return True, f"both elect {shared_s}; merged elects {joint_s}"

    if axiom == "inclusion_sp":
        got = inclusion_sp_violation(rule, spec, k, w["voter_index"],
                                     w["new_ballot"], num_cand=num_cand)
        if got is None:
            return False, "the misreport did not strictly improve the manipulator"
        honest, manip, got_h, got_m = got
        msg = (f"honest -> {fmt(honest, names)} (she gets {fmt(got_h, names)}); "
               f"misreport -> {fmt(manip, names)} (she gets {fmt(got_m, names)})")
        dep = inclusion_sp_tiebreak_dependence(
            rule, spec, k, w["voter_index"], w["new_ballot"], num_cand=num_cand)
        if dep is not None:
            paying, non_paying = dep
            claimed = w.get("tiebreak_dependent", False)
            actual = bool(paying and non_paying)
            if claimed != actual:
                return False, (f"tiebreak_dependent={claimed} but the manipulated "
                               f"profile has {len(paying)} paying / "
                               f"{len(non_paying)} non-paying tied committees")
            if actual:
                msg += f"  [TIEBREAK-DEPENDENT: {len(non_paying)} tied committee(s) "
                msg += "would not pay — table cell stays OPEN]"
        return True, msg

    return False, f"unknown axiom {axiom!r}"


AXIOM_TITLES = {
    "pareto": "Pareto efficiency (Def. 3.1)",
    "committee_monotonicity": "Committee monotonicity (Def. 3.2)",
    "support_mono_with": "Support monotonicity WITH additional voters (Def. 3.3)",
    "support_mono_without": "Support monotonicity WITHOUT additional voters (Def. 3.3)",
    "consistency": "Consistency (Def. 3.4)",
    "inclusion_sp": "Inclusion-strategyproofness (Def. 3.7)",
}


def run_all(verbose=False):
    failures = []
    by_axiom = {}
    for w in WITNESSES:
        by_axiom.setdefault(w["axiom"], []).append(w)

    print("--- Table 3.1 witnesses replayed through abcvoting ---")
    for axiom in ("pareto", "committee_monotonicity", "support_mono_with",
                  "support_mono_without", "consistency", "inclusion_sp"):
        if axiom not in by_axiom:
            continue
        print(f"\n{AXIOM_TITLES[axiom]}")
        for w in by_axiom[axiom]:
            ok, msg = check_witness(w, verbose=verbose)
            mark = "REPRODUCED" if ok else "*** FAILED ***"
            label = dict(TABLE_RULES).get(w["rule"])
            label = next((n for n, r in TABLE_RULES if r == w["rule"]), w["rule"])
            print(f"  [{mark}] {label:22s} {w['cite']:18s} {msg}")
            if verbose:
                print(f"               profile: {fmt_profile(w['spec'])}  (k={w['k']})")
                print(f"               book:    {w['note']}")
            if not ok:
                failures.append((axiom, w["rule"], msg))

    print(f"\n{len(WITNESSES) - len(failures)}/{len(WITNESSES)} witnesses reproduced.")
    if failures:
        print("\nFAILED:")
        for axiom, rule, msg in failures:
            print(f"  {axiom} / {rule}: {msg}")
    return 1 if failures else 0


def search_pareto(rule_id, trials, seed=0, max_cand=6, max_voters=6, max_k=3):
    """Random small-profile hunt for a Pareto violation. Refutation only."""
    rng = random.Random(seed)
    for t in range(trials):
        m = rng.randint(3, max_cand)
        n = rng.randint(2, max_voters)
        spec = []
        for _ in range(n):
            size = rng.randint(1, max(1, m - 1))
            approvals = "".join(sorted(rng.sample(
                [chr(ord("a") + i) for i in range(m)], size)))
            spec.append((1, approvals))
        k = rng.randint(1, min(max_k, m - 1))
        profile, names = parse_profile(spec, num_cand=m)
        got = pareto_violation(rule_id, profile, k)
        if got is not None:
            w_, dom = got
            return dict(trial=t, spec=spec, k=k,
                        winner=fmt(w_, names), dominator=fmt(dom, names))
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verbose", "-v", action="store_true",
                    help="print each witness profile and the book's description")
    ap.add_argument("--search", type=int, metavar="TRIALS", default=0,
                    help="hunt for a Pareto violation on random small profiles for "
                         "each rule the book marks 'strong' (refutation only)")
    args = ap.parse_args(argv)

    if not ABCVOTING_AVAILABLE:
        print("abcvoting is not installed — `uv sync` or `pip install abcvoting`.")
        return 2

    status = run_all(verbose=args.verbose)

    if args.search:
        print(f"\n--- refutation search: {args.search} random profiles per rule ---")
        print("The book marks AV, PAV and SAV STRONGLY Pareto efficient. A hit here")
        print("would refute the table (or this module's reading of it); a miss proves")
        print("nothing, it only fails to refute.")
        for rule_id in ("av", "pav", "sav"):
            hit = search_pareto(rule_id, args.search)
            if hit:
                print(f"  {rule_id}: VIOLATION at trial {hit['trial']}: "
                      f"{fmt_profile(hit['spec'])} k={hit['k']} -> "
                      f"{hit['winner']} dominated by {hit['dominator']}")
                status = 1
            else:
                print(f"  {rule_id}: no violation in {args.search} profiles (as expected)")

    return status


if __name__ == "__main__":
    sys.exit(main())
