---
search:
  exclude: true
---

# The eight ambiguous CSV lines, disambiguated (BV issue #778 ex1)

*Generated from [`csv_ambiguity_ex1_c4_b8.yaml`](../csv_ambiguity_ex1_c4_b8.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../01_Learn/README.md) · **1 seat** · **Expected winner:** B

**Official tie-break (lot) order:** A > B > C > D — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The eight-line CSV posted in BetterVoting issue #778 ("YAML File standard"),
rewritten in this library's schema so every line states what it means.
The bare CSV could not say whether a zero was a real low score, a blank, a
deliberate abstention, or a spoiled ballot — and it never said which method
to count it by. Here the method, the seat count, the candidate names and the
intent behind every zero are all in the one file, and the engine can run it.
Note line 7: four real zeros, cast on purpose. The engine reports 2 of 8
ballots as abstentions - the race abstention and the spoiled ballot - and
leaves the all-zero ballot in the count, where it belongs.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
A,B,C,D
0,1,0,0   # line 1 - four real scores, nothing ambiguous
~,~,~,~   # line 2 - race abstention: skipped the whole race
0,1,0,&   # line 3 - candidate-level abstention on D
0,0,1,1   # line 4 - four real scores
?,?,?,?   # line 5 - spoiled ballot
0,1,0,-   # line 6 - D left blank
0,0,0,0   # line 7 - all zeros ON PURPOSE - this is NOT an abstention
0,-,0,-   # line 8 - B and D left blank
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = B
  Approval = A   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 8 ballots. Note: 2 of 8 ballots are marked as abstentions.
A,B,C,D
0,1,0,0
~,~,~,~
0,1,0,&
0,0,1,1
?,?,?,?
0,1,0,-
0,0,0,0
0,-,0,-
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 3 -- First place
   C             -- 1 -- Tied for second place
   D             -- 1 -- Tied for second place
   A             -- 0
 B advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   C             -- 0 -- Tied for second place
   D             -- 0 -- Tied for second place
   Equal Support -- 8
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   C             -- 0 -- Tied for second place
   D             -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['A', 'B', 'C', 'D']

[Tiebreaker: Lot Number Priority]
  Tie among: ['C', 'D']
  Resolved: ['C'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 3 -- First place
   C             -- 1
   Equal Support -- 4
 B wins.
   Runoff math:
     8  ballots cast
   − 4  Equal Support (no preference between the two finalists)
     ─
     4  voters with a preference  (majority = 3)
           B 3 (75%)  ·  C 1 (25%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 B
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
        Note: C and D tied at 1 in the Scoring Round, and the lot rung (the
              ballots could not separate them) advanced C. The * marks who
              advanced, not who scored highest.

               |      A     |   * B     |   * C     |     D     |
-----------------------------------------------------------------
           A > |    ---     |0 - 5 - 3  |0 - 7 - 1  |0 - 7 - 1  |
         * B > | 3 - 5 - 0  |   ---     |3 - 4 - 1  |3 - 4 - 1  |
         * C > | 1 - 7 - 0  |1 - 4 - 3  |   ---     |0 - 8 - 0  |
           D > | 1 - 7 - 0  |1 - 4 - 3  |0 - 8 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: B — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: A — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total   Avg
A          0  0  0  0  0  6    2  |     0   0.0
B          0  0  0  0  3  2    3  |     3   0.6
C          0  0  0  0  1  5    2  |     1   0.2
D          0  0  0  0  1  2    5  |     1   0.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/csv_ambiguity_ex1_c4_b8_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/02_Examples/cases/csv_ambiguity_ex1_c4_b8.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/csv_ambiguity_ex1_c4_b8.md) — its entry in the divergence review ledger
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [02a_c3_b1_three-candidates](02a_c3_b1_three-candidates.md) · [02b_c3_b2_three-candidates](02b_c3_b2_three-candidates.md) · [03a_c3_b3_style-bullet-vote](03a_c3_b3_style-bullet-vote.md) · [03b_c3_b3_1_style-protest-vote](03b_c3_b3_1_style-protest-vote.md) · [03b_c3_b3_2_expand_style-protest-vote](03b_c3_b3_2_expand_style-protest-vote.md) · [03c_c6_b8_style-gallery](03c_c6_b8_style-gallery.md) · [03d_c5_b5_style-gallery-five-more](03d_c5_b5_style-gallery-five-more.md) · [04b_c4_b3_display-options-all](04b_c4_b3_display-options-all.md) · [05a_c5_b3_unanimous-ballots](05a_c5_b3_unanimous-ballots.md) · [06a_c9_b3_large-field-equal-support](06a_c9_b3_large-field-equal-support.md) · [06b_c9_runoff-overturns-leader](06b_c9_runoff-overturns-leader.md) · [09_c4_b100_tennessee-capital](09_c4_b100_tennessee-capital.md) · [abstentions](abstentions.md) · [bv2182_tg4779_faq_runoff_reversal](bv2182_tg4779_faq_runoff_reversal.md) · [bv2184_fyy886_lunch_vote](bv2184_fyy886_lunch_vote.md) · [bv2187_qrw6wb_ann-bob-cal](bv2187_qrw6wb_ann-bob-cal.md) · [bv2256_c8h3tb_traditional_style](bv2256_c8h3tb_traditional_style.md) · [bv2263_xw23m9_over_50_percent](bv2263_xw23m9_over_50_percent.md) · [display_options_demo](display_options_demo.md) · [equal_support_runoff_demo](equal_support_runoff_demo.md) · [quorum_demo_c3_b6](quorum_demo_c3_b6.md) · [quorum_fail_demo_c3_b6](quorum_fail_demo_c3_b6.md) · [star_ala_approval](star_ala_approval.md) · [three_winners_cw_score_runoff](three_winners_cw_score_runoff.md) · [vote_splitting](vote_splitting.md) · [vote_splitting2](vote_splitting2.md) · [vote_splitting3](vote_splitting3.md) · [vote_splitting_scenario1_spoiler](vote_splitting_scenario1_spoiler.md) · [vote_splitting_scenario2_bloc_leads](vote_splitting_scenario2_bloc_leads.md) · [vote_splitting_scenario3_outsider_wins](vote_splitting_scenario3_outsider_wins.md)
