# Condorcet centrist, full form (100 voters, 47/47/3/3) — STAR elects Casey

*Generated from [`bv2172_bkwfjr_star.yaml`](../bv2172_bkwfjr_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Casey

## Scenario

The STAR race (lead of seven) in the full Condorcet-centrist election (BV2172, bvid bkwfjr; BV-confirmed) — the profile as drawn in the "Should we always elect the Condorcet winner?" explainer (youtu.be/NlisR8vbpN4). 100 voters, three candidates — Avery (left pole), Blake (right pole), Casey (centrist). Casey is the Condorcet winner (beats Avery 53–47 and Blake 53–47) but has only 6 first choices. Ranks mapped to 0–5 scores (top=5, mid=3, bottom=1): Casey tops the score round 312 (Avery/Blake tie at 294) and wins the automatic runoff 53–47.

Seven methods, one electorate. Whole-ballot methods — STAR, STAR-PR (1 seat), Approval (approve top two), Ranked Robin — elect Casey. First-choice methods — RCV-IRV, STV (1 seat), Choose-One — eliminate Casey first and, because the poles are a mirror image, deadlock Avery vs Blake in an exact tie (random on BV, not freezable). See the overview page for all seven.

Live results: https://bettervoting.com/bkwfjr/results
Overview: bv2172_bkwfjr_all_methods.md · Minimal 8-voter version: bv2171_h93tm4_star.yaml (BV2171) · Original 4-method cut: ../symmetric_centrist_bv2170/

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Avery,Blake,Casey
47:5,1,3   # Avery > Casey > Blake  (left pole)
47:1,5,3   # Blake > Casey > Avery  (right pole)
3:3,1,5    # Casey > Avery > Blake  (centrist, leans left)
3:1,3,5    # Casey > Blake > Avery  (centrist, leans right)
```

## What the engine says

Full report from the [`_tabulated` mirror](../symmetric_centrist_all_methods_tabulated/bv2172_bkwfjr_star_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Avery    |    Blake    |  * Casey    |
-------------------------------------------------------------
       * Avery > |     ---      |50 -  0 - 50 |47 -  0 - 53 |
         Blake > | 50 -  0 - 50 |    ---      |47 -  0 - 53 |
       * Casey > | 53 -  0 - 47 |53 -  0 - 47 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Casey — matches the STAR winner

[Divergence from STAR]
  STAR                   = Casey
  Choose-One (Plurality) = Avery   (differs from STAR)
  RCV-IRV                = Avery   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: symmetric_centrist_all_methods_tabulated/bv2172_bkwfjr_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Avery,Blake,Casey
   47 ×     5,    1,    3
   47 ×     1,    5,    3
    3 ×     3,    1,    5
    3 ×     1,    3,    5

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Avery      47   0   3   0  50   0  |   294   2.9
Blake      47   0   3   0  50   0  |   294   2.9
Casey       6   0  94   0   0   0  |   312   3.1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Casey         -- 312 -- First place
   Avery         -- 294 -- Tied for second place
   Blake         -- 294 -- Tied for second place
 Casey advances, but there's a two-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Avery         -- 50 -- Tied for second place
   Blake         -- 50 -- Tied for second place
   Equal Support --  0
 There's still a two-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Avery         -- 47 -- Tied for second place
   Blake         -- 47 -- Tied for second place
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
   Casey         -- 53 -- First place
   Avery         -- 47
   Equal Support --  0
 Casey wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Casey 53 (53%)  ·  Avery 47 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Casey
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/symmetric_centrist_all_methods/bv2172_bkwfjr_star.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2172_bkwfjr_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../00_start_here/topics/ties/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2171_h93tm4_star](bv2171_h93tm4_star.md)
