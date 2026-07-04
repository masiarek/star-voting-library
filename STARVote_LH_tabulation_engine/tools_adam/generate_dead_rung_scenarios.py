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

Why the swap (it looks backwards but isn't): each round breaks its tie with the
OTHER round's yardstick, because the measure that tied can't be the one that
separates. The scoring round ranks by total SCORE, so a scoring-round tie means
scores are equal -> break it by PAIRWISE (the runoff's question). The runoff
decides by PAIRWISE preference, so a runoff tie means preference is equal ->
break it by SCORE (the scoring round's measure). Five-star is the shared second
rung; the lot is the floor of both. (Full write-up:
00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md.)

This script builds a tie that lands on the five-star rung, and lets you set what
that rung finds:

  --rung alive   one tied candidate has a 5 the other lacks -> five-star DECIDES
  --rung dead    nobody scored a 5 (capped at --cap)        -> 0-0, falls to the LOT
  --rung tied    both tied candidates have equal 5s          -> runs but decides
                 nothing (e.g. 1-1) -> falls to the LOT

Rounds:

  --round scoring   3 candidates; a leader wins, two others tie for the 2nd slot
  --round runoff    2 candidates tie in the automatic runoff
  --round full      a fully symmetric k-candidate tie (--candidates k): every
                    candidate a rotation of the others, so the lot alone decides
                    and ANY of the k can win. Divergence from a published order is
                    (k-1)/k. The k-candidate analog of BV jfk7pd. Add --pad N to
                    bury the tie in symmetric noise ballots (a "less obvious" case
                    that still tabulates to an exact tie).

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

  # a FULL symmetric k-candidate tie: any of the k can win by lot (divergence (k-1)/k)
  python generate_dead_rung_scenarios.py --round full --candidates 4 --run

  # a "less obvious" tie: bury it in symmetric noise ballots (still an exact tie)
  python generate_dead_rung_scenarios.py --round full --candidates 3 --pad 4 --seed 7 --run

Full write-up: see generate_dead_rung_scenarios.md next to this script.
"""
from __future__ import annotations

import string

import argparse
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

# Candidate name banks, in lot / column order (distinct initials A, B, C, ...).
NAME_BANKS: dict[str, list[str]] = {
    "letters": list(string.ascii_uppercase),   # A..Z (26), for large --candidates
    "classic": ["Ann", "Ben", "Cara", "Dan", "Eve"],   # matches the case set
    "fruits":  ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
    "flavors": ["Almond", "Brownie", "Cocoa", "Dulce", "Espresso"],
    "capitals": ["Athens", "Berlin", "Cairo", "Delhi", "Edinburgh"],
}

# Flat schema (top-level keys), matching the checked-in tie_break_dead_rung
# cases 01-09 -- this is the shape auto-discovered by test_single_winner_positive.
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


def build_template(round_: str, rung: str, adversarial: bool, cap: int,
                   candidates: int = 3, pad: int = 0, seed: int | None = None,
                   pad_vector: list[int] | None = None) -> Template:
    """Return the verified ballot template for a (round, rung, adversarial) case.

    Non-adversarial cases teach *which rung decides* (the leader wins either way).
    Adversarial cases make the *elected winner* depend on the ladder order.
    Ballots mirror the checked-in cases in 01_STAR/tie_break_dead_rung/.
    """
    c = cap
    if round_ == "full":
        # Full symmetric tie: k candidates, k ballots, ballot i gives candidate i
        # the score `cap` and everyone else 0 (an identity matrix × cap). Every
        # candidate totals `cap`, every pairwise is 1-1, and (cap < 5) nobody has a
        # 5 -> a dead rung. Nothing separates them: the lot alone decides, and any
        # of the k candidates can win. rung / adversarial do not apply.
        k = candidates
        rows = [[c if i == j else 0 for j in range(k)] for i in range(k)]
        pad_note = ""
        if pad > 0:
            # "Less obvious" padding: for each block, append the orbit of a noise
            # score vector under ALL candidate relabelings — i.e. its distinct
            # permutations. The orbit treats every candidate identically, so it
            # preserves the exact tie (totals, pairwise, AND five-star all stay
            # equal) while burying it in varied-looking ballots. Then shuffle so the
            # tidy identity rows don't stand out.
            #
            # KEY: a vector with REPEATED scores has a far smaller orbit. All-distinct
            # entries give k! ballots (720 at k=6); a half-cap/half-zero vector like
            # [4,4,4,0,0,0] gives only k!/(m!·(k-m)!) = 20 — same symmetry, readable
            # file. We dedup with set() so repeats don't re-inflate the count.
            import itertools
            import random as _random
            rng = _random.Random(seed)
            for b in range(pad):
                if pad_vector is not None:
                    v = list(pad_vector)           # explicit --pad-vector (same each block)
                else:
                    # Default: block b puts (b+1) candidates at `cap`, the rest at 0
                    # (clamped to k-1 so it's never all-cap). Repeated scores keep the
                    # orbit small; distinct block shapes keep multiple blocks varied.
                    n_cap = min(b + 1, k - 1)
                    v = [c] * n_cap + [0] * (k - n_cap)
                orbit = sorted(set(itertools.permutations(v)))
                rows.extend(list(p) for p in orbit)
            rng.shuffle(rows)
            pad_note = (f" Padded with {pad} symmetric noise block(s) "
                        f"({len(rows)} ballots total) so the tie is non-obvious.")
        pct = f"{(k - 1)}/{k}"
        teach = (f"all {k} candidates perfectly symmetric (capped at {c}); "
                 f"every rung ties -> the LOT alone decides. {k} winners are reachable; "
                 f"a random draw diverges from a published order {pct} of the time." + pad_note)
        return Template(k, rows, list(range(k)), 0, teach)

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
    ballot_lines = "\n".join(["  " + header]
                             + ["  " + ",".join(str(s) for s in r) for r in rows])
    winner = cols[t.winner]

    lot_line = ""
    if t.lot is not None:
        lot_line = "lot_numbers: [" + ", ".join(cols[i] for i in t.lot) + "]\n"

    if title is None:
        if round_ == "full":
            title = (f"Full symmetric dead-rung tie — {t.ncols} candidates, "
                     f"cap {cap} ({winner} wins by lot [{', '.join(cols)}])")
        else:
            adv = " (adversarial lot)" if adversarial else ""
            capnote = f", cap {cap}" if rung == "dead" else ""
            title = (f"Dead rung — {round_} round, {rung} five-star rung{capnote}{adv}")

    if round_ == "full":
        description = (
            f"Generated FULL symmetric dead-rung tie ({t.ncols} candidates). "
            + t.teach + " "
            "Every candidate is a perfect rotation of the others, so no STAR rung "
            "(pairwise, five-star) can separate them and the pre-published lot order "
            "picks the winner. This is the k-candidate analog of BV jfk7pd. "
            "See 01_STAR/tie_break_dead_rung/README.md and "
            "00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md."
        )
    else:
        description = (
            f"Generated dead-rung scenario ({round_} round, '{rung}' five-star rung"
            + (", adversarial lot" if adversarial else "") + "). "
            + t.teach + " "
            "STAR's second rung counts only score-5 votes and never steps down to 4s; "
            "when it can't separate the tied candidates the lot decides. "
            "See 01_STAR/tie_break_dead_rung/README.md and "
            "00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md."
        )

    # Flat schema (top-level keys) to match tie_break_dead_rung/ cases 01-09,
    # so the file is auto-discovered by test_single_winner_positive.
    return f"""\
election_title: {title!r}

scenario_description: |-
  {description}

{OPTIONS_BLOCK}

num_winners: 1
voting_method: STAR
{lot_line}ballots: |-
{ballot_lines}

expected_winners:
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
    p.add_argument("--round", choices=["scoring", "runoff", "full"], default="scoring",
                   help="where the tie sits: scoring, runoff, or 'full' (a fully "
                        "symmetric k-candidate tie; use --candidates) (default scoring)")
    p.add_argument("--rung", choices=["alive", "dead", "tied"], default="alive",
                   help="state of the five-star rung (default alive; ignored for --round full)")
    p.add_argument("--candidates", type=int, default=3,
                   help="number of candidates for --round full (>=2; default 3). "
                        "Any of the k can win by lot; divergence is (k-1)/k.")
    p.add_argument("--cap", type=int, choices=[4, 3, 2], default=4,
                   help="score ceiling for a DEAD / full rung -- the 'what about 4s?' knob (default 4)")
    p.add_argument("--adversarial-lot", action="store_true",
                   help="pin the lot to favor the wrong candidate (strict regression test)")
    p.add_argument("--scale", type=int, default=1,
                   help="duplicate the ballot block N times for a bigger electorate (default 1)")
    p.add_argument("--pad", type=int, default=0,
                   help="[--round full only] add N symmetric 'noise' blocks (each = the "
                        "distinct permutations of a repeated-score vector) to bury the tie "
                        "in varied-looking ballots. The tie stays mathematically exact. "
                        "Repeated scores keep each block small. (default 0)")
    p.add_argument("--pad-vector", default=None,
                   help="[--round full only] explicit noise vector, e.g. '4,4,4,0,0,0' "
                        "(length must equal --candidates). Its distinct permutations form "
                        "one balanced block. Fewer distinct values = shorter file. "
                        "Default: half the candidates at --cap, half at 0.")
    p.add_argument("--seed", type=int, default=None,
                   help="random seed for --pad (reproducible ballots)")
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
    if args.round == "full":
        if args.candidates < 2:
            raise SystemExit("error: --round full needs --candidates >= 2.")
        if args.adversarial_lot or args.rung != "alive":
            print("note: --round full ignores --rung / --adversarial-lot "
                  "(it's an inherently symmetric dead rung).", file=sys.stderr)
        if args.pad < 0:
            raise SystemExit("error: --pad must be >= 0.")
        if args.pad_vector is not None:
            try:
                pad_vector = [int(x) for x in args.pad_vector.split(",")]
            except ValueError:
                raise SystemExit("error: --pad-vector must be comma-separated integers, "
                                 "e.g. '4,4,4,0,0,0'.")
            if len(pad_vector) != args.candidates:
                raise SystemExit(f"error: --pad-vector has {len(pad_vector)} entries but "
                                 f"--candidates is {args.candidates}; lengths must match.")
            if any(x < 0 or x > args.cap for x in pad_vector):
                raise SystemExit(f"error: --pad-vector entries must be between 0 and "
                                 f"--cap ({args.cap}).")
            args.pad_vector = pad_vector
        # Orbit size = distinct permutations of the (repeated-score) noise vector.
        from math import factorial
        from collections import Counter
        if args.pad:
            def _orbit(vec):
                n = factorial(len(vec))
                for m in Counter(vec).values():
                    n //= factorial(m)
                return n
            if args.pad_vector is not None:
                total = _orbit(args.pad_vector) * args.pad
            else:
                half = args.candidates // 2
                total = sum(_orbit([1] * min(b + 1, args.candidates - 1) +
                                   [0] * (args.candidates - min(b + 1, args.candidates - 1)))
                            for b in range(args.pad))
            if total > 1000:
                print(f"note: the noise blocks add {total} ballots. Use a --pad-vector with "
                      f"more repeated scores (e.g. '{args.cap},0,0,...'), fewer --pad blocks, "
                      f"or fewer --candidates for a shorter file.", file=sys.stderr)
    else:
        if args.pad:
            print("note: --pad only applies to --round full; ignored here.", file=sys.stderr)
        if args.rung != "dead" and args.cap != 4:
            print("note: --cap only applies to a dead rung; ignored here.", file=sys.stderr)
        if args.adversarial_lot and args.rung == "dead" and args.cap != 4:
            print("note: adversarial dead template is fixed at cap 4; --cap ignored.", file=sys.stderr)
            args.cap = 4

    t = build_template(args.round, args.rung, args.adversarial_lot, args.cap,
                       candidates=args.candidates, pad=args.pad, seed=args.seed,
                       pad_vector=(args.pad_vector if args.round == "full" else None))
    names = NAME_BANKS[args.theme]
    if t.ncols > len(names):
        raise SystemExit(
            f"error: theme '{args.theme}' has {len(names)} names but {t.ncols} are "
            f"needed. Use --theme letters (26) or fewer --candidates.")

    yaml_text = render_yaml(t, names, args.scale, args.round, args.rung,
                            args.adversarial_lot, args.cap, args.title)

    if args.round == "full":
        auto_name = f"dead_rung_full_c{args.candidates}_cap{args.cap}"
        if args.pad:
            auto_name += f"_pad{args.pad}" + (f"_s{args.seed}" if args.seed is not None else "")
    else:
        auto_name = (f"dead_rung_{args.round}_{args.rung}"
                     + (f"_cap{args.cap}" if args.rung == "dead" else ""))
    auto_name += ("_advlot" if (args.adversarial_lot and args.round != "full") else "")
    auto_name += (f"_x{args.scale}" if args.scale > 1 else "") + ".yaml"

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
