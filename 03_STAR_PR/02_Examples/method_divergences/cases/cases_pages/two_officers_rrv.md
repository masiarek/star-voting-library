---
search:
  exclude: true
---

# Two officers, three candidates — Reweighted Range Voting

*Generated from [`two_officers_rrv.yaml`](../two_officers_rrv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Reweighted Range Voting (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Dana, Eli

## Scenario

The companion to "three neighbors": the smallest election that splits the
DIVISOR method off from the two QUOTA methods. Three voters, three
candidates, two seats. Dana leads on score (9, against Eli 8 and Finn 7) and
takes seat 1 under every method. Seat 2 is the argument.

Voters 1 and 2 both gave Dana 4 stars; voter 3 gave her only 1. Everything
turns on how hard those two big backers are charged for the seat they won --
and the three methods form a clean ladder from harshest to gentlest:

  * Allocated Score charges them down to 1/4. The 1.5-voter quota is
    overfilled by the two 4-star ballots, so fractional surplus leaves them
    at a quarter. Voter 3 is never reached by the score tiers at all and
    keeps FULL weight.      ->  Eli 4+1/4, Finn 4+3/4  ->  Dana, Finn

  * SSS charges them down to 1/3, against a SCORE quota (total 9, Hare score
    quota 7+1/2) rather than a ballot quota. Voter 3 pays too, landing at
    5/6.                     ->  Eli 4+1/6, Finn 4+1/3  ->  Dana, Finn

  * RRV computes no quota at all and merely DIVIDES: weight becomes
    1 / (1 + score_given_to_winners / max_score), so the two land at 5/9 --
    dampened, not spent. They keep enough to carry their shared second
    choice.                  ->  Eli 5+5/18, Finn 5     ->  Dana, Eli

1/4, 1/3, 5/9. As the charge gets gentler the partly-satisfied voters keep
more say, and at the last rung their second choice overtakes. Found by
exhaustive smallest-first search, verified stable across five tiebreaker
seeds, so no lot is involved.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dana,Eli,Finn
4,3,1      # Voter 1 — Dana first, Eli a solid second
4,2,2      # Voter 2 — Dana first, Eli and Finn equal behind
1,3,4      # Voter 3 — Finn first, barely backs Dana
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Reweighted Range Voting Method (2 winners) ---

[Reweighted Range Voting]
 Tabulating 3 ballots to fill 2 seats.
Dana,Eli,Finn
   4,  3,   1
   4,  2,   2
   1,  3,   4

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Dana          -- 9 -- First place
   Eli           -- 8
   Finn          -- 7
 Dana wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 3 ballots:
   2 ballots reweighted from 1 to 5/9.
   1 ballot reweighted from 1 to 5/6.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Eli           -- 5+5/18 -- First place
   Finn          -- 5
 Eli wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (2 winners)]
 Dana
 Eli
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Dana   |  * Eli    |    Finn   |
-----------------------------------------------------
      * Dana > |    ---     |2 - 0 - 1  |2 - 0 - 1  |
       * Eli > | 1 - 0 - 2  |   ---     |1 - 1 - 1  |
        Finn > | 1 - 0 - 2  |1 - 1 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Dana — matches the STAR winner

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: Eli, Finn (winless — pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Dana       0  2  0  0  1  0  |     9   3.0
Eli        0  0  2  1  0  0  |     8   2.7
Finn       0  1  0  1  1  0  |     7   2.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/two_officers_rrv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/02_Examples/method_divergences/cases/two_officers_rrv.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Exhausted ballots (conversation)](../../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [three_neighbors_allocated](three_neighbors_allocated.md) · [three_neighbors_rrv](three_neighbors_rrv.md) · [three_neighbors_sss](three_neighbors_sss.md) · [two_officers_allocated](two_officers_allocated.md) · [two_officers_sss](two_officers_sss.md)
