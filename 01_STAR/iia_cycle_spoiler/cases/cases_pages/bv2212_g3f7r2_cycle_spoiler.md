# STAR's runoff is spoiler-sensitive under a Condorcet cycle — a losing candidate (Ben) flips Alice vs Carla (BV2212, g3f7r2)

*Generated from [`bv2212_g3f7r2_cycle_spoiler.yaml`](../bv2212_g3f7r2_cycle_spoiler.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Alice

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/g3f7r2) · **[results ↗](https://bettervoting.com/g3f7r2/results)** (election `g3f7r2`).

## Scenario

STAR's sharpest honest limit, made mechanical. 23 voters, three candidates,
three rotating factions voting SINCERELY (favorite 5, compromise 3, last 0).
The head-to-head results form a Condorcet CYCLE — Alice beats Ben, Ben beats
Carla, Carla beats Alice — so there is NO Condorcet winner.

Scoring round: Alice 71, Ben 60, Carla 53 — the finalists are Alice and Ben,
and Alice wins the automatic runoff (Alice beats Ben head-to-head). STAR elects
Alice, and BetterVoting agrees deterministically (no tie: tieBreakType "none").

Now delete Ben — who never had a chance to win. With only Alice and Carla
scored, the finalists become Alice (71) and Carla (53), and the runoff FLIPS:
Carla beats Alice head-to-head, so STAR would elect Carla. A losing candidate
(Ben) decided whether Alice or Carla wins, with not one voter changing a single
score. That is an Independence-of-Irrelevant-Alternatives (IIA) failure
introduced by the runoff STAGE — a cardinal ballot, but an ordinal finish, and
the cycle is exactly where the two values pull apart. It needs no strategy: the
ballots are perfectly sincere. (Origin: r/EndFPTP, Excellent_Air8235, 2026-07.)

Bonus divergence — one election separates all three ranked/score counts of the
same opinions: STAR = Alice, RCV-IRV = Carla (Ben eliminated first, transfers
to Carla), Ranked Robin = Alice (Copeland 3-way tie, broken by LH margin). The
RR result is a tie-break, so it is NOT freezable on BV (BV breaks the Copeland
tie randomly) — this case ships STAR-only, like BV830.

Live results: https://bettervoting.com/g3f7r2/results
Lesson: bv2212_g3f7r2_cycle_spoiler.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Alice, Ben, Carla
    3,   0,     5
    5,   3,     0
    5,   3,     0
    0,   5,     3
    5,   3,     0
    3,   0,     5
    3,   0,     5
    5,   3,     0
    5,   3,     0
    3,   0,     5
    5,   3,     0
    0,   5,     3
    0,   5,     3
    0,   5,     3
    3,   0,     5
    5,   3,     0
    0,   5,     3
    3,   0,     5
    5,   3,     0
    0,   5,     3
    5,   3,     0
    3,   0,     5
    5,   3,     0
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR    = Alice
  RCV-IRV = Carla   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2212_g3f7r2_cycle_spoiler_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 23 ballots.
Count × Alice,Ben,Carla
   10 ×     5,  3,    0
    7 ×     3,  0,    5
    6 ×     0,  5,    3

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Alice         -- 71 -- First place
   Ben           -- 60 -- Second place
   Carla         -- 53
 Alice and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Alice         -- 17 -- First place
   Ben           --  6
   Equal Support --  0
 Alice wins.
   Runoff math:
     23  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     23  voters with a preference  (majority = 12)
           Alice 17 (74%)  ·  Ben 6 (26%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Alice
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |   * Alice    |   * Ben     |    Carla    |
-------------------------------------------------------------
       * Alice > |     ---      |17 -  0 -  6 |10 -  0 - 13 |
         * Ben > |  6 -  0 - 17 |    ---      |16 -  0 -  7 |
         Carla > | 13 -  0 - 10 | 7 -  0 - 16 |    ---      |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Alice > Ben > Carla > Alice)

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Alice      10   0   7   0   0   6  |    71   3.1
Ben         6   0  10   0   0   7  |    60   2.6
Carla       7   0   6   0   0  10  |    53   2.3
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2212_g3f7r2_cycle_spoiler_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/iia_cycle_spoiler/cases/bv2212_g3f7r2_cycle_spoiler.yaml
```

## See also

- [Methods disagree on this election](../../../../method_comparisons/divergence_review/cases/CYCLE_OR_THREE_WAY/bv2212_g3f7r2_cycle_spoiler.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Ties & tie-breaking (topic hub)](../../../../00_start_here/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
