---
search:
  exclude: true
---

# BV2209 — Burial in Ranked Robin (2/2): fifteen voters rank the leader last, and it pays

*Generated from [`bv2209_fxhw6g_burial_pays.yaml`](../bv2209_fxhw6g_burial_pays.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Amber

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/fxhw6g) · **[results ↗](https://bettervoting.com/fxhw6g/results)** (election `fxhw6g` · test `BV2209`).

## Scenario

The burial. Same 42 voters as part 1 (bv2208_7q6by8_burial_sincere.yaml), except the 15 Amber-first voters now rank Amber>Coral>Diamond>Beryl — burying Beryl, their honest SECOND choice, below two gems they like less. The mechanics: burial's reach is exactly the buriers' own weight inside the victim's coalitions. Beryl's 33-9 over Coral and 27-15 over Diamond both contained the buriers' 15 ballots, so withdrawing them flips both (Coral 24-18, Diamond 30-12). Her 27-15 over Amber contained none of them (they already ranked Amber first) — untouchable, which is why Amber can never beat Beryl DIRECTLY and must win through the record instead. The round-robin becomes a cycle with Amber and Coral tied on top at 2-1, and Amber takes the tie on EVERY metric: total pairwise margin +12 vs 0 (LH's rung), the direct head-to-head 27-15 (BV's rung), first choices 15 vs 9. The buriers turned Beryl's win into Amber's — and left fingerprints: a cycle where sincere ballots showed none. Burial needs a large coordinated bloc sitting inside the leader's own majorities, good polling, and a lie; the printed round-robin table is where you'd catch it. (Contrast BV2142: a THREE-way RR tie is random on BV — this pair stays freezable because a 2-way tie resolves by head-to-head, deterministically.) Triple-checked: LH native (margin rung), pref_voting Copeland-leader set {Amber, Coral}, BetterVoting live (Amber, tieBreakType none). Live results: https://bettervoting.com/fxhw6g/results

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
15:Amber>Coral>Diamond>Beryl
12:Beryl>Amber>Diamond>Coral
9:Coral>Diamond>Beryl>Amber
6:Diamond>Beryl>Coral>Amber
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 42 ballots (ranked ballots).

Ballots:
    15 × Amber > Coral > Diamond > Beryl
    12 × Beryl > Amber > Diamond > Coral
     9 × Coral > Diamond > Beryl > Amber
     6 × Diamond > Beryl > Coral > Amber

Round-Robin — every pair, head-to-head (For – Against):
   Amber    beats Coral     27 – 15
   Amber    beats Diamond   27 – 15
   Beryl    beats Amber     27 – 15
   Coral    beats Diamond   24 – 18
   Coral    beats Beryl     24 – 18
   Diamond  beats Beryl     30 – 12

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
            |    Amber     |   Coral     |  Diamond    |   Beryl     |
----------------------------------------------------------------------
    Amber > |     ---      |27 -  0 - 15 |27 -  0 - 15 |15 -  0 - 27 |
    Coral > | 15 -  0 - 27 |    ---      |24 -  0 - 18 |24 -  0 - 18 |
  Diamond > | 15 -  0 - 27 |18 -  0 - 24 |    ---      |30 -  0 - 12 |
    Beryl > | 27 -  0 - 15 |18 -  0 - 24 |12 -  0 - 30 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Amber      2–1–0         2     +12           +12  Coral, Diamond
    2  Coral      2–1–0         2      +0           -12  Diamond, Beryl
    3  Diamond    1–2–0         1      +0             —  Beryl
    4  Beryl      1–2–0         1     -12             —  Amber

Winner — Ranked Robin (RCV-RR): Amber
   *** 2 candidates tie for the most wins (Amber, Coral) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Amber has the greatest sum of win margins over the other finalists (+12).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): Amber, Coral, Diamond, Beryl
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Amber, Coral) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Amber is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2209_fxhw6g_burial_pays_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/burial/cases/bv2209_fxhw6g_burial_pays.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2208_7q6by8_burial_sincere](bv2208_7q6by8_burial_sincere.md)
