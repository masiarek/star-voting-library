# Exercise 12 — Two seats, one neighborhood: Allocated Score shares

*Generated from [`ex12_proportional_share.yaml`](../ex12_proportional_share.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Asa, Cleo

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/89wwvr) · **[results ↗](https://bettervoting.com/89wwvr/results)** (election `89wwvr`).

## Scenario

The same ten ballots as ex12_bloc_sweep.yaml, tabulated as Allocated
Score (STAR-PR). Round 1 elects the highest scorer, Asa (30) — and then
ALLOCATES a quota's worth (10 voters / 2 seats = 5 ballots) of Asa's
strongest supporters, spending most of the north side's voting weight.
Round 2 runs on what remains: the north's leftover fraction gives Bram
almost nothing, while the south side's four untouched ballots give Cleo
20 — Cleo takes seat 2. Board: Asa (north) + Cleo (south), one seat per
faction, matching their 60/40 weight. Same ballots as the Bloc STAR
sweep, opposite philosophy: proportional methods spend a faction's
weight as it wins seats so the rest of the room is heard. Exercise:
ex12_bloc_vs_proportional.md. Ballots and cast are this repo's own.
Live on BetterVoting (Test ID BV2199): https://bettervoting.com/89wwvr/results
— BV's STAR_PR race agrees: Asa + Cleo. (Its results page banners the
race "Tied!" — a systemic quirk of BV's STAR_PR serializer, which
echoes the elected pair as "tied" with no round detail on every
STAR_PR election, e.g. the older jwxr3j; the underlying scores here
are a clean 30, then 20/16/4.)

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
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 10 ballots to fill 2 seats.
Count × Asa,Bram,Cleo,Dane
    6 ×   5,   4,   0,   0
    4 ×   0,   0,   5,   4

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Asa           -- 30 -- First place
   Bram          -- 24
   Cleo          -- 20
   Dane          -- 16
 Asa wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 5 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 6 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 83.33% of these ballots.
 Keeping these ballots, but multiplying their weights by 1/6.
 6 ballots reweighted from 1 to 1/6.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Cleo          -- 20 -- First place
   Dane          -- 16
   Bram          --  4
 Cleo wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Asa
 Cleo
```

### Full audit — preference matrix, Condorcet, and score distribution

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
 Hare quota is 5.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex12_proportional_share_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex12_proportional_share.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex09_game_night_cycle](ex09_game_night_cycle.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md)
