---
search:
  exclude: true
---

# Ranked Robin vs Consensus Choice — the same cycle, two different winners

*Generated from [`rr_vs_mwsl_cycle_c3_b32.yaml`](../rr_vs_mwsl_cycle_c3_b32.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn) · **1 seat** · **Expected winner:** Ana

## Scenario

32 ranked ballots, 3 candidates, one Condorcet cycle: Ana beats Bruno by 20, Bruno beats Celia by 4, Celia beats Ana by 8. Everyone finishes 1-1, so Copeland ties all three and the CYCLE RULE alone decides the election. The two rival "consensus" brands answer differently on these very same ballots. Equal Vote's Ranked Robin breaks the tie by net win margin and elects ANA (+12). Better Choices for Democracy's Consensus Choice breaks it by "Most Wins, Smallest Loss" and elects CELIA, whose single defeat is the mildest at 4 votes (Ana's is 8, Bruno's is 20). The engine below computes the Ranked Robin answer; the Consensus Choice answer is read straight off the same pairwise matrix.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:Ana>Bruno>Celia
6:Bruno>Celia>Ana
14:Celia>Ana>Bruno
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 32 ballots (ranked ballots).

Ballots:
    12 × Ana > Bruno > Celia
     6 × Bruno > Celia > Ana
    14 × Celia > Ana > Bruno

Round-Robin — every pair, head-to-head (For – Against):
   Ana    beats Bruno   26 –  6
   Celia  beats Ana     20 – 12
   Bruno  beats Celia   18 – 14

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |     Ana      |   Bruno     |   Celia     |
------------------------------------------------------
    Ana > |     ---      |26 -  0 -  6 |12 -  0 - 20 |
  Bruno > |  6 -  0 - 26 |    ---      |18 -  0 - 14 |
  Celia > | 20 -  0 - 12 |14 -  0 - 18 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ana        1–1–0         1     +12  Bruno
    2  Celia      1–1–0         1      +4  Ana
    3  Bruno      1–1–0         1     -16  Celia

Winner — Ranked Robin (RCV-RR): Ana
   *** 3 candidates tie for the most wins (Ana, Bruno, Celia) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): Ana, Bruno, Celia
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Ana is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/rr_vs_mwsl_cycle_c3_b32_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/02_Examples/consensus_choice_divergence/cases/rr_vs_mwsl_cycle_c3_b32.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)
