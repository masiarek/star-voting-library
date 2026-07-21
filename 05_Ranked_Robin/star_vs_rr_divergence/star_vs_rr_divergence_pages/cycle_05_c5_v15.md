# STAR vs Ranked Robin divergence — cycle_05_c5_v15 (STAR B, RR D)

*Generated from [`cycle_05_c5_v15.yaml`](../cycle_05_c5_v15.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** B

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence sample (cycle). 5 candidates, 15 voters, noise model. STAR elects B; Ranked Robin elects D; no Condorcet winner (cycle). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:5,0,4,3,0
1:4,0,5,3,4
1:5,1,0,5,1
1:0,5,1,3,3
1:1,4,0,3,5
1:5,5,1,0,5
1:4,0,1,5,0
1:0,0,1,5,3
1:0,2,5,2,2
1:2,5,1,3,0
1:3,5,3,0,4
1:1,5,3,4,0
1:3,5,1,1,0
1:3,2,0,2,5
1:4,2,0,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = B
  RCV-IRV  = A   (differs from STAR)
  Approval = D   (differs from STAR)
  RCV-RR   = D   (differs from STAR)
  Note: 9 of 15 ballots (60%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_05_c5_v15_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_05_c5_v15_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (D)
 - Runoff Round Winner   = (B)
  Candidate D earned the highest total score, but
  Candidate B won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 15 ballots.
A,B,C,D,E
5,0,4,3,0
4,0,5,3,4
5,1,0,5,1
0,5,1,3,3
1,4,0,3,5
5,5,1,0,5
4,0,1,5,0
0,0,1,5,3
0,2,5,2,2
2,5,1,3,0
3,5,3,0,4
1,5,3,4,0
3,5,1,1,0
3,2,0,2,5
4,2,0,5,4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 44 -- First place
   B             -- 41 -- Second place
   A             -- 40
   E             -- 36
   C             -- 26
 D and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 7 -- First place
   D             -- 6
   Equal Support -- 2
 B wins.
   Runoff math:
     15  ballots cast
   −  2  Equal Support (no preference between the two finalists)
     ──
     13  voters with a preference  (majority = 7)
           B 7 (54%)  ·  D 6 (46%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |    * B      |      C      |    * D      |      E      |
-----------------------------------------------------------------------------------------
             A > |     ---      | 6 -  2 -  7 | 9 -  1 -  5 | 6 -  1 -  8 | 6 -  3 -  6 |
           * B > |  7 -  2 -  6 |    ---      |10 -  0 -  5 | 7 -  2 -  6 | 5 -  5 -  5 |
             C > |  5 -  1 -  9 | 5 -  0 - 10 |    ---      | 5 -  1 -  9 | 7 -  0 -  8 |
           * D > |  8 -  1 -  6 | 6 -  2 -  7 | 9 -  1 -  5 |    ---      | 8 -  2 -  5 |
             E > |  6 -  3 -  6 | 5 -  5 -  5 | 8 -  0 -  7 | 5 -  2 -  8 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: B — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          3  3  3  1  2  3  |    40   2.7
B          6  1  0  3  1  4  |    41   2.7
C          2  1  2  0  6  4  |    26   1.7
D          4  1  5  2  1  2  |    44   2.9
E          3  3  2  1  1  5  |    36   2.4
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_05_c5_v15_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_05_c5_v15.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_01_c5_v21](cycle_01_c5_v21.md) · [cycle_02_c5_v15](cycle_02_c5_v15.md) · [cycle_03_c5_v21](cycle_03_c5_v21.md) · [cycle_04_c5_v21](cycle_04_c5_v21.md) · [cycle_06_c4_v21](cycle_06_c4_v21.md) · [cycle_07_c4_v21](cycle_07_c4_v21.md) · [cycle_09_c3_v21](cycle_09_c3_v21.md) · [cycle_10_c4_v15](cycle_10_c4_v15.md) · [cycle_11_c4_v21](cycle_11_c4_v21.md) · [cycle_12_c3_v15](cycle_12_c3_v15.md) · [cycle_13_c5_v21](cycle_13_c5_v21.md) · [cycle_14_c3_v21](cycle_14_c3_v21.md) · [cycle_15_c5_v21](cycle_15_c5_v21.md) · [cycle_16_c3_v15](cycle_16_c3_v15.md) · [darkhorse_01_c5_v21](darkhorse_01_c5_v21.md) · [darkhorse_02_c4_v15](darkhorse_02_c4_v15.md) · [darkhorse_03_c5_v15](darkhorse_03_c5_v15.md) · [darkhorse_04_c4_v21](darkhorse_04_c4_v21.md) · [darkhorse_05_c5_v21](darkhorse_05_c5_v21.md) · [darkhorse_06_c4_v15](darkhorse_06_c4_v15.md) · [darkhorse_08_c5_v21](darkhorse_08_c5_v21.md) · [darkhorse_10_c5_v21](darkhorse_10_c5_v21.md) · [darkhorse_11_c5_v21](darkhorse_11_c5_v21.md) · [darkhorse_12_c5_v21](darkhorse_12_c5_v21.md) · [darkhorse_15_c5_v21](darkhorse_15_c5_v21.md) · [darkhorse_16_c4_v15](darkhorse_16_c4_v15.md) · [darkhorse_18_c4_v21](darkhorse_18_c4_v21.md) · [darkhorse_19_c4_v15](darkhorse_19_c4_v15.md) · [darkhorse_20_c5_v15](darkhorse_20_c5_v15.md)
