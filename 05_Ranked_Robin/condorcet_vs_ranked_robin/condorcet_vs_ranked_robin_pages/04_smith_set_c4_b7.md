# The Smith set — the smallest club that beats everyone outside it

*Generated from [`04_smith_set_c4_b7.yaml`](../04_smith_set_c4_b7.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara > Dave — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The 02_cycle election (Ada beats Ben, Ben beats Cara, Cara beats Ada — no Condorcet winner) with ONE change: a fourth candidate, Dave, whom every voter ranks last. All three cycle members beat Dave 7-0, and no smaller group beats everyone outside it — so the SMITH SET is exactly {Ada, Ben, Cara}. Dave is outside the club. Ranked Robin (Copeland) is Smith-efficient: its winner (Ada, on margins) comes from inside the set.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Ada>Ben>Cara>Dave
Ada>Ben>Cara>Dave
Ada>Ben>Cara>Dave
Ben>Cara>Ada>Dave
Ben>Cara>Ada>Dave
Cara>Ada>Ben>Dave
Cara>Ada>Ben>Dave
```

## What the engine says

Full report from the [`_tabulated` mirror](../condorcet_vs_ranked_robin_tabulated/04_smith_set_c4_b7_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cara > Dave
     2 × Ben > Cara > Ada > Dave
     2 × Cara > Ada > Ben > Dave

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    5 – 2
   Cara  beats Ada    4 – 3
   Ada   beats Dave   7 – 0
   Ben   beats Cara   5 – 2
   Ben   beats Dave   7 – 0
   Cara  beats Dave   7 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |  Dave    |
-------------------------------------------------------
   Ada > |    ---    |5 - 0 - 2 |3 - 0 - 4 |7 - 0 - 0 |
   Ben > | 2 - 0 - 5 |   ---    |5 - 0 - 2 |7 - 0 - 0 |
  Cara > | 4 - 0 - 3 |2 - 0 - 5 |   ---    |7 - 0 - 0 |
  Dave > | 0 - 0 - 7 |0 - 0 - 7 |0 - 0 - 7 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–1–0         2      +9  Ben, Dave
    2  Ben        2–1–0         2      +7  Cara, Dave
    3  Cara       2–1–0         2      +5  Ada, Dave
    4  Dave       0–3–0         0     -21  —

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie for the most wins (Ada, Ben, Cara) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/condorcet_vs_ranked_robin/04_smith_set_c4_b7.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01_condorcet_winner](01_condorcet_winner.md) · [02_cycle_no_condorcet](02_cycle_no_condorcet.md) · [03_real_record0_c6_b5](03_real_record0_c6_b5.md) · [bv2140_48hjkv_most_pairwise_wins](bv2140_48hjkv_most_pairwise_wins.md)
