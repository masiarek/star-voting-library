---
search:
  exclude: true
---

# BV2266 — Seat order: the candidate who beats every rival is seated second

*Generated from [`bv2266_k7pfqt_condorcet_winner_seated_second.yaml`](../bv2266_k7pfqt_condorcet_winner_seated_second.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../../03_STAR_PR/01_Learn) · **2 seats** · **Expected winners:** Dev, Anika

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/k7pfqt) · **[results ↗](https://bettervoting.com/k7pfqt/results)** (election `k7pfqt` · test `BV2266`).

## Scenario

Seven voters, four candidates, two seats, counted by Bloc STAR.

Anika beats every rival head to head — over Bo 4-2, over Cora 5-2, over Dev
4-3 — so she is the Condorcet winner of this electorate. She is seated SECOND.

  - Seat 1: scores Dev 24, Bo 22, Anika 21, Cora 15. Anika misses the
    automatic runoff by a single point; Dev beats Bo 2-1 (four voters express
    no preference between them) and takes the seat.
  - Seat 2: Dev is removed and the same ballots are re-counted. Bo 22,
    Anika 21, Cora 15; Anika beats Bo 4-2.

The lesson is what seat order means: under Bloc STAR it is the order the
runoffs finish in, not a ranking of how much the electorate wants each winner.
That matters wherever the first seat carries something extra — a chair, a
longer term, a tie-breaking vote.

The honest other half: counted for ONE seat these same ballots elect Dev and
Anika loses outright (an ordinary STAR Condorcet failure — she is third by
score and never reaches the runoff). The second seat is what rescues the
majority-preferred candidate. No tie-break is used anywhere in this election.

Reproduced on BetterVoting (election k7pfqt): BV elects Dev then Anika,
nTallyVotes 7, tieBreakType none — an exact match with the LH count. Frozen
export: bv2266_k7pfqt_condorcet_winner_seated_second_bv_export.json.
Live results: https://bettervoting.com/k7pfqt/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Anika,Bo,Cora,Dev
4,2,3,2
1,5,5,5
4,3,0,3
5,4,0,3
4,2,2,3
1,1,4,3
2,5,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Dev
  Choose-One (Plurality) = Anika   (differs from STAR)
  RCV-IRV                = Anika   (differs from STAR)
  RCV-RR (Condorcet)     = Anika   (differs from STAR)
  Note: 6 of 7 ballots (86%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2266_k7pfqt_condorcet_winner_seated_second_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/bv2266_k7pfqt_condorcet_winner_seated_second_RCV-RR_tabulated.txt

--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 7 ballots to fill 2 seats.
Anika,Bo,Cora,Dev
    4, 2,   3,  2
    1, 5,   5,  5
    4, 3,   0,  3
    5, 4,   0,  3
    4, 2,   2,  3
    1, 1,   4,  3
    2, 5,   1,  5

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dev           -- 24 -- First place
   Bo            -- 22 -- Second place
   Anika         -- 21
   Cora          -- 15
 Dev and Bo advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dev           -- 2 -- First place
   Bo            -- 1
   Equal Support -- 4
 Dev wins.
   Runoff math:
     7  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Dev 2 (67%)  ·  Bo 1 (33%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bo            -- 22 -- First place
   Anika         -- 21 -- Second place
   Cora          -- 15
 Bo and Anika advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Anika         -- 4 -- First place
   Bo            -- 2
   Equal Support -- 1
 Anika wins.
   Runoff math:
     7  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Anika 4 (67%)  ·  Bo 2 (33%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Dev
 Anika
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Anika   |   * Bo    |    Cora   |  * Dev    |
-----------------------------------------------------------------
       Anika > |    ---     |4 - 1 - 2  |5 - 0 - 2  |4 - 0 - 3  |
        * Bo > | 2 - 1 - 4  |   ---     |3 - 2 - 2  |1 - 4 - 2  |
        Cora > | 2 - 0 - 5  |2 - 2 - 3  |   ---     |2 - 1 - 4  |
       * Dev > | 3 - 0 - 4  |2 - 4 - 1  |4 - 1 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Anika — STAR elected Dev instead (Anika was eliminated in the scoring round)

[Condorcet Loser]
  Condorcet Loser: Cora — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Anika      1  3  0  1  2  0  |    21   3.0
Bo         2  1  1  2  1  0  |    22   3.1
Cora       1  1  1  1  1  2  |    15   2.1
Dev        2  0  4  1  0  0  |    24   3.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2266_k7pfqt_condorcet_winner_seated_second_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/03_Criteria/seat_order/cases/bv2266_k7pfqt_condorcet_winner_seated_second.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)
