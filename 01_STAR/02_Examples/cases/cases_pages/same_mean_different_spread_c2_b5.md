---
search:
  exclude: true
---

# Same mean, different spread — the consensus candidate and the polarizing one

*Generated from [`same_mean_different_spread_c2_b5.yaml`](../same_mean_different_spread_c2_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Blake

## Scenario

Two candidates, five voters, and an exact tie in the Scoring Round: Alice 15,
Blake 15, both averaging 3.0. Every difference between them is SPREAD. Alice
is a flat 3 on all five ballots; Blake is three 5s and two 0s. The Score
Distribution block is the whole lesson — same mean, variance 0.0 vs 6.0 —
and 6.0 is the LARGEST variance arithmetically possible at a mean of 3.0 on
a 0-5 scale, so Blake is exactly as divisive as this ballot allows.
Because the totals tie, pure Score cannot separate them at all; the
divergence block's Approval reading (approve = 3+ stars) picks Alice 5-3;
STAR's Automatic Runoff hands the seat to Blake 3-2. "Polarizing" is not a
mood — it is variance, and only the second round reads it.

## Ballots

The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| # | Ballot as marked | Alice | Blake |
|:--:|:--|:--:|:--:|
| 1 | <img src="../img/same_mean_different_spread_c2_b5_ballot_1.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Blake is my champion; Alice is fine: Alice 3, Blake 5."> | 3 | 5 |
| 2 | <img src="../img/same_mean_different_spread_c2_b5_ballot_2.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Blake is my champion; Alice is fine: Alice 3, Blake 5."> | 3 | 5 |
| 3 | <img src="../img/same_mean_different_spread_c2_b5_ballot_3.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Blake is my champion; Alice is fine: Alice 3, Blake 5."> | 3 | 5 |
| 4 | <img src="../img/same_mean_different_spread_c2_b5_ballot_4.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Alice is fine; Blake, absolutely not: Alice 3, Blake 0."> | 3 | 0 |
| 5 | <img src="../img/same_mean_different_spread_c2_b5_ballot_5.png" width="330" style="min-width:330px" alt="A 0–5 STAR ballot — Alice is fine; Blake, absolutely not: Alice 3, Blake 0."> | 3 | 0 |

The same ballots as the file records them:

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice,Blake
3,5 # Blake is my champion; Alice is fine
3,5 # Blake is my champion; Alice is fine
3,5 # Blake is my champion; Alice is fine
3,0 # Alice is fine; Blake, absolutely not
3,0 # Alice is fine; Blake, absolutely not
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Blake
  Approval = Alice   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Alice,Blake
    3 ×     3,    5
    2 ×     3,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 15 -- First place
   Blake         -- 15 -- Second place
 Alice and Blake advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blake         -- 3 -- First place
   Alice         -- 2
   Equal Support -- 0
 Blake wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Blake 3 (60%)  ·  Alice 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Blake
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Alice   | * Blake   |
-----------------------------------------
     * Alice > |    ---     |2 - 0 - 3  |
     * Blake > | 3 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Blake — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Alice — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Alice      0  0  5  0  0  0  |    15   3.0
Blake      3  0  0  0  0  2  |    15   3.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/same_mean_different_spread_c2_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/02_Examples/cases/same_mean_different_spread_c2_b5.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/same_mean_different_spread_c2_b5.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [03d_c5_b5_style-gallery-five-more](03d_c5_b5_style-gallery-five-more.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2182_tg4779_faq_runoff_reversal](bv2182_tg4779_faq_runoff_reversal.md) · [bv2184_fyy886_lunch_vote](bv2184_fyy886_lunch_vote.md) · [bv2187_qrw6wb_ann-bob-cal](bv2187_qrw6wb_ann-bob-cal.md) · [bv2256_c8h3tb_traditional_style](bv2256_c8h3tb_traditional_style.md) · [bv2263_xw23m9_over_50_percent](bv2263_xw23m9_over_50_percent.md) · [csv_ambiguity_ex1_c4_b8](csv_ambiguity_ex1_c4_b8.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
