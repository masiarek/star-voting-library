---
search:
  exclude: true
---

# The Alabama paradox — 3 seats

*Generated from [`alabama_3seats.yaml`](../alabama_3seats.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../01_Learn/README.md) · **3 seats**

## Scenario

Five gardeners scoring four candidates for a community-garden committee. These are the SAME five ballots as the other file in this folder; the only difference is how many seats are up. At two seats Proportional STAR seats Basil and Dahlia. At three seats it seats Aster, Basil and Clover — Dahlia has LOST her seat because the committee grew. That is the Alabama paradox, a failure of house-size monotonicity, and it is a known property of quota methods rather than a bug in this file.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Aster,Basil,Clover,Dahlia
3,3,2,4
5,4,0,2
1,0,4,3
0,5,5,3
5,5,0,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Aster
  RCV-IRV  = Dahlia   (differs from STAR)
  Approval = Basil   (differs from STAR)
  RCV-RR   = Basil   (differs from STAR)
  Note: 3 of 5 ballots (60%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/alabama_3seats_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/alabama_3seats_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Basil)
 - Runoff Round Winner   = (Aster)
  Candidate Basil earned the highest total score, but
  Candidate Aster won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
 Tabulating 5 ballots to fill 3 seats.
Aster,Basil,Clover,Dahlia
    3,    3,     2,     4
    5,    4,     0,     2
    1,    0,     4,     3
    0,    5,     5,     3
    5,    5,     0,     0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Basil         -- 17 -- First place
   Aster         -- 14
   Dahlia        -- 12
   Clover        -- 11
 Basil wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 1+2/3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 83.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/6.
 2 ballots reweighted from 1 to 1/6.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Aster         -- 9+5/6 -- First place
   Dahlia        -- 9+1/2
   Clover        -- 6+5/6
 Aster wins a seat.

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 1+2/3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 1 ballot at score 5.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 2]
 Remaining allocation quota is 2/3.
 Allocating 1 ballot at score 3.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 66.67% of this ballot.
 Keeping this ballot, but multiplying its weight by 1/3.
 1 ballot reweighted from 1 to 1/3.

[Allocated Score Voting: Round 3]
 Tabulating 4 remaining ballots.
Aster,Basil,Clover,Dahlia
    3,    3,     2,     4
    5,    4,     0,     2
    1,    0,     4,     3
    0,    5,     5,     3
    5,    5,     0,     0

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Aster
 Basil
 Clover
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 3-winner count below,
        so no Top-2 finalists are marked.
               |    Aster   |   Basil   |   Clover  |   Dahlia  |
-----------------------------------------------------------------
       Aster > |    ---     |2 - 2 - 1  |3 - 0 - 2  |2 - 0 - 3  |
       Basil > | 1 - 2 - 2  |   ---     |3 - 1 - 1  |3 - 0 - 2  |
      Clover > | 2 - 0 - 3  |1 - 1 - 3  |   ---     |2 - 1 - 2  |
      Dahlia > | 3 - 0 - 2  |2 - 0 - 3  |2 - 1 - 2  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Aster > Basil > Dahlia > Aster)

[Condorcet Loser]
  No strict Condorcet loser; weak Condorcet loser: Clover (never wins a matchup)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Aster      2  0  1  0  1  1  |    14   2.8
Basil      2  1  1  0  0  1  |    17   3.4
Clover     1  1  0  1  0  2  |    11   2.2
Dahlia     0  1  2  1  0  1  |    12   2.4
 Hare quota is 5/3.

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Aster      2  0  1  0  1  1  |    14   2.8
Basil      2  1  1  0  0  1  |    17   3.4
Clover     1  1  0  1  0  2  |    11   2.2
Dahlia     0  1  2  1  0  1  |    12   2.4
 The highest-scoring candidate wins a seat.
   Clover        -- 5+1/2 -- First place
   Dahlia        -- 4+5/6
 Clover wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/alabama_3seats_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/alabama_paradox/cases/alabama_3seats.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../../07_Concepts/topics/monotonicity/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [alabama_2seats](alabama_2seats.md)
