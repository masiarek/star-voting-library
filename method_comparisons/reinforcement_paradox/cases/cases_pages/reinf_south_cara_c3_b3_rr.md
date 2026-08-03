---
search:
  exclude: true
---

# Reinforcement — South district, Cara branch (3 voters, Cara is the clear Condorcet winner)

*Generated from [`reinf_south_cara_c3_b3_rr.yaml`](../reinf_south_cara_c3_b3_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** Cara

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The third and last branch of the case analysis in Zwicker's proof of
Proposition 2.5 ("all Condorcet extension SCFs for three or more alternatives
violate reinforcement"), completing reinf_south_c3_b3_rr.yaml (Ada branch) and
reinf_south_ben_c3_b3_rr.yaml (Ben branch).

North (reinf_north_c3_b6_rr.yaml) is the perfectly symmetric 6-voter cycle: an
anonymous, neutral rule can only call it a three-way tie, but a RESOLUTE engine
must name one winner. North is invariant under the rotation Ada→Ben→Cara→Ada, so
rotating South twice gives the branch for a North winner of Cara. Here —

    Cara beats Ben 2–1 · Cara beats Ada 3–0 · Ben beats Ada 3–0

so Cara is the Condorcet winner and every method elects her. Cara is also a
co-winner of North's dead heat, so reinforcement demands Cara win the merged
9-voter election. She doesn't — BEN does (reinf_combined_cara_c3_b9_rr.yaml).

With all three branches built, the demonstration no longer depends on which
candidate the cycle happens to resolve to: whichever one it is, there is a South
district that agrees with it and a merged electorate that overturns it.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Cara>Ben>Ada
1:Ben>Cara>Ada
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (ranked ballots).

Ballots:
     2 × Cara > Ben > Ada
     1 × Ben > Cara > Ada

Round-Robin — every pair, head-to-head (For – Against):
   Cara  beats Ben    2 – 1
   Cara  beats Ada    3 – 0
   Ben   beats Ada    3 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |   Cara    |   Ben    |   Ada    |
--------------------------------------------
  Cara > |    ---    |2 - 0 - 1 |3 - 0 - 0 |
   Ben > | 1 - 0 - 2 |   ---    |3 - 0 - 0 |
   Ada > | 0 - 0 - 3 |0 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Cara       2–0–0         2      +4  Ben, Ada
    2  Ben        1–1–0         1      +2  Ada
    3  Ada        0–2–0         0      -6  —

Winner — Ranked Robin (RCV-RR): Cara
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Cara
   Outside (2):        Ben, Ada
   One member ⇒ Cara is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Cara is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reinf_south_cara_c3_b3_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reinforcement_paradox/cases/reinf_south_cara_c3_b3_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [reinf_combined_ben_c3_b9_rr](reinf_combined_ben_c3_b9_rr.md) · [reinf_combined_c3_b9_rr](reinf_combined_c3_b9_rr.md) · [reinf_combined_c3_b9_star](reinf_combined_c3_b9_star.md) · [reinf_combined_cara_c3_b9_rr](reinf_combined_cara_c3_b9_rr.md) · [reinf_north_c3_b6_rr](reinf_north_c3_b6_rr.md) · [reinf_south_ben_c3_b3_rr](reinf_south_ben_c3_b3_rr.md) · [reinf_south_c3_b3_rr](reinf_south_c3_b3_rr.md)
