---
search:
  exclude: true
---

# Reinforcement — Combined, Cara branch (9 voters; both halves say Cara, the whole says Ben)

*Generated from [`reinf_combined_cara_c3_b9_rr.yaml`](../reinf_combined_cara_c3_b9_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn) · **1 seat** · **Expected winner:** Ben

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

North (6 voters, the symmetric cycle) merged with the CARA-branch South
(reinf_south_cara_c3_b3_rr.yaml). Cara is a co-winner of North's three-way tie
and the outright Condorcet winner of South — a winner in both halves — so
reinforcement (consistency) demands Cara win the union.

She doesn't. A NEW Condorcet winner appears in the merged electorate:

    Ben beats Ada 5–4 · Ben beats Cara 5–4 · Cara beats Ada 7–2

so every Condorcet method elects BEN. Rotated one more step from the Ben branch,
and the mechanism is identical: the two 5–4 pairwise majorities that decide the
merged election exist in neither half by itself. Head-to-head majorities are not
additive across electorates, and that non-additivity is precisely what Zwicker's
Proposition 2.5 turns into an impossibility — no Condorcet extension is
reinforcing, at any number of candidates from three up.

Branch companions: reinf_combined_c3_b9_rr.yaml (Ada branch → Cara wins),
reinf_combined_ben_c3_b9_rr.yaml (Ben branch → Ada wins).

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ada>Ben>Cara
3:Ben>Cara>Ada
2:Cara>Ada>Ben
2:Cara>Ben>Ada
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 9 ballots (ranked ballots).

Ballots:
     2 × Ada > Ben > Cara
     3 × Ben > Cara > Ada
     2 × Cara > Ada > Ben
     2 × Cara > Ben > Ada

Round-Robin — every pair, head-to-head (For – Against):
   Ben   beats Ada    5 – 4
   Cara  beats Ada    7 – 2
   Ben   beats Cara   5 – 4

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |4 - 0 - 5 |2 - 0 - 7 |
   Ben > | 5 - 0 - 4 |   ---    |5 - 0 - 4 |
  Cara > | 7 - 0 - 2 |4 - 0 - 5 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ben        2–0–0         2      +2  Cara, Ada
    2  Cara       1–1–0         1      +4  Ada
    3  Ada        0–2–0         0      -6  —

Winner — Ranked Robin (RCV-RR): Ben
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Ben
   Outside (2):        Ada, Cara
   One member ⇒ Ben is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Ben is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/reinf_combined_cara_c3_b9_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/reinforcement_paradox/cases/reinf_combined_cara_c3_b9_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [reinf_combined_ben_c3_b9_rr](reinf_combined_ben_c3_b9_rr.md) · [reinf_combined_c3_b9_rr](reinf_combined_c3_b9_rr.md) · [reinf_combined_c3_b9_star](reinf_combined_c3_b9_star.md) · [reinf_north_c3_b6_rr](reinf_north_c3_b6_rr.md) · [reinf_south_ben_c3_b3_rr](reinf_south_ben_c3_b3_rr.md) · [reinf_south_c3_b3_rr](reinf_south_c3_b3_rr.md) · [reinf_south_cara_c3_b3_rr](reinf_south_cara_c3_b3_rr.md)
