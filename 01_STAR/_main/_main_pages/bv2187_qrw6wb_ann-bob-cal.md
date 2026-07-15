# Ann, Bob, Cal - the canonical leading example (single-winner STAR)

*Generated from [`bv2187_qrw6wb_ann-bob-cal.yaml`](../bv2187_qrw6wb_ann-bob-cal.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bob

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qrw6wb) · **[results ↗](https://bettervoting.com/qrw6wb/results)** (election `qrw6wb`).

## Scenario

THE repo's leading example - the exact election shown in the root README, the
YAML authoring template, and "Why YAML test cases". One file, three voters,
three candidates: the smallest STAR election where both rounds do visible,
different work. If a page needs "a STAR election" and nothing scenario-specific,
it should show THIS one (see 00_start_here/tips/TIPS_canonical_elections.md).

Live results: https://bettervoting.com/qrw6wb/results (BetterVoting election
qrw6wb, Test ID BV2187; write-ins disabled - the candidate list is locked).

What each ballot teaches:
- Voter 1 (5,4,0): likes BOTH Ann (5) and Bob (4) - no vote-splitting fear.
  In the runoff her ballot is one full vote for Ann (5 > 4): a near-tie in
  scores is still a whole vote in the runoff.
- Voter 2 (3,5,2): a Bob fan who honestly scores the others too.
- Voter 3 (0,3,5): loves Cal, rates Bob a lukewarm 3 - and that honest 3 is
  exactly what makes Bob everyone's acceptable choice.

The count: Scoring Round totals Bob 12, Ann 8, Cal 7 -> finalists Bob & Ann.
Automatic Runoff: Bob is preferred on 2 ballots, Ann on 1 -> Bob wins 2-1.
Bob leads the scores AND wins the runoff - deliberately no twist, so the
PROCEDURE is the whole lesson. (Bob is also the Condorcet winner.)

CANONICAL = FROZEN: never edit these ballots. A lesson needing different
ballots gets a new scenario with a new cast of names.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ann,Bob,Cal
5,4,0
3,5,2
0,3,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Bob
  Choose-One (Plurality) = Ann   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Ann,Bob,Cal
  5,  4,  0
  3,  5,  2
  0,  3,  5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bob           -- 12 -- First place
   Ann           --  8 -- Second place
   Cal           --  7
 Bob and Ann advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bob           -- 2 -- First place
   Ann           -- 1
   Equal Support -- 0
 Bob wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Bob 2 (67%)  ·  Ann 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bob
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ann    |  * Bob    |    Cal    |
-----------------------------------------------------
       * Ann > |    ---     |1 - 0 - 2  |2 - 0 - 1  |
       * Bob > | 2 - 0 - 1  |   ---     |2 - 0 - 1  |
         Cal > | 1 - 0 - 2  |1 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bob — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ann        1  0  1  0  0  1  |     8   2.7
Bob        1  1  1  0  0  0  |    12   4.0
Cal        1  0  0  1  0  1  |     7   2.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/bv2187_qrw6wb_ann-bob-cal_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/bv2187_qrw6wb_ann-bob-cal.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2182_tg4779_faq_runoff_reversal](bv2182_tg4779_faq_runoff_reversal.md) · [bv2184_fyy886_lunch_vote](bv2184_fyy886_lunch_vote.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
