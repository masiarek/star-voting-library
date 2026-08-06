# 02_STAR_Bloc/03_Criteria — what Bloc STAR keeps, and what it drops

The formal side of [Bloc STAR](../01_Learn/bloc_star.md), always as **runnable elections rather than assertions**. Each set below isolates one criterion on the smallest electorate that shows it, and every one of them is a criterion the single-winner method is usually asked about — so the honest answer for the multi-winner version has to be checked, not inherited.

The prose companions live in [`01_Learn/`](../01_Learn/README.md); this folder is where those claims get numbers. Levels follow the [curriculum](../../07_Concepts/CURRICULUM.md): 🟢 101 · 🟡 201 · 🔴 301.

Why the folder exists at all: Bloc STAR **is** single-winner STAR, run once per seat — so it is tempting to assume every STAR property carries over. Some do. Two of the three sets below are cases where one does *not*, and the reason is always the same mechanism: the removal step builds a **fresh finalist pair** for every seat, and a change that cannot touch the first pair can still change the second.

| Set | Level | Elections | What it shows |
|---|:--:|---|---|
| [Participation](participation/README.md) | 🔴 301 | BV2264 [`j3hqvb`](https://bettervoting.com/j3hqvb/results) · BV2265 [`th3pbp`](https://bettervoting.com/th3pbp/results) | A voter joins, votes honestly, and gets a **worse council by their own ballot** — because their support lifted their favourite into the seat-2 runoff, where a candidate they scored 0 beat them. |
| [Seat order](seat_order/README.md) | 🟡 201 | BV2266 [`k7pfqt`](https://bettervoting.com/k7pfqt/results) | The candidate who beats **every** rival head-to-head is seated **second**. "First seated" is not "most preferred," which matters wherever the top finisher gets the chair. |
| [The committee spoiler](committee_spoiler/README.md) | 🔴 301 | BV2267 [`my9jd9`](https://bettervoting.com/my9jd9/results) · BV2268 [`6m3gxq`](https://bettervoting.com/6m3gxq/results) | Adding a candidate who **wins no seat** changes *which* candidates do — independence of irrelevant alternatives, at the level of the committee. |

Every one of the five elections is live on BetterVoting and reproduced independently in the LH engine, and **BV agrees with LH exactly** in all five: same winners, same seat order, every ballot counted, and `tieBreakType: none` at every seat — nothing here rests on a lot. The ballots, the seat-by-seat count and the frozen export live with the case.

## What is *not* here (yet)

Recorded so the gaps are visible rather than implied:

- **Monotonicity.** Raising a seated candidate has not been made to cost them their seat: a strict search over ~377,000 tie-free profiles found no failure, and the two-seat case looks provable (a seat-2 winner had to beat the overall score leader head-to-head — the very opponent a raise would put in front of them at seat 1). Being settled; see the working note in `_notes/`.
- **Reinforcement, clones, and strategic min-maxing.** Claimed in [honest limits](../01_Learn/bloc_honest_limits.md), not yet backed by a runnable case.
- **Proportionality axioms (JR / PJR / EJR).** The formal statement of "Bloc STAR is not proportional," which the folder currently teaches by [worked sweep](../01_Learn/majority_sweep.md) instead.

## Related

- The method and its limits: [Bloc STAR](../01_Learn/bloc_star.md) · [honest limits](../01_Learn/bloc_honest_limits.md) · [ties, seat by seat](../01_Learn/bloc_tiebreaks.md)
- The single-winner criteria gallery this mirrors: [01_STAR/03_Criteria](../../01_STAR/03_Criteria/README.md)
- The proportional alternative these criteria keep pointing at: [STAR-PR](../../03_STAR_PR/README.md)

# file: README.md
