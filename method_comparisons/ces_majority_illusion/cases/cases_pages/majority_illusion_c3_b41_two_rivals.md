---
search:
  exclude: true
---

# The majority illusion, one score changed — the majority loses Alice

*Generated from [`majority_illusion_c3_b41_two_rivals.yaml`](../majority_illusion_c3_b41_two_rivals.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Brian

## Scenario

The counterfactual companion to majority_illusion_c3_b41_score_vs_star.
Same 41 voters, same cast, ONE number changed: Alice's 21-voter majority
now scores Colin a 3 instead of a 0. Nothing about their opinion of Alice
moved — she is still their 5, still the first choice of an outright
51.2% majority, and still the Condorcet winner.

That single act of generosity to a SECOND rival lifts Colin from 50 to
113 and pushes Alice (105, unchanged) out of the top two. The finalists
become Brian and Colin, Alice is never in the runoff, and Brian wins
31 to 10.

This is the Majority-Criterion failure and the Later-No-Harm failure in
the same move — and it is the exact hinge Equal Vote's Relaxed Majority
Criterion draws the line at. Supporting ONE rival at "max minus 1"
(Brian a 4, the other file) is safe; supporting a SECOND is not. STAR
passes RMC and fails the strict majority criterion, and this pair shows
what the gap between those two facts costs on a real published profile.

These ballots are counterfactual — nobody cast them — so this case is
deliberately LH-only and is not reproduced on BetterVoting.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Alice,Brian,Colin
21:5,4,3
10:0,5,0
10:0,4,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Brian
  Choose-One (Plurality) = Alice   (differs from STAR)
  RCV-IRV                = Alice   (differs from STAR)
  RCV-RR (Condorcet)     = Alice   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/majority_illusion_c3_b41_two_rivals_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/majority_illusion_c3_b41_two_rivals_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 41 ballots.
Count × Alice,Brian,Colin
   21 ×     5,    4,    3
   10 ×     0,    5,    0
   10 ×     0,    4,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Brian         -- 174 -- First place
   Colin         -- 113 -- Second place
   Alice         -- 105
 Brian and Colin advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Brian         -- 31 -- First place
   Colin         -- 10
   Equal Support --  0
 Brian wins.
   Runoff math:
     41  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     41  voters with a preference  (majority = 21)
           Brian 31 (76%)  ·  Colin 10 (24%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Brian
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     Alice    |  * Brian    |  * Colin    |
-------------------------------------------------------------
         Alice > |     ---      |21 -  0 - 20 |21 - 10 - 10 |
       * Brian > | 20 -  0 - 21 |    ---      |31 -  0 - 10 |
       * Colin > | 10 - 10 - 21 |10 -  0 - 31 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Alice — STAR elected Brian instead (Alice was eliminated in the scoring round)

[Condorcet Loser]
  Condorcet Loser: Colin — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alice      21   0   0   0   0  20  |   105   2.6
Brian      10  31   0   0   0   0  |   174   4.2
Colin      10   0  21   0   0  10  |   113   2.8
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/majority_illusion_c3_b41_two_rivals_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/ces_majority_illusion/cases/majority_illusion_c3_b41_two_rivals.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/STAR_OUTLIER_RR_WITH_IRV/majority_illusion_c3_b41_two_rivals.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [majority_illusion_c3_b41_score_vs_star](majority_illusion_c3_b41_score_vs_star.md)
