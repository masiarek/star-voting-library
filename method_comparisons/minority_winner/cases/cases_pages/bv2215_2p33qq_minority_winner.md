# Minority winner — 34% wins Choose-One, but STAR & Ranked Robin elect the majority's real choice (BV2215, 2p33qq)

*Generated from [`bv2215_2p33qq_minority_winner.yaml`](../bv2215_2p33qq_minority_winner.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [STAR (single winner)](../../../../00_start_here/STAR_Voting) · **1 seat** · **Expected winner:** Cleo

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/2p33qq) · **[results ↗](https://bettervoting.com/2p33qq/results)** (election `2p33qq`).

## Scenario

The canonical minority-winner example. 100 voters, three candidates for a seat.
Ada has a passionate third of the room: 34 people rank her first — so under
Choose-One (Plurality), where only your top pick counts, Ada WINS with 34%. But
she's a minority winner: 66 of the 100 voters score her 0 or 1. Cleo is the
opposite — nobody's fiery favorite (only 33 first choices), but everyone's warm
second (most rate her 4 or 5). Reading the whole ballot finds her: Cleo leads
STAR's scoring round (433), wins the automatic runoff over Ada 66-34, and beats
both rivals head-to-head (the Condorcet winner). So STAR and Ranked Robin both
elect Cleo, the candidate a majority is genuinely glad about; only first-choice
counting crowns Ada on a third of the vote. Same opinions, no strategy — the whole
difference is how much of the ballot the method reads. (It can be worse: with a
bigger field, Choose-One winners can take office on 10-20%. A third is just the
most common, most believable version.)
Live results (BV2215): https://bettervoting.com/2p33qq/results
Lesson: 00_start_here/topics/plurality.md · README.md

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Ada,Ben,Cleo
34:5,0,4
33:0,5,4
33:2,1,5
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

```text
[Divergence from STAR]
  STAR                   = Cleo
  Choose-One (Plurality) = Ada   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Ada,Ben,Cleo
   34 ×   5,  0,   4
   33 ×   0,  5,   4
   33 ×   2,  1,   5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Cleo          -- 433 -- First place
   Ada           -- 236 -- Second place
   Ben           -- 198
 Cleo and Ada advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cleo          -- 66 -- First place
   Ada           -- 34
   Equal Support --  0
 Cleo wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Cleo 66 (66%)  ·  Ada 34 (34%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Cleo
```

<details>
<summary>Full audit — preference matrix, Condorcet, and score distribution</summary>

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ada     |     Ben     |   * Cleo    |
-------------------------------------------------------------
         * Ada > |     ---      |67 -  0 - 33 |34 -  0 - 66 |
           Ben > | 33 -  0 - 67 |    ---      |33 -  0 - 67 |
        * Cleo > | 66 -  0 - 34 |67 -  0 - 33 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Cleo — matches the STAR winner

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ada        34   0   0  33   0  33  |   236   2.4
Ben        33   0   0   0  33  34  |   198   2.0
Cleo       33  67   0   0   0   0  |   433   4.3
```

</details>

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv2215_2p33qq_minority_winner_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/minority_winner/cases/bv2215_2p33qq_minority_winner.yaml
```

## See also

- [Condorcet efficiency (topic hub)](../../../../00_start_here/topics/condorcet/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/runoff_overturns_leader/README.md)
- [Glossary](../../../../00_start_here/GLOSSARY.md) · [all cases by method](../../../../00_start_here/YAML_test_case_index/README.md)
