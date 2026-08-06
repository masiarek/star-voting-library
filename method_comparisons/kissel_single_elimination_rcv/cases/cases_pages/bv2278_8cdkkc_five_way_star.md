---
search:
  exclude: true
---

# Kissel's five-way example (STAR) — the compromise reaches the runoff and wins

*Generated from [`bv2278_8cdkkc_five_way_star.yaml`](../bv2278_8cdkkc_five_way_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** C

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8cdkkc) · **[results ↗](https://bettervoting.com/8cdkkc/results)** (election `8cdkkc` · test `BV2278`).

## Scenario

The same electorate as …_irv.yaml and …_rr.yaml — the five-candidate field from p.5 of Adam Kissel's "Can Ranked-Choice Voting Work? A Conservative Approach" — on a 0-5 score ballot instead of a ranking. The paper concedes that no form of RCV counts the A and B voters' second choices, and floats "an even more complicated point system" as a possible fix while dismissing it as voter confusion. That fix is STAR, and it is one grid on the ballot: the scoring round reads every ballot, C leads it (3221 to A's 2695), and the automatic runoff confirms the head-to-head the paper says is never revealed — C over A, 511-489. The scores are the paper's own preference order expressed as strengths; the ranked files hold the identical order.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

Markers on these ballots: `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all tabulate as 0 (reported honestly).

```text
Count:A,B,C,D,E
306:5,0,3,1,0     # A-partisans — moderate C is their second choice
300:0,5,3,1,0     # B-partisans — moderate C is their second choice too
111:3,1,5,0,0     # moderates leaning A
 91:1,3,5,0,0     # moderates leaning B
183:4,0,2,5,0     # D's voters lean A
  9:1,0,3,4,5     # the <1% candidate the paper says is eliminated first
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = C
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2278_8cdkkc_five_way_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 1000 ballots.
Count × A,B,C,D,E
  306 × 5,0,3,1,0
  300 × 0,5,3,1,0
  183 × 4,0,2,5,0
  111 × 3,1,5,0,0
   91 × 1,3,5,0,0
    9 × 1,0,3,4,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 3221 -- First place
   A             -- 2695 -- Second place
   B             -- 1884
   D             -- 1557
   E             --   45
 C and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 511 -- First place
   A             -- 489
   Equal Support --   0
 C wins.
   Runoff math:
     1000  ballots cast
   −    0  Equal Support (no preference between the two finalists)
     ────
     1000  voters with a preference  (majority = 501)
           C 511 (51%)  ·  A 489 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                    |       * A       |        B       |      * C       |        D       |        E       |
-----------------------------------------------------------------------------------------------------------
              * A > |       ---       |609 -   0 - 391 |489 -   0 - 511 |508 -   0 - 492 |691 - 300 -   9 |
                B > | 391 -   0 - 609 |      ---       |300 -   0 - 700 |502 -   0 - 498 |502 - 489 -   9 |
              * C > | 511 -   0 - 489 |700 -   0 - 300 |      ---       |808 -   0 - 192 |991 -   0 -   9 |
                D > | 492 -   0 - 508 |498 -   0 - 502 |192 -   0 - 808 |      ---       |789 - 202 -   9 |
                E > |   9 - 300 - 691 |  9 - 489 - 502 |  9 -   0 - 991 |  9 - 202 - 789 |      ---       |

[Condorcet Winner]
  Condorcet Winner: C — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: E — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                      Score
Candidate    5    4    3    2    1    0  | Total   Avg
A          306  183  111    0  100  300  |  2695   2.7
B          300    0   91    0  111  498  |  1884   1.9
C          202    0  615  183    0    0  |  3221   3.2
D          183    9    0    0  606  202  |  1557   1.6
E            9    0    0    0    0  991  |    45   0.0
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2278_8cdkkc_five_way_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/kissel_single_elimination_rcv/cases/bv2278_8cdkkc_five_way_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/IRV_OUTLIER_RR_WITH_STAR/bv2278_8cdkkc_five_way_star.md) — its entry in the divergence review ledger
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2277_tqfdbg_mayor_irv](bv2277_tqfdbg_mayor_irv.md) · [bv2277_tqfdbg_mayor_plurality](bv2277_tqfdbg_mayor_plurality.md) · [bv2277_tqfdbg_mayor_rr](bv2277_tqfdbg_mayor_rr.md) · [bv2277_tqfdbg_mayor_star](bv2277_tqfdbg_mayor_star.md) · [bv2278_8cdkkc_five_way_irv](bv2278_8cdkkc_five_way_irv.md) · [bv2278_8cdkkc_five_way_plurality](bv2278_8cdkkc_five_way_plurality.md) · [bv2278_8cdkkc_five_way_rr](bv2278_8cdkkc_five_way_rr.md)
