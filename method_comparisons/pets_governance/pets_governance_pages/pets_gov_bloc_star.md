# Pets Governance — Council by Bloc STAR (3 seats): majority sweeps

*Generated from [`pets_gov_bloc_star.yaml`](../pets_gov_bloc_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **3 seats** · **Expected winners:** Dog, Fish, Cat

## Scenario

One of six races in the Pets Governance election (BV2134, bvid kcf8vf; BV-confirmed). 22 voters split into a
13-voter MAJORITY ("Furries": Dog, Cat, Fish) and a 9-voter MINORITY ("Others":
Bird, Rabbit, Hamster). This race fills a 3-seat Council by Bloc STAR — a
MAJORITARIAN method. The majority's top three sweep every seat: Dog, Fish, Cat.
The minority gets nothing. Contrast with the STAR-PR and STV races on the same
ballots, where the minority earns a seat (proportional).

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
--- Bloc STAR Voting Method (3 winners) ---

[Bloc STAR]
 Tabulating 22 ballots to fill 3 seats.
Count × Dog,Cat,Fish,Bird,Rabbit,Hamster
   13 ×   5,  4,   4,   1,     0,      0
    9 ×   0,  0,   1,   5,     4,      4

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dog           -- 65 -- First place
   Fish          -- 61 -- Second place
   Bird          -- 58
   Cat           -- 52
   Hamster       -- 36
   Rabbit        -- 36
 Dog and Fish advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dog           -- 13 -- First place
   Fish          --  9
   Equal Support --  0
 Dog wins.
   Runoff math:
     22  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     22  voters with a preference  (majority = 12)
           Dog 13 (59%)  ·  Fish 9 (41%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Fish          -- 61 -- First place
   Bird          -- 58 -- Second place
   Cat           -- 52
   Hamster       -- 36
   Rabbit        -- 36
 Fish and Bird advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Fish          -- 13 -- First place
   Bird          --  9
   Equal Support --  0
 Fish wins.
   Runoff math:
     22  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     22  voters with a preference  (majority = 12)
           Fish 13 (59%)  ·  Bird 9 (41%)

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bird          -- 58 -- First place
   Cat           -- 52 -- Second place
   Hamster       -- 36
   Rabbit        -- 36
 Bird and Cat advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cat           -- 13 -- First place
   Bird          --  9
   Equal Support --  0
 Cat wins.
   Runoff math:
     22  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     22  voters with a preference  (majority = 12)
           Cat 13 (59%)  ·  Bird 9 (41%)

[Bloc STAR: Winners — Bloc STAR Voting Method (3 winners)]
 Dog
 Fish
 Cat
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
```

</details>

Everything in one file: the [`_tabulated` mirror](../pets_governance_tabulated/pets_gov_bloc_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/pets_governance/pets_gov_bloc_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [pets_gov_approval](pets_gov_approval.md) · [pets_gov_bloc_plurality](pets_gov_bloc_plurality.md) · [pets_gov_ranked_robin](pets_gov_ranked_robin.md) · [pets_gov_star_pr](pets_gov_star_pr.md) · [pets_gov_stv](pets_gov_stv.md)
