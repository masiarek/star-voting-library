# Sincere STAR — the center wins (Beth is the Condorcet winner)

*Generated from [`s1_sincere_thin_moderate_c3_b100.yaml`](../s1_sincere_thin_moderate_c3_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Beth

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/2kcwbw) · **[results ↗](https://bettervoting.com/2kcwbw/results)** (election `2kcwbw`).

## Scenario

A 1-D center-squeeze electorate: Ana (left) and Cole (right) are the poles;
Beth is the broadly-liked moderate and the Condorcet winner (she beats Ana
52–48 and Cole 53–47). Beth has a THIN first-choice base (only 5 voters), but
on SINCERE ballots the poles' supporters score her a genuine 3, so she leads
the scoring round (310) and wins the runoff — STAR elects the Condorcet
winner. The strategic-5-1-0 twin (s2) shows what happens when voters min-max
instead. Part of the rb-j "does STAR collapse to IRV under 5-1-0?" claim-check.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana, Beth, Cole
48 × 5, 3, 0
47 × 0, 3, 5
 5 × 2, 5, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Beth
  Choose-One (Plurality) = Ana   (differs from STAR)
  RCV-IRV                = Ana   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/s1_sincere_thin_moderate_c3_b100_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Ana,Beth,Cole
   48 ×   5,   3,   0
   47 ×   0,   3,   5
    5 ×   2,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Beth          -- 310 -- First place
   Ana           -- 250 -- Second place
   Cole          -- 235
 Beth and Ana advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Beth          -- 52 -- First place
   Ana           -- 48
   Equal Support --  0
 Beth wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Beth 52 (52%)  ·  Ana 48 (48%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Beth
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ana     |   * Beth    |     Cole    |
-------------------------------------------------------------
         * Ana > |     ---      |48 -  0 - 52 |53 -  0 - 47 |
        * Beth > | 52 -  0 - 48 |    ---      |53 -  0 - 47 |
          Cole > | 47 -  0 - 53 |47 -  0 - 53 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Beth — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ana        48   0   0   5   0  47  |   250   2.5
Beth        5   0  95   0   0   0  |   310   3.1
Cole       47   0   0   0   0  53  |   235   2.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/s1_sincere_thin_moderate_c3_b100_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/star_5_1_0_challenge/cases/s1_sincere_thin_moderate_c3_b100.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/s1_sincere_thin_moderate_c3_b100.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [s2_strategic_510_thin_moderate_c3_b100](s2_strategic_510_thin_moderate_c3_b100.md) · [s3_irv_thin_moderate_c3_b100](s3_irv_thin_moderate_c3_b100.md) · [s4_strategic_510_real_moderate_c3_b100](s4_strategic_510_real_moderate_c3_b100.md) · [s5_irv_real_moderate_c3_b100](s5_irv_real_moderate_c3_b100.md)
