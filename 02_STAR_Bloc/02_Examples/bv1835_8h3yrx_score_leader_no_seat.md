# BV1835 — Bloc STAR, 100 voters, 4 seats: the score leader wins no seat

<!-- case-meta:start — managed by build_yaml_pages.py; edit the YAML, not these lines -->
**Method:** [Bloc STAR (multi-winner, majoritarian)](../../03_STAR_PR/01_Learn/README.md) · **4 seats** · **Expected winners:** Bianca, Cedric, Deegan, Eli · [full count →](cases/cases_pages/bv1835_8h3yrx_score_leader_no_seat.md)
<!-- case-meta:end -->

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/8h3yrx) · **[results ↗](https://bettervoting.com/8h3yrx/results)** (election `8h3yrx` · test `BV1835`).

*Sass's Bloc STAR example, run as a real BetterVoting election (id `8h3yrx`, 100 ballots). Ava leads the scoring round of **all four** rounds by sixty-three points and takes **no seat**, losing every automatic runoff 51–49. LH and BetterVoting agree exactly: winners **Bianca, Cedric, Deegan, Eli**.*

Reference files: [`bv1835_8h3yrx_score_leader_no_seat.yaml`](cases/bv1835_8h3yrx_score_leader_no_seat.yaml) (`expected_winners: [Bianca, Cedric, Deegan, Eli]`) · frozen export [`bv1835_8h3yrx_score_leader_no_seat_bv_export.json`](cases/bv1835_8h3yrx_score_leader_no_seat_bv_export.json) (BV `8h3yrx`) · full count [`bv1835_8h3yrx_score_leader_no_seat.md`](cases/cases_pages/bv1835_8h3yrx_score_leader_no_seat.md). Backs sheet row **BV1835**.

This is the first case in this folder at a realistic electorate — every other one here is 2–16 ballots.

## The election

Bloc STAR, 5 candidates, 4 seats, 100 ballots — five voter blocs:

```
Count × Ava,Bianca,Cedric,Deegan,Eli
   25 ×   3,     5,     4,     0,  0
   24 ×   3,     4,     5,     0,  0
   25 ×   3,     0,     0,     5,  4
   24 ×   3,     0,     0,     4,  5
    2 ×   0,     5,     4,     3,  2
```

Totals: **Ava 294**, Bianca 231, Cedric 228, Deegan 227, Eli 224.

The structure is two mirror-image camps of 49 that share no candidates — one scores Bianca and Cedric 5/4 and zeroes Deegan and Eli, the other does the reverse — plus a 2-ballot swing bloc.

## What makes it interesting

**Ava is simultaneously the score leader and the Condorcet loser.** 98 of the 100 voters give her a 3, which is enough to put her first in every scoring round by a wide margin. It is also the *lowest* score either camp awards to anyone they didn't zero: each camp ranks its own two candidates above her. So on Ava-versus-anyone the two camps split 49–49, and the 2 swing voters — who score Ava 0 and everyone else 5/4/3/2 — turn every one of those into **51–49**. She loses all four head-to-heads and finishes with nothing.

Three things worth drawing out:

- **This is the runoff step, not a bug.** Bloc STAR seats whoever is *preferred* head to head, not whoever accumulates the most points. A broadly acceptable candidate who is nobody's favourite can be shut out of an entire four-seat body. The engine flags it as a Runoff Reversal in all four rounds.
- **It is *not* a majority sweep.** The usual Bloc complaint is that a cohesive majority takes every seat; here the two camps split the seats 2–2 and the result is arguably well-balanced. It is the compromise candidate alone who is excluded — a different failure mode from the one [the section README](../README.md) warns about.
- **Approval would elect her.** Scoring Ava 3 clears the approval threshold, so under Approval she wins 98 approvals to everyone else's 51/51/51/49. The method that asks only "is this person acceptable?" seats her first; the method that asks "which of these two do you prefer?" never does. That contrast is the whole lesson in one election.

Compare [BV1525](bv1525_condorcet_loser_bloc.md), where a Score *co-leader* is a near-Condorcet loser on 16 ballots. BV1835 is the full-strength version at 100.

## View 1 — BetterVoting

Result: **Bianca, Cedric, Deegan, Eli** — elected in that seat order. `nTallyVotes: 100`, `nAbstentions: 0`, `tieBreakType: "none"` in all four rounds. No tie, no lot; the whole result is deterministic and both engines reach it independently.

*(Aside: the export labels `votingMethod: "STAR"` with `num_winners: 4` — "Bloc STAR" is never written down. See the [#1086 method-name note](bv129_1086_method_name_note.md).)*

## View 2 — the LH report (inline)

<!-- report:bv1835_8h3yrx_score_leader_no_seat -->
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
<!-- /report -->
Rounds 2, 3 and 4 are the same shape: Ava leads the scoring round, meets the next candidate in the runoff, and loses it 51–49. Full audit copy: [`cases_tabulated/bv1835_8h3yrx_score_leader_no_seat_tabulated.txt`](cases/cases_tabulated/bv1835_8h3yrx_score_leader_no_seat_tabulated.txt).

## Cross-check against EPR

Stevan Leonard ran these same 100 ballots through [EPRv3](https://github.com/lsleonard/evaluative-proportional-representation) in September 2023 and reported weights A: 0, B: 27, C: 24, D: 25, E: 24 — the **same four winners**, ordered B, D, C, E. A majoritarian method and a proportional one both exclude the score leader, which is a stronger statement than either makes alone.

Two caveats before leaning on that comparison. EPR's scale is 1–6 with **1 = Reject**, not 0–5, so the ballots had to be remapped; the mapping used lives only in that email thread, and the result depends on it. And Leonard had to raise EPR's retention cap from 20% to 30% for this run, because the highest weight came out at 27%. It is not the same test case as the EPR repo's bundled simulated election ([`epr-voter-data-v2/v3`](https://github.com/lsleonard/evaluative-proportional-representation/tree/master/EPR-Simulated-Election) — 70 voters, 10 candidates, 7 seats).

## Related

- The section's own framing of majoritarian-vs-proportional: [02_STAR_Bloc README](../README.md) · the proportional cousin: [STAR-PR](../../03_STAR_PR/README.md)
- A Score co-leader as near-Condorcet loser, 16 ballots: [BV1525](bv1525_condorcet_loser_bloc.md)
- The clean no-tie control: [`00_c3_b3_bloc-baseline-2-seats`](cases/cases_pages/00_c3_b3_bloc-baseline-2-seats.md)
- The method-name label ("STAR" vs "Bloc STAR"): [#1086 note](bv129_1086_method_name_note.md)
