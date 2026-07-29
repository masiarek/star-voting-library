# Ranked Robin — winning the most matchups does NOT make you the Condorcet winner

*Generated from [`bgg9qh9_most_wins_is_not_condorcet.yaml`](../bgg9qh9_most_wins_is_not_condorcet.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../concepts) · **1 seat** · **Expected winner:** Cora

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/gg9qh9) · **[results ↗](https://bettervoting.com/gg9qh9/results)** (election `gg9qh9`).

**Official tie-break (lot) order:** Amy > Blake > Cora > Diego > Erin — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

18 ranked ballots, 5 candidates, three equal blocs. A counterexample to a claim that circulates in voting-reform discussion: "if you win head-to-head against more candidates than anyone else, you must be the Condorcet winner."
Cora wins THREE of four matchups — strictly more than anyone else, not tied — and finishes 3-1-0 with a Copeland score of 3 against everyone else's 2 or 1. Cora is elected. And Amy beats Cora 12-6. So Cora is not the Condorcet winner, and in fact there is no Condorcet winner here at all: the Smith set is all five candidates.
Note what this does NOT depend on. There is not a single drawn matchup in the profile, so the raw win count and the Copeland score coincide exactly. The claim fails on its own terms — it is the converse error, not a technicality about how draws are credited. What IS true is the one-way version: a Condorcet winner always has the uniquely highest Copeland score. The converse does not follow.
Second lesson, free with the first: Cora has ZERO first-choice votes. The three blocs lead with Blake, Amy and Diego, so first choices split 6-6-6-0-0. Cora is the broadly-acceptable second choice nobody puts first, which is precisely why Cora wins the round robin — and precisely why Choose-One and RCV-IRV cannot even produce an answer here without a coin flip (both deadlock three ways at 6). That is also why this is a single Ranked Robin race on BetterVoting rather than a method line-up: the other methods' results here are not reproducible.
Live results: https://bettervoting.com/gg9qh9/results (election gg9qh9, BV2260). Triple-checked — the LH engine, BetterVoting's RankedRobin.ts (see the frozen _bv_export.json) and pref_voting's independent Copeland all elect Cora.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
6:Blake>Erin>Amy>Cora>Diego
6:Amy>Cora>Erin>Diego>Blake
6:Diego>Cora>Blake>Erin>Amy
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 18 ballots (ranked ballots).

Ballots:
     6 × Blake > Erin > Amy > Cora > Diego
     6 × Amy > Cora > Erin > Diego > Blake
     6 × Diego > Cora > Blake > Erin > Amy

Round-Robin — every pair, head-to-head (For – Against):
   Blake  beats Erin    12 –  6
   Blake  beats Amy     12 –  6
   Cora   beats Blake   12 –  6
   Diego  beats Blake   12 –  6
   Erin   beats Amy     12 –  6
   Cora   beats Erin    12 –  6
   Erin   beats Diego   12 –  6
   Amy    beats Cora    12 –  6
   Amy    beats Diego   12 –  6
   Cora   beats Diego   12 –  6

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |    Blake     |    Erin     |    Amy      |    Cora     |   Diego     |
----------------------------------------------------------------------------------
  Blake > |     ---      |12 -  0 -  6 |12 -  0 -  6 | 6 -  0 - 12 | 6 -  0 - 12 |
   Erin > |  6 -  0 - 12 |    ---      |12 -  0 -  6 | 6 -  0 - 12 |12 -  0 -  6 |
    Amy > |  6 -  0 - 12 | 6 -  0 - 12 |    ---      |12 -  0 -  6 |12 -  0 -  6 |
   Cora > | 12 -  0 -  6 |12 -  0 -  6 | 6 -  0 - 12 |    ---      |12 -  0 -  6 |
  Diego > | 12 -  0 -  6 | 6 -  0 - 12 | 6 -  0 - 12 | 6 -  0 - 12 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Cora       3–1–0         3     +12  Blake, Erin, Diego
    2  Amy        2–2–0         2      +0  Cora, Diego
    3  Blake      2–2–0         2      +0  Amy, Erin
    4  Erin       2–2–0         2      +0  Amy, Diego
    5  Diego      1–3–0         1     -12  Blake

Winner — Ranked Robin (RCV-RR): Cora
   the most head-to-head wins (3).
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (5 of 5): Cora, Blake, Erin, Amy, Diego
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   Note: the Copeland leaders (Cora) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Cora is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bgg9qh9_most_wins_is_not_condorcet_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/most_wins_vs_condorcet/cases/bgg9qh9_most_wins_is_not_condorcet.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)
