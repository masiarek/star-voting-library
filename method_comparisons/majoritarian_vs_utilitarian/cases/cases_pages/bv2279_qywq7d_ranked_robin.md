---
search:
  exclude: true
---

# Three brothers, one fruit — Ranked Robin confirms the majoritarian winner

*Generated from [`bv2279_qywq7d_ranked_robin.yaml`](../bv2279_qywq7d_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Banana

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/qywq7d) · **[results ↗](https://bettervoting.com/qywq7d/results)** (election `qywq7d` · test `BV2279`).

## Scenario

Race 2 of 3 in the three-brothers election (BV2279, bvid qywq7d; BV-confirmed).
The setup, the source and the x5/11 rescale are documented in the STAR race,
bv2279_qywq7d_star.yaml.

The same three opinions written as ranks. Boys 1 and 2 rank Banana first;
boy 3 ranks Banana LAST, behind a fruit he scored a 2.

Ranked Robin elects Banana on 2 pairwise wins — Banana beats Orange 2-1 and
Apple 2-1, Orange beats Apple 3-0. Banana is the Condorcet winner, Apple the
Condorcet loser.

This race exists to show that the majoritarian answer is not an artifact of
STAR's runoff. A method that reads only the order, and reads all of it, lands
on Banana too — because the majoritarian ideal is exactly what pairwise
counting measures.

And it shows what the ranks cost. Written this way, boy 3's ballot says
"Orange, then Apple, then Banana" — the same sentence he would write if
Banana were merely his least favorite rather than worth nothing at all. The
0 that makes Orange the utilitarian winner is not in this file. Compare the
Approval race (bv2279_qywq7d_approval.yaml), which keeps enough of the level
to elect Orange.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Banana>Orange>Apple   # Boy 1
Banana>Orange>Apple   # Boy 2
Orange>Apple>Banana   # Boy 3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (ranked ballots).

Ballots:
     2 × Banana > Orange > Apple
     1 × Orange > Apple > Banana

Round-Robin — every pair, head-to-head (For – Against):
   Banana  beats Orange   2 – 1
   Banana  beats Apple    2 – 1
   Orange  beats Apple    3 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
           |  Banana   | Orange   |  Apple   |
----------------------------------------------
  Banana > |    ---    |2 - 0 - 1 |2 - 0 - 1 |
  Orange > | 1 - 0 - 2 |   ---    |3 - 0 - 0 |
   Apple > | 1 - 0 - 2 |0 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Banana     2–0–0         2      +2  Orange, Apple
    2  Orange     1–1–0         1      +2  Apple
    3  Apple      0–2–0         0      -4  —

Winner — Ranked Robin (RCV-RR): Banana
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Banana
   Outside (2):        Orange, Apple
   One member ⇒ Banana is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Banana is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2279_qywq7d_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/majoritarian_vs_utilitarian/cases/bv2279_qywq7d_ranked_robin.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2279_qywq7d_approval](bv2279_qywq7d_approval.md) · [bv2279_qywq7d_star](bv2279_qywq7d_star.md)
