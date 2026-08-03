#!/usr/bin/env python3
"""
check_star_vs_rr_labels.py
==========================
Guard the ANSWER KEYS of 05_Ranked_Robin/02_Examples/star_vs_rr_divergence/ against the LH
engine — every place a sample *names* its STAR or Ranked Robin winner.

WHY THIS EXISTS. The 30 samples are auto-generated, and the generator that made
them modelled STAR in numpy (06_Other/simulations/star_vs_rr_divergence.py,
star_winner(), since corrected). That model resolved ties by column order; the
real engine has further rungs — pairwise wins, five-star count, then lot. So a
model that does not implement those rungs can
name a winner the engine does not elect, and the generator wrote that name into
the title, the description AND expected_winners. It happened once:
cycle_C10_fewV29_bloc_2 claimed "STAR A" while its own `_tabulated` mirror — in
the same commit — printed "STAR = C" (fixed in 7ddde36; 1 of the 30).

`expected_winners` alone is already covered by tests/test_method_positive.py.
The PROSE was not, which is why the bad title and description survived five days
after the key was caught. This checker covers all four label sites at once:

    1. expected_winners:            - the yaml's answer key
    2. election_title:              - "(STAR C, RR B)"
    3. scenario_description:        - "STAR elects C; Ranked Robin elects B."
                                      + the per-cause clause that repeats them
    4. the `_tabulated` mirror:     - "STAR = C" / "RCV-RR = B"
    5. the folder README table:     - the STAR and RR columns of that file's row

Truth is the engine, never the mirror: winners come from a real tabulation
(tools_adam/scenario_eval.py for STAR, the engine's copeland_winner() for RR —
the same call that prints the [Divergence from STAR] block). The mirror is then
checked as one more label site, so a stale mirror is reported rather than
believed.

Usage:
    python tools_adam/scripts/check_star_vs_rr_labels.py            # check, exit 1 on drift
    python tools_adam/scripts/check_star_vs_rr_labels.py --fix      # rewrite yaml labels
    python tools_adam/scripts/check_star_vs_rr_labels.py --dir DIR  # check a copy

--fix rewrites the yaml label sites (1-3) from the engine's answer. It does NOT
touch the mirror or the README: re-run the yaml through the engine to refresh the
mirror, then rebuild pages/README. Anything --fix cannot rewrite confidently is
reported, never silently left stale.
"""

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ENGINE_DIR = SCRIPT_DIR.parent.parent
REPO_ROOT = ENGINE_DIR.parent
sys.path.insert(0, str(ENGINE_DIR))
sys.path.insert(0, str(ENGINE_DIR / "tools_adam"))

import starvote_larry_hastings as wrapper  # noqa: E402
from scenario_eval import scenario_winners  # noqa: E402

DEFAULT_DIR = REPO_ROOT / "05_Ranked_Robin" / "02_Examples" / "star_vs_rr_divergence"

# --- the label sites, as (name, pattern, star-group, rr-group) --------------
# Each pattern must capture the STAR and the RR name so one regex both CHECKS
# and (via re.sub) FIXES the site.
TITLE_SITE = ("election_title", re.compile(r"\(STAR (\w+), RR (\w+)\)"), 1, 2)
DESC_SITES = [
    ("description headline",
     re.compile(r"STAR elects (\w+); Ranked Robin elects (\w+)\."), 1, 2),
    # cycle files
    ("cycle clause",
     re.compile(r"RR falls back on Copeland/margin \((\w+)\); "
                r"STAR runs its two score-leaders off \((\w+)\)"), 2, 1),
    # dark-horse files
    ("dark-horse clause",
     re.compile(r"STAR elects runoff winner (\w+); "
                r"RR elects the Condorcet winner (\w+)"), 1, 2),
]
# The mirror's [Divergence from STAR] block. RCV-RR prints as "RCV-RR" or, when
# it agrees with Condorcet and both differ from STAR, as "RCV-RR (Condorcet)".
MIRROR_STAR = re.compile(r"^\s*STAR\s+= (\S+)", re.M)
MIRROR_RR = re.compile(r"^\s*RCV-RR(?: \(Condorcet\))?\s+= (\S+)", re.M)
# The answer key itself. Anchored with [ \t] rather than \s so the match stops at
# the winner's name — a greedy \s*$ swallows the blank line that follows and
# --fix then silently deletes it.
KEY_SITE = re.compile(r"(^expected_winners:[ \t]*\n[ \t]+-[ \t]*)(\S+)", re.M)


def engine_winners(path):
    """(STAR winner, RR winner) straight from the engine — the only source of truth."""
    star, _seats = scenario_winners(path)
    el = wrapper.load_election(str(path))
    candidates, ballots, _ = wrapper.parse_ballots_from_string(el["ballots"])
    priority = el.get("lot_numbers") or candidates
    rr = wrapper.copeland_winner(candidates, ballots, priority)
    return star[0], str(rr)


def mirror_path(yaml_path):
    d = yaml_path.parent
    return d / f"{d.name}_tabulated" / f"{yaml_path.stem}_tabulated.txt"


def check_file(path, readme_rows):
    """Return a list of problem strings for one sample (empty == clean)."""
    problems = []
    try:
        star, rr = engine_winners(path)
    except Exception as e:  # noqa: BLE001
        return [f"engine failed: {e}"]

    if star == rr:
        problems.append(
            f"STAR and RR both elect {star} — this folder is *divergence* samples")

    text = path.read_text(encoding="utf-8")

    # 1. expected_winners (also covered by test_method_positive, kept here so a
    #    single run reports every drifted site at once).
    key = KEY_SITE.search(text)
    if not key:
        problems.append("no single-winner expected_winners block found")
    elif key.group(2) != star:
        problems.append(f"expected_winners = {key.group(2)}, engine elects {star}")

    # 2-3. title + description label sites
    for name, pat, sg, rg in [TITLE_SITE] + DESC_SITES:
        m = pat.search(text)
        if not m:
            if name in ("election_title", "description headline"):
                problems.append(f"{name}: no 'STAR x / RR y' label found")
            continue  # cause clauses are per-flavour; absence is normal
        if m.group(sg) != star or m.group(rg) != rr:
            problems.append(
                f"{name}: says STAR {m.group(sg)} / RR {m.group(rg)}, "
                f"engine says STAR {star} / RR {rr}")

    # 4. the _tabulated mirror
    mp = mirror_path(path)
    if not mp.exists():
        problems.append(f"missing mirror {mp.relative_to(REPO_ROOT)}")
    else:
        mt = mp.read_text(encoding="utf-8", errors="replace")
        ms, mr = MIRROR_STAR.search(mt), MIRROR_RR.search(mt)
        if not ms:
            problems.append("mirror has no '[Divergence from STAR]  STAR = x' line")
        elif ms.group(1) != star:
            problems.append(f"mirror says STAR = {ms.group(1)}, engine elects {star}")
        if not mr:
            problems.append("mirror has no 'RCV-RR = y' line")
        elif mr.group(1) != rr:
            problems.append(f"mirror says RCV-RR = {mr.group(1)}, engine elects {rr}")

    # 5. the folder README table row
    row = readme_rows.get(path.stem)
    if row is None:
        problems.append("no README table row")
    elif row != (star, rr):
        problems.append(
            f"README row says STAR {row[0]} / RR {row[1]}, "
            f"engine says STAR {star} / RR {rr}")

    return problems


def readme_table(folder):
    """{file stem: (STAR, RR)} parsed from the folder README's sample table."""
    readme = folder / "README.md"
    rows = {}
    if not readme.exists():
        return rows
    for line in readme.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 10:
            continue
        stem = re.search(r"\[`([^`]+)`\]", cells[-1])
        star = re.fullmatch(r"\*\*(\w+)\*\*", cells[4])
        rr = re.fullmatch(r"\*\*(\w+)\*\*", cells[5])
        if stem and star and rr:
            rows[stem.group(1)] = (star.group(1), rr.group(1))
    return rows


def fix_file(path):
    """Rewrite the yaml's label sites from the engine. Returns (changed, notes)."""
    star, rr = engine_winners(path)
    text = original = path.read_text(encoding="utf-8")
    notes = []
    for name, pat, sg, rg in [TITLE_SITE] + DESC_SITES:
        m = pat.search(text)
        if not m:
            continue

        def repl(mm, sg=sg, rg=rg):
            """Rebuild the matched text, swapping only the two captured names."""
            whole, base = mm.group(0), mm.start(0)
            spans = sorted([(mm.start(sg) - base, mm.end(sg) - base, star),
                            (mm.start(rg) - base, mm.end(rg) - base, rr)])
            out, last = "", 0
            for start, end, value in spans:
                out += whole[last:start] + value
                last = end
            return out + whole[last:]

        text = pat.sub(repl, text, count=1)
        if pat.search(text) is None or pat.search(text).group(sg) != star:
            notes.append(f"could not rewrite {name} — fix by hand")

    if KEY_SITE.search(text):
        text = KEY_SITE.sub(lambda m: m.group(1) + star, text, count=1)
    else:
        notes.append("no expected_winners block to rewrite — add one by hand")

    if text != original:
        path.write_text(text, encoding="utf-8")
    return text != original, notes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=str(DEFAULT_DIR),
                    help="sample folder to check (default: the divergence set)")
    ap.add_argument("--fix", action="store_true",
                    help="rewrite the yaml label sites from the engine's answer")
    args = ap.parse_args(argv)

    folder = Path(args.dir).resolve()
    samples = sorted(p for p in folder.glob("*.yaml"))
    if not samples:
        print(f"no samples found in {folder}", file=sys.stderr)
        return 2

    rows = readme_table(folder)
    print(f"Checking {len(samples)} sample(s) in {folder.name} against the LH engine\n")

    if args.fix:
        changed = 0
        for p in samples:
            did, notes = fix_file(p)
            for n in notes:
                print(f"  !! {p.name}: {n}")
            if did:
                changed += 1
                print(f"  relabelled {p.name}")
        print(f"\n{changed} file(s) relabelled. Re-run them through the engine to "
              f"refresh the _tabulated mirrors, then rebuild pages + README.")
        return 0

    bad = 0
    for p in samples:
        problems = check_file(p, rows)
        if problems:
            bad += 1
            print(f"  FAIL {p.name}")
            for prob in problems:
                print(f"       - {prob}")
    if bad:
        print(f"\n{bad} of {len(samples)} sample(s) have labels that disagree with "
              f"the engine.\nRe-run with --fix (then refresh mirrors/pages/README).")
        return 1
    print(f"  OK — all {len(samples)} samples: expected_winners, title, description, "
          f"mirror\n       and README row all match the engine.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
