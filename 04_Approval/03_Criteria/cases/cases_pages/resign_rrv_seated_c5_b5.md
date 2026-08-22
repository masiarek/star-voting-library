---
search:
  exclude: true
---

# Resignation monotonicity — the three seats RRV fills

*Generated from [`resign_rrv_seated_c5_b5.yaml`](../resign_rrv_seated_c5_b5.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Reweighted Range Voting (proportional STAR)](../../../../03_STAR_PR/01_Learn/README.md) · **3 seats** · **Expected winners:** Fern, Gus, Hana

## Scenario

Five voters, three seats, under Reweighted Range Voting — the other
proportional score rule in this engine.

Fern and Gus each have exactly one supporter and nothing else. Hana, Ivan and
Juno share three overlapping supporters, one of whom (the fifth voter) also
backs Fern.

RRV elects Fern, Gus and Hana — unique under every tie-breaking order.

BEFORE half of a matched pair; Hana then resigns in
`resign_rrv_after_hana_c4_b5.yaml`.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Fern,Gus,Hana,Ivan,Juno
5,0,0,0,0     # Fern only
0,5,0,0,0     # Gus only
0,0,5,5,0     # Hana + Ivan
0,0,5,0,5     # Hana + Juno
5,0,5,5,5     # Fern + the whole Hana/Ivan/Juno slate
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Hana
  Choose-One (Plurality) = Fern   (differs from STAR)

--- Reweighted Range Voting Method (3 winners) ---

[Reweighted Range Voting]
 Tabulating 5 ballots to fill 3 seats.
Fern,Gus,Hana,Ivan,Juno
   5,  0,   0,   0,   0
   0,  5,   0,   0,   0
   0,  0,   5,   5,   0
   0,  0,   5,   0,   5
   5,  0,   5,   5,   5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Hana          -- 15 -- First place
   Fern          -- 10
   Ivan          -- 10
   Juno          -- 10
   Gus           --  5
 Hana wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 3 ballots reweighted from 1 to 1/2.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Fern          -- 7+1/2 -- First place
   Gus           -- 5
   Ivan          -- 5
   Juno          -- 5
 Fern wins a seat.

[Reweighted Range Voting: Round 2: Reweighing Ballots]
 Reweighted 2 ballots:
   1 ballot reweighted from 1 to 1/2.
   1 ballot reweighted from 1/2 to 1/3.

[Reweighted Range Voting: Round 3: Score round]
 The highest-scoring candidate wins a seat.
   Gus           -- 5     -- First place
   Ivan          -- 4+1/6
   Juno          -- 4+1/6
 Gus wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (3 winners)]
 Fern
 Gus
 Hana
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Preference Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        Informational only — not part of the 3-winner count below,
        so no Top-2 finalists are marked.
               |     Fern   |    Gus    |    Hana   |    Ivan   |    Juno   |
-----------------------------------------------------------------------------
        Fern > |    ---     |2 - 2 - 1  |1 - 2 - 2  |1 - 3 - 1  |1 - 3 - 1  |
         Gus > | 1 - 2 - 2  |   ---     |1 - 1 - 3  |1 - 2 - 2  |1 - 2 - 2  |
        Hana > | 2 - 2 - 1  |3 - 1 - 1  |   ---     |1 - 4 - 0  |1 - 4 - 0  |
        Ivan > | 1 - 3 - 1  |2 - 2 - 1  |0 - 4 - 1  |   ---     |1 - 3 - 1  |
        Juno > | 1 - 3 - 1  |2 - 2 - 1  |0 - 4 - 1  |1 - 3 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Hana — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Gus — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Fern       2  0  0  0  0  3  |    10   2.0
Gus        1  0  0  0  0  4  |     5   1.0
Hana       3  0  0  0  0  2  |    15   3.0
Ivan       2  0  0  0  0  3  |    10   2.0
Juno       2  0  0  0  0  3  |    10   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/resign_rrv_seated_c5_b5_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 04_Approval/03_Criteria/cases/resign_rrv_seated_c5_b5.yaml
```

## See also

- [Monotonicity (topic hub)](../../../../07_Concepts/topics/monotonicity/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [abc_committee_monotonicity_1seat_c3_b10](abc_committee_monotonicity_1seat_c3_b10.md) · [abc_committee_monotonicity_2seats_c3_b10](abc_committee_monotonicity_2seats_c3_b10.md) · [cc_pareto_dominated_c4_b2](cc_pareto_dominated_c4_b2.md) · [monroe_pareto_dominated_c4_b24](monroe_pareto_dominated_c4_b24.md) · [resign_av_holds_after_kai_c6_b5](resign_av_holds_after_kai_c6_b5.md) · [resign_av_holds_c7_b5](resign_av_holds_c7_b5.md) · [resign_rrv_after_hana_c4_b5](resign_rrv_after_hana_c4_b5.md) · [resign_star_pr_after_bruno_c3_b5](resign_star_pr_after_bruno_c3_b5.md) · [resign_star_pr_seated_c4_b5](resign_star_pr_seated_c4_b5.md) · [sav_strategy_bullet_vote_c5_b2](sav_strategy_bullet_vote_c5_b2.md)
