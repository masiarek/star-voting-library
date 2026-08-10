---
search:
  exclude: true
---

# Ranked Robin — a dead heat that runs the whole tiebreak ladder (LH-only)

*Generated from [`dead_heat_lot_tiebreak.yaml`](../dead_heat_lot_tiebreak.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../01_Learn/README.md) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

4 score ballots, 3 candidates. Ada and Ben are a perfect head-to-head TIE: two voters score them EQUAL (Equal Support — no preference), the other two split one each, so the matchup is 1-1. Both beat Cara outright. So Ada and Ben each go 1-0-1 (Copeland 1.5) AND their total margins are identical (+4). Ranked Robin walks the FULL tiebreak ladder — most wins (tie) -> total margin (tie) -> lot order — and only the pre-published lot [Ada, Ben, Cara] settles it, in Ada's favor. Showcases the Equal Support column and the +1/2 Copeland credit that no other case in the set exercises.
LH-ONLY ON PURPOSE. This case is exactly where the LH and BetterVoting tiebreak rules DIVERGE. LH: most wins -> margin -> lot (fully deterministic). BetterVoting RankedRobin.ts: most wins -> head-to-head (2-way only) -> RANDOM. Here the two leaders tie each other head-to-head too, so BV would fall through to a random pick — un-freezable — which is why there is no BV election for this case. See 05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ada,Ben,Cara
5,5,0
5,5,0
4,3,1
3,4,1
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 4 ballots (score ballots).

Ballots:
   the ranking Ranked Robin reads ("=" = tied); source scores follow in () per column: Ada, Ben, Cara
     2 × Ada=Ben > Cara      (5, 5, 0)
     1 × Ada > Ben > Cara      (4, 3, 1)
     1 × Ben > Ada > Cara      (3, 4, 1)

Round-Robin — every pair, head-to-head (For – Against):
   Ada   ties  Ben    1 – 1
   Ada   beats Cara   4 – 0
   Ben   beats Cara   4 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |1 - 2 - 1 |4 - 0 - 0 |
   Ben > | 1 - 2 - 1 |   ---    |4 - 0 - 0 |
  Cara > | 0 - 0 - 4 |0 - 0 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–0–1       1.5      +4  Cara
    2  Ben        1–0–1       1.5      +4  Cara
    3  Cara       0–2–0         0      -8  —

Winner — Ranked Robin (RCV-RR): Ada
   *** 2 candidates tie on the highest Copeland score (1.5): Ada, Ben — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (2 of 3): Ada, Ben
   Outside (1):        Cara
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   dead heat (its members DRAW each other head-to-head), so the strongest
   "candidate" is a set, not a person. No member beats another, so there is no
   loop for Minimax / Ranked Pairs / Schulze to disagree about — which member
   wins is left to the tiebreak, not to a cycle rule. See
   05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md.
   Ranked Robin (RCV-RR) winner Ada is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   Fine print: this set contains a pairwise DRAW, and a draw is enough to keep a
   candidate in the Smith set but not in the tighter Schwartz set — so Schwartz
   may be smaller here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/dead_heat_lot_tiebreak_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/03_Criteria/rr_tiebreaks/cases/dead_heat_lot_tiebreak.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2141_3r3yf7_four_degree_tie](bv2141_3r3yf7_four_degree_tie.md) · [bv2261_y2fbpc_tiebreak_recorded_cycle](bv2261_y2fbpc_tiebreak_recorded_cycle.md) · [bv2261_y2fbpc_tiebreak_recorded_draws](bv2261_y2fbpc_tiebreak_recorded_draws.md) · [bv2262_2gvwr9_nine_way_dead_heat](bv2262_2gvwr9_nine_way_dead_heat.md) · [bv2270_8h4bvh_head_to_head_vs_margin](bv2270_8h4bvh_head_to_head_vs_margin.md)
