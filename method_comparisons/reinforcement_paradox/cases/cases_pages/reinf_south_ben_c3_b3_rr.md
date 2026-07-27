# Reinforcement — South district, Ben branch (3 voters, Ben is the clear Condorcet winner)

*Generated from [`reinf_south_ben_c3_b3_rr.yaml`](../reinf_south_ben_c3_b3_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Ben

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

A rotated companion to reinf_south_c3_b3_rr.yaml, built to complete the case
analysis in Zwicker's proof of Proposition 2.5 ("all Condorcet extension SCFs
for three or more alternatives violate reinforcement").

North (reinf_north_c3_b6_rr.yaml) is the perfectly symmetric 6-voter cycle, so
an anonymous, neutral rule can only call it a three-way tie: every candidate is
a co-winner. But a RESOLUTE engine — like the LH tabulator, which spends
neutrality on a published lot order — must name exactly one of them. Which one
it names decides which South district is needed to spring the contradiction.

North is invariant under the rotation Ada→Ben→Cara→Ada, so rotating the
original South gives the branch for each possible North winner. This file is the
BEN branch: Ben beats both rivals head-to-head here —

    Ben beats Ada 2–1 · Ben beats Cara 3–0 · Ada beats Cara 3–0

so every method elects Ben. Ben is also a co-winner of North's dead heat, so
reinforcement demands Ben win the merged 9-voter election. He doesn't — ADA does
(see reinf_combined_ben_c3_b9_rr.yaml). The contradiction fires no matter which
way the cycle is resolved; that is the whole content of the proposition.

Branch companions: reinf_south_c3_b3_rr.yaml (Ada branch → combined elects Cara),
reinf_south_cara_c3_b3_rr.yaml (Cara branch → combined elects Ben).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ben>Ada>Cara
1:Ada>Ben>Cara
```

## What the engine says

Full report from the [`_tabulated` mirror](../cases_tabulated/reinf_south_ben_c3_b3_rr_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (ranked ballots).

Ballots:
     2 × Ben > Ada > Cara
     1 × Ada > Ben > Cara

Round-Robin — every pair, head-to-head (For – Against):
   Ben   beats Ada    2 – 1
   Ben   beats Cara   3 – 0
   Ada   beats Cara   3 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ben    |   Ada    |  Cara    |
--------------------------------------------
   Ben > |    ---    |2 - 0 - 1 |3 - 0 - 0 |
   Ada > | 1 - 0 - 2 |   ---    |3 - 0 - 0 |
  Cara > | 0 - 0 - 3 |0 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ben        2–0–0         2      +4  Ada, Cara
    2  Ada        1–1–0         1      +2  Cara
    3  Cara       0–2–0         0      -6  —

Winner — Ranked Robin (RCV-RR): Ben
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reinforcement_paradox/cases/reinf_south_ben_c3_b3_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [reinf_combined_ben_c3_b9_rr](reinf_combined_ben_c3_b9_rr.md) · [reinf_combined_c3_b9_rr](reinf_combined_c3_b9_rr.md) · [reinf_combined_c3_b9_star](reinf_combined_c3_b9_star.md) · [reinf_combined_cara_c3_b9_rr](reinf_combined_cara_c3_b9_rr.md) · [reinf_north_c3_b6_rr](reinf_north_c3_b6_rr.md) · [reinf_south_c3_b3_rr](reinf_south_c3_b3_rr.md) · [reinf_south_cara_c3_b3_rr](reinf_south_cara_c3_b3_rr.md)
