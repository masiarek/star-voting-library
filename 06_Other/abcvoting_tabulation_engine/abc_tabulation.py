"""
abc_tabulation.py — multi-winner Approval (ABC) rules via `abcvoting`.

Runs approval-based committee (ABC) rules from Martin Lackner's peer-reviewed
`abcvoting` library (https://github.com/martinlackner/abcvoting) on this
repo's approval YAML files. Two jobs:

1. **Extend** the LH engine: the LH engine tabulates *bloc* Approval only
   (top-`num_winners` by approvals). This wrapper adds the PROPORTIONAL
   rules on the same ballots — **SPAV** (seqpav), **PAV** (pav),
   **seq-Phragmén** (seqphragmen) — the rules described in
   `00_start_here/Approval_Voting/approval_multiwinner.md`.
2. **Cross-check**: abcvoting's plain `av` rule must match the LH engine's
   bloc-Approval result (see `tests/test_abcvoting_crosscheck.py`).

Usage (CLI):
    python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py FILE.yaml
    python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py FILE.yaml --rules av,seqpav,pav
    python 06_Other/abcvoting_tabulation_engine/abc_tabulation.py FILE.yaml --seats 3

Programmatic:
    from abc_tabulation import tabulate_abc
    result = tabulate_abc("path/to/election.yaml")   # dict: rule -> [committee, ...]

Requires: pip install abcvoting  (optional dependency; importers should guard).
Ties: a rule may return SEVERAL tied committees; all are reported.
"""
import argparse
import os
import sys

import yaml

# abcvoting is optional; callers (e.g. the pytest) should skip if absent.
try:
    from abcvoting.preferences import Profile
    from abcvoting import abcrules
    ABCVOTING_AVAILABLE = True
except Exception:  # pragma: no cover
    ABCVOTING_AVAILABLE = False

#: Default rule set. `av` = bloc Approval (the LH engine's method — the
#: cross-check anchor); the rest are the proportional rules the concept
#: page describes.
DEFAULT_RULES = ("av", "seqpav", "pav", "seqphragmen")

#: Ballot markers that tabulate as "not approved" (house convention:
#: blank / race abstention / candidate abstention / spoiled / reissued).
_ZERO_MARKS = {"", "-", "~", "&", "?", "%", "0"}


# --------------------------------------------------------------------------- #
# Parsing: one approval YAML -> (candidate names, list of approval index sets,
# seats). Accepts the repo's flat schema (`ballots:` CSV block).
# --------------------------------------------------------------------------- #
def load_approval_election(path):
    d = yaml.safe_load(open(path))
    if not isinstance(d, dict) or "ballots" not in d:
        raise ValueError(f"{path}: no top-level `ballots:` block (flat schema required).")
    method = str(d.get("voting_method", "")).lower()
    if "approval" not in method and method not in ("av", "approve"):
        raise ValueError(f"{path}: voting_method {d.get('voting_method')!r} is not an "
                         f"Approval method; this engine reads approval ballots only.")
    rows = [r.strip() for r in d["ballots"].splitlines() if r.strip()]
    names = [c.strip() for c in rows[0].split(",")]
    voters = []
    for row in rows[1:]:
        cells = row.split("#", 1)[0].split(",")
        if len(cells) != len(names):
            raise ValueError(f"{path}: row {row!r} has {len(cells)} cells, "
                             f"expected {len(names)}.")
        approved = set()
        for i, cell in enumerate(cells):
            mark = cell.strip()
            if mark in _ZERO_MARKS:
                continue
            if mark != "1":
                raise ValueError(f"{path}: invalid Approval mark {mark!r} in row "
                                 f"{row!r} (only 0/1/markers allowed).")
            approved.add(i)
        voters.append(approved)
    seats = int(d.get("num_winners", 1))
    return names, voters, seats


def tabulate_abc(path, rules=DEFAULT_RULES, seats=None):
    """Run each ABC rule; return {rule: [sorted name-list per tied committee]}."""
    names, voters, file_seats = load_approval_election(path)
    k = seats if seats is not None else file_seats
    profile = Profile(len(names))
    # abcvoting requires non-empty approval sets; ballots approving no one
    # can't affect any ABC rule, so they are dropped (count is reported).
    nonempty = [v for v in voters if v]
    profile.add_voters(nonempty)
    out = {}
    for rule in rules:
        committees = abcrules.compute(rule, profile, committeesize=k)
        out[rule] = [sorted(names[i] for i in c) for c in committees]
    out["_meta"] = {"names": names, "seats": k, "ballots": len(voters),
                    "empty_ballots": len(voters) - len(nonempty)}
    return out


def _print_report(path, result):
    meta = result["_meta"]
    print(f"\n--- abcvoting: approval-based committee rules "
          f"({meta['seats']} seats) ---")
    note = (f" ({meta['empty_ballots']} empty — ignored)"
            if meta["empty_ballots"] else "")
    print(f" {os.path.basename(path)}: {meta['ballots']} ballots{note}, "
          f"candidates: {', '.join(meta['names'])}")
    for rule, committees in result.items():
        if rule == "_meta":
            continue
        longname = abcrules.Rule(rule).longname if ABCVOTING_AVAILABLE else rule
        pretty = "  |  ".join(", ".join(c) for c in committees)
        tie = f"  [{len(committees)} tied committees]" if len(committees) > 1 else ""
        print(f"   {rule:12s} {longname:42s} ->  {pretty}{tie}")
    print("   (av = bloc Approval, the LH engine's method; "
          "seqpav/pav/seqphragmen are proportional.)")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("files", nargs="+", help="approval election YAML file(s)")
    ap.add_argument("--rules", default=",".join(DEFAULT_RULES),
                    help="comma-separated abcvoting rule ids "
                         f"(default: {','.join(DEFAULT_RULES)})")
    ap.add_argument("--seats", type=int, default=None,
                    help="override the file's num_winners")
    args = ap.parse_args(argv)
    if not ABCVOTING_AVAILABLE:
        sys.exit("Error: the `abcvoting` library is not installed. "
                 "Install with: pip install abcvoting")
    rules = [r.strip() for r in args.rules.split(",") if r.strip()]
    for path in args.files:
        try:
            result = tabulate_abc(path, rules=rules, seats=args.seats)
        except ValueError as e:
            sys.exit(f"Error: {e}")
        _print_report(path, result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
