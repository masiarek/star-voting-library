# BV2140 — Ranked Robin worked example: most pairwise wins, no Condorcet winner (electowiki)

*Generated from [`bv2140_48hjkv_most_pairwise_wins.yaml`](../bv2140_48hjkv_most_pairwise_wins.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ava

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/48hjkv) · **[results ↗](https://bettervoting.com/48hjkv/results)** (election `48hjkv`).

## Scenario

The electowiki Ranked Robin worked example (electowiki.org/wiki/Ranked_Robin), and the first repo case built on EQUAL-RANK ballots. 35 voters, five candidates (Ava, Bianca, Cedric, Deegan, Eli); several ballots tie candidates (e.g. Ava=Bianca=Cedric). Ranked Robin (Copeland) compares every pair head-to-head and elects whoever wins the most matchups: Ava wins 3 of 4 and is elected. Yet there is NO Condorcet winner — Ava actually loses head-to-head to Bianca 15-14, and {Ava, Bianca, Cedric} form a 3-cycle (Ava>Cedric, Cedric>Bianca, Bianca>Ava). So no one beats everyone, but Ranked Robin still names the strongest all-round candidate by win count. Reproduced natively by the LH engine (its round-robin parser reads equal ranks as ties); the pairwise matrix matches electowiki exactly. Live results: https://bettervoting.com/48hjkv/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
8:Ava>Cedric>Deegan>Bianca>Eli
6:Ava=Bianca=Cedric>Eli>Deegan
6:Eli>Ava>Bianca=Cedric=Deegan
6:Deegan>Bianca=Cedric>Eli>Ava
4:Bianca>Ava>Eli>Deegan>Cedric
3:Eli>Deegan>Bianca=Cedric>Ava
2:Deegan=Eli>Bianca=Cedric>Ava
```

## What the engine says

Full report from the [`_tabulated` mirror](../condorcet_vs_ranked_robin_tabulated/bv2140_48hjkv_most_pairwise_wins_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 35 ballots (ranked ballots).

Ballots:
     8 × Ava > Cedric > Deegan > Bianca > Eli
     6 × Ava=Bianca=Cedric > Eli > Deegan
     6 × Eli > Ava > Bianca=Cedric=Deegan
     6 × Deegan > Bianca=Cedric > Eli > Ava
     4 × Bianca > Ava > Eli > Deegan > Cedric
     3 × Eli > Deegan > Bianca=Cedric > Ava
     2 × Deegan=Eli > Bianca=Cedric > Ava

Round-Robin — every pair, head-to-head (For – Against):
   Ava     beats Cedric   18 – 11
   Ava     beats Deegan   24 – 11
   Bianca  beats Ava      15 – 14
   Ava     beats Eli      18 – 17
   Deegan  beats Cedric   15 – 14
   Cedric  beats Bianca    8 –  4
   Cedric  beats Eli      20 – 15
   Deegan  beats Bianca   19 – 10
   Eli     beats Deegan   19 – 14
   Bianca  beats Eli      24 – 11

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |     Ava      |   Cedric    |   Deegan    |   Bianca    |    Eli      |
-----------------------------------------------------------------------------------
     Ava > |     ---      |18 -  6 - 11 |24 -  0 - 11 |14 -  6 - 15 |18 -  0 - 17 |
  Cedric > | 11 -  6 - 18 |    ---      |14 -  6 - 15 | 8 - 23 -  4 |20 -  0 - 15 |
  Deegan > | 11 -  0 - 24 |15 -  6 - 14 |    ---      |19 -  6 - 10 |14 -  2 - 19 |
  Bianca > | 15 -  6 - 14 | 4 - 23 -  8 |10 -  6 - 19 |    ---      |24 -  0 - 11 |
     Eli > | 17 -  0 - 18 |15 -  0 - 20 |19 -  2 - 14 |11 -  0 - 24 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ava        3–1–0         3     +20  Cedric, Deegan, Eli
    2  Cedric     2–2–0         2      +1  Bianca, Eli
    3  Bianca     2–2–0         2      +1  Ava, Eli
    4  Deegan     2–2–0         2      -8  Cedric, Bianca
    5  Eli        1–3–0         1     -14  Deegan

Winner — Ranked Robin (RCV-RR): Ava
   the most head-to-head wins (3).
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/condorcet_vs_ranked_robin/bv2140_48hjkv_most_pairwise_wins.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01_condorcet_winner](01_condorcet_winner.md) · [02_cycle_no_condorcet](02_cycle_no_condorcet.md) · [03_real_record0_c6_b5](03_real_record0_c6_b5.md)
