# Vote-Splitting / Spoiler Examples

Dramatic single-winner elections where **Choose-One Plurality elects the wrong winner** because a majority bloc splits its vote across similar candidates — and **STAR elects the candidate the majority actually preferred.**

→ **How often does this happen in real elections?** There's a published count — 11.9% of 2022 US primaries — and a careful reading of what it does and doesn't prove: **[How often does vote splitting actually happen?](how_often_does_vote_splitting_happen.md)**

Each file declares a `blocs:` group, so the engine's `[Vote-splitting check]` confirms the spoiler automatically. Run any of them through the STAR engine:

> **Why these are LH-only (house principle).** The teaching contrast here is **Plurality vs STAR**, not **BV vs LH** — BetterVoting and the LH engine *agree* on these results, so a BV screenshot would just duplicate the LH numbers. Two-view (BV beside LH) is reserved for cases where the two **diverge** (the bug *is* the lesson — see [Flat scores, ties & tie-breaking — and the BetterVoting bugs](../../01_STAR/03_Criteria/Flat_scores_ties/), [`Runoff_07`](../../01_STAR/04_Real_Elections/runoff_reversal_bv_cases/Runoff_07_flat_ballot_bv_bug_tf73v9.md)) or where reading BV's own UI is the point.

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py \
       split_voting/01_political_left_split.yaml
```

| File | Story | Choose-One winner | STAR winner |
|------|-------|-------------------|-------------|
| `01_political_left_split.yaml` | A 66% progressive coalition splits 3 ways | **Conservative (34%)** — the spoiler | **Labour** — the coalition's consensus |
| `02_icecream_chocolate_split.yaml` | Chocolate lovers (66%) split across 3 chocolates | **Vanilla (34%)** | **MilkChoco** |
| `03_lunch_veggie_vs_meat.yaml` | A 70% veggie majority splits across 3 dishes | **BeefBurger (30%)** | **VeggieCurry** |
| [`06_sub_majority_not_spoiled.yaml`](_main/_main_pages/06_sub_majority_not_spoiled.md) | **The control case** — a 41% winner that nothing spoiled | Aspen (41%) | **Aspen** — *same winner* |

In the first three the bloc is an outright majority, yet Choose-One hands the win to the lone outsider. STAR lets each voter score every candidate, so the bloc isn't split — and the automatic runoff elects the majority's compromise pick.

`06` is the deliberate **control**: the same sub-majority arithmetic (a 41% winner, losers combining to a majority) with **no spoiler underneath it** — STAR, Ranked Robin and RCV-IRV all confirm the plurality winner. Keep it next to `01`: identical warning signs, opposite verdicts, which is exactly why "the winner got under 50%" is a screening flag and not a finding.

> Teaching tip: show the **Choose-One first choices** line first (the wrong winner) and let it sting, then reveal the STAR result. The `[Vote-splitting check]` block states the verdict in numbers.
