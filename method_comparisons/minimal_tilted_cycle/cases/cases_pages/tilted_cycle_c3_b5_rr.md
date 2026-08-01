---
search:
  exclude: true
---

# Minimal tilted cycle — 5 voters, margins 3–1–1 (Ranked Robin)

*Generated from [`tilted_cycle_c3_b5_rr.yaml`](../tilted_cycle_c3_b5_rr.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

The Fig. 1 profile from Brandt, Dong & Peters, "Condorcet-Consistent Choice
Among Three Candidates" (arXiv:2411.19857) — the SMALLEST electorate that can
produce a *tilted* (asymmetric) Condorcet cycle:

    Ada beats Ben   4–1   (margin +3)
    Ben beats Cara  3–2   (margin +1)
    Cara beats Ada  3–2   (margin +1)

Every voter here is perfectly transitive; the electorate is not. Copeland
(Ranked Robin) ties all three at 1–1 — the "three-way dead rung" shape — and
falls through to LH's margins tiebreak, which is ALIVE here (+2 / 0 / −2), so
Ada wins deterministically without a lot.

The tilt is what makes this profile useful: on the SYMMETRIC 6-voter cycle
(reinforcement_paradox/cases/reinf_north_c3_b6_rr.yaml) every Condorcet method
returns all three candidates and even the margins rung is dead. Tilt it by one
voter and Copeland STILL ties all three, while the maximin family (Minimax /
Ranked Pairs / Schulze / Kemeny — one and the same rule at three candidates)
drops Ben and returns {Ada, Cara}. That is the minimal proof that Ranked
Robin's Copeland count is NOT in the maximin family.

Why 5 voters and why 3–1–1: see the minimality proof in the folder README —
the three cyclic margins always sum to at most n and share n's parity, so
n = 3 forces the symmetric (1,1,1) cycle, n = 4 admits NO cycle at all, and
n = 5 leaves (3,1,1) as the only tilted shape in existence.

LH-only by design: the Copeland three-way tie is exactly the case where
BetterVoting breaks ties at RANDOM, so a BV result here could not be frozen.

Companion: tilted_cycle_c3_b5_irv.yaml (same ballots, RCV-IRV → Cara).

## Parameters (from the YAML)

```yaml
voting_method: RankedRobin
num_winners: 1
expected_winners:
- Ada
lot_numbers:
- Ada
- Ben
- Cara
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
2:Ada>Ben>Cara
1:Ben>Cara>Ada
2:Cara>Ada>Ben
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 5 ballots (ranked ballots).

Ballots:
     2 × Ada > Ben > Cara
     1 × Ben > Cara > Ada
     2 × Cara > Ada > Ben

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    4 – 1
   Cara  beats Ada    3 – 2
   Ben   beats Cara   3 – 2

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |
--------------------------------------------
   Ada > |    ---    |4 - 0 - 1 |2 - 0 - 3 |
   Ben > | 1 - 0 - 4 |   ---    |3 - 0 - 2 |
  Cara > | 3 - 0 - 2 |2 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        1–1–0         1      +2  Ben
    2  Cara       1–1–0         1      +0  Ada
    3  Ben        1–1–0         1      -2  Cara

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie for the most wins (Ada, Ben, Cara) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/concepts/cycle_resolution.md.)
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 3): Ada, Ben, Cara
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Ada is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/tilted_cycle_c3_b5_rr_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minimal_tilted_cycle/cases/tilted_cycle_c3_b5_rr.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [tilted_cycle_c3_b5_irv](tilted_cycle_c3_b5_irv.md)
