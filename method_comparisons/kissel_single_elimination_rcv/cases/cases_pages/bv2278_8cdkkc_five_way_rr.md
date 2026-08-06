---
search:
  exclude: true
---

# Kissel's five-way example (Ranked Robin) — the same ballots elect C

*Generated from [`bv2278_8cdkkc_five_way_rr.yaml`](../bv2278_8cdkkc_five_way_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** C

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8cdkkc) · **[results ↗](https://bettervoting.com/8cdkkc/results)** (election `8cdkkc` · test `BV2278`).

## Scenario

The identical ballots as …_irv.yaml — the five-candidate field from p.5 of Adam Kissel's "Can Ranked-Choice Voting Work? A Conservative Approach" — counted by Ranked Robin (RCV-RR / Copeland) instead of instant runoff. Every ballot is read in every pairing, so the A voters' and B voters' second choices DO get counted, and C wins the round-robin 4-0: 511-489 over A, 700-300 over B, 808-192 over D, 991-9 over E. This is the direct refutation of the paper's claim that denying some voters their second choice is "essentially the same in all forms of RCV" — it is a property of ELIMINATION, not of the ranked ballot. Nothing about the ballots changed; only the count did.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
306:A>C>D>B>E     # A-partisans — moderate C is their second choice
300:B>C>D>A>E     # B-partisans — moderate C is their second choice too
111:C>A>B>D>E     # moderates leaning A
 91:C>B>A>D>E     # moderates leaning B
183:D>A>C>B>E     # D's voters lean A
  9:E>D>C>A>B     # the <1% candidate the paper says is eliminated first
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 1000 ballots (ranked ballots).

Ballots:
   306 × A > C > D > B > E
   300 × B > C > D > A > E
   111 × C > A > B > D > E
    91 × C > B > A > D > E
   183 × D > A > C > B > E
     9 × E > D > C > A > B

Round-Robin — every pair, head-to-head (For – Against):
   C  beats A   511 – 489
   A  beats D   508 – 492
   A  beats B   609 – 391
   A  beats E   991 –   9
   C  beats D   808 – 192
   C  beats B   700 – 300
   C  beats E   991 –   9
   B  beats D   502 – 498
   D  beats E   991 –   9
   B  beats E   991 –   9

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
      |        A        |       C        |       D        |       B        |       E        |
---------------------------------------------------------------------------------------------
  A > |       ---       |489 -   0 - 511 |508 -   0 - 492 |609 -   0 - 391 |991 -   0 -   9 |
  C > | 511 -   0 - 489 |      ---       |808 -   0 - 192 |700 -   0 - 300 |991 -   0 -   9 |
  D > | 492 -   0 - 508 |192 -   0 - 808 |      ---       |498 -   0 - 502 |991 -   0 -   9 |
  B > | 391 -   0 - 609 |300 -   0 - 700 |502 -   0 - 498 |      ---       |991 -   0 -   9 |
  E > |   9 -   0 - 991 |  9 -   0 - 991 |  9 -   0 - 991 |  9 -   0 - 991 |      ---       |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  C          4–0–0         4   +2020  A, B, D, E
    2  A          3–1–0         3   +1194  B, D, E
    3  B          2–2–0         2    +368  D, E
    4  D          1–3–0         1    +346  E
    5  E          0–4–0         0   -3928  —

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
   Outside (4):        A, D, B, E
   One member ⇒ C is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner C is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2278_8cdkkc_five_way_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/kissel_single_elimination_rcv/cases/bv2278_8cdkkc_five_way_rr.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2277_tqfdbg_mayor_irv](bv2277_tqfdbg_mayor_irv.md) · [bv2277_tqfdbg_mayor_plurality](bv2277_tqfdbg_mayor_plurality.md) · [bv2277_tqfdbg_mayor_rr](bv2277_tqfdbg_mayor_rr.md) · [bv2277_tqfdbg_mayor_star](bv2277_tqfdbg_mayor_star.md) · [bv2278_8cdkkc_five_way_irv](bv2278_8cdkkc_five_way_irv.md) · [bv2278_8cdkkc_five_way_plurality](bv2278_8cdkkc_five_way_plurality.md) · [bv2278_8cdkkc_five_way_star](bv2278_8cdkkc_five_way_star.md)
