# P3 sincere — STAR elects Dublin (ranks converted 5/4/3/2/0)

*Generated from [`p3_sincere_star.yaml`](../p3_sincere_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/concepts) · **1 seat** · **Expected winner:** Dublin

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/4w96tr) · **[results ↗](https://bettervoting.com/4w96tr/results)** (election `4w96tr`).

## Scenario

The same seven sincere voters under STAR, with each ranking converted to scores on a 5/4/3/2/0 spacing (five candidates will not fit 0-5 evenly, so some spacing must be chosen; this outcome is robust — 5/4/3/1/0 and 5/3/2/1/0 also elect Dublin). Scoring round: Dublin 23, Edinburgh 22, Cork 20, Bergen 17, Athens 16. Finalists Dublin and Edinburgh; the runoff goes to Dublin 5-2, because Dublin beats Edinburgh head-to-head. So STAR and plurality agree on Dublin here while Copeland/Ranked Robin and Borda both say Edinburgh. The manipulated counterpart is p3_manip_star.yaml — STAR is manipulable on this profile too.

## Parameters (from the YAML)

```yaml
voting_method: STAR
num_winners: 1
expected_winners:
- Dublin
bv_election_id: 4w96tr
bv_test_id: BV2253
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Athens,Bergen,Cork,Dublin,Edinburgh
2:3,0,4,2,5
3:0,3,2,5,4
2:5,4,3,2,0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Dublin
  Approval = Bergen   (differs from STAR)
  RCV-RR   = Edinburgh   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/p3_sincere_star_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 7 ballots.
Count × Athens,Bergen,Cork,Dublin,Edinburgh
    3 ×      0,     3,   2,     5,        4
    2 ×      3,     0,   4,     2,        5
    2 ×      5,     4,   3,     2,        0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dublin        -- 23 -- First place
   Edinburgh     -- 22 -- Second place
   Cork          -- 20
   Bergen        -- 17
   Athens        -- 16
 Dublin and Edinburgh advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Dublin        -- 5 -- First place
   Edinburgh     -- 2
   Equal Support -- 0
 Dublin wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Dublin 5 (71%)  ·  Edinburgh 2 (29%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Dublin
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |     Athens    |    Bergen    |     Cork     |  * Dublin    | * Edinburgh  |
-----------------------------------------------------------------------------------------------
         Athens > |      ---      |  4 - 0 - 3   |  2 - 0 - 5   |  4 - 0 - 3   |  2 - 0 - 5   |
         Bergen > |   3 - 0 - 4   |     ---      |  5 - 0 - 2   |  2 - 0 - 5   |  2 - 0 - 5   |
           Cork > |   5 - 0 - 2   |  2 - 0 - 5   |     ---      |  4 - 0 - 3   |  2 - 0 - 5   |
       * Dublin > |   3 - 0 - 4   |  5 - 0 - 2   |  3 - 0 - 4   |     ---      |  5 - 0 - 2   |
    * Edinburgh > |   5 - 0 - 2   |  5 - 0 - 2   |  5 - 0 - 2   |  2 - 0 - 5   |     ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Athens > Bergen > Cork > Athens)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Athens     2  0  2  0  0  3  |    16   2.3
Bergen     0  2  3  0  0  2  |    17   2.4
Cork       0  2  2  3  0  0  |    20   2.9
Dublin     3  0  0  4  0  0  |    23   3.3
Edinburgh  2  3  0  0  0  2  |    22   3.1
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/p3_sincere_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/manipulability_p3/cases/p3_sincere_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/p3_sincere_star.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [p3_manip_compromise_rr](p3_manip_compromise_rr.md) · [p3_manip_reversal_rr](p3_manip_reversal_rr.md) · [p3_manip_star](p3_manip_star.md) · [p3_sincere_ranked_robin](p3_sincere_ranked_robin.md)
