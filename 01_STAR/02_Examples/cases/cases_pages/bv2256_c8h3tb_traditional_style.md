---
search:
  exclude: true
---

# Traditional voting style — one mark each (BV2256, c8h3tb)

*Generated from [`bv2256_c8h3tb_traditional_style.yaml`](../bv2256_c8h3tb_traditional_style.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../01_Learn) · **1 seat** · **Expected winner:** Ella

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/c8h3tb) · **[results ↗](https://bettervoting.com/c8h3tb/results)** (election `c8h3tb` · test `BV2256`).

## Scenario

The "traditional" voting style, done to the hilt. Three voters, five candidates,
and every voter fills out the 5-star ballot the old familiar way: one 5 for a
favorite, the other four rows blank (a blank counts as 0). One marks Carmen, two
mark Ella.

Said plainly: as an approach and as a strategy this is a POOR use of a STAR
ballot — unless one candidate really is your only acceptable choice, period, in
which case it is exactly honest and you should vote it. Otherwise you spend 5 of
the 25 points the ballot offers, say nothing about the rest of the field, and if
your one pick misses the runoff your ballot has no voice in the final head-to-head.
Nothing is penalized: a bullet vote is legal, full-weight and impossible to spoil,
and a backup score can never hurt your favorite. You are simply choosing not to
use the ballot.

Watch what it costs the count. STAR's scoring round becomes nothing but a
first-choice tally — Ella 10, Carmen 5, and Andre, Blake and David on 0 with
nothing ever said about them — and the automatic runoff has nothing left to add
(Ella 2 - Carmen 1, nobody at Equal Support). A ballot carrying one bit per voter
gives the method one bit to read, so this count could not have done better than
the choose-one ballot it is imitating.

Live results (BV2256): https://bettervoting.com/c8h3tb/results
Lesson: 01_STAR/01_Learn/voting_styles/traditional.md

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

<!-- --8<-- [start:report] -->
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
<!-- --8<-- [end:report] -->

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

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2256_c8h3tb_traditional_style_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/02_Examples/cases/bv2256_c8h3tb_traditional_style.yaml
```

## See also

- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [03d_c5_b5_style-gallery-five-more](03d_c5_b5_style-gallery-five-more.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2182_tg4779_faq_runoff_reversal](bv2182_tg4779_faq_runoff_reversal.md) · [bv2184_fyy886_lunch_vote](bv2184_fyy886_lunch_vote.md) · [bv2187_qrw6wb_ann-bob-cal](bv2187_qrw6wb_ann-bob-cal.md) · [bv2263_xw23m9_over_50_percent](bv2263_xw23m9_over_50_percent.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
