# Felsenthal Ex.1 — Choose-One (Plurality): the absolute loser wins

*Generated from [`bv2144_mxfmhm_plurality.yaml`](../bv2144_mxfmhm_plurality.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [plurality](../../../00_start_here) · **1 seat** · **Expected winner:** Ana

**Official tie-break (lot) order:** Ana > Cal > Bo — consulted only if every deterministic tiebreaker stays tied ([how the ladder works](../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)).

## Scenario

Race 1 of 2 in the Felsenthal plurality-paradoxes election (BV2144, bvid mxfmhm; BV-confirmed). Source: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected", University of Haifa / LSE, revised 26 May 2010 (Leverhulme Trust "Voting Power in Practice" workshop, Château du Baffy, Normandy); Appendix A1, Example 1.
7 voters, three candidates (Ana=a, Bo=b, Cal=c); rankings 3×(Ana>Bo>Cal), 2×(Bo>Cal>Ana), 2×(Cal>Bo>Ana). Bo is the Condorcet winner (beats Ana 4–3, Cal 5–2). Ana is both the Condorcet LOSER and the ABSOLUTE loser — a majority (4 of 7) rank Ana dead last. Yet Choose-One elects Ana 3–2–2 on first choices; and if Cal dropped out, Bo would beat Ana 4–3 — Felsenthal's SCC (the spoiler effect). Four paradoxes in one 7-voter election.
Live results: https://bettervoting.com/mxfmhm/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Bo,Cal
1,0,0
1,0,0
1,0,0
0,1,0
0,1,0
0,0,1
0,0,1
```

## What the engine says

Full report from the [`_tabulated` mirror](../felsenthal_paradoxes_tabulated/bv2144_mxfmhm_plurality_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |   * Ana    |     Bo    |  * Cal    |
-----------------------------------------------------
       * Ana > |    ---     |3 - 2 - 2  |3 - 2 - 2  |
          Bo > | 2 - 2 - 3  |   ---     |2 - 3 - 2  |
       * Cal > | 2 - 2 - 3  |2 - 3 - 2  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Ana — matches the STAR winner

--- Choose-One / Plurality Voting Method (single winner) ---
[STAR Voting]
 Tabulating 7 ballots.
Count × Ana,Bo,Cal
    3 ×   1, 0,  0
    2 ×   0, 1,  0
    2 ×   0, 0,  1

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ana        0  0  0  0  3  4  |     3   0.4
Bo         0  0  0  0  2  5  |     2   0.3
Cal        0  0  0  0  2  5  |     2   0.3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 3 -- First place
   Bo            -- 2 -- Tied for second place
   Cal           -- 2 -- Tied for second place
 Ana advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Bo            -- 2 -- Tied for second place
   Cal           -- 2 -- Tied for second place
   Equal Support -- 3
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Bo            -- 0 -- Tied for second place
   Cal           -- 0 -- Tied for second place
 There's still a two-way tie for second.

*(Ties are resolved by choosing the tied candidate with the highest-priority official lot number.)*
    Lot-number priority order: ['Ana', 'Cal', 'Bo']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Bo', 'Cal']
  Resolved: ['Cal'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 3 -- First place
   Cal           -- 2
   Equal Support -- 2
 Ana wins.
   Runoff math:
     7  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     5  voters with a preference  (majority = 3)
           Ana 3 (60%)  ·  Cal 2 (40%)

[STAR Voting: Winner — Choose-One / Plurality Voting Method (single winner)]
 Ana
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/felsenthal_paradoxes/bv2144_mxfmhm_plurality.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2144_mxfmhm_star](bv2144_mxfmhm_star.md)
