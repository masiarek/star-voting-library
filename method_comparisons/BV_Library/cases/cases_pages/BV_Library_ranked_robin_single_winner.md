---
search:
  exclude: true
---

# BV parity — Ranked Robin: Condorcet winner (equal ranks allowed)

*Generated from [`BV_Library_ranked_robin_single_winner.yaml`](../BV_Library_ranked_robin_single_winner.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** Alice

## Scenario

Ported from BetterVoting's tabulator unit tests (RankedRobin.test.ts :: "Single winner test").
BetterVoting supplies rank ballots (1 = best) including EQUAL ranks and an abstention.
Converted here to score ballots for the LH engine (higher score = more preferred,
equal scores = equal rank, blank = unranked): rank 1->4, 2->3, 3->2, 4->1, unranked->0.
One original out-of-bounds mark (rank -1 for Dave) becomes a blank. Alice wins every
head-to-head (Condorcet winner); Copeland scores match BetterVoting (Alice 3, Bob 2,
Carol 1, Dave 0).

## Parameters (from the YAML)

```yaml
voting_method: RankedRobin
num_winners: 1
expected_winners: [Alice]
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Alice,Bob,Carol,Dave
4,3,2,0
4,3,2,1
4,3,2,1
4,4,3,2
4,4,3,2
3,4,2,1
3,4,2,1
3,2,4,1
3,2,1,4
-,-,-,-
3,2,1,-
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 11 ballots (score ballots).

Ballots:
   the ranking Ranked Robin reads ("=" = tied); source scores follow in () per column: Alice, Bob, Carol, Dave
     1 × Alice > Bob > Carol > Dave      (4, 3, 2, 0)
     2 × Alice > Bob > Carol > Dave      (4, 3, 2, 1)
     2 × Alice=Bob > Carol > Dave      (4, 4, 3, 2)
     2 × Bob > Alice > Carol > Dave      (3, 4, 2, 1)
     1 × Carol > Alice > Bob > Dave      (3, 2, 4, 1)
     1 × Dave > Alice > Bob > Carol      (3, 2, 1, 4)
     1 × Alice=Bob=Carol=Dave      (0, 0, 0, 0)
     1 × Alice > Bob > Carol > Dave      (3, 2, 1, 0)

Round-Robin — every pair, head-to-head (For – Against):
   Alice  beats Bob     6 – 2
   Alice  beats Carol   9 – 1
   Alice  beats Dave    9 – 1
   Bob    beats Carol   9 – 1
   Bob    beats Dave    9 – 1
   Carol  beats Dave    9 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Alice   |   Bob    |  Carol   |  Dave    |
--------------------------------------------------------
  Alice > |    ---    |6 - 3 - 2 |9 - 1 - 1 |9 - 1 - 1 |
    Bob > | 2 - 3 - 6 |   ---    |9 - 1 - 1 |9 - 1 - 1 |
  Carol > | 1 - 1 - 9 |1 - 1 - 9 |   ---    |9 - 1 - 1 |
   Dave > | 1 - 1 - 9 |1 - 1 - 9 |1 - 1 - 9 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Alice      3–0–0         3     +20  Bob, Carol, Dave
    2  Bob        2–1–0         2     +12  Carol, Dave
    3  Carol      1–2–0         1      -8  Dave
    4  Dave       0–3–0         0     -24  —

Winner — Ranked Robin (RCV-RR): Alice
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): Alice
   Outside (3):        Bob, Carol, Dave
   One member ⇒ Alice is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Alice is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/BV_Library_ranked_robin_single_winner_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/BV_Library/cases/BV_Library_ranked_robin_single_winner.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [BV_Library_approval_single_winner](BV_Library_approval_single_winner.md) · [BV_Library_plurality_single_winner](BV_Library_plurality_single_winner.md) · [BV_Library_ranked_robin_ties](BV_Library_ranked_robin_ties.md) · [BV_Library_star_condorcet_winner](BV_Library_star_condorcet_winner.md) · [BV_Library_star_pr_basic_two_seats](BV_Library_star_pr_basic_two_seats.md) · [BV_Library_star_pr_fractional_surplus](BV_Library_star_pr_fractional_surplus.md) · [BV_Library_star_pr_voters_fewer_than_seats](BV_Library_star_pr_voters_fewer_than_seats.md) · [BV_Library_star_runnerup_tie](BV_Library_star_runnerup_tie.md) · [BV_Library_star_runoff](BV_Library_star_runoff.md) · [BV_Library_star_runoff_score_tie_five_star](BV_Library_star_runoff_score_tie_five_star.md) · [BV_Library_star_runoff_tie_score_resolves](BV_Library_star_runoff_tie_score_resolves.md)
