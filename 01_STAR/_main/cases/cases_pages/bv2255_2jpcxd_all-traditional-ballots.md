# Everyone voted "traditional" — one mark each, and every method agrees (BV2255, 2jpcxd)

*Generated from [`bv2255_2jpcxd_all-traditional-ballots.yaml`](../bv2255_2jpcxd_all-traditional-ballots.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ella

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/2jpcxd) · **[results ↗](https://bettervoting.com/2jpcxd/results)** (election `2jpcxd`).

## Scenario

The "traditional" voting style, all the way down. Three voters, five candidates,
and every single voter fills out the 5-star ballot the old familiar way: one 5
for a favorite, four blanks. One voter marks Carmen; two mark Ella. Nothing is
ever said about Andre, Blake or David.

On BetterVoting the SAME three single marks were written on all three ballot
formats and counted four ways — Choose-One (Plurality), STAR, RCV-IRV and Ranked
Robin. All four elect Ella, and that agreement is the lesson: when every ballot
carries one bit, every method has the same one bit to read, so no method can do
better than choose-one. STAR's automatic runoff still runs (Ella 2 - Carmen 1,
nobody Equal Support) but it has nothing left to add — the finalists were already
the only two candidates anyone said anything about.

Nothing here is penalized. A bullet vote is legal, full-weight and impossible to
spoil. It just hands back the expressiveness the ballot was offering: each voter
spent 5 of the 25 points on the sheet, and the three candidates nobody scored
finish jointly winless. Compare the companion case where voters DO use the range:
method_comparisons/minority_winner (same idea, opposite outcome — a rich ballot
makes the methods disagree, and the fuller counts find the majority's choice).

Live results (BV2255): https://bettervoting.com/2jpcxd/results
Lesson: 00_start_here/STAR_Voting/voting_styles/traditional.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Andre,Blake,Carmen,David,Ella
    0,    0,     5,    0,   0   # traditional: "Carmen. Period."
    0,    0,     0,    0,   5   # traditional: "Ella. Period."
    0,    0,     0,    0,   5   # traditional: "Ella. Period."
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Count × Andre,Blake,Carmen,David,Ella
    2 ×     0,    0,     0,    0,   5
    1 ×     0,    0,     5,    0,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ella          -- 10 -- First place
   Carmen        --  5 -- Second place
   Andre         --  0
   Blake         --  0
   David         --  0
 Ella and Carmen advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ella          -- 2 -- First place
   Carmen        -- 1
   Equal Support -- 0
 Ella wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           Ella 2 (67%)  ·  Carmen 1 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ella
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    Andre   |   Blake   | * Carmen  |   David   |  * Ella   |
-----------------------------------------------------------------------------
       Andre > |    ---     |0 - 3 - 0  |0 - 2 - 1  |0 - 3 - 0  |0 - 1 - 2  |
       Blake > | 0 - 3 - 0  |   ---     |0 - 2 - 1  |0 - 3 - 0  |0 - 1 - 2  |
    * Carmen > | 1 - 2 - 0  |1 - 2 - 0  |   ---     |1 - 2 - 0  |1 - 0 - 2  |
       David > | 0 - 3 - 0  |0 - 3 - 0  |0 - 2 - 1  |   ---     |0 - 1 - 2  |
      * Ella > | 2 - 1 - 0  |2 - 1 - 0  |2 - 0 - 1  |2 - 1 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ella — matches the STAR winner

[Condorcet Loser]
  No strict Condorcet loser; jointly weak Condorcet losers: Andre, Blake, David (winless — pairwise ties)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Andre      0  0  0  0  0  3  |     0   0.0
Blake      0  0  0  0  0  3  |     0   0.0
Carmen     1  0  0  0  0  2  |     5   1.7
David      0  0  0  0  0  3  |     0   0.0
Ella       2  0  0  0  0  1  |    10   3.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2255_2jpcxd_all-traditional-ballots_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/cases/bv2255_2jpcxd_all-traditional-ballots.yaml
```

## See also

- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../00_start_here/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2182_tg4779_faq_runoff_reversal](bv2182_tg4779_faq_runoff_reversal.md) · [bv2184_fyy886_lunch_vote](bv2184_fyy886_lunch_vote.md) · [bv2187_qrw6wb_ann-bob-cal](bv2187_qrw6wb_ann-bob-cal.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
