# The Downward Monotonicity Paradox — when ranking a *loser* lower makes him win (San Francisco 2020)

*The mirror of the [upward paradox](upward_monotonicity_alaska.md). A voting method should never **reward** a candidate for losing support. RCV-IRV can. In the real **2020 San Francisco Board of Supervisors, District 7** race, shifting the losing candidate **Engardio** *down* one rank on about **800** ballots — giving him **less** first-place support and changing nothing else — would have made **Engardio the winner**. This page reproduces it on the real full-scale counts, then shows that **STAR and Ranked Robin cannot do it.***

→ Part of the [monotonicity worked set](README.md). Companions: [**Upward** paradox — Alaska 2022](upward_monotonicity_alaska.md) (its mirror) · [non-monotonicity (concept)](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md) · [monotonicity topic hub](../../00_start_here/topics/monotonicity/README.md).

---

## Two flavours of the paradox — this is the second

Non-monotonicity comes in a matched pair (Graham-Squire & McCune, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075)):

- **Upward monotonicity paradox** ("more is less"): raise the **winner** and the winner *loses*. → [Alaska 2022](upward_monotonicity_alaska.md).
- **Downward monotonicity paradox** ("less is more"): shift a **losing** candidate L *down* the rankings on some ballots — keeping every other candidate's relative order the same — and L *wins*. Giving a candidate **less** support elects them. **← this page.**

The Alaska example is *only* an upward paradox — there, shifting Begich or Palin down leaves them losers. To see a real downward paradox, the paper turns to San Francisco.

## The real example: San Francisco D7, 2020

The 2020 SF Board of Supervisors race in District 7 had seven candidates. Following the RCV-IRV eliminations down to the final three (the paper's Table 2), the profile is **Engardio**, **Melgar**, **Nguyen**. Counted by RCV-IRV:

**BEFORE — Engardio loses; Melgar wins.** ([`sf_d7_downward_before`](cases/cases_pages/sf_d7_downward_before.md))

```
ROUND 1
Engardio  14119   Hopeful       ← leads on first-choices
Melgar    11652   Hopeful
Nguyen    10855   Rejected       ← fewest, eliminated
Melgar    18561   Elected        ← Nguyen's transfers carry Melgar past Engardio
Engardio  16370   Rejected       ← Engardio LOSES
```

**AFTER — rank the loser lower, and he wins.** Shift **800** `Engardio > Nguyen > Melgar` ballots down to `Nguyen > Engardio > Melgar`. Engardio simply *loses* 800 first-place votes; nothing else changes. ([`sf_d7_downward_after`](cases/cases_pages/sf_d7_downward_after.md))

```
ROUND 1
Engardio  13319   Hopeful       ← Engardio LOST support (14119 → 13319)
Nguyen    11655   Hopeful       ← +800, now just 3 votes ahead of Melgar
Melgar    11652   Rejected       ← Melgar now has the fewest, eliminated instead of Nguyen
Engardio  15819   Elected        ← Melgar's transfers, and Engardio beats Nguyen
Nguyen    15155   Rejected
```

**Engardio lost first-place support and turned from loser into winner.**

### Why less support wins

Exactly as in [Alaska](upward_monotonicity_alaska.md), the trick is the **order of elimination**. Those 800 ballots, moved off Engardio and onto Nguyen, lift Nguyen's first-round count *just past* Melgar's — by **3 votes** — so **Melgar** is eliminated first instead of Nguyen. Melgar's ballots transfer, and in the resulting final Engardio defeats Nguyen. The candidate Engardio needed gone was **Melgar**, and the way to eliminate Melgar was to make Engardio *look weaker*. Sequential elimination made a candidate stronger by taking his votes away.

> **Knife-edge — why full scale.** The flip hinges on a **3-vote** Round-1 gap (Melgar 11652 vs Nguyen 11655). A reduced toy model can't hold a 3-in-36,000 margin, so this case uses the **real full-scale counts**. The Round-1 three-way (14119 / 11652 / 10855) and the BEFORE final (Melgar 18561, Engardio 16370) reproduce the paper's published figures exactly; Melgar's own second-preference split — not printed in the quoted table — is reconstructed to complete the three-way, consistent with the paper's stated result (Engardio wins the AFTER final). Reproduce: `uv run python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/sf_d7_downward_after.yaml`.

## STAR and Ranked Robin can't do this

Both methods are **monotonic** — lowering a candidate can never *help* them, and raising one can never *hurt* — so **neither has a downward (or upward) monotonicity paradox.**

- **Ranked Robin** (Condorcet / Copeland) reads every head-to-head, so the elimination-order trick has no purchase. On the **same** ballots it elects **Melgar both times** — before *and* after — because Melgar is the [Condorcet winner](../../00_start_here/topics/condorcet/) (he beats Engardio 18561–16370 and Nguyen 24971–11655). Note the sharp contrast: RCV-IRV's result *moves off* the Condorcet winner under the paradox; Ranked Robin stays on him. (Same ranked ballot, a monotonic count.)
- **STAR** passes **mono-raise** and its downward form: a candidate losing points can only ever *hurt* their own total, never help. (See [STAR & monotonicity](../../00_start_here/STAR_Voting/properties_and_limits/STAR_monotonicity.md) and the runnable [STAR before/after pair](cases/cases_pages/monotonicity_star_before.md).)

## Keep it in proportion — the fair reading

- **Real and documented** — SF D7 2020 is a genuine recorded election, one of the cleanest downward-paradox cases in the literature. That's why it teaches well.
- **But rare.** Like its mirror, the downward paradox needs a near-three-way race with a specific transfer structure; most IRV elections never trigger one. The durable point is *structural*: IRV's winner depends on elimination order, which can move the wrong way in **both** directions.
- **IRV-specific, not "ranked voting."** The same ballots under [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/README.md) are monotonic. It's *instant-runoff* that fails here, not ranked ballots as such.
- **STAR's own limit stays on the table.** STAR passes mono-raise but fails the stronger **mono-raise-delete** in lab constructions — [conceded in the worked set](README.md#the-301-nuance-star-fails-a-stronger-variant). Naming both sides is the point.

The takeaway matches the upward page: **a voter's honest ranking shouldn't be able to backfire** — up *or* down — and STAR and Ranked Robin give that guarantee where instant-runoff can't.

## Sources

- Graham-Squire & McCune, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075) — defines the upward/downward paradoxes and gives both the Alaska (upward) and San Francisco D7 (downward) real-world examples; Table 2 is the SF profile modelled here.
- This library's [upward companion (Alaska 2022)](upward_monotonicity_alaska.md) and the [monotonicity worked set](README.md).
