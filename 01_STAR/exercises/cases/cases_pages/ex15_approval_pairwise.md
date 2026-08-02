---
search:
  exclude: true
---

# Exercise 15a, second look — the same Yes/No ballots read pairwise

*Generated from [`ex15_approval_pairwise.yaml`](../ex15_approval_pairwise.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../concepts) · **1 seat** · **Expected winner:** Blair

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/d4v2dh) · **[results ↗](https://bettervoting.com/d4v2dh/results)** (election `d4v2dh`).

## Scenario

The SAME 35 ballots as ex15_approval_yes_no.yaml, with each approval written
as a 5 and each non-approval as a 0, so the engine prints the pairwise matrix
and names the Condorcet winner. The magnitudes carry no information here —
every head-to-head count depends only on the two-class order (approved above
not-approved), which is what makes this a DICHOTOMOUS PROFILE.

The payoff: the head-to-head order reproduces the approval order exactly.
Blair beats Cosmo 13-7 (15 voters approved both, so they express no
preference) and beats Ada 20-7; Cosmo beats Ada 15-8. Blair > Cosmo > Ada,
the same ranking as the approval totals 28 > 22 > 15.

That is guaranteed, not luck. On a dichotomous profile "more voters strictly
prefer x to y" reduces to "more voters approve x than y", so a Condorcet
winner always exists and approval voting agrees with every Condorcet method.
The caveat lives one folder over: real approval ballots are compressed from
richer opinions, and the Condorcet winner of the uncompressed opinions can be
someone else — see method_comparisons/black_curtain/condorcet_compression.md.

Exercise page: ../ex15_read_the_ballot.md
Live results: https://bettervoting.com/d4v2dh/results (BV2258, race 2 of 2 —
the same 35 ballots as race 1, cast as 5/0 scores; BV's STAR count agrees:
Blair. The frozen export sits beside the sibling yaml,
ex15_approval_yes_no_bv_export.json — one export covers both races.)

## Parameters (from the YAML)

```yaml
voting_method: STAR
num_winners: 1
expected_winners: [Blair]
bv_election_id: d4v2dh
bv_test_id: BV2258
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Blair,Cosmo
15:0,5,5
8:5,5,0
7:5,0,5
5:0,5,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 35 ballots.
Count × Ada,Blair,Cosmo
   15 ×   0,    5,    5
    8 ×   5,    5,    0
    7 ×   5,    0,    5
    5 ×   0,    5,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Blair         -- 140 -- First place
   Cosmo         -- 110 -- Second place
   Ada           --  75
 Blair and Cosmo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Blair         -- 13 -- First place
   Cosmo         --  7
   Equal Support -- 15
 Blair wins.
   Runoff math:
     35  ballots cast
   − 15  Equal Support (no preference between the two finalists)
     ──
     20  voters with a preference  (majority = 11)
           Blair 13 (65%)  ·  Cosmo 7 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Blair
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Ada     |  * Blair    |  * Cosmo    |
-------------------------------------------------------------
           Ada > |     ---      | 7 -  8 - 20 | 8 - 12 - 15 |
       * Blair > | 20 -  8 -  7 |    ---      |13 - 15 -  7 |
       * Cosmo > | 15 - 12 -  8 | 7 - 15 - 13 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Blair — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ada — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ada        15   0   0   0   0  20  |    75   2.1
Blair      28   0   0   0   0   7  |   140   4.0
Cosmo      22   0   0   0   0  13  |   110   3.1
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex15_approval_pairwise_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex15_approval_pairwise.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [The Black Curtain (worked set)](../../../../method_comparisons/black_curtain/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md) · [ex15_approval_yes_no](ex15_approval_yes_no.md) · [ex15_score_profile](ex15_score_profile.md)
