# "Should I rank my favorite *second*?" — the plain RCV-IRV betrayal incentive, runnable

*The question RCV voters keep asking — and the honest answer is **sometimes, yes.** Under RCV-IRV, ranking your true favorite first can elect your **worst** candidate; ranking the compromise first can rescue them. This is **favorite betrayal**, and here it is in the simplest possible 3-bloc form you can run yourself. Then: **STAR and Ranked Robin elect the compromise from the honest ballots — no betrayal required.***

**▶ Live on BetterVoting:**
- **Honest ballots** (STAR + RCV-IRV + Ranked Robin, same voters): [vote](https://bettervoting.com/3xgkck) · **[results ↗](https://bettervoting.com/3xgkck/results)** (election `3xgkck`, BV2227)
- **The betrayal** (RCV-IRV, 2 voters rank the compromise first): [vote](https://bettervoting.com/bgcmxx) · **[results ↗](https://bettervoting.com/bgcmxx/results)** (election `bgcmxx`, BV2228)

→ The deep-dive concept page: [Favorite Betrayal — the full explainer](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md). Related: [center squeeze](../center_squeeze/README.md) · [strategic voting](../../07_Concepts/topics/strategic_voting.md) · [what makes a good winner?](../../07_Concepts/topics/what_makes_a_good_winner.md).

---

## The setup

Three candidates on a spectrum — **Left**, **Center**, **Right** — and 34 voters. Center is everyone's second choice and the [Condorcet winner](../../07_Concepts/topics/condorcet/README.md) (beats Left 22–12, beats Right 21–13 head-to-head), but has the fewest first-choices.

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

<!-- report:bv2227_3xgkck_honest_star -->
```text
[Divergence from STAR]
  STAR                   = Center
  Choose-One (Plurality) = Right   (differs from STAR)
  RCV-IRV                = Right   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/bv2227_3xgkck_honest_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 34 ballots.
Count × Left,Center,Right
   13 ×    0,     3,    5
   12 ×    5,     3,    0
    5 ×    0,     5,    3
    4 ×    3,     5,    0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Center        -- 120 -- First place
   Right         --  80 -- Second place
   Left          --  72
 Center and Right advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Center        -- 21 -- First place
   Right         -- 13
   Equal Support --  0
 Center wins.
   Runoff math:
     34  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     34  voters with a preference  (majority = 18)
           Center 21 (62%)  ·  Right 13 (38%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Center
```
<!-- /report -->
**STAR → Center. Ranked Robin → Center. RCV-IRV → Right.** On the *identical honest preferences*, the two methods that read the whole ballot elect the compromise the electorate actually prefers; only instant-runoff needed the betrayal. Under STAR you score your honest favorite a 5 and your compromise a 3, and the compromise still wins — no games, no regret.

## The takeaway

- **The incentive is real**, not a debating trick: under RCV-IRV, sincerely ranking a viable favorite first can elect your worst outcome, and betraying them can prevent it.
- **A common wrong rebuttal:** *"if your favorite gets eliminated round 1, ranking them second changes nothing."* True but beside the point — the betrayal bites precisely when your favorite is **strong enough to squeeze the center**, not when they're hopeless.
- **STAR and Ranked Robin don't have this hole.** They elect the Condorcet-winning compromise from honest ballots, so honesty is safe. That's the pitch — and the reason [Later-No-Harm ≠ Favorite Betrayal](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) is worth keeping straight.
- **Fair note:** STAR has its *own* rare strategic seams (min/maxing), conceded in [strategic voting](../../07_Concepts/topics/strategic_voting.md) and [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md). The claim isn't "STAR is strategy-proof" — it's "STAR doesn't punish plain honesty the way IRV can here."

## Reproduce it

```
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2227_3xgkck_honest_irv.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2228_bgcmxx_betray_irv.yaml
python3 STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/favorite_betrayal_irv/cases/bv2227_3xgkck_honest_star.yaml
```
