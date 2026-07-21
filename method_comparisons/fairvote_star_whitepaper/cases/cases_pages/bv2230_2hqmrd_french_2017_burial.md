# FairVote white paper — French 2017 (BURIAL): coordinated strategy squeezes Macron out

*Generated from [`bv2230_2hqmrd_french_2017_burial.yaml`](../bv2230_2hqmrd_french_2017_burial.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Melenchon

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/2hqmrd) · **[results ↗](https://bettervoting.com/2hqmrd/results)** (election `2hqmrd`).

## Scenario

The coordinated-burial scenario from FairVote's white paper: to keep the centrist
Macron out of the runoff, every non-Macron faction scores Macron 0 and inflates the
OTHER non-Macron wings to 4 — even rating their ideological opposites highly. Same
voters and honest first choices as french_2017_honest; only the strategy changes.
It works: Macron collapses to 130 and misses the runoff (Melenchon 399, Fillon 398);
STAR elects Melenchon. So FairVote's claim is CONCEDED — coordinated burial can squeeze
the centrist under STAR. The honest caveats (see ../README.md): it requires every rival
faction to bury Macron AND rate their enemies 4 (a risky, implausible conspiracy);
honest STAR elects Macron; and RCV-IRV on these same strategic ballots elects Le Pen
(the far right) — a worse miss. STAR squeezes the center only under STRATEGY; IRV
center-squeezes under HONESTY (Burlington, Alaska). Concept: ../README.md.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Macron,LePen,Fillon,Melenchon
26:5,0,3,3   # Macron base — honest
25:0,4,4,5   # Melenchon voters bury Macron, inflate the right wings
24:0,4,5,4   # Fillon voters bury Macron, inflate the others
25:0,5,4,4   # Le Pen voters bury Macron, inflate the others
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Melenchon
  Choose-One (Plurality) = Macron   (differs from STAR)
  RCV-IRV                = LePen   (differs from STAR)
  Approval               = Fillon   (differs from STAR)
  Note: 100 of 100 ballots (100%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2230_2hqmrd_french_2017_burial_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Macron,LePen,Fillon,Melenchon
   26 ×      5,    0,     3,        3
   25 ×      0,    4,     4,        5
   25 ×      0,    5,     4,        4
   24 ×      0,    4,     5,        4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Melenchon     -- 399 -- First place
   Fillon        -- 398 -- Second place
   LePen         -- 321
   Macron        -- 130
 Melenchon and Fillon advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Melenchon     -- 25 -- First place
   Fillon        -- 24
   Equal Support -- 51
 Melenchon wins.
   Runoff math:
     100  ballots cast
   −  51  Equal Support (no preference between the two finalists)
     ───
      49  voters with a preference  (majority = 25)
           Melenchon 25 (51%)  ·  Fillon 24 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Melenchon
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                  |     Macron    |     LePen    |  * Fillon    | * Melenchon  |
--------------------------------------------------------------------------------
         Macron > |      ---      |26 -  0 - 74  |26 -  0 - 74  |26 -  0 - 74  |
          LePen > | 74 -  0 - 26  |     ---      |25 - 25 - 50  |25 - 24 - 51  |
       * Fillon > | 74 -  0 - 26  |50 - 25 - 25  |     ---      |24 - 51 - 25  |
    * Melenchon > | 74 -  0 - 26  |51 - 24 - 25  |25 - 51 - 24  |     ---      |

[Condorcet Winner]
  Condorcet Winner: Melenchon — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Macron     26   0   0   0   0  74  |   130   1.3
LePen      25  49   0   0   0  26  |   321   3.2
Fillon     24  50  26   0   0   0  |   398   4.0
Melenchon  25  49  26   0   0   0  |   399   4.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2230_2hqmrd_french_2017_burial_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/fairvote_star_whitepaper/cases/bv2230_2hqmrd_french_2017_burial.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_DIFFERS_ARTIFACT/bv2230_2hqmrd_french_2017_burial.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2229_7j2bqf_french_2017_honest](bv2229_7j2bqf_french_2017_honest.md) · [bv2231_b4yr3v_wa_2010_honest](bv2231_b4yr3v_wa_2010_honest.md) · [bv2232_24b623_wa_2010_burial](bv2232_24b623_wa_2010_burial.md)
