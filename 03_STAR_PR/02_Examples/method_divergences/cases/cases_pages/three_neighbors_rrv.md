---
search:
  exclude: true
---

# Three neighbors, two seats — Reweighted Range Voting

*Generated from [`three_neighbors_rrv.yaml`](../three_neighbors_rrv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Reweighted Range Voting (proportional STAR)](../../../../01_Learn/README.md) · **2 seats** · **Expected winners:** Ana, Cleo

## Scenario

The smallest election in which two proportional STAR tabulations disagree:
three voters, three candidates, two seats. Ana, Bo and Cleo are up; Cleo is
the runaway favorite and takes seat 1 under every method. The argument is
entirely about seat 2.

Neighbor 2 is the odd one out. She is lukewarm on Cleo (2 stars), cool on Bo
(2), and gives Ana nothing. Neighbors 1 and 3 both love Cleo (5) and like
Ana (4).

After Cleo is seated, the three methods disagree about what neighbor 2's
two-star support for Cleo COST her:

  * Allocated Score allocates by score TIER. The 5-star group (neighbors 1
    and 3) already overfills the 1.5-voter quota, so neighbor 2 is never
    allocated at all and keeps her FULL weight. She alone decides seat 2,
    and her best remaining candidate is Bo -- who has 3 points in total,
    against Ana's 8.  ->  Bo, Cleo

  * Sequentially Spent Score charges every supporter in PROPORTION to the
    score they gave, so neighbor 2's 2 stars for Cleo did cost her weight.
    She can no longer outweigh the residue left to neighbors 1 and 3, and
    their 4-star support carries Ana in.  ->  Ana, Cleo

  * Reweighted Range Voting divides every ballot's weight instead of
    spending it, and lands with SSS.  ->  Ana, Cleo

Same three ballots; the seat turns purely on how a partial supporter is
charged for a winner they only partly wanted. Found by an exhaustive
smallest-first search and verified stable across five tiebreaker seeds, so
no lot is involved.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Bo,Cleo
4,0,5      # Neighbor 1 — loves Cleo, likes Ana
0,2,2      # Neighbor 2 — lukewarm on Cleo and Bo, nothing for Ana
4,1,5      # Neighbor 3 — loves Cleo, likes Ana
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Cleo
  Approval = Ana   (differs from STAR)

--- Reweighted Range Voting Method (2 winners) ---

[Reweighted Range Voting]
 Tabulating 3 ballots to fill 2 seats.
Ana,Bo,Cleo
  4, 0,   5
  0, 2,   2
  4, 1,   5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Cleo          -- 12 -- First place
   Ana           --  8
   Bo            --  3
 Cleo wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 3 ballots:
   2 ballots reweighted from 1 to 1/2.
   1 ballot reweighted from 1 to 5/7.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Ana           -- 4       -- First place
   Bo            -- 1+13/14
 Ana wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (2 winners)]
 Ana
 Cleo
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Ana    |     Bo    |    Cleo   |
-----------------------------------------------------
         Ana > |    ---     |2 - 0 - 1  |0 - 0 - 3  |
          Bo > | 1 - 0 - 2  |   ---     |0 - 1 - 2  |
        Cleo > | 3 - 0 - 0  |2 - 1 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cleo — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Bo — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        0  2  0  0  0  1  |     8   2.7
Bo         0  0  0  1  1  1  |     3   1.0
Cleo       2  0  0  1  0  0  |    12   4.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/three_neighbors_rrv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 03_STAR_PR/02_Examples/method_divergences/cases/three_neighbors_rrv.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Exhausted ballots (conversation)](../../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [three_neighbors_allocated](three_neighbors_allocated.md) · [three_neighbors_sss](three_neighbors_sss.md) · [two_officers_allocated](two_officers_allocated.md) · [two_officers_rrv](two_officers_rrv.md) · [two_officers_sss](two_officers_sss.md)
