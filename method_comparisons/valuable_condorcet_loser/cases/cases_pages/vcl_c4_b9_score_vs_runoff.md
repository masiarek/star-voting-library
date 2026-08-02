---
search:
  exclude: true
---

# The valuable Condorcet loser — Score elects her, the runoff rejects her

*Generated from [`vcl_c4_b9_score_vs_runoff.yaml`](../vcl_c4_b9_score_vs_runoff.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/concepts) · **1 seat** · **Expected winner:** Ben

## Scenario

The "valuable Condorcet loser" instance from Ebadian, Latifian & Shah,
"The Distortion of Approval Voting with Runoff" (AAMAS 2023, Example 5.1),
scaled down to nine countable ballots. Amy is adored by a 4-voter minority
(5s across the board) and scored zero by the 5-voter majority, who spread
mild support over Ben, Cora, and Dan. Amy has nearly DOUBLE anyone else's
score total (20 vs 11) — she is the utilitarian (Score-voting) winner —
and she is simultaneously the CONDORCET LOSER: head-to-head she loses to
every rival 4:5. Any method with a majority runoff (STAR here; approval-
with-runoff in the paper; St. Louis-style top-two) therefore rejects her:
she reaches the STAR runoff on her score total and loses it 4:5 to Ben,
the Condorcet winner. In the paper's unit-sum worst case this scenario is
exactly why ADDING a majority runoff RAISES approval voting's distortion
from Theta(m) to Theta(m^2): the runoff structurally blocks the high-
welfare candidate. One election, two defensible verdicts — the
majoritarian one (Ben) and the utilitarian one (Amy) — and which is
"right" is the values question, not arithmetic.

## Parameters (from the YAML)

```yaml
voting_method: STAR
num_winners: 1
expected_winners: [Ben]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Amy,Ben,Cora,Dan
5,0,0,0
5,0,0,0
5,0,0,0
5,0,0,0
0,2,2,2
0,2,2,2
0,2,2,2
0,2,2,2
0,3,2,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Ben
  Approval = Amy   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Amy)
 - Runoff Round Winner   = (Ben)
  Candidate Amy earned the highest total score, but
  Candidate Ben won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Amy,Ben,Cora,Dan
    4 ×   5,  0,   0,  0
    4 ×   0,  2,   2,  2
    1 ×   0,  3,   2,  1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Amy           -- 20 -- First place
   Ben           -- 11 -- Second place
   Cora          -- 10
   Dan           --  9
 Amy and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ben           -- 5 -- First place
   Amy           -- 4
   Equal Support -- 0
 Ben wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Ben 5 (56%)  ·  Amy 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ben
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Amy    |  * Ben    |    Cora   |    Dan    |
-----------------------------------------------------------------
       * Amy > |    ---     |4 - 0 - 5  |4 - 0 - 5  |4 - 0 - 5  |
       * Ben > | 5 - 0 - 4  |   ---     |1 - 8 - 0  |1 - 8 - 0  |
        Cora > | 5 - 0 - 4  |0 - 8 - 1  |   ---     |1 - 8 - 0  |
         Dan > | 5 - 0 - 4  |0 - 8 - 1  |0 - 8 - 1  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ben — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Amy — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Amy        4  0  0  0  0  5  |    20   2.2
Ben        0  0  1  4  0  4  |    11   1.2
Cora       0  0  0  5  0  4  |    10   1.1
Dan        0  0  0  4  1  4  |     9   1.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/vcl_c4_b9_score_vs_runoff_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/valuable_condorcet_loser/cases/vcl_c4_b9_score_vs_runoff.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/vcl_c4_b9_score_vs_runoff.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)
