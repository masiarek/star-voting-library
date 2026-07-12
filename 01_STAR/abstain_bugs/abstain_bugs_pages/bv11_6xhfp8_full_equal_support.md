# BV11 — full & equal support (5,5) counted as abstentions

*Generated from [`bv11_6xhfp8_full_equal_support.yaml`](../bv11_6xhfp8_full_equal_support.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ann

## Scenario

Two candidates, three voters, every ballot **5,5** — full and equal support. This
is a valid STAR ballot (it contributes 5 to both in the scoring round).

**BetterVoting** treats each all-equal ballot as an abstention (policy
bettervoting#884): it reports nTallyVotes = 0, nAbstentions = 3, and the submit
dialog warns "Abstained / No preference" on a full-support ballot (the bug in
bettervoting#1053) — yet it still declares a winner (Ann) off zero tallied votes.

**LH diverges:** it counts all three as real votes (Ann 15, Bob 15), so it's a
genuine tie, resolved to Ann by lot (CSV column order). Same winner, opposite
reasoning: BetterVoting says "everyone abstained," LH says "everyone tied." LH's
treatment matches the view that full, equal support is a cast vote, not an
abstention — the #884 dispute.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Bob
5,5
5,5
5,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Count × Ann,Bob
    3 ×   5,  5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ann           -- 15 -- First place
   Bob           -- 15 -- Second place
 Ann and Bob advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ann           -- 0 -- Tied for first place
   Bob           -- 0 -- Tied for first place
   Equal Support -- 3
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Ann           -- 15 -- Tied for first place
   Bob           -- 15 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Ann           -- 3 -- Tied for first place
   Bob           -- 3 -- Tied for first place
 There's still a two-way tie for first.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Ann', 'Bob']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Ann', 'Bob']
  Resolved: ['Ann'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ann
```

<details>
<summary>▸ Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |  * Bob    |
-----------------------------------------
       * Ann > |    ---     |0 - 3 - 0  |
       * Bob > | 0 - 3 - 0  |   ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Ann, Bob (pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ann        3  0  0  0  0  0  |    15   5.0
Bob        3  0  0  0  0  0  |    15   5.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../abstain_bugs_tabulated/bv11_6xhfp8_full_equal_support_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/abstain_bugs/bv11_6xhfp8_full_equal_support.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv1570_6hv7jf_undecided_plurality](bv1570_6hv7jf_undecided_plurality.md) · [bv655_jfrk9t_equal_opposition](bv655_jfrk9t_equal_opposition.md)
