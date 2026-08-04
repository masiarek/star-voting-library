---
search:
  exclude: true
---

# Condorcet's 1788 rebuttal to Borda — STAR elects the Condorcet winner

*Generated from [`condorcet_1788_star.yaml`](../condorcet_1788_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn) · **1 seat** · **Expected winner:** Peter

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/khcwm4) · **[results ↗](https://bettervoting.com/khcwm4/results)** (election `khcwm4` · test `BV2250`).

## Scenario

Condorcet's own counterexample to the Borda count, in the simplified 11-voter
form modern textbooks use. Three candidates (Condorcet's Peter, Paul and James)
and four blocs of voters:

    4 : Peter > Paul  > James
    3 : Paul  > James > Peter
    2 : Paul  > Peter > James
    2 : James > Peter > Paul

Borda had argued (1770) that his rank-points rule beat plurality because the
plurality winner can lose a direct majority contest. Condorcet's reply: your rule
has the same disease. Here BOTH plurality (Paul, 5 first choices) and Borda
(Paul, 14 points to Peter's 12) elect Paul — yet Peter beats Paul head-to-head
6-5, and beats James 6-5 as well. Peter is the Condorcet winner, and Paul is not.

This file runs the profile under STAR. Ranks carry no intensity, so the ranked
ballots are converted to scores with an even 5 / 3 / 0 spacing; the winner is
robust to that choice (5/4/0, 5/2/0, 5/1/0 and 4/2/0 all give the same result —
Paul leads the scoring round, Peter wins the runoff).

The result is a runoff reversal, and that is the whole lesson. STAR's scoring
round is a positional count — under a uniform spacing it IS a Borda count — so
it reproduces Borda's answer and puts Paul first with 37 points. Then the
automatic runoff runs exactly the direct majority contest Condorcet demanded,
and Peter wins it 6-5. STAR is Borda's scoring step followed by Condorcet's
check, and on Condorcet's own counterexample it returns Condorcet's answer.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Peter,Paul,James
4:5,3,0
3:0,5,3
2:3,5,0
2:3,0,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Peter
  Choose-One (Plurality) = Paul   (differs from STAR)
  Approval               = Paul   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Paul)
 - Runoff Round Winner   = (Peter)
  Candidate Paul earned the highest total score, but
  Candidate Peter won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 11 ballots.
Count × Peter,Paul,James
    4 ×     5,   3,    0
    3 ×     0,   5,    3
    2 ×     3,   5,    0
    2 ×     3,   0,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Paul          -- 37 -- First place
   Peter         -- 32 -- Second place
   James         -- 19
 Paul and Peter advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Peter         -- 6 -- First place
   Paul          -- 5
   Equal Support -- 0
 Peter wins.
   Runoff math:
     11  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     11  voters with a preference  (majority = 6)
           Peter 6 (55%)  ·  Paul 5 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Peter
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Peter   |  * Paul   |   James   |
-----------------------------------------------------
     * Peter > |    ---     |6 - 0 - 5  |6 - 0 - 5  |
      * Paul > | 5 - 0 - 6  |   ---     |9 - 0 - 2  |
       James > | 5 - 0 - 6  |2 - 0 - 9  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Peter — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: James — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Peter      4  0  4  0  0  3  |    32   2.9
Paul       5  0  4  0  0  2  |    37   3.4
James      2  0  3  0  0  6  |    19   1.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/condorcet_1788_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/borda_condorcet_1788/cases/condorcet_1788_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/condorcet_1788_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [condorcet_1788_irv](condorcet_1788_irv.md) · [condorcet_1788_ranked_robin](condorcet_1788_ranked_robin.md)
