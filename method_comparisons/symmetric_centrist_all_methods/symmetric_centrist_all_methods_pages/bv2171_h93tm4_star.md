# Condorcet centrist, minimal form (8 voters) — STAR elects Casey

*Generated from [`bv2171_h93tm4_star.yaml`](../bv2171_h93tm4_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Casey

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/h93tm4) · **[results ↗](https://bettervoting.com/h93tm4/results)** (election `h93tm4`).

## Scenario

The STAR race (lead of seven) in the minimal Condorcet-centrist election (BV2171, bvid h93tm4; BV-confirmed). The fewest ballots that still reproduce the whole center-squeeze symptom: 8 voters, three candidates — Avery (left pole), Blake (right pole), Casey (centrist). Casey is the Condorcet winner (beats Avery 5–3 and Blake 5–3) but has only 2 first choices, the fewest. Ranks mapped to 0–5 scores (top=5, mid=3, bottom=1): Casey tops the score round 28 (Avery/Blake tie at 22) and wins the automatic runoff 5–3.

Seven methods, one electorate. Whole-ballot methods — STAR, STAR-PR (1 seat), Approval (approve top two), Ranked Robin — elect Casey. First-choice methods — RCV-IRV, STV (1 seat), Choose-One — eliminate Casey first and, because the poles are a mirror image, deadlock Avery vs Blake in an exact tie (random on BV, not freezable). See the overview page for all seven.

Live results: https://bettervoting.com/h93tm4/results
Overview: bv2171_h93tm4_all_methods.md · Full 100-voter version: bv2172_bkwfjr_star.yaml (BV2172) · Original 4-method cut: ../symmetric_centrist_bv2170/

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Avery,Blake,Casey
3:5,1,3   # Avery > Casey > Blake  (left pole)
3:1,5,3   # Blake > Casey > Avery  (right pole)
1:3,1,5   # Casey > Avery > Blake  (centrist, leans left)
1:1,3,5   # Casey > Blake > Avery  (centrist, leans right)
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Casey
  Choose-One (Plurality) = Avery   (differs from STAR)
  RCV-IRV                = Avery   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: symmetric_centrist_all_methods_tabulated/bv2171_h93tm4_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 8 ballots.
Count × Avery,Blake,Casey
    3 ×     5,    1,    3
    3 ×     1,    5,    3
    1 ×     3,    1,    5
    1 ×     1,    3,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Casey         -- 28 -- First place
   Avery         -- 22 -- Tied for second place
   Blake         -- 22 -- Tied for second place
 Casey advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Avery         -- 4 -- Tied for second place
   Blake         -- 4 -- Tied for second place
   Equal Support -- 0
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Avery         -- 3 -- Tied for second place
   Blake         -- 3 -- Tied for second place
 There's still a two-way tie for second.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Avery', 'Blake', 'Casey']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Avery', 'Blake']
  Resolved: ['Avery'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: the deterministic rungs
    (pairwise / score, then five-star) all came back equal, so the
    pre-published LOT order chose among the tied candidates — the
    result here was set by lot, not by the votes. Usually the
    "dead rung": no tied candidate held a score-5 vote (five-star
    counts fives, not fours). Verify the tied candidates' 5-counts.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Casey         -- 5 -- First place
   Avery         -- 3
   Equal Support -- 0
 Casey wins.
   Runoff math:
     8  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     8  voters with a preference  (majority = 5)
           Casey 5 (62%)  ·  Avery 3 (38%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Casey
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Avery   |   Blake   | * Casey   |
-----------------------------------------------------
     * Avery > |    ---     |4 - 0 - 4  |3 - 0 - 5  |
       Blake > | 4 - 0 - 4  |   ---     |3 - 0 - 5  |
     * Casey > | 5 - 0 - 3  |5 - 0 - 3  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Casey — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Avery      3  0  1  0  4  0  |    22   2.8
Blake      3  0  1  0  4  0  |    22   2.8
Casey      2  0  6  0  0  0  |    28   3.5
```

</details>

Everything in one file: the [`_tabulated` mirror](../symmetric_centrist_all_methods_tabulated/bv2171_h93tm4_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/symmetric_centrist_all_methods/bv2171_h93tm4_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2171_h93tm4_star.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2172_bkwfjr_star](bv2172_bkwfjr_star.md)
