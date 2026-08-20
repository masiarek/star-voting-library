---
search:
  exclude: true
---

# BV2270 — the two-way Copeland tie that showed the engine was starting the ladder one rung too low

*Generated from [`bv2270_8h4bvh_head_to_head_vs_margin.yaml`](../bv2270_8h4bvh_head_to_head_vs_margin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Alder

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8h4bvh) · **[results ↗](https://bettervoting.com/8h4bvh/results)** (election `8h4bvh` · test `BV2270`).

## Scenario

Nine voters rank four trees for a street-planting commission, and the count lands on the middle rung of the Ranked Robin tiebreak ladder — the rung the other cases in this folder fall straight past. Alder and Birch finish level on pairwise wins: Alder beats Birch and Cedar but loses to Dogwood; Birch beats Cedar and Dogwood but loses to Alder. Two wins each, Copeland 2. Cedar and Dogwood take one each.
A tie of exactly two used to be where LH and BetterVoting parted company, and this file is the case that made the parting visible. Neither engine reaches for a lot here — both have a deterministic rung available, and for two years the rungs disagreed:

  LH  (before 2026-08-19)  TOTAL MARGIN.  Birch +3 (6-3 over Cedar, 5-4 over Dogwood,
                           4-5 to Alder) beats Alder +1 (5-4, 5-4, 4-5) -> BIRCH.
  BV                       HEAD-TO-HEAD.  Alder and Birch played each other and Alder won
                           it 5-4 -> ALDER.

Ranked Robin's published protocol settles which of those is the method's own answer, and it is not the one this engine was giving. The 1st Degree tiebreaker declares the tied candidates FINALISTS and elects the one with the greatest sum of win margins over THE OTHER FINALISTS — with exactly two finalists that sum is a single number, their own head-to-head. Total margin over the whole field is the 2nd Degree, reached only when the finalists are level against each other. So BetterVoting's rung was right and the engine's was one rung too low; the engine was corrected on 2026-08-19 and now elects ALDER too. pref_voting's independent Copeland still declines to break the tie at all, returning the leader set {Alder, Birch} — the honest position for a library that implements the tally and not the tiebreak. Read the full ladder in 05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md.
Note also that the whole field is one Smith set: Alder>Birch>Dogwood>Alder cycles, so there is no Condorcet winner and the Copeland leaders understate how wide the contention really is.
The election was minted to expose a BetterVoting DISPLAY defect, and it does: the results page reads "Alder wins!" while the star and the gold table row sit on Birch, because the page highlights by row position while the winner is decided by the ladder. Filed as bettervoting#1480. Do not read the star on that page as BV's answer — BV's answer is Alder, stated in the heading and in the export's `elected`.
Lesson: 05_Ranked_Robin/03_Criteria/rr_tiebreaks/bv2270_8h4bvh_head_to_head_vs_margin.md Live results: https://bettervoting.com/8h4bvh/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Alder>Birch>Cedar>Dogwood
3:Dogwood>Cedar>Birch>Alder
1:Birch>Cedar>Dogwood>Alder
1:Dogwood>Alder>Birch>Cedar
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 9 ballots (ranked ballots).

Ballots:
     4 × Alder > Birch > Cedar > Dogwood
     3 × Dogwood > Cedar > Birch > Alder
     1 × Birch > Cedar > Dogwood > Alder
     1 × Dogwood > Alder > Birch > Cedar

Round-Robin — every pair, head-to-head (For – Against):
   Alder    beats Birch     5 – 4
   Alder    beats Cedar     5 – 4
   Dogwood  beats Alder     5 – 4
   Birch    beats Cedar     6 – 3
   Birch    beats Dogwood   5 – 4
   Cedar    beats Dogwood   5 – 4

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
            |   Alder   |  Birch   |  Cedar   | Dogwood  |
----------------------------------------------------------
    Alder > |    ---    |5 - 0 - 4 |5 - 0 - 4 |4 - 0 - 5 |
    Birch > | 4 - 0 - 5 |   ---    |6 - 0 - 3 |5 - 0 - 4 |
    Cedar > | 4 - 0 - 5 |3 - 0 - 6 |   ---    |5 - 0 - 4 |
  Dogwood > | 5 - 0 - 4 |4 - 0 - 5 |4 - 0 - 5 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Alder      2–1–0         2      +1            +1  Birch, Cedar
    2  Birch      2–1–0         2      +3            -1  Cedar, Dogwood
    3  Cedar      1–2–0         1      -3             —  Dogwood
    4  Dogwood    1–2–0         1      -1             —  Alder

Winner — Ranked Robin (RCV-RR): Alder
   *** 2 candidates tie for the most wins (Alder, Birch) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Alder has the greatest sum of win margins over the other finalists (+1).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): Alder, Birch, Cedar, Dogwood
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Alder, Birch) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Alder is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2270_8h4bvh_head_to_head_vs_margin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/bv2270_8h4bvh_head_to_head_vs_margin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md) · [rr_degrees_finalists_vs_field](rr_degrees_finalists_vs_field.md) · [rr_degrees_three_way_cycle](rr_degrees_three_way_cycle.md) · [rr_degrees_what_counts_as_a_win](rr_degrees_what_counts_as_a_win.md)
