#!/usr/bin/env python3
"""Cross-check our ranked cases against rcv-lab.org, and keep its Sankey art.

Two jobs, one file, because they share the parser and neither is useful alone.

WHY A THIRD ENGINE AT ALL. The Ranked Robin cases get cross-verified three ways
(LH, BetterVoting, and `pref_voting`'s independent Copeland) precisely because a
tally that only ever agrees with itself is not evidence. The RCV-IRV cases had no
such leg: the vendored pyrankvote engine is the only thing that counts them, so
"our IRV numbers are right" rested on one implementation. <https://rcv-lab.org>
is that missing leg — a wholly independent tabulator, and one that can *also* run
the certified RCTab engine, which is the reference implementation the RCV
Resource Center maintains.

WHY THE PICTURES ARE WORTH KEEPING. Our IRV engine prints rounds as text. The one
thing a reader cannot see in a column of numbers is where a transferred vote came
FROM — and that is the whole subject of every page in this repo that argues about
center squeeze or exhausted ballots. RCV Lab draws it as a Sankey with exact
traced provenance (not the estimated ribbons some visualizers draw), and it gives
exhausted ballots their own column, labelled "No Further Rankings". We export
those to `<case dir>/img/<stem>_sankey.svg` and commit them, rather than linking
out: the repo does not control that site, the art must survive it going away, and
a static SVG renders on GitHub, on the built site, and in a local viewer alike.

  # 1. write one CVR CSV per ranked IRV case
  python3 build_rcvlab_sankey.py emit --out /tmp/rcvlab

  # 2. drive rcv-lab.org over those CSVs (Analysis -> CVR -> Tabulate ->
  #    Visualize -> Sankey), collecting {stem, winners, rounds, svg} per case
  #    into one JSON array. See docs/ below for the browser recipe.

  # 3. verify every winner against the YAML answer key + install the art
  python3 build_rcvlab_sankey.py install results.json --min-rounds 3

TWO THINGS ABOUT THEIR CSV THAT WILL COST YOU AN AFTERNOON (both learned the hard
way on 2026-08-08, both silent):

 1. **The first column is eaten as a ballot ID.** Their generic CSV is documented
    as "one column per candidate, cell = rank" — and it is, starting at column
    TWO. Feed it a bare `Purple,Green,Blue,Pink` header and Purple is dropped
    from the election with no warning at all; our Post-it case came back "Green,
    2 rounds" instead of Purple in 3, looking entirely legitimate. So `emit`
    always writes a leading `BallotID` column, which makes the site say
    "In CVR but not in config: BallotID" — that message is the sign it parsed
    correctly, not a problem to fix.
 2. **The filename must contain "cvr"** or the site raises a `confirm()` that an
    automated browser suppresses, silently rejecting the file. Hence `_cvr.csv`.

Scope: ranked ballots only. RCV Lab does IRV, STV/PR and bloc, plus plurality /
approval / cumulative "for comparison" — it has no STAR and no Ranked Robin, so
this tool refuses anything that is not a ranked IRV case rather than pretending.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Iterator, NamedTuple

REPO_ROOT = Path(__file__).resolve().parents[3]

# Only these tabulate as IRV on the LH side. `RCV_IRV`/`RCV-IRV` are the house
# spellings; the engine also accepts bare `IRV`, which is what the files use.
IRV_METHODS = {"irv", "rcv_irv", "rcv-irv"}

# Where the art lands, relative to the case's own folder — same `img/` convention
# the ballot art uses, so a case folder has one place for pictures.
IMG_SUBDIR = "img"


class Case(NamedTuple):
    stem: str
    yaml_path: Path
    title: str
    candidates: list[str]
    ballots: list[tuple[int, list[str]]]   # (weight, ranking) — weight FIRST
    expected: list[str]


# ---------------------------------------------------------------- parsing


def _block(text: str, key: str) -> str | None:
    """Return the literal-block body under `key:` (`|-` / `|`), or None."""
    m = re.search(rf"^{key}:\s*\|-?\s*\n((?:[ \t]+.*\n?|\n)+)", text, re.M)
    return m.group(1) if m else None


def _scalar(text: str, key: str) -> str | None:
    m = re.search(rf"^{key}:[ \t]*(.+?)[ \t]*$", text, re.M)
    if not m:
        return None
    return m.group(1).strip().strip("\"'")


def _expected(text: str) -> list[str]:
    """`expected_winners:` as either a flow list or a block list.

    Strips trailing `#` comments: several cases annotate the answer key inline
    (`- Avery   # LH seeded-tiebreak result; BV's draw this run = Blake`), and
    carrying that comment into the name reports a false disagreement.
    """
    def clean(s: str) -> str:
        return s.split("#", 1)[0].strip().strip("\"'")

    flow = re.search(r"^expected_winners:[ \t]*\[(.*?)\]", text, re.M)
    if flow:
        return [c for w in flow.group(1).split(",") if (c := clean(w))]
    blk = re.search(r"^expected_winners:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)", text, re.M)
    if not blk:
        return []
    return [c for ln in blk.group(1).splitlines()
            if ln.strip() and (c := clean(ln.split("-", 1)[1]))]


def parse_case(path: Path) -> Case | None:
    """Parse a ranked IRV case, or return None if this file isn't one.

    Deliberately conservative: anything with a score-style candidate header, an
    equal-rank `=`, or a non-IRV method is refused rather than approximated. A
    wrong picture is worse than no picture.
    """
    text = path.read_text(encoding="utf-8")

    method = (_scalar(text, "voting_method") or "").lower()
    if method not in IRV_METHODS:
        return None

    body = _block(text, "ballots")
    if body is None:
        return None

    ballots: list[tuple[int, list[str]]] = []
    candidates: list[str] = []
    for raw in body.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue

        weight = 1
        # A leading `N:` is the bloc size. The house rule is that a ballot's
        # weight comes FIRST, and the parser only ever matches it there.
        m = re.match(r"^(\d+)\s*:\s*(.*)$", line)
        if m:
            weight, line = int(m.group(1)), m.group(2).strip()

        if not line:
            continue
        if "=" in line:
            return None      # equal ranks — RCV Lab supports them, we don't emit them
        if ">" not in line and "," in line:
            return None      # score-style candidate header: not a ranked file

        ranking = [c.strip() for c in line.split(">") if c.strip()]
        if not ranking:
            continue
        for c in ranking:
            if c not in candidates:
                candidates.append(c)
        ballots.append((weight, ranking))

    if not ballots or len(candidates) < 2:
        return None

    return Case(
        stem=path.stem,
        yaml_path=path,
        title=_scalar(text, "election_title") or path.stem,
        candidates=candidates,
        ballots=ballots,
        expected=_expected(text),
    )


def discover(root: Path) -> Iterator[Case]:
    """Every ranked IRV case in the tree, skipping generated mirrors + fixtures.

    Dot-directories are skipped for the same reason `migrate_concept_links.py`
    lists `.claude` in its SKIP_DIRS: the repo's own skill files carry example
    elections that are documentation, not cases. They outnumbered the real ones
    244 to 64 on the first run of this script.
    """
    skip = {"_tabulated", "negative_cases", "2_negative", "harness_cases", "site"}
    for path in sorted(root.rglob("*.yaml")):
        if any(part.startswith(".") for part in path.parts):
            continue
        if any(part in skip or part.endswith("_tabulated") for part in path.parts):
            continue
        case = parse_case(path)
        if case is not None:
            yield case


# ---------------------------------------------------------------- emit


def to_cvr_rows(case: Case) -> list[list[str]]:
    """Generic-CSV rows: `BallotID`, then one column per candidate holding a rank.

    Weighted blocs are expanded to one row per ballot — the compact weighted form
    is RCV Lab's own native format, whose spec we don't have, and an expanded
    generic CSV is the form both their engine and RCTab read.
    """
    rows = [["BallotID"] + case.candidates]
    ballot_id = 0
    for weight, ranking in case.ballots:
        rank_of = {c: str(i + 1) for i, c in enumerate(ranking)}
        for _ in range(weight):
            ballot_id += 1
            rows.append([str(ballot_id)] + [rank_of.get(c, "") for c in case.candidates])
    return rows


def cmd_emit(args: argparse.Namespace) -> int:
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    cases = list(discover(REPO_ROOT))
    if args.only:
        wanted = set(args.only)
        cases = [c for c in cases if c.stem in wanted]
        missing = wanted - {c.stem for c in cases}
        for stem in sorted(missing):
            print(f"  ! no ranked IRV case named {stem}", file=sys.stderr)

    manifest = []
    for case in cases:
        rows = to_cvr_rows(case)
        # "cvr" in the name is load-bearing — see the module docstring.
        csv_path = out / f"{case.stem}_cvr.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as fh:
            csv.writer(fh).writerows(rows)
        manifest.append({
            "stem": case.stem,
            "title": case.title,
            "yaml": str(case.yaml_path.relative_to(REPO_ROOT)),
            "csv": csv_path.name,
            "candidates": case.candidates,
            "ballots": len(rows) - 1,
            "expected_winners": case.expected,
        })
        print(f"  {case.stem:52s} {len(rows)-1:>6d} ballots  {len(case.candidates)} candidates")

    (out / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n{len(manifest)} CVR files + manifest.json -> {out}")
    return 0


# ---------------------------------------------------------------- install

# The site's SVG carries Svelte's scoped class names and gets all of its type
# styling from a stylesheet that does not travel with the markup. Stripped and
# re-styled here so the committed file stands on its own in every viewer.
_SVELTE_CLASS = re.compile(r"\s+class=\"([^\"]*?)\s*svelte-[0-9a-z]+\"")
_STYLE = """<style>
  text { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; fill: #222; }
  .value-label { font-size: 9px; }
  .name-label  { font-size: 9px; }
  .round-label { font-size: 8px; font-weight: 600; fill: #445; }
  .marker      { font-size: 9px; }
  .name-tick   { stroke: #99a; fill: none; stroke-width: 1; }
</style>
"""


def tidy_svg(svg: str, title: str) -> str:
    svg = _SVELTE_CLASS.sub(lambda m: f' class="{m.group(1)}"' if m.group(1) else "", svg)
    svg = svg.replace("<!---->", "")
    if "xmlns=" not in svg:
        svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)
    # A white plate under the ribbons: the page renders on white, and a
    # transparent SVG inverts unreadably in a dark-theme viewer.
    head, sep, tail = svg.partition(">")
    plate = '<rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>'
    return f"{head}{sep}<title>{title}</title>{_STYLE}{plate}{tail}"


def cmd_install(args: argparse.Namespace) -> int:
    results = json.loads(Path(args.results).read_text(encoding="utf-8"))
    if isinstance(results, dict):
        results = results.get("results", [])

    by_stem = {c.stem: c for c in discover(REPO_ROOT)}
    ledger, wrote, disagreed = [], 0, 0

    for entry in results:
        stem = entry["stem"]
        case = by_stem.get(stem)
        if case is None:
            print(f"  ! {stem}: no such ranked IRV case", file=sys.stderr)
            continue

        theirs = sorted(entry.get("winners") or [])
        ours = sorted(case.expected)
        rounds = entry.get("rounds")
        agree = bool(ours) and theirs == ours
        if not agree:
            disagreed += 1

        svg_rel = ""
        svg = entry.get("svg")
        if svg and rounds and rounds >= args.min_rounds:
            img_dir = case.yaml_path.parent / IMG_SUBDIR
            img_dir.mkdir(exist_ok=True)
            svg_path = img_dir / f"{stem}_sankey.svg"
            svg_path.write_text(tidy_svg(svg, case.title), encoding="utf-8")
            svg_rel = str(svg_path.relative_to(REPO_ROOT))
            wrote += 1

        ledger.append({
            "stem": stem,
            "title": case.title,
            "yaml": str(case.yaml_path.relative_to(REPO_ROOT)),
            "ours": ours,
            "theirs": theirs,
            "rounds": rounds,
            "agree": agree,
            "svg": svg_rel,
        })
        flag = "OK " if agree else "!! "
        print(f"  {flag}{stem:52s} ours={','.join(ours) or '-':<12s} "
              f"rcvlab={','.join(theirs) or '-':<12s} rounds={rounds}")

    Path(args.ledger).write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
    print(f"\n{len(ledger)} verified, {disagreed} DISAGREE, {wrote} SVG written")
    print(f"ledger -> {args.ledger}")
    return 1 if disagreed else 0


# ---------------------------------------------------------------- cli


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("emit", help="write RCV Lab CVR CSVs for ranked IRV cases")
    e.add_argument("--out", default="/tmp/rcvlab", help="staging dir (not in the repo)")
    e.add_argument("--only", nargs="*", help="limit to these case stems")
    e.set_defaults(func=cmd_emit)

    i = sub.add_parser("install", help="verify winners + write the Sankey SVGs")
    i.add_argument("results", help="JSON collected from rcv-lab.org")
    i.add_argument("--ledger", default="/tmp/rcvlab/ledger.json")
    i.add_argument("--min-rounds", type=int, default=3,
                   help="skip art below this many rounds (a 2-round Sankey "
                        "shows one transfer and teaches nothing)")
    i.set_defaults(func=cmd_install)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
