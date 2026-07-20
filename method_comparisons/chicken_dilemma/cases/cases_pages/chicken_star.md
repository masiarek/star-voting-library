# Chicken / Burr dilemma — STAR resolves it (allies A & B beat C; A wins honestly)

*Generated from [`chicken_star.yaml`](../chicken_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** A

## Scenario

The chicken (a.k.a. Burr) dilemma from Jameson Quinn's strategic-pathology set. Two
similar candidates A and B must team up to beat a third, C, whom the majority opposes:
  35: A>B>C (A9 B8 C0)   25: B>A>C (A8 B9 C0)   40: C (C9, A0 B0)
Under APPROVAL voting this is a trap: if the 60 A/B voters honestly approve both A and
B, the result is an exact 60-60 A/B TIE (the "Burr dilemma", after the 1800 Jefferson-
Burr tie) — and each side is tempted to bullet-vote only its favorite, a slippery slope
that can hand the win to C if too many defect. See the companion chicken_approval.yaml.
STAR removes the slope. Scored honestly on 0-5, A and B voters give BOTH allies high
marks (no bullet needed — the runoff, not the sum, decides between them). C is beaten
in the scoring round (A 275, B 265, C 200), and A — the honest pairwise winner — takes
the runoff 35-25. Honesty is safe. The [Divergence from STAR] block confirms Ranked
Robin also elects A. Concept: ../../00_start_here/topics/strategic_pathologies.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:A,B,C
35:5,4,0   # A > B > C
25:4,5,0   # B > A > C
40:0,0,5   # C
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = A
  Choose-One (Plurality) = C   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × A,B,C
   40 × 0,0,5
   35 × 5,4,0
   25 × 4,5,0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   A             -- 275 -- First place
   B             -- 265 -- Second place
   C             -- 200
 A and B advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   A             -- 35 -- First place
   B             -- 25
   Equal Support -- 40
 A wins.
   Runoff math:
     100  ballots cast
   −  40  Equal Support (no preference between the two finalists)
     ───
      60  voters with a preference  (majority = 31)
           A 35 (58%)  ·  B 25 (42%)

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
           * A > |     ---      |35 - 40 - 25 |60 -  0 - 40 |
           * B > | 25 - 40 - 35 |    ---      |60 -  0 - 40 |
             C > | 40 -  0 - 60 |40 -  0 - 60 |    ---      |

[Condorcet Winner]
  Condorcet Winner: A — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
A          35  25   0   0   0  40  |   275   2.8
B          25  35   0   0   0  40  |   265   2.7
C          40   0   0   0   0  60  |   200   2.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/chicken_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/chicken_dilemma/cases/chicken_star.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [chicken_approval](chicken_approval.md)
