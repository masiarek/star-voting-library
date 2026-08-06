---
search:
  exclude: true
---

# The mayor's race (STAR) — one grid, and Cora wins the runoff 69-31

*Generated from [`bv2277_tqfdbg_mayor_star.yaml`](../bv2277_tqfdbg_mayor_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/01_Learn/README.md) · **1 seat** · **Expected winner:** Cora

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/tqfdbg) · **[results ↗](https://bettervoting.com/tqfdbg/results)** (election `tqfdbg` · test `BV2277`).

## Scenario

The same 100-voter mayoral race as …_irv.yaml and …_rr.yaml, on a 0-5 score ballot. Cora leads the scoring round (356 to Blake's 280) and wins the automatic runoff 69-31. The paper asks for a ballot that is "one grid for the first choice and a separate one for the second choice" and for a count with no rounds to keep track of; STAR is one grid, one pass, and no elimination order — and on these ballots it finds the majority-preferred candidate that the paper's two-column model does not. Scores express the same preference order the ranked companions hold.

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Blake,Cora,Dean
33:5,1,3,0     # Ada's voters — Cora is their second choice
31:1,5,3,0     # Blake's voters — Cora is their second choice too
20:1,3,5,0     # the moderates, leaning Blake
16:0,2,4,5     # Dean's voters — Cora again
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR                   = Cora
  Choose-One (Plurality) = Ada   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Ada,Blake,Cora,Dean
   33 ×   5,    1,   3,   0
   31 ×   1,    5,   3,   0
   20 ×   1,    3,   5,   0
   16 ×   0,    2,   4,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cora          -- 356 -- First place
   Blake         -- 280 -- Second place
   Ada           -- 216
   Dean          --  80
 Cora and Blake advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cora          -- 69 -- First place
   Blake         -- 31
   Equal Support --  0
 Cora wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Cora 69 (69%)  ·  Blake 31 (31%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cora
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |      Ada     |  * Blake    |   * Cora    |     Dean    |
---------------------------------------------------------------------------
           Ada > |     ---      |33 -  0 - 67 |33 -  0 - 67 |84 -  0 - 16 |
       * Blake > | 67 -  0 - 33 |    ---      |31 -  0 - 69 |84 -  0 - 16 |
        * Cora > | 67 -  0 - 33 |69 -  0 - 31 |    ---      |84 -  0 - 16 |
          Dean > | 16 -  0 - 84 |16 -  0 - 84 |16 -  0 - 84 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Cora — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Dean — loses every head-to-head matchup

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ada        33   0   0   0  51  16  |   216   2.2
Blake      31   0  20  16  33   0  |   280   2.8
Cora       20  16  64   0   0   0  |   356   3.6
Dean       16   0   0   0   0  84  |    80   0.8
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2277_tqfdbg_mayor_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/kissel_single_elimination_rcv/cases/bv2277_tqfdbg_mayor_star.yaml
```

## See also

- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [bv2277_tqfdbg_mayor_irv](bv2277_tqfdbg_mayor_irv.md) · [bv2277_tqfdbg_mayor_plurality](bv2277_tqfdbg_mayor_plurality.md) · [bv2277_tqfdbg_mayor_rr](bv2277_tqfdbg_mayor_rr.md) · [kissel_five_way_c5_b1000_irv](kissel_five_way_c5_b1000_irv.md) · [kissel_five_way_c5_b1000_rr](kissel_five_way_c5_b1000_rr.md) · [kissel_five_way_c5_b1000_star](kissel_five_way_c5_b1000_star.md)
