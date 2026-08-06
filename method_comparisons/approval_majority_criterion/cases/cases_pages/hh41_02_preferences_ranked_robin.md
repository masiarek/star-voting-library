---
search:
  exclude: true
---

# Hamlin & Hua §4.1 — the assumed preferences, counted pairwise: A is the Condorcet winner

*Generated from [`hh41_02_preferences_ranked_robin.yaml`](../hh41_02_preferences_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** A

**Official tie-break (lot) order:** A > B > C — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The SAME electorate as hh41_01_approval_as_printed.yaml, but reading the
paper's ASSUMED PREFERENCES as ranked ballots instead of the approval marks
they were compressed into:
  60 voters: A > B > C
  30 voters: B > C > A
  10 voters: C > B > A

The paper opens §4.1 by observing that "there is not always a Condorcet
winner." True in general — but this profile has one, and it is A: A beats B
60-40 and beats C 60-40. So A is not merely the first choice of a majority
(the majority criterion), A is also the candidate a majority prefers in every
head-to-head. Ranked Robin, Choose-One and RCV-IRV all elect A here; the
approval count elects B.

This file exists to establish that fact from the engine rather than by hand,
because it is the one thing the paper's own framing does not say about its
own example.

Claim-check page: ../../../04_Approval/01_Learn/hamlin_hua_2023.md
Set overview: ../README.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
60:A>B>C
30:B>C>A
10:C>B>A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 100 ballots (ranked ballots).

Ballots:
    60 × A > B > C
    30 × B > C > A
    10 × C > B > A

Round-Robin — every pair, head-to-head (For – Against):
   A  beats B   60 – 40
   A  beats C   60 – 40
   B  beats C   90 – 10

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |      A       |     B       |     C       |
--------------------------------------------------
  A > |     ---      |60 -  0 - 40 |60 -  0 - 40 |
  B > | 40 -  0 - 60 |    ---      |90 -  0 - 10 |
  C > | 40 -  0 - 60 |10 -  0 - 90 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  A          2–0–0         2     +40  B, C
    2  B          1–1–0         1     +60  C
    3  C          0–2–0         0    -100  —

Winner — Ranked Robin (RCV-RR): A
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): A
   Outside (2):        B, C
   One member ⇒ A is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner A is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/hh41_02_preferences_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/approval_majority_criterion/cases/hh41_02_preferences_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [hh41_01_approval_as_printed](hh41_01_approval_as_printed.md) · [hh41_03_marks_read_pairwise](hh41_03_marks_read_pairwise.md) · [hh41_04_stipulated_utilities_star](hh41_04_stipulated_utilities_star.md) · [hh41_05_majority_bullet_votes](hh41_05_majority_bullet_votes.md)
