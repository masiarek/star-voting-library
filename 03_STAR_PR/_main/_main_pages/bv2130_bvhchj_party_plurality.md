# BV2130 — Presidential Board: party alignment (Plurality)

*Generated from [`bv2130_bvhchj_party_plurality.yaml`](../bv2130_bvhchj_party_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Democrat

## Scenario

The second race of the Presidential Board election (BetterVoting bvhchj) — a choose-one Plurality poll of party alignment, alongside the 7-seat STAR-PR board race in the same election. 102 voters, 8 parties; Democrat leads with 39 first-choices and wins. Companion to bv2130_presidential_board_star_pr.yaml (the STAR-PR board seats). BV also elects Democrat. Live results: https://bettervoting.com/bvhchj/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Democrat,Republican,Libertarian,Green,Constitution,Socialism and Liberation,Solidarity,Independent
39: 1,0,0,0,0,0,0,0
15: 0,0,0,0,0,1,0,0
14: 0,0,0,0,0,0,0,1
11: 0,0,1,0,0,0,0,0
11: 0,0,0,1,0,0,0,0
7: 0,0,0,0,0,0,1,0
2: 0,1,0,0,0,0,0,0
2: 0,0,0,0,1,0,0,0
1: 0,0,0,0,0,0,0,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/bv2130_bvhchj_party_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                                 |          * Democrat          |          Republican         |         Libertarian         |            Green            |         Constitution        | * Socialism and Liberation  |          Solidarity         |         Independent         |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    * Democrat > |             ---              |        39 - 61 -  2         |        39 - 52 - 11         |        39 - 52 - 11         |        39 - 61 -  2         |        39 - 48 - 15         |        39 - 56 -  7         |        39 - 49 - 14         |
                    Republican > |          2 - 61 - 39         |            ---              |         2 - 89 - 11         |         2 - 89 - 11         |         2 - 98 -  2         |         2 - 85 - 15         |         2 - 93 -  7         |         2 - 86 - 14         |
                   Libertarian > |         11 - 52 - 39         |        11 - 89 -  2         |            ---              |        11 - 80 - 11         |        11 - 89 -  2         |        11 - 76 - 15         |        11 - 84 -  7         |        11 - 77 - 14         |
                         Green > |         11 - 52 - 39         |        11 - 89 -  2         |        11 - 80 - 11         |            ---              |        11 - 89 -  2         |        11 - 76 - 15         |        11 - 84 -  7         |        11 - 77 - 14         |
                  Constitution > |          2 - 61 - 39         |         2 - 98 -  2         |         2 - 89 - 11         |         2 - 89 - 11         |            ---              |         2 - 85 - 15         |         2 - 93 -  7         |         2 - 86 - 14         |
    * Socialism and Liberation > |         15 - 48 - 39         |        15 - 85 -  2         |        15 - 76 - 11         |        15 - 76 - 11         |        15 - 85 -  2         |            ---              |        15 - 80 -  7         |        15 - 73 - 14         |
                    Solidarity > |          7 - 56 - 39         |         7 - 93 -  2         |         7 - 84 - 11         |         7 - 84 - 11         |         7 - 93 -  2         |         7 - 80 - 15         |            ---              |         7 - 81 - 14         |
                   Independent > |         14 - 49 - 39         |        14 - 86 -  2         |        14 - 77 - 11         |        14 - 77 - 11         |        14 - 86 -  2         |        14 - 73 - 15         |        14 - 81 -  7         |            ---              |

[Condorcet Winner]
  Condorcet Winner: Democrat — matches the STAR winner

--- Choose-One / Plurality Voting Method (single winner) ---
[STAR Voting]
 Tabulating 102 ballots.
Count × Democrat,Republican,Libertarian,Green,Constitution,Socialism and Liberation,Solidarity,Independent
   39 ×        1,         0,          0,    0,           0,                       0,         0,          0
   15 ×        0,         0,          0,    0,           0,                       1,         0,          0
   14 ×        0,         0,          0,    0,           0,                       0,         0,          1
   11 ×        0,         0,          1,    0,           0,                       0,         0,          0
   11 ×        0,         0,          0,    1,           0,                       0,         0,          0
    7 ×        0,         0,          0,    0,           0,                       0,         1,          0
    2 ×        0,         1,          0,    0,           0,                       0,         0,          0
    2 ×        0,         0,          0,    0,           1,                       0,         0,          0
    1 ×        0,         0,          0,    0,           0,                       0,         0,          0

[Score Distribution] (how many ballots gave each star rating)
                                     Score
Candidate                   5    4    3    2    1    0  | Total   Avg
Democrat                    0    0    0    0   39   63  |    39   0.4
Republican                  0    0    0    0    2  100  |     2   0.0
Libertarian                 0    0    0    0   11   91  |    11   0.1
Green                       0    0    0    0   11   91  |    11   0.1
Constitution                0    0    0    0    2  100  |     2   0.0
Socialism and Liberation    0    0    0    0   15   87  |    15   0.1
Solidarity                  0    0    0    0    7   95  |     7   0.1
Independent                 0    0    0    0   14   88  |    14   0.1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Democrat                 -- 39 -- First place
   Socialism and Liberation -- 15 -- Second place
   Independent              -- 14
   Green                    -- 11
   Libertarian              -- 11
   Solidarity               --  7
   Constitution             --  2
   Republican               --  2
 Democrat and Socialism and Liberation advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Democrat                 -- 39 -- First place
   Socialism and Liberation -- 15
   Equal Support            -- 48
 Democrat wins.
   Runoff math:
     102  ballots cast
   −  48  Equal Support (no preference between the two finalists)
     ───
      54  voters with a preference  (majority = 28)
           Democrat 39 (72%)  ·  Socialism and Liberation 15 (28%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Democrat
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/_main/bv2130_bvhchj_party_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [02a_c5_b63_proportional-allocated-score](02a_c5_b63_proportional-allocated-score.md) · [02b_c5_b63_proportional-sss](02b_c5_b63_proportional-sss.md) · [02c_c5_b63_proportional-rrv](02c_c5_b63_proportional-rrv.md) · [03b_star_pr_3seats](03b_star_pr_3seats.md) · [bv2130_presidential_board_star_pr](bv2130_presidential_board_star_pr.md) · [lackner_skowron_shadow_star_pr_c7_b12](lackner_skowron_shadow_star_pr_c7_b12.md) · [lackner_skowron_shadow_star_pr_rrv_c7_b12](lackner_skowron_shadow_star_pr_rrv_c7_b12.md) · [rrv_sample_c15_b13_three-parties](rrv_sample_c15_b13_three-parties.md)
