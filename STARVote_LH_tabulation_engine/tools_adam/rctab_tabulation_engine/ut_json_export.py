#!/usr/bin/env python3
"""ut_json_export.py — a ranked case YAML → Universal RCV Tabulator JSON.

WHY THIS EXISTS. RCTab's own `*_detailed_report.json` is already this format, so
for a case that has been through `rctab_crosscheck.py` there is nothing to do.
This is the no-Java path: it recounts the ballots here and writes the same shape,
which is what RCVis (<https://www.rcvis.com/>) ingests. Concept page:
07_Concepts/tabulation_engines/rcvis.md.

THE PART THAT IS NOT A REFORMAT. Our RCV-IRV report prints round tallies and
nothing else — it never says where a transferred vote went. A Sankey is *made
of* that missing information, so the transfers are recomputed from the ballots
here: for every ballot held by an eliminated candidate, find its next surviving
preference, or count it exhausted.

TWO THINGS THE FORMAT INSISTS ON, both learned by having a file rejected:

 1. **An eliminated candidate must LEAVE the tally.** Our report keeps them
    listed at 0 down the rest of the page; the schema treats a name reappearing
    after its elimination as an error ("they should be removed from all future
    vote tallies"). Emit only the survivors each round.
 2. **Vote counts are STRINGS, not numbers** (`"315"`, not `315`) — the schema's
    decimal-as-string type, so fractional STV transfers survive round-tripping.

Exhausted ballots ride in the `transfers` map under the key `exhausted`, which is
how RCVis derives its "Inactive Ballots: N with no choices left" line.

ON A DEAD TIE THIS DOES NOT MATCH THE LH ENGINE, AND CANNOT. When every
remaining candidate is tied, the vendored pyrankvote's winner falls out of the
order the ballot ROWS happen to be written in (see 07_Concepts/topics/ties/
batch_elimination.md); this drops the first-seen name instead. On
`batch_all_out_cycle_c3_b3` the engine prints Amy and this eliminates her. That
case's own file says the engine's answer "is not the method's answer", so the
disagreement is between two arbitrary conventions rather than a bug in either --
but do not export a tie-decided case and present the picture as our count.

    uv run STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/ut_json_export.py FILE.yaml [-o OUT.json]

Validation is optional and skipped if `rcvformats` (MIT, `pip install
rcvformats`) is absent; when present the file is checked before it is written.
"""
import argparse
import json
import os
import re
import sys


# Methods whose ballots are ranked. Anything else (STAR, Score, Approval,
# Plurality, the PR variants) has no ranking to export and is refused outright
# rather than mangled -- an allowlist, so a new method defaults to "no".
RANKED_METHODS = {"rcv", "rcv_irv", "rcvirv", "irv", "stv", "hare",
                  "rankedrobin", "rcv_rr", "copeland", "consensus"}


def load_case(path):
    """Return (title, [(weight, [ranked names])]) from a ranked case YAML."""
    raw = open(path, encoding="utf-8").read()
    m = re.search(r'^election_title:\s*"?(.+?)"?\s*$', raw, re.M)
    title = m.group(1) if m else os.path.splitext(os.path.basename(path))[0]

    m = re.search(r'^voting_method:\s*"?([\w-]+)"?', raw, re.M)
    method = (m.group(1) if m else "").lower().replace("-", "_")
    if method and method not in RANKED_METHODS:
        sys.exit(f"{path}: voting_method '{method}' is not a ranked method — "
                 "this writes ranked (IRV) JSON only")

    m = re.search(r'^ballots:\s*\|-?\n((?:[ \t]+.*\n?)+)', raw, re.M)
    if not m:
        sys.exit(f"{path}: no ballots: block found")

    ballots = []
    for line in m.group(1).splitlines():
        line = re.sub(r"\s*#.*$", "", line).strip()   # drop trailing comments
        if not line:
            continue
        weight, sep, rest = line.partition(":")
        if not sep or not weight.strip().isdigit():   # unweighted row
            weight, rest = "1", line
        ranks = [c.strip() for c in rest.split(">") if c.strip()]
        if not ranks:
            continue
        ballots.append((int(weight), ranks))
    if not ballots:
        sys.exit(f"{path}: no usable ballot rows")
    # A ranked file has at least one '>' somewhere; a score file's rows survive
    # the parse above as a single bogus "candidate" per row, so catch it here.
    if not any(len(r) > 1 for _, r in ballots):
        sys.exit(f"{path}: no ranked ballots found (no '>' in any row) — "
                 "this writes ranked (IRV) JSON only")
    return title, ballots


def tabulate(ballots):
    """Batch-elimination IRV. Returns the `results` array, transfers included."""
    active = []
    for _, ranks in ballots:
        for c in ranks:
            if c not in active:
                active.append(c)

    def tally(live):
        t = {c: 0 for c in live}
        for w, ranks in ballots:
            nxt = next((c for c in ranks if c in live), None)
            if nxt:
                t[nxt] += w
        return t

    results, rnd = [], 0
    while True:
        rnd += 1
        t = tally(active)
        total = sum(t.values())
        leader = max(t, key=lambda c: t[c])
        entry = {"round": rnd,
                 "tally": {c: str(t[c]) for c in active},   # survivors only
                 "tallyResults": []}

        if total == 0 or t[leader] * 2 > total or len(active) <= 2:
            entry["tallyResults"].append({"elected": leader, "transfers": {}})
            results.append(entry)
            return results

        # drop the trailing run that cannot reach the next survivor above it
        order = sorted(active, key=lambda c: t[c])
        losers, cum = [], 0
        for c in order:
            rest = [x for x in order if x not in losers and x != c]
            if not rest or cum + t[c] >= min(t[x] for x in rest):
                break
            losers.append(c)
            cum += t[c]
        if not losers:                      # dead tie — drop the trailing name
            losers = [order[0]]

        after = [c for c in active if c not in losers]
        moved = {L: {} for L in losers}
        for w, ranks in ballots:
            held = next((c for c in ranks if c in active), None)
            if held not in losers:
                continue
            dest = next((c for c in ranks if c in after), None) or "exhausted"
            moved[held][dest] = moved[held].get(dest, 0) + w

        for L in sorted(losers, key=lambda c: t[c]):
            entry["tallyResults"].append(
                {"eliminated": L,
                 "transfers": {k: str(v) for k, v in moved[L].items()}})
        results.append(entry)
        active = after


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("yaml")
    ap.add_argument("-o", "--out", help="output path (default: <stem>_ut.json beside the yaml)")
    args = ap.parse_args()

    title, ballots = load_case(args.yaml)
    data = {"config": {"contest": title}, "results": tabulate(ballots)}

    try:
        from rcvformats.schemas import universaltabulator
        schema = universaltabulator.SchemaV0()
        ok = (schema.validate_data(data) if hasattr(schema, "validate_data")
              else schema.validate(data))
        if not ok:
            sys.exit(f"schema rejected the output: {schema.last_error()}")
        print("schema: VALID (rcvformats universaltabulator)")
    except ImportError:
        print("schema: NOT CHECKED — pip install rcvformats to validate", file=sys.stderr)

    out = args.out or os.path.splitext(args.yaml)[0] + "_ut.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")
    for r in data["results"]:
        print(f"  round {r['round']}: " +
              ", ".join(f"{k} {v}" for k, v in r["tally"].items()))
    print("wrote", out)


if __name__ == "__main__":
    main()
