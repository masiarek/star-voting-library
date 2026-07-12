#!/usr/bin/env python3
"""3-2-1 Voting — a standalone tabulation engine for this repo.

3-2-1 Voting (Jameson Quinn / Center for Election Science): voters rate each
candidate **Good / OK / Bad**, and the winner is found in three steps:

  1. Semifinalists — the 3 candidates with the most **Good** ratings.
  2. Finalists     — of those 3, the 2 with the fewest **Bad** ratings.
  3. Winner        — of those 2, the one rated higher on more ballots
                     (a virtual head-to-head runoff).

WHY THIS EXISTS / PROVENANCE
    No off-the-shelf, cleanly-licensed 3-2-1 engine exists (BetterVoting, the
    LH starvote engine, pref_voting, abcvoting and pyrankvote all lack it).
    The only authoritative implementation is Jameson Quinn's `V321` class in
    the Center for Election Science's `vse-sim` — but that repo carries no
    LICENSE (so it can't be vendored) and is coupled to a simulation framework.

    3-2-1 is a *published, documented* method, so this is a clean-room
    implementation of the public spec (electowiki.org/wiki/3-2-1_voting). It is
    VERIFIED to reproduce every one of Quinn's own `V321` doctest vectors — see
    QUINN_VECTORS below and `--selftest`. So "faithful" here means: matches the
    published rules AND the inventor's reference test cases.

SCOPE / KNOWN GAPS (documented, not faked)
    This matches Quinn's `V321.results()`, which applies the plain 3-step. The
    full electowiki spec adds two guard rules that `V321` does NOT apply:
      * dark-horse rule — the 3rd semifinalist must have >= half the Good count
        of the 1st, else the top two semifinalists go straight to finalists;
      * party-clone rule — the 3rd semifinalist can't share a party with both
        others. We have no party data on ballots, so this rule is omitted.
    The dark-horse rule is available via `apply_dark_horse=True` but OFF by
    default so results match the verified V321 reference.

BALLOT ENCODING
    Good = 2, OK = 1, Bad = 0. A blank / unmarked candidate counts as **Bad**
    (0) — the natural 3-2-1 reading (you didn't rate them, so they're not Good
    or OK). Markers (-, ~, &, ?, %) all read as Bad, matching the repo's
    "all markers tabulate as 0" convention.

USAGE
    python three_two_one_tabulation.py <election.yaml>
    python three_two_one_tabulation.py --selftest
"""

import sys
import re

GOOD, OK, BAD = 2, 1, 0
_MARKERS = set("-~&?%")


def tabulate_321(ballots, apply_dark_horse=False):
    """Run 3-2-1 on `ballots` (list of per-voter score lists; higher = better,
    Good=2/OK=1/Bad=0). Returns a dict with the winner index and each step's
    working, so a report can show *why*. Mirrors Jameson Quinn's V321.results().
    """
    if not ballots:
        raise ValueError("no ballots")
    n = len(ballots[0])
    if n < 2:
        raise ValueError("need at least 2 candidates")
    cols = list(zip(*ballots))
    good = [sum(1 for s in cols[c] if s > OK) for c in range(n)]      # count of Good (2)
    notbad = [sum(1 for s in cols[c] if s > BAD) for c in range(n)]   # count of not-Bad (>=OK)
    bad = [len(ballots) - notbad[c] for c in range(n)]

    # Step 1 — semifinalists: the (up to) 3 candidates with the most Good.
    # Stable ascending sort then take the top slice, mirroring numpy argsort[-3:].
    order_by_good = sorted(range(n), key=lambda i: good[i])
    semis = order_by_good[-3:]                      # [.., second, first] by Good

    # Optional dark-horse guard (OFF by default; see module docstring).
    dark_horse_triggered = False
    if apply_dark_horse and len(semis) == 3:
        first = max(semis, key=lambda c: good[c])
        third = min(semis, key=lambda c: good[c])
        if good[third] * 2 < good[first]:
            dark_horse_triggered = True
            semis = sorted(semis, key=lambda c: good[c])[-2:]  # top two straight to finalists

    # Step 2 — finalists: of the semifinalists, the ones with the fewest Bad
    # (i.e. the most not-Bad). Keep the top two.
    by_fewest_bad = sorted(semis, key=lambda c: notbad[c])   # ascending not-Bad
    finalists = by_fewest_bad[-2:] if len(by_fewest_bad) >= 2 else by_fewest_bad
    top = finalists[-1]                                       # fewest Bad
    runner_up = finalists[0]

    # Step 3 — runoff: whichever finalist more ballots score strictly higher.
    # A tie (upset == 0) leaves `top` (the fewest-Bad seed) as the winner.
    upset = sum((b[runner_up] > b[top]) - (b[runner_up] < b[top]) for b in ballots)
    runoff_for_top = sum(1 for b in ballots if b[top] > b[runner_up])
    runoff_for_runner = sum(1 for b in ballots if b[runner_up] > b[top])
    runoff_equal = len(ballots) - runoff_for_top - runoff_for_runner
    winner = runner_up if upset > 0 else top

    return {
        "winner": winner,
        "good": good, "ok": [sum(1 for s in cols[c] if s == OK) for c in range(n)],
        "bad": bad, "notbad": notbad,
        "semifinalists": sorted(semis, key=lambda c: -good[c]),
        "finalists": sorted(finalists, key=lambda c: -notbad[c]),
        "runoff": {"top": top, "runner_up": runner_up,
                   "for_top": runoff_for_top, "for_runner": runoff_for_runner,
                   "equal": runoff_equal},
        "dark_horse_triggered": dark_horse_triggered,
    }


# --- Jameson Quinn's V321 doctest vectors (the reference oracle) --------------
# From electionscience/vse-sim methods.py, class V321. Each is (ballots, winner
# index). Our engine must reproduce every winner; run with --selftest.
QUINN_VECTORS = [
    ([[0, 1, 2]], 2),
    ([[0, 1, 2], [2, 1, 0]], 1),
    ([[0, 1, 2]] * 4 + [[2, 1, 0]] * 3 + [[1, 2, 0]] * 2, 1),
    ([[0, 1, 2, 1]] * 29 + [[1, 2, 0, 1]] * 30 + [[2, 0, 1, 1]] * 31 + [[1, 1, 1, 2]] * 10, 0),
    ([[1, 0, 2, 1]] * 29 + [[0, 2, 1, 1]] * 30 + [[2, 1, 0, 1]] * 31 + [[1, 1, 1, 2]] * 10, 0),
]


def selftest():
    ok = True
    for i, (ballots, expected) in enumerate(QUINN_VECTORS, 1):
        got = tabulate_321(ballots)["winner"]
        good = got == expected
        ok &= good
        print(f"  vector {i}: winner={got} expected={expected} "
              f"{'OK' if good else 'MISMATCH'}")
    print("3-2-1 engine reproduces Jameson Quinn's V321 doctest vectors ✓"
          if ok else "*** MISMATCH vs V321 — do not trust this build ***")
    return ok


# --- YAML / ballot parsing ----------------------------------------------------
_LEVEL = {"2": GOOD, "1": OK, "0": BAD, "g": GOOD, "o": OK, "b": BAD}


def _cell(tok):
    tok = tok.strip().lower()
    if tok == "" or tok in _MARKERS:
        return BAD
    if tok in _LEVEL:
        return _LEVEL[tok]
    raise ValueError(f"bad 3-2-1 cell {tok!r} — use Good/OK/Bad as 2/1/0 (or "
                     f"G/O/B); blank = Bad")


def parse_ballots_block(text):
    """Parse a `ballots:` literal block into (candidate_names, ballots).
    Row form: `A,B,C,D` header, then `2,1,,0` rows; optional `N × ...` weight;
    trailing `# comment` ignored."""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        raise ValueError("empty ballots block")
    names = [c.strip() for c in re.split(r"[,\t]", lines[0].split("#")[0])]
    ncand = len(names)
    ballots = []
    for ln in lines[1:]:
        row = ln.split("#")[0].strip()
        if not row:
            continue
        weight = 1
        m = re.match(r"^\s*(\d+)\s*[×xX*:]\s*(.*)$", row)
        if m:
            weight, row = int(m.group(1)), m.group(2)
        cells = re.split(r"[,\t]", row)
        if len(cells) != ncand:
            raise ValueError(f"row has {len(cells)} cells, expected {ncand}: {ln!r}")
        scores = [_cell(c) for c in cells]
        ballots.extend([scores] * weight)
    return names, ballots


def _load_yaml(path):
    try:
        import yaml
        with open(path) as f:
            return yaml.safe_load(f)
    except ImportError:
        # minimal fallback: pull the ballots: |- block + election_title
        with open(path) as f:
            raw = f.read()
        data = {}
        mt = re.search(r"^election_title:\s*(.+)$", raw, re.M)
        if mt:
            data["election_title"] = mt.group(1).strip()
        mb = re.search(r"^ballots:\s*\|-?\s*\n((?:[ \t]+.*\n?)+)", raw, re.M)
        if mb:
            data["ballots"] = "\n".join(l.strip() for l in mb.group(1).splitlines())
        me = re.search(r"^expected_winner:\s*(.+)$", raw, re.M)
        if me:
            data["expected_winner"] = me.group(1).strip()
        return data


def _report(data, res, names):
    title = data.get("election_title", "3-2-1 election")
    W = names[res["winner"]]
    out = [f"=== {title} ===", "", "--- 3-2-1 Voting ---",
           f" Tabulating {sum(1 for _ in range(len(names)))} candidates, "
           f"Good=2 / OK=1 / Bad=0 (blank = Bad).", ""]
    out.append("Ratings tally (Good / OK / Bad):")
    for c, nm in enumerate(names):
        out.append(f"   {nm:<14} Good {res['good'][c]:>4} | OK {res['ok'][c]:>4} "
                   f"| Bad {res['bad'][c]:>4}")
    out.append("")
    out.append("Step 1 — Semifinalists (most Good): " +
               ", ".join(f"{names[c]} ({res['good'][c]})" for c in res["semifinalists"]))
    if res["dark_horse_triggered"]:
        out.append("   (dark-horse rule triggered: top two go straight to finalists)")
    out.append("Step 2 — Finalists (fewest Bad): " +
               ", ".join(f"{names[c]} (Bad {res['bad'][c]})" for c in res["finalists"]))
    r = res["runoff"]
    equal_note = f" ({r['equal']} rated equal)" if r["equal"] else ""
    out.append(f"Step 3 — Runoff: {names[r['top']]} {r['for_top']} vs "
               f"{names[r['runner_up']]} {r['for_runner']}{equal_note}")
    out.append("")
    out.append(f"Winner — 3-2-1 Voting: {W}")
    return "\n".join(out)


def main(argv):
    if len(argv) == 2 and argv[1] == "--selftest":
        return 0 if selftest() else 1
    if len(argv) != 2:
        print(__doc__)
        return 2
    data = _load_yaml(argv[1])
    if not data or "ballots" not in data:
        print("error: no `ballots:` block found in", argv[1])
        return 1
    names, ballots = parse_ballots_block(data["ballots"])
    res = tabulate_321(ballots)
    print(_report(data, res, names))
    exp = data.get("expected_winner")
    if exp and exp != names[res["winner"]]:
        print(f"\n*** expected_winner={exp!r} but engine says "
              f"{names[res['winner']]!r} ***")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
