---
search:
  exclude: true
---

# Condorcet's 1788 rebuttal to Borda — the ranked profile, counted pairwise

*Generated from [`condorcet_1788_ranked_robin.yaml`](../condorcet_1788_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Peter

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/khcwm4) · **[results ↗](https://bettervoting.com/khcwm4/results)** (election `khcwm4` · test `BV2250`).

## Scenario

The same election as condorcet_1788_star.yaml, kept in its original RANKED form
and counted the way Condorcet said it should be: every pair, head-to-head.

    4 : Peter > Paul  > James
    3 : Paul  > James > Peter
    2 : Paul  > Peter > James
    2 : James > Peter > Paul

The round-robin table is the argument. Peter beats Paul 6-5 and beats James 6-5,
so Peter is the Condorcet winner. Borda's positional count elects Paul (14 points
to Peter's 12), and plurality elects Paul too (5 first choices) — both crown a
candidate who loses a direct majority contest, which was precisely the defect
Borda had accused plurality of.

Ranked Robin reads only the ORDER on each ballot, never the rank numbers, so it
cannot be led astray by positional points the way Borda is. That distinction —
same ranked ballot, different tabulation — is the whole reason "RCV" names a
ballot and not a count.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
4:Peter>Paul>James
3:Paul>James>Peter
2:Paul>Peter>James
2:James>Peter>Paul
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 11 ballots (ranked ballots).

Ballots:
     4 × Peter > Paul > James
     3 × Paul > James > Peter
     2 × Paul > Peter > James
     2 × James > Peter > Paul

Round-Robin — every pair, head-to-head (For – Against):
   Peter  beats Paul    6 – 5
   Peter  beats James   6 – 5
   Paul   beats James   9 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Peter   |  Paul    |  James   |
---------------------------------------------
  Peter > |    ---    |6 - 0 - 5 |6 - 0 - 5 |
   Paul > | 5 - 0 - 6 |   ---    |9 - 0 - 2 |
  James > | 5 - 0 - 6 |2 - 0 - 9 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Peter      2–0–0         2      +2  Paul, James
    2  Paul       1–1–0         1      +6  James
    3  James      0–2–0         0      -8  —

Winner — Ranked Robin (RCV-RR): Peter
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Peter
   Outside (2):        Paul, James
   One member ⇒ Peter is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Peter is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/condorcet_1788_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/borda_condorcet_1788/cases/condorcet_1788_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [condorcet_1788_irv](condorcet_1788_irv.md) · [condorcet_1788_star](condorcet_1788_star.md)
