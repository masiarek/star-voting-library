# FairVote's own hypothetical (45/12/43) — the moderate IS the majority's pairwise choice

*Generated from [`bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.yaml`](../bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Moderate

## Scenario

FairVote's article "Why the Condorcet Criterion Is Less Important Than It
Seems" (Alec Slatky, 2010) argues from a hypothetical: "a strong liberal who
commands between 40% to 50% of the vote, a moderate with about 10% to 15%,
and a strong conservative between 40% and 50%." This file tabulates exactly
that electorate: Liberal 45, Moderate 12, Conservative 43 (100 voters).

What the count shows: the Moderate is the Condorcet winner — a 55-voter
majority prefers Moderate over Liberal, and a 57-voter majority prefers
Moderate over Conservative. The article reads the 45/12/43 FIRST-CHOICE
split as "80-90% would prefer their candidate have a chance"; the pairwise
count is the answer — majorities, not the 12%, choose the Moderate against
either rival. And the method the article defends, RCV-IRV, eliminates that
Moderate first (fewest first choices) and elects the Liberal — the classic
center squeeze, in the article's own numbers.

Honest nuance the scores add: the poles only lukewarm-support the Moderate
(2 of 5), so the Liberal actually tops the SCORE sum 237 to 236 — the
article's "hated least isn't liked most" point, made visible. STAR shows
both facts (score round: Liberal first; runoff: Moderate wins 55-45).

LIVE on BetterVoting as BV2168 — two races on the same 100 voters: this
STAR race plus an RCV-IRV race, so the squeeze is clickable live.
Live results: https://bettervoting.com/6w2gq7/results
Matched file: bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.yaml (same
cast, electorate shifts left — the "strong liberal" becomes the Condorcet
winner).
Full claim-by-claim reading of the article:
00_start_here/topics/condorcet/fairvote_condorcet_claim_check.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Liberal,Moderate,Conservative
45:5,2,0   # Liberal > Moderate > Conservative
43:0,2,5   # Conservative > Moderate > Liberal
6:2,5,0    # Moderate > Liberal > Conservative
6:0,5,2    # Moderate > Conservative > Liberal
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Moderate
  Choose-One (Plurality) = Liberal   (differs from STAR)
  RCV-IRV                = Liberal   (differs from STAR)
  Approval               = Liberal   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: fairvote_condorcet_claims_tabulated/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw_RCV-IRV_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Liberal)
 - Runoff Round Winner   = (Moderate)
  Candidate Liberal earned the highest total score, but
  Candidate Moderate won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Liberal,Moderate,Conservative
   45 ×       5,       2,           0
   43 ×       0,       2,           5
    6 ×       2,       5,           0
    6 ×       0,       5,           2

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Liberal       -- 237 -- First place
   Moderate      -- 236 -- Second place
   Conservative  -- 227
 Liberal and Moderate advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Moderate      -- 55 -- First place
   Liberal       -- 45
   Equal Support --  0
 Moderate wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Moderate 55 (55%)  ·  Liberal 45 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Moderate
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                     |    * Liberal     |   * Moderate    |   Conservative  |
-----------------------------------------------------------------------------
         * Liberal > |       ---        |  45 -  0 - 55   |  51 -  0 - 49   |
        * Moderate > |   55 -  0 - 45   |      ---        |  57 -  0 - 43   |
      Conservative > |   49 -  0 - 51   |  43 -  0 - 57   |      ---        |

[Condorcet Winner]
  Condorcet Winner: Moderate — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate      5   4   3   2   1   0  | Total   Avg
Liberal       45   0   0   6   0  49  |   237   2.4
Moderate      12   0   0  88   0   0  |   236   2.4
Conservative  43   0   0   6   0  51  |   227   2.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../fairvote_condorcet_claims_tabulated/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/fairvote_condorcet_claims/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Methods disagree on this election](../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Vote splitting (worked set)](../../split_voting/README.md)
- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2169_2jrfpg_fairvote_shifted_left_liberal_cw](bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.md)
