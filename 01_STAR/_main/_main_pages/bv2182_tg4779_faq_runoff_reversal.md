# BV2182 — why the automatic runoff (and Equal Support)

*Generated from [`bv2182_tg4779_faq_runoff_reversal.yaml`](../bv2182_tg4779_faq_runoff_reversal.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Almond

## Scenario

A 10-voter STAR election built for the FAQ. Berry is the consensus candidate —
broadly liked, so Berry wins the Scoring Round on total stars. But more voters
strictly prefer Almond head-to-head, so Almond wins the Automatic Runoff: a
clean Runoff Reversal that shows why the second step exists. One voter scores
both finalists 5 (Equal Support) — counted, but expressing no preference between
the two, so it lands in neither finalist's runoff column.
Live results: https://bettervoting.com/tg4779/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Almond,Berry,Cocoa
5,4,1
5,4,1
5,4,1
5,4,1
5,4,0
5,4,0
0,5,2
0,5,2
0,5,2
5,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Almond
  Approval = Berry   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Berry)
 - Runoff Round Winner   = (Almond)
  Candidate Berry earned the highest total score, but
  Candidate Almond won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 10 ballots.
Count × Almond,Berry,Cocoa
    4 ×      5,    4,    1
    3 ×      0,    5,    2
    2 ×      5,    4,    0
    1 ×      5,    5,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Berry         -- 44 -- First place
   Almond        -- 35 -- Second place
   Cocoa         -- 10
 Berry and Almond advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Almond        -- 6 -- First place
   Berry         -- 3
   Equal Support -- 1
 Almond wins.
   Runoff math:
     10  ballots cast
   −  1  Equal Support (no preference between the two finalists)
     ──
      9  voters with a preference  (majority = 5)
           Almond 6 (67%)  ·  Berry 3 (33%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Almond
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Almond   |  * Berry    |    Cocoa    |
-------------------------------------------------------------
      * Almond > |     ---      | 6 -  1 -  3 | 7 -  0 -  3 |
       * Berry > |  3 -  1 -  6 |    ---      |10 -  0 -  0 |
         Cocoa > |  3 -  0 -  7 | 0 -  0 - 10 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Almond — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Almond     7  0  0  0  0  3  |    35   3.5
Berry      4  6  0  0  0  0  |    44   4.4
Cocoa      0  0  0  3  4  3  |    10   1.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../_main_tabulated/bv2182_tg4779_faq_runoff_reversal_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/_main/bv2182_tg4779_faq_runoff_reversal.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/bv2182_tg4779_faq_runoff_reversal.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [01_c3_b3_ann-bob-cal](01_c3_b3_ann-bob-cal.md) · [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2184_fyy886_lunch_vote](bv2184_fyy886_lunch_vote.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
