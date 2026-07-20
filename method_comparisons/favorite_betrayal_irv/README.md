# "Should I rank my favorite *second*?" — the plain RCV-IRV betrayal incentive, runnable

*The question RCV voters keep asking — and the honest answer is **sometimes, yes.** Under RCV-IRV, ranking your true favorite first can elect your **worst** candidate; ranking the compromise first can rescue them. This is **favorite betrayal**, and here it is in the simplest possible 3-bloc form you can run yourself. Then: **STAR and Ranked Robin elect the compromise from the honest ballots — no betrayal required.***

**▶ Live on BetterVoting:**
- **Honest ballots** (STAR + RCV-IRV + Ranked Robin, same voters): [vote](https://bettervoting.com/3xgkck) · **[results ↗](https://bettervoting.com/3xgkck/results)** (election `3xgkck`, BV2227)
- **The betrayal** (RCV-IRV, 2 voters rank the compromise first): [vote](https://bettervoting.com/bgcmxx) · **[results ↗](https://bettervoting.com/bgcmxx/results)** (election `bgcmxx`, BV2228)

→ The deep-dive concept page: [Favorite Betrayal — the full explainer](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md). Related: [center squeeze](../center_squeeze/) · [strategic voting](../../00_start_here/topics/strategic_voting.md) · [what makes a good winner?](../../00_start_here/topics/what_makes_a_good_winner.md).

---

## The setup

Three candidates on a spectrum — **Left**, **Center**, **Right** — and 34 voters. Center is everyone's second choice and the [Condorcet winner](../../00_start_here/topics/condorcet/) (beats Left 22–12, beats Right 21–13 head-to-head), but has the fewest first-choices.

| Voters | Ballot |
|---|---|
| 12 | Left > Center > Right |
| 4 | Center > Left > Right |
| 5 | Center > Right > Left |
| 13 | Right > Center > Left |

## 1. Honest ballots → RCV-IRV elects your *worst* ([`bv2227_3xgkck_honest_irv`](cases/cases_pages/bv2227_3xgkck_honest_irv.md))

The 12 Left voters vote sincerely, favorite first:

```
ROUND 1
Right   13   Hopeful
Left    12   Hopeful
Center   9   Rejected      ← fewest first-choices, squeezed out
Right   18   Elected
Left    16   Rejected
```

Center — the candidate a majority prefers to *either* wing — is eliminated first, and **Right wins**. The Left voters' honest ballots elected their **least-favorite** candidate. (Right was their bottom choice.)

## 2. Rank your favorite *second* → you win ([`bv2228_bgcmxx_betray_irv`](cases/cases_pages/bv2228_bgcmxx_betray_irv.md))

Change **just 2** of the 12 Left voters: they betray their favorite and rank **Center first**, Left second (`Center > Left > Right`). Nothing else moves.

```
ROUND 1
Right   13   Hopeful
Center  11   Hopeful
Left    10   Rejected      ← now Left is fewest, eliminated instead of Center
Center  21   Elected
Right   13   Rejected
```

Now **Left** is squeezed out, their ballots flow to Center, and **Center wins 21–13**. Two voters, by *hiding* who they actually liked best, flipped the result from their worst choice to their compromise. That is favorite betrayal — and it's exactly why the advice under IRV is *"putting your favorite first is only safe when they're either very strong or have no chance at all."*

## 3. The fix: STAR & Ranked Robin elect Center from the *honest* ballots ([`bv2227_3xgkck_honest_star`](cases/cases_pages/bv2227_3xgkck_honest_star.md))

Score the **same honest preferences** 0–5 (favorite 5, compromise 3, worst 0) — no strategy:

```
Scoring Round
   Center  -- 120 -- First place
   Right   --  80
   Left    --  72
Automatic Runoff Round
   Center  -- 21 -- First place
   Right   -- 13
 Center wins.

[Divergence from STAR]
  STAR          = Center
  RCV-IRV       = Right   (differs from STAR)
  Ranked Robin (RCV-RR) agrees with STAR — RCV-IRV is the lone outlier.
```

**STAR → Center. Ranked Robin → Center. RCV-IRV → Right.** On the *identical honest preferences*, the two methods that read the whole ballot elect the compromise the electorate actually prefers; only instant-runoff needed the betrayal. Under STAR you score your honest favorite a 5 and your compromise a 3, and the compromise still wins — no games, no regret.

## The takeaway

- **The incentive is real**, not a debating trick: under RCV-IRV, sincerely ranking a viable favorite first can elect your worst outcome, and betraying them can prevent it.
- **A common wrong rebuttal:** *"if your favorite gets eliminated round 1, ranking them second changes nothing."* True but beside the point — the betrayal bites precisely when your favorite is **strong enough to squeeze the center**, not when they're hopeless.
- **STAR and Ranked Robin don't have this hole.** They elect the Condorcet-winning compromise from honest ballots, so honesty is safe. That's the pitch — and the reason [Later-No-Harm ≠ Favorite Betrayal](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) is worth keeping straight.
- **Fair note:** STAR has its *own* rare strategic seams (min/maxing), conceded in [strategic voting](../../00_start_here/topics/strategic_voting.md) and [STAR's honest limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md). The claim isn't "STAR is strategy-proof" — it's "STAR doesn't punish plain honesty the way IRV can here."

## Reproduce it

```
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2227_3xgkck_honest_irv.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2228_bgcmxx_betray_irv.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2227_3xgkck_honest_star.yaml
```
