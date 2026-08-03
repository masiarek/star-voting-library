---
search:
  exclude: true
---

# P3 manipulated — Zwicker's complete reversal makes Dublin a 4-0 Condorcet winner

*Generated from [`p3_manip_reversal_rr.yaml`](../p3_manip_reversal_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** Dublin

**Official tie-break (lot) order:** Athens > Bergen > Cork > Dublin > Edinburgh — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The book's own printed manipulation. One of the two sincere Athens>Bergen>Cork>Dublin>Edinburgh voters completely REVERSES their ballot to Edinburgh>Dublin>Cork>Bergen>Athens. That single reversed ballot flips two knife-edge 4-3 contests (Athens vs Dublin and Cork vs Dublin), and Dublin goes from 2-2 to 4-0: a symmetric Copeland score of +4, the maximum possible for five candidates, and now an outright Condorcet winner. The manipulator has replaced their LAST choice (Edinburgh) with their 4th (Dublin) — a strict gain — by submitting a ballot that misrepresents every single pairwise preference they hold. IMPORTANT for this repo: Ranked Robin IS Copeland plus a tiebreak, so the book's showcase manipulation is a manipulation of a method this library advocates.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Edinburgh>Cork>Athens>Dublin>Bergen
3:Dublin>Edinburgh>Bergen>Cork>Athens
1:Athens>Bergen>Cork>Dublin>Edinburgh
1:Edinburgh>Dublin>Cork>Bergen>Athens
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     2 × Edinburgh > Cork > Athens > Dublin > Bergen
     3 × Dublin > Edinburgh > Bergen > Cork > Athens
     1 × Athens > Bergen > Cork > Dublin > Edinburgh
     1 × Edinburgh > Dublin > Cork > Bergen > Athens

Round-Robin — every pair, head-to-head (For – Against):
   Edinburgh  beats Cork        6 – 1
   Edinburgh  beats Athens      6 – 1
   Dublin     beats Edinburgh   4 – 3
   Edinburgh  beats Bergen      6 – 1
   Cork       beats Athens      6 – 1
   Dublin     beats Cork        4 – 3
   Bergen     beats Cork        4 – 3
   Dublin     beats Athens      4 – 3
   Bergen     beats Athens      4 – 3
   Dublin     beats Bergen      6 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
              |  Edinburgh  |   Cork     |  Athens    |  Dublin    |  Bergen    |
---------------------------------------------------------------------------------
  Edinburgh > |     ---     | 6 - 0 - 1  | 6 - 0 - 1  | 3 - 0 - 4  | 6 - 0 - 1  |
       Cork > |  1 - 0 - 6  |    ---     | 6 - 0 - 1  | 3 - 0 - 4  | 3 - 0 - 4  |
     Athens > |  1 - 0 - 6  | 1 - 0 - 6  |    ---     | 3 - 0 - 4  | 3 - 0 - 4  |
     Dublin > |  4 - 0 - 3  | 4 - 0 - 3  | 4 - 0 - 3  |    ---     | 6 - 0 - 1  |
     Bergen > |  1 - 0 - 6  | 4 - 0 - 3  | 4 - 0 - 3  | 1 - 0 - 6  |    ---     |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Dublin     4–0–0         4      +8  Edinburgh, Bergen, Cork, Athens
    2  Edinburgh  3–1–0         3     +14  Bergen, Cork, Athens
    3  Bergen     2–2–0         2      -8  Cork, Athens
    4  Cork       1–3–0         1      -2  Athens
    5  Athens     0–4–0         0     -12  —

Winner — Ranked Robin (RCV-RR): Dublin
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 5): Dublin
   Outside (4):        Edinburgh, Cork, Athens, Bergen
   One member ⇒ Dublin is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Dublin is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/p3_manip_reversal_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/manipulability_p3/cases/p3_manip_reversal_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [p3_manip_compromise_rr](p3_manip_compromise_rr.md) · [p3_manip_star](p3_manip_star.md) · [p3_sincere_ranked_robin](p3_sincere_ranked_robin.md) · [p3_sincere_star](p3_sincere_star.md)
