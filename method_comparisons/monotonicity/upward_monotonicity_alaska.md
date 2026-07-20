# The Upward Monotonicity Paradox — when ranking the winner *higher* makes her lose (Alaska 2022)

*A voting method should never punish a candidate for gaining support. RCV-IRV can. In the real **Alaska 2022** US House special, had about **6,000** Palin-only voters instead ranked the eventual winner **Peltola** first — giving her *more* first-place support and changing nothing else — **Peltola would have lost**. This is the **upward monotonicity paradox**, and this page reproduces it on a faithful model of the real ballots, then shows that **STAR and Ranked Robin cannot do it.***

→ Part of the [monotonicity worked set](README.md). Companions: [**Downward** paradox — San Francisco 2020](downward_monotonicity_sf.md) (its mirror) · [Alaska 2022 (the full case)](../alaska_2022/) · [the burial attack on the same numbers](../condorcet_burial_alaska/) · [non-monotonicity (concept)](../../00_start_here/RCV_IRV/RCV_IRV_non_monotonicity.md) · [monotonicity topic hub](../../00_start_here/topics/monotonicity/README.md).

---

## Two flavours of the paradox

Non-monotonicity comes in a matched pair (Graham-Squire & McCune, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075)):

- **Upward monotonicity paradox** ("more is less"): shift the **winner up** the rankings on some ballots — keeping every other candidate's relative order the same — and the winner *loses*. Giving a candidate **more** support defeats them. **← this page.**
- **Downward monotonicity paradox** ("less is more"): shift a **loser down** on some ballots and that loser *wins*. Giving a candidate **less** support elects them. → [San Francisco D7 2020](downward_monotonicity_sf.md).

Both are failures of the **monotonicity criterion**: raising a candidate should never hurt them, and lowering one should never help them. (Note: monotonicity is **not** the same as [Later-No-Harm](../../00_start_here/STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md) — a common conflation.)

## The real example: Alaska 2022

The August 2022 Alaska US House special, reduced ~960:1 to a faithful **200-voter** model (the same profile as the [full Alaska case](../alaska_2022/)). Three candidates: **Peltola** (D), **Begich** (R, the moderate), **Palin** (R). Counted by RCV-IRV:

**BEFORE — Peltola wins.** ([`alaska_upward_before`](cases/cases_pages/alaska_upward_before.md))

```
ROUND 1
Peltola   80   Hopeful
Palin     63   Hopeful
Begich    57   Rejected      ← fewest first-choices, eliminated
Peltola   96   Elected       ← Begich's ballots split; Peltola wins the final
Palin     92   Rejected
```

**AFTER — raise the winner, and she loses.** Change **7** of the 23 Palin-only ballots to `Peltola > Palin`. Nothing else moves — Peltola simply *gains* 7 first-place votes. ([`alaska_upward_after`](cases/cases_pages/alaska_upward_after.md))

```
ROUND 1
Peltola   87   Hopeful       ← Peltola GAINED support (80 → 87)
Begich    57   Hopeful
Palin     56   Rejected      ← Palin now has the fewest, eliminated instead of Begich
Begich    93   Elected       ← Palin's ballots swing to Begich; Begich wins the final
Peltola   91   Rejected      ← the previous winner now LOSES
```

**Peltola gained first-place support and turned from winner into loser.**

### Why more support backfires

The winner's fate under IRV depends on *who gets eliminated first*, and that depends on **first-place counts** — the one thing the extra support changed. In the BEFORE election Begich has the fewest first-choices and is eliminated; his second-choices (which favour Peltola enough) carry her to the win. The 7 shifted ballots pull **Palin** below Begich, so now **Palin** is eliminated first instead — and Palin's ballots break heavily to **Begich** (they're Republican-aligned: `Palin > Begich`), who then beats Peltola head-to-head. Peltola's extra first-place votes rescued her *rival's* rival. That is the mechanism, and it is structural to sequential elimination.

> **Model note.** At this 200-voter reduction, moving **6** ballots makes an exact **57–57** Begich/Palin tie in Round 1 (a coarse-model artifact whose outcome hinges on a tie-break); moving **7** clears it cleanly, so we use 7 for a tie-free, engine-independent demonstration. The real election's figure is **~6,000** Palin-only ballots, which crosses the threshold comfortably. Reproduce: `uv run python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/monotonicity/cases/alaska_upward_after.yaml`.

## STAR and Ranked Robin can't do this

Both methods are **monotonic** in this sense — raising a candidate on some ballots can never cost them the election — so **neither has an upward monotonicity paradox.**

- **Ranked Robin** (Condorcet / Copeland) reads the *whole* pairwise picture, not just who's eliminated first, so the shift doesn't move it at all. On the **same** ballots it elects **Begich both times** — before *and* after — because Begich is the [Condorcet winner](../../00_start_here/topics/condorcet/) who beats each rival head-to-head (Begich > Peltola, Begich > Palin). It's completely unmoved by the raise. (Same ballot as RCV-IRV, a monotonic count — the olive branch to ranked-choice voters.)
- **STAR** passes **mono-raise**: raising your score for a candidate can only ever help them reach and win the runoff. (See the runnable [STAR before/after pair](cases/cases_pages/monotonicity_star_before.md) and [STAR & monotonicity](../../00_start_here/STAR_Voting/properties_and_limits/STAR_monotonicity.md).)

## Keep it in proportion — the fair reading

- **This is a real, documented failure**, not a hypothetical — Alaska 2022 is one of the clearest real-world monotonicity failures on record, which is exactly why it's worth teaching.
- **But it is rare.** Monotonicity failures need a near-three-way race with a specific transfer structure; most IRV elections never trigger one. Don't oversell frequency — sell the *structural* point: IRV's winner can depend on elimination order, and elimination order can move the wrong way.
- **It is IRV-specific, not "ranked voting" writ large.** The same ranked ballots counted by [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/README.md) are monotonic. Saying "ranked voting is non-monotonic" is imprecise; it's *instant-runoff* that is.
- **STAR is not perfectly immune to every monotonicity variant.** It passes mono-raise (no upward paradox), but fails the stronger **mono-raise-delete** in lab constructions — conceded and shown in the [worked set](README.md#the-301-nuance-star-fails-a-stronger-variant). Honesty is naming both.

The takeaway isn't "IRV is bad." It's that **a voter should be able to rank their favourite honestly without the ranking backfiring** — and STAR and Ranked Robin deliver that guarantee where instant-runoff can't.

## Sources

- Graham-Squire & McCune, *An Examination of the... [monotonicity] Paradoxes in the 2022 Alaska Special Election*, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075) — the origin of the upward/downward framing and the 6,000-ballot finding.
- [realrcv.equal.vote/alaska22](https://realrcv.equal.vote/alaska22) — an interactive walk-through (Equal Vote; advocacy-adjacent, clear on the mechanics).
- This library's [full Alaska 2022 case](../alaska_2022/) (101/201/301) and [burial companion](../condorcet_burial_alaska/) — the same real numbers, other pathologies.
