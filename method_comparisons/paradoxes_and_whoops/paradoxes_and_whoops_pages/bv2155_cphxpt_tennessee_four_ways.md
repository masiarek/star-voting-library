# Tennessee capital, four ways — same ballots; Memphis, Knoxville or Nashville by count (BV2155)

*Generated from [`bv2155_cphxpt_tennessee_four_ways.yaml`](../bv2155_cphxpt_tennessee_four_ways.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Nashville

## Scenario

The classic Tennessee state-capital example. One set of ballots; Plurality picks
MEMPHIS, RCV-IRV picks KNOXVILLE, and Condorcet + STAR pick NASHVILLE (the central
compromise that beats everyone head-to-head). Nobody is being strategic — these are
sincere ballots. The whoops belongs to Plurality and IRV here. Scores are a simple
geographic-distance spatial model. Level 201. Fairness note in the lesson.
Live results: https://bettervoting.com/cphxpt/results (all races LH<->BV confirmed).
Lesson: bv2155_cphxpt_tennessee_four_ways.md
Live on BetterVoting: https://bettervoting.com/cphxpt/results (BV-confirmed; STAR is race 1).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Memphis, Nashville, Chattanooga, Knoxville
42 × 5, 2, 1, 0      # Memphis voters (far west)
26 × 1, 5, 3, 2      # Nashville voters (central)
15 × 0, 3, 5, 4      # Chattanooga voters (southeast)
17 × 0, 3, 4, 5      # Knoxville voters (east)
```

## What the engine says

Full report from the [`_tabulated` mirror](../paradoxes_and_whoops_tabulated/bv2155_cphxpt_tennessee_four_ways_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |      Memphis    |  * Nashville   | * Chattanooga  |    Knoxville   |
------------------------------------------------------------------------------------------
          Memphis > |       ---       | 42 -  0 - 58   | 42 -  0 - 58   | 42 -  0 - 58   |
      * Nashville > |  58 -  0 - 42   |      ---       | 68 -  0 - 32   | 68 -  0 - 32   |
    * Chattanooga > |  58 -  0 - 42   | 32 -  0 - 68   |      ---       | 83 -  0 - 17   |
        Knoxville > |  58 -  0 - 42   | 32 -  0 - 68   | 17 -  0 - 83   |      ---       |

[Condorcet Winner]
  Condorcet Winner: Nashville — matches the STAR winner

[Divergence from STAR]
  STAR                   = Nashville
  Choose-One (Plurality) = Memphis   (differs from STAR)
  RCV-IRV                = Knoxville   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: paradoxes_and_whoops_tabulated/bv2155_cphxpt_tennessee_four_ways_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Memphis,Nashville,Chattanooga,Knoxville
   42 ×       5,        2,          1,        0
   26 ×       1,        5,          3,        2
   17 ×       0,        3,          4,        5
   15 ×       0,        3,          5,        4

[Score Distribution] (how many ballots gave each star rating)
                     Score
Candidate     5   4   3   2   1   0  | Total   Avg
Memphis      42   0   0   0  26  32  |   236   2.4
Nashville    26   0  32  42   0   0  |   310   3.1
Chattanooga  15  17  26   0  42   0  |   263   2.6
Knoxville    17  15   0  26   0  42  |   197   2.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Nashville     -- 310 -- First place
   Chattanooga   -- 263 -- Second place
   Memphis       -- 236
   Knoxville     -- 197
 Nashville and Chattanooga advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Nashville     -- 68 -- First place
   Chattanooga   -- 32
   Equal Support --  0
 Nashville wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Nashville 68 (68%)  ·  Chattanooga 32 (32%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Nashville
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/paradoxes_and_whoops/bv2155_cphxpt_tennessee_four_ways.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2155_cphxpt_tennessee_four_ways.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2156_3grpbb_star_misses_condorcet](bv2156_3grpbb_star_misses_condorcet.md) · [bv2157_mmcmpy_condorcet_cycle_rps](bv2157_mmcmpy_condorcet_cycle_rps.md) · [bv2158_gr72hd_ossipoff_centrist_irv](bv2158_gr72hd_ossipoff_centrist_irv.md) · [bv2159_f4cjpy_brams_irv_pathologies](bv2159_f4cjpy_brams_irv_pathologies.md)
