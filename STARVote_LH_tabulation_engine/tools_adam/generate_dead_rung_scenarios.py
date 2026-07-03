#!/usr/bin/env python3
"""Generate STAR "dead rung" tie-break scenarios as tabulatable YAML.

The one fact these elections isolate: STAR's second tie-break rung counts votes
equal to the **scale maximum (5)** -- "most five-star votes" -- and it does **NOT**
step down to 4s if the 5s tie or are absent. When no tied candidate has a 5, that
rung reads 0-0: it's a **dead rung**, and the tie falls straight through to the
**lot**. Piling up 4s never revives it.

STAR's two tie-break ladders:

    SCORING ROUND  (which two become finalists):  pairwise  ->  five-star  ->  lot
    AUTOMATIC RUNOFF (which finalist wins):        score     ->  five-star  ->  lot

This script builds a tie that lands on the five-star rung, and lets you set what
that rung finds:

  --rung alive   one tied candidate has a 5 the other lacks -> five-star DECIDES
  --rung dead    nobody scored a 5 (capped at --cap)        -> 0-0, falls to the LOT
  --rung tied    both tied candidates have equal 5s          -> runs but decides
                 nothing (e.g. 1-1) -> falls to the LOT

Rounds:

  --round scoring   3 candidates; a leader wins, two others tie for the 2nd slot
  --round runoff    2 candidates tie in the automatic runoff

Regression mode:

  --adversarial-lot   pins lot_numbers to favor the "wrong" candidate, so the
                      asserted winner is only elected if the ladder is consulted
                      in the correct order. This is what turns a teaching example
                      into a test that CATCHES a mis-ordered cascade. (In this
                      mode the five-star vs lot choice changes the *elected
                      winner*, not just which rung fired.)

Every generated file carries an `expected_winners:` assertion, so it doubles as a
positive test case. The ballots are taken from the verified cases in
`01_STAR/tie_break_dead_rung/` (cases 01-09), generalized over the score cap,
electorate scale, and candidate names.

Examples
--------
  # scoring-round tie, a 5 exists -> five-star advances the 2nd finalist
  python generate_dead_rung_scenarios.py --round scoring --rung alive

  # same tie, capped at 4 -> DEAD rung -> the lot decides (the core lesson)
  python generate_dead_rung_scenarios.py --round scoring --rung dead

  # "what about the 4s?" -> cap at 3 or 2, still dead, still the lot
  python generate_dead_rung_scenarios.py --round runoff --rung dead --cap 3

  # strict regression: the elected winner depends on the ladder order
  python generate_dead_rung_scenarios.py --round runoff --rung alive --adversarial-lot --run

Full write-up: see generate_dead_rung_scenarios.md next to this script.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

# Candidate name banks, in lot / column order (distinct initials A, B, C, ...).
NAME_BANKS: dict[str, list[str]] = {
    "letters": ["A", "B", "C", "D", "E"],
    "classic": ["Ann", "Ben", "Cara", "Dan", "Eve"],   # matches the case set
    "fruits":  ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
    "flavors": ["Almond", "Brownie", "Cocoa", "Dulce", "Espresso"],
    "capitals": ["Athens", "Berlin", "Cairo", "Delhi", "Edinburgh"],
}

OPTIONS_BLOCK = """\
  options:
    show_description: false
    show_matrix: true
    matrix_finalists_only: true
    show_condorcet: false
    show_score_counts: true
    show_irv: false
    show_runoff_percent: true
    brief: true
    collapse_ballots: false
    count_separator: "×"\
"""


@dataclass
class Template:
    ncols: int
    rows: list[list[int]]        # score rows, by column index
    lot: list[int] | None        # lot order as column indices, or None (no lot line)
    winner: int                  # winning column index
    teach: str                   # one-line explanation of what the rung does here


def build_template(round_: str, rung: str, adversarial: bool, cap: int) -> Template:
    """Return the verified ballot template for a (round, rung, adversarial) case.

    Non-adversarial cases teach *which rung decides* (the leader wins either way).
    Adversarial cases make the *elected winner* depend on the ladder order.
    Ballots mirror the checked-in cases in 01_STAR/tie_break_dead_rung/.
    """
    c = cap
    if not adversarial:
        table: dict[tuple[str, str], Template] = {
            # SCORING: col0 leads & wins; col1/col2 tie for the 2nd finalist slot.
            ("scoring", "alive"): Template(
                3, [[5, 5, 3], [5, 1, 3]], None, 0,
                "col1 has a 5, col2 has none -> five-star advances col1 (ballots decide)."),
            ("scoring", "dead"): Template(
                3, [[c, c, 1], [c, 0, c - 1]], [0, 1, 2], 0,
                f"no 5 anywhere (capped at {c}) -> five-star 0-0 -> the LOT picks the 2nd finalist."),
            ("scoring", "tied"): Template(
                3, [[5, 5, 1], [5, 1, 5]], [0, 1, 2], 0,
                "col1 and col2 each have one 5 -> five-star 1-1, non-separating -> the LOT."),
            # RUNOFF: the two candidates tie in the automatic runoff.
            ("runoff", "alive"): Template(
                2, [[5, 1], [0, 4]], None, 0,
                "runoff tie; col0 has a 5, col1 none -> five-star wins it for col0."),
            ("runoff", "dead"): Template(
                2, [[c, 0], [0, c]], [0, 1], 0,
                f"runoff tie; no 5 (capped at {c}) -> five-star 0-0 -> the LOT wins it for col0."),
            ("runoff", "tied"): Template(
                2, [[5, 0], [0, 5]], [0, 1], 0,
                "runoff tie; one 5 each -> five-star 1-1, decides nothing -> the LOT for col0."),
        }
        key = (round_, rung)
        if key not in table:
            raise SystemExit(f"error: no template for --round {round_} --rung {rung}.")
        return table[key]

    # Adversarial: lot favors the WRONG candidate; correct ladder order still elects
    # the asserted winner. (cap is fixed at 4 here -- changing it breaks the tie.)
    if rung == "tied":
        raise SystemExit("error: --rung tied has no adversarial template "
                         "(use alive or dead with --adversarial-lot).")
    adv: dict[tuple[str, str], Template] = {
        # cols: Ann=0, Ben=1, Cara=2. lot favors Cara(2). Ben/Cara tie for 2nd slot.
        ("scoring", "alive"): Template(
            3, [[3, 5, 1], [3, 5, 0], [4, 0, 3], [4, 0, 4], [0, 1, 1]], [2, 0, 1], 1,
            "five-star OUTRANKS the lot: col1's 5s advance it over lot-favored col2; col1 then wins."),
        ("scoring", "dead"): Template(
            3, [[3, 4, 1], [3, 4, 0], [4, 0, 3], [4, 0, 4], [0, 1, 1]], [2, 0, 1], 0,
            "dead rung -> the lot advances col2, who loses the runoff to col0 (the winner flips vs alive)."),
        # cols: Ann=0, Ben=1. lot favors Ben(1).
        ("runoff", "alive"): Template(
            2, [[5, 1], [0, 4]], [1, 0], 0,
            "five-star OUTRANKS the lot: col0's 5 wins the runoff over lot-favored col1."),
        ("runoff", "dead"): Template(
            2, [[c, 0], [0, c]], [1, 0], 1,
            f"dead rung (capped at {c}) -> only the lot is left, so lot-favored col1 wins."),
    }
    key = (round_, rung)
    if key not in adv:
        raise SystemExit(f"error: no adversarial template for --round {round_} --rung {rung}.")
    return adv[key]


def render_yaml(t: Template, names: list[str], scale: int, round_: str, rung: str,
                adversarial: bool, cap: int, title: str | None) -> str:
    cols = names[:t.ncols]
    header = ",".join(cols)
    rows = t.rows * scale
    ballot_lines = "\n".join(["      " + header]
                             + ["      " + ",".join(str(s) for s in r) for r in rows])
    winner = cols[t.winner]

    lot_line = ""
    if t.lot is not None:
        lot_line = "    lot_numbers: [" + ", ".join(cols[i] for i in t.lot) + "]\n"

    if title is None:
        adv = " (adversarial lot)" if adversarial else ""
        capnote = f", cap {cap}" if rung == "dead" else ""
        title = (f"Dead rung — {round_} round, {rung} five-star rung{capnote}{adv}")

    description = (
        f"Generated dead-rung scenario ({round_} round, '{rung}' five-star rung"
        + (", adversarial lot" if adversarial else "") + "). "
        + t.teach + " "
        "STAR's second rung counts only score-5 votes and never steps down to 4s; "
        "when it can't separate the tied candidates the lot decides. "
        "See 01_STAR/tie_break_dead_rung/README.md and "
        "00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md."
    )

    return f"""\
election:
  election_title: {title}
  election_description: |-
    {description}
{OPTIONS_BLOCK}
  races:
  - race_id: '0'
    race_description: "generated by generate_dead_rung_scenarios.py"
    num_winners: 1
    voting_method: STAR
    ballots: |-
{ballot_lines}
{lot_line}    expected_results:
      winners:
      - {winner}

# file generated by generate_dead_rung_scenarios.py
"""


def find_engine(start: Path) -> Path | None:
    for parent in [start, *start.parents]:
        cand = parent / "STARVote_LH_tabulation_engine" / "starvote_larry_hastings.py"
        if cand.exists():
            return cand
    return None


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Generate STAR 'dead rung' tie-break scenarios (see module docstring).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--round", choices=["scoring", "runoff"], default="scoring",
                   help="where the tie sits (default scoring)")
    p.add_argument("--rung", choices=["alive", "dead", "tied"], default="alive",
                   help="state of the five-star rung (default alive)")
    p.add_argument("--cap", type=int, choices=[4, 3, 2], default=4,
                   help="score ceiling for a DEAD rung -- the 'what about 4s?' knob (default 4)")
    p.add_argument("--adversarial-lot", action="store_true",
                   help="pin the lot to favor the wrong candidate (strict regression test)")
    p.add_argument("--scale", type=int, default=1,
                   help="duplicate the ballot block N times for a bigger electorate (default 1)")
    p.add_argument("--theme", choices=sorted(NAME_BANKS), default="letters",
                   help="candidate name bank (default letters)")
    p.add_argument("--title", default=None, help="override the election_title")
    p.add_argument("-o", "--out", default=None,
                   help="save to this file (or DIR, auto-named). Omit to print to screen.")
    p.add_argument("--run", action="store_true",
                   help="tabulate the file with the LH engine after writing")
    args = p.parse_args(argv)

    if args.scale < 1:
        raise SystemExit("error: --scale must be >= 1.")
    if args.rung != "dead" and args.cap != 4:
        print("note: --cap only applies to a dead rung; ignored here.", file=sys.stderr)
    if args.adversarial_lot and args.rung == "dead" and args.cap != 4:
        print("note: adversarial dead template is fixed at cap 4; --cap ignored.", file=sys.stderr)
        args.cap = 4

    t = build_template(args.round, args.rung, args.adversarial_lot, args.cap)
    names = NAME_BANKS[args.theme]
    if t.ncols > len(names):
        raise SystemExit(f"error: theme '{args.theme}' needs {t.ncols} names.")

    yaml_text = render_yaml(t, names, args.scale, args.round, args.rung,
                            args.adversarial_lot, args.cap, args.title)

    auto_name = (f"dead_rung_{args.round}_{args.rung}"
                 + (f"_cap{args.cap}" if args.rung == "dead" else "")
                 + ("_advlot" if args.adversarial_lot else "")
                 + (f"_x{args.scale}" if args.scale > 1 else "") + ".yaml")

    out: Path | None = None
    if args.out:
        out = Path(args.out)
        if out.is_dir():
            out = out / auto_name
    elif args.run:
        out = Path(tempfile.gettempdir()) / auto_name

    print("─" * 70)
    print(yaml_text, end="")
    print("─" * 70)
    print(f"  rung behavior: {t.teach}")

    if out is not None:
        out.write_text(yaml_text, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print("(printed to screen only — pass --out FILE to save, or --out DIR for an auto name)")

    if args.run:
        engine = find_engine(out.resolve()) or find_engine(Path(__file__).resolve())
        if engine is None:
            print("note: --run given but engine not found; skipping tabulation.", file=sys.stderr)
            return 0
        print(f"tabulating with {engine.name} ...")
        proc = subprocess.run([sys.executable, str(engine), str(out)],
                              capture_output=True, text=True)
        sys.stdout.write(proc.stdout)
        if proc.returncode != 0:
            sys.stderr.write(proc.stderr)
            return proc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
