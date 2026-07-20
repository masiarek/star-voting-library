# Favorite betrayal in STAR (2 of 2) — nine voters demote their favorite and it pays

*Generated from [`bv2207_b6xrdr_fbc_betrayal_pays.yaml`](../bv2207_b6xrdr_fbc_betrayal_pays.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Bluebell

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/b6xrdr) · **[results ↗](https://bettervoting.com/b6xrdr/results)** (election `b6xrdr`).

## Scenario

The betrayal — half 2 of the repo's worked STAR favorite-betrayal
pair. Same 57 voters as half 1
(bv2206_7mckyg_fbc_honest_tepid_consensus.yaml), except the nine
Aster-fans now score Aster 4 instead of 5 — strictly below Bluebell on
their own ballots. Note what they could NOT do: raise Bluebell. She
was already at 5 — STAR let them equal-top the compromise for free,
and it wasn't enough, because the problem was Aster's own score total
keeping Bluebell OUT of the runoff. Demoting him is the only move
left, and it is a true favorite betrayal (scoring your favorite below
another candidate). Scores become Clover 72, Bluebell 69, Aster 66 —
the runoff flips from Aster-vs-Clover to Clover-vs-Bluebell, and the
Condorcet winner Bluebell takes it 33-18. The nine turned their
outcome from Clover (their 0) into Bluebell (their 5). The knife-edge
that makes it a lab specimen, not a strategy: it needs AT LEAST 7 of
the 9 to coordinate (6 betrayers leave Aster and Bluebell tied at 69
for the second runoff seat; 5 or fewer changes nothing), plus exact
knowledge of a 3-point standings gap. This is the ~2% of STAR
betrayals that pay — the other ~98% backfire (see
favorite_betrayal_voting_301.md and 06_Other/simulations/).
Live on BetterVoting (Test ID BV2207): https://bettervoting.com/b6xrdr
Live results: https://bettervoting.com/b6xrdr/results (BV agrees:
Bluebell, no tiebreaks).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Aster,Bluebell,Clover
9: 4,5,0
6: 5,0,0
24: 0,1,0
18: 0,0,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Bluebell
  Approval = Clover   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Clover)
 - Runoff Round Winner   = (Bluebell)
  Candidate Clover earned the highest total score, but
  Candidate Bluebell won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 57 ballots.
Count × Aster,Bluebell,Clover
   24 ×     0,       1,     0
   18 ×     0,       0,     4
    9 ×     4,       5,     0
    6 ×     5,       0,     0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Clover        -- 72 -- First place
   Bluebell      -- 69 -- Second place
   Aster         -- 66
 Clover and Bluebell advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bluebell      -- 33 -- First place
   Clover        -- 18
   Equal Support --  6
 Bluebell wins.
   Runoff math:
     57  ballots cast
   −  6  Equal Support (no preference between the two finalists)
     ──
     51  voters with a preference  (majority = 26)
           Bluebell 33 (65%)  ·  Clover 18 (35%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Bluebell
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     Aster    | * Bluebell  |  * Clover   |
-------------------------------------------------------------
         Aster > |     ---      | 6 - 18 - 33 |15 - 24 - 18 |
    * Bluebell > | 33 - 18 -  6 |    ---      |33 -  6 - 18 |
      * Clover > | 18 - 24 - 15 |18 -  6 - 33 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Bluebell — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Aster       6   9   0   0   0  42  |    66   1.2
Bluebell    9   0   0   0  24  24  |    69   1.2
Clover      0  18   0   0   0  39  |    72   1.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2207_b6xrdr_fbc_betrayal_pays_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/favorite_betrayal/cases/bv2207_b6xrdr_fbc_betrayal_pays.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/bv2207_b6xrdr_fbc_betrayal_pays.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2206_7mckyg_fbc_honest_tepid_consensus](bv2206_7mckyg_fbc_honest_tepid_consensus.md)
