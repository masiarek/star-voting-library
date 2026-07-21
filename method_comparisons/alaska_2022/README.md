# Alaska 2022 — one real electorate, four counts, two winners

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/k3fmwv) · **[results ↗](https://bettervoting.com/k3fmwv/results)** (election `k3fmwv`, Test ID BV2213 — all four races).

**▶ Runnable companion to a published analysis.** This case makes **[Clelland (2023), *Ranked Choice Voting and Condorcet Failure in the Alaska 2022 Special Election*](https://arxiv.org/abs/2303.00108)** hands-on. She worked out — by hand, from the full Cast Vote Record — what STAR and Approval *would* have done in this election. Here you can **click the tabulated results and run the ballots yourself**, and check her conclusions against a live engine. (Her ballot profile, our reduced model, and [Graham-Squire & McCune](https://arxiv.org/abs/2301.12075) all agree.)

> **Which Alaska election is this?** The **August 2022 US House *special*** — the one where RCV-IRV misfired. It is *not* the November general (which worked fine — that's the [runnable counterpart](../alaska_2022_general/README.md)). Confused by all the Alaska elections? See the map: **[Alaska's RCV elections — the whole picture](../../00_start_here/RCV_IRV/case_studies/alaska_rcv_elections.md)**.

**One line:** in the August 2022 Alaska US House special election, **Begich beat both other candidates head-to-head** — a majority preferred him to Peltola *and* to Palin — yet **RCV-IRV eliminated him first** for having the fewest first choices, and Peltola won. Count the *same ballots* with a method that reads the whole ballot — **Ranked Robin** or **STAR** — and Begich, the Condorcet winner, wins. That is the [center squeeze](../../00_start_here/topics/center_squeeze/README.md), in a real federal race.

This folder reproduces it as a **runnable, reduced 200-voter model** so you can tabulate it yourself and see all four methods diverge.

## Learn it in three levels

New to this, or the "how did the guy who beat everyone lose?" part isn't clicking yet? Work up through these — each ends with **"challenge your understanding"** questions so you can check you actually get it:

1. **[101 — what happened, in plain language](alaska_101.md)** (zero jargon; the core intuition)
2. **[201 — the vote math, round by round](alaska_201.md)** (the exact IRV transfers, exhaustion, and head-to-head grid)
3. **[301 — every pathology, and is this fair?](alaska_301.md)** (spoiler / monotonicity / exhaustion — *and* the honest question of whether it's fair to STAR)

---

## Provenance — a faithful scaling of the real profile

This is **not** the raw Alaska ballots; it is a **~943:1 reduction** of the official preference profile (Table 1 of Graham-Squire & McCune, *An Examination of Ranked Choice Voting in the United States, 2004-2022*, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075)). Every one of the nine real ballot types is preserved:

| Real ballots (paper Table 1) | Reduced | Scores (Peltola, Begich, Palin) |
|---|---:|:---|
| 47,407 Peltola › Begich › Palin | 50 | `5,4,0` |
| 23,733 Peltola (bullet) | 25 | `5,0,0` |
| 4,647 Peltola › Palin › Begich | 5 | `5,0,4` |
| 34,078 Palin › Begich › Peltola | 36 | `0,4,5` |
| 21,237 Palin (bullet) | 23 | `0,0,5` |
| 3,659 Palin › Peltola › Begich | 4 | `4,3,5` |
| 27,070 Begich › Palin › Peltola | 29 | `0,5,4` |
| 15,478 Begich › Peltola › Palin | 16 | `4,5,0` |
| 11,262 Begich (bullet) | 12 | `0,5,0` |

Scores are a rank→score modeling overlay (favorite 5, then 4/3, unranked 0). The reduced model reproduces every headline figure within rounding. Companion visualizer: Equal Vote's [Real RCV](https://realrcv.equal.vote/alaska22).

---

## The four counts

| Method | Winner | Why |
|---|:---:|---|
| **Choose-One (Plurality)** | **Peltola** | Most first choices: Peltola 80, Palin 63, Begich 57 |
| **RCV-IRV (Hare)** | **Peltola** | Begich (fewest firsts) eliminated; 12 ballots exhaust; Peltola beats Palin **96–92** |
| **Ranked Robin (Condorcet)** | **Begich** | Beats Peltola 93–84 **and** Palin 107–68 — wins every matchup |
| **STAR** | **Begich** | Score finalists Begich (641) & Peltola (480); Begich wins the runoff **93–84** |

Two of the four elect **Peltola**; the two that read the whole ballot elect **Begich**, the candidate a majority actually preferred. IRV is the lone method that fails the Condorcet winner — the center-squeeze signature. **BetterVoting and an independent open-source count agree on all four winners**, every race deterministic (`tieBreakType: none`).

---

## View 1 — on BetterVoting (the live election)

Four races on the one electorate, live: **[bettervoting.com/k3fmwv/results](https://bettervoting.com/k3fmwv/results)**. BetterVoting's own counts return **Plurality Peltola · IRV Peltola · Ranked Robin Begich · STAR Begich**, matching the independent count below exactly. Frozen export: [`bv2213_k3fmwv_alaska_2022_bv_export.json`](cases/bv2213_k3fmwv_alaska_2022_bv_export.json).

## View 2 — an independent count (the full tabulation)

*The same ballots, re-counted by the open-source engine this repo runs — **Larry Hastings' `starvote`, extended here** (added reporting and the RCV-IRV / Ranked Robin comparisons) — so you can verify the result yourself instead of taking the platform's word for it. It's tagged "LH" (Larry Hastings) elsewhere in this repo.*

The score model tabulates STAR and auto-derives the other three counts (the `[Divergence from STAR]` block):

```
--- Runoff (Preference) Matrix ---
                    |    * Peltola    |   * Begich     |      Palin     |
        * Peltola > |       ---       | 84 -  23 -  93 | 96 -  12 -  92 |
         * Begich > |  93 -  23 -  84 |      ---       |107 -  25 -  68 |
            Palin > |  92 -  12 -  96 | 68 -  25 - 107 |      ---       |

[Condorcet Winner]
  Condorcet Winner: Begich — matches the STAR winner

[Divergence from STAR]
  STAR                   = Begich
  Choose-One (Plurality) = Peltola   (differs from STAR)
  RCV-IRV                = Peltola   (differs from STAR)
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.

Scoring Round
   Begich        -- 641 -- First place
   Peltola       -- 480 -- Second place
   Palin         -- 451
 Begich and Peltola advance.

Automatic Runoff Round
   Begich        -- 93 -- First place
   Peltola       -- 84
   Equal Support -- 23
 Begich wins.
   Voters with a preference: 177 of 200 (23 Equal Support).
   Begich 93 (53%) vs Peltola 84 (47%); majority = 89.
```

And the RCV-IRV rounds show the squeeze and the exhaustion directly:

```
ROUND 1
Peltola  80  Hopeful
Palin    63  Hopeful
Begich   57  Rejected      # the Condorcet winner, cut for fewest FIRST choices

FINAL RESULT
Peltola      96  Elected
Palin        92  Rejected
Blank Votes  12  Rejected  # ballots that exhausted when Begich was eliminated
```

Peltola's 96 is only **48% of the 200 ballots cast** — a "majority" of the *surviving* ballots, on a denominator shrunk by exhaustion (the paper's *majoritarian failure*).

Full engine detail: [`alaska_2022_tabulated/`](cases/cases_tabulated/) · run it: [`bv2213_k3fmwv_alaska_2022.yaml`](cases/bv2213_k3fmwv_alaska_2022.yaml).

---

## The same profile also carries the other IRV pathologies

The paper documents several failures in this one election; the reduced model reproduces each:

- **Spoiler.** Remove the losing candidate Palin and **Begich wins** — a candidate who couldn't win changed who did.
- **Upward monotonicity.** Had ~6,000 Palin-bullet voters (≈6 in the model) instead ranked the *winner* Peltola first, Peltola would have **lost**: those votes eliminate Palin first, and Begich then beats Peltola. Ranking the winner higher defeats the winner.
- **No-show / truncation.** Had ~5,400 `Palin › Begich` voters stayed home, Palin is eliminated first, Begich beats Peltola, and those voters get a *better* result by *not voting*.
- **Majoritarian failure.** The winner holds only 48.4% of all ballots (48% here) once exhausted ballots are set aside.

Methods that read the whole ballot — Ranked Robin, any Condorcet method, and STAR via its runoff — sidestep all of these, because none of them gate survival on first-choice counts. The lesson isn't "ranked ballots are bad"; it's that **the tabulation matters, and Hare elimination is the part that failed here.**

---

## Related

- **Three-level explainer:** [101](alaska_101.md) · [201](alaska_201.md) · [301](alaska_301.md)
- **Equal Vote's Real RCV tool:** [this election](https://realrcv.equal.vote/alaska22) · [browse every real US RCV election](https://realrcv.equal.vote) — worth doing: most of them worked fine, which is the honest backdrop for why Alaska stands out (see [301](alaska_301.md) on rarity)
- **Founder's narrative writeup:** Mark Frohnmayer, ["What the heck happened in Alaska?"](https://nardopolo.medium.com/what-the-heck-happened-in-alaska-3c2d7318decc) — the accessible, story-first version (STAR-founder source, so **advocacy-leaning**; its facts match the academic analyses above, and it adds the "breadth of support" lens now in [301](alaska_301.md))
- **Reproduce from the raw ballots:** the public [Cast Vote Record + tabulation code](https://github.com/nardo/Equal.Vote/tree/master/alaska) and Alaska's [official RCV detailed report](https://www.elections.alaska.gov/results/22SSPG/RcvDetailedReport.pdf) — the actual data behind this case's reduced model
- [Alaska 2022 — RCV-IRV case study](../../00_start_here/RCV_IRV/case_studies/RCV_IRV_alaska_2022.md) (the prose write-up with the real vote totals)
- [Burlington 2009](../burlington_2009/README.md) — the other canonical real IRV center squeeze, also runnable
- [Center squeeze](../../00_start_here/topics/center_squeeze/README.md) · [Favorite betrayal (301)](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) · [Non-monotonicity](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md)
