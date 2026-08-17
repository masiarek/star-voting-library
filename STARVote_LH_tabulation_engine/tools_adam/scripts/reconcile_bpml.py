#!/usr/bin/env python3
"""Reconcile BetterVoting's BPML process sheet against this repo's BV case registry.

Three inventories track BetterVoting test coverage, and until now none of them knew
about the others:

  1. the **BPML sheet** (Drive) -- one row per L1/L2/L3 business process, with a
     "Test Case" column that sometimes names a BVxxx id;
  2. the **Test Cases sheet** (Drive) -- the manual QA log, one row per BVxxx with
     a pass/fail status;
  3. **bv_cases.csv** (this repo) -- every BV-backed election that exists as a
     runnable YAML case with a published answer key.

"Do we have coverage?" is a join across all three, and nobody had run it. This
script runs it and writes RECONCILIATION.md next to the snapshots.

The two Drive sheets cannot be read from CI, so they are committed here as dated
CSV **snapshots**. They are point-in-time copies, not a live feed -- the header of
the generated page says so, and re-snapshotting is a manual step.

    .venv/bin/python STARVote_LH_tabulation_engine/tools_adam/scripts/reconcile_bpml.py
"""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
BPML_DIR = REPO / "07_Concepts" / "tabulation_engines" / "BV" / "bpml"
REGISTRY = REPO / "07_Concepts" / "YAML_test_case_index" / "bv_cases.csv"
OUT = BPML_DIR / "RECONCILIATION.md"

SNAPSHOT_DATE = "2026-08-16"
ID_RE = re.compile(r"\bBV\d+[a-z]?(?:-r\d+)?\b", re.I)

# Cells that record a gap rather than a test id. Kept verbatim from the sheet.
GAP_MARKERS = {"missing", "missing document", "missing functionality",
               "missing functionality?"}

# The scope split. A BPML row is about COUNTING votes (which the library verifies)
# or about THE APPLICATION (which the Drive QA log verifies). Deciding this per row
# is the whole re-scope: the two inventories have almost disjoint subject matter,
# which is why joining them on test ids returned almost nothing.
COUNTING_L1 = {"Voting Methods", "Tabulation", "Establish Election Procedures"}
COUNTING_PROCESS_HINTS = ("Preference Matrix",)


def is_counting(row: dict) -> bool:
    return (row["L1"] in COUNTING_L1
            or any(h in row["L3_process"] for h in COUNTING_PROCESS_HINTS))


def _rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def _norm(tid: str) -> str:
    """BV0015 / bv15 / BV15 all key the same. Suffixes (-r2, a) are significant."""
    m = re.match(r"(?i)^bv0*(\d+)(.*)$", tid.strip())
    return f"BV{m.group(1)}{m.group(2).lower()}" if m else tid.strip().upper()


LIB_INDEX = "https://github.com/masiarek/star-voting-library/blob/master/07_Concepts/YAML_test_case_index/README.md"

# Which library method family verifies each seam row. Keyed by a substring of the
# L3 process name; the value is the Method value in bv_cases.csv to count.
SEAM_METHOD = {
    "Ranked Robin": "RankedRobin",
    "Single-Winner - Approval": "Approval",
    "scoring/runoff divergence": "STAR",
    "Plurality (chose one)": "Plurality",
    "Bloc STAR": "Bloc STAR",
    "Multi-winner Plurality": "Plurality",
}

# Defect rows to drop outright (see SCOPE.md). Matched on the L3 process name.
DROP_ROWS = {
    "State / Status - Test",          # no test state exists; draft IS test mode
    "(unnamed - placeholder)",        # the sheet's "co to" placeholder
}

# L1 values to merge: {from: to}
MERGE_L1 = {"Voter": "Electors (Voters)"}


def _write_rescoped(bpml, repo, drive_ids, repo_ids) -> None:
    """Emit bpml_rescoped.csv -- the proposed sheet, ready to import into Drive."""
    counts = Counter(r.get("Method", "").strip() for r in repo)
    out = BPML_DIR / "bpml_rescoped.csv"
    n_drop = n_merge = 0
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["L1", "L3_process", "Scope", "Help URL", "Spec",
                    "Verified by", "Status", "Additional info"])
        for r in bpml:
            if r["L3_process"] in DROP_ROWS:
                n_drop += 1
                continue
            l1 = r["L1"]
            if l1 in MERGE_L1:
                l1 = MERGE_L1[l1]
                n_merge += 1
            cell = (r["test_case_cell"] or "").strip()
            spec = (r["doc_cell"] or "").strip()
            if spec in GAP_MARKERS:
                spec = ""

            if is_counting(r):
                scope = "Counting"
                method = next((m for k, m in SEAM_METHOD.items()
                               if k in r["L3_process"]), None)
                n = counts.get(method, 0) if method else 0
                verified = (f"library: {method} ({n} cases) — {LIB_INDEX}"
                            if n else f"library — {LIB_INDEX}")
                status = "covered" if n else "unchecked"
            else:
                scope = "Application"
                if cell.lower() in GAP_MARKERS:
                    verified, status = "", "gap"
                else:
                    ids = [_norm(m) for m in ID_RE.findall(cell)]
                    verified = " ".join(ids)
                    if not ids:
                        status = "unchecked"
                    elif any(i in repo_ids or i in drive_ids for i in ids):
                        status = "covered"
                    else:
                        status = "gap"          # cites an id that exists nowhere
            w.writerow([l1, r["L3_process"], scope, "", spec, verified, status, ""])
    print(f"  wrote {out.relative_to(REPO)}  "
          f"(dropped {n_drop} defect row(s), merged {n_merge} Voter row(s))")


def main() -> int:
    bpml = _rows(BPML_DIR / "bpml_snapshot.csv")
    drive = _rows(BPML_DIR / "bv_testcases_snapshot.csv")
    repo = _rows(REGISTRY)

    drive_ids = {_norm(r["TestID"]) for r in drive if r["TestID"].strip()}
    repo_ids = {_norm(r["TestID"]) for r in repo if r.get("TestID", "").strip()}

    # --- BPML side -------------------------------------------------------
    cited: dict[str, list[str]] = {}
    gap_rows, doc_rows = [], 0
    for r in bpml:
        cell = (r["test_case_cell"] or "").strip()
        if r["doc_cell"].strip() and r["doc_cell"].strip() not in GAP_MARKERS:
            doc_rows += 1
        if cell.lower() in GAP_MARKERS:
            gap_rows.append(r)
            continue
        for tid in (_norm(m) for m in ID_RE.findall(cell)):
            cited.setdefault(tid, []).append(r["L3_process"])

    cited_ids = set(cited)
    in_repo = cited_ids & repo_ids
    in_drive_only = (cited_ids & drive_ids) - repo_ids
    nowhere = cited_ids - repo_ids - drive_ids

    # --- the other direction ---------------------------------------------
    repo_unreferenced = repo_ids - cited_ids
    drive_not_in_repo = drive_ids - repo_ids
    repo_not_in_drive = repo_ids - drive_ids

    count_rows = [r for r in bpml if is_counting(r)]
    app_rows = [r for r in bpml if not is_counting(r)]

    by_l1 = Counter(r["L1"] for r in bpml)
    untested = [r for r in bpml
                if not (r["test_case_cell"] or "").strip()]

    def pct(n, d):
        return f"{100.0 * n / d:.0f}%" if d else "n/a"

    L = []
    a = L.append
    a("# BPML ↔ library reconciliation")
    a("")
    a("**Level: reference · deep dive**")
    a("")
    a(f"Generated by [`reconcile_bpml.py`](../../../../STARVote_LH_tabulation_engine/tools_adam/scripts/reconcile_bpml.py) "
      f"from committed snapshots of the two Drive sheets taken **{SNAPSHOT_DATE}**, "
      "joined against the live registry. The snapshots are point-in-time copies, not a live "
      "feed — re-snapshot before trusting a number that matters.")
    a("")
    a("## The headline")
    a("")
    a("| | |")
    a("|---|---:|")
    a(f"| BPML process rows | {len(bpml)} |")
    a(f"| …citing a test id | {sum(len(v) for v in cited.values())} |")
    a(f"| …recording a gap (`missing…`) | {len(gap_rows)} |")
    a(f"| …with **no test reference at all** | {len(untested)} ({pct(len(untested), len(bpml))}) |")
    a(f"| Distinct test ids cited by BPML | {len(cited_ids)} |")
    a(f"| …that exist as a runnable case in this repo | **{len(in_repo)}** |")
    a(f"| …that exist only in the Drive test sheet | {len(in_drive_only)} |")
    a(f"| …that exist in neither | {len(nowhere)} |")
    a("")
    a("| | |")
    a("|---|---:|")
    a(f"| Case rows in the library registry | {len(repo)} |")
    a(f"| …distinct BV elections behind them | {len(repo_ids)} |")
    a(f"| …referenced by any BPML row | {len(repo_ids & cited_ids)} |")
    a(f"| …**referenced by nothing in the sheet** | {len(repo_unreferenced)} ({pct(len(repo_unreferenced), len(repo_ids))}) |")
    a("")
    a(f"(The registry holds {len(repo)} rows but {len(repo_ids)} distinct ids: a multirace "
      "election backs several cases that all carry its one test id.)")
    a("")
    a("## What the numbers mean")
    a("")
    a(f"The sheet's coverage column is **{pct(len(untested), len(bpml))} empty** — which is honest, "
      "not a failure: it was built as a backlog. The problem is the other direction. The library "
      f"holds {len(repo)} runnable BV-backed case rows ({len(repo_ids)} distinct elections) and the sheet references "
      f"{len(repo_ids & cited_ids)} of them, so **{pct(len(repo_unreferenced), len(repo_ids))} of the "
      "testing work this project has already done is invisible to the document that is supposed to "
      "track testing coverage**.")
    a("")
    a("The two inventories also barely overlap by construction:")
    a("")
    a(f"- Drive test-sheet ids not in the library: **{len(drive_not_in_repo)}**")
    a(f"- Library cases not in the Drive test sheet: **{len(repo_not_in_drive)}**")
    a("")
    a("The Drive sheet is the older manual-QA range and stops in the low hundreds; the library's "
      "ids run to BV2284. They are not two views of one inventory — they are two inventories.")
    a("")
    a("## Why the join returns almost nothing")
    a("")
    a("Not neglect — **disjoint subject matter**. Split the sheet's rows by what they are "
      "actually about:")
    a("")
    a("| | rows | |")
    a("|---|---:|---|")
    a(f"| BPML rows about **the application** | {len(app_rows)} | {pct(len(app_rows), len(bpml))} |")
    a(f"| BPML rows about **counting votes** | {len(count_rows)} | {pct(len(count_rows), len(bpml))} |")
    a(f"| Library elections, every one about **counting votes** | {len(repo_ids)} | 100% |")
    a("")
    a("The sheet is overwhelmingly an **application** inventory — create an election, change a "
      "race, upload voters, download a CSV, log in, archive. The library is entirely a "
      "**tabulation** inventory — given these ballots, is this the right winner. Those are two "
      "different testing activities, and no single test-id column can be the coverage map for "
      "both.")
    a("")
    a("The nine rows where they genuinely meet:")
    a("")
    a("| L1 | Process | Currently cites |")
    a("|---|---|---|")
    for r in count_rows:
        cell = (r["test_case_cell"] or "").strip() or "—"
        a(f"| {r['L1']} | {r['L3_process']} | {cell} |")
    a("")
    a("**The consequence for the sheet: it should not gain 162 rows. It should gain nine links.** "
      "A counting row's verification is a whole family of elections in the library, not one id — "
      "so it points at [the by-method index](../../../YAML_test_case_index/README.md), and the "
      "library's own count is the coverage number. See [SCOPE.md](SCOPE.md) for the re-scope and "
      "the resulting column spec.")
    a("")

    if in_repo:
        a("## BPML rows that DO have a runnable case")
        a("")
        a("| Test id | BPML process | Library case |")
        a("|---|---|---|")
        idx = {_norm(r["TestID"]): r for r in repo if r.get("TestID")}
        for tid in sorted(in_repo, key=lambda s: int(re.sub(r"\D", "", s) or 0)):
            row = idx.get(tid, {})
            case = row.get("Case", "") or "—"
            for proc in cited[tid]:
                a(f"| `{tid}` | {proc} | {case} |")
        a("")

    if in_drive_only or nowhere:
        a("## BPML rows citing a test id with no runnable case")
        a("")
        a("These are the sheet's real coverage gaps — a process it believes is tested, "
          "where nothing in the library reproduces it.")
        a("")
        a("| Test id | BPML process | Where it exists |")
        a("|---|---|---|")
        for tid in sorted(in_drive_only | nowhere,
                          key=lambda s: int(re.sub(r"\D", "", s) or 0)):
            where = "Drive test sheet only" if tid in in_drive_only else "**nowhere**"
            for proc in cited[tid]:
                a(f"| `{tid}` | {proc} | {where} |")
        a("")

    if gap_rows:
        a("## Rows the sheet already flags as gaps")
        a("")
        a("The sheet doing its job — these cells are the most useful thing in it.")
        a("")
        a("| BPML process | Marker |")
        a("|---|---|")
        for r in gap_rows:
            a(f"| {r['L3_process']} | `{r['test_case_cell']}` |")
        a("")

    a("## Process rows by area")
    a("")
    a("| L1 area | rows |")
    a("|---|---:|")
    for k, v in sorted(by_l1.items(), key=lambda kv: (-kv[1], kv[0])):
        a(f"| {k} | {v} |")
    a("")
    a("---")
    a("")
    a("Related: [the docs information architecture](../bv_docs_information_architecture.md) · "
      "[BV registry](../../../YAML_test_case_index/BV_registry.md) · "
      "[all cases by method](../../../YAML_test_case_index/README.md)")

    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    _write_rescoped(bpml, repo, drive_ids, repo_ids)
    print(f"reconcile_bpml: {len(bpml)} process rows, {len(repo_ids)} registry cases")
    print(f"  cited ids: {len(cited_ids)}  in repo: {len(in_repo)}  "
          f"drive-only: {len(in_drive_only)}  nowhere: {len(nowhere)}")
    print(f"  registry cases referenced by no BPML row: {len(repo_unreferenced)}")
    print(f"  wrote {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
