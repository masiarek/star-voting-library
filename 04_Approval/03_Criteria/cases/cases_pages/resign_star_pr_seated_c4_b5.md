---
search:
  exclude: true
---

# Resignation monotonicity — the board STAR-PR actually elects

*Generated from [`resign_star_pr_seated_c4_b5.yaml`](../resign_star_pr_seated_c4_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Ana, Bruno

## Scenario

A two-seat board. Four of the five voters are one bloc: every one of them backs
Bruno, and they split evenly on a second name — two also back Cleo, two also
back Dev. The fifth voter backs Ana and nobody else.

Allocated Score (the STAR-PR rule BetterVoting runs) does what proportional
representation is supposed to do: the four-voter bloc gets one of the two seats
(Bruno), and the lone voter gets the other (Ana). One seat each, no ties
anywhere in the count.

This is the BEFORE half of a matched pair. Bruno then resigns, and the count is
re-run on the remaining three names in
`resign_star_pr_after_bruno_c3_b5.yaml` — where Ana loses her seat too.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Bruno,Cleo,Dev
5,0,0,0     # the lone voter — Ana only
0,5,5,0     # bloc voter, Cleo wing
0,5,5,0     # bloc voter, Cleo wing
0,5,0,5     # bloc voter, Dev wing
0,5,0,5     # bloc voter, Dev wing
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 5 ballots to fill 2 seats.
Count × Ana,Bruno,Cleo,Dev
    2 ×   0,    5,   5,  0
    2 ×   0,    5,   0,  5
    1 ×   5,    0,   0,  0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Bruno         -- 20 -- First place
   Cleo          -- 10
   Dev           -- 10
   Ana           --  5
 Bruno wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 2+1/2 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 4 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 62.50% of these ballots.
 Keeping these ballots, but multiplying their weights by 3/8.
 4 ballots reweighted from 1 to 3/8.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Ana           -- 5     -- First place
   Cleo          -- 3+3/4
   Dev           -- 3+3/4
 Ana wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Ana
 Bruno
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 2-winner count below,
        so no Top-2 finalists are marked.
               |     Ana    |   Bruno   |    Cleo   |    Dev    |
-----------------------------------------------------------------
         Ana > |    ---     |1 - 0 - 4  |1 - 2 - 2  |1 - 2 - 2  |
       Bruno > | 4 - 0 - 1  |   ---     |2 - 3 - 0  |2 - 3 - 0  |
        Cleo > | 2 - 2 - 1  |0 - 3 - 2  |   ---     |2 - 1 - 2  |
         Dev > | 2 - 2 - 1  |0 - 3 - 2  |2 - 1 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Bruno — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ana — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        1  0  0  0  0  4  |     5   1.0
Bruno      4  0  0  0  0  1  |    20   4.0
Cleo       2  0  0  0  0  3  |    10   2.0
Dev        2  0  0  0  0  3  |    10   2.0
 Hare quota is 5/2.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/resign_star_pr_seated_c4_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/resign_star_pr_seated_c4_b5.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [resign_av_holds_after_kai_c6_b5](resign_av_holds_after_kai_c6_b5.md) · [resign_av_holds_c7_b5](resign_av_holds_c7_b5.md) · [resign_rrv_after_hana_c4_b5](resign_rrv_after_hana_c4_b5.md) · [resign_rrv_seated_c5_b5](resign_rrv_seated_c5_b5.md) · [resign_star_pr_after_bruno_c3_b5](resign_star_pr_after_bruno_c3_b5.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
