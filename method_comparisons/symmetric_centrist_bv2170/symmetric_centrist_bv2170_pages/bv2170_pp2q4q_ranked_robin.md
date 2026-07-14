# Symmetric centrist (47/47/3/3) — Ranked Robin: elects Casey, beats everyone head-to-head

*Generated from [`bv2170_pp2q4q_ranked_robin.yaml`](../bv2170_pp2q4q_ranked_robin.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Ranked Robin (RCV-RR / Copeland)](../../../00_start_here/RCV_Ranked_Robin) · **1 seat** · **Expected winner:** Casey

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/pp2q4q) · **[results ↗](https://bettervoting.com/pp2q4q/results)** (election `pp2q4q`).

**Official tie-break (lot) order:** Avery > Casey > Blake — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

One of four races in the Symmetric Centrist election (BV2170, bvid pp2q4q; BV-confirmed). 100 voters, three candidates, ONE electorate tabulated four ways. Avery is the left pole, Blake the right pole, Casey the centrist. Ranked Robin (Copeland) compares every pair head-to-head: Casey beats Avery 53–47 and Casey beats Blake 53–47, while Avery ties Blake 50–50. Casey wins both matchups (2–0) — the Condorcet winner — so Ranked Robin elects Casey directly and deterministically (no cycle, no tiebreak), agreeing with STAR and disagreeing with the center-squeeze methods IRV and Choose-One.

Live results: https://bettervoting.com/pp2q4q/results
Companion races: bv2170_pp2q4q_star.yaml, bv2170_pp2q4q_irv.yaml, bv2170_pp2q4q_plurality.yaml.
Overview page: bv2170_pp2q4q_symmetric_centrist.md

## Ballots

Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
47:Avery>Casey>Blake
47:Blake>Casey>Avery
3:Casey>Avery>Blake
3:Casey>Blake>Avery
```

## What the engine says

Full report from the [`_tabulated` mirror](../symmetric_centrist_bv2170_tabulated/bv2170_pp2q4q_ranked_robin_tabulated.txt) (regenerated on every run; every analysis forced on):

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

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Casey      2–0–0         2     +12  Avery, Blake
    2  Avery      0–1–1       0.5      -6  —
    3  Blake      0–1–1       0.5      -6  —

Winner — Ranked Robin (RCV-RR): Casey
   beats every opponent head-to-head — the Condorcet winner.
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/symmetric_centrist_bv2170/bv2170_pp2q4q_ranked_robin.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2170_pp2q4q_irv](bv2170_pp2q4q_irv.md) · [bv2170_pp2q4q_plurality](bv2170_pp2q4q_plurality.md) · [bv2170_pp2q4q_star](bv2170_pp2q4q_star.md)
