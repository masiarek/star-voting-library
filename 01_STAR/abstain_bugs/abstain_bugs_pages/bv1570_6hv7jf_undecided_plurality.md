# BV1570 — undecided plurality election still declares a winner

*Generated from [`bv1570_6hv7jf_undecided_plurality.yaml`](../bv1570_6hv7jf_undecided_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Approve

## Scenario

A Plurality ("choose one") race, two options, three voters, all "undecided":
one ballot deselects Approve (a `0`, then blank), one is fully blank, one
deselects Reject. Markers: `&` = the BetterVoting `null` (left blank).

**BetterVoting** counts all three as abstentions (nTallyVotes = 0), reports the
wrong voter count (the results view showed 2, not 3), and still declares a winner
(Approve) off zero tallied votes (bettervoting#894).

**LH diverges:** only the fully-blank ballot abstains. The two ballots that carry
an explicit `0` are real tally votes (both options score 0), so LH sees
nTallyVotes = 2, nAbstentions = 1, a 0-0 tie, resolved to Approve by lot. Same
winner, different count — LH counts an explicit 0 as a cast vote, per the #884
dispute.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Approve,Reject
0,&
&,&
&,0
```

## What the engine says

Full report from the [`_tabulated` mirror](../abstain_bugs_tabulated/bv1570_6hv7jf_undecided_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                |  * Approve  | * Reject   |
--------------------------------------------
    * Approve > |     ---     | 0 - 3 - 0  |
     * Reject > |  0 - 3 - 0  |    ---     |

[Condorcet Winner]
  No strict Condorcet winner; unbeaten candidates: Approve, Reject (pairwise ties)

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 3 ballots. Note: 1 of 3 ballots is marked as an abstention.
Approve,Reject
      0,     &
      &,     &
      &,     0

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total   Avg
Approve    0  0  0  0  0  1    2  |     0   0.0
Reject     0  0  0  0  0  1    2  |     0   0.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Approve       -- 0 -- First place
   Reject        -- 0 -- Second place
 Approve and Reject advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Approve       -- 0 -- Tied for first place
   Reject        -- 0 -- Tied for first place
   Equal Support -- 3
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Approve       -- 0 -- Tied for first place
   Reject        -- 0 -- Tied for first place
 There's still a two-way tie for first.

[STAR Voting: Automatic Runoff Round: Second tiebreaker]
 The candidate with the most votes of score 5 wins.
   Approve       -- 0 -- Tied for first place
   Reject        -- 0 -- Tied for first place
 There's still a two-way tie for first.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Approve', 'Reject']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Approve', 'Reject']
  Resolved: ['Approve'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Approve
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/abstain_bugs/bv1570_6hv7jf_undecided_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv11_6xhfp8_full_equal_support](bv11_6xhfp8_full_equal_support.md) · [bv655_jfrk9t_equal_opposition](bv655_jfrk9t_equal_opposition.md)
