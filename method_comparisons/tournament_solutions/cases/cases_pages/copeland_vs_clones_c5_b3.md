---
search:
  exclude: true
---

# Copeland picks one, composition-consistency demands all five (tournament solutions)

*Generated from [`copeland_vs_clones_c5_b3.yaml`](../copeland_vs_clones_c5_b3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** D

## Scenario

The companion case: where Ranked Robin's simple count and the literature's favourite structural axiom flatly disagree. Three voters, five candidates: A>B>C>E>D, D>C>A>B>E, E>D>B>C>A. Again every head-to-head is decided, so this is a genuine tournament, and again there is no Condorcet winner. The graph has a shape worth seeing: A, B and C form a rock-paper-scissors 3-cycle; D beats all three of them; E beats D; and A, B, C all beat E. So the whole thing is one big cycle at a higher level — {A,B,C} -> E -> D -> {A,B,C}. Because {A,B,C} is a COMPONENT (all three stand in the same relation to D and to E), the tournament decomposes into {A,B,C}, {D}, {E} with a 3-cycle summary. Composition-consistency — "choose the best from the best components" — then forces a solution to select ALL FIVE candidates, since nonemptiness and neutrality make a 3-cycle unsplittable. The uncovered, Banks and bipartisan sets duly return all five. Copeland does not. D has the most wins (3, over A, B and C) so the Copeland set is {D} alone, and Ranked Robin elects D outright with no tiebreak. That is not a bug in the engine — it is Copeland failing composition-consistency, a known and published limit of the rule (chapter Section 3.3.1), and the same arithmetic behind Ranked Robin's one clone-independence weakness, teaming (see 05_Ranked_Robin/concepts/rr_clone_independence.md). This is Figure 3.1 / 3.2 of Brandt, Brill & Harrenstein, "Tournament Solutions" (Handbook of Computational Social Choice, 2016, ch. 3) — their own three-voter profile, run through this repo's engines. Bare A-E labels match the figure on purpose. Verified two ways: LH's Ranked Robin below, and pref_voting's C1 module via tournament_solutions_report.py. LH-only: nothing here needs a live BetterVoting election, and the teaching point is the disagreement between two published rules, not a live tally.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
A>B>C>E>D
D>C>A>B>E
E>D>B>C>A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (ranked ballots).

Ballots:
     1 × A > B > C > E > D
     1 × D > C > A > B > E
     1 × E > D > B > C > A

Round-Robin — every pair, head-to-head (For – Against):
   A  beats B   2 – 1
   C  beats A   2 – 1
   A  beats E   2 – 1
   D  beats A   2 – 1
   B  beats C   2 – 1
   B  beats E   2 – 1
   D  beats B   2 – 1
   C  beats E   2 – 1
   D  beats C   2 – 1
   E  beats D   2 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |     A     |    B     |    C     |    E     |    D     |
---------------------------------------------------------------
  A > |    ---    |2 - 0 - 1 |1 - 0 - 2 |2 - 0 - 1 |1 - 0 - 2 |
  B > | 1 - 0 - 2 |   ---    |2 - 0 - 1 |2 - 0 - 1 |1 - 0 - 2 |
  C > | 2 - 0 - 1 |1 - 0 - 2 |   ---    |2 - 0 - 1 |1 - 0 - 2 |
  E > | 1 - 0 - 2 |1 - 0 - 2 |1 - 0 - 2 |   ---    |2 - 0 - 1 |
  D > | 2 - 0 - 1 |2 - 0 - 1 |2 - 0 - 1 |1 - 0 - 2 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  D          3–1–0         3      +2  A, B, C
    2  A          2–2–0         2      +0  B, E
    3  B          2–2–0         2      +0  C, E
    4  C          2–2–0         2      +0  A, E
    5  E          1–3–0         1      -2  D

Winner — Ranked Robin (RCV-RR): D
   the most head-to-head wins (3).
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (5 of 5): D, A, B, C, E
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   Note: the Copeland leaders (D) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner D is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/copeland_vs_clones_c5_b3_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/tournament_solutions/cases/copeland_vs_clones_c5_b3.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [five_answers_one_election_c4_b3](five_answers_one_election_c4_b3.md) · [star_elects_a_covered_candidate_c4_b5](star_elects_a_covered_candidate_c4_b5.md)
