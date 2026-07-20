# BV2105 — Favorite ice cream (Bloc STAR): a partial ballot mis-filed as an abstention

*BetterVoting test **BV2105** (`r4dqvd`, "Favorite ice cream (Bloc STAR) - without end date"). Bloc STAR, 3 flavors, 2 seats, 4 ballots. The winners are right (**Chocolate, Strawberry**) and the seat-2 score tiebreak matches LH exactly — but BetterVoting's count is wrong: it files a **real partial ballot as an abstention**, reporting `nTallyVotes 2 / nAbstentions 2` where the truth is 3 tallied + 1 abstention. Guards the (closed) bug [bettervoting#1056](https://github.com/Equal-Vote/bettervoting/issues/1056).*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/r4dqvd) · **[results ↗](https://bettervoting.com/r4dqvd/results)** (election `r4dqvd`).

Reference file: [`bv2105_r4dqvd_ice_cream_bloc.yaml`](cases/bv2105_r4dqvd_ice_cream_bloc.yaml) (`expected_winners: [Chocolate, Strawberry]`). Frozen export: [`bv2105_r4dqvd_ice_cream_bloc_bv_export.json`](cases/bv2105_r4dqvd_ice_cream_bloc_bv_export.json). Backs sheet row **BV2105**.

## The election

Bloc STAR, 3 flavors, **2 seats**, 4 ballots:

```
Vanilla,Chocolate,Strawberry
5,5,5     an all-5s ballot (loves everything)
-,-,-     fully blank — a TRUE abstention
1,-,-     Vanilla=1, the rest blank — a REAL (partial) vote
2,5,4     a full ballot
```

Chocolate takes seat 1. Seat 2 is a **Vanilla/Strawberry runoff tie (1–1)**, broken by score — Strawberry 9 > Vanilla 8 — so BetterVoting's `tieBreakType: score` and LH agree. Winners: **Chocolate, Strawberry**.

## The regression (counting, not tabulation)

BetterVoting's `summaryData` reports **`nTallyVotes: 2`, `nAbstentions: 2`** — it counts only the two *full* ballots and files **both** the blank ballot **and** the partial `1,-,-` ballot as abstentions. You can see the partial ballot was dropped from the tally, not just mislabelled: BV's per-candidate score is an average over **2** ballots, so Vanilla reads `(5+2)/2 = 3` — the `1` from ballot 3 never entered the sum.

The LH engine counts it correctly: **4 ballots, 1 abstention** (only the fully-blank row), Vanilla total **8** (5 + 1 + 2). Same winners here — the discarded ballot only helped Vanilla, the seat-2 loser — so this is a **reporting/counting** regression rather than a wrong result. But a dropped cast ballot can flip a closer election, which is why it earns a guard.

This is the **opposite-direction sibling of [BV15](../../01_STAR/pet_real_bv_election/bv15_4h89vj_plurality_abstain.md) / bettervoting#740**: #740 *drops* abstentions from the displayed turnout; BV2105 mis-classifies a *real* partial ballot **as** an abstention. Both are abstention-accounting defects. Since **#1056 is closed/fixed**, this case is a **regression guard** — the frozen export preserves the buggy counts, and this LH reference pins the correct ones for a future re-check.

## The LH report (the correct count)

```text
--- Bloc STAR Voting Method (2 winners) ---
 Tabulating 4 ballots to fill 2 seats. Note: 1 of 4 ballots is marked as an abstention.
Vanilla,Chocolate,Strawberry
      5,        5,         5
      -,        -,         -
      1,        -,         -
      2,        5,         4

[Score Distribution] (how many ballots gave each star rating)
                 Score
Candidate   5  4  3  2  1  0  Abs  | Total   Avg
Vanilla     1  0  0  1  1  0    1  |     8   2.7
Chocolate   2  0  0  0  0  0    2  |    10   5.0
Strawberry  1  1  0  0  0  0    2  |     9   4.5

Round 1: Chocolate (10) & Strawberry (9) advance → Chocolate wins the runoff (1 vs 0, 3 Equal Support).
Round 2: Strawberry (9) & Vanilla (8) advance → runoff ties 1–1 → score tiebreak → Strawberry (9 > 8).

Winners — Bloc STAR Voting Method (2 winners)
 Chocolate
 Strawberry
```

Full audit copy: [`_main_tabulated/bv2105_r4dqvd_ice_cream_bloc_tabulated.txt`](cases/cases_tabulated/bv2105_r4dqvd_ice_cream_bloc_tabulated.txt).

## LH ↔ BetterVoting

| Quantity | BetterVoting `summaryData` | LH engine | Agree? |
|---|:--:|:--:|:--:|
| Winners | Chocolate, Strawberry | Chocolate, Strawberry | ✓ |
| Seat-2 tiebreak | `score` (Strawberry) | score (Strawberry 9 > Vanilla 8) | ✓ |
| Ballots tallied | `nTallyVotes` 2 | **3** | ✗ |
| Abstentions | `nAbstentions` 2 | **1** (blank only) | ✗ |
| Vanilla total | 3 (avg over 2 ballots) | **8** (5 + 1 + 2) | ✗ |

The winner path matches; the **count** is where BV's (now-fixed) bug shows — it drops the `1,-,-` ballot as an abstention.

## Related

- [BV15 — Plurality abstain (bettervoting#740)](../../01_STAR/pet_real_bv_election/bv15_4h89vj_plurality_abstain.md) — the mirror-image abstention bug (turnout undercount).
- [BV132 — verify number of votes cast (#1073)](bv132_verify_votes_bloc.md) — another Bloc count-verification case.
- [02_STAR_Bloc README](README.md) · [BV registry](../../00_start_here/YAML_test_case_index/BV_registry.md).
