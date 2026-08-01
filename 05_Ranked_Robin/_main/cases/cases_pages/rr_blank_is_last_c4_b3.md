---
search:
  exclude: true
---

# Ranked Robin — a blank is ranked LAST (and rank numbers don't matter)

*Generated from [`rr_blank_is_last_c4_b3.yaml`](../rr_blank_is_last_c4_b3.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../concepts) · **1 seat** · **Expected winner:** Ada

**Official tie-break (lot) order:** Ada > Ben > Cara > Dan — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

A tiny teaching case for the question that trips up newcomers: on a Ranked Robin
ballot, what happens to a candidate you leave BLANK — and does it matter whether
you rank your worst choice "last" or just leave them blank?

Answer: a blank is ranked below every candidate you DID rank, and it makes no
difference to the count whether you write that candidate in the last tier or
leave them blank. Ranked Robin reads only the PREFERENCE ORDER on each ballot,
never the numeric rank label — so "5th vs 6th vs blank" is a distinction without
a difference. Here Dan is ranked explicitly last by voter 1 and left blank by
voters 2 and 3, yet he is treated identically (dead last) in every head-to-head:
he loses all three pairwise contests 3–0. Ada beats everyone (the Condorcet
winner), so Ada wins outright.

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
- Dan
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
1:Ada>Ben>Cara>Dan
1:Ada>Cara>Ben
1:Ben>Ada>Cara
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 3 ballots (ranked ballots).

Ballots:
   Ada > Ben > Cara > Dan
   Ada > Cara > Ben
   Ben > Ada > Cara

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    2 – 1
   Ada   beats Cara   3 – 0
   Ada   beats Dan    3 – 0
   Ben   beats Cara   2 – 1
   Ben   beats Dan    3 – 0
   Cara  beats Dan    3 – 0

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |    Ada    |   Ben    |  Cara    |   Dan    |
-------------------------------------------------------
   Ada > |    ---    |2 - 0 - 1 |3 - 0 - 0 |3 - 0 - 0 |
   Ben > | 1 - 0 - 2 |   ---    |2 - 0 - 1 |3 - 0 - 0 |
  Cara > | 0 - 0 - 3 |1 - 0 - 2 |   ---    |3 - 0 - 0 |
   Dan > | 0 - 0 - 3 |0 - 0 - 3 |0 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        3–0–0         3      +7  Ben, Cara, Dan
    2  Ben        2–1–0         2      +3  Cara, Dan
    3  Cara       1–2–0         1      -1  Dan
    4  Dan        0–3–0         0      -9  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 4): Ada
   Outside (3):        Ben, Cara, Dan
   One member ⇒ Ada is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Ada is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/rr_blank_is_last_c4_b3_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/_main/cases/rr_blank_is_last_c4_b3.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [ranked_robin_consensus_center](ranked_robin_consensus_center.md)
