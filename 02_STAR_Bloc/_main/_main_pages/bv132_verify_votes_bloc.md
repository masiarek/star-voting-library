# BV132 — verify number of votes cast (Bloc STAR, 2 seats)

*Generated from [`bv132_verify_votes_bloc.yaml`](../bv132_verify_votes_bloc.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../00_start_here/proportional_representation) · **2 seats** · **Expected winners:** C, B

## Scenario

Bloc STAR, 3 candidates, 2 seats, 4 ballots — two of them "flat" (every
candidate scored the same: 1,1,1 and 5,5,5). This is the LH reference for
BetterVoting test BV132 / issue #1073 ("verify number of votes cast").

LH counts ALL 4 ballots: totals C=12, B=10, A=8.
  - Seat 1: C and B advance; in the runoff C is preferred (C 2, B 0, Equal 2),
    so C takes seat 1.
  - Seat 2: remove C; B beats A in the runoff (B 2, A 0, Equal 2), so B takes
    seat 2.
Winners: C, B.

The BV bug (#1073): BetterVoting reports only "2 voters" with totals A=2, B=4,
C=6 — which is exactly the two non-flat ballots (1,2,3 and 1,2,3). It has
DROPPED the two flat ballots, the same "flat ballot treated as an abstention"
family as #1407 / #1035. Note the winners (C, B) are UNAFFECTED — a flat ballot
adds equally to every candidate and is Equal in every head-to-head, so it can
never change a STAR/Bloc result. The defect is the vote-count / turnout display,
not the winner.

Confirmed from the frozen BV export (election 3494cb, bv132_..._bv_export.json):
all 4 ballots ARE stored in the export's Ballots array — so ingestion is fine.
The drop happens in TABULATION: summaryData reports nAbstentions=2, nTallyVotes=2,
i.e. BV classifies the two flat ballots as abstentions and tallies only the two
1,2,3 ballots (A=2, B=4, C=6). Same root cause as #1407 (flat ballot mis-filed
as abstention). The export also labels votingMethod "STAR" rather than "Bloc
STAR" — cf. #904.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
A,B,C
1,1,1
5,5,5
1,2,3
1,2,3
```

## What the engine says

Full report from the [`_tabulated` mirror](../_main_tabulated/bv132_verify_votes_bloc_tabulated.txt) (regenerated on every run; every analysis forced on):

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |      A     |   * B     |   * C     |
-----------------------------------------------------
           A > |    ---     |0 - 2 - 2  |0 - 2 - 2  |
         * B > | 2 - 2 - 0  |   ---     |0 - 2 - 2  |
         * C > | 2 - 2 - 0  |2 - 2 - 0  |   ---     |

[Condorcet Winner]
  Condorcet Winner: C — matches the STAR winner

[Divergence from STAR]
  STAR                   = C
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Note: 2 of 4 ballots (50%) had equal non-zero scores, so their ranks were
        decided by candidate priority order. The RCV-IRV result may be an
        artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: _main_tabulated/bv132_verify_votes_bloc_RCV-IRV_tabulated.txt

--- Bloc STAR Voting Method (2 winners) ---
[Bloc STAR]
 Tabulating 4 ballots.
Count × A,B,C
    2 × 1,2,3
    1 × 1,1,1
    1 × 5,5,5

[Score Distribution] (number of ballots giving each score)
   5  4  3  2  1  0  | Total   Avg
A  1  0  0  0  3  0  |     8   2.0
B  1  0  0  2  1  0  |    10   2.5
C  1  0  2  0  1  0  |    12   3.0
 Want to fill 2 seats.

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 12 -- First place
   B             -- 10 -- Second place
   A             --  8
 C and B advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 2 -- First place
   B             -- 0
   Equal Support -- 2
 C wins.
   Runoff math:
     4  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           C 2 (100%)  ·  B 0 (0%)

──────────────────────────────────────────────────
[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   B             -- 10 -- First place
   A             --  8 -- Second place
 B and A advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   B             -- 2 -- First place
   A             -- 0
   Equal Support -- 2
 B wins.
   Runoff math:
     4  ballots cast
   − 2  Equal Support (no preference between the two finalists)
     ─
     2  voters with a preference  (majority = 2)
           B 2 (100%)  ·  A 0 (0%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 C
 B
```

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/_main/bv132_verify_votes_bloc.yaml
```

## See also

- [Runoff reversal (worked set)](../../../01_STAR/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../00_start_here/ballot_and_terminology_basics.md)
- [Glossary](../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../00_start_here/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md)
