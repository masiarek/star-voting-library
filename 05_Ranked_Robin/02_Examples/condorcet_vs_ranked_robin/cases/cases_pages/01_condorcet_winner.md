---
search:
  exclude: true
---

# Condorcet winner exists — Ranked Robin elects it

*Generated from [`01_condorcet_winner.yaml`](../01_condorcet_winner.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

5 ranked ballots, 3 candidates. Ada beats both Ben and Cara head-to-head, so Ada is the Condorcet winner — and Ranked Robin (most pairwise wins) elects Ada. When a Condorcet winner exists, Ranked Robin and "the Condorcet winner" are the SAME answer.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Ada>Ben>Cara
Ada>Ben>Cara
Ada>Ben>Cara
Ben>Ada>Cara
Ben>Ada>Cara
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 5 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cara
     2 × Ben > Ada > Cara

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    3 – 2
   Ada   beats Cara   5 – 0
   Ben   beats Cara   5 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |3 - 0 - 2 |5 - 0 - 0 |
   Ben > | 2 - 0 - 3 |   ---    |5 - 0 - 0 |
  Cara > | 0 - 0 - 5 |0 - 0 - 5 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +6  Ben, Cara
    2  Ben        1–1–0         1      +4  Cara
    3  Cara       0–2–0         0     -10  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Ada
   Outside (2):        Ben, Cara
   One member ⇒ Ada is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Ada is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/01_condorcet_winner_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/02_Examples/condorcet_vs_ranked_robin/cases/01_condorcet_winner.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [02_cycle_no_condorcet](02_cycle_no_condorcet.md) · [03_real_record0_c6_b5](03_real_record0_c6_b5.md) · [04_smith_set_c4_b7](04_smith_set_c4_b7.md) · [bv2140_48hjkv_most_pairwise_wins](bv2140_48hjkv_most_pairwise_wins.md)
