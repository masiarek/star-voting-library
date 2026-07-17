#!/usr/bin/env python3
"""
build_multirace_index.py — a register of MULTI-RACE (contested) BV elections.

The per-case BV registry (build_bv_registry.py) has one row per race, so a
multi-race election (one ballot, several contests / methods) scatters across
several rows with no grouping. This index fixes that: it scans the frozen
`*_bv_export.json` files, keeps the elections that have MORE THAN ONE race, and
writes a grouped view — one block per election, one line per race — answering
"which elections are contested, and for each race: what method, how many
candidates, how many ballots, who won?".

Source of truth is the frozen export (Election.races[], Ballots[], Results[]),
not the YAMLs, so the ballot count is the real voter count (not line count).

Writes:  00_start_here/YAML_test_case_index/multirace_elections.md
Run:     python STARVote_LH_tabulation_engine/tools_adam/scripts/build_multirace_index.py
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(REPO, "00_start_here", "YAML_test_case_index", "multirace_elections.md")


def _find_exports():
    hits = []
    for p in glob.glob(os.path.join(REPO, "**", "*_bv_export.json"), recursive=True):
        if "/.venv/" in p or "/_demo_dropbox/" in p or "/site/" in p:
            continue  # /site/ = mkdocs build output (mirrors the whole repo)
        hits.append(p)
    return sorted(hits)


def _load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return None


def _election(d):
    return d.get("Election") or d.get("election") or d


def _winners_by_race(results):
    """Map race_id -> winner name(s) from the Results list (best-effort)."""
    out = {}
    for res in results or []:
        el = [e.get("name") for e in (res.get("elected") or []) if e.get("name")]
        # Results entries don't always carry race_id; fall back to positional.
        out[res.get("race_id")] = ", ".join(el) if el else "?"
    return out


def _test_id(elec, path):
    m = re.search(r"\bBV\w+\b", elec.get("title", ""))
    if m:
        return m.group(0)
    m = re.match(r"bv([0-9]+[a-z]?)", os.path.basename(path))
    return "BV" + m.group(1) if m else "—"


def main():
    rows = []
    for path in _find_exports():
        d = _load(path)
        if not d:
            continue
        elec = _election(d)
        races = elec.get("races") or []
        if len(races) < 2:
            continue                      # single-race elections belong in the main registry
        ballots = d.get("Ballots") or d.get("ballots") or []
        results = d.get("Results") or d.get("results") or []
        win = _winners_by_race(results)
        # positional winner fallback when race_id keys are absent/misaligned
        pos = [", ".join(e.get("name") for e in (r.get("elected") or []) if e.get("name")) or "?"
               for r in results]
        eid = elec.get("election_id", "?")
        rows.append({
            "eid": eid,
            "test_id": _test_id(elec, path),
            "title": elec.get("title", "?"),
            "nballots": len(ballots),
            "races": [
                {
                    "title": r.get("title", "?"),
                    "method": r.get("voting_method", "?"),
                    "ncand": len(r.get("candidates") or []),
                    "winner": win.get(r.get("race_id")) or (pos[i] if i < len(pos) else "?"),
                }
                for i, r in enumerate(races)
            ],
            "rel": os.path.relpath(path, os.path.dirname(OUT)),
        })

    lines = [
        "# Multi-race (contested) BV elections",
        "",
        "*Generated — do not edit by hand. Regenerate: "
        "`python STARVote_LH_tabulation_engine/tools_adam/scripts/build_multirace_index.py`.*",
        "",
        "Elections with **more than one race** (several contests / methods on one "
        "ballot). One block per election; ballot count is the real voter count from "
        "the frozen export. Single-race elections live in "
        "[BV_registry.md](BV_registry.md).",
        "",
    ]
    if not rows:
        lines += ["_No multi-race elections found._", ""]
    for r in sorted(rows, key=lambda x: x["test_id"]):
        # Don't repeat the Test ID if the title already leads with it.
        head = r["title"] if r["title"].startswith(r["test_id"]) else f"{r['test_id']} — {r['title']}"
        lines.append(f"## {head}")
        lines.append("")
        lines.append(f"**Election** [`{r['eid']}`](https://bettervoting.com/{r['eid']}/results) "
                     f"· **{len(r['races'])} races** · **{r['nballots']} ballots** · "
                     f"[frozen export]({r['rel']})")
        lines.append("")
        lines.append("| Race | Method | Candidates | Winner |")
        lines.append("|------|--------|:----------:|--------|")
        for rc in r["races"]:
            lines.append(f"| {rc['title']} | {rc['method']} | {rc['ncand']} | **{rc['winner']}** |")
        lines.append("")

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {os.path.relpath(OUT, REPO)} "
          f"({len(rows)} multi-race election(s))")


if __name__ == "__main__":
    main()
