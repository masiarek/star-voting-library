---
search:
  exclude: true
---

# Exercise 9 — Game night: nobody is unbeatable (a Ranked Robin ladder drill)

*Generated from [`ex09_game_night_cycle.yaml`](../ex09_game_night_cycle.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** Azul

**Official tie-break (lot) order:** Azul > Boggle > Catan > Dominion — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Ten friends rank four board games. Azul beats Boggle 7-3, Boggle beats
Catan 7-3, Catan beats Azul 6-4 — a rock-paper-scissors cycle, so there
is NO Condorcet winner — and everything beats Dominion 10-0. Ranked
Robin walks its ladder: most pairwise wins first (Azul, Boggle, and
Catan all tie at 2-1), then TOTAL WIN MARGIN: Azul +12, Boggle +10,
Catan +8 — Azul wins, deterministically, no lot needed. This is an
LH-only exercise on purpose: BetterVoting resolves a 3-way wins tie at
RANDOM (the BV2142 caveat), so a frozen BV result cannot exist.
Exercise: ex09_game_night_cycle.md. Ballots and cast are this repo's
own.

## Parameters (from the YAML)

```yaml
voting_method: RankedRobin
num_winners: 1
expected_winners:
- Azul
lot_numbers:
- Azul
- Boggle
- Catan
- Dominion
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Azul>Boggle>Catan>Dominion
Azul>Boggle>Catan>Dominion
Azul>Boggle>Catan>Dominion
Azul>Boggle>Catan>Dominion
Boggle>Catan>Azul>Dominion
Boggle>Catan>Azul>Dominion
Boggle>Catan>Azul>Dominion
Catan>Azul>Boggle>Dominion
Catan>Azul>Boggle>Dominion
Catan>Azul>Boggle>Dominion
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 10 ballots (ranked ballots).

Ballots:
     4 × Azul > Boggle > Catan > Dominion
     3 × Boggle > Catan > Azul > Dominion
     3 × Catan > Azul > Boggle > Dominion

Round-Robin — every pair, head-to-head (For – Against):
   Azul      beats Boggle      7 –  3
   Catan     beats Azul        6 –  4
   Azul      beats Dominion   10 –  0
   Boggle    beats Catan       7 –  3
   Boggle    beats Dominion   10 –  0
   Catan     beats Dominion   10 –  0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
             |     Azul     |   Boggle    |   Catan     |  Dominion   |
-----------------------------------------------------------------------
      Azul > |     ---      | 7 -  0 -  3 | 4 -  0 -  6 |10 -  0 -  0 |
    Boggle > |  3 -  0 -  7 |    ---      | 7 -  0 -  3 |10 -  0 -  0 |
     Catan > |  6 -  0 -  4 | 3 -  0 -  7 |    ---      |10 -  0 -  0 |
  Dominion > |  0 -  0 - 10 | 0 -  0 - 10 | 0 -  0 - 10 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Azul       2–1–0         2     +12  Boggle, Dominion
    2  Boggle     2–1–0         2     +10  Catan, Dominion
    3  Catan      2–1–0         2      +8  Azul, Dominion
    4  Dominion   0–3–0         0     -30  —

Winner — Ranked Robin (RCV-RR): Azul
   *** 3 candidates tie for the most wins (Azul, Boggle, Catan) — a Condorcet cycle (no candidate beats all others). Resolved by total margin, then lot order. (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/concepts/cycle_resolution.md.)
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (3 of 4): Azul, Boggle, Catan
   Outside (1):        Dominion
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/concepts/cycle_resolution.md.
   Ranked Robin (RCV-RR) winner Azul is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/ex09_game_night_cycle_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex09_game_night_cycle.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [ex01_district_combined](ex01_district_combined.md) · [ex01_district_east](ex01_district_east.md) · [ex01_district_west](ex01_district_west.md) · [ex02_bella_exits](ex02_bella_exits.md) · [ex02_nine_ballots](ex02_nine_ballots.md) · [ex02_tenth_ballot](ex02_tenth_ballot.md) · [ex03_five_verdicts](ex03_five_verdicts.md) · [ex04_olympics_1994](ex04_olympics_1994.md) · [ex05_center_squeeze](ex05_center_squeeze.md) · [ex06_bullet_backfire](ex06_bullet_backfire.md) · [ex06_bullet_honest](ex06_bullet_honest.md) · [ex07_vanishing_votes](ex07_vanishing_votes.md) · [ex08_minimal_reversal_2c](ex08_minimal_reversal_2c.md) · [ex08_minimal_reversal_3c](ex08_minimal_reversal_3c.md) · [ex10_generous](ex10_generous.md) · [ex10_reticent](ex10_reticent.md) · [ex11_spoiler_added](ex11_spoiler_added.md) · [ex11_two_way_base](ex11_two_way_base.md) · [ex12_bloc_sweep](ex12_bloc_sweep.md) · [ex12_proportional_share](ex12_proportional_share.md) · [ex13_approve3](ex13_approve3.md) · [ex13_approve4](ex13_approve4.md) · [ex13_bullet](ex13_bullet.md) · [ex13_opinions](ex13_opinions.md) · [ex14_two_novels](ex14_two_novels.md) · [ex14_two_novels_fullranks](ex14_two_novels_fullranks.md) · [ex15_approval_pairwise](ex15_approval_pairwise.md) · [ex15_approval_yes_no](ex15_approval_yes_no.md) · [ex15_score_profile](ex15_score_profile.md)
