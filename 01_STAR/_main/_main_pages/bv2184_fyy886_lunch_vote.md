# BV2184 — The team lunch vote

*Generated from [`bv2184_fyy886_lunch_vote.yaml`](../bv2184_fyy886_lunch_vote.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Pizza

## Scenario

The beginner's running example (STAR — start here). Five coworkers pick lunch
from Sushi, Tacos, or Pizza. Two love Sushi, two love Tacos — and everyone is
perfectly happy with Pizza. Under Choose-One each person names ONE favorite,
so the vote splits (Sushi 2, Tacos 2, Pizza 1) and Pizza — the option nobody
objected to — comes LAST; a coin flip hands lunch to Sushi or Tacos and half
the team is stuck with something they rated 0. STAR reads the whole ballot:
Pizza tops the Scoring Round (17) and wins the runoff 3-2. The compromise
everyone can live with wins, and no one had to vote strategically. (Choose-One
and RCV-IRV both elect Sushi here; STAR elects Pizza.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Sushi,Tacos,Pizza
5,0,3
5,0,3
0,5,3
0,5,3
3,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Pizza
  Choose-One (Plurality) = Sushi   (differs from STAR)
  RCV-IRV                = Sushi   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/bv2184_fyy886_lunch_vote_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Sushi,Tacos,Pizza
    2 ×     5,    0,    3
    2 ×     0,    5,    3
    1 ×     3,    1,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Pizza         -- 17 -- First place
   Sushi         -- 13 -- Second place
   Tacos         -- 11
 Pizza and Sushi advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Pizza         -- 3 -- First place
   Sushi         -- 2
   Equal Support -- 0
 Pizza wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Pizza 3 (60%)  ·  Sushi 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Pizza
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Sushi   |   Tacos   | * Pizza   |
-----------------------------------------------------
     * Sushi > |    ---     |3 - 0 - 2  |2 - 0 - 3  |
       Tacos > | 2 - 0 - 3  |   ---     |2 - 0 - 3  |
     * Pizza > | 3 - 0 - 2  |3 - 0 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Pizza — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Sushi      2  0  1  0  0  2  |    13   2.6
Tacos      2  0  0  0  1  2  |    11   2.2
Pizza      1  0  4  0  0  0  |    17   3.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/bv2184_fyy886_lunch_vote_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/bv2184_fyy886_lunch_vote.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2184_fyy886_lunch_vote.md) — its entry in the divergence review ledger
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2182_tg4779_faq_runoff_reversal](bv2182_tg4779_faq_runoff_reversal.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
