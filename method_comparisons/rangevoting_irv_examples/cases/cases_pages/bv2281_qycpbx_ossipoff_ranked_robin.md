---
search:
  exclude: true
---

# Ossipoff's 303 — Ranked Robin on the identical ballots

*Generated from [`bv2281_qycpbx_ossipoff_ranked_robin.yaml`](../bv2281_qycpbx_ossipoff_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** C

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qycpbx) · **[results ↗](https://bettervoting.com/qycpbx/results)** (election `qycpbx` · test `BV2281`).

## Scenario

The SAME 303 ballots as bv2281_qycpbx_ossipoff_irv.yaml, not one mark
changed, counted by Ranked Robin instead of Hare elimination. Same paper, same
voters, same rankings — only the counting rule differs.

Hare eliminates C in round 3 and elects D. Ranked Robin compares every pair
head-to-head and elects C, who beats A 202-101, B 202-101, D 201-102 and
E 201-102 — every rival, by roughly two to one.

This is the pairing worth leading with when talking to someone who likes
ranked ballots, because it asks for NOTHING from them: no new ballot, no
scores, no relearning how to vote. The ranked ballot they already support is
fine. It is the tabulation that threw C away.

TRIPLE-CHECKED, all three legs agreeing on C: this LH native tally,
BetterVoting's own RankedRobin.ts (live election qycpbx, race 2 — frozen in
bv2281_qycpbx_bv_export.json, tieBreakType 'none'), and pref_voting's
independent Copeland (ranked_robin_report.py — AGREE, unique leader C).

Live on BetterVoting (Test ID BV2281): https://bettervoting.com/qycpbx
Live results: https://bettervoting.com/qycpbx/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
50:A>B>C>D>E
51:B>A>C>D>E
100:C>D>B>E>A
53:D>E>C>B>A
49:E>D>C>B>A
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 303 ballots (ranked ballots).

Ballots:
    50 × A > B > C > D > E
    51 × B > A > C > D > E
   100 × C > D > B > E > A
    53 × D > E > C > B > A
    49 × E > D > C > B > A

Round-Robin — every pair, head-to-head (For – Against):
   B  beats A   253 –  50
   C  beats A   202 – 101
   D  beats A   202 – 101
   E  beats A   202 – 101
   C  beats B   202 – 101
   D  beats B   202 – 101
   B  beats E   201 – 102
   C  beats D   201 – 102
   C  beats E   201 – 102
   D  beats E   254 –  49

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |        A        |       B        |       C        |       D        |       E        |
---------------------------------------------------------------------------------------------
  A > |       ---       | 50 -   0 - 253 |101 -   0 - 202 |101 -   0 - 202 |101 -   0 - 202 |
  B > | 253 -   0 -  50 |      ---       |101 -   0 - 202 |101 -   0 - 202 |201 -   0 - 102 |
  C > | 202 -   0 - 101 |202 -   0 - 101 |      ---       |201 -   0 - 102 |201 -   0 - 102 |
  D > | 202 -   0 - 101 |202 -   0 - 101 |102 -   0 - 201 |      ---       |254 -   0 -  49 |
  E > | 202 -   0 - 101 |102 -   0 - 201 |102 -   0 - 201 | 49 -   0 - 254 |      ---       |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  C          4–0–0         4    +400  D, B, E, A
    2  D          3–1–0         3    +308  B, E, A
    3  B          2–2–0         2    +100  E, A
    4  E          1–3–0         1    -302  A
    5  A          0–4–0         0    -506  —

Winner — Ranked Robin (RCV-RR): C
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 5): C
   Outside (4):        A, B, D, E
   One member ⇒ C is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner C is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2281_qycpbx_ossipoff_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/rangevoting_irv_examples/cases/bv2281_qycpbx_ossipoff_ranked_robin.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2281_qycpbx_ossipoff_irv](bv2281_qycpbx_ossipoff_irv.md) · [bv2282_hf3ckp_brams_irv](bv2282_hf3ckp_brams_irv.md) · [bv2282_hf3ckp_brams_ranked_robin](bv2282_hf3ckp_brams_ranked_robin.md)
