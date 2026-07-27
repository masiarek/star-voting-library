# Reinforcement — North district alone (6 voters, a perfect cycle)

*Generated from [`reinf_north_c3_b6_rr.yaml`](../reinf_north_c3_b6_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

District 1 of the reinforcement-paradox pair from Brandt, Dong & Peters,
"Condorcet-Consistent Choice Among Three Candidates" (2024), Theorem 2 —
the "double Condorcet cycle" P1. Six voters split evenly three ways, so the
three candidates form a perfect rock-paper-scissors tie:

    Ada beats Ben · Ben beats Cara · Cara beats Ada   (each 4–2)

Every method reports a three-way tie here (Ranked Robin's Copeland count ties
them 1–1 and falls to lot). The point of this district is only that **Ada is
among its winners** — which, with South (where Ada wins outright), is what sets
up the paradox when the two are combined. See the folder README.

Companion cases: reinf_south_c3_b3_rr.yaml (Ada wins outright),
reinf_combined_c3_b9_rr.yaml and reinf_combined_c3_b9_star.yaml (Cara wins).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ada>Ben>Cara
2:Ben>Cara>Ada
2:Cara>Ada>Ben
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/reinf_north_c3_b6_rr_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 6 ballots (ranked ballots).

Ballots:
     2 × Ada > Ben > Cara
     2 × Ben > Cara > Ada
     2 × Cara > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    4 – 2
   Cara  beats Ada    4 – 2
   Ben   beats Cara   4 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |4 - 0 - 2 |2 - 0 - 4 |
   Ben > | 2 - 0 - 4 |   ---    |4 - 0 - 2 |
  Cara > | 4 - 0 - 2 |2 - 0 - 4 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–1–0         1      +0  Ben
    2  Ben        1–1–0         1      +0  Cara
    3  Cara       1–1–0         1      +0  Ada

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie for the most wins (Ada, Ben, Cara) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 00_start_here/RCV_Ranked_Robin/cycle_resolution.md.)
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reinforcement_paradox/cases/reinf_north_c3_b6_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [reinf_combined_ben_c3_b9_rr](reinf_combined_ben_c3_b9_rr.md) · [reinf_combined_c3_b9_rr](reinf_combined_c3_b9_rr.md) · [reinf_combined_c3_b9_star](reinf_combined_c3_b9_star.md) · [reinf_combined_cara_c3_b9_rr](reinf_combined_cara_c3_b9_rr.md) · [reinf_south_ben_c3_b3_rr](reinf_south_ben_c3_b3_rr.md) · [reinf_south_c3_b3_rr](reinf_south_c3_b3_rr.md) · [reinf_south_cara_c3_b3_rr](reinf_south_cara_c3_b3_rr.md)
