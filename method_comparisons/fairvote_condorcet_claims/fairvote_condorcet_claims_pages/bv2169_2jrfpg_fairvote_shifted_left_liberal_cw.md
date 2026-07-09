# Same three candidates, electorate shifts left — the 'strong liberal' IS the Condorcet winner

*Generated from [`bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.yaml`](../bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Liberal

## Scenario

The refutation-by-example of FairVote's claim that "Condorcet winners are
centrist by nature, regardless of the preferences of the electorate" (and
that agreeing with the Condorcet criterion "is equivalent to saying that
moderate candidates should always win"). Same cast as
bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.yaml, but the electorate has
moved left: Liberal 56 first choices, Moderate 12, Conservative 32.

Now the strong LIBERAL — a pole candidate, not the moderate — is the
Condorcet winner: 56-44 over Moderate, 62-38 over Conservative. A candidate
ranked first by an outright majority is automatically the Condorcet winner,
so every landslide winner in history satisfies the criterion trivially. The
Condorcet winner is defined BY the preferences of the electorate and moves
with them; "centrist regardless of preferences" is exactly backwards.
Every method here agrees (STAR, RCV-IRV, Choose-One, Ranked Robin): Liberal.

LIVE on BetterVoting as BV2169 — two races on the same 100 voters: this
STAR race plus an RCV-IRV race that agrees (first-choice majority).
Live results: https://bettervoting.com/2jrfpg/results
Full claim-by-claim reading of the article:
00_start_here/topics/condorcet/fairvote_condorcet_claim_check.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Liberal,Moderate,Conservative
56:5,2,0   # Liberal > Moderate > Conservative
32:0,2,5   # Conservative > Moderate > Liberal
6:2,5,0    # Moderate > Liberal > Conservative
6:0,5,2    # Moderate > Conservative > Liberal
```

## What the engine says

Full report from the [`_tabulated` mirror](../fairvote_condorcet_claims_tabulated/bv2169_2jrfpg_fairvote_shifted_left_liberal_cw_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                     |    * Liberal     |   * Moderate    |   Conservative  |
-----------------------------------------------------------------------------
         * Liberal > |       ---        |  56 -  0 - 44   |  62 -  0 - 38   |
        * Moderate > |   44 -  0 - 56   |      ---        |  68 -  0 - 32   |
      Conservative > |   38 -  0 - 62   |  32 -  0 - 68   |      ---        |

[Condorcet Winner]
  Condorcet Winner: Liberal — matches the STAR winner

--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 100 ballots.
Count × Liberal,Moderate,Conservative
   56 ×       5,       2,           0
   32 ×       0,       2,           5
    6 ×       2,       5,           0
    6 ×       0,       5,           2

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate      5   4   3   2   1   0  | Total   Avg
Liberal       56   0   0   6   0  38  |   292   2.9
Moderate      12   0   0  88   0   0  |   236   2.4
Conservative  32   0   0   6   0  62  |   172   1.7

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Liberal       -- 292 -- First place
   Moderate      -- 236 -- Second place
   Conservative  -- 172
 Liberal and Moderate advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Liberal       -- 56 -- First place
   Moderate      -- 44
   Equal Support --  0
 Liberal wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Liberal 56 (56%)  ·  Moderate 44 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Liberal
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/fairvote_condorcet_claims/bv2169_2jrfpg_fairvote_shifted_left_liberal_cw.yaml
```

## See also

- [This set's lesson (README)](../README.md) — the hand-written teaching context for every case in this folder
- [Condorcet efficiency (topic hub)](../../../00_start_here/topics/condorcet/README.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2168_6w2gq7_fairvote_40_15_40_moderate_cw](bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.md)
