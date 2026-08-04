---
search:
  exclude: true
---

# Reinforcement — South district alone (3 voters, Ada is the clear Condorcet winner)

*Generated from [`reinf_south_c3_b3_rr.yaml`](../reinf_south_c3_b3_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

District 2 of the reinforcement-paradox pair from Brandt, Dong & Peters,
"Condorcet-Consistent Choice Among Three Candidates" (2024), Theorem 2 (the
profile P2). Three voters, and Ada beats both rivals head-to-head:

    Ada beats Cara 2–1 · Ada beats Ben 3–0 · Cara beats Ben 3–0

So Ada is the Condorcet winner and every method elects her here. Combined with
North (a dead tie in which Ada is also a co-winner), reinforcement/consistency
demands that Ada win the merged 9-voter election too — but she doesn't. See the
folder README.

Companion cases: reinf_north_c3_b6_rr.yaml (a 3-way tie),
reinf_combined_c3_b9_rr.yaml and reinf_combined_c3_b9_star.yaml (Cara wins).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ada>Cara>Ben
1:Cara>Ada>Ben
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (ranked ballots).

Ballots:
     2 × Ada > Cara > Ben
     1 × Cara > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Cara   2 – 1
   Ada   beats Ben    3 – 0
   Cara  beats Ben    3 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |  Cara    |   Ben    |
--------------------------------------------
   Ada > |    ---    |2 - 0 - 1 |3 - 0 - 0 |
  Cara > | 1 - 0 - 2 |   ---    |3 - 0 - 0 |
   Ben > | 0 - 0 - 3 |0 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +4  Cara, Ben
    2  Cara       1–1–0         1      +2  Ben
    3  Ben        0–2–0         0      -6  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Ada
   Outside (2):        Cara, Ben
   One member ⇒ Ada is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Ada is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reinf_south_c3_b3_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reinforcement_paradox/cases/reinf_south_c3_b3_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [reinf_combined_ben_c3_b9_rr](reinf_combined_ben_c3_b9_rr.md) · [reinf_combined_c3_b9_rr](reinf_combined_c3_b9_rr.md) · [reinf_combined_c3_b9_star](reinf_combined_c3_b9_star.md) · [reinf_combined_cara_c3_b9_rr](reinf_combined_cara_c3_b9_rr.md) · [reinf_north_c3_b6_rr](reinf_north_c3_b6_rr.md) · [reinf_south_ben_c3_b3_rr](reinf_south_ben_c3_b3_rr.md) · [reinf_south_cara_c3_b3_rr](reinf_south_cara_c3_b3_rr.md)
