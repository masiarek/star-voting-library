---
search:
  exclude: true
---

# BV2263 — Over 50%: single-winner STAR, a candidate with every point on every ballot

*Generated from [`bv2263_xw23m9_over_50_percent.yaml`](../bv2263_xw23m9_over_50_percent.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../01_Learn) · **1 seat** · **Expected winner:** A

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/xw23m9) · **[results ↗](https://bettervoting.com/xw23m9/results)** (election `xw23m9` · test `BV2263`).

## Scenario

The ceiling case, and the control for reading every other STAR result: what a
landslide looks like when it is as large as a landslide can get.

Three voters, three candidates. A is scored 5 by all three; one voter gives B
a single point; nobody scores C at all.
  - Scoring round: A = 15 of a possible 15 (100% of the maximum, average 5.0),
    B = 1, C = 0. A and B advance.
  - Automatic runoff: all three ballots prefer A. A 3, B 0, Equal Support 0.
A wins on every denominator there is — 100% of the maximum score, 100% of the
ballots, 100% of the voters with a preference between the finalists.

Two things this case is here to show, both easier to see at the ceiling than
in a close race:
  1. STAR does not stop early. Even a unanimous max-score candidate is put
     through the automatic runoff; there is no "wins outright in round 1"
     shortcut the way a majority of first choices ends an RCV-IRV count in
     its first round. The scoring round chooses finalists, never the winner.
  2. "Over 50%" is three different questions. Score share, ballot share and
     decided-voter share coincide here and only here; they come apart as soon
     as a ballot rates the two finalists equally.

The multi-seat twin is BV1815 (02_STAR_Bloc), whose three ballots hand A 12 of
15 and still buy exactly one seat: the second goes to C on 2 points, after a
runoff nobody wins. Read the pair together — 02_STAR_Bloc/01_Learn/over_50_percent.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C
5,0,0
5,1,0
5,0,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 3 ballots.
Count × A,B,C
    2 × 5,0,0
    1 × 5,1,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 15 -- First place
   B             --  1 -- Second place
   C             --  0
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 3 -- First place
   B             -- 0
   Equal Support -- 0
 A wins.
   Runoff math:
     3  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     3  voters with a preference  (majority = 2)
           A 3 (100%)  ·  B 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |    * A     |   * B     |     C     |
-----------------------------------------------------
         * A > |    ---     |3 - 0 - 0  |3 - 0 - 0  |
         * B > | 0 - 0 - 3  |   ---     |1 - 2 - 0  |
           C > | 0 - 0 - 3  |0 - 2 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: C — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
A          3  0  0  0  0  0  |    15   5.0
B          0  0  0  0  1  2  |     1   0.3
C          0  0  0  0  0  3  |     0   0.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2263_xw23m9_over_50_percent_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/02_Examples/cases/bv2263_xw23m9_over_50_percent.yaml
```

## See also

- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [03d_c5_b5_style-gallery-five-more](03d_c5_b5_style-gallery-five-more.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2182_tg4779_faq_runoff_reversal](bv2182_tg4779_faq_runoff_reversal.md) · [bv2184_fyy886_lunch_vote](bv2184_fyy886_lunch_vote.md) · [bv2187_qrw6wb_ann-bob-cal](bv2187_qrw6wb_ann-bob-cal.md) · [bv2256_c8h3tb_traditional_style](bv2256_c8h3tb_traditional_style.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
