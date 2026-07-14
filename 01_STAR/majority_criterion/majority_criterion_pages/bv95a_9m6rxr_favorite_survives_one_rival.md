# BV95a — Majority Criterion: favorite survives when the majority backs ONE rival

*Generated from [`bv95a_9m6rxr_favorite_survives_one_rival.yaml`](../bv95a_9m6rxr_favorite_survives_one_rival.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ada

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9m6rxr) · **[results ↗](https://bettervoting.com/9m6rxr/results)** (election `9m6rxr`).

## Scenario

Backs sheet row BV95a (pair with BV95b / mc_02). A 5-voter STAR election. A 3-voter MAJORITY gives Ada their top score (5). The
question: can Ada still win once those voters honestly support other candidates
too? Here they back only ONE other candidate (Bruno = 4) and leave Cleo at 0.

Ada 15, Bruno 22, Cleo 10. Ada still reaches the runoff (top two by score are
Bruno and Ada), and in the runoff the 3-voter majority prefers Ada over Bruno,
so ADA WINS. Supporting a single second choice did NOT cost the majority their
favorite. Pair this with mc_02 (they back TWO rivals) to see when it flips.

Reproduced on BetterVoting (election 9m6rxr): BV also elects Ada
(nTallyVotes 5), confirming the LH result. Frozen export:
bv95a_9m6rxr_favorite_survives_one_rival_bv_export.json. Live:
https://bettervoting.com/9m6rxr/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Bruno,Cleo
5,4,0
5,4,0
5,4,0
0,5,5
0,5,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Ada
  Approval = Bruno   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Bruno)
 - Runoff Round Winner   = (Ada)
  Candidate Bruno earned the highest total score, but
  Candidate Ada won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 5 ballots.
Count × Ada,Bruno,Cleo
    3 ×   5,    4,   0
    2 ×   0,    5,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 22 -- First place
   Ada           -- 15 -- Second place
   Cleo          -- 10
 Bruno and Ada advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ada           -- 3 -- First place
   Bruno         -- 2
   Equal Support -- 0
 Ada wins.
   Runoff math:
     5  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Ada 3 (60%)  ·  Bruno 2 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ada
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ada    | * Bruno   |    Cleo   |
-----------------------------------------------------
       * Ada > |    ---     |3 - 0 - 2  |3 - 0 - 2  |
     * Bruno > | 2 - 0 - 3  |   ---     |3 - 2 - 0  |
        Cleo > | 2 - 0 - 3  |0 - 2 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ada — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        3  0  0  0  0  2  |    15   3.0
Bruno      2  3  0  0  0  0  |    22   4.4
Cleo       2  0  0  0  0  3  |    10   2.0
```

</details>

Everything in one file: the [`_tabulated` mirror](../majority_criterion_tabulated/bv95a_9m6rxr_favorite_survives_one_rival_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/majority_criterion/bv95a_9m6rxr_favorite_survives_one_rival.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../../method_comparisons/divergence_review/cases/APPROVAL_OR_MINOR/bv95a_9m6rxr_favorite_survives_one_rival.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv95b_7pdq3r_favorite_loses_two_rivals](bv95b_7pdq3r_favorite_loses_two_rivals.md)
