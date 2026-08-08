---
search:
  exclude: true
---

# Nine candidates, 25 voters — the 0–5 score ballot

*Generated from [`ballot_expressiveness_c9_star.yaml`](../ballot_expressiveness_c9_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Finn

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/37yf8x) · **[results ↗](https://bettervoting.com/37yf8x/results)** (election `37yf8x` · test `BV2280`).

**Official tie-break (lot) order:** Ada > Ben > Cleo > Dev > Emma > Finn > Gus > Hugo > Iris — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

THE COARSE BALLOT GETS IT RIGHT. Finn beats all eight rivals head-to-head, and STAR
elects them from a ballot that cannot even rank the field.

Nine candidates will not fit on six rungs — 0, 1, 2, 3, 4 and 5 hold six distinct
places, so every voter here must give at least two candidates the same score. They
actually tie far more than that minimum: about 16% of all candidate pairs go equal on
this paper, against a pigeonhole floor of 8%. Most of the flattening is rounding, not
the hard limit.

And it does not matter. The preference that decides this election — Finn over everyone
— survives the rounding, so STAR returns the Condorcet winner anyway.

Read this file against ballot_expressiveness_c9_rr_top5.yaml, where the same 25 voters
fill in a RANKED ballot capped at five names, the cap New York City and Maine actually
use, and the count elects Gus instead. The ballot usually called "more expressive"
loses the answer that these six rungs kept.

Construction: build_cases.py in this folder. 25 voters and 9 candidates at frozen
positions on one spectrum — Ada −0.73 · Ben −0.37 · Cleo −0.18 · Dev −0.17 ·
Emma −0.11 · Finn +0.24 · Gus +0.41 · Hugo +0.80 · Iris +0.84; utility = minus the
distance; scores = each voter's own min-max scaling onto 0–5; rankings = those same
utilities in order. Nothing is tuned to the result, and **no count in this folder is
settled by a tie-break** — that was a search constraint, so every winner here survives
any lot rule.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cleo,Dev,Emma,Finn,Gus,Hugo,Iris
4,5,4,4,4,2,2,0,0    # voter at -0.43
0,2,2,2,3,4,5,5,5    # voter at +0.60
5,4,4,3,3,2,1,0,0    # voter at -0.67
0,1,2,2,2,3,4,5,5    # voter at +0.89
0,2,3,3,4,5,4,2,1    # voter at +0.18
2,4,5,5,5,3,2,0,0    # voter at -0.13
0,2,2,2,3,4,5,5,5    # voter at +0.59
0,1,2,2,2,4,4,5,5    # voter at +0.72
0,2,3,3,3,5,5,3,3    # voter at +0.34
0,1,2,2,2,4,4,5,5    # voter at +0.69
0,2,3,3,3,5,4,2,2    # voter at +0.23
3,5,5,5,4,3,2,0,0    # voter at -0.30
5,5,4,4,4,2,2,0,0    # voter at -0.51
0,1,2,2,2,3,4,5,5    # voter at +0.89
1,3,5,5,5,4,3,0,0    # voter at -0.05
0,2,2,2,3,4,5,5,5    # voter at +0.60
0,2,3,3,3,5,5,2,2    # voter at +0.28
4,5,4,4,4,2,2,0,0    # voter at -0.40
0,2,2,2,3,4,5,5,5    # voter at +0.62
5,4,4,4,3,2,2,0,0    # voter at -0.63
0,2,3,3,3,5,4,2,2    # voter at +0.27
5,5,4,4,4,2,2,0,0    # voter at -0.61
5,4,3,3,3,2,1,0,0    # voter at -1.33
3,5,5,5,5,3,2,0,0    # voter at -0.23
5,4,3,3,3,2,1,0,0    # voter at -1.82
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Finn
  Choose-One (Plurality) = Ada   (differs from STAR)
  Approval               = Emma   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 25 ballots.
Count × Ada,Ben,Cleo,Dev,Emma,Finn,Gus,Hugo,Iris
    4 ×   0,  2,   2,  2,   3,   4,  5,   5,   5
    2 ×   4,  5,   4,  4,   4,   2,  2,   0,   0
    2 ×   0,  1,   2,  2,   2,   3,  4,   5,   5
    2 ×   0,  1,   2,  2,   2,   4,  4,   5,   5
    2 ×   0,  2,   3,  3,   3,   5,  4,   2,   2
    2 ×   5,  5,   4,  4,   4,   2,  2,   0,   0
    2 ×   5,  4,   3,  3,   3,   2,  1,   0,   0
    1 ×   5,  4,   4,  3,   3,   2,  1,   0,   0
    1 ×   0,  2,   3,  3,   4,   5,  4,   2,   1
    1 ×   2,  4,   5,  5,   5,   3,  2,   0,   0
    1 ×   0,  2,   3,  3,   3,   5,  5,   3,   3
    1 ×   3,  5,   5,  5,   4,   3,  2,   0,   0
    1 ×   1,  3,   5,  5,   5,   4,  3,   0,   0
    1 ×   0,  2,   3,  3,   3,   5,  5,   2,   2
    1 ×   5,  4,   4,  4,   3,   2,  2,   0,   0
    1 ×   3,  5,   5,  5,   5,   3,  2,   0,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Finn          -- 84 -- First place
   Emma          -- 83 -- Second place
   Cleo          -- 81
   Dev           -- 80
   Gus           -- 80
   Ben           -- 75
   Hugo          -- 51
   Iris          -- 50
   Ada           -- 47
 Finn and Emma advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Finn          -- 13 -- First place
   Emma          -- 12
   Equal Support --  0
 Finn wins.
   Runoff math:
     25  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     25  voters with a preference  (majority = 13)
           Finn 13 (52%)  ·  Emma 12 (48%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Finn
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Ada     |     Ben     |     Cleo    |     Dev     |   * Emma    |   * Finn    |     Gus     |     Hugo    |     Iris    |
-------------------------------------------------------------------------------------------------------------------------------------------------
           Ada > |     ---      | 4 -  2 - 19 | 6 -  2 - 17 | 6 -  2 - 17 | 6 -  2 - 17 | 8 -  2 - 15 |10 -  1 - 14 |12 -  0 - 13 |12 -  0 - 13 |
           Ben > | 19 -  2 -  4 |    ---      | 6 -  8 - 11 | 7 -  7 - 11 | 9 -  1 - 15 |11 -  0 - 14 |11 -  1 - 13 |12 -  4 -  9 |13 -  3 -  9 |
          Cleo > | 17 -  2 -  6 |11 -  8 -  6 |    ---      | 1 - 24 -  0 | 3 - 17 -  5 |12 -  0 - 13 |12 -  0 - 13 |16 -  1 -  8 |16 -  1 -  8 |
           Dev > | 17 -  2 -  6 |11 -  7 -  7 | 0 - 24 -  1 |    ---      | 2 - 18 -  5 |12 -  0 - 13 |12 -  0 - 13 |16 -  1 -  8 |16 -  1 -  8 |
        * Emma > | 17 -  2 -  6 |15 -  1 -  9 | 5 - 17 -  3 | 5 - 18 -  2 |    ---      |12 -  0 - 13 |12 -  1 - 12 |16 -  1 -  8 |16 -  1 -  8 |
        * Finn > | 15 -  2 -  8 |14 -  0 - 11 |13 -  0 - 12 |13 -  0 - 12 |13 -  0 - 12 |    ---      |10 -  9 -  6 |17 -  0 -  8 |17 -  0 -  8 |
           Gus > | 14 -  1 - 10 |13 -  1 - 11 |13 -  0 - 12 |13 -  0 - 12 |12 -  1 - 12 | 6 -  9 - 10 |    ---      |17 -  4 -  4 |17 -  4 -  4 |
          Hugo > | 13 -  0 - 12 | 9 -  4 - 12 | 8 -  1 - 16 | 8 -  1 - 16 | 8 -  1 - 16 | 8 -  0 - 17 | 4 -  4 - 17 |    ---      | 1 - 24 -  0 |
          Iris > | 13 -  0 - 12 | 9 -  3 - 13 | 8 -  1 - 16 | 8 -  1 - 16 | 8 -  1 - 16 | 8 -  0 - 17 | 4 -  4 - 17 | 0 - 24 -  1 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Finn — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ada — loses every head-to-head matchup — elected by Choose-One (Plurality)!

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ada         6   2   2   1   1  13  |    47   1.9
Ben         6   5   1   9   4   0  |    75   3.0
Cleo        4   6   7   8   0   0  |    81   3.2
Dev         4   5   8   8   0   0  |    80   3.2
Emma        3   6  12   4   0   0  |    83   3.3
Finn        5   7   5   8   0   0  |    84   3.4
Gus         6   7   1   8   3   0  |    80   3.2
Hugo        8   0   1   4   0  12  |    51   2.0
Iris        8   0   1   3   1  12  |    50   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ballot_expressiveness_c9_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/ballot_expressiveness/cases/ballot_expressiveness_c9_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/ballot_expressiveness_c9_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [ballot_expressiveness_c9_irv_full](ballot_expressiveness_c9_irv_full.md) · [ballot_expressiveness_c9_irv_top5](ballot_expressiveness_c9_irv_top5.md) · [ballot_expressiveness_c9_rr_full](ballot_expressiveness_c9_rr_full.md) · [ballot_expressiveness_c9_rr_top5](ballot_expressiveness_c9_rr_top5.md)
