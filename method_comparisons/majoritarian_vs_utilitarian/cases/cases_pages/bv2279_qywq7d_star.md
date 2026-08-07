---
search:
  exclude: true
---

# Three brothers, one fruit — the majoritarian winner is not the utilitarian one

*Generated from [`bv2279_qywq7d_star.yaml`](../bv2279_qywq7d_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Banana

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qywq7d) · **[results ↗](https://bettervoting.com/qywq7d/results)** (election `qywq7d` · test `BV2279`).

## Scenario

Race 1 of 3 in the three-brothers election (BV2279, bvid qywq7d; BV-confirmed).
Live results: https://bettervoting.com/qywq7d/results
Companion races: bv2279_qywq7d_ranked_robin.yaml (also elects Banana) and
bv2279_qywq7d_approval.yaml (elects Orange).

The smallest election in which the two deepest ideals of a "good winner"
name different candidates.

The construction is Warren Smith's "three brothers split one fruit"
(rangevoting.org), quoted for years in this repo as a prose table of
happiness numbers on an arbitrary 0-11 scale. This file is that table
made runnable: the utilities are rescaled x5/11 onto a real 0-5 STAR
ballot, which preserves every relation the example turns on — the
ordering of the totals, and every head-to-head.

  original utility   Apple  Orange  Banana        this ballot   Apple  Orange  Banana
  boy 1                  2       7       8        boy 1             1       3       4
  boy 2                  3       9      10        boy 2             1       4       5
  boy 3                  4      11       0        boy 3             2       5       0
  average                3       9       6        total             4      12       9

Two answers, both defensible:

UTILITARIAN — Orange maximizes total satisfaction (12 points to
Banana's 9). Banana is the favorite of two brothers but is worth
literally nothing to the third, and that zero is the whole story.
Orange is everyone's good-enough fruit.

MAJORITARIAN — Banana is the Condorcet winner. It beats Orange 2-1
head-to-head and Apple 2-1, so it wins every one-on-one matchup. A
majority prefers it, and majority preference does not care that boy 3's
loss is far larger than boys 1 and 2's gain.

What the engine shows is which ideal each stage of STAR is chasing.
The SCORING ROUND is a utilitarian count and Orange leads it. The
AUTOMATIC RUNOFF is a majoritarian check and it overturns that result:
Banana 2, Orange 1. STAR elects Banana.

So this is a case where STAR does NOT elect the utilitarian winner —
by design. The runoff exists precisely to make the score leader survive
a majority vote, and here it doesn't. Score voting and Approval elect
Orange; STAR, Ranked Robin, IRV and Plurality all elect Banana. Only
the two methods that never take a majority vote reach the utilitarian
answer.

Apple is the Condorcet LOSER and finishes last everywhere. It is in the
file to keep the pairwise matrix from being a two-candidate echo of the
runoff — with only Orange and Banana there is no "beats everyone"
ideal to distinguish, because head-to-head and majority rule coincide.

Neither winner is wrong. They optimize different things, which is the
point of the page this case backs.

## Ballots

The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| Ballot as marked | Apple | Orange | Banana |
|:--|:--:|:--:|:--:|
| <img src="../img/bv2279_qywq7d_star_ballot_1.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Boy 1 — banana by a nose, orange close behind: Apple 1, Orange 3, Banana 4."> | 1 | 3 | 4 |
| <img src="../img/bv2279_qywq7d_star_ballot_2.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Boy 2 — banana best, orange nearly as good: Apple 1, Orange 4, Banana 5."> | 1 | 4 | 5 |
| <img src="../img/bv2279_qywq7d_star_ballot_3.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Boy 3 — orange is everything, banana is worthless: Apple 2, Orange 5, Banana 0."> | 2 | 5 | 0 |

The same ballots as the file records them:

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Apple,Orange,Banana
1,3,4   # Boy 1 — banana by a nose, orange close behind
1,4,5   # Boy 2 — banana best, orange nearly as good
2,5,0   # Boy 3 — orange is everything, banana is worthless
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Banana
  Approval = Orange   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Orange)
 - Runoff Round Winner   = (Banana)
  Candidate Orange earned the highest total score, but
  Candidate Banana won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Apple,Orange,Banana
    1,     3,     4
    1,     4,     5
    2,     5,     0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Orange        -- 12 -- First place
   Banana        --  9 -- Second place
   Apple         --  4
 Orange and Banana advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Banana        -- 2 -- First place
   Orange        -- 1
   Equal Support -- 0
 Banana wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Banana 2 (67%)  ·  Orange 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Banana
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Apple   | * Orange  | * Banana  |
-----------------------------------------------------
       Apple > |    ---     |0 - 0 - 3  |1 - 0 - 2  |
    * Orange > | 3 - 0 - 0  |   ---     |1 - 0 - 2  |
    * Banana > | 2 - 0 - 1  |2 - 0 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Banana — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Apple — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Apple      0  0  0  1  2  0  |     4   1.3
Orange     1  1  1  0  0  0  |    12   4.0
Banana     1  1  0  0  0  1  |     9   3.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2279_qywq7d_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/majoritarian_vs_utilitarian/cases/bv2279_qywq7d_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/bv2279_qywq7d_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2279_qywq7d_approval](bv2279_qywq7d_approval.md) · [bv2279_qywq7d_ranked_robin](bv2279_qywq7d_ranked_robin.md)
