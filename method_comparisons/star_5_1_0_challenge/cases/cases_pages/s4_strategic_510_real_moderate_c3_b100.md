# Strategic 5-1-0 STAR, real moderate base — STAR STILL elects the CW

*Generated from [`s4_strategic_510_real_moderate_c3_b100.yaml`](../s4_strategic_510_real_moderate_c3_b100.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Beth

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/dyh93j) · **[results ↗](https://bettervoting.com/dyh93j/results)** (election `dyh93j`).

## Scenario

The nuance rb-j's "the 1s contribute little" misses. Same 5-1-0 min-max
strategy, but the moderate Beth has a real first-choice base (25, vs poles
40/35). Now the 75 "1"s plus her 25 fives lift Beth to 200 — past Cole (175)
and into the runoff — and she wins as the Condorcet winner. Under the identical
strategic ballot, STAR elects the CW here while RCV-IRV does not (s5): the "1"s
carry real weight, so 5-1-0 STAR is strictly more moderate-friendly than IRV.
So "everyone votes 5-1-0 ⇒ STAR = IRV" is false as a general claim.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana, Beth, Cole
40 × 5, 1, 0
35 × 0, 1, 5
25 × 1, 5, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Beth
  Choose-One (Plurality) = Ana   (differs from STAR)
  RCV-IRV                = Ana   (differs from STAR)
  Approval               = Ana   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/s4_strategic_510_real_moderate_c3_b100_RCV-IRV_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Ana)
 - Runoff Round Winner   = (Beth)
  Candidate Ana earned the highest total score, but
  Candidate Beth won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Ana,Beth,Cole
   40 ×   5,   1,   0
   35 ×   0,   1,   5
   25 ×   1,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 225 -- First place
   Beth          -- 200 -- Second place
   Cole          -- 175
 Ana and Beth advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Beth          -- 60 -- First place
   Ana           -- 40
   Equal Support --  0
 Beth wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Beth 60 (60%)  ·  Ana 40 (40%)

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
         * Ana > |     ---      |40 -  0 - 60 |65 -  0 - 35 |
        * Beth > | 60 -  0 - 40 |    ---      |65 -  0 - 35 |
          Cole > | 35 -  0 - 65 |35 -  0 - 65 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Beth — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ana        40   0   0   0  25  35  |   225   2.3
Beth       25   0   0   0  75   0  |   200   2.0
Cole       35   0   0   0   0  65  |   175   1.8
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/s4_strategic_510_real_moderate_c3_b100_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/star_5_1_0_challenge/cases/s4_strategic_510_real_moderate_c3_b100.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/s4_strategic_510_real_moderate_c3_b100.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [s1_sincere_thin_moderate_c3_b100](s1_sincere_thin_moderate_c3_b100.md) · [s2_strategic_510_thin_moderate_c3_b100](s2_strategic_510_thin_moderate_c3_b100.md) · [s3_irv_thin_moderate_c3_b100](s3_irv_thin_moderate_c3_b100.md) · [s5_irv_real_moderate_c3_b100](s5_irv_real_moderate_c3_b100.md)
