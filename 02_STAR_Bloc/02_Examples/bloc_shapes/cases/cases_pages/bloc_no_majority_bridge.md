---
search:
  exclude: true
---

# Bloc STAR — no faction has a majority, and the second-largest wins nothing

*Generated from [`bloc_no_majority_bridge.yaml`](../bloc_no_majority_bridge.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../01_Learn/README.md) · **4 seats** · **Expected winners:** Jaya, Ada, Gita, Bram

## Scenario

One hundred and one voters fill FOUR seats from TEN candidates. No faction has
a majority: Blue 40%, Green 35%, Amber 26%. Jaya runs as an independent and is
nobody's favourite — every faction scores Jaya 3 or 4.

  - Seat 1: Jaya 324 leads the scoring round outright, ahead of Ada 227 and
    Bram 219. Jaya beats Ada in the runoff 61-40.
  - Seat 2: Ada 227 v Bram 219 — both Blue. Ada wins 8-0, with 93 of the 101
    voters expressing no preference between two candidates they scored equally.
  - Seat 3: Bram 219 v Gita 190 — Gita (Amber) wins the runoff 54-47.
  - Seat 4: Bram 219 v Dov 189 — Bram wins 60-41.

Council: Jaya, Ada, Gita, Bram. No rung of the tie-break ladder is consulted.

Two things here are worth slowing down for.

FIRST — Jaya. A candidate with no faction at all wins the first seat, on
breadth rather than depth: 3s and 4s from everybody add up to more than 5s from
40% of the electorate. That is the thing a 0-5 ballot can see and a choose-one
ballot cannot, and it is Bloc STAR working WELL. Jaya is elected under every
method tried here.

SECOND — Green. The second-largest faction, 35% of the electorate, elects
NOBODY. Its best candidate Dov scores 189, behind Bram's 219, so Dov only
reaches a runoff in the final round and loses it. Meanwhile Amber, at 26%, wins
a seat. Bloc STAR's seat allocation does not track faction size, and here it
is not even monotone in it: a smaller faction is represented and a larger one
is not.

Proportional STAR (Allocated Score, and both other PR methods) elects Ada, Dov,
Gita and Jaya — one seat for each of the three factions, plus the independent.
That is the clean statement of the difference: the same ballots, one count
answering "who is most liked?" four times over, the other asking "who is not
yet represented?"

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Bram,Ceci,Dov,Esme,Finn,Gita,Hank,Ines,Jaya
32:5,5,4,0,0,0,1,1,1,3   # Blue loyalists
8:5,4,4,1,1,1,0,0,0,4    # Blue leaners
28:0,0,0,5,5,4,1,1,1,3   # Green loyalists
7:1,1,1,5,4,4,0,0,0,4    # Green leaners
20:1,1,1,0,0,0,5,5,4,3   # Amber loyalists
6:0,0,0,1,1,1,5,4,4,4    # Amber leaners
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Jaya
  Choose-One (Plurality) = Ada   (differs from STAR)
  RCV-IRV                = Ada   (differs from STAR)
  Note: 101 of 101 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bloc_no_majority_bridge_RCV-IRV_tabulated.txt

--- Bloc STAR Voting Method (4 winners) ---

[Bloc STAR]
 Tabulating 101 ballots to fill 4 seats.
Count × Ada,Bram,Ceci,Dov,Esme,Finn,Gita,Hank,Ines,Jaya
   32 ×   5,   5,   4,  0,   0,   0,   1,   1,   1,   3
   28 ×   0,   0,   0,  5,   5,   4,   1,   1,   1,   3
   20 ×   1,   1,   1,  0,   0,   0,   5,   5,   4,   3
    8 ×   5,   4,   4,  1,   1,   1,   0,   0,   0,   4
    7 ×   1,   1,   1,  5,   4,   4,   0,   0,   0,   4
    6 ×   0,   0,   0,  1,   1,   1,   5,   4,   4,   4

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Jaya          -- 324 -- First place
   Ada           -- 227 -- Second place
   Bram          -- 219
   Gita          -- 190
   Dov           -- 189
   Ceci          -- 187
   Hank          -- 184
   Esme          -- 182
   Ines          -- 164
   Finn          -- 154
 Jaya and Ada advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Jaya          -- 61 -- First place
   Ada           -- 40
   Equal Support --  0
 Jaya wins.
   Runoff math:
     101  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     101  voters with a preference  (majority = 51)
           Jaya 61 (60%)  ·  Ada 40 (40%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 227 -- First place
   Bram          -- 219 -- Second place
   Gita          -- 190
   Dov           -- 189
   Ceci          -- 187
   Hank          -- 184
   Esme          -- 182
   Ines          -- 164
   Finn          -- 154
 Ada and Bram advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 8 -- First place
   Bram          -- 0
   Equal Support -- 93
 Ada wins.
   Runoff math:
     101  ballots cast
   −  93  Equal Support (no preference between the two finalists)
     ───
       8  voters with a preference  (majority = 5)
           Ada 8 (100%)  ·  Bram 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bram          -- 219 -- First place
   Gita          -- 190 -- Second place
   Dov           -- 189
   Ceci          -- 187
   Hank          -- 184
   Esme          -- 182
   Ines          -- 164
   Finn          -- 154
 Bram and Gita advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Gita          -- 54 -- First place
   Bram          -- 47
   Equal Support --  0
 Gita wins.
   Runoff math:
     101  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     101  voters with a preference  (majority = 51)
           Gita 54 (53%)  ·  Bram 47 (47%)

──────────────────────────────────────────────────

[Bloc STAR: Round 4: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bram          -- 219 -- First place
   Dov           -- 189 -- Second place
   Ceci          -- 187
   Hank          -- 184
   Esme          -- 182
   Ines          -- 164
   Finn          -- 154
 Bram and Dov advance.

[Bloc STAR: Round 4: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bram          -- 60 -- First place
   Dov           -- 41
   Equal Support --  0
 Bram wins.
   Runoff math:
     101  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     101  voters with a preference  (majority = 51)
           Bram 60 (59%)  ·  Dov 41 (41%)

[Bloc STAR: Winners — Bloc STAR Voting Method (4 winners)]
 Jaya
 Ada
 Gita
 Bram
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 4-winner count below,
        so no Top-2 finalists are marked.
                 |      Ada     |     Bram    |     Ceci    |     Dov     |     Esme    |     Finn    |     Gita    |     Hank    |     Ines    |     Jaya    |
---------------------------------------------------------------------------------------------------------------------------------------------------------------
           Ada > |     ---      | 8 - 93 -  0 |40 - 61 -  0 |60 -  0 - 41 |60 -  0 - 41 |60 -  0 - 41 |47 -  0 - 54 |47 -  0 - 54 |47 -  0 - 54 |40 -  0 - 61 |
          Bram > |  0 - 93 -  8 |    ---      |32 - 69 -  0 |60 -  0 - 41 |60 -  0 - 41 |60 -  0 - 41 |47 -  0 - 54 |47 -  0 - 54 |47 -  0 - 54 |32 -  8 - 61 |
          Ceci > |  0 - 61 - 40 | 0 - 69 - 32 |    ---      |60 -  0 - 41 |60 -  0 - 41 |60 -  0 - 41 |47 -  0 - 54 |47 -  0 - 54 |47 -  0 - 54 |32 -  8 - 61 |
           Dov > | 41 -  0 - 60 |41 -  0 - 60 |41 -  0 - 60 |    ---      | 7 - 94 -  0 |35 - 66 -  0 |43 -  0 - 58 |43 -  0 - 58 |43 -  0 - 58 |35 -  0 - 66 |
          Esme > | 41 -  0 - 60 |41 -  0 - 60 |41 -  0 - 60 | 0 - 94 -  7 |    ---      |28 - 73 -  0 |43 -  0 - 58 |43 -  0 - 58 |43 -  0 - 58 |28 -  7 - 66 |
          Finn > | 41 -  0 - 60 |41 -  0 - 60 |41 -  0 - 60 | 0 - 66 - 35 | 0 - 73 - 28 |    ---      |43 -  0 - 58 |43 -  0 - 58 |43 -  0 - 58 |28 -  7 - 66 |
          Gita > | 54 -  0 - 47 |54 -  0 - 47 |54 -  0 - 47 |58 -  0 - 43 |58 -  0 - 43 |58 -  0 - 43 |    ---      | 6 - 95 -  0 |26 - 75 -  0 |26 -  0 - 75 |
          Hank > | 54 -  0 - 47 |54 -  0 - 47 |54 -  0 - 47 |58 -  0 - 43 |58 -  0 - 43 |58 -  0 - 43 | 0 - 95 -  6 |    ---      |20 - 81 -  0 |20 -  6 - 75 |
          Ines > | 54 -  0 - 47 |54 -  0 - 47 |54 -  0 - 47 |58 -  0 - 43 |58 -  0 - 43 |58 -  0 - 43 | 0 - 75 - 26 | 0 - 81 - 20 |    ---      |20 -  6 - 75 |
          Jaya > | 61 -  0 - 40 |61 -  8 - 32 |61 -  8 - 32 |66 -  0 - 35 |66 -  7 - 28 |66 -  7 - 28 |75 -  0 - 26 |75 -  6 - 20 |75 -  6 - 20 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Jaya — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Finn — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ada        40   0   0   0  27  34  |   227   2.2
Bram       32   8   0   0  27  34  |   219   2.2
Ceci        0  40   0   0  27  34  |   187   1.9
Dov        35   0   0   0  14  52  |   189   1.9
Esme       28   7   0   0  14  52  |   182   1.8
Finn        0  35   0   0  14  52  |   154   1.5
Gita       26   0   0   0  60  15  |   190   1.9
Hank       20   6   0   0  60  15  |   184   1.8
Ines        0  26   0   0  60  15  |   164   1.6
Jaya        0  21  80   0   0   0  |   324   3.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bloc_no_majority_bridge_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/bloc_shapes/cases/bloc_no_majority_bridge.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bloc_all_but_one](bloc_all_but_one.md) · [bloc_condorcet_winner_no_seat](bloc_condorcet_winner_no_seat.md) · [bloc_divided_majority](bloc_divided_majority.md) · [bloc_equal_support_seat](bloc_equal_support_seat.md) · [bloc_finalist_wins_nothing](bloc_finalist_wins_nothing.md) · [bloc_harborview_council](bloc_harborview_council.md) · [bloc_one_voter_council](bloc_one_voter_council.md) · [bloc_score_leader_shut_out](bloc_score_leader_shut_out.md) · [bloc_widest_field](bloc_widest_field.md)
