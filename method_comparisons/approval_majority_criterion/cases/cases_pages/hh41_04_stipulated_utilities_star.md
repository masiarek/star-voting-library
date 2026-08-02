---
search:
  exclude: true
---

# Hamlin & Hua §4.1 — their own utility stipulation, on a 0-5 ballot: A 380, B 370, A wins

*Generated from [`hh41_04_stipulated_utilities_star.yaml`](../hh41_04_stipulated_utilities_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/concepts) · **1 seat** · **Expected winner:** A

## Scenario

Section 4.1 defends the majority-criterion failure by arguing that for B to be
genuinely worse than A "would require certain assumptions. This would mean
that the set of 60 voters would have to strongly prefer candidate A and barely
find candidate B acceptable. And the remainder of voters would have to just
barely disapprove of candidate A. To the degree that this is true, it's
challenging to arrive at a plausible scenario where this violation has a
meaningfully large utility discrepancy."

This file IS that scenario, written down. Their stipulation maps onto a 0-5
STAR ballot with nothing left to interpretation:
  "strongly prefer A"            -> A = 5
  "barely find B acceptable"     -> B = 3   (right at the approval line)
  "just barely disapprove of A"  -> A = 2   (just under it)

Two things follow, and they cut in opposite directions — both worth stating.

1. The paper is RIGHT that the utility gap is small. The scoring round is
   A 380, B 370 — ten points out of five hundred, near enough to a tie.

2. The paper is WRONG that this rescues the approval result. STAR still elects
   A, because after the scoring round it asks the majority question: A 60,
   B 40. And the approval count on these very same voters reports B over A by
   100 to 60 — a landslide, where the full-resolution ballot shows a coin
   flip. Approval doesn't just miss the gap, it inverts and magnifies it.

Consistency check the engine performs for free: the [Divergence from STAR]
block cuts these scores at the approval line (3+) and reports Approval = B —
i.e. these 0-5 ballots reproduce the paper's assumed approval ballots exactly.
This is not a different election. It is their election at higher resolution.

Claim-check page: ../../../04_Approval/concepts/hamlin_hua_2023.md
Set overview: ../README.md

## Parameters (from the YAML)

```yaml
voting_method: STAR
num_winners: 1
expected_winners: [A]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
60:5,3,0   # strongly prefer A; B barely acceptable (at the approval line)
30:2,5,4   # A just barely disapproved of (just under the line)
10:2,4,5   # same, C first
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = A
  Approval = B   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × A,B,C
   60 × 5,3,0
   30 × 2,5,4
   10 × 2,4,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 380 -- First place
   B             -- 370 -- Second place
   C             -- 170
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 60 -- First place
   B             -- 40
   Equal Support --  0
 A wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           A 60 (60%)  ·  B 40 (40%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 A
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |     * A      |    * B      |      C      |
-------------------------------------------------------------
           * A > |     ---      |60 -  0 - 40 |60 -  0 - 40 |
           * B > | 40 -  0 - 60 |    ---      |90 -  0 - 10 |
             C > | 40 -  0 - 60 |10 -  0 - 90 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: C — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          60   0   0  40   0   0  |   380   3.8
B          30  10  60   0   0   0  |   370   3.7
C          10  30   0   0   0  60  |   170   1.7
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/hh41_04_stipulated_utilities_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/approval_majority_criterion/cases/hh41_04_stipulated_utilities_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/APPROVAL_OR_MINOR/hh41_04_stipulated_utilities_star.md) — its entry in the divergence review ledger
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [hh41_01_approval_as_printed](hh41_01_approval_as_printed.md) · [hh41_02_preferences_ranked_robin](hh41_02_preferences_ranked_robin.md) · [hh41_03_marks_read_pairwise](hh41_03_marks_read_pairwise.md) · [hh41_05_majority_bullet_votes](hh41_05_majority_bullet_votes.md)
