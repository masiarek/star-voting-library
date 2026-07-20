# Exercise 12 — Two seats, one neighborhood: Bloc STAR sweeps

*Generated from [`ex12_bloc_sweep.yaml`](../ex12_bloc_sweep.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Asa, Bram

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/89wwvr) · **[results ↗](https://bettervoting.com/89wwvr/results)** (election `89wwvr`).

## Scenario

A neighborhood association elects a two-seat board. The north side (6 of
10 voters) runs Asa and Bram; the south side (4 of 10) runs Cleo and
Dane. Bloc STAR fills seats by running single-winner STAR once per seat:
seat 1 goes to Asa (30 points; runoff 6-0 over Bram with 4 Equal
Support), then Asa is removed and seat 2 goes to Bram (runoff 6-4 over
Cleo). The cohesive 60% takes 100% of the board — majoritarian by
design, the right tool when the body must act as one and the wrong one
when it should mirror the neighborhood. The companion file
ex12_proportional_share.yaml reruns the same ten ballots under Allocated
Score (STAR-PR): the south side's 40% earns one of the two seats.
Exercise: ex12_bloc_vs_proportional.md. Ballots and cast are this
repo's own.
Live on BetterVoting (Test ID BV2199): https://bettervoting.com/89wwvr/results
— one election, both races (Bloc STAR + STAR-PR); BV agrees on both
seat pairs.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Asa,Bram,Cleo,Dane
5,4,0,0 # 6 north-side voters: Asa first, Bram close behind
5,4,0,0
5,4,0,0
5,4,0,0
5,4,0,0
5,4,0,0
0,0,5,4 # 4 south-side voters: Cleo first, Dane close behind
0,0,5,4
0,0,5,4
0,0,5,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 10 ballots to fill 2 seats.
Count × Asa,Bram,Cleo,Dane
    6 ×   5,   4,   0,   0
    4 ×   0,   0,   5,   4

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Asa           -- 30 -- First place
   Bram          -- 24 -- Second place
   Cleo          -- 20
   Dane          -- 16
 Asa and Bram advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Asa           -- 6 -- First place
   Bram          -- 0
   Equal Support -- 4
 Asa wins.
   Runoff math:
     10  ballots cast
   −  4  Equal Support (no preference between the two finalists)
     ──
      6  voters with a preference  (majority = 4)
           Asa 6 (100%)  ·  Bram 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bram          -- 24 -- First place
   Cleo          -- 20 -- Second place
   Dane          -- 16
 Bram and Cleo advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bram          -- 6 -- First place
   Cleo          -- 4
   Equal Support -- 0
 Bram wins.
   Runoff math:
     10  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     10  voters with a preference  (majority = 6)
           Bram 6 (60%)  ·  Cleo 4 (40%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Asa
 Bram
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Asa    |  * Bram   |    Cleo   |    Dane   |
-----------------------------------------------------------------
       * Asa > |    ---     |6 - 4 - 0  |6 - 0 - 4  |6 - 0 - 4  |
      * Bram > | 0 - 4 - 6  |   ---     |6 - 0 - 4  |6 - 0 - 4  |
        Cleo > | 4 - 0 - 6  |4 - 0 - 6  |   ---     |4 - 6 - 0  |
        Dane > | 4 - 0 - 6  |4 - 0 - 6  |0 - 6 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Asa — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Asa        6  0  0  0  0  4  |    30   3.0
Bram       0  6  0  0  0  4  |    24   2.4
Cleo       4  0  0  0  0  6  |    20   2.0
Dane       0  4  0  0  0  6  |    16   1.6
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex12_bloc_sweep_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex12_bloc_sweep.yaml
```

## See also

- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
