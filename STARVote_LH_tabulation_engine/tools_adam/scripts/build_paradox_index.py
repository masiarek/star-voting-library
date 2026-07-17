#!/usr/bin/env python3
"""
build_paradox_index.py — group the repo's test cases by voting paradox.

Scans the teaching/test YAML files for a top-level `paradoxes: [tag, …]` list
(the tabulation engine ignores the field) and regenerates:

  * 00_start_here/YAML_test_case_index/PARADOX_index.md — cases grouped by
    paradox, each linked to its teaching page in 00_start_here/voting_paradoxes/
    (when one exists) and to the case's reader-friendly .md page (the sibling
    two-view page if present, else the generated <set>_pages page), with the
    raw .yaml demoted to the last column per house link style.
  * 00_start_here/YAML_test_case_index/paradox_cases.csv — the same, flat.

TAG VOCABULARY IS CONTROLLED. Tags must come from VOCAB below; unknown tags are
reported loudly (and listed in a trailing section so nothing silently drops).
To add a paradox: add a VOCAB entry (display name, Felsenthal kind, teaching
page or None, one-line definition), then tag the case YAMLs.

Run from the repo root:
    python STARVote_LH_tabulation_engine/tools_adam/scripts/build_paradox_index.py
"""

import csv
import os
import re
import sys

import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT_DIR = os.path.join(REPO, "00_start_here", "YAML_test_case_index")
OUT_MD = os.path.join(OUT_DIR, "PARADOX_index.md")
OUT_CSV = os.path.join(OUT_DIR, "paradox_cases.csv")
PAGES_DIR = "00_start_here/voting_paradoxes"

EXCLUDE = ("_tabulated", "_generated", "_demo_dropbox", "/tests/", "/negative",
           "/2_negative", "harness_cases", "trash_delete",
           "/site/")  # mkdocs build output (mirrors the whole repo)

# tag -> (display name, Felsenthal kind, teaching page filename or None, definition)
VOCAB = {
    "condorcet-winner": ("Condorcet winner paradox", "Simple",
                         "condorcet_winner_paradox.md",
                         "The candidate who beats every rival head-to-head is not elected (a.k.a. thwarted majorities; center squeeze is the IRV route)."),
    "condorcet-loser": ("Condorcet loser paradox", "Simple",
                        "condorcet_loser_paradox.md",
                        "The candidate who loses to every rival head-to-head is elected (a.k.a. Borda's paradox)."),
    "absolute-loser": ("Absolute loser paradox", "Simple",
                       "absolute_loser_paradox.md",
                       "A candidate ranked last by an outright majority is elected."),
    "spoiler-scc": ("SCC / spoiler", "Conditional",
                    "spoiler_scc.md",
                    "A candidate who cannot win enters or leaves the race and the winner changes."),
    "condorcet-cycle": ("Condorcet's paradox (cycle)", "Simple", None,
                        "Pairwise majorities form a cycle; no Condorcet winner exists."),
    "non-monotonicity": ("Non-monotonicity", "Conditional", "non_monotonicity.md",
                         "Ranking/scoring a candidate HIGHER makes them lose (or lower makes them win); a.k.a. more-is-less, additional-support paradox."),
    "no-show": ("No-show paradox", "Conditional", "no_show.md",
                "Voters do better by staying home: adding ballots ranking X last can make X win."),
    "twin": ("Twin paradox (weak form)", "Conditional", "no_show.md",
             "Voters are made worse off by the arrival of 'twins' — added voters with an identical preference ordering."),
    "truncation": ("Truncation paradox", "Conditional", "truncation.md",
                   "Ranking fewer candidates gives a voter a better outcome than ranking all."),
    "clone-teaming": ("Clone dependence / teaming", "Conditional", None,
                      "Adding a near-copy of a candidate changes who wins (teaming = doing it on purpose)."),
    "favorite-betrayal": ("Favorite betrayal", "Conditional", None,
                          "A voter gets a better result by ranking/scoring their true favorite below another candidate."),
    "multiple-districts": ("Reinforcement / multiple-districts paradox", "Conditional", "multiple_districts.md",
                           "A candidate wins in every district separately but loses the combined election (a.k.a. inconsistency paradox)."),
    "majority-failure": ("Majority criterion failure", "Simple", None,
                         "A candidate who is the first choice of an absolute majority is not elected (Felsenthal's Absolute Majority paradox)."),
    "pareto": ("Pareto-dominated winner", "Simple", None,
               "A candidate is (or can be) elected although EVERY voter prefers some other candidate."),
}


def find_yamls():
    hits = []
    for root, dirs, files in os.walk(REPO):
        rel_root = os.path.relpath(root, REPO)
        if rel_root.startswith("."):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
        path_l = ("/" + rel_root.replace(os.sep, "/") + "/").lower()
        if any(x in path_l for x in EXCLUDE):
            dirs[:] = []
            continue
        for f in files:
            if f.endswith((".yaml", ".yml")) and not any(x in f.lower() for x in EXCLUDE):
                hits.append(os.path.join(root, f))
    return sorted(hits)


def load_case(path):
    try:
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
    except Exception as ex:
        print(f"  ⚠ unparseable YAML skipped: {os.path.relpath(path, REPO)} ({ex.__class__.__name__})")
        return None
    if not isinstance(doc, dict):
        return None
    tags = doc.get("paradoxes")
    if not tags:
        return None
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    # Flat schema fields, with a nested-schema fallback for title/method.
    title = doc.get("election_title")
    method = doc.get("voting_method")
    winners = doc.get("expected_winners")
    if title is None and isinstance(doc.get("election"), dict):
        e = doc["election"]
        title = e.get("election_title")
        races = e.get("races") or []
        if races and isinstance(races[0], dict):
            method = races[0].get("voting_method")
            ew = races[0].get("expected_results") or {}
            winners = ew.get("winners")
    return {
        "path": os.path.relpath(path, REPO).replace(os.sep, "/"),
        "tags": [str(t) for t in tags],
        "title": title or os.path.basename(path),
        "method": method or "?",
        "winners": ", ".join(winners) if isinstance(winners, list) else (winners or ""),
        "bvid": doc.get("bv_election_id") or "",
        "test_id": doc.get("bv_test_id") or "",
    }


def best_page(rel_yaml):
    """Reader-friendly page for a case: sibling .md > generated _pages .md > None."""
    d, base = os.path.split(rel_yaml)
    stem = os.path.splitext(base)[0]
    sibling = f"{d}/{stem}.md"
    if os.path.exists(os.path.join(REPO, sibling)):
        return sibling
    gen = f"{d}/{os.path.basename(d)}_pages/{stem}.md"
    if os.path.exists(os.path.join(REPO, gen)):
        return gen
    # Set-level two-view page (multi-race exports share one .md, e.g. bv2137):
    m = re.match(r"(bv\w+_\w+)_", stem)
    if m:
        for f in sorted(os.listdir(os.path.join(REPO, d))):
            if f.startswith(m.group(1)) and f.endswith(".md"):
                return f"{d}/{f}"
    return None


def rel_from_index(rel):
    """Path relative to OUT_DIR (00_start_here/YAML_test_case_index/)."""
    return os.path.relpath(os.path.join(REPO, rel), OUT_DIR).replace(os.sep, "/")


def main():
    cases = [c for c in (load_case(p) for p in find_yamls()) if c]
    by_tag, unknown = {}, {}
    for c in cases:
        for t in c["tags"]:
            (by_tag if t in VOCAB else unknown).setdefault(t, []).append(c)

    for t in unknown:
        print(f"  ⚠ UNKNOWN paradox tag {t!r} — add it to VOCAB or fix the YAML "
              f"({', '.join(c['path'] for c in unknown[t])})")

    lines = [
        "# Paradox index — test cases grouped by voting paradox",
        "",
        "Auto-generated by `tools_adam/scripts/build_paradox_index.py` from each case YAML's `paradoxes:` tags — do not edit by hand. "
        "Taxonomy and teaching pages: [voting_paradoxes/README.md](../voting_paradoxes/README.md).",
        "",
        f"**{len(cases)} tagged case(s), {len(by_tag)} paradox(es).**",
        "",
    ]
    for tag in sorted(by_tag, key=lambda t: list(VOCAB).index(t)):
        display, kind, page, definition = VOCAB[tag]
        head = f"## {display}"
        if page:
            head = f"## [{display}](../voting_paradoxes/{page})"
        lines += [head, "", f"*{kind} paradox (Felsenthal).* {definition}", "",
                  "| Case | Method | Expected winner(s) | BV | YAML |", "|---|---|---|---|---|"]
        for c in sorted(by_tag[tag], key=lambda c: c["path"]):
            page_rel = best_page(c["path"])
            name = c["title"]
            case_cell = f"[{name}]({rel_from_index(page_rel)})" if page_rel else name
            bv = (f"[{c['test_id'] or c['bvid']}](https://bettervoting.com/{c['bvid']}/results)"
                  if c["bvid"] else "—")
            lines.append(f"| {case_cell} | {c['method']} | {c['winners'] or '—'} | {bv} "
                         f"| [{os.path.basename(c['path'])}]({rel_from_index(c['path'])}) |")
        lines.append("")
    if unknown:
        lines += ["## ⚠ Unrecognized tags", ""]
        for t, cs in sorted(unknown.items()):
            lines.append(f"- `{t}`: " + ", ".join(f"`{c['path']}`" for c in cs))
        lines.append("")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["paradox", "kind", "case_title", "method", "expected_winners",
                    "bv_test_id", "bv_election_id", "yaml_path"])
        for tag in sorted(by_tag, key=lambda t: list(VOCAB).index(t)):
            display, kind, _pg, _d = VOCAB[tag]
            for c in sorted(by_tag[tag], key=lambda c: c["path"]):
                w.writerow([display, kind, c["title"], c["method"], c["winners"],
                            c["test_id"], c["bvid"], c["path"]])
    print(f"wrote {os.path.relpath(OUT_MD, REPO)} and paradox_cases.csv "
          f"({len(cases)} cases, {len(by_tag)} paradoxes, {len(unknown)} unknown tags)")
    return 1 if unknown else 0


if __name__ == "__main__":
    sys.exit(main())
