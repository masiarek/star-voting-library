# Strategic 5-1-0 STAR — the center is squeezed out (fails the CW)

*Generated from [`bv2222_rfyk46_510_thin_star.yaml`](../bv2222_rfyk46_510_thin_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Ana

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/rfyk46) · **[results ↗](https://bettervoting.com/rfyk46/results)** (election `rfyk46`).

## Scenario

The SAME electorate as s1, but every voter min-maxes rb-j's way: favorite 5,
lesser-evil 1, hated 0. Now Beth's scoring total collapses to 120 (75 ones +
25 from her base) — below both poles — so she misses the runoff, and Ana (a
pole) wins. STAR fails to elect the Condorcet winner, exactly as rb-j argues:
under coordinated 5-1-0 with a thin moderate base, STAR center-squeezes like
IRV. Confirmed identical to RCV-IRV on this electorate (s3).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana, Beth, Cole
48 × 5, 1, 0
47 × 0, 1, 5
 5 × 1, 5, 0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR               = Ana
  RCV-RR (Condorcet) = Beth   (differs from STAR)
  Full round-by-round reports (generated for review):
  RCV-RR round-robin: cases_tabulated/bv2222_rfyk46_510_thin_star_RCV-RR_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Ana,Beth,Cole
   48 ×   5,   1,   0
   47 ×   0,   1,   5
    5 ×   1,   5,   0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ana           -- 245 -- First place
   Cole          -- 235 -- Second place
   Beth          -- 120
 Ana and Cole advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ana           -- 53 -- First place
   Cole          -- 47
   Equal Support --  0
 Ana wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Ana 53 (53%)  ·  Cole 47 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ana
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ana     |     Beth    |   * Cole    |
-------------------------------------------------------------
         * Ana > |     ---      |48 -  0 - 52 |53 -  0 - 47 |
          Beth > | 52 -  0 - 48 |    ---      |53 -  0 - 47 |
        * Cole > | 47 -  0 - 53 |47 -  0 - 53 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Beth — STAR elected Ana instead (Beth was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ana        48   0   0   0   5  47  |   245   2.5
Beth        5   0   0   0  95   0  |   120   1.2
Cole       47   0   0   0   0  53  |   235   2.4
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2222_rfyk46_510_thin_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/star_5_1_0_challenge/cases/bv2222_rfyk46_510_thin_star.yaml
```

## See also

- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2221_2kcwbw_sincere](bv2221_2kcwbw_sincere.md) · [bv2222_rfyk46_510_thin_irv](bv2222_rfyk46_510_thin_irv.md) · [bv2223_dyh93j_510_real_irv](bv2223_dyh93j_510_real_irv.md) · [bv2223_dyh93j_510_real_star](bv2223_dyh93j_510_real_star.md)
