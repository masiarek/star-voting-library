# `generate_flat_tie_scenarios.py` — build "strange" flat-score / tie STAR elections

A small generator for the deliberately-degenerate elections documented in
[Flat scores, ties & tie-breaking (all cases)](../../01_STAR/Flat_scores_ties/README.md):
elections where several candidates tie at **every** score-based step, so STAR
falls all the way through its tie-break cascade and the **lot order** is the only
thing left to decide the winner. You hand it a size (candidates × ballots) and it
prints a ready-to-tabulate YAML election.

Why these matter: they're the worst case for any STAR implementation. A correct
engine must resolve them *deterministically* and *show its work*; several
BetterVoting bugs (#1052 "no ballots cast", #1035 "NaN", #1379 wrong finalists,
#1407 flat-ballot-as-abstention) are exactly failures to handle this shape. This
script lets you spin up that shape at any size on demand.

---

## The idea in one picture

Every voter gives the tied candidates the **same** score. So nothing on the
ballots separates them — not the totals, not head-to-head, not the count of top
scores. Here's the whole scenario for 3 candidates, 4 ballots, all 5s:

```
A, B, C
5, 5, 5
5, 5, 5
5, 5, 5
5, 5, 5
```

- **Scoring Round:** A, B, C each total 20 → a 3-way tie for the two finalist slots.
- **Tiebreak 1 (head-to-head):** every pair is 0–0 "Equal Support" → still tied.
- **Tiebreak 2 (most 5s):** all equal → still tied.
- **Tiebreak 3 (lot number):** the published order `[A, B, C]` picks **A, B** as finalists.
- **Automatic Runoff:** A vs B is 0–0 → tied again → the cascade repeats → lot picks **A**.

**Winner: A** — chosen entirely by the lot order, because the ballots were
silent. That determinism (same ballots + same lot ⇒ same winner, every time, and
every step printed) is the property the scenario is built to test.

> **"But `5,5,5,0` works fine, right?"** No — that's still a 3-way tie among the
> top three (all total the same). What actually avoids a tie is an *unambiguous
> top two and a decisive runoff*. The honest contrast is **tie vs no-tie**, not
> flat vs not-flat. This script always builds the tie on purpose.

---

## What it produces

A single YAML election in the house schema used by `Flat_scores_ties/` — the
minimal options block, a `lot_numbers:` line (so the result is reproducible), and
an `expected_results.winners:` assertion (always the lot favorite, candidate A),
so the file doubles as a positive test case:

```yaml
election:
  election_title: Flat-tie scenario — 3-way tie, 3 candidates, 4 ballots (highest=5)
  election_description: |-
    Generated strange scenario: all 3 candidates scored 5 by every voter -> a
    fully-flat, maximal tie. ...
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
    count_separator: "×"
  races:
  - race_id: '0'
    num_winners: 1
    voting_method: STAR
    ballots: |-
      A, B, C
      5, 5, 5
      5, 5, 5
      5, 5, 5
      5, 5, 5
    lot_numbers: [A, B, C]
    expected_results:
      winners:
      - A
```

By default the YAML is printed **to the screen only** — nothing is written to
disk unless you ask (`--out`). That keeps the "where did the file go?" question
out of the way while you experiment.

---

## Parameters

| Flag | Meaning | Default |
|------|---------|---------|
| `-c`, `--candidates N` | number of candidates (columns) | `3` |
| `-b`, `--ballots N` | number of (identical) ballots (rows) | `4` |
| `-t`, `--tie N` | how many of the top candidates tie | all candidates |
| `--highest {5,4,3,2}` | the flat score the tied candidates share | `5` |
| `--loser {4,3,2,1,0}` | score for the non-tied also-rans (must be `< --highest`) | `1` |
| `--theme {letters,names,fruits,flavors,capitals}` | candidate name bank (lot order) | `letters` |
| `--title "…"` | override the generated `election_title` | auto |
| `-o`, `--out PATH` | save to a file (or a directory, auto-named). Omit → screen only | — |
| `--run` | tabulate the file with the LH engine after writing | off |
| `--compare-bv` | report whether BV's random tie-break could pick a different winner | off |
| `--draws N` | random draws for the `--compare-bv` Monte Carlo | `10000` |
| `--seed N` | seed for reproducible `--compare-bv` draws | none |

### `--highest` — the "it's not just 5s" knob

A flat tie has nothing to do with the number 5. `4,4,4`, `3,3,3`, `2,2,2` all tie
exactly the same way `5,5,5` does — the totals are still equal and every pairwise
is still 0–0. `--highest` lets you show that directly. (This is the parameter you
asked for: `highest_4_or_3_or_2`.)

### `--tie` — full tie vs partial tie

- `--tie == --candidates` (default): a **fully-flat** ballot — everyone ties
  (the case 07 shape).
- `--tie < --candidates`: the top `--tie` candidates tie for the finalist slots
  while the remaining `--candidates − --tie` also-rans sit decisively lower at
  `--loser`. This is the case 04 (2-way), 05 (3-way), 06 (4-way) shape. The
  winner is still the lot favorite among the tied group (candidate A).

---

## Worked examples

**1) Default — 3-way tie at every step, printed to screen.**

```
python generate_flat_tie_scenarios.py -c 3 -b 4
```

Prints the YAML above and nothing is saved.

**2) The `--highest` point — a top-3 tie at 3s with a clear loser, themed cast.**

```
python generate_flat_tie_scenarios.py -c 4 -b 6 -t 3 --highest 3 --loser 0 --theme flavors
```

Ballots become:

```
Almond, Brownie, Cocoa, Dulce
3, 3, 3, 0
3, 3, 3, 0
...(6 rows)
```

Almond/Brownie/Cocoa tie at 18; Dulce is out at 0; the lot picks Almond.

**3) Generate and tabulate in one step (verify the winner).**

```
python generate_flat_tie_scenarios.py -c 5 -b 5 --highest 2 --run
```

Writes a temp file, runs the LH engine, and prints the full audit — you'll see
the scoring round tie, each tiebreaker step, and `Winner … A`. (`--run` needs a
file, so with no `--out` it uses a temp file and tells you the path.)

**4) Save it into a folder.**

```
python generate_flat_tie_scenarios.py -c 4 -b 5 --highest 4 -o ../../01_STAR/Flat_scores_ties/
```

Saves `flat_tie_c4_b5_t4_h4.yaml` there (directory → auto-named).

---

## `--compare-bv`: would BetterVoting and this script pick *different* winners?

**Short answer: yes — and often.** This is the subtle, important part.

When the tie is total, the ballots decide *nothing* about the winner — the
**tie-break order** decides everything. Proof: take the same ballots and only
change the lot order.

```
lot_numbers: [A, B, C]   →  winner A
lot_numbers: [C, A, B]   →  winner C
```

Same votes, different winner, purely from the order. So the two *approaches* to
tie-breaking matter:

- **This script / the LH engine** uses a **published lot order** (`[A, B, C, …]`).
  The winner is fixed and reproducible — always candidate A.
- **BetterVoting** currently uses a **random draw** each time it hits a tie. Its
  winner is uniform over the tied candidates.

They agree only when BV's random draw happens to put A first — probability
`1/tie`. So they **disagree with probability `(tie − 1)/tie`**:

| tied candidates | chance BV ≠ this script |
|:--:|:--:|
| 2 | 1/2 = 50% |
| 3 | 2/3 ≈ 67% |
| 4 | 3/4 = 75% |
| 5 | 4/5 = 80% |

`--compare-bv` shows this concretely — one representative random draw, the exact
probability, and a Monte Carlo distribution:

```
python generate_flat_tie_scenarios.py -c 3 -b 4 --compare-bv --seed 1
```

```
BV (random tie-break)  vs  this script (published lot)  —  do they differ?
  Tied finalists (nobody separated by ballots): A, B, C
  LH / this script  — published lot, A-first  -> always A
  BV — one random draw ['B', 'C', 'A']  -> B   << DIFFERENT winner!
  Exact chance they DIFFER: (tie-1)/tie = 2/3 = 67%
  Monte Carlo over 10,000 random draws:
    A            3,277 (32.8%) ██████████  <- LH winner
    B            3,369 (33.7%) ██████████
    C            3,354 (33.5%) ██████████
  => BV picked a DIFFERENT winner than this script in 6,723/10,000 (67%) of draws.
```

This is exactly the argument behind BetterVoting issue
[#1063 — deterministic lot-number tie-breaking](https://github.com/Equal-Vote/bettervoting/issues/1063):
without a *pre-published* lot, a genuine tie can flip to a different winner every
time you re-run the count. LH already implements the published-lot rule; BV, so
far, does not. (The randomized order is now at least *exported*, per
[#1371](https://github.com/Equal-Vote/bettervoting/issues/1371), so an outside
engine can import it and reproduce a given BV result after the fact.)

> **Modeling note.** `--compare-bv` treats BV's tie-break as a uniform random
> draw over the tied candidates, which is faithful *for these total-tie
> scenarios* — the winner is provably the first tied candidate in whatever order
> the tie-breaker produces (verified against the LH engine by reordering the
> lot). It does not model any partial ordering BV might apply before the random
> step; for these fully-symmetric ties there is none.

---

## How it guarantees the tie (implementation notes)

- **Identical rows.** Every ballot is the same row, and the tied candidates share
  one score. Identical columns guarantee equal totals *and* 0–0 pairwise, so the
  tie survives head-to-head and most-5s, not just the raw sum. Any asymmetry could
  break a step, so the generator keeps the tied block perfectly symmetric.
- **Losers go last.** Non-tied also-rans get the last columns and a lower score,
  so they're eliminated cleanly and the tied group occupies the finalist slots.
- **Winner = candidate A.** `lot_numbers` is the candidate order, so the
  deterministic winner is always the first candidate — which the file asserts in
  `expected_results.winners`, making every generated file a valid positive test.
- **Engine discovery for `--run`.** The script finds
  `starvote_larry_hastings.py` by walking up from the output file *and* from its
  own location, so `--run` works even when the YAML is written to a temp dir
  outside the repo.

---

## Where this lives / related

- Script: `generate_flat_tie_scenarios.py` (this folder, `tools_adam/`).
- The hand-built case set this generalizes:
  [Flat scores, ties & tie-breaking (all cases)](../../01_STAR/Flat_scores_ties/README.md).
- Concept backing:
  [STAR Tie-Breaking](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
  · [The Automatic Runoff Round](../../00_start_here/STAR_Voting/STAR_Automatic_Runoff.md)
  · [reporting true ties](../../00_start_here/STAR_reporting/reporting_ties.md).
