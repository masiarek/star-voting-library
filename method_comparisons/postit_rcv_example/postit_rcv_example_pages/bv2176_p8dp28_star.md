# The Post-it RCV example (20 voters) — STAR: Blue wins the runoff RCV-IRV never held

*Generated from [`bv2176_p8dp28_star.yaml`](../bv2176_p8dp28_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Blue

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28`).

## Scenario

One of three races in the Post-it RCV example (BV2176, bvid p8dp28;
BV-confirmed). The 20-voter election from Equal Vote's video "Updated: How
does RCV work? — With Post-its!" (https://youtu.be/Vte4nly_Neg), using the
video's own 0-5 scores from the same voters whose ranked ballots it walks
through. Scoring round: Purple 46, Blue 44, Pink 44, Green 38 — Purple
advances, and the 44-44 tie for the second finalist breaks head-to-head
(Blue is preferred over Pink 10-3). Automatic runoff: Blue beats Purple
10-9 (1 Equal Support) — a Runoff Reversal (the score leader loses the
majority check), and it is exactly the 10-9 majority the video surfaces in
its "what if Green had been eliminated instead of Blue?" hypothetical.
RCV-IRV on these voters' ranked ballots elects Purple without ever holding
that matchup (see the companion race). BetterVoting agrees: Blue, with
tieBreakType head_to_head on the scoring tie.

Live results: https://bettervoting.com/p8dp28/results
Companion races: bv2176_p8dp28_irv.yaml, bv2176_p8dp28_ranked_robin.yaml.
Overview page: bv2176_p8dp28_postit_rcv_example.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Purple,Green,Blue,Pink
5,0,0,0
5,0,0,0
5,0,0,0
5,0,0,0
5,0,0,0
5,0,0,0
5,0,0,0
0,5,4,3
0,5,4,3
0,5,4,3
0,5,4,3
0,5,4,3
0,5,4,3
0,0,5,4
0,0,5,4
0,4,5,3
4,0,5,0
3,4,0,5
4,0,0,5
0,0,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Blue
  Choose-One (Plurality) = Purple   (differs from STAR)
  RCV-IRV                = Purple   (differs from STAR)
  Approval               = Pink   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: postit_rcv_example_tabulated/bv2176_p8dp28_star_RCV-IRV_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Purple)
 - Runoff Round Winner   = (Blue)
  Candidate Purple earned the highest total score, but
  Candidate Blue won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 20 ballots.
Count × Purple,Green,Blue,Pink
    7 ×      5,    0,   0,   0
    6 ×      0,    5,   4,   3
    2 ×      0,    0,   5,   4
    1 ×      0,    4,   5,   3
    1 ×      4,    0,   5,   0
    1 ×      3,    4,   0,   5
    1 ×      4,    0,   0,   5
    1 ×      0,    0,   0,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Purple        -- 46 -- First place
   Blue          -- 44 -- Tied for second place
   Pink          -- 44 -- Tied for second place
   Green         -- 38
 Purple advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Blue          -- 10 -- Second place
   Pink          --  3
   Equal Support --  7
 Purple and Blue advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blue          -- 10 -- First place
   Purple        --  9
   Equal Support --  1
 Blue wins.
   Runoff math:
     20  ballots cast
   −  1  Equal Support (no preference between the two finalists)
     ──
     19  voters with a preference  (majority = 10)
           Blue 10 (53%)  ·  Purple 9 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Blue
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Purple   |    Green    |   * Blue    |     Pink    |
---------------------------------------------------------------------------
      * Purple > |     ---      | 9 -  3 -  8 | 9 -  1 - 10 | 8 -  0 - 12 |
         Green > |  8 -  3 -  9 |    ---      | 7 -  9 -  4 | 7 -  8 -  5 |
        * Blue > | 10 -  1 -  9 | 4 -  9 -  7 |    ---      |10 -  7 -  3 |
          Pink > | 12 -  0 -  8 | 5 -  8 -  7 | 3 -  7 - 10 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Purple > Green > Blue > Pink > Purple)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Purple      7   2   1   0   0  10  |    46   2.3
Green       6   2   0   0   0  12  |    38   1.9
Blue        4   6   0   0   0  10  |    44   2.2
Pink        3   2   7   0   0   8  |    44   2.2
```

</details>

Everything in one file: the [`_tabulated` mirror](../postit_rcv_example_tabulated/bv2176_p8dp28_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/bv2176_p8dp28_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/CYCLE_OR_THREE_WAY/bv2176_p8dp28_star.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_irv](bv2176_p8dp28_irv.md) · [bv2176_p8dp28_ranked_robin](bv2176_p8dp28_ranked_robin.md) · [bv2177_v8r66y_approval](bv2177_v8r66y_approval.md) · [bv2177_v8r66y_plurality](bv2177_v8r66y_plurality.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_ranked_robin](bv2178_8kg698_ranked_robin.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
