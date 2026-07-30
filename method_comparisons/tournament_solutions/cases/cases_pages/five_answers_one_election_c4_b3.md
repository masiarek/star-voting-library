# Five defensible answers, one three-ballot election (tournament solutions)

*Generated from [`five_answers_one_election_c4_b3.yaml`](../five_answers_one_election_c4_b3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** B

## Scenario

The smallest election that makes the whole tournament-solutions literature necessary. Three voters, four candidates, ballots that are just one ranking rotated: A>B>C>D, B>C>D>A, D>A>B>C. Every head-to-head is decided (no ties), so the pairwise results form a genuine TOURNAMENT — a complete directed graph. There is no Condorcet winner: D beats A, so the top of the graph cycles. Now the famous C1 rules, which read ONLY that graph, split five ways: Top cycle / Schwartz = {A, B, C, D} (everyone); Uncovered set = Banks set = Bipartisan set = {A, B, D} (C is COVERED — B beats C and beats everyone C beats, so C is strictly redundant); Copeland set = {A, B} (both win 2, C and D win 1); Slater set = Markov set = {A}. Five different answers to "who should win," each with a published defense, from three ballots. Ranked Robin is the Copeland set, so the LH engine lands on {A, B} and must break the tie — by TOTAL MARGIN, electing B (+3 vs A's +1). That step is the lesson: margins are not in the tournament. The moment Ranked Robin consults them it has left C1 and is reading C2 information, and it elects B where Slater and Markov both elect A. This is Figure 3.3 of Brandt, Brill & Harrenstein, "Tournament Solutions" (Handbook of Computational Social Choice, 2016, ch. 3), turned back into ballots — the chapter gives the graph, and McGarvey's theorem guarantees some profile produces it; this three-voter rotation is one. Candidate labels are kept as bare A/B/C/D deliberately, matching the figure, so the book can be read side by side with the tabulation. Verified two ways: the LH engine's Ranked Robin below, and pref_voting's independent C1 module via tournament_solutions_report.py. LH-only by necessity — the winner turns on a Copeland tiebreak, and BetterVoting breaks Ranked Robin ties at random, so this result is not freezable on BV.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
A>B>C>D
B>C>D>A
D>A>B>C
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (ranked ballots).

Ballots:
     1 × A > B > C > D
     1 × B > C > D > A
     1 × D > A > B > C

Round-Robin — every pair, head-to-head (For – Against):
   A  beats B   2 – 1
   A  beats C   2 – 1
   D  beats A   2 – 1
   B  beats C   3 – 0
   B  beats D   2 – 1
   C  beats D   2 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |     A     |    B     |    C     |    D     |
----------------------------------------------------
  A > |    ---    |2 - 0 - 1 |2 - 0 - 1 |1 - 0 - 2 |
  B > | 1 - 0 - 2 |   ---    |3 - 0 - 0 |2 - 0 - 1 |
  C > | 1 - 0 - 2 |0 - 0 - 3 |   ---    |2 - 0 - 1 |
  D > | 2 - 0 - 1 |1 - 0 - 2 |1 - 0 - 2 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  B          2–1–0         2      +3  D, C
    2  A          2–1–0         2      +1  B, C
    3  D          1–2–0         1      -1  A
    4  C          1–2–0         1      -3  D

Winner — Ranked Robin (RCV-RR): B
   *** 2 candidates tie for the most wins (A, B) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by total margin, then lot order.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): A, B, C, D
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   Note: the Copeland leaders (A, B) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner B is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/five_answers_one_election_c4_b3_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/tournament_solutions/cases/five_answers_one_election_c4_b3.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [copeland_vs_clones_c5_b3](copeland_vs_clones_c5_b3.md) · [star_elects_a_covered_candidate_c4_b5](star_elects_a_covered_candidate_c4_b5.md)
