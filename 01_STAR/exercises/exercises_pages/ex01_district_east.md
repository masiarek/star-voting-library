# Exercise 1 — Two districts, one mayor: EAST district

*Generated from [`ex01_district_east.yaml`](../ex01_district_east.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Avery

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/rhbfj7) · **[results ↗](https://bettervoting.com/rhbfj7/results)** (election `rhbfj7`).

## Scenario

East District's nine ballots, tallied on their own — a mirror of West with
Blake and Diego trading places. Scoring round: Avery 35, Diego 33, Carmen 32,
Elena 25, Blake 0 — Avery and Diego advance. Eight of the nine ballots score
the two finalists identically (Equal Support), and the one decided voter
prefers Avery. East's winner: Avery.
Part 2 of 3 of the consistency exercise (ex01_two_districts.md): West also
elects Avery, yet the combined city elects Carmen. Ballots adapted from a
RangeVoting.org example, posed as an exercise in Brendan W. Sullivan,
"An Introduction to the Math of Voting Methods" (2022), ch. 5.
Live on BetterVoting (Test ID BV2189): https://bettervoting.com/rhbfj7/results
— the election carries a second, Ranked Robin race on the same opinions
(equal ranks allowed): Elena, the district's Condorcet winner, wins it 4-0.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Avery,Blake,Carmen,Diego,Elena
3,0,4,3,5 # 5 East voters: Elena first, Carmen second, Avery = Diego
3,0,4,3,5
3,0,4,3,5
3,0,4,3,5
3,0,4,3,5
5,0,3,5,0 # 3 East voters: Avery = Diego at the top, Carmen third
5,0,3,5,0
5,0,3,5,0
5,0,3,3,0 # 1 East voter: Avery OVER Diego — the only decided runoff vote
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Avery
  Choose-One (Plurality) = Elena   (differs from STAR)
  RCV-IRV                = Elena   (differs from STAR)
  RCV-RR (Condorcet)     = Elena   (differs from STAR)
  Note: 9 of 9 ballots (100%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: exercises_tabulated/ex01_district_east_RCV-IRV_tabulated.txt
  RCV-RR round-robin: exercises_tabulated/ex01_district_east_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Avery,Blake,Carmen,Diego,Elena
    5 ×     3,    0,     4,    3,    5
    3 ×     5,    0,     3,    5,    0
    1 ×     5,    0,     3,    3,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Avery         -- 35 -- First place
   Diego         -- 33 -- Second place
   Carmen        -- 32
   Elena         -- 25
   Blake         --  0
 Avery and Diego advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Avery         -- 1 -- First place
   Diego         -- 0
   Equal Support -- 8
 Avery wins.
   Runoff math:
     9  ballots cast
   − 8  Equal Support (no preference between the two finalists)
     ─
     1  voters with a preference  (majority = 1)
           Avery 1 (100%)  ·  Diego 0 (0%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Avery
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Avery   |   Blake   |   Carmen  | * Diego   |   Elena   |
-----------------------------------------------------------------------------
     * Avery > |    ---     |9 - 0 - 0  |4 - 0 - 5  |1 - 8 - 0  |4 - 0 - 5  |
       Blake > | 0 - 0 - 9  |   ---     |0 - 0 - 9  |0 - 0 - 9  |0 - 4 - 5  |
      Carmen > | 5 - 0 - 4  |9 - 0 - 0  |   ---     |5 - 1 - 3  |4 - 0 - 5  |
     * Diego > | 0 - 8 - 1  |9 - 0 - 0  |3 - 1 - 5  |   ---     |4 - 0 - 5  |
       Elena > | 5 - 0 - 4  |5 - 4 - 0  |5 - 0 - 4  |5 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Elena — STAR elected Avery instead (Elena was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Avery      4  0  5  0  0  0  |    35   3.9
Blake      0  0  0  0  0  9  |     0   0.0
Carmen     0  5  4  0  0  0  |    32   3.6
Diego      3  0  6  0  0  0  |    33   3.7
Elena      5  0  0  0  0  4  |    25   2.8
```

</details>

Everything in one file: the [`_tabulated` mirror](../exercises_tabulated/ex01_district_east_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/ex01_district_east.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/ex01_district_east.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
