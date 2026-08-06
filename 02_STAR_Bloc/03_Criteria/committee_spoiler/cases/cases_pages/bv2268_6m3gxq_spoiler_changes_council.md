---
search:
  exclude: true
---

# BV2268 — Committee spoiler (2 of 2): a fourth candidate wins nothing and changes who does

*Generated from [`bv2268_6m3gxq_spoiler_changes_council.yaml`](../bv2268_6m3gxq_spoiler_changes_council.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../../03_STAR_PR/01_Learn/README.md) · **2 seats** · **Expected winners:** Cyrus, Bea

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6m3gxq) · **[results ↗](https://bettervoting.com/6m3gxq/results)** (election `6m3gxq` · test `BV2268`).

## Scenario

The same seven voters and the same two seats as BV2267 (my9jd9), with a fourth
candidate on the ballot: Dane. Every score anyone gave Ari, Bea and Cyrus is
unchanged; the voters simply also say what they think of Dane.

  - Seat 1: scores Cyrus 17, Dane 17, Bea 16, Ari 11. Dane's arrival pushes
    Bea out of the finalist pair; Cyrus beats Dane 4-3 and takes the seat —
    the same seat-1 winner as the control.
  - Seat 2: Cyrus is removed. Dane 17, Bea 16, Ari 11, so Ari — who won this
    seat in the control election — is not even a finalist. Bea beats Dane 4-2.

Council: Cyrus and Bea, where the same ballots without Dane elected Cyrus and
Ari. Dane wins nothing and loses both runoffs he reaches.

This is a failure of independence of irrelevant alternatives at the level of
the committee, and note what it did NOT need: no Condorcet cycle (unlike the
single-winner spoiler case) and no tie-break. Each seat rebuilds the finalist
pair from whoever is left, so an also-ran with a competitive score can crowd
out the candidate who would otherwise have won that seat.

Reproduced on BetterVoting (election 6m3gxq): BV elects Cyrus then Bea,
nTallyVotes 7, tieBreakType none — an exact match with the LH count. Frozen
export: bv2268_6m3gxq_spoiler_changes_council_bv_export.json.
Live results: https://bettervoting.com/6m3gxq/results

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ari,Bea,Cyrus,Dane
5,3,3,0
0,3,4,2
1,0,1,5
0,5,2,1
4,2,4,1
1,0,1,5
0,3,2,3
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Cyrus
  Choose-One (Plurality) = Ari   (differs from STAR)
  RCV-IRV                = Bea   (differs from STAR)
  Approval               = Bea   (differs from STAR)
  Note: 5 of 7 ballots (71%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2268_6m3gxq_spoiler_changes_council_RCV-IRV_tabulated.txt

--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 7 ballots to fill 2 seats.
Count × Ari,Bea,Cyrus,Dane
    2 ×   1,  0,    1,   5
    1 ×   5,  3,    3,   0
    1 ×   0,  3,    4,   2
    1 ×   0,  5,    2,   1
    1 ×   4,  2,    4,   1
    1 ×   0,  3,    2,   3

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cyrus         -- 17 -- First place
   Dane          -- 17 -- Second place
   Bea           -- 16
   Ari           -- 11
 Cyrus and Dane advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cyrus         -- 4 -- First place
   Dane          -- 3
   Equal Support -- 0
 Cyrus wins.
   Runoff math:
     7  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     7  voters with a preference  (majority = 4)
           Cyrus 4 (57%)  ·  Dane 3 (43%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Dane          -- 17 -- First place
   Bea           -- 16 -- Second place
   Ari           -- 11
 Dane and Bea advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bea           -- 4 -- First place
   Dane          -- 2
   Equal Support -- 1
 Bea wins.
   Runoff math:
     7  ballots cast
   − 1  Equal Support (no preference between the two finalists)
     ─
     6  voters with a preference  (majority = 4)
           Bea 4 (67%)  ·  Dane 2 (33%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Cyrus
 Bea
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |     Ari    |    Bea    | * Cyrus   |  * Dane   |
-----------------------------------------------------------------
         Ari > |    ---     |4 - 0 - 3  |1 - 3 - 3  |2 - 0 - 5  |
         Bea > | 3 - 0 - 4  |   ---     |2 - 1 - 4  |4 - 1 - 2  |
     * Cyrus > | 3 - 3 - 1  |4 - 1 - 2  |   ---     |4 - 0 - 3  |
      * Dane > | 5 - 0 - 2  |2 - 1 - 4  |3 - 0 - 4  |   ---     |

[Condorcet Winner]
  Condorcet Winner: Cyrus — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ari        1  1  0  0  2  3  |    11   1.6
Bea        1  0  3  1  0  2  |    16   2.3
Cyrus      0  2  1  2  2  0  |    17   2.4
Dane       2  0  1  1  2  1  |    17   2.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2268_6m3gxq_spoiler_changes_council_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/03_Criteria/committee_spoiler/cases/bv2268_6m3gxq_spoiler_changes_council.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../../07_Concepts/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2267_my9jd9_council_before_dane](bv2267_my9jd9_council_before_dane.md)
