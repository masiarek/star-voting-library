#!/usr/bin/env python3
"""Generate 'strange' flat-score / tie STAR scenarios as tabulatable YAML.

These are the deliberately-degenerate elections documented in
`01_STAR/Flat_scores_ties/README.md`: several candidates tie at *every*
score-based tiebreaker, so STAR falls all the way through its cascade
(head-to-head -> most 5s -> lot number) and the pre-published **lot order**
decides the winner. That determinism is the whole lesson, and it's what several
BetterVoting bugs (#1052, #1035, #1379, #1407) fail to reproduce.

The generator makes the tie reproducible by construction:

  * The top `--tie` candidates are scored **identically** (`--highest`) on every
    ballot, so their column totals are equal AND every pairwise matchup between
    them is 0-0 "Equal Support" -- the tie survives head-to-head and most-5s.
  * Any remaining candidates are scored `--loser` (< highest) so they're
    decisively out (unless `--tie` == candidates, i.e. a fully-flat ballot).
  * `lot_numbers` is the candidate order (A, B, C, ...), so the deterministic
    winner is always the first candidate -- which the file asserts in
    `expected_results`.

Parameters
----------
  -c/--candidates N   how many candidates (columns)            [default 3]
  -b/--ballots N      how many identical ballots (rows)         [default 4]
  -t/--tie N          how many top candidates tie               [default = candidates]
  --highest {5,4,3,2} the flat score the tied candidates share  [default 5]
  --loser {4,3,2,1,0} score for the non-tied also-rans          [default 1]
  --theme ...         candidate name bank (letters/names/...)   [default letters]

The `--highest` knob makes the README's point that flat ties aren't a "5s only"
artifact: `4,4,4` or `2,2,2` tie exactly the same way `5,5,5` does.

Examples
--------
  # 3-way tie at every step, 4 ballots, all 5s (case 06/07 shape)
  python generate_flat_tie_scenarios.py -c 3 -b 4

  # 4 candidates, top 3 tie at 3s, one loser -- "5,5,5,0 is still a tie" made general
  python generate_flat_tie_scenarios.py -c 4 -b 6 -t 3 --highest 3 --loser 0

  # generate and immediately tabulate to check the winner
  python generate_flat_tie_scenarios.py -c 5 -b 5 --highest 2 --run

  # would BV's random tie-break disagree with this script's published lot?
  python generate_flat_tie_scenarios.py -c 3 -b 4 --compare-bv

Full write-up (concept, every parameter, the BV-vs-LH divergence, worked
examples): see generate_flat_tie_scenarios.md next to this script.
"""
from __future__ import annotations

import argparse
import string
import subprocess
import sys
import tempfile
from pathlib import Path

# Candidate name banks, in lot-priority order (distinct initials A, B, C, ...).
NAME_BANKS: dict[str, list[str]] = {
    "letters": list(string.ascii_uppercase),
    "names":   ["Ava", "Ben", "Cara", "Dan", "Eve", "Finn", "Gwen", "Hana",
                "Ike", "Jo", "Kai", "Lena"],
    "fruits":  ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig",
                "Grape", "Honeydew", "Kiwi", "Lemon"],
    "flavors": ["Almond", "Brownie", "Cocoa", "Dulce", "Espresso", "Fudge",
                "Ginger", "Hazelnut", "Irish", "Java"],
    "capitals": ["Athens", "Berlin", "Cairo", "Delhi", "Edinburgh", "Florence",
                 "Geneva", "Helsinki", "Istanbul", "Jakarta"],
}

# The house "minimal + score-distribution" options block used by this case set
# (matches the existing Flat_scores_ties_*.yaml files).
OPTIONS_BLOCK = """\
  options:
    show_description: false
    show_matrix: false
    matrix_finalists_only: true
    show_condorcet: false
    show_score_counts: true
    show_irv: false
    show_runoff_percent: true
    brief: true
    collapse_ballots: false
    count_separator: "×"\
"""


def build_names(count: int, theme: str) -> list[str]:
    bank = NAME_BANKS[theme]
    if count > len(bank):
        raise SystemExit(
            f"error: theme '{theme}' has only {len(bank)} names; "
            f"need {count}. Use --theme letters (26) or fewer candidates."
        )
    return bank[:count]


def build_ballot_rows(names: list[str], ballots: int, tie: int,
                      highest: int, loser: int) -> list[str]:
    """One identical row per ballot: first `tie` cols = highest, rest = loser."""
    scores = [highest] * tie + [loser] * (len(names) - tie)
    row = ", ".join(str(s) for s in scores)
    return [row] * ballots


def build_yaml(names: list[str], ballots: int, tie: int, highest: int,
               loser: int, title: str | None) -> str:
    winner = names[0]
    header = ", ".join(names)
    rows = build_ballot_rows(names, ballots, tie, highest, loser)
    ballots_block = "\n".join(["      " + header] + ["      " + r for r in rows])
    lot = "[" + ", ".join(names) + "]"

    n_losers = len(names) - tie
    if tie == len(names):
        shape = (f"all {len(names)} candidates scored {highest} by every voter "
                 f"-> a fully-flat, maximal tie")
    else:
        shape = (f"the top {tie} candidates tie at {highest} while "
                 f"{n_losers} also-ran(s) sit at {loser}")

    if title is None:
        title = (f"Flat-tie scenario — {tie}-way tie, {len(names)} candidates, "
                 f"{ballots} ballots (highest={highest})")

    description = (
        f"Generated strange scenario: {shape}. The tie survives every "
        f"score-based tiebreaker (head-to-head 0-0, equal most-{highest}s), so "
        f"the lot order decides -> {winner}. Demonstrates that a flat tie is not "
        f"a '5s-only' artifact: highest={highest} ties exactly like 5s do. "
        f"See Flat_scores_ties/README.md. (BV id pending.)"
    )

    return f"""\
election:
  election_title: {title}
  election_description: |-
    {description}
{OPTIONS_BLOCK}
  races:
  - race_id: '0'
    race_description: "generated by generate_flat_tie_scenarios.py"
    num_winners: 1
    voting_method: STAR
    ballots: |-
{ballots_block}
    lot_numbers: {lot}
    expected_results:
      winners:
      - {winner}

# file generated by generate_flat_tie_scenarios.py
"""


def compare_bv(names: list[str], tie: int, draws: int, seed: int | None) -> None:
    """Show whether BV's *random* tie-break could disagree with LH's *published* lot.

    In a total tie among the top `tie` candidates the ballots separate nobody, so
    the winner is decided entirely by tie-break order (proven: reorder the lot,
    the winner moves with it). LH uses a fixed published order -> names[0] always
    wins. BV currently draws a random order, so its winner is uniform over the
    tied candidates. They agree only when BV's draw happens to put names[0] first
    (prob 1/tie); they DIFFER with probability (tie-1)/tie.
    """
    import random as _random

    rng = _random.Random(seed)
    tied = names[:tie]
    lh_winner = names[0]

    # One representative BV random draw.
    sample = tied[:]
    rng.shuffle(sample)
    bv_sample_winner = sample[0]

    # Monte Carlo over random draws (models BV's random tie-break).
    counts = {c: 0 for c in tied}
    for _ in range(draws):
        order = tied[:]
        rng.shuffle(order)
        counts[order[0]] += 1
    differ = draws - counts[lh_winner]
    exact_p = (tie - 1) / tie

    print("═" * 70)
    print("BV (random tie-break)  vs  this script (published lot)  —  do they differ?")
    print(f"  Tied finalists (nobody separated by ballots): {', '.join(tied)}")
    print(f"  LH / this script  — published lot, {lh_winner}-first  -> always {lh_winner}")
    print(f"  BV — one random draw {sample}  -> {bv_sample_winner}"
          + ("   << DIFFERENT winner!" if bv_sample_winner != lh_winner
             else "   (same as LH this time)"))
    print(f"  Exact chance they DIFFER: (tie-1)/tie = {tie - 1}/{tie} = {exact_p:.0%}")
    print(f"  Monte Carlo over {draws:,} random draws:")
    for c in tied:
        pct = counts[c] / draws
        bar = "█" * round(pct * 30)
        flag = "  <- LH winner" if c == lh_winner else ""
        print(f"    {c:<10} {counts[c]:>7,} ({pct:5.1%}) {bar}{flag}")
    print(f"  => BV picked a DIFFERENT winner than this script in "
          f"{differ:,}/{draws:,} ({differ / draws:.0%}) of draws.")
    print("═" * 70)


def find_engine(start: Path) -> Path | None:
    """Walk upward for STARVote_LH_tabulation_engine/starvote_larry_hastings.py."""
    for parent in [start, *start.parents]:
        cand = parent / "STARVote_LH_tabulation_engine" / "starvote_larry_hastings.py"
        if cand.exists():
            return cand
    return None


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Generate flat-score / tie STAR scenarios (see module docstring).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("-c", "--candidates", type=int, default=3,
                   help="number of candidates / columns (default 3)")
    p.add_argument("-b", "--ballots", type=int, default=4,
                   help="number of identical ballots / rows (default 4)")
    p.add_argument("-t", "--tie", type=int, default=None,
                   help="how many top candidates tie (default: all candidates)")
    p.add_argument("--highest", type=int, choices=[5, 4, 3, 2], default=5,
                   help="flat score shared by the tied candidates (default 5)")
    p.add_argument("--loser", type=int, choices=[4, 3, 2, 1, 0], default=1,
                   help="score for the non-tied also-rans (default 1)")
    p.add_argument("--theme", choices=sorted(NAME_BANKS), default="letters",
                   help="candidate name bank (default letters)")
    p.add_argument("--title", default=None, help="override the election_title")
    p.add_argument("-o", "--out", default=None,
                   help="save to this file (or DIR, auto-named). "
                        "Omit to print to screen only.")
    p.add_argument("--run", action="store_true",
                   help="tabulate the file with the LH engine after writing")
    p.add_argument("--compare-bv", action="store_true",
                   help="show whether BV's random tie-break could pick a "
                        "different winner than this script's published lot")
    p.add_argument("--draws", type=int, default=10000,
                   help="random draws for the --compare-bv Monte Carlo (default 10000)")
    p.add_argument("--seed", type=int, default=None,
                   help="random seed for --compare-bv (reproducible draws)")
    args = p.parse_args(argv)

    tie = args.candidates if args.tie is None else args.tie

    # Validation.
    if args.candidates < 2:
        raise SystemExit("error: need at least 2 candidates.")
    if args.ballots < 1:
        raise SystemExit("error: need at least 1 ballot.")
    if not (2 <= tie <= args.candidates):
        raise SystemExit(
            f"error: --tie must be between 2 and --candidates ({args.candidates}); got {tie}."
        )
    if args.loser >= args.highest:
        raise SystemExit(
            f"error: --loser ({args.loser}) must be below --highest ({args.highest}) "
            f"so the also-rans actually lose."
        )

    names = build_names(args.candidates, args.theme)
    yaml_text = build_yaml(names, args.ballots, tie, args.highest, args.loser, args.title)
    auto_name = f"flat_tie_c{args.candidates}_b{args.ballots}_t{tie}_h{args.highest}.yaml"

    # Decide the destination.
    #   (no --out)      -> print the YAML to the screen only (no file written).
    #   --out FILE/DIR  -> write there (a directory gets the auto-name appended).
    #   --run           -> a file is required, so with no --out we use a temp file
    #                      and tell you exactly where it landed.
    out: Path | None = None
    if args.out:
        out = Path(args.out)
        if out.is_dir():
            out = out / auto_name
    elif args.run:
        out = Path(tempfile.gettempdir()) / auto_name

    # Always echo the generated scenario (ballots in YAML format) to the screen.
    print("─" * 70)
    print(yaml_text, end="")
    print("─" * 70)

    if out is not None:
        out.write_text(yaml_text, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print("(printed to screen only — pass --out FILE to save, "
              "or --out DIR to save with an auto name)")

    if args.run:
        # Try the output file's tree first, then fall back to this script's own
        # location (which lives inside the repo even when --out is a temp dir).
        engine = find_engine(out.resolve()) or find_engine(Path(__file__).resolve())
        if engine is None:
            print("note: --run given but engine not found; skipping tabulation.",
                  file=sys.stderr)
            return 0
        print(f"tabulating with {engine.name} ...")
        proc = subprocess.run([sys.executable, str(engine), str(out)],
                              capture_output=True, text=True)
        sys.stdout.write(proc.stdout)
        if proc.returncode != 0:
            sys.stderr.write(proc.stderr)
            return proc.returncode

    if args.compare_bv:
        compare_bv(names, tie, args.draws, args.seed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
