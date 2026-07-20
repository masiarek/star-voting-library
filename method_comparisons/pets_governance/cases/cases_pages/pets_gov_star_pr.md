# Pets Governance — Council by STAR-PR (3 seats): minority earns a seat

*Generated from [`pets_gov_star_pr.yaml`](../pets_gov_star_pr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Allocated Score (proportional STAR)](../../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Bird, Dog, Fish

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kcf8vf) · **[results ↗](https://bettervoting.com/kcf8vf/results)** (election `kcf8vf`).

## Scenario

One of six races in the Pets Governance election (BV2134, bvid kcf8vf; BV-confirmed). Same 22 voters, same
scores as the Bloc STAR race — a 13-voter MAJORITY (Dog, Cat, Fish) and a 9-voter
MINORITY (Bird, Rabbit, Hamster). This race fills the 3-seat Council by STAR-PR
(Allocated Score) — a PROPORTIONAL method. After the majority elects its first
seat its ballots are down-weighted, so the minority's Bird wins a seat: the
result is Bird, Dog, Fish — 2 majority + 1 minority. Same ballots as Bloc STAR
(which swept all three for the majority): proportional vs majoritarian, side by
side.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Dog,Cat,Fish,Bird,Rabbit,Hamster
13: 5,4,4,1,0,0
9: 0,0,1,5,4,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Allocated Score Voting Method (3 winners) ---

[Allocated Score Voting]
 Tabulating 22 ballots to fill 3 seats.
Count × Dog,Cat,Fish,Bird,Rabbit,Hamster
   13 ×   5,  4,   4,   1,     0,      0
    9 ×   0,  0,   1,   5,     4,      4

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Dog           -- 65 -- First place
   Fish          -- 61
   Bird          -- 58
   Cat           -- 52
   Hamster       -- 36
   Rabbit        -- 36
 Dog wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 7+1/3 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 13 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 56.41% of these ballots.
 Keeping these ballots, but multiplying their weights by 17/39.
 13 ballots reweighted from 1 to 17/39.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Bird          -- 50+2/3 -- First place
   Hamster       -- 36
   Rabbit        -- 36
   Fish          -- 31+2/3
   Cat           -- 22+2/3
 Bird wins a seat.

[Allocated Score Voting: Round 2: Ballot allocation round]
 Allocating 7+1/3 ballots.

[Allocated Score Voting: Round 2: Ballot allocation round: Round 1]
 Allocating 9 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 81.48% of these ballots.
 Keeping these ballots, but multiplying their weights by 5/27.
 9 ballots reweighted from 1 to 5/27.

[Allocated Score Voting: Round 3]
 The highest-scoring candidate wins a seat.
   Fish          -- 24+1/3 -- First place
   Cat           -- 22+2/3
   Hamster       --  6+2/3
   Rabbit        --  6+2/3
 Fish wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (3 winners)]
 Bird
 Dog
 Fish
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Dog     |     Cat     |   * Fish    |     Bird    |    Rabbit   |   Hamster   |
-------------------------------------------------------------------------------------------------------
         * Dog > |     ---      |13 -  9 -  0 |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |
           Cat > |  0 -  9 - 13 |    ---      | 0 - 13 -  9 |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |
        * Fish > |  9 -  0 - 13 | 9 - 13 -  0 |    ---      |13 -  0 -  9 |13 -  0 -  9 |13 -  0 -  9 |
          Bird > |  9 -  0 - 13 | 9 -  0 - 13 | 9 -  0 - 13 |    ---      |22 -  0 -  0 |22 -  0 -  0 |
        Rabbit > |  9 -  0 - 13 | 9 -  0 - 13 | 9 -  0 - 13 | 0 -  0 - 22 |    ---      | 0 - 22 -  0 |
       Hamster > |  9 -  0 - 13 | 9 -  0 - 13 | 9 -  0 - 13 | 0 -  0 - 22 | 0 - 22 -  0 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Dog — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Dog        13   0   0   0   0   9  |    65   3.0
Cat         0  13   0   0   0   9  |    52   2.4
Fish        0  13   0   0   9   0  |    61   2.8
Bird        9   0   0   0  13   0  |    58   2.6
Rabbit      0   9   0   0   0  13  |    36   1.6
Hamster     0   9   0   0   0  13  |    36   1.6
 Hare quota is 22/3.
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/pets_gov_star_pr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/cases/pets_gov_star_pr.yaml
```

## See also

- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_approval](pets_gov_approval.md) · [pets_gov_bloc_plurality](pets_gov_bloc_plurality.md) · [pets_gov_bloc_star](pets_gov_bloc_star.md) · [pets_gov_ranked_robin](pets_gov_ranked_robin.md) · [pets_gov_stv](pets_gov_stv.md)
