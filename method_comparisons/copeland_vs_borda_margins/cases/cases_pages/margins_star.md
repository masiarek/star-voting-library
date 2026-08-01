---
search:
  exclude: true
---

# Margins matter — STAR on the same twelve ballots (rank converted 5/3/0)

*Generated from [`margins_star.yaml`](../margins_star.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../01_STAR/concepts) · **1 seat** · **Expected winner:** Almond

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kdjjkq) · **[results ↗](https://bettervoting.com/kdjjkq/results)** (election `kdjjkq`).

## Scenario

The same twelve gelato voters, with each ranking converted to scores on an even 5/3/0 spacing so a SCORE method can run on a RANKED profile. Under a uniform spacing the STAR scoring round IS a Borda count, so round one reproduces Borda's answer — Berry first — and then the automatic runoff runs the head-to-head Borda never runs: Almond beats Berry 7-5, and Almond wins. Honest caveat, stated on the page: unlike Condorcet's 1788 profile, this outcome is NOT robust to the spacing. 5/3/0, 5/4/0, 5/2/0 and 4/2/0 all give Almond, but a polarized 5/1/0 makes Cocoa a finalist instead of Berry and elects Cocoa. With no Condorcet winner to anchor it (the pairwise contests cycle), the rank-to-score mapping is doing real work — which is exactly the objection the Borda page raises against inventing intensities.

## Parameters (from the YAML)

```yaml
voting_method: STAR
num_winners: 1
expected_winners:
- Almond
bv_election_id: kdjjkq
bv_test_id: BV2251
```

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Almond,Berry,Cocoa
5,3,0
5,3,0
5,3,0
5,3,0
5,3,0
0,5,3
0,5,3
0,5,3
3,0,5
3,0,5
0,3,5
0,3,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR     = Almond
  RCV-IRV  = Cocoa   (differs from STAR)
  Approval = Berry   (differs from STAR)
  RCV-RR   = Berry   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/margins_star_RCV-IRV_tabulated.txt
  RCV-RR round-robin: cases_tabulated/margins_star_RCV-RR_tabulated.txt

[Runoff Reversal]
 - Score Round Winner(s) = (Berry)
 - Runoff Round Winner   = (Almond)
  Candidate Berry earned the highest total score, but
  Candidate Almond won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 12 ballots.
Count × Almond,Berry,Cocoa
    5 ×      5,    3,    0
    3 ×      0,    5,    3
    2 ×      3,    0,    5
    2 ×      0,    3,    5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Berry         -- 36 -- First place
   Almond        -- 31 -- Second place
   Cocoa         -- 29
 Berry and Almond advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Almond        -- 7 -- First place
   Berry         -- 5
   Equal Support -- 0
 Almond wins.
   Runoff math:
     12  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     12  voters with a preference  (majority = 7)
           Almond 7 (58%)  ·  Berry 5 (42%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Almond
```

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
               |  * Almond  | * Berry   |   Cocoa   |
-----------------------------------------------------
    * Almond > |    ---     |7 - 0 - 5  |5 - 0 - 7  |
     * Berry > | 5 - 0 - 7  |   ---     |8 - 0 - 4  |
       Cocoa > | 7 - 0 - 5  |4 - 0 - 8  |   ---     |

[Condorcet Winner]
  No Condorcet winner (majority cycle: Almond > Berry > Cocoa > Almond)

[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Almond     5  0  2  0  0  5  |    31   2.6
Berry      3  0  7  0  0  2  |    36   3.0
Cocoa      4  0  3  0  0  5  |    29   2.4
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/margins_star_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/copeland_vs_borda_margins/cases/margins_star.yaml
```

## See also

- [Methods disagree on this election](../../../divergence_review/cases/CYCLE_OR_THREE_WAY/margins_star.md) — its entry in the divergence review ledger
- [Condorcet efficiency (topic hub)](../../../../07_Concepts/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [margins_irv](margins_irv.md) · [margins_paper_exact_304](margins_paper_exact_304.md) · [margins_ranked_robin](margins_ranked_robin.md)
