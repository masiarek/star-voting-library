# STAR vs RR divergence -- 5 cands, 45 voters, cycle (STAR D, RR B)

*Generated from [`cycle_C05_medV45_noise_2.yaml`](../cycle_C05_medV45_noise_2.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** D

## Scenario

Auto-generated STAR-vs-Ranked-Robin divergence. 5 candidates, 45 voters, ungrouped (independent random ballots). STAR elects D; Ranked Robin elects B. CAUSE = CONDORCET CYCLE: no candidate beats all others (C>E>D>C), so there is no 'right' winner. RR falls back on Copeland/margin (B); STAR runs its two score-leaders off (D). See the [Divergence from STAR] block below for RCV-IRV, Approval and Plurality on the same ballots.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C,D,E
1:0,4,2,3,5
1:1,3,4,1,1
1:1,3,2,5,5
1:0,2,4,4,3
1:3,2,4,2,4
1:3,5,0,2,1
1:2,0,5,2,3
1:1,4,3,0,3
1:3,3,1,1,2
1:2,0,1,1,1
1:4,4,0,2,2
1:2,5,4,4,5
1:4,0,2,3,2
1:4,4,1,2,0
1:0,0,1,2,0
1:2,0,3,2,3
1:0,1,5,3,3
1:4,2,0,1,5
1:5,4,2,1,1
1:3,1,4,5,0
1:1,0,2,3,4
1:1,0,2,1,2
1:3,2,2,1,2
1:5,3,3,5,2
1:2,2,5,4,5
1:1,2,2,4,3
1:0,1,2,3,1
1:2,5,1,4,3
1:4,4,5,4,2
1:4,1,5,4,4
1:2,5,4,0,1
1:1,5,2,4,2
1:1,3,3,2,2
1:0,0,0,1,2
1:2,4,3,2,2
1:5,4,5,1,2
1:1,4,0,4,1
1:0,3,3,5,0
1:3,2,1,0,0
1:4,1,2,3,5
1:2,2,2,2,4
1:0,4,4,4,2
1:0,3,0,1,2
1:4,4,0,3,2
1:0,4,2,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = D
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = B   (differs from STAR)
  Approval               = B   (differs from STAR)
  RCV-RR                 = B   (differs from STAR)
  Note: 32 of 45 ballots (71%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: star_vs_rr_divergence_tabulated/cycle_C05_medV45_noise_2_RCV-IRV_tabulated.txt
  RCV-RR round-robin: star_vs_rr_divergence_tabulated/cycle_C05_medV45_noise_2_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 45 ballots.
A,B,C,D,E
0,4,2,3,5
1,3,4,1,1
1,3,2,5,5
0,2,4,4,3
3,2,4,2,4
3,5,0,2,1
2,0,5,2,3
1,4,3,0,3
3,3,1,1,2
2,0,1,1,1
4,4,0,2,2
2,5,4,4,5
4,0,2,3,2
4,4,1,2,0
0,0,1,2,0
2,0,3,2,3
0,1,5,3,3
4,2,0,1,5
5,4,2,1,1
3,1,4,5,0
1,0,2,3,4
1,0,2,1,2
3,2,2,1,2
5,3,3,5,2
2,2,5,4,5
1,2,2,4,3
0,1,2,3,1
2,5,1,4,3
4,4,5,4,2
4,1,5,4,4
2,5,4,0,1
1,5,2,4,2
1,3,3,2,2
0,0,0,1,2
2,4,3,2,2
5,4,5,1,2
1,4,0,4,1
0,3,3,5,0
3,2,1,0,0
4,1,2,3,5
2,2,2,2,4
0,4,4,4,2
0,3,0,1,2
4,4,0,3,2
0,4,2,5,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   D             -- 116 -- First place
   B             -- 115 -- Second place
   C             -- 108
   E             -- 104
   A             --  92
 D and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 20 -- Tied for first place
   D             -- 20 -- Tied for first place
   Equal Support --  5
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   D             -- 116 -- First place
   B             -- 115
 D wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 D
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |       A      |    * B      |      C      |    * D      |      E      |
-----------------------------------------------------------------------------------------
             A > |     ---      |16 -  9 - 20 |15 -  4 - 26 |16 -  9 - 20 |15 -  7 - 23 |
           * B > | 20 -  9 - 16 |    ---      |19 -  8 - 18 |20 -  5 - 20 |23 -  4 - 18 |
             C > | 26 -  4 - 15 |18 -  8 - 19 |    ---      |17 -  6 - 22 |20 -  9 - 16 |
           * D > | 20 -  9 - 16 |20 -  5 - 20 |22 -  6 - 17 |    ---      |17 - 10 - 18 |
             E > | 23 -  7 - 15 |18 -  4 - 23 |16 -  9 - 20 |18 - 10 - 17 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; weak Condorcet winner: B — STAR elected D instead

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A           3   8   6   9   9  10  |    92   2.0
B           5  12   7   8   5   8  |   115   2.6
C           6   7   6  13   6   7  |   108   2.4
D           5  10   7  10  10   3  |   116   2.6
E           6   4   7  15   7   6  |   104   2.3
```

Everything in one file: the [`_tabulated` mirror](../star_vs_rr_divergence_tabulated/cycle_C05_medV45_noise_2_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/star_vs_rr_divergence/cycle_C05_medV45_noise_2.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_C03_fewV15_noise_1](cycle_C03_fewV15_noise_1.md) · [cycle_C03_fewV15_noise_2](cycle_C03_fewV15_noise_2.md) · [cycle_C03_medV45_noise_1](cycle_C03_medV45_noise_1.md) · [cycle_C03_medV45_noise_2](cycle_C03_medV45_noise_2.md) · [cycle_C05_fewV15_noise_1](cycle_C05_fewV15_noise_1.md) · [cycle_C05_fewV15_noise_2](cycle_C05_fewV15_noise_2.md) · [cycle_C05_fewV28_bloc_1](cycle_C05_fewV28_bloc_1.md) · [cycle_C05_medV45_noise_1](cycle_C05_medV45_noise_1.md) · [cycle_C07_fewV15_noise_1](cycle_C07_fewV15_noise_1.md) · [cycle_C07_fewV28_bloc_2](cycle_C07_fewV28_bloc_2.md) · [cycle_C07_largeV598_bloc_1](cycle_C07_largeV598_bloc_1.md) · [cycle_C07_medV149_bloc_2](cycle_C07_medV149_bloc_2.md) · [cycle_C10_fewV15_noise_1](cycle_C10_fewV15_noise_1.md) · [cycle_C10_fewV15_noise_2](cycle_C10_fewV15_noise_2.md) · [cycle_C10_fewV28_bloc_1](cycle_C10_fewV28_bloc_1.md) · [cycle_C10_fewV29_bloc_2](cycle_C10_fewV29_bloc_2.md) · [cycle_C10_medV148_bloc_1](cycle_C10_medV148_bloc_1.md) · [cycle_C10_medV149_bloc_2](cycle_C10_medV149_bloc_2.md) · [cycle_C10_medV45_noise_1](cycle_C10_medV45_noise_1.md) · [cycle_C10_medV45_noise_2](cycle_C10_medV45_noise_2.md) · [darkhorse_C03_fewV15_noise_1](darkhorse_C03_fewV15_noise_1.md) · [darkhorse_C05_largeV599_bloc_1](darkhorse_C05_largeV599_bloc_1.md) · [darkhorse_C07_fewV30_bloc_1](darkhorse_C07_fewV30_bloc_1.md) · [darkhorse_C07_largeV597_bloc_1](darkhorse_C07_largeV597_bloc_1.md) · [darkhorse_C07_largeV598_bloc_2](darkhorse_C07_largeV598_bloc_2.md) · [darkhorse_C07_medV147_bloc_1](darkhorse_C07_medV147_bloc_1.md) · [darkhorse_C07_medV45_noise_1](darkhorse_C07_medV45_noise_1.md) · [darkhorse_C10_largeV598_bloc_1](darkhorse_C10_largeV598_bloc_1.md) · [darkhorse_C10_largeV599_bloc_2](darkhorse_C10_largeV599_bloc_2.md)
