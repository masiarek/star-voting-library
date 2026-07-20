# Ice cream ladder — a STAR tie in both rounds, settled without the lot (BV2180, `fp62p2`)

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/fp62p2) · **[results ↗](https://bettervoting.com/fp62p2/results)** (election `fp62p2`).

> 🪜 **The happy-path tiebreak.** This is the worked example from **[the STAR tie-breaking ladder](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md)**, now a live election. It ties in **both** rounds — a three-way tie for the second finalist, then a two-way tie in the runoff — and settles **both with deterministic rungs** (five-star, then score). The pre-published **lot order is never consulted**, so LH and BetterVoting agree and the result is fully reproducible. It's the deliberate contrast to **[BV555/`xmyf7k`](../Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md)**, where every rung ties down to the random floor.

**Level 201/301.** Two voters, six ice-cream flavors. Winner: **Strawberry**.

## The ballots (2 voters)

```
Chocolate, Chocolate Chip, Fudge Brownie, Vanilla, Strawberry, Mango
4,         5,              4,             1,       2,          -
1,         0,              0,             4,       5,          4
```

(`-` = left blank ≡ 0.) Source: [`bv2180_fp62p2_ice_cream_ladder.yaml`](cases/bv2180_fp62p2_ice_cream_ladder.yaml).

## How the winner is found — the ladder in action

| Step | What happens | Rung that decides |
|---|---|---|
| Scoring round | Strawberry **7** leads; Chocolate, Chocolate Chip, Vanilla tie at **5** for the 2nd slot | — (tie) |
| Scoring tiebreak 1 | pairwise among the three: all **2** → still tied | pairwise (no-op) |
| Scoring tiebreak 2 | five-star count: **Chocolate Chip 1**, Chocolate 0, Vanilla 0 → advances | **five-star** ✓ |
| Runoff | Strawberry **1** vs Chocolate Chip **1** head-to-head → tied | — (tie) |
| Runoff tiebreak 1 | total score: **Strawberry 7** > Chocolate Chip 5 → wins | **score** ✓ |

Both ties resolve *before* the lot. The elegant part (see the ladder doc): each round breaks its tie with the **other** round's yardstick — a scoring-round tie (equal totals) is broken by the runoff's *pairwise*, then *five-star*; a runoff tie (equal preference) is broken by the scoring round's *total score*.

## View 1 — BetterVoting (`fp62p2`)

BetterVoting runs the same protocol; because no random rung is reached, it elects **Strawberry** too.

> 📷 _Paste the BetterVoting `fp62p2` result screenshot here (filename suffix `_fp62p2`, under `img/`)._

## View 2 — the LH engine (reference)

```
--- STAR Voting Method (single winner) ---
[STAR Voting]
 Tabulating 2 ballots.

[Score Distribution] (how many ballots gave each star rating)
                     Score
Candidate       5  4  3  2  1  0  Abs  | Total   Avg
Chocolate       0  1  0  0  1  0    0  |     5   2.5
Chocolate Chip  1  0  0  0  0  1    0  |     5   2.5
Fudge Brownie   0  1  0  0  0  1    0  |     4   2.0
Vanilla         0  1  0  0  1  0    0  |     5   2.5
Strawberry      1  0  0  1  0  0    0  |     7   3.5
Mango           0  1  0  0  0  0    1  |     4   4.0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Strawberry     -- 7 -- First place
   Chocolate      -- 5 -- Tied for second place
   Chocolate Chip -- 5 -- Tied for second place
   Vanilla        -- 5 -- Tied for second place
   Fudge Brownie  -- 4
   Mango          -- 4
 Strawberry advances, but there's a three-way tie for second.

[STAR Voting: Scoring Round: First tiebreaker]
 The candidate preferred in the most head-to-head matchups advances.
   Chocolate      -- 2 -- Tied for second place
   Chocolate Chip -- 2 -- Tied for second place
   Vanilla        -- 2 -- Tied for second place
   Equal Support  -- 0
 There's still a three-way tie for second.

[STAR Voting: Scoring Round: Second tiebreaker]
 The candidate with the most votes of score 5 advances.
   Chocolate Chip -- 1 -- Second place
   Chocolate      -- 0
   Vanilla        -- 0
 Strawberry and Chocolate Chip advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Chocolate Chip -- 1 -- Tied for first place
   Strawberry     -- 1 -- Tied for first place
   Equal Support  -- 0
 There's a two-way tie for first.

[STAR Voting: Automatic Runoff Round: First tiebreaker]
 The highest-scoring candidate wins.
   Strawberry     -- 7 -- First place
   Chocolate Chip -- 5
 Strawberry wins.

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Strawberry
```

Full audit copy: [`_tabulated`](cases/cases_tabulated/bv2180_fp62p2_ice_cream_ladder_tabulated.txt).

## BV vs LH

Both engines elect **Strawberry** — confirmed against BetterVoting's frozen export ([`_bv_export.json`](cases/bv2180_fp62p2_ice_cream_ladder_bv_export.json)), whose Results record `tieBreakType: five_star` for the scoring round: BV broke the three-way tie by the five-star count, exactly as LH does. Unlike the 3-way dead heat, they *must* agree here: every tie is broken by a deterministic rung (five-star, then score), so no random shuffle is reached. That's what makes this case **freezable / BV-backable** where [BV555/`xmyf7k`](../Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) is LH-only.

## See also

- [The STAR tie-breaking ladder (full chain)](../../00_start_here/STAR_Voting/Tie_Breaking_STAR/tie_breaking.md) — this is its worked example
- [BV555 / `xmyf7k` — the 3-way tie that reaches the random floor](../Flat_scores_ties/Flat_scores_ties_05_scoring_tie_3way_xmyf7k.md) (the contrast case)
- [Dead-rung tie-breaks](../tie_break_dead_rung/) — when five-star has no 5s to weigh
