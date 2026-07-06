# Ranked Robin — a dead heat that runs the whole tiebreak ladder (LH-only)

*Generated from [`dead_heat_lot_tiebreak.yaml`](../dead_heat_lot_tiebreak.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

4 score ballots, 3 candidates. Ada and Ben are a perfect head-to-head TIE: two voters score them EQUAL (Equal Support — no preference), the other two split one each, so the matchup is 1-1. Both beat Cara outright. So Ada and Ben each go 1-0-1 (Copeland 1.5) AND their total margins are identical (+4). Ranked Robin walks the FULL tiebreak ladder — most wins (tie) -> total margin (tie) -> lot order — and only the pre-published lot [Ada, Ben, Cara] settles it, in Ada's favor. Showcases the Equal Support column and the +1/2 Copeland credit that no other case in the set exercises.
LH-ONLY ON PURPOSE. This case is exactly where the LH and BetterVoting tiebreak rules DIVERGE. LH: most wins -> margin -> lot (fully deterministic). BetterVoting RankedRobin.ts: most wins -> head-to-head (2-way only) -> RANDOM. Here the two leaders tie each other head-to-head too, so BV would fall through to a random pick — un-freezable — which is why there is no BV election for this case. See 00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md.

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

Full report from the [`_tabulated` mirror](../rr_tiebreaks_tabulated/dead_heat_lot_tiebreak_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–0–1       1.5      +4  Cara
    2  Ben        1–0–1       1.5      +4  Cara
    3  Cara       0–2–0         0      -8  —

Winner — Ranked Robin (RCV-RR): Ada
   *** 2 candidates tie for the most wins (Ada, Ben) — a dead heat (they draw head-to-head, not a cycle). Resolved by total margin, then lot order.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/rr_tiebreaks/dead_heat_lot_tiebreak.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../method_comparisons/split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)
