---
search:
  exclude: true
---

# BV2270 — a two-way Copeland tie where LH and BetterVoting elect DIFFERENT candidates

*Generated from [`bv2270_8h4bvh_head_to_head_vs_margin.yaml`](../bv2270_8h4bvh_head_to_head_vs_margin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn) · **1 seat** · **Expected winner:** Birch

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8h4bvh) · **[results ↗](https://bettervoting.com/8h4bvh/results)** (election `8h4bvh` · test `BV2270`).

## Scenario

Nine voters rank four trees for a street-planting commission, and the count lands on the middle rung of the Ranked Robin tiebreak ladder — the rung the other cases in this folder fall straight past. Alder and Birch finish level on pairwise wins: Alder beats Birch and Cedar but loses to Dogwood; Birch beats Cedar and Dogwood but loses to Alder. Two wins each, Copeland 2. Cedar and Dogwood take one each.
A tie of exactly two is where LH and BetterVoting part company, and this file is the case that makes the parting visible. Neither engine reaches for a lot here — both have a deterministic rung available, and the rungs disagree:

  LH  rung 2 = TOTAL MARGIN.   Birch +3 (6-3 over Cedar, 5-4 over Dogwood, 4-5 to Alder)
                               beats Alder +1 (5-4, 5-4, 4-5). LH elects BIRCH.
  BV  rung 2 = HEAD-TO-HEAD.   Alder and Birch played each other and Alder won it 5-4,
                               so BetterVoting elects ALDER.

Same ballots, same Copeland table, two derivable winners. This is a sharper divergence than dead_heat_lot_tiebreak.yaml, where the ladders differ but both engines still end up at a rung of last resort: here BOTH answers are computable from the ballots and they are simply not the same answer. pref_voting's independent Copeland agrees with the tally and declines to break the tie at all, returning the leader set {Alder, Birch} — which is the honest position, since the disagreement is about the RULE, not about the count.
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

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Birch      2–1–0         2      +3  Dogwood, Cedar
    2  Alder      2–1–0         2      +1  Birch, Cedar
    3  Dogwood    1–2–0         1      -1  Alder
    4  Cedar      1–2–0         1      -3  Dogwood

Winner — Ranked Robin (RCV-RR): Birch
   *** 2 candidates tie for the most wins (Alder, Birch) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
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
   Ranked Robin (RCV-RR) winner Birch is INSIDE the Smith set. ✓
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

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [dead_heat_lot_tiebreak](dead_heat_lot_tiebreak.md)
