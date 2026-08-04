---
search:
  exclude: true
---

# The Post-it RCV example (20 voters) — RCV-IRV: Purple wins the video's whiteboard count

*Generated from [`bv2176_p8dp28_irv.yaml`](../bv2176_p8dp28_irv.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [RCV-IRV (Instant Runoff)](../../../../06_Other/RCV_IRV/concepts) · **1 seat** · **Expected winner:** Purple

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28` · test `BV2176`).

## Scenario

One of three races in the Post-it RCV example (BV2176, bvid p8dp28;
BV-confirmed). The 20 ranked ballots from Equal Vote's video "Updated: How
does RCV work? — With Post-its!" (https://youtu.be/Vte4nly_Neg), counted
exactly as on the whiteboard. Round 1: Purple 7, Green 6, Blue 4, Pink 3 —
Pink is eliminated (1 ballot goes to Green, 1 to Purple, and 1 bullet-vote
Pink ballot exhausts). Round 2: Purple 8, Green 7, Blue 4 — Blue is
eliminated (1 to Green, 1 to Purple, and the 2 Blue>Pink ballots exhaust,
Pink being already gone). Final: Purple 9, Green 8 — Purple wins with 9 of
the 17 still-active ballots. The sting the video builds to: Blue, the round-2
eliminee, beats Purple head-to-head 10-9 — a runoff RCV-IRV never held, but
the STAR race on these voters' scores does (and Blue wins it).

Live results: https://bettervoting.com/p8dp28/results
Companion races: bv2176_p8dp28_star.yaml, bv2176_p8dp28_ranked_robin.yaml.
Overview page: bv2176_p8dp28_postit_rcv_example.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Purple
Purple
Purple
Purple
Purple
Purple
Purple
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Green>Blue>Pink
Blue>Pink
Blue>Pink
Blue>Green>Pink
Blue>Purple
Pink>Green>Purple
Pink>Purple
Pink
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
--- RCV / Instant-Runoff Voting (single winner) ---
  The Post-it RCV example (20 voters) — RCV-IRV: Purple wins the video's whiteboard count
 Tabulating 20 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Purple             7  Hopeful
Green              6  Hopeful
Blue               4  Hopeful
Pink               3  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
Purple             8  Hopeful
Green              7  Hopeful
Blue               4  Rejected
Pink               0  Rejected
Blank Votes        1  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Purple             9  Elected
Green              8  Rejected
Blue               0  Rejected
Pink               0  Rejected
Blank Votes        3  Rejected


Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Purple
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Smith Set (the generalized Condorcet winner) ---
The smallest group whose every member beats every candidate outside it —
the honest answer to "who is even in contention?".
   Smith set (4 of 4): Green, Blue, Purple, Pink
   Outside (0):        —
   More than one member ⇒ NO Condorcet winner: the top of the tournament is a
   cycle, so the strongest "candidate" is a set, not a person. Which member of
   the set should win is exactly what Minimax / Ranked Pairs / Schulze disagree
   about — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.
   Note: the Copeland leaders (Green, Blue) are only part of the set — the
   win–loss table's top block understates how wide the contention is.
   RCV-IRV winner Purple is INSIDE the Smith set. ✓
      Not guaranteed — RCV-IRV is not Smith-efficient — but it holds here.
   More: 07_Concepts/topics/smith_set.md
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2176_p8dp28_irv_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/postit_rcv_example/cases/bv2176_p8dp28_irv.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Exhausted ballots (conversation)](../../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2176_p8dp28_ranked_robin](bv2176_p8dp28_ranked_robin.md) · [bv2176_p8dp28_star](bv2176_p8dp28_star.md) · [bv2177_v8r66y_approval](bv2177_v8r66y_approval.md) · [bv2177_v8r66y_plurality](bv2177_v8r66y_plurality.md) · [bv2178_8kg698_irv](bv2178_8kg698_irv.md) · [bv2178_8kg698_ranked_robin](bv2178_8kg698_ranked_robin.md) · [bv2178_8kg698_star](bv2178_8kg698_star.md)
