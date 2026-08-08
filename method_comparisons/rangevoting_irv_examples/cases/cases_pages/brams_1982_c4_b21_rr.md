---
search:
  exclude: true
---

# Brams 1982 — Ranked Robin on the identical ballots

*Generated from [`brams_1982_c4_b21_rr.yaml`](../brams_1982_c4_b21_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** G

## Scenario

The SAME 21 ballots as brams_1982_c4_b21.yaml, not one mark changed, counted
by Ranked Robin instead of Hare elimination.

Hare eliminates G in round 2 and elects B 13-8. Ranked Robin elects G, who
beats B 14-7, N 13-8 and F 18-3 — every rival head-to-head.

Twenty-one ballots and four candidates: small enough that a skeptic can check
both counts by hand and satisfy themselves that the disagreement is real and
not an artifact of anyone's software.

Triple-check status: LH native tally + pref_voting's independent Copeland
(ranked_robin_report.py). No BetterVoting leg — this is a published profile
reproduced from the literature, not a BV-backed case.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
7:B>G>N>F
6:G>B>N>F
5:N>G>B>F
3:F>N>G>B
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 21 ballots (ranked ballots).

Ballots:
     7 × B > G > N > F
     6 × G > B > N > F
     5 × N > G > B > F
     3 × F > N > G > B

Round-Robin — every pair, head-to-head (For – Against):
   G  beats B   14 –  7
   B  beats N   13 –  8
   B  beats F   18 –  3
   G  beats N   13 –  8
   G  beats F   18 –  3
   N  beats F   18 –  3

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |      B       |     G       |     N       |     F       |
----------------------------------------------------------------
  B > |     ---      | 7 -  0 - 14 |13 -  0 -  8 |18 -  0 -  3 |
  G > | 14 -  0 -  7 |    ---      |13 -  0 -  8 |18 -  0 -  3 |
  N > |  8 -  0 - 13 | 8 -  0 - 13 |    ---      |18 -  0 -  3 |
  F > |  3 -  0 - 18 | 3 -  0 - 18 | 3 -  0 - 18 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  G          3–0–0         3     +27  B, N, F
    2  B          2–1–0         2     +13  N, F
    3  N          1–2–0         1      +5  F
    4  F          0–3–0         0     -45  —

Winner — Ranked Robin (RCV-RR): G
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): G
   Outside (3):        B, N, F
   One member ⇒ G is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner G is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/brams_1982_c4_b21_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/rangevoting_irv_examples/cases/brams_1982_c4_b21_rr.yaml
```

## See also

- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [brams_1982_c4_b21](brams_1982_c4_b21.md) · [ossipoff_leader_eliminated_c5_b303](ossipoff_leader_eliminated_c5_b303.md) · [ossipoff_leader_eliminated_c5_b303_rr](ossipoff_leader_eliminated_c5_b303_rr.md)
