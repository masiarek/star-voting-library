---
search:
  exclude: true
---

# Rung 4 — the same nine voters, scored 0-5: STAR elects Gala

*Generated from [`07d_apples_full_menu_star.yaml`](../07d_apples_full_menu_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Gala

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/vq78wk) · **[results ↗](https://bettervoting.com/vq78wk/results)** (election `vq78wk` · test `BV2293`).

## Scenario

The identical nine voters and the identical eight-candidate menu as rung 3.
One thing changes: instead of one mark, each voter scores every candidate 0-5.

Nothing here is new information the voters invented for the occasion. The
scores simply write down what rung 3's ballot never asked: an apple person
likes ALL the apples and does not want the banana. Choose-One did not miscount
those opinions. It never collected them.

Scoring Round: Gala 29, Granny Smith 24, Fuji 17, Honeycrisp 16, McIntosh 16,
Pink Lady 13, Red Delicious 12, Banana 11 — the Choose-One winner finishes LAST
of eight. Gala and Granny Smith advance, and the Automatic Runoff goes to Gala
6-3 with nobody at Equal Support.

Gala is also the Condorcet winner: it beats every other candidate head-to-head.
Live results: https://bettervoting.com/vq78wk/results

## Parameters (from the YAML)

```yaml
blocs:
  Apples: [Granny Smith, Gala, Fuji, Honeycrisp, Pink Lady, Red Delicious, McIntosh]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Granny Smith,Gala,Fuji,Honeycrisp,Pink Lady,Red Delicious,McIntosh,Banana
5,4,2,2,1,1,2,0   # Granny Smith first - but any apple beats a banana
3,5,2,2,2,1,2,0   # Gala first
3,4,5,2,2,1,2,0   # Fuji first
3,4,2,5,1,1,3,0   # Honeycrisp first
3,4,2,1,5,1,1,0   # Pink Lady first
2,4,2,1,1,5,1,1   # Red Delicious first
3,4,2,3,1,1,5,0   # McIntosh first
1,0,0,0,0,1,0,5   # banana person
1,0,0,0,0,0,0,5   # banana person
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Gala
  Choose-One (Plurality) = Banana   (differs from STAR)

[Vote-splitting check]
  Choose-One first choices: Banana 2, Granny Smith 1, Gala 1, Fuji 1, Honeycrisp 1, Pink Lady 1, Red Delicious 1, McIntosh 1
  Plurality winner: Banana (2, 22.2%)
  Bloc 'Apples' = Granny Smith, Gala, Fuji, Honeycrisp, Pink Lady, Red Delicious, McIntosh: combined 7 (77.8%); winner Banana is OUTSIDE it.
  => VOTE SPLITTING: the 'Apples' bloc is an outright majority (7 vs
     Banana's 2) but split across 7 candidates, so Banana won Choose-One.
     STAR elected Gala.

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Granny Smith,Gala,Fuji,Honeycrisp,Pink Lady,Red Delicious,McIntosh,Banana
           5,   4,   2,         2,        1,            1,       2,     0
           3,   5,   2,         2,        2,            1,       2,     0
           3,   4,   5,         2,        2,            1,       2,     0
           3,   4,   2,         5,        1,            1,       3,     0
           3,   4,   2,         1,        5,            1,       1,     0
           2,   4,   2,         1,        1,            5,       1,     1
           3,   4,   2,         3,        1,            1,       5,     0
           1,   0,   0,         0,        0,            1,       0,     5
           1,   0,   0,         0,        0,            0,       0,     5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Gala          -- 29 -- First place
   Granny Smith  -- 24 -- Second place
   Fuji          -- 17
   Honeycrisp    -- 16
   McIntosh      -- 16
   Pink Lady     -- 13
   Red Delicious -- 12
   Banana        -- 11
 Gala and Granny Smith advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Gala          -- 6 -- First place
   Granny Smith  -- 3
   Equal Support -- 0
 Gala wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Gala 6 (67%)  ·  Granny Smith 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Gala
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                      |  * Granny Smith   |     * Gala       |       Fuji       |    Honeycrisp    |     Pink Lady    |   Red Delicious  |     McIntosh     |      Banana      |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     * Granny Smith > |        ---        |    3 - 0 - 6     |    7 - 1 - 1     |    7 - 1 - 1     |    8 - 0 - 1     |    7 - 1 - 1     |    7 - 1 - 1     |    7 - 0 - 2     |
             * Gala > |     6 - 0 - 3     |       ---        |    6 - 2 - 1     |    6 - 2 - 1     |    6 - 2 - 1     |    6 - 1 - 2     |    6 - 2 - 1     |    7 - 0 - 2     |
               Fuji > |     1 - 1 - 7     |    1 - 2 - 6     |       ---        |    3 - 4 - 2     |    5 - 3 - 1     |    6 - 1 - 2     |    3 - 4 - 2     |    7 - 0 - 2     |
         Honeycrisp > |     1 - 1 - 7     |    1 - 2 - 6     |    2 - 4 - 3     |       ---        |    3 - 5 - 1     |    5 - 2 - 2     |    1 - 7 - 1     |    6 - 1 - 2     |
          Pink Lady > |     1 - 0 - 8     |    1 - 2 - 6     |    1 - 3 - 5     |    1 - 5 - 3     |       ---        |    3 - 4 - 2     |    1 - 5 - 3     |    6 - 1 - 2     |
      Red Delicious > |     1 - 1 - 7     |    2 - 1 - 6     |    2 - 1 - 6     |    2 - 2 - 5     |    2 - 4 - 3     |       ---        |    2 - 2 - 5     |    7 - 0 - 2     |
           McIntosh > |     1 - 1 - 7     |    1 - 2 - 6     |    2 - 4 - 3     |    1 - 7 - 1     |    3 - 5 - 1     |    5 - 2 - 2     |       ---        |    6 - 1 - 2     |
             Banana > |     2 - 0 - 7     |    2 - 0 - 7     |    2 - 0 - 7     |    2 - 1 - 6     |    2 - 1 - 6     |    2 - 0 - 7     |    2 - 1 - 6     |       ---        |

[Condorcet Winner]
  Condorcet Winner: Gala — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Banana — loses every head-to-head matchup — elected by Choose-One (Plurality)!

[Score Distribution] (how many ballots gave each star rating)
                    Score
Candidate      5  4  3  2  1  0  | Total   Avg
Granny Smith   1  0  5  1  2  0  |    24   2.7
Gala           1  6  0  0  0  2  |    29   3.2
Fuji           1  0  0  6  0  2  |    17   1.9
Honeycrisp     1  0  1  3  2  2  |    16   1.8
Pink Lady      1  0  0  2  4  2  |    13   1.4
Red Delicious  1  0  0  0  7  1  |    12   1.3
McIntosh       1  0  1  3  2  2  |    16   1.8
Banana         2  0  0  0  1  6  |    11   1.2
```

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/07d_apples_full_menu_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_voting/_main/07d_apples_full_menu_star.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_plurality_vs_majority](00_plurality_vs_majority.md) · [01_political_left_split](01_political_left_split.md) · [02_icecream_chocolate_split](02_icecream_chocolate_split.md) · [03_lunch_veggie_vs_meat](03_lunch_veggie_vs_meat.md) · [04_star_wars_vote_split](04_star_wars_vote_split.md) · [05a_residual_split_bullet-voting](05a_residual_split_bullet-voting.md) · [05b_residual_split_expressive-fix](05b_residual_split_expressive-fix.md) · [06_sub_majority_not_spoiled](06_sub_majority_not_spoiled.md) · [07a_apples_two_candidates](07a_apples_two_candidates.md) · [07b_apples_six_candidates](07b_apples_six_candidates.md) · [07c_apples_full_menu](07c_apples_full_menu.md) · [07e_apples_full_menu_approval](07e_apples_full_menu_approval.md) · [07f_apples_full_menu_irv](07f_apples_full_menu_irv.md) · [07g_apples_full_menu_ranked_robin](07g_apples_full_menu_ranked_robin.md) · [08a_smallest_spoiler_plurality](08a_smallest_spoiler_plurality.md) · [08b_smallest_spoiler_star](08b_smallest_spoiler_star.md) · [08c_smallest_spoiler_ranked_robin](08c_smallest_spoiler_ranked_robin.md) · [09a_clones_are_voters_not_labels](09a_clones_are_voters_not_labels.md) · [09b_same_ballots_grouped_by_label](09b_same_ballots_grouped_by_label.md)
