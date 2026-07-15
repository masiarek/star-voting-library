# Runoff reversal, the convincing case — an intense minority favorite loses to the majority's compromise

*Generated from [`reversal_convincing_c3_b100.yaml`](../reversal_convincing_c3_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Nora

## Scenario

A *convincing* runoff reversal (the one nearly everyone agrees with). 100 voters, three candidates: Max is a passionate-minority favorite (45 voters give him a 5), Nora is the broad compromise, Cal is a no-hoper who never reaches the runoff. Max tops the SCORE round (335 vs Nora 255, Cal 55) on the strength of his intense base — but the runoff is Max vs Nora, and 55 of 100 voters prefer Nora, so she wins 55–45. Pure Score voting would crown Max on lopsided intensity; STAR's runoff catches that a majority actually wants Nora. This is the "runoff earns its keep" half of the pair; the companion reversal_jarring_c3_b100 shows the *jarring* case where the reversal is genuinely debatable.
Lesson: 00_start_here/STAR_Voting/STAR_second_round_FAQ.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Max,Nora,Cal
45:5,2,0    # Max's intense base — love Max, mildly prefer Nora to Cal
55:2,3,1    # the majority — mildly prefer Nora
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Runoff Reversal]
 - Score Round Winner(s) = (Max)
 - Runoff Round Winner   = (Nora)
  Candidate Max earned the highest total score, but
  Candidate Nora won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Max,Nora,Cal
   55 ×   2,   3,  1
   45 ×   5,   2,  0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Max           -- 335 -- First place
   Nora          -- 255 -- Second place
   Cal           --  55
 Max and Nora advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Nora          -- 55 -- First place
   Max           -- 45
   Equal Support --  0
 Nora wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Nora 55 (55%)  ·  Max 45 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Nora
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |      * Max      |    * Nora      |       Cal      |
-------------------------------------------------------------------------
            * Max > |       ---       | 45 -   0 -  55 |100 -   0 -   0 |
           * Nora > |  55 -   0 -  45 |      ---       |100 -   0 -   0 |
              Cal > |   0 -   0 - 100 |  0 -   0 - 100 |      ---       |

[Condorcet Winner]
  Condorcet Winner: Nora — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Max        45   0   0  55   0   0  |   335   3.4
Nora        0   0  55  45   0   0  |   255   2.6
Cal         0   0   0   0  55  45  |    55   0.6
```

</details>

Everything in one file: the [`_tabulated` mirror](../runoff_overturns_leader_tabulated/reversal_convincing_c3_b100_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/runoff_overturns_leader/reversal_convincing_c3_b100.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Runoff reversal (worked set)](../README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01a_c3_b3_more-stars-fewer-voters](01a_c3_b3_more-stars-fewer-voters.md) · [01b_c3_b9_overturn-holds-at-scale](01b_c3_b9_overturn-holds-at-scale.md) · [02_c5_b5_leader-overturned](02_c5_b5_leader-overturned.md) · [03_c7_b3_ice-cream-live](03_c7_b3_ice-cream-live.md) · [04_c4_b3_runoff-confirms-leader](04_c4_b3_runoff-confirms-leader.md) · [05_c3_b5_low-scores-bv1265](05_c3_b5_low-scores-bv1265.md) · [reversal_jarring_c3_b100](reversal_jarring_c3_b100.md)
