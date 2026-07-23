# A cycle Copeland can't break — three trails tie 1-1, and the refined rules all rescue Alder

*Generated from [`cycle_copeland_ties_c4_b21.yaml`](../cycle_copeland_ties_c4_b21.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Alder

**Official tie-break (lot) order:** Alder > Birch > Cedar > Dogwood — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The first worked profile from "Cycle Resolution — why Minimax, Ranked Pairs,
and Schulze exist" (00_start_here/RCV_Ranked_Robin/cycle_resolution.md), now
runnable. 21 hikers rank four trails; Dogwood is everyone's last choice, and
the other three form a majority CYCLE:

    Alder beats Birch by 9 · Birch beats Cedar by 11 · Cedar beats Alder by 1

So there is no Condorcet winner, and Ranked Robin's underlying Copeland count
(pairwise wins minus losses) ties Alder, Birch and Cedar at +1 each — the
simple count cannot pick. That tie-proneness is exactly why the refined
cycle-resolution rules exist.

Every one of them then agrees on Alder, whose only defeat (to Cedar, by 1) is
the mildest loss in the cycle: Minimax picks Alder ("least badly beaten"),
Ranked Pairs locks Birch>Cedar and Alder>Birch and skips the cycle-closing
Cedar>Alder, Schulze's strongest beat-paths run Alder's way, and Split Cycle
discards the weakest defeat in the cycle — Cedar>Alder — leaving Alder
undefeated. Four different philosophies, one winner.

Verified with pref_voting:
  uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py \
    method_comparisons/cycle_resolution/cases/cycle_copeland_ties_c4_b21.yaml

LH-only (no BetterVoting election): LH and BV break a Copeland tie differently
— LH by margin then lot, BV at random — so a tie-deciding case cannot be frozen
on BV. The companion case where the refined rules DISAGREE:
cycle_schulze_vs_ranked_pairs_c4_b40.yaml

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
10:Alder>Birch>Cedar>Dogwood
6:Birch>Cedar>Alder>Dogwood
5:Cedar>Alder>Birch>Dogwood
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/cycle_copeland_ties_c4_b21_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 21 ballots (ranked ballots).

Ballots:
    10 × Alder > Birch > Cedar > Dogwood
     6 × Birch > Cedar > Alder > Dogwood
     5 × Cedar > Alder > Birch > Dogwood

Round-Robin — every pair, head-to-head (For – Against):
   Alder    beats Birch     15 –  6
   Cedar    beats Alder     11 – 10
   Alder    beats Dogwood   21 –  0
   Birch    beats Cedar     16 –  5
   Birch    beats Dogwood   21 –  0
   Cedar    beats Dogwood   21 –  0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
            |    Alder     |   Birch     |   Cedar     |  Dogwood    |
----------------------------------------------------------------------
    Alder > |     ---      |15 -  0 -  6 |10 -  0 - 11 |21 -  0 -  0 |
    Birch > |  6 -  0 - 15 |    ---      |16 -  0 -  5 |21 -  0 -  0 |
    Cedar > | 11 -  0 - 10 | 5 -  0 - 16 |    ---      |21 -  0 -  0 |
  Dogwood > |  0 -  0 - 21 | 0 -  0 - 21 | 0 -  0 - 21 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Alder      2–1–0         2     +29  Birch, Dogwood
    2  Birch      2–1–0         2     +23  Cedar, Dogwood
    3  Cedar      2–1–0         2     +11  Alder, Dogwood
    4  Dogwood    0–3–0         0     -63  —

Winner — Ranked Robin (RCV-RR): Alder
   *** 3 candidates tie for the most wins (Alder, Birch, Cedar) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/cycle_resolution/cases/cycle_copeland_ties_c4_b21.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [cycle_schulze_vs_ranked_pairs_c4_b40](cycle_schulze_vs_ranked_pairs_c4_b40.md)
