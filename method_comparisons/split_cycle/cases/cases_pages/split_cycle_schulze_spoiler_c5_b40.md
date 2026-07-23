# A candidate nobody prefers still flips the winner — Schulze's spoiler, and Split Cycle's immunity

*Generated from [`split_cycle_schulze_spoiler_c5_b40.yaml`](../split_cycle_schulze_spoiler_c5_b40.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Cascade

**Official tie-break (lot) order:** Arches > Bryce > Cascade > Denali > Everglade — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

A runnable counterexample for Holliday & Pacuit's central claim in "Split Cycle"
(arXiv:2004.02350; Public Choice 197, 2023): that Schulze/beat-path is NOT immune
to spoilers, and Split Cycle is. Reproduced independently — this is not the
paper's own profile — with pref_voting, on the smallest electorate a search
turned up. 40 hikers rank five national parks.

Cascade beats Bryce 40-0: NOT ONE VOTER prefers Bryce to Cascade. Bryce wins
under no method, in any field. And yet:

    Schulze WITHOUT Bryce on the ballot  ->  Cascade
    Schulze WITH    Bryce on the ballot  ->  Everglade

Bryce's mere presence takes the win away from a park she is unanimously behind,
and hands it to a third party. That is exactly the paper's Definition 4.1: Bryce
spoils the election for Cascade — Cascade wins without Bryce, a majority (here,
everyone) prefers Cascade to Bryce, and with Bryce present neither of them wins.

Split Cycle does not do this. It returns {Cascade, Everglade} with Bryce present
and {Cascade} without — Cascade is never dropped, so no spoiler effect occurs.
That is the paper's "stability for winners" in action, and the reason the authors
argue the criterion is worth the cost (Split Cycle sometimes declines to break a
tie that Schulze and Ranked Pairs break by convention).

Read the honest fine print on the lesson page: this is a five-candidate profile
with no Condorcet winner and a Smith set of ALL FIVE parks — a genuinely knotted
election, not an everyday one. Ranked Pairs happens to elect Cascade here too, so
this profile does not exhibit its (separately proven) spoiler failure. Nothing
here is evidence about STAR or Ranked Robin, neither of which is a C2 method.

Verified with pref_voting, both fields:
  uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py \
    method_comparisons/split_cycle/cases/split_cycle_schulze_spoiler_c5_b40.yaml
  uv run …/cycle_resolution_report.py …/split_cycle_schulze_spoiler_c5_b40.yaml --drop Bryce

LH-only (no BetterVoting election): neither BV nor the LH engine implements
Schulze or Split Cycle, and the LH Copeland result here is a tie. Lesson page:
00_start_here/topics/condorcet/split_cycle.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
11:Everglade>Denali>Cascade>Bryce>Arches
11:Arches>Denali>Cascade>Everglade>Bryce
8:Everglade>Cascade>Bryce>Arches>Denali
10:Cascade>Bryce>Arches>Denali>Everglade
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/split_cycle_schulze_spoiler_c5_b40_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 40 ballots (ranked ballots).

Ballots:
    11 × Everglade > Denali > Cascade > Bryce > Arches
    11 × Arches > Denali > Cascade > Everglade > Bryce
     8 × Everglade > Cascade > Bryce > Arches > Denali
    10 × Cascade > Bryce > Arches > Denali > Everglade

Round-Robin — every pair, head-to-head (For – Against):
   Denali     beats Everglade   21 – 19
   Cascade    beats Everglade   21 – 19
   Everglade  beats Bryce       30 – 10
   Arches     beats Everglade   21 – 19
   Denali     beats Cascade     22 – 18
   Denali     beats Bryce       22 – 18
   Arches     beats Denali      29 – 11
   Cascade    beats Bryce       40 –  0
   Cascade    beats Arches      29 – 11
   Bryce      beats Arches      29 – 11

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
              |  Everglade   |   Denali    |  Cascade    |   Bryce     |   Arches    |
--------------------------------------------------------------------------------------
  Everglade > |     ---      |19 -  0 - 21 |19 -  0 - 21 |30 -  0 - 10 |19 -  0 - 21 |
     Denali > | 21 -  0 - 19 |    ---      |22 -  0 - 18 |22 -  0 - 18 |11 -  0 - 29 |
    Cascade > | 21 -  0 - 19 |18 -  0 - 22 |    ---      |40 -  0 -  0 |29 -  0 - 11 |
      Bryce > | 10 -  0 - 30 |18 -  0 - 22 | 0 -  0 - 40 |    ---      |29 -  0 - 11 |
     Arches > | 21 -  0 - 19 |29 -  0 - 11 |11 -  0 - 29 |11 -  0 - 29 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Cascade    3–1–0         3     +56  Arches, Everglade, Bryce
    2  Denali     3–1–0         3      -8  Cascade, Everglade, Bryce
    3  Arches     2–2–0         2     -16  Denali, Everglade
    4  Everglade  1–3–0         1     +14  Bryce
    5  Bryce      1–3–0         1     -46  Arches

Winner — Ranked Robin (RCV-RR): Cascade
   *** 2 candidates tie for the most wins (Denali, Cascade) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/split_cycle/cases/split_cycle_schulze_spoiler_c5_b40.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
