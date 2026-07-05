# BV95b — Majority Criterion: the favorite LOSES (majority backs TWO rivals)

*The same 5-voter STAR election as [BV95a](bv95a_9m6rxr_favorite_survives_one_rival.md), changed in one spot: the 3-voter majority that scores **Ada** highest now *also* gives **Cleo** a 3 (a second honestly-liked candidate) instead of 0. That one change makes **Ada — the top choice of a clear majority — lose.** This is STAR's [Majority-Criterion](../../00_start_here/topics/majority_criterion/README.md) failure, and it shows exactly how narrow it is.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/7pdq3r) · **[results ↗](https://bettervoting.com/7pdq3r/results)** (election `7pdq3r`).

Reference files: [`bv95b_7pdq3r_favorite_loses_two_rivals.yaml`](bv95b_7pdq3r_favorite_loses_two_rivals.yaml) (`expected_winners: [Bruno]`) · frozen export [`bv95b_7pdq3r_favorite_loses_two_rivals_bv_export.json`](bv95b_7pdq3r_favorite_loses_two_rivals_bv_export.json). Backs sheet row **BV95b**.

## The ballots

```
Ada,Bruno,Cleo
5,4,3     ← the 3-voter majority (×3): love Ada, but also back Bruno AND Cleo
0,5,5     ← the 2-voter minority (×2): reject Ada, love Bruno & Cleo
```

The only difference from BV95a is the majority's `Cleo` score: **3 instead of 0**.

## The STAR tabulation (LH)

```
[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  | Total   Avg
Ada        3  0  0  0  0  2  |    15   3.0
Bruno      2  3  0  0  0  0  |    22   4.4
Cleo       2  0  3  0  0  0  |    19   3.8

Scoring Round — the two highest scores advance:
   Bruno  -- 22 -- First place
   Cleo   -- 19 -- Second place
   Ada    -- 15                 ← Ada is now THIRD — eliminated before the runoff
 Bruno and Cleo advance.

Automatic Runoff:
   Bruno  -- 3 -- First place
   Cleo   -- 0
   Equal Support -- 2
 Bruno wins.

Winner — STAR Voting Method (single winner):  Bruno
```

Full audit copy: [`majority_criterion_tabulated/bv95b_7pdq3r_favorite_loses_two_rivals_tabulated.txt`](majority_criterion_tabulated/bv95b_7pdq3r_favorite_loses_two_rivals_tabulated.txt).

## Why Ada loses — and why it's mild

By also giving Cleo a 3, the majority pushed **Cleo's** total to 19 — above **Ada's** 15. Now the top two by score are Bruno (22) and Cleo (19), so **Ada never reaches the runoff**, despite being the outright favorite of 3 of 5 voters. The winner (Bruno) is the candidate almost everyone rates highly; the majority's own favorite (Ada) is the one 40% of voters score at 0.

The key lesson: it took the majority supporting **two** other candidates (Bruno *and* Cleo) to lose Ada. In BV95a, supporting only **one** left Ada safe. That gap — "needs two rivals, not one" — is exactly what Equal Vote's **Relaxed Majority Criterion** measures, and it's why STAR's majority-criterion failure is considered mild (Score and Approval can drop the favorite on a single supported rival). It is also the same event as a **Later-No-Harm** failure: the majority's honest 3 for Cleo (a *later* preference) is what harmed their favorite Ada. See the [topic hub](../../00_start_here/topics/majority_criterion/README.md).

## Confirmed on BetterVoting

Reproduced live at [`bettervoting.com/7pdq3r`](https://bettervoting.com/7pdq3r): BV also elects **Bruno** (`nTallyVotes 5`), matching LH. Election created via [`create_bv_test_election.py`](../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py).

## See also

- The concept, the Relaxed Majority Criterion, and the Later-No-Harm link: **[Majority Criterion topic hub](../../00_start_here/topics/majority_criterion/README.md)**.
- The twin where the favorite survives: [BV95a — majority backs only one rival](bv95a_9m6rxr_favorite_survives_one_rival.md).
- [STAR's honest limits #8](../../00_start_here/STAR_Voting/STAR_honest_limits.md).
