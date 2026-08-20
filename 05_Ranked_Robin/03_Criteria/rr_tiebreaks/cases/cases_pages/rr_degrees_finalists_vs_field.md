---
search:
  exclude: true
---

# The 1st Degree counts the finalists only — and it elects someone else

*Generated from [`rr_degrees_finalists_vs_field.yaml`](../rr_degrees_finalists_vs_field.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Alma

## Scenario

Twenty-six neighbours rank four candidates for a community board, and three of them — Alma, Ben and Cleo — cycle: Alma beats Ben, Ben beats Cleo, Cleo beats Alma. All three finish on two matchup wins, so all three are FINALISTS. Dane loses every matchup and is not one.
Ranked Robin's tie-breaking protocol says what to do, and this file is here because the two obvious readings of "greatest sum of win margins" give different winners:

  1st Degree — margins over THE OTHER FINALISTS.  Alma +2, Cleo 0, Ben -2.
               Alma is elected.
  2nd Degree — margins over ALL CANDIDATES.       Ben +24, Alma +12, Cleo +10.
               Ben would be elected.

Ben's +24 is almost entirely one number: he beats Dane 26-0, while Alma and Cleo only beat Dane 18-8. So under the second reading the winner is decided by how hard each finalist beat a candidate who was never in contention — a candidate the finalists' own tie has nothing to do with. That is why the protocol asks the finalists-only question FIRST and keeps the whole-field question in reserve for finalists who are level against each other.
This engine got that order wrong until 2026-08-19: it had no finalists-only rung at all and ranked ties on total margin, so it elected Ben on these ballots. BetterVoting gets it wrong the other way — it has no margins rung of any kind, so a three-way tie falls straight to its random rung and the winner tracks the order the candidates were listed in (filed as bettervoting#1469). Companion: rr_degrees_three_way_cycle.yaml, the minimal version of the same BetterVoting failure. Lesson: degrees_of_ties.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
8:Ben>Dane>Cleo>Alma
9:Cleo>Alma>Ben>Dane
9:Alma>Ben>Cleo>Dane
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 26 ballots (ranked ballots).

Ballots:
     8 × Ben > Dane > Cleo > Alma
     9 × Cleo > Alma > Ben > Dane
     9 × Alma > Ben > Cleo > Dane

Round-Robin — every pair, head-to-head (For – Against):
   Ben   beats Dane   26 –  0
   Ben   beats Cleo   17 –  9
   Alma  beats Ben    18 –  8
   Cleo  beats Dane   18 –  8
   Alma  beats Dane   18 –  8
   Cleo  beats Alma   17 –  9

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |     Ben      |    Dane     |    Cleo     |    Alma     |
-------------------------------------------------------------------
   Ben > |     ---      |26 -  0 -  0 |17 -  0 -  9 | 8 -  0 - 18 |
  Dane > |  0 -  0 - 26 |    ---      | 8 -  0 - 18 | 8 -  0 - 18 |
  Cleo > |  9 -  0 - 17 |18 -  0 -  8 |    ---      |17 -  0 -  9 |
  Alma > | 18 -  0 -  8 |18 -  0 -  8 | 9 -  0 - 17 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Alma       2–1–0         2     +12            +2  Ben, Dane
    2  Cleo       2–1–0         2     +10             0  Alma, Dane
    3  Ben        2–1–0         2     +24            -2  Cleo, Dane
    4  Dane       0–3–0         0     -46             —  —

Winner — Ranked Robin (RCV-RR): Alma
   *** 3 candidates tie for the most wins (Ben, Cleo, Alma) — a Condorcet cycle (no candidate beats all others). Resolved by the 1st Degree tiebreaker: Alma has the greatest sum of win margins over the other finalists (+2). (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 4): Ben, Cleo, Alma
   Outside (1):        Dane
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Alma is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/rr_degrees_finalists_vs_field_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/rr_degrees_finalists_vs_field.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [bv2270_8h4bvh_head_to_head_vs_margin](bv2270_8h4bvh_head_to_head_vs_margin.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md) · [rr_degrees_three_way_cycle](rr_degrees_three_way_cycle.md) · [rr_degrees_what_counts_as_a_win](rr_degrees_what_counts_as_a_win.md)
