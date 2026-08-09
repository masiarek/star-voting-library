---
search:
  exclude: true
---

# Two bullet voters, two seats — Sequentially Spent Score

*Generated from [`two_bullet_voters_sss.yaml`](../two_bullet_voters_sss.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Sequentially Spent Score (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Amy, Cy

## Scenario

The smallest known election where vote unitarity does real work: seven
voters, three candidates, two seats, counted by Sequentially Spent Score.

Round 1 seats Cy with 17 points against a Hare score quota of 17 1/2 —
no surplus, so every Cy supporter pays their FULL Cy score out of their
5-star budget. One ballot (2,2,5) gave Cy all 5 and exhausts to zero.

The two Amy bullet voters scored Cy 0. They spent nothing, so vote
unitarity — influence is only spent in exchange for representation
gained — says they keep their entire 5-star budgets. In round 2 those
budgets decide the seat: Amy 11 3/5 beats Bo 5 1/5.

This profile is also the regression case for a fork-fixed engine defect
(upstream larryhastings/starvote#19): an engine that silently drops the
zero-score ballots when another ballot exhausts elects Bo instead of Amy.
Correct SSS elects Amy and Cy.

## Ballots

The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| Ballot as marked | Amy | Bo | Cy |
|:--|:--:|:--:|:--:|
| <img src="../img/two_bullet_voters_sss_ballot_1.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Bo fan, warm on Cy: Amy 0, Bo 5, Cy 3."> | 0 | 5 | 3 |
| <img src="../img/two_bullet_voters_sss_ballot_2.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Amy bullet voter #1 — scores Cy 0: Amy 5, Bo 0, Cy 0."> | 5 | 0 | 0 |
| <img src="../img/two_bullet_voters_sss_ballot_3.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Cy leaner: Amy 0, Bo 3, Cy 4."> | 0 | 3 | 4 |
| <img src="../img/two_bullet_voters_sss_ballot_4.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Cy 5, no surplus — exhausts in round 1: Amy 2, Bo 2, Cy 5."> | 2 | 2 | 5 |
| <img src="../img/two_bullet_voters_sss_ballot_5.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Amy bullet voter #2 — scores Cy 0: Amy 5, Bo 1, Cy 0."> | 5 | 1 | 0 |
| <img src="../img/two_bullet_voters_sss_ballot_6.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Cy-only supporter: Amy 0, Bo 0, Cy 4."> | 0 | 0 | 4 |
| <img src="../img/two_bullet_voters_sss_ballot_7.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — spread-out moderate: Amy 2, Bo 2, Cy 1."> | 2 | 2 | 1 |

The same ballots as the file records them:

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy,Bo,Cy
0,5,3      # Bo fan, warm on Cy
5,0,0      # Amy bullet voter #1 — scores Cy 0
0,3,4      # Cy leaner
2,2,5      # Cy 5, no surplus — exhausts in round 1
5,1,0      # Amy bullet voter #2 — scores Cy 0
0,0,4      # Cy-only supporter
2,2,1      # spread-out moderate
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Cy
  Choose-One (Plurality) = Amy   (differs from STAR)

--- Sequentially Spent Score Voting Method (2 winners) ---

[Sequentially Spent Score]
 Tabulating 7 ballots to fill 2 seats.
Amy,Bo,Cy
  0, 5, 3
  5, 0, 0
  0, 3, 4
  2, 2, 5
  5, 1, 0
  0, 0, 4
  2, 2, 1

[Sequentially Spent Score: Round 1]
 The highest-scoring candidate wins a seat.
   Cy            -- 17 -- First place
   Amy           -- 14
   Bo            -- 13
 Cy wins a seat.

[Sequentially Spent Score: Round 1: Ballot allocation round]
 Total score is 17, Hare score quota is 17+1/2, no surplus to give back.
 Reducing each ballot's stars by their vote.
 Allocated 1 ballot.
 Reweighted 4 ballots:
    2 ballots voted 4, stars reduced from 5 to 1, reweighted to 1/5.
    1 ballot voted 3, stars reduced from 5 to 2, reweighted to 2/5.
    1 ballot voted 1, stars reduced from 5 to 4, reweighted to 4/5.

[Sequentially Spent Score: Round 2]
 The highest-scoring candidate wins a seat.
   Amy           -- 11+3/5 -- First place
   Bo            --  5+1/5
 Amy wins a seat.

[Sequentially Spent Score: Winners — Sequentially Spent Score Voting Method (2 winners)]
 Amy
 Cy
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Amy    |     Bo    |     Cy    |
-----------------------------------------------------
         Amy > |    ---     |2 - 3 - 2  |3 - 0 - 4  |
          Bo > | 2 - 3 - 2  |   ---     |3 - 1 - 3  |
          Cy > | 4 - 0 - 3  |3 - 1 - 3  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Bo, Cy (pairwise ties)

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: Amy, Bo (winless — pairwise ties) — Amy elected by Choose-One (Plurality)!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        2  0  0  2  0  3  |    14   2.0
Bo         1  0  1  2  1  2  |    13   1.9
Cy         1  2  1  0  1  2  |    17   2.4
 Hare score quota is 17+1/2.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/two_bullet_voters_sss_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/03_Criteria/vote_unitarity/cases/two_bullet_voters_sss.yaml
```

## See also

- [Exhausted ballots (conversation)](../../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)
