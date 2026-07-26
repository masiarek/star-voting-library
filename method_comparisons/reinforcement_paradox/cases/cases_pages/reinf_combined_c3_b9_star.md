# Reinforcement — combined 9 voters, counted by STAR (scoring round → Ada, runoff → Cara)

*Generated from [`reinf_combined_c3_b9_star.yaml`](../reinf_combined_c3_b9_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cara

## Scenario

The same merged 9-voter electorate as reinf_combined_c3_b9_rr.yaml, on STAR
score ballots (top = 5, middle = 3, last = 0 — the natural encoding of each
voter's ranking). It shows exactly where STAR sits on the reinforcement
question from Brandt, Dong & Peters (2024):

  - Scoring Round: Ada 29, Cara 27, Ben 16 — Ada leads. This is the pure
    Score/Range result, and it AGREES with Ada winning both districts:
    additive point methods satisfy reinforcement (Young 1975), so no paradox.
  - Automatic Runoff: Cara beats Ada 5–4. STAR's runoff is a pairwise step,
    and it catches Cara's head-to-head win — flipping the result to Cara.

So STAR's scoring round is consistent, but its runoff re-imports the same
Condorcet flip Ranked Robin shows: a Runoff Reversal, with Cara the Condorcet
winner. The engine's divergence block also reports Choose-One = Ada and
Approval = Ada — the additive methods that keep the reinforcement promise here.
Full discussion: the folder README.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cara
2:5,3,0
2:0,5,3
3:3,0,5
2:5,0,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Cara
  Choose-One (Plurality) = Ada   (differs from STAR)
  Approval               = Ada   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Ada)
 - Runoff Round Winner   = (Cara)
  Candidate Ada earned the highest total score, but
  Candidate Cara won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Ada,Ben,Cara
    3 ×   3,  0,   5
    2 ×   5,  3,   0
    2 ×   0,  5,   3
    2 ×   5,  0,   3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ada           -- 29 -- First place
   Cara          -- 27 -- Second place
   Ben           -- 16
 Ada and Cara advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cara          -- 5 -- First place
   Ada           -- 4
   Equal Support -- 0
 Cara wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Cara 5 (56%)  ·  Ada 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cara
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ada    |    Ben    |  * Cara   |
-----------------------------------------------------
       * Ada > |    ---     |7 - 0 - 2  |4 - 0 - 5  |
         Ben > | 2 - 0 - 7  |   ---     |4 - 0 - 5  |
      * Cara > | 5 - 0 - 4  |5 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cara — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ben — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        4  0  3  0  0  2  |    29   3.2
Ben        2  0  2  0  0  5  |    16   1.8
Cara       3  0  4  0  0  2  |    27   3.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reinf_combined_c3_b9_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reinforcement_paradox/cases/reinf_combined_c3_b9_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/reinf_combined_c3_b9_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [reinf_combined_ben_c3_b9_rr](reinf_combined_ben_c3_b9_rr.md) · [reinf_combined_c3_b9_rr](reinf_combined_c3_b9_rr.md) · [reinf_combined_cara_c3_b9_rr](reinf_combined_cara_c3_b9_rr.md) · [reinf_north_c3_b6_rr](reinf_north_c3_b6_rr.md) · [reinf_south_ben_c3_b3_rr](reinf_south_ben_c3_b3_rr.md) · [reinf_south_c3_b3_rr](reinf_south_c3_b3_rr.md) · [reinf_south_cara_c3_b3_rr](reinf_south_cara_c3_b3_rr.md)
