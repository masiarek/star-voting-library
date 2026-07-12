# Symmetric centrist (47/47/3/3) — Choose-One: the poles tie, the centrist gets 6

*Generated from [`bv2170_pp2q4q_plurality.yaml`](../bv2170_pp2q4q_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Blake

**Official tie-break (lot) order:** Casey > Blake > Avery — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the Symmetric Centrist election (BV2170, bvid pp2q4q; BV-confirmed). 100 voters, three candidates, ONE electorate tabulated four ways. Under Choose-One (Plurality) only first choices count: Avery 47, Blake 47, Casey 6. The centrist Condorcet winner finishes last on first choices, and the two poles tie 47–47.

Random tiebreak — NOT freezable. The 47–47 pole tie is exact (perfect symmetry), so BetterVoting breaks it at RANDOM; this run elected Blake (frozen in the export), but a re-tally could elect Avery. lot_numbers is pinned to BV's `perm` for this run so LH reproduces the frozen result; the winner here is a coin flip, not a property of the ballots.

Live results: https://bettervoting.com/pp2q4q/results
Companion races: bv2170_pp2q4q_star.yaml, bv2170_pp2q4q_irv.yaml, bv2170_pp2q4q_ranked_robin.yaml.
Overview page: bv2170_pp2q4q_symmetric_centrist.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Avery,Blake,Casey
47:1,0,0
47:0,1,0
3:0,0,1
3:0,0,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Blake
  RCV-IRV  = Avery   (differs from STAR)
  Approval = Casey   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: symmetric_centrist_bv2170_tabulated/bv2170_pp2q4q_plurality_RCV-IRV_tabulated.txt

--- Choose-One / Plurality Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Avery,Blake,Casey
   47 ×     1,    0,    0
   47 ×     0,    1,    0
    6 ×     0,    0,    1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Avery         -- 47 -- First place
   Blake         -- 47 -- Second place
   Casey         --  6
 Avery and Blake advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Avery         -- 47 -- Tied for first place
   Blake         -- 47 -- Tied for first place
   Equal Support --  6
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Avery         -- 47 -- Tied for first place
   Blake         -- 47 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Avery         -- 0 -- Tied for first place
   Blake         -- 0 -- Tied for first place
 There's still a two-way tie for first.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Casey', 'Blake', 'Avery']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Avery', 'Blake']
  Resolved: ['Blake'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Blake
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Avery    |  * Blake    |    Casey    |
-------------------------------------------------------------
       * Avery > |     ---      |47 -  6 - 47 |47 - 47 -  6 |
       * Blake > | 47 -  6 - 47 |    ---      |47 - 47 -  6 |
         Casey > |  6 - 47 - 47 | 6 - 47 - 47 |    ---      |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Avery, Blake (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Avery       0   0   0   0  47  53  |    47   0.5
Blake       0   0   0   0  47  53  |    47   0.5
Casey       0   0   0   0   6  94  |     6   0.1
```

</details>

Everything in one file: the [`_tabulated` mirror](../symmetric_centrist_bv2170_tabulated/bv2170_pp2q4q_plurality_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/symmetric_centrist_bv2170/bv2170_pp2q4q_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2170_pp2q4q_irv](bv2170_pp2q4q_irv.md) · [bv2170_pp2q4q_ranked_robin](bv2170_pp2q4q_ranked_robin.md) · [bv2170_pp2q4q_star](bv2170_pp2q4q_star.md)
