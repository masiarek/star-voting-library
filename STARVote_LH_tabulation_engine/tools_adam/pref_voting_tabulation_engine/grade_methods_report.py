#!/usr/bin/env python3
"""
grade_methods_report.py — RANGE VOTING (the mean) and MAJORITY JUDGMENT (the median).

Why this exists: Felsenthal's Appendices A8 and A9 put two grade-ballot procedures on
trial, and neither could be counted here. Range Voting grades 1-10 and Majority
Judgment grades on letters A-J; the LH engine's YAML path validates scores against
`max_score=5` because STAR ballots are 0-5 by convention, so neither table can go
through it, and BetterVoting implements neither method. So
`07_Concepts/voting_paradoxes/range_voting.md` and `majority_judgment.md` could only
assert their examples in prose.

  * **Range Voting (RV)** — every voter grades every candidate on a cardinal scale;
    the highest MEAN grade wins.
  * **Majority Judgment (MJ)** — Balinski & Laraki's rule: the highest MEDIAN grade
    wins. When medians tie, one instance of the shared median is removed from each
    tied candidate and the medians are recomputed, repeatedly, until they separate.

Both are counted here from scratch and then cross-checked against Eric Pacuit's
`pref_voting` (`score_voting` and `majority_judgement` over a `GradeProfile`), so
every number is computed twice by independent code.

**The file format is Felsenthal's table, transposed as little as possible** — a
`grades:` block whose header row names the voters and whose remaining rows are one
candidate each:

    grade_scale: "1-10"        # or "A-H"; for letters, LATER letters are HIGHER
    grades: |-
      ,V1,V2,V3,V4,V5
      x,2,2,2,3,10
      y,1,1,1,10,7

A blank cell means the voter did not grade that candidate. **Under both procedures an
ungraded candidate takes the LOWEST grade on the scale** — that convention is not
incidental, it is the entire mechanism of the truncation paradox in Examples 24 and
28, so the report says how many cells it filled in and what it filled them with.

Because this format is not the LH engine's `ballots:` block, these files are not
election YAMLs and get no `_tabulated` mirror or generated page; the concept pages
carry the count instead.

Usage:
    uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/grade_methods_report.py FILE.yaml
    uv run ... grade_methods_report.py --ungraded VOTER FILE.yaml   # truncation: drop one voter's grades
"""
import os
import statistics
import sys

import yaml


def _scale(spec):
    """'1-10' -> [1..10] as ints; 'A-H' -> ['A'..'H']; a pipe-separated list ->
    those words. Lowest first, highest last.

    The word form is what Majority Judgment actually asks for. Balinski & Laraki's
    argument is not "grade on six levels" but that the levels are a COMMON
    LANGUAGE — Excellent, Very Good, Good, Acceptable, Poor, To Reject — whose
    shared meaning is what supplies the interpersonal comparability a numeric
    score can't. Felsenthal's examples happen to use letters, so letters were all
    this tool needed at first; a file that teaches the method wants the words.
    """
    spec = str(spec).strip()
    if "|" in spec:
        words = [w.strip() for w in spec.split("|") if w.strip()]
        if len(words) < 2:
            raise SystemExit(f"grade_scale {spec!r} needs at least two grades")
        return words
    lo, _, hi = spec.partition("-")
    lo, hi = lo.strip(), hi.strip()
    if lo.isdigit() and hi.isdigit():
        return list(range(int(lo), int(hi) + 1))
    if len(lo) == 1 and len(hi) == 1 and lo.isalpha() and hi.isalpha():
        return [chr(c) for c in range(ord(lo.upper()), ord(hi.upper()) + 1)]
    raise SystemExit(f"grade_scale {spec!r} must look like '1-10', 'A-H', "
                     f"or 'To Reject|Poor|…|Excellent'")


def parse_grade_file(path, ungrade=(), abstain=()):
    """(voters, candidates, {cand: {voter: grade}}, scale, filled) from a grade YAML.

    Two distinct levers, because Felsenthal's examples use both and they are not the
    same thing:

      * `ungrade` — a set of "CAND/VOTER" cells to strike. The voter still votes and
        still grades everyone else; they simply decline to grade this one candidate,
        who then takes the scale floor. This is TRUNCATION (Examples 24 and 28).
      * `abstain` — voters removed from the electorate entirely. This is a NO-SHOW
        (Example 27), and it changes the denominator, which is exactly why it can
        move a median.

    `filled` lists the (cand, voter) cells that ended up at the scale floor without a
    grade being written for them — blanks in the file plus anything `ungrade` struck."""
    data = yaml.safe_load(open(path, encoding="utf-8"))
    if "grades" not in data:
        raise SystemExit(f"{path}: no `grades:` block — this is not a grade-ballot file")
    scale = _scale(data.get("grade_scale", "1-10"))
    lines = [l for l in data["grades"].splitlines() if l.strip()]
    voters = [c.strip() for c in lines[0].split(",")][1:]
    for v in abstain:
        if v not in voters:
            raise SystemExit(f"--abstain {v!r}: no such voter (have: {', '.join(voters)})")
    struck = set()
    for spec in ungrade:
        if "/" not in spec:
            raise SystemExit(f"--ungrade {spec!r} must be CANDIDATE/VOTER, e.g. y/V4")
        struck.add(tuple(s.strip() for s in spec.split("/", 1)))
    voters = [v for v in voters if v not in abstain]
    cands, grades, filled = [], {}, []
    for line in lines[1:]:
        cells = [c.strip() for c in line.split(",")]
        cand, cells = cells[0], cells[1:]
        header = [c.strip() for c in lines[0].split(",")][1:]
        if len(cells) != len(header):
            raise SystemExit(f"{path}: row {cand!r} has {len(cells)} grades but the "
                             f"header names {len(header)} voters")
        cands.append(cand)
        row = {}
        for v, cell in zip(header, cells):
            if v not in voters:
                continue
            if not cell or (cand, v) in struck:
                row[v] = scale[0]
                filled.append((cand, v))
            else:
                # Matched case-insensitively and stored as the scale spells it, so
                # "very good" and "Very Good" are the same grade and the report
                # prints one of them.
                canon = {str(g).upper(): g for g in scale}
                val = int(cell) if cell.lstrip("-").isdigit() else canon.get(cell.upper())
                if val not in scale:
                    raise SystemExit(f"{path}: grade {cell!r} for {cand}/{v} is not on "
                                     f"the {data.get('grade_scale')} scale")
                row[v] = val
        grades[cand] = row
    unknown = [f"{c}/{v}" for c, v in struck if c not in cands]
    if unknown:
        raise SystemExit(f"--ungrade names unknown candidate(s): {', '.join(unknown)}")
    return voters, cands, grades, scale, filled


def _mj_winner(cands, grades, voters, scale):
    """Majority Judgment: highest median, Balinski-Laraki tie-break. Returns
    (winners, rounds) where rounds records each tie-break iteration."""
    rank = {g: i for i, g in enumerate(scale)}
    pools = {c: sorted((grades[c][v] for v in voters), key=lambda g: rank[g])
             for c in cands}
    alive = list(cands)
    rounds = []
    while True:
        meds = {c: pools[c][(len(pools[c]) - 1) // 2] for c in alive}
        best = max(meds.values(), key=lambda g: rank[g])
        top = [c for c in alive if meds[c] == best]
        rounds.append((dict(meds), list(top)))
        if len(top) == 1:
            return top, rounds
        if all(len(pools[c]) <= 1 for c in top):
            return sorted(top), rounds          # genuinely tied, no further split
        alive = top
        # Remove ONE instance of the shared median from each tied candidate.
        for c in alive:
            p = pools[c]
            p.pop((len(p) - 1) // 2)


def report(path, ungrade=(), abstain=()):
    voters, cands, grades, scale, filled = parse_grade_file(
        path, ungrade=ungrade, abstain=abstain)
    rank = {g: i for i, g in enumerate(scale)}
    n = len(voters)

    out = []
    out.append("=== Range Voting (mean) and Majority Judgment (median) ===")
    bits = []
    if abstain:
        bits.append(f"{', '.join(abstain)} ABSTAINED")
    if ungrade:
        bits.append(f"{', '.join(ungrade)} UNGRADED")
    note = f", {'; '.join(bits)}" if bits else ""
    out.append(f" {n} voters, {len(cands)} candidates, grades "
               f"{scale[0]}–{scale[-1]}{note}.\n")

    # --- The table, as the source prints it. ---
    w = max(len(c) for c in cands) + 2
    # Column width follows the widest thing that goes in it — "Very Good" is a
    # grade, not an overflow.
    gw = max(6, max(len(str(g)) for g in scale) + 2, max(len(v) for v in voters) + 2)
    mw = max(8, max(len(str(g)) for g in scale) + 2)
    out.append("Grades:")
    out.append("   " + "".join([f"{'':<{w}}"] + [f"{v:>{gw}}" for v in voters])
               + f"{'mean':>9}{'median':>{mw}}")
    for c in cands:
        row = [grades[c][v] for v in voters]
        mean = statistics.mean(rank[g] for g in row) if isinstance(scale[0], str) \
            else statistics.mean(row)
        med = sorted(row, key=lambda g: rank[g])[(n - 1) // 2]
        shown = f"{mean:.3f}" if not isinstance(scale[0], str) else f"({mean:.2f})"
        out.append("   " + "".join([f"{c:<{w}}"] + [f"{str(g):>{gw}}" for g in row])
                   + f"{shown:>9}{str(med):>{mw}}")
    out.append("")
    if filled:
        cells = ", ".join(f"{c}/{v}" for c, v in filled)
        out.append(f" {len(filled)} ungraded cell(s) took the scale floor "
                   f"({scale[0]}): {cells}.")
        out.append(" That convention — ungraded equals lowest — is what makes "
                   "truncation profitable under both rules.\n")

    # --- Range Voting: the mean. ---
    means = {c: statistics.mean(rank[grades[c][v]] for v in voters) for c in cands}
    rv_best = max(means.values())
    rv = sorted(c for c in cands if means[c] == rv_best)
    out.append(f"Winner — Range Voting (highest mean): {' / '.join(rv)}")
    if isinstance(scale[0], str):
        out.append(f"   (grades scored by position on the scale, {scale[0]}=0)")
    out.append("")

    # --- Majority Judgment: the median, then Balinski-Laraki. ---
    mj, rounds = _mj_winner(cands, grades, voters, scale)
    out.append(f"Winner — Majority Judgment (highest median): {' / '.join(mj)}")
    for i, (meds, top) in enumerate(rounds):
        shown = ", ".join(f"{c} {meds[c]}" for c in sorted(meds))
        if i == 0:
            out.append(f"   medians: {shown}")
        else:
            out.append(f"   tie-break {i}: {shown}")
    if len(rounds) > 1:
        out.append(f"   {len(rounds) - 1} Balinski-Laraki iteration(s) were needed — the "
                   "medians tied and one instance of the shared median was dropped from "
                   "each tied candidate until they separated.")
    if len(mj) > 1:
        out.append("   ⚠️  still tied after the tie-break is exhausted — no winner.")
    out.append("")

    # --- What a majority actually thinks, which is what these examples indict. ---
    #
    # This used to run only on a two-candidate file, because Felsenthal's §A8/§A9
    # examples all happen to be two-candidate. That silently exempted every
    # teaching case with a real field: `mj_vs_score_c3_b5` was built, published
    # and reviewed before anyone noticed by hand that Majority Judgment elects
    # Asha there while Bodhi beats her head-to-head 3–2. A page comparing two
    # grade rules has to say when one of them overrules a majority, so the check
    # now runs at any size.
    def _above(x, y):
        return sum(1 for v in voters if rank[grades[x][v]] > rank[grades[y][v]])

    if len(cands) == 2:
        x, y = cands
        fx, fy = _above(x, y), _above(y, x)
        out.append(f"Head-to-head — how many voters graded each ABOVE the other:")
        out.append(f"   {x} above {y}: {fx}      {y} above {x}: {fy}"
                   f"      (equal: {n - fx - fy})")
        maj = max((x, fx), (y, fy), key=lambda t: t[1])
        if maj[1] > n / 2:
            loser = y if maj[0] == x else x
            out.append(f"   {maj[0]} is the Condorcet winner ({maj[1]} of {n}), "
                       f"{loser} the Condorcet loser.")
            for rule, w_ in (("Range Voting", rv), ("Majority Judgment", mj)):
                if maj[0] not in w_:
                    out.append(f"   ⚠️  {rule} elects {' / '.join(w_)} — the Condorcet "
                               f"LOSER. An absolute majority is overruled.")
    else:
        out.append("Head-to-head — every pair, by how many voters graded one "
                   "ABOVE the other:")
        beats = {c: 0 for c in cands}
        for i, x in enumerate(cands):
            for y in cands[i + 1:]:
                fx, fy = _above(x, y), _above(y, x)
                if fx > fy:
                    beats[x] += 1
                    out.append(f"   {x} beats {y}   {fx}–{fy}")
                elif fy > fx:
                    beats[y] += 1
                    out.append(f"   {y} beats {x}   {fy}–{fx}")
                else:
                    out.append(f"   {x} ties {y}   {fx}–{fy}")
        cw = [c for c in cands if beats[c] == len(cands) - 1]
        if cw:
            out.append(f"   {cw[0]} is the Condorcet winner — beats every rival "
                       f"head-to-head.")
            for rule, w_ in (("Range Voting", rv), ("Majority Judgment", mj)):
                if cw[0] not in w_:
                    lost = " / ".join(w_)
                    out.append(f"   ⚠️  {rule} elects {lost} — NOT the Condorcet "
                               f"winner. {cw[0]} beats {lost} head-to-head.")
        else:
            out.append("   No Condorcet winner — the pairwise results cycle.")

    # Absolute winner / loser: a majority putting a candidate at the scale's edge.
    for c in cands:
        top_ct = sum(1 for v in voters if grades[c][v] == scale[-1])
        bot_ct = sum(1 for v in voters if grades[c][v] == scale[0])
        if bot_ct > n / 2:
            out.append(f"   {c} is the ABSOLUTE LOSER — {bot_ct} of {n} gave the "
                       f"lowest possible grade ({scale[0]}).")
        if top_ct > n / 2:
            out.append(f"   {c} is the ABSOLUTE WINNER — {top_ct} of {n} gave the "
                       f"highest possible grade ({scale[-1]}).")
    out.append("")

    # --- Independent second computation. Loud when skipped, never silently. ---
    try:
        from pref_voting.grade_profiles import GradeProfile
        from pref_voting.grade_methods import score_voting, majority_judgement
    except Exception:
        out.append(" [pref_voting cross-check SKIPPED — library not installed. "
                   "Run `uv sync` (pref_voting is declared in pyproject.toml).]")
        return "\n".join(out)
    try:
        gmaps = [{c: rank[grades[c][v]] for c in cands} for v in voters]
        prof = GradeProfile(gmaps, list(range(len(scale))), candidates=list(cands))
        pv_rv = sorted(score_voting(prof))
        pv_mj = sorted(majority_judgement(prof))
    except Exception as ex:
        out.append(f" [pref_voting cross-check ERROR: {ex!r}]")
        return "\n".join(out)

    for label, mine, theirs in (("Range (mean)", rv, pv_rv),
                                ("Majority Judgment", mj, pv_mj)):
        status = "AGREE ✓" if mine == theirs else "DISAGREE ✗  — INVESTIGATE"
        out.append(f" pref_voting {label}: {', '.join(theirs)}   "
                   f"vs this report ({', '.join(mine)}): {status}")
    return "\n".join(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    ungrade, abstain = [], []
    if "--ungrade" in args:
        i = args.index("--ungrade")
        ungrade = [s.strip() for s in args[i + 1].split(",") if s.strip()]
        del args[i:i + 2]
    if "--abstain" in args:
        i = args.index("--abstain")
        abstain = [s.strip() for s in args[i + 1].split(",") if s.strip()]
        del args[i:i + 2]
    if not args:
        sys.exit("usage: python grade_methods_report.py [--ungrade CAND/VOTER,...] "
                 "[--abstain VOTER,...] FILE.yaml [FILE2.yaml ...]")
    for p in args:
        print(report(p, ungrade=ungrade, abstain=abstain))
        print()
