# Same matrix, different plurality — electorate P3: Ranked Robin

*Generated from [`same_matrix_p3_ranked_robin.yaml`](../same_matrix_p3_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ben

## Scenario

One of three 12-ballot electorates (P3) that produce the *identical* pairwise
table: Ben beats Ada 7-5, Ada ties Cal 6-6, Ben beats Cal 7-5. Every method that
reads only the pairwise matrix — Ranked Robin, Minimax, Ranked Pairs, Kemeny — and
Borda too, must return the same answer on all three. Ben, here. The companion
Plurality file on this same electorate returns Cal, and the three electorates
give three different plurality winners. That is what it means for plurality to sit
outside the pairwise matrix (Fishburn C3).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
3:Ada>Ben>Cal
3:Cal>Ben>Ada
3:Ben>Ada>Cal
1:Ben>Cal>Ada
2:Cal>Ada>Ben
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/same_matrix_p3_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 12 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cal
     3 × Cal > Ben > Ada
     3 × Ben > Ada > Cal
     1 × Ben > Cal > Ada
     2 × Cal > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ben  beats Ada   7 – 5
   Ada  ties  Cal   6 – 6
   Ben  beats Cal   7 – 5

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
        |    Ada    |   Ben    |   Cal    |
-------------------------------------------
  Ada > |    ---    |5 - 0 - 7 |6 - 0 - 6 |
  Ben > | 7 - 0 - 5 |   ---    |7 - 0 - 5 |
  Cal > | 6 - 0 - 6 |5 - 0 - 7 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ben        2–0–0         2      +4  Ada, Cal
    2  Ada        0–1–1       0.5      -2  —
    3  Cal        0–1–1       0.5      -2  —

Winner — Ranked Robin (RCV-RR): Ben
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/same_matrix_different_plurality/cases/same_matrix_p3_ranked_robin.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [same_matrix_p1_plurality](same_matrix_p1_plurality.md) · [same_matrix_p1_ranked_robin](same_matrix_p1_ranked_robin.md) · [same_matrix_p2_plurality](same_matrix_p2_plurality.md) · [same_matrix_p2_ranked_robin](same_matrix_p2_ranked_robin.md) · [same_matrix_p3_plurality](same_matrix_p3_plurality.md)
