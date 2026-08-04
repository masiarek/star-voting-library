# BV95a — Majority Criterion: the favorite survives (majority backs ONE rival)

<!-- case-meta:start — managed by build_yaml_pages.py; edit the YAML, not these lines -->
**Method:** [STAR (single winner)](../../01_Learn) · **1 seat** · **Expected winner:** Ada · [full count →](cases/cases_pages/bv95a_9m6rxr_favorite_survives_one_rival.md)
<!-- case-meta:end -->

*A 5-voter STAR election. A 3-voter majority scores **Ada** highest (5). They also honestly support **one** other candidate — Bruno gets a 4 — and leave Cleo at 0. Question: does supporting a compromise candidate cost the majority their favorite? **No — Ada wins.** This is the "safe" half of the [Majority Criterion](../../../07_Concepts/topics/majority_criterion/README.md) pair; its twin [BV95b](bv95b_7pdq3r_favorite_loses_two_rivals.md) shows what tips it over.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/9m6rxr) · **[results ↗](https://bettervoting.com/9m6rxr/results)** (election `9m6rxr`).

Reference files: [`bv95a_9m6rxr_favorite_survives_one_rival.yaml`](cases/bv95a_9m6rxr_favorite_survives_one_rival.yaml) (`expected_winners: [Ada]`) · frozen export [`bv95a_9m6rxr_favorite_survives_one_rival_bv_export.json`](cases/bv95a_9m6rxr_favorite_survives_one_rival_bv_export.json). Backs sheet row **BV95a**.

## The ballots

```
Ada,Bruno,Cleo
5,4,0     ← the 3-voter majority (×3): love Ada, like Bruno, ignore Cleo
0,5,5     ← the 2-voter minority (×2): reject Ada, love Bruno & Cleo
```

## The STAR tabulation (LH)

--8<-- "01_STAR/03_Criteria/majority_criterion/cases/cases_pages/bv95a_9m6rxr_favorite_survives_one_rival.md:report"
Full audit copy: [`majority_criterion_tabulated/bv95a_9m6rxr_favorite_survives_one_rival_tabulated.txt`](cases/cases_tabulated/bv95a_9m6rxr_favorite_survives_one_rival_tabulated.txt).

## Why Ada wins

Bruno leads the *scoring* round (22 — nearly everyone rates him highly), and Ada is second on score (15). But STAR's second step is the **automatic runoff**: of the two finalists, which does a majority actually prefer? Here the 3-voter majority put Ada (5) above Bruno (4), so **Ada takes the runoff 3–2** and wins. The majority's honest support for *one* compromise candidate (Bruno = 4) got Bruno into the finals but did **not** cost them their favorite. That's the Majority Criterion holding — and, in Equal Vote's terms, the Relaxed-Majority-Criterion "safe" behavior: a majority can give a second choice `max − 1` without sinking their first.

## Confirmed on BetterVoting

Reproduced live at [**bettervoting.com/9m6rxr/results**](https://bettervoting.com/9m6rxr/results): BV also elects **Ada** (`nTallyVotes 5`), matching LH. Election created via [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py).

## See also

- The concept, the Relaxed Majority Criterion, and the Later-No-Harm link: **[Majority Criterion topic hub](../../../07_Concepts/topics/majority_criterion/README.md)**.
- The twin that flips: [BV95b — the favorite loses when the majority backs *two* rivals](bv95b_7pdq3r_favorite_loses_two_rivals.md).
- [STAR's honest limits #8](../../01_Learn/properties_and_limits/STAR_honest_limits.md).
