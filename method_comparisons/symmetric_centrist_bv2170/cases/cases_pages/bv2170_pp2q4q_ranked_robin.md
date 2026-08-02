---
search:
  exclude: true
---

# Symmetric centrist (47/47/3/3) — Ranked Robin: elects Casey, beats everyone head-to-head

*Generated from [`bv2170_pp2q4q_ranked_robin.yaml`](../bv2170_pp2q4q_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../../05_Ranked_Robin/concepts) · **1 seat** · **Expected winner:** Casey

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/pp2q4q) · **[results ↗](https://bettervoting.com/pp2q4q/results)** (election `pp2q4q`).

**Official tie-break (lot) order:** Avery > Casey > Blake — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the Symmetric Centrist election (BV2170, bvid pp2q4q; BV-confirmed). 100 voters, three candidates, ONE electorate tabulated four ways. Avery is the left pole, Blake the right pole, Casey the centrist. Ranked Robin (Copeland) compares every pair head-to-head: Casey beats Avery 53–47 and Casey beats Blake 53–47, while Avery ties Blake 50–50. Casey wins both matchups (2–0) — the Condorcet winner — so Ranked Robin elects Casey directly and deterministically (no cycle, no tiebreak), agreeing with STAR and disagreeing with the center-squeeze methods IRV and Choose-One.

Live results: https://bettervoting.com/pp2q4q/results
Companion races: bv2170_pp2q4q_star.yaml, bv2170_pp2q4q_irv.yaml, bv2170_pp2q4q_plurality.yaml.
Overview page: bv2170_pp2q4q_symmetric_centrist.md

## Parameters (from the YAML)

```yaml
voting_method: RankedRobin
num_winners: 1
expected_winners: [Casey]
lot_numbers: [Avery, Casey, Blake]
bv_election_id: pp2q4q
bv_test_id: BV2170
```

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
47:Avery>Casey>Blake
47:Blake>Casey>Avery
3:Casey>Avery>Blake
3:Casey>Blake>Avery
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 100 ballots (ranked ballots).

Ballots:
    47 × Avery > Casey > Blake
    47 × Blake > Casey > Avery
     3 × Casey > Avery > Blake
     3 × Casey > Blake > Avery

Round-Robin — every pair, head-to-head (For – Against):
   Casey  beats Avery   53 – 47
   Avery  ties  Blake   50 – 50
   Casey  beats Blake   53 – 47

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |    Avery     |   Casey     |   Blake     |
------------------------------------------------------
  Avery > |     ---      |47 -  0 - 53 |50 -  0 - 50 |
  Casey > | 53 -  0 - 47 |    ---      |53 -  0 - 47 |
  Blake > | 50 -  0 - 50 |47 -  0 - 53 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Casey      2–0–0         2     +12  Avery, Blake
    2  Avery      0–1–1       0.5      -6  —
    3  Blake      0–1–1       0.5      -6  —

Winner — Ranked Robin (RCV-RR): Casey
   beats every opponent head-to-head — the Condorcet winner.
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (1 of 3): Casey
   Outside (2):        Avery, Blake
   One member ⇒ Casey is the Condorcet winner, beating every rival head-to-head.
   Ranked Robin (RCV-RR) winner Casey is INSIDE the Smith set. ✓
      Guaranteed: Ranked Robin (Copeland) is Smith-efficient — every member of
      the set outscores every outsider, so the top of the win–loss table is
      always inside the set, however the tie among them is then broken.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2170_pp2q4q_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/symmetric_centrist_bv2170/cases/bv2170_pp2q4q_ranked_robin.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../07_Concepts/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/concepts/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2170_pp2q4q_irv](bv2170_pp2q4q_irv.md) · [bv2170_pp2q4q_plurality](bv2170_pp2q4q_plurality.md) · [bv2170_pp2q4q_star](bv2170_pp2q4q_star.md)
