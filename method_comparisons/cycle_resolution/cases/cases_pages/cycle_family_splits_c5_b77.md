---
search:
  exclude: true
---

# The whole Condorcet family splits — Minimax & Schulze pick Ava, Ranked Pairs picks Ben, on one set of ballots

*Generated from [`cycle_family_splits_c5_b77.yaml`](../cycle_family_splits_c5_b77.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/01_Learn/README.md) · **1 seat** · **Expected winner:** Ben

**Official tie-break (lot) order:** Ava > Ben > Cole > Dana > Ezra — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The five-candidate profile behind the "…but they don't always agree" table in
05_Ranked_Robin/01_Learn/cycle_resolution.md. 77 members of a program
committee rank five finalists, and majority preference is knotted about as
badly as it can be: there is no Condorcet winner and the Smith set is ALL FIVE
candidates — every finalist is in a beat-cycle with the rest.

On these identical ballots the Condorcet family gives four different answers:

    Copeland (Ranked Robin)  Ava, Ben   (tie — both go 2-2; the 1st Degree gives it to Ben)
    Minimax                  Ava
    Schulze (beat path)      Ava
    Ranked Pairs             Ben
    Split Cycle              Ava, Ben

Minimax and Schulze land on Ava (her worst defeat is the mildest); Ranked Pairs
locks the biggest margins first and they carry Ben; Copeland cannot separate the
two on the tally and hands it to Ben on its 1st Degree tiebreaker (Ben beat Ava
head-to-head, 40-37); Split Cycle deliberately returns both. That is the entire lesson of the
cycle-resolution page in one election: "Condorcet method" names a FAMILY, and
inside a cycle the family stops agreeing.

The LH engine tabulates the Copeland column (= Ranked Robin) and breaks the
Ava/Ben tie by Ranked Robin's own degrees — margins among the tied finalists
first, which for two finalists is their head-to-head — then margins over the
whole field, then lot. Until 2026-08-19 it started at the second of those and
reported Ava; see 05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md. The other four rules are printed by:
  uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py \
    method_comparisons/cycle_resolution/cases/cycle_family_splits_c5_b77.yaml

LH-only (no BetterVoting election): the result is a Copeland tie, and BV breaks
Copeland ties at random, so this can't be frozen on BV. Constructed by search
and verified with pref_voting (it is NOT a profile from the literature — an
earlier draft mis-attributed a 100-voter version to Heitzig; this replaces it
with a real, reproducible one). Companion: cycle_schulze_vs_ranked_pairs_c4_b40.yaml.

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
12:Ezra>Ava>Dana>Ben>Cole
7:Ezra>Cole>Ava>Dana>Ben
14:Ben>Ava>Ezra>Cole>Dana
8:Dana>Ben>Ava>Ezra>Cole
5:Cole>Ava>Dana>Ezra>Ben
11:Dana>Ben>Ava>Cole>Ezra
13:Ezra>Cole>Ava>Ben>Dana
7:Ben>Ava>Cole>Ezra>Dana
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 77 ballots (ranked ballots).

Ballots:
    12 × Ezra > Ava > Dana > Ben > Cole
     7 × Ezra > Cole > Ava > Dana > Ben
    14 × Ben > Ava > Ezra > Cole > Dana
     8 × Dana > Ben > Ava > Ezra > Cole
     5 × Cole > Ava > Dana > Ezra > Ben
    11 × Dana > Ben > Ava > Cole > Ezra
    13 × Ezra > Cole > Ava > Ben > Dana
     7 × Ben > Ava > Cole > Ezra > Dana

Round-Robin — every pair, head-to-head (For – Against):
   Ava   beats Ezra   45 – 32
   Ezra  beats Dana   53 – 24
   Ben   beats Ezra   40 – 37
   Ezra  beats Cole   54 – 23
   Ava   beats Dana   58 – 19
   Ben   beats Ava    40 – 37
   Ava   beats Cole   52 – 25
   Dana  beats Ben    43 – 34
   Cole  beats Dana   46 – 31
   Ben   beats Cole   52 – 25

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |     Ezra     |    Ava      |    Dana     |    Ben      |    Cole     |
---------------------------------------------------------------------------------
  Ezra > |     ---      |32 -  0 - 45 |53 -  0 - 24 |37 -  0 - 40 |54 -  0 - 23 |
   Ava > | 45 -  0 - 32 |    ---      |58 -  0 - 19 |37 -  0 - 40 |52 -  0 - 25 |
  Dana > | 24 -  0 - 53 |19 -  0 - 58 |    ---      |43 -  0 - 34 |31 -  0 - 46 |
   Ben > | 40 -  0 - 37 |40 -  0 - 37 |34 -  0 - 43 |    ---      |52 -  0 - 25 |
  Cole > | 23 -  0 - 54 |25 -  0 - 52 |46 -  0 - 31 |25 -  0 - 52 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Ben        3–1–0         3     +24            +3  Ava, Ezra, Cole
    2  Ava        3–1–0         3     +76            -3  Ezra, Cole, Dana
    3  Ezra       2–2–0         2     +44             —  Cole, Dana
    4  Cole       1–3–0         1     -70             —  Dana
    5  Dana       1–3–0         1     -74             —  Ben

Winner — Ranked Robin (RCV-RR): Ben
   *** 2 candidates tie for the most wins (Ava, Ben) — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Ben has the greatest sum of win margins over the other finalists (+3).
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (5 of 5): Ava, Ben, Ezra, Dana, Cole
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Ava, Ben) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   Ranked Robin (RCV-RR) winner Ben is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/cycle_family_splits_c5_b77_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/cycle_resolution/cases/cycle_family_splits_c5_b77.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../split_voting/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [cycle_copeland_ties_c4_b21](cycle_copeland_ties_c4_b21.md) · [cycle_schulze_vs_ranked_pairs_c4_b40](cycle_schulze_vs_ranked_pairs_c4_b40.md) · [cycle_vote_on_the_rule_irv_c5_b999](cycle_vote_on_the_rule_irv_c5_b999.md) · [cycle_vote_on_the_rule_rr_c5_b999](cycle_vote_on_the_rule_rr_c5_b999.md)
