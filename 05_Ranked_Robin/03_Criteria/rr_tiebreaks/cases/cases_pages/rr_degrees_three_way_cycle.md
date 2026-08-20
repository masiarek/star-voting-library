---
search:
  exclude: true
---

# A three-way cycle has a deterministic answer — and BetterVoting draws lots for it

*Generated from [`rr_degrees_three_way_cycle.yaml`](../rr_degrees_three_way_cycle.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Frank

## Scenario

Eleven voters, three candidates, one rock-paper-scissors cycle: Dre beats Edith 7-4, Edith beats Frank 6-5, Frank beats Dre 9-2. All three tie at one matchup win, so all three are finalists and Ranked Robin reaches for its 1st Degree tiebreaker — the sum of each finalist's win margins over the other finalists:

  Frank  (+7) + (-1) = +6      <- elected
  Edith  (-3) + (+1) = -2
  Dre    (+3) + (-7) = -4

Frank is elected, deterministically, from the ballots alone. Note how lopsided it is: Frank's +6 on 11 ballots is a 54-point swing, and he is the only finalist with a positive sum, which the protocol argues is what "majority preferred among finalists" means.
BetterVoting elects nobody in particular. Its tabulator has a rung for exactly two tied candidates and nothing for three, so this count falls to the random rung and returns whoever happens to sit first in the shuffled candidate order — enter the same election with the candidates listed as Edith, Frank, Dre and the page reports Edith. That is bettervoting#1469, and it is not a corner case: with three candidates and no drawn matchups, EVERY Condorcet cycle is a three-way Copeland tie, so the two-way rung can never fire on one.
This engine has answered Frank since 2026-08-19; before that it used total margin over the whole field, which on three candidates is the same pool as the finalists and happens to agree. The case that separates the two pools is the companion, rr_degrees_finalists_vs_field.yaml. Lesson: degrees_of_ties.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Dre>Edith>Frank
Dre>Edith>Frank
Edith>Frank>Dre
Edith>Frank>Dre
Edith>Frank>Dre
Edith>Frank>Dre
Frank>Dre>Edith
Frank>Dre>Edith
Frank>Dre>Edith
Frank>Dre>Edith
Frank>Dre>Edith
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 11 ballots (ranked ballots).

Ballots:
     2 × Dre > Edith > Frank
     4 × Edith > Frank > Dre
     5 × Frank > Dre > Edith

Round-Robin — every pair, head-to-head (For – Against):
   Dre    beats Edith   7 – 4
   Frank  beats Dre     9 – 2
   Edith  beats Frank   6 – 5

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |    Dre    |  Edith   |  Frank   |
---------------------------------------------
    Dre > |    ---    |7 - 0 - 4 |2 - 0 - 9 |
  Edith > | 4 - 0 - 7 |   ---    |6 - 0 - 5 |
  Frank > | 9 - 0 - 2 |5 - 0 - 6 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Frank      1–1–0         1      +6            +6  Dre
    2  Edith      1–1–0         1      -2            -2  Frank
    3  Dre        1–1–0         1      -4            -4  Edith

Winner — Ranked Robin (RCV-RR): Frank
   *** 3 candidates tie for the most wins (Dre, Edith, Frank) — a Condorcet cycle (no candidate beats all others). Resolved by the 1st Degree tiebreaker: Frank has the greatest sum of win margins over the other finalists (+6). (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): Dre, Edith, Frank
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Frank is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/rr_degrees_three_way_cycle_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/rr_degrees_three_way_cycle.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [bv2270_8h4bvh_head_to_head_vs_margin](bv2270_8h4bvh_head_to_head_vs_margin.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md) · [rr_degrees_finalists_vs_field](rr_degrees_finalists_vs_field.md) · [rr_degrees_what_counts_as_a_win](rr_degrees_what_counts_as_a_win.md)
