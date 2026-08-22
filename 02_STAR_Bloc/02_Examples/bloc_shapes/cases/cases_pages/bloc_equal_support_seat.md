---
search:
  exclude: true
---

# Bloc STAR — a seat decided by 11 voters out of 31

*Generated from [`bloc_equal_support_seat.yaml`](../bloc_equal_support_seat.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../01_Learn/README.md) · **3 seats** · **Expected winners:** Croissant, Almond, Brioche

## Scenario

Thirty-one voters fill three seats from five pastries. The interesting seat is
the second one, and the interesting number is not who won but how many voters
had any say in it.

  - Seat 1: Croissant 133, Almond 120, Brioche 117, Danish 20, Eclair 11.
    Finalists Croissant and Almond; Croissant wins the runoff 25-6.
  - Seat 2: Croissant is removed. Finalists Almond 120 and Brioche 117 — and
    TWENTY of the thirty-one voters scored both of them 4. Those twenty express
    no preference. The seat is decided 6-5 by the eleven voters who did
    differentiate, and Almond takes it.
  - Seat 3: Brioche 117 v Danish 20; Brioche wins 31-0.

Council: Croissant, Almond, Brioche. No rung of the tie-break ladder is
consulted.

The engine's runoff summary line states this in full rather than leaving the
denominator to be inferred: "Voters with a preference: 11 of 31 (20 Equal
Support). Almond 6 (55%) vs Brioche 5 (45%); majority = 6."

This is not a defect, and it is worth being precise about why. Equal Support is
a real expression: those twenty voters were asked which of Almond and Brioche
they preferred and answered "neither, equally". A method that forced them to
invent a preference would be recording something they did not say. But it does
mean a bloc seat can turn on a small slice of the electorate, and a report that
prints only "Almond 6, Brioche 5" would hide that.

All three proportional STAR methods elect the same three pastries here, in a
different seat order. This is one of the cases where the choice of method does
not change the outcome — included deliberately, because a folder of nothing but
divergences would misrepresent how often they happen.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Almond,Brioche,Croissant,Danish,Eclair
4,4,5,1,0   # twenty voters rate Almond and Brioche identically
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
4,4,5,1,0
5,2,3,0,1   # six voters clearly prefer Almond
5,2,3,0,1
5,2,3,0,1
5,2,3,0,1
5,2,3,0,1
5,2,3,0,1
2,5,3,0,1   # five voters clearly prefer Brioche
2,5,3,0,1
2,5,3,0,1
2,5,3,0,1
2,5,3,0,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Bloc STAR Voting Method (3 winners) ---

[Bloc STAR]
 Tabulating 31 ballots to fill 3 seats.
Count × Almond,Brioche,Croissant,Danish,Eclair
   20 ×      4,      4,        5,     1,     0
    6 ×      5,      2,        3,     0,     1
    5 ×      2,      5,        3,     0,     1

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Croissant     -- 133 -- First place
   Almond        -- 120 -- Second place
   Brioche       -- 117
   Danish        --  20
   Eclair        --  11
 Croissant and Almond advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Croissant     -- 25 -- First place
   Almond        --  6
   Equal Support --  0
 Croissant wins.
   Runoff math:
     31  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     31  voters with a preference  (majority = 16)
           Croissant 25 (81%)  ·  Almond 6 (19%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Almond        -- 120 -- First place
   Brioche       -- 117 -- Second place
   Danish        --  20
   Eclair        --  11
 Almond and Brioche advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Almond        -- 6 -- First place
   Brioche       -- 5
   Equal Support -- 20
 Almond wins.
   Runoff math:
     31  ballots cast
   − 20  Equal Support (no preference between the two finalists)
     ──
     11  voters with a preference  (majority = 6)
           Almond 6 (55%)  ·  Brioche 5 (45%)

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Brioche       -- 117 -- First place
   Danish        --  20 -- Second place
   Eclair        --  11
 Brioche and Danish advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Brioche       -- 31 -- First place
   Danish        --  0
   Equal Support --  0
 Brioche wins.
   Runoff math:
     31  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     31  voters with a preference  (majority = 16)
           Brioche 31 (100%)  ·  Danish 0 (0%)

[Bloc STAR: Winners — Bloc STAR Voting Method (3 winners)]
 Croissant
 Almond
 Brioche
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 3-winner count below,
        so no Top-2 finalists are marked.
                  |     Almond    |    Brioche   |   Croissant  |    Danish    |    Eclair    |
-----------------------------------------------------------------------------------------------
         Almond > |      ---      | 6 - 20 -  5  | 6 -  0 - 25  |31 -  0 -  0  |31 -  0 -  0  |
        Brioche > |  5 - 20 -  6  |     ---      | 5 -  0 - 26  |31 -  0 -  0  |31 -  0 -  0  |
      Croissant > | 25 -  0 -  6  |26 -  0 -  5  |     ---      |31 -  0 -  0  |31 -  0 -  0  |
         Danish > |  0 -  0 - 31  | 0 -  0 - 31  | 0 -  0 - 31  |     ---      |20 -  0 - 11  |
         Eclair > |  0 -  0 - 31  | 0 -  0 - 31  | 0 -  0 - 31  |11 -  0 - 20  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Croissant — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Eclair — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Almond      6  20   0   5   0   0  |   120   3.9
Brioche     5  20   0   6   0   0  |   117   3.8
Croissant  20   0  11   0   0   0  |   133   4.3
Danish      0   0   0   0  20  11  |    20   0.6
Eclair      0   0   0   0  11  20  |    11   0.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bloc_equal_support_seat_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/bloc_shapes/cases/bloc_equal_support_seat.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bloc_all_but_one](bloc_all_but_one.md) · [bloc_condorcet_winner_no_seat](bloc_condorcet_winner_no_seat.md) · [bloc_divided_majority](bloc_divided_majority.md) · [bloc_finalist_wins_nothing](bloc_finalist_wins_nothing.md) · [bloc_harborview_council](bloc_harborview_council.md) · [bloc_no_majority_bridge](bloc_no_majority_bridge.md) · [bloc_one_voter_council](bloc_one_voter_council.md) · [bloc_score_leader_shut_out](bloc_score_leader_shut_out.md) · [bloc_widest_field](bloc_widest_field.md)
