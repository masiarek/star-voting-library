# Alaska 2022 US House special (reduced model) — STAR & Ranked Robin elect Begich, the Condorcet winner RCV-IRV cut

*Generated from [`bv2213_k3fmwv_alaska_2022.yaml`](../bv2213_k3fmwv_alaska_2022.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Begich

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/k3fmwv) · **[results ↗](https://bettervoting.com/k3fmwv/results)** (election `k3fmwv`).

## Scenario

A reduced 200-voter TEACHING MODEL of the August 2022 Alaska US House special
election (Peltola / Begich / Palin) — not the real vote data, but a faithful
~943:1 scaling of the official preference profile in Table 1 of Graham-Squire &
McCune, "An Examination of Ranked Choice Voting in the United States, 2004-2022"
(arXiv:2301.12075); all nine ballot types match the paper. One electorate, FOUR
counts. First choices: Peltola 80, Palin 63, Begich 57 — so Choose-One
(Plurality) elects Peltola. RCV-IRV eliminates Begich (fewest first choices), 12
ballots exhaust, and Peltola beats Palin 96-92 — also Peltola. But Begich is the
Condorcet winner (beats Peltola 93-84 and Palin 107-68), so Ranked Robin and STAR
both elect Begich — the broadly-preferred centrist IRV's first-choice elimination
threw out (the center squeeze). Same ballots, four counts, two winners; IRV is the
lone method that fails the Condorcet winner. Scores are a rank->score modeling
overlay (favorite 5, then 4/3, unranked 0). Real ballots & every headline figure:
the paper above; Equal Vote's Real RCV visualizer: realrcv.equal.vote/alaska22.
Live results (BV2213, all four races): https://bettervoting.com/k3fmwv/results
Lesson: README.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Peltola, Begich, Palin
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,0,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,4,0
  5,0,4
  5,0,4
  5,0,4
  5,0,4
  5,0,4
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  0,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  4,5,0
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,5,4
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  0,0,5
  4,3,5
  4,3,5
  4,3,5
  4,3,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
  0,4,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Begich
  Choose-One (Plurality) = Peltola   (differs from STAR)
  RCV-IRV                = Peltola   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2213_k3fmwv_alaska_2022_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 200 ballots.
Count × Peltola,Begich,Palin
   50 ×       5,     4,    0
   36 ×       0,     4,    5
   29 ×       0,     5,    4
   25 ×       5,     0,    0
   23 ×       0,     0,    5
   16 ×       4,     5,    0
   12 ×       0,     5,    0
    5 ×       5,     0,    4
    4 ×       4,     3,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Begich        -- 641 -- First place
   Peltola       -- 480 -- Second place
   Palin         -- 451
 Begich and Peltola advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Begich        -- 93 -- First place
   Peltola       -- 84
   Equal Support -- 23
 Begich wins.
   Runoff math:
     200  ballots cast
   −  23  Equal Support (no preference between the two finalists)
     ───
     177  voters with a preference  (majority = 89)
           Begich 93 (53%)  ·  Peltola 84 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Begich
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |    * Peltola    |   * Begich     |      Palin     |
-------------------------------------------------------------------------
        * Peltola > |       ---       | 84 -  23 -  93 | 96 -  12 -  92 |
         * Begich > |  93 -  23 -  84 |      ---       |107 -  25 -  68 |
            Palin > |  92 -  12 -  96 | 68 -  25 - 107 |      ---       |

[Condorcet Winner]
  Condorcet Winner: Begich — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
Peltola     80   20    0    0    0  100  |   480   2.4
Begich      57   86    4    0    0   53  |   641   3.2
Palin       63   34    0    0    0  103  |   451   2.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2213_k3fmwv_alaska_2022_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/alaska_2022/cases/bv2213_k3fmwv_alaska_2022.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2213_k3fmwv_alaska_2022.md) — its entry in the divergence review ledger
- [Center squeeze (topic hub)](../../../../00_start_here/topics/center_squeeze/README.md)
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Exhausted ballots (conversation)](../../../../00_start_here/RCV_IRV/exhausted_ballots_301.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
