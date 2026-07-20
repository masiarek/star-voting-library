# 01_STAR/favorite_betrayal — the worked STAR favorite-betrayal pair

The rare construction [favorite_betrayal_voting_301.md](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) describes but — until now — never showed with numbers: **STAR is not formally FBC-compliant, and its leak lives in the runoff.** Your scores don't just support candidates; they pick the two *finalists*. In a delicately balanced electorate, the score you give your favorite can be exactly what keeps your compromise **out** of the runoff — and then the only repair is scoring your favorite lower. That's a favorite betrayal, it happens here, and it pays.

This is the repo's concession case. We show STAR's own criterion failure at full volume, with the live elections to click — because the credibility of every center-squeeze page in this repo is bought by pages like this one.

**▶ Live on BetterVoting:**
- Half 1, honest: [vote](https://bettervoting.com/7mckyg) · **[results ↗](https://bettervoting.com/7mckyg/results)** (election `7mckyg`, Test ID BV2206)
- Half 2, betrayal: [vote](https://bettervoting.com/b6xrdr) · **[results ↗](https://bettervoting.com/b6xrdr/results)** (election `b6xrdr`, Test ID BV2207)

BetterVoting agrees with the LH engine on both halves (Clover; Bluebell) — no tiebreaks anywhere.

## The electorate

A garden club of 57 picks the town flower: **Aster**, **Bluebell**, **Clover**.

| Count | Aster | Bluebell | Clover | who they are |
|:---:|:---:|:---:|:---:|---|
| 9 | **5** | **5** | 0 | the double-fans: love Aster, love Bluebell — *the betrayers-to-be* |
| 6 | **5** | 0 | 0 | Aster-only fans |
| 24 | 0 | **1** | 0 | the tepid consensus: "Bluebell? …fine." |
| 18 | 0 | 0 | **4** | the Clover bloc |

**Bluebell is the Condorcet winner** — she beats Aster head-to-head 24–6 and Clover 33–18. But her support is broad and *feeble* (twenty-four 1s), and score totals are what pick STAR's finalists.

## Half 1 — honest ballots elect Clover

```text
Scoring Round
   Aster         -- 75 -- First place
   Clover        -- 72 -- Second place
   Bluebell      -- 69
 Aster and Clover advance.

Automatic Runoff Round
   Clover        -- 18 -- First place
   Aster         -- 15
   Equal Support -- 24
 Clover wins.
   Voters with a preference: 33 of 57 (24 Equal Support).
   Clover 18 (55%) vs Aster 15 (45%); majority = 17.
```

The pairwise matrix behind it (the engine's full view — note Bluebell's row):

```text
                 |   * Aster    |   Bluebell  |  * Clover   |
-------------------------------------------------------------
       * Aster > |     ---      | 6 - 27 - 24 |15 - 24 - 18 |
      Bluebell > | 24 - 27 -  6 |    ---      |33 -  6 - 18 |
      * Clover > | 18 - 24 - 15 |18 -  6 - 33 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Bluebell — STAR elected Clover instead (Bluebell was
  eliminated in the scoring round)
```

The compromise a majority prefers to *everyone* misses the runoff by three points. (This half is also a clean [Condorcet-winner paradox](../../00_start_here/voting_paradoxes/condorcet_winner_paradox.md) instance for STAR, alongside [BV2156](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md).)

## Half 2 — nine voters demote their favorite, and it pays

The nine double-fans see the standings. Notice what they **cannot** do: raise Bluebell. She's already at 5 on their ballots — STAR let them equal-top the compromise for free, and it wasn't enough, because the problem is *Aster's own total* keeping Bluebell out of the runoff. The only move left is scoring their true favorite **lower** — Aster 5 → 4, strictly below Bluebell. That is the definition of favorite betrayal.

```text
Scoring Round
   Clover        -- 72 -- First place
   Bluebell      -- 69 -- Second place
   Aster         -- 66
 Clover and Bluebell advance.

Automatic Runoff Round
   Bluebell      -- 33 -- First place
   Clover        -- 18
   Equal Support --  6
 Bluebell wins.
   Voters with a preference: 51 of 57 (6 Equal Support).
   Bluebell 33 (65%) vs Clover 18 (35%); majority = 26.
```

The runoff pairing flips from Aster-vs-Clover to Clover-vs-Bluebell, and the Condorcet winner wins it 33–18. The nine turned their outcome from **Clover (their 0)** into **Bluebell (their 5)** by lowering their favorite. STAR failed the Favorite Betrayal Criterion, exactly as its ❌ on the criteria chart says it can.

## Why this is a lab specimen, not a strategy

The [301 page](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) claims STAR's FBC failures are "fragile and unactionable." This case *demonstrates* the fragility rather than asserting it:

- **It takes 7 of the 9.** Each betrayer moves Aster down one point. Seven or more: the flip works. Exactly six: Aster and Bluebell **tie at 69** for the last runoff seat and the outcome falls to a tie-break. Five or fewer: nothing changes — Clover still wins, and the betrayers gave up score-support for their favorite for free.
- **It needs the standings to 3 points.** The whole construction balances on Aster 75 / Clover 72 / Bluebell 69. Real electorates don't publish their totals in advance; polling error alone swamps a 3-point gap in a 57-voter race.
- **It needs the compromise pre-maxed.** If the nine had any room to raise Bluebell instead, that honest, non-betrayal repair would come first — STAR's equal-top is free. The betrayal is only *forced* because the honest fix is already spent.

Measured across thousands of random elections, betrayals that actually pay are the ~2% tail in STAR — the other ~98% backfire ([fbc_simulation.py](../../06_Other/simulations/fbc_simulation.py)). This page is what one of the 2% looks like: engineered, coordinated, knife-edged. Compare the RCV-IRV failure mode — the [center squeeze](../../00_start_here/topics/center_squeeze/README.md) — which is *systematic*, arrives in ordinary competitive three-way races, and gives a whole political wing a standing reason to betray (Alaska 2022, worked on the 301 page).

## Reading this fairly

Both sides of the honesty ledger, in one breath: **STAR fails FBC** — this pair is the proof, concede it without a number attached. **And** the failure needed a 3-point knife edge, a pre-maxed compromise, and 7-of-9 coordination to appear, while the same electorate under RCV-IRV rules would have been an ordinary center-squeeze setup. Neither method is betrayal-proof; the theorem says something had to give (no method satisfies both Favorite Betrayal and Later-No-Harm). What differs is whether the failure is a lab specimen or a repeating pattern.

## Run it yourself

```
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/favorite_betrayal/cases/bv2206_7mckyg_fbc_honest_tepid_consensus.yaml
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/favorite_betrayal/cases/bv2207_b6xrdr_fbc_betrayal_pays.yaml
```

Sources: [bv2206_7mckyg_fbc_honest_tepid_consensus.yaml](cases/bv2206_7mckyg_fbc_honest_tepid_consensus.yaml) · [bv2207_b6xrdr_fbc_betrayal_pays.yaml](cases/bv2207_b6xrdr_fbc_betrayal_pays.yaml). Full mirrors: [`favorite_betrayal_tabulated/`](cases/cases_tabulated/).

---

**Where this comes from.** Ballots and cast are this repo's own, built to instantiate the finalist-pairing mechanism described in [favorite_betrayal_voting_301.md §5](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) ("your scores can change *which two candidates are finalists*"). Related: [runoff reversal](../runoff_overturns_leader/README.md) (the benign face of the same score-vs-runoff two-step) · [residual vote splitting](../../00_start_here/STAR_Voting/properties_and_limits/residual_vote_splitting.md) (the other runoff-born edge case) · [monotonicity](../../method_comparisons/monotonicity/README.md) (STAR's clean bill on the *raise* direction).

# file: README.md
