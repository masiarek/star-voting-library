---
search:
  exclude: true
---

# Center Squeeze — Ranked Robin (Copeland): the Condorcet winner survives

*Generated from [`bv2137_ywckmg_ranked_robin.yaml`](../bv2137_ywckmg_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Anderson

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/ywckmg) · **[results ↗](https://bettervoting.com/ywckmg/results)** (election `ywckmg` · test `BV2137`).

**Official tie-break (lot) order:** Anderson > Carter > Reagan — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the Center Squeeze election (BV2137, bvid ywckmg; BV-confirmed). 100 voters, three candidates, ONE ranked electorate tabulated four ways. Anderson is the Condorcet winner (beats Reagan 55–45, Carter 65–35) but holds the fewest first-choices (20). Ranked Robin counts head-to-heads: Anderson beats BOTH rivals, so RR → Anderson — the Condorcet winner IRV threw away.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
45:Reagan>Anderson>Carter
20:Anderson>Carter>Reagan
35:Carter>Anderson>Reagan
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 100 ballots (ranked ballots).

Ballots:
    45 × Reagan > Anderson > Carter
    20 × Anderson > Carter > Reagan
    35 × Carter > Anderson > Reagan

Round-Robin — every pair, head-to-head (For – Against):
   Anderson  beats Reagan     55 – 45
   Carter    beats Reagan     55 – 45
   Anderson  beats Carter     65 – 35

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
             |    Reagan    |  Anderson   |   Carter    |
---------------------------------------------------------
    Reagan > |     ---      |45 -  0 - 55 |45 -  0 - 55 |
  Anderson > | 55 -  0 - 45 |    ---      |65 -  0 - 35 |
    Carter > | 55 -  0 - 45 |35 -  0 - 65 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Anderson   2–0–0         2     +40  Carter, Reagan
    2  Carter     1–1–0         1     -20  Reagan
    3  Reagan     0–2–0         0     -20  —

Winner — Ranked Robin (RCV-RR): Anderson
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Anderson
   Outside (2):        Reagan, Carter
   One member ⇒ Anderson is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Anderson is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2137_ywckmg_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/center_squeeze_bv2137/cases/bv2137_ywckmg_ranked_robin.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../07_Concepts/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2137_ywckmg_irv](bv2137_ywckmg_irv.md) · [bv2137_ywckmg_star](bv2137_ywckmg_star.md) · [bv2137_ywckmg_stv](bv2137_ywckmg_stv.md)
