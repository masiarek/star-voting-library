---
search:
  exclude: true
---

# BV1835 — Bloc STAR, 100 voters, 4 seats: the score leader wins no seat

*Generated from [`bv1835_8h3yrx_score_leader_no_seat.yaml`](../bv1835_8h3yrx_score_leader_no_seat.yaml) — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_yaml_pages.py`.*

**Method:** [Bloc STAR (multi-winner, majoritarian)](../../../../03_STAR_PR/01_Learn) · **4 seats** · **Expected winners:** Bianca, Cedric, Deegan, Eli

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8h3yrx) · **[results ↗](https://bettervoting.com/8h3yrx/results)** (election `8h3yrx` · test `BV1835`).

## Scenario

The LH reference for BetterVoting test BV1835 (a real election, id 8h3yrx).
Sass's Bloc STAR example at 100 voters — the first case in this folder at a
realistic electorate; every other one here is 2-16 ballots.

Bloc STAR, 5 candidates, 4 seats, 100 ballots.
Totals: Ava=294, Bianca=231, Cedric=228, Deegan=227, Eli=224.

Ava is the compromise candidate: 98 of the 100 voters score her 3, and she
leads the SCORING round of all four rounds by a wide margin (294 against a
best rival of 231). She wins NO seat. Each round she reaches the automatic
runoff and loses it 51-49.

Why: the electorate is two mirror-image camps of 49 that share no candidates.
One camp scores Bianca and Cedric 5/4 and zeroes Deegan and Eli; the other
does the reverse. Both camps score Ava 3 — above the pair they zeroed, below
their own two. So on Ava-vs-anyone the camps split 49-49, and the 2-ballot
swing bloc (which scores Ava 0 and everyone else 5/4/3/2) turns every one of
those into 51-49.

Winners: Bianca, Cedric, Deegan, Eli. BetterVoting agrees exactly — elected in
that seat order, tieBreakType "none" in all four rounds, nTallyVotes 100,
nAbstentions 0. No tie, no lot; the whole result is deterministic.

The lesson is the runoff step. Bloc STAR seats whoever is PREFERRED head to
head, not whoever accumulates the most points, so a broadly acceptable
candidate who is nobody's favourite can be shut out of the entire body. Note
this is NOT the usual Bloc complaint: no majority sweeps here — the two camps
split the seats 2-2. It is the score leader alone who is excluded.

(Aside: the BV export labels votingMethod "STAR" with num_winners 4 — "Bloc
STAR" is never written down; #1086.)

## Ballots

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ava,Bianca,Cedric,Deegan,Eli
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,5,4,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,4,5,0,0
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,5,4
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
3,0,0,4,5
0,5,4,3,2
0,5,4,3,2
```

## What the engine says

The count, step by step — the rounds and how the winner is reached:

<!-- --8<-- [start:report] -->
```text
[Divergence from STAR]
  STAR     = Bianca
  Approval = Ava   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Ava)
 - Runoff Round Winner   = (Bianca)
  Candidate Ava earned the highest total score, but
  Candidate Bianca won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- Bloc STAR Voting Method (4 winners) ---

[Bloc STAR]
 Tabulating 100 ballots to fill 4 seats.
Count × Ava,Bianca,Cedric,Deegan,Eli
   25 ×   3,     5,     4,     0,  0
   25 ×   3,     0,     0,     5,  4
   24 ×   3,     4,     5,     0,  0
   24 ×   3,     0,     0,     4,  5
    2 ×   0,     5,     4,     3,  2

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ava           -- 294 -- First place
   Bianca        -- 231 -- Second place
   Cedric        -- 228
   Deegan        -- 227
   Eli           -- 224
 Ava and Bianca advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bianca        -- 51 -- First place
   Ava           -- 49
   Equal Support --  0
 Bianca wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Bianca 51 (51%)  ·  Ava 49 (49%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ava           -- 294 -- First place
   Cedric        -- 228 -- Second place
   Deegan        -- 227
   Eli           -- 224
 Ava and Cedric advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Cedric        -- 51 -- First place
   Ava           -- 49
   Equal Support --  0
 Cedric wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Cedric 51 (51%)  ·  Ava 49 (49%)

──────────────────────────────────────────────────

[Bloc STAR: Round 3: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ava           -- 294 -- First place
   Deegan        -- 227 -- Second place
   Eli           -- 224
 Ava and Deegan advance.

[Bloc STAR: Round 3: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Deegan        -- 51 -- First place
   Ava           -- 49
   Equal Support --  0
 Deegan wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Deegan 51 (51%)  ·  Ava 49 (49%)

──────────────────────────────────────────────────

[Bloc STAR: Round 4: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Ava           -- 294 -- First place
   Eli           -- 224 -- Second place
 Ava and Eli advance.

[Bloc STAR: Round 4: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Eli           -- 51 -- First place
   Ava           -- 49
   Equal Support --  0
 Eli wins.
   Runoff math:
     100  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     100  voters with a preference  (majority = 51)
           Eli 51 (51%)  ·  Ava 49 (49%)

[Bloc STAR: Winners — Bloc STAR Voting Method (4 winners)]
 Bianca
 Cedric
 Deegan
 Eli
```
<!-- --8<-- [end:report] -->

### Full audit — preference matrix, Condorcet, and score distribution

```text
--- Runoff (Preference) Matrix ---
Head-to-head / pairwise comparison
Legend: For - Equal Support - Against
        * indicates Top 2 Finalist
                 |    * Ava     |  * Bianca   |    Cedric   |    Deegan   |     Eli     |
-----------------------------------------------------------------------------------------
         * Ava > |     ---      |49 -  0 - 51 |49 -  0 - 51 |49 -  0 - 51 |49 -  0 - 51 |
      * Bianca > | 51 -  0 - 49 |    ---      |27 - 49 - 24 |51 -  0 - 49 |51 -  0 - 49 |
        Cedric > | 51 -  0 - 49 |24 - 49 - 27 |    ---      |51 -  0 - 49 |51 -  0 - 49 |
        Deegan > | 51 -  0 - 49 |49 -  0 - 51 |49 -  0 - 51 |    ---      |27 - 49 - 24 |
           Eli > | 51 -  0 - 49 |49 -  0 - 51 |49 -  0 - 51 |24 - 49 - 27 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Bianca — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Ava — loses every head-to-head matchup — elected by Approval!

[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Ava         0   0  98   0   0   2  |   294   2.9
Bianca     27  24   0   0   0  49  |   231   2.3
Cedric     24  27   0   0   0  49  |   228   2.3
Deegan     25  24   2   0   0  49  |   227   2.3
Eli        24  25   0   2   0  49  |   224   2.2
```

Everything in one file: the [`_tabulated` mirror](../cases_tabulated/bv1835_8h3yrx_score_leader_no_seat_tabulated.txt) (regenerated on every run; every analysis forced on).

Run it yourself:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 02_STAR_Bloc/02_Examples/cases/bv1835_8h3yrx_score_leader_no_seat.yaml
```

## See also

- [Ties & tie-breaking (topic hub)](../../../../07_Concepts/topics/ties/README.md)
- [The tie-breaking ladder (full chain)](../../../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md)
- [Vote splitting (worked set)](../../../../method_comparisons/split_voting/README.md)
- [Runoff reversal (worked set)](../../../../01_STAR/02_Examples/runoff_overturns_leader/README.md)
- [Ballot & terminology basics](../../../../07_Concepts/topics/ballot_and_terminology_basics.md)
- [Glossary](../../../../07_Concepts/GLOSSARY.md) · [all cases by method](../../../../07_Concepts/YAML_test_case_index/README.md)

More cases in this set: [00_c3_b3_bloc-baseline-2-seats](00_c3_b3_bloc-baseline-2-seats.md) · [01_c4_b2_bloc-star-2-seats](01_c4_b2_bloc-star-2-seats.md) · [bloc_lot_path_dependence_a_c3_b5](bloc_lot_path_dependence_a_c3_b5.md) · [bloc_lot_path_dependence_b_c3_b5](bloc_lot_path_dependence_b_c3_b5.md) · [bv129_score_tiebreak_bloc](bv129_score_tiebreak_bloc.md) · [bv130_bloc_pagination_731](bv130_bloc_pagination_731.md) · [bv130r2_dead_rung_bloc](bv130r2_dead_rung_bloc.md) · [bv131_guido_bloc](bv131_guido_bloc.md) · [bv132_verify_votes_bloc](bv132_verify_votes_bloc.md) · [bv1525_condorcet_loser_bloc](bv1525_condorcet_loser_bloc.md) · [bv1815_bloc_3c2s_basic](bv1815_bloc_3c2s_basic.md) · [bv2105_r4dqvd_ice_cream_bloc](bv2105_r4dqvd_ice_cream_bloc.md) · [bv750_tie_breaking_bloc](bv750_tie_breaking_bloc.md) · [lackner_skowron_shadow_bloc_star_c7_b12](lackner_skowron_shadow_bloc_star_c7_b12.md)
