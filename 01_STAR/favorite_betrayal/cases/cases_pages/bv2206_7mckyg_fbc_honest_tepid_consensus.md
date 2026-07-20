# Favorite betrayal in STAR (1 of 2) — honest ballots: the tepid consensus misses the runoff

*Generated from [`bv2206_7mckyg_fbc_honest_tepid_consensus.yaml`](../bv2206_7mckyg_fbc_honest_tepid_consensus.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Clover

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/7mckyg) · **[results ↗](https://bettervoting.com/7mckyg/results)** (election `7mckyg`).

## Scenario

Honest ballots — half 1 of the repo's worked STAR favorite-betrayal
pair (the rare construction favorite_betrayal_voting_301.md describes:
STAR's FBC leak lives in the runoff, because scores pick the
FINALISTS). A garden club of 57 picks the town flower. Nine voters
love Aster and Bluebell equally (5,5); six back Aster alone (5); a
broad, TEPID twenty-four give Bluebell a shrug of support (1); a solid
eighteen-voter bloc backs Clover (4). Bluebell is the Condorcet winner
— she beats Aster 24-6 and Clover 33-18 head-to-head — but her tepid
totals leave her THIRD in the score round (Aster 75, Clover 72,
Bluebell 69), three points shy of the runoff. Aster-vs-Clover goes to
Clover, 18-15 with 24 Equal Support. STAR elects Clover while the
compromise a majority prefers stands outside the door. Half 2
(bv2207_b6xrdr_fbc_betrayal_pays.yaml) shows the nine Aster-fans
fixing this by DEMOTING their favorite — they cannot fix it any other
way, because they already score Bluebell 5 (equal-top is free in STAR,
and here it is not enough).
Live on BetterVoting (Test ID BV2206): https://bettervoting.com/7mckyg
Live results: https://bettervoting.com/7mckyg/results (BV agrees:
Clover, no tiebreaks).

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Aster,Bluebell,Clover
9: 5,5,0
6: 5,0,0
24: 0,1,0
18: 0,0,4
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Clover
  Choose-One (Plurality) = Bluebell   (differs from STAR)
  RCV-IRV                = Bluebell   (differs from STAR)
  RCV-RR (Condorcet)     = Bluebell   (differs from STAR)
  Note: 9 of 57 ballots (16%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) sides with RCV-IRV, so STAR is the outlier
        here — STAR need not elect the Condorcet candidate.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2206_7mckyg_fbc_honest_tepid_consensus_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/bv2206_7mckyg_fbc_honest_tepid_consensus_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Aster)
 - Runoff Round Winner   = (Clover)
  Candidate Aster earned the highest total score, but
  Candidate Clover won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 57 ballots.
Count × Aster,Bluebell,Clover
   24 ×     0,       1,     0
   18 ×     0,       0,     4
    9 ×     5,       5,     0
    6 ×     5,       0,     0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Aster         -- 75 -- First place
   Clover        -- 72 -- Second place
   Bluebell      -- 69
 Aster and Clover advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Clover        -- 18 -- First place
   Aster         -- 15
   Equal Support -- 24
 Clover wins.
   Runoff math:
     57  ballots cast
   − 24  Equal Support (no preference between the two finalists)
     ──
     33  voters with a preference  (majority = 17)
           Clover 18 (55%)  ·  Aster 15 (45%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Clover
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Aster    |   Bluebell  |  * Clover   |
-------------------------------------------------------------
       * Aster > |     ---      | 6 - 27 - 24 |15 - 24 - 18 |
      Bluebell > | 24 - 27 -  6 |    ---      |33 -  6 - 18 |
      * Clover > | 18 - 24 - 15 |18 -  6 - 33 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Bluebell — STAR elected Clover instead (Bluebell was eliminated in the scoring round)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Aster      15   0   0   0   0  42  |    75   1.3
Bluebell    9   0   0   0  24  24  |    69   1.2
Clover      0  18   0   0   0  39  |    72   1.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2206_7mckyg_fbc_honest_tepid_consensus_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/favorite_betrayal/cases/bv2206_7mckyg_fbc_honest_tepid_consensus.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/IRV_DIFFERS_ARTIFACT/bv2206_7mckyg_fbc_honest_tepid_consensus.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [bv2207_b6xrdr_fbc_betrayal_pays](bv2207_b6xrdr_fbc_betrayal_pays.md)
