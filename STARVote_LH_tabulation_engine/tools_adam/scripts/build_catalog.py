#!/usr/bin/env python3
"""
build_catalog.py — the ONE faceted catalog of every election & race.

The other indexes each give one cut:
  * BV_registry.md      — BV-backed cases, one row per race yaml
  * multirace_elections.md — multi-race elections, grouped
  * YAML index README   — yamls grouped by method

This catalog unifies them at the two real grains and adds the facets you actually
want to slice by:

  * ELECTION grain — the container: one electorate, 1..N races, a bvid (or LH-only).
  * RACE grain     — the atom: one method, one seat count, one candidate set, one
                     ballot type, one winner set.  This is the fact table.

Derived facets per race: ballot_type (score / ranked / approval / choose-one),
seat_class (single-winner / multi-winner), character (majoritarian / proportional
/ Condorcet). Covers BOTH yaml-backed races AND BV-only races read from the frozen
exports (e.g. Bloc Plurality, which has no yaml).

Writes:
  * 00_start_here/YAML_test_case_index/races.csv        — the full sortable fact table
  * 00_start_here/YAML_test_case_index/elections.csv    — one row per election
  * 00_start_here/YAML_test_case_index/CATALOG.md       — the hub: descriptions,
        the elections table, and every facet cut, + a "how it's organized" guide.

Run: python STARVote_LH_tabulation_engine/tools_adam/scripts/build_catalog.py
"""
import csv
import glob
import json
import os
import re
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:
    yaml = None

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
IDXDIR = os.path.join(REPO, "00_start_here", "YAML_test_case_index")

EXCLUDE = ("/.venv/", "/_tabulated", "_tabulated/", "/_pages/", "_pages/",
           "/_generated", "_generated/", "/tests/", "/2_negative/",
           "/negative_cases/", "/harness_cases/", "/_demo_dropbox/")

# --- method vocabulary --------------------------------------------------------
# Canonical family so a yaml's "Bloc STAR"/"allocated" lines up with BV's
# "STAR"/"STAR_PR" from the export.
CANON = {
    "star": "STAR", "bloc star": "STAR", "bloc_star": "STAR",
    "star_pr": "STAR_PR", "allocated": "STAR_PR", "sss": "STAR_PR", "rrv": "STAR_PR",
    "approval": "Approval", "approval_multi_winner": "Approval",
    "plurality": "Plurality", "choose_one": "Plurality", "fptp": "Plurality",
    "rankedrobin": "RankedRobin", "rcv_rr": "RankedRobin", "rr": "RankedRobin",
    "copeland": "RankedRobin", "consensus": "RankedRobin",
    "irv": "IRV", "rcv_irv": "IRV", "rcv": "IRV",
    "stv": "STV", "range": "Range",
}
BALLOT_TYPE = {
    "STAR": "score", "STAR_PR": "score", "Range": "score",
    "Approval": "approval", "Plurality": "choose-one",
    "RankedRobin": "ranked", "IRV": "ranked", "STV": "ranked",
}
PROPORTIONAL = {"STAR_PR", "STV"}
CONDORCET = {"RankedRobin"}


def _canon(method):
    return CANON.get((method or "").strip().lower(), (method or "").strip() or "?")


def _character(canon, seats):
    if canon in PROPORTIONAL:
        return "proportional"
    if canon in CONDORCET:
        return "Condorcet"
    return "majoritarian"


def _seat_class(seats):
    return "single-winner" if (seats or 1) == 1 else "multi-winner"


def _ballot_shape(ballots):
    """(n_candidates, n_voters) — sums weighted rows; handles score + ranked."""
    if not isinstance(ballots, str):
        return (0, 0)
    raw = [ln.split("#", 1)[0].strip() for ln in ballots.splitlines()]
    raw = [ln for ln in raw if ln]
    if not raw:
        return (0, 0)
    w = lambda ln: (int(re.match(r"^\s*(\d+)\s*[:xX×]", ln).group(1))
                    if re.match(r"^\s*(\d+)\s*[:xX×]", ln) else 1)
    strip = lambda ln: re.sub(r"^\s*\d+\s*[:xX×]\s*", "", ln)
    if any(">" in ln for ln in raw):
        cands = set()
        for ln in raw:
            cands.update(t.strip() for t in strip(ln).split(">") if t.strip())
        return (len(cands), sum(w(ln) for ln in raw))
    ncand = len([c for c in raw[0].split(",") if c.strip()])
    return (ncand, sum(w(ln) for ln in raw[1:]))


def _rel(path):
    return os.path.relpath(path, REPO).replace(os.sep, "/")


def _sibling_eid(yaml_path):
    """bvid from a same-stem `<stem>_bv_export.json` sibling (older cases carry the
    bvid in the filename/export, not a `bv_election_id` field)."""
    exp = yaml_path[:-5] + "_bv_export.json"
    if not os.path.exists(exp):
        return None
    try:
        d = json.load(open(exp, encoding="utf-8"))
        E = d.get("Election") or d.get("election") or d
        return E.get("election_id") or None
    except Exception:
        return None


def _export_meta():
    """{election_id: {title, nvoters, races:[{canon, method, ncand, winners}]}}"""
    meta = {}
    for p in glob.glob(os.path.join(REPO, "**", "*_bv_export.json"), recursive=True):
        if any(s in "/" + _rel(p) for s in EXCLUDE):
            continue
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        E = d.get("Election") or d.get("election") or d
        eid = E.get("election_id")
        if not eid:
            continue
        races = E.get("races") or []
        results = d.get("Results") or d.get("results") or []
        rlist = []
        for i, r in enumerate(races):
            elected = []
            if i < len(results):
                elected = [e.get("name") for e in (results[i].get("elected") or [])
                           if e.get("name")]
            rlist.append({"canon": _canon(r.get("voting_method")),
                          "method": r.get("voting_method"),
                          "title": r.get("title", ""),
                          "ncand": len(r.get("candidates") or []),
                          "winners": ", ".join(elected)})
        meta[eid] = {"title": E.get("title", eid),
                     "nvoters": len(d.get("Ballots") or d.get("ballots") or []),
                     "export": _rel(p), "races": rlist}
    return meta


def collect():
    exports = _export_meta()
    races = []                       # race-grain rows
    covered = defaultdict(list)      # election_id -> [canon] seen from yamls
    for p in sorted(glob.glob(os.path.join(REPO, "**", "*.yaml"), recursive=True)):
        rel = _rel(p)
        if any(s in "/" + rel for s in EXCLUDE):
            continue
        name = os.path.basename(rel).lower()
        if any(t in name for t in ("temp", "trash", "scratch", "delete")):
            continue
        try:
            d = yaml.safe_load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        # Normalize BOTH schemas to (election title, election-level bvid, [race dicts]):
        #   flat:   top-level ballots / voting_method / num_winners / expected_winners
        #   nested: election: { races: [ {voting_method, num_winners, ballots,
        #                                 expected_results: {winners}} ] }
        if isinstance(d.get("election"), dict):
            elec = d["election"]
            etitle = elec.get("election_title", "")
            eid = (d.get("bv_election_id") or elec.get("bv_election_id")
                   or _sibling_eid(p))
            race_dicts = elec.get("races") or ([elec] if "ballots" in elec else [])
        else:
            etitle = d.get("election_title", "")
            eid = d.get("bv_election_id") or _sibling_eid(p)
            race_dicts = [d] if "ballots" in d else []
        if not race_dicts:
            continue
        election_id = eid or f"LH:{os.path.splitext(os.path.basename(rel))[0]}"
        exp = exports.get(eid) if eid else None
        for r in race_dicts:
            method = r.get("voting_method") or "STAR"
            canon = _canon(method)
            seats = int(r.get("num_winners") or 1)
            ncand, nvoters = _ballot_shape(r.get("ballots"))
            win = r.get("expected_winners")
            if win is None:
                win = (r.get("expected_results") or {}).get("winners")
            winners = ", ".join(win) if isinstance(win, list) else (win or "")
            races.append({
                "election_id": election_id,
                "election_title": (exp["title"] if exp else etitle),
                "race_title": r.get("title") or etitle or os.path.basename(rel),
                "method": method, "canon": canon,
                "ballot_type": BALLOT_TYPE.get(canon, "?"),
                "seats": seats, "seat_class": _seat_class(seats),
                "character": _character(canon, seats),
                "candidates": ncand, "voters": nvoters, "winners": winners,
                "backing": "BV" if eid else "LH-only",
                "yaml": rel,
            })
            if eid:
                covered[eid].append(canon)

    # Add BV-only races (in an export, no yaml) — e.g. Bloc Plurality.
    for eid, m in exports.items():
        seen = Counter(covered.get(eid, []))
        for r in m["races"]:
            if seen[r["canon"]] > 0:
                seen[r["canon"]] -= 1
                continue
            seats = 1
            mt = re.search(r"(\d+)\s*seat", r["title"].lower())
            seats = int(mt.group(1)) if mt else (len(r["winners"].split(",")) if r["winners"] else 1)
            races.append({
                "election_id": eid, "election_title": m["title"],
                "race_title": r["title"], "method": r["method"], "canon": r["canon"],
                "ballot_type": BALLOT_TYPE.get(r["canon"], "?"),
                "seats": seats, "seat_class": _seat_class(seats),
                "character": _character(r["canon"], seats),
                "candidates": r["ncand"], "voters": m["nvoters"],
                "winners": r["winners"], "backing": "BV (no yaml)", "yaml": "",
            })
    return races, exports


def _elections(races, exports):
    by = defaultdict(list)
    for r in races:
        by[r["election_id"]].append(r)
    rows = []
    for eid, rr in by.items():
        exp = exports.get(eid)
        title = exp["title"] if exp else rr[0]["election_title"] or rr[0]["race_title"]
        methods = sorted({r["canon"] for r in rr})
        rows.append({
            "election_id": eid,
            "title": title,
            "races": len(rr),
            "kind": "single-race" if len(rr) == 1 else "contested (multi-race)",
            "voters": max((r["voters"] for r in rr), default=0),
            "methods": ", ".join(methods),
            "backing": "BV" if not eid.startswith("LH:") else "LH-only",
        })
    rows.sort(key=lambda x: (x["kind"] != "contested (multi-race)", x["election_id"]))
    return rows


def _facet(rows, key, title, blurb):
    c = Counter(r[key] for r in rows)
    out = [f"### By {title}\n", blurb + "\n",
           f"| {title} | # races | example elections |", "|---|--:|---|"]
    ex = defaultdict(set)
    for r in rows:
        ex[r[key]].add(r["election_id"].replace("LH:", ""))
    for val, n in c.most_common():
        examples = ", ".join(sorted(ex[val])[:4])
        out.append(f"| {val} | {n} | {examples} |")
    return "\n".join(out) + "\n"


def main():
    if yaml is None:
        raise SystemExit("pyyaml required")
    races, exports = collect()
    elections = _elections(races, exports)

    os.makedirs(IDXDIR, exist_ok=True)
    # races.csv
    cols = ["election_id", "election_title", "race_title", "method", "canon",
            "ballot_type", "seats", "seat_class", "character", "candidates",
            "voters", "winners", "backing", "yaml"]
    with open(os.path.join(IDXDIR, "races.csv"), "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=cols)
        wr.writeheader()
        wr.writerows(sorted(races, key=lambda r: (r["election_id"], r["race_title"])))
    # elections.csv
    with open(os.path.join(IDXDIR, "elections.csv"), "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=["election_id", "title", "races", "kind",
                                            "voters", "methods", "backing"])
        wr.writeheader()
        wr.writerows(elections)

    # CATALOG.md
    M = []
    M.append("# Test-case catalog — slice the elections & races every way\n")
    M.append("*Generated — do not edit by hand. Regenerate: "
             "`python STARVote_LH_tabulation_engine/tools_adam/scripts/build_catalog.py`.*\n")
    M.append("Two grains underlie every view here:\n")
    M.append("- **Election** = the container: one electorate casting into **1..N races**, "
             "with a `bvid` (or LH-only). *Single-race* = one contest; *contested* = several.\n"
             "- **Race** = the atom that gets tabulated: exactly **one method, one seat "
             "count, one candidate set, one ballot type, one winner set**. This is the fact "
             "table ([`races.csv`](races.csv)).\n")
    M.append("Each race carries derived facets so you can slice: **ballot type** "
             "(score / ranked / approval / choose-one), **seat class** (single- vs "
             "multi-winner), and **character** (majoritarian / proportional / Condorcet). "
             "BV-only races with no yaml (e.g. Bloc Plurality) are pulled in from the "
             "frozen exports.\n")
    M.append(f"**Totals:** {len(elections)} elections, {len(races)} races. "
             "Full drill-down: [`races.csv`](races.csv) · [`elections.csv`](elections.csv). "
             "Related: [BV registry](BV_registry.md) · "
             "[multi-race index](multirace_elections.md) · [by method](README.md).\n")

    M.append("## Elections\n")
    M.append("| Election | Title | Races | Kind | Voters | Methods | Backing |")
    M.append("|---|---|--:|---|--:|---|---|")
    for e in elections:
        eid = e["election_id"].replace("LH:", "")
        M.append(f"| {eid} | {e['title'][:52]} | {e['races']} | {e['kind']} | "
                 f"{e['voters']} | {e['methods']} | {e['backing']} |")
    M.append("")

    M.append("## Cuts\n")
    M.append("Counts per facet with example elections; drill into [`races.csv`](races.csv) "
             "to filter/sort the full set (GitHub renders CSV with sortable, filterable "
             "columns — it's the closest thing to a database view).\n")
    # single vs multi-race is an election property; show it as a race facet via election kind
    kind_by_race = []
    ekind = {e["election_id"]: e["kind"] for e in elections}
    for r in races:
        rr = dict(r); rr["election_kind"] = ekind.get(r["election_id"], "single-race")
        kind_by_race.append(rr)
    M.append(_facet(kind_by_race, "election_kind", "single vs multi-race",
                    "Whether a race sits in a single-contest election or a **contested** "
                    "(multi-race) one — same electorate, several races."))
    M.append(_facet(races, "seat_class", "seat class",
                    "**Single-winner** (num_winners = 1) vs **multi-winner** (a body of seats)."))
    M.append(_facet(races, "ballot_type", "ballot type",
                    "What the voter marks: **score** (0–5), **ranked** (A>B>C), "
                    "**approval** (0/1), or **choose-one**."))
    M.append(_facet(races, "character", "character",
                    "A rough teaching cut: **majoritarian** (a majority can take every "
                    "seat), **proportional** (seats track factions — STAR-PR, STV), or "
                    "**Condorcet** (elects the pairwise winner — Ranked Robin)."))
    M.append(_facet(races, "canon", "method (family)",
                    "Canonical method family — e.g. Bloc STAR and STAR both normalize to "
                    "STAR; allocated/sss/rrv to STAR_PR."))
    M.append(_facet(races, "backing", "backing (BV vs LH-only)",
                    "**BV** = reproduced on BetterVoting (has a frozen export). "
                    "**LH-only** = tabulated only by our engine. Goal: keep LH-only near "
                    "zero — reproduce cases on BV unless BV genuinely can't (e.g. a "
                    "deterministic tie-break BV resolves at random). Filter "
                    "`races.csv` by `backing=LH-only` to find migration candidates."))

    M.append("## How this is organized (for adding cases)\n")
    M.append(
        "- **One yaml = one race.** A single-race election is one yaml; a **contested "
        "election is several yamls that share `bv_election_id`** (its bvid). The catalog "
        "groups them by that id.\n"
        "- **Facets are DERIVED, not hand-tagged** — from `voting_method` (→ family + "
        "ballot type + character) and `num_winners` (→ seat class). So a case shows up in "
        "the right cuts automatically; just set those two fields correctly.\n"
        "- **BV-only races** (a race that exists on BetterVoting but has no LH yaml, e.g. "
        "Bloc Plurality) are read from the frozen `*_bv_export.json` and appear tagged "
        "`BV (no yaml)`.\n"
        "- **Naming:** BV-backed case files carry the bvid (`bv<testid>_<bvid>_<descriptor>`); "
        "LH-only files use a descriptive name. A contested election keeps its races in one "
        "folder with a lead `.md` and a `README.md`.\n"
        "- **To add a case:** drop the yaml(s), run the engine (writes the `_tabulated` "
        "mirror), then regenerate the indexes (`build_yaml_pages`, `build_bv_registry`, "
        "`build_multirace_index`, `build_catalog`). The pre-commit hook refreshes the "
        "generated indexes automatically.\n")

    with open(os.path.join(IDXDIR, "CATALOG.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(m for m in M if m is not None) + "\n")
    print(f"wrote CATALOG.md, races.csv ({len(races)} races), "
          f"elections.csv ({len(elections)} elections)")


if __name__ == "__main__":
    main()
