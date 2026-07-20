# Food-Truck Row — STAR-PR / Allocated Score: one seat per side

*Generated from [`bv2210_fvg8y8_star_pr_share.yaml`](../bv2210_fvg8y8_star_pr_share.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** Arepa, Donut

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/fvg8y8) · **[results ↗](https://bettervoting.com/fvg8y8/results)** (election `fvg8y8`).

## Scenario

One 100-voter electorate, two food-truck spots, five counts — this file is the STAR-PR / Allocated Score count (score ballots, quota-allocated seats). The savory side is a 57-voter OUTRIGHT MAJORITY split across three trucks (Arepa 20 first choices, Bao 19, Churro 18); the sweet side is a disciplined 43-voter minority on two (Donut 22, Eclair 21). Same opinions on every ballot; only the counting rule changes: SNTV hands the majority ZERO seats (Donut+Eclair), Bloc STAR and Bloc Ranked Robin hand it BOTH (Arepa+Bao), STAR-PR and STV share them one per side (Arepa+Donut). THE HEADLINE HERE: the proportional count. Arepa wins the first seat; the quota of voters who elected him is spent; the remaining weight is majority-sweet, and Donut takes the second seat. 57/43 room, 1/1 seats. NOTE a BV display quirk on this race: BetterVoting banners the elected pair as 'Tied!' with tieBreakType random and no tie anywhere — the same STAR_PR serializer quirk first seen on 89wwvr (ex12) and jwxr3j; this election is the third confirming instance. The seats themselves are correct and agree with LH. Full lesson: README.md in this folder. Live on BetterVoting (Test ID BV2210): https://bettervoting.com/fvg8y8 — all five races agree with the LH engine, no genuine tie anywhere. Live results: https://bettervoting.com/fvg8y8/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Arepa,Bao,Churro,Donut,Eclair
20: 5,4,3,0,0
19: 4,5,3,0,0
18: 4,3,5,0,0
22: 0,0,0,5,4
21: 0,0,0,4,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Arepa
  Choose-One (Plurality) = Donut   (differs from STAR)

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 100 ballots to fill 2 seats.
Count × Arepa,Bao,Churro,Donut,Eclair
   22 ×     0,  0,     0,    5,     4
   21 ×     0,  0,     0,    4,     5
   20 ×     5,  4,     3,    0,     0
   19 ×     4,  5,     3,    0,     0
   18 ×     4,  3,     5,    0,     0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Arepa         -- 248 -- First place
   Bao           -- 229
   Churro        -- 207
   Donut         -- 194
   Eclair        -- 193
 Arepa wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 50 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 20 ballots at score 5.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 2]
 Remaining allocation quota is 30.
 Allocating 37 ballots at score 4.
 This allocation overfills the remaining quota.  Returning fractional surplus.
 Allocating only 81.08% of these ballots.
 Keeping these ballots, but multiplying their weights by 7/37.
 37 ballots reweighted from 1 to 7/37.

[Allocated Score Voting: Round 2]
 Tabulating 80 remaining ballots.
Count × Arepa,Bao,Churro,Donut,Eclair
   22 ×     0,  0,     0,    5,     4
   21 ×     0,  0,     0,    4,     5
   20 ×     5,  4,     3,    0,     0
   19 ×     4,  5,     3,    0,     0
   18 ×     4,  3,     5,    0,     0

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Arepa
 Donut
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Arepa    |   * Bao     |    Churro   |    Donut    |    Eclair   |
-----------------------------------------------------------------------------------------
       * Arepa > |     ---      |38 - 43 - 19 |39 - 43 - 18 |57 -  0 - 43 |57 -  0 - 43 |
         * Bao > | 19 - 43 - 38 |    ---      |39 - 43 - 18 |57 -  0 - 43 |57 -  0 - 43 |
        Churro > | 18 - 43 - 39 |18 - 43 - 39 |    ---      |57 -  0 - 43 |57 -  0 - 43 |
         Donut > | 43 -  0 - 57 |43 -  0 - 57 |43 -  0 - 57 |    ---      |22 - 57 - 21 |
        Eclair > | 43 -  0 - 57 |43 -  0 - 57 |43 -  0 - 57 |21 - 57 - 22 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Arepa — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Arepa      20  37   0   0   0  43  |   248   2.5
Bao        19  20  18   0   0  43  |   229   2.3
Churro     18   0  39   0   0  43  |   207   2.1
Donut      22  21   0   0   0  57  |   194   1.9
Eclair     21  22   0   0   0  57  |   193   1.9
 Hare quota is 50.

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Arepa      20  37   0   0   0  43  |   248   2.5
Bao        19  20  18   0   0  43  |   229   2.3
Churro     18   0  39   0   0  43  |   207   2.1
Donut      22  21   0   0   0  57  |   194   1.9
Eclair     21  22   0   0   0  57  |   193   1.9
 The highest-scoring candidate wins a seat.
   Donut         -- 194       -- First place
   Eclair        -- 193
   Bao           --  28+ 7/37
   Churro        --  27+30/37
 Donut wins a seat.
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2210_fvg8y8_star_pr_share_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/food_truck_row/cases/bv2210_fvg8y8_star_pr_share.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2210_fvg8y8_bloc_rr_sweep](bv2210_fvg8y8_bloc_rr_sweep.md) · [bv2210_fvg8y8_bloc_star_sweep](bv2210_fvg8y8_bloc_star_sweep.md) · [bv2210_fvg8y8_sntv_split](bv2210_fvg8y8_sntv_split.md) · [bv2210_fvg8y8_stv_share](bv2210_fvg8y8_stv_share.md)
