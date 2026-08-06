# 02_STAR_Bloc — Bloc STAR (multi-winner, majoritarian)

*Score every candidate 0–5, exactly as in single-winner STAR. Then run that entire count once per seat.*

<img src="01_Learn/img/ballot_bloc_star.png" width="460" alt="A Bloc STAR ballot. Heading: Bloc STAR Voting. Above the race: This election will elect 3 winners. Instructions: give your favorite candidate five stars; give your last choice zero stars or leave them blank; equal scores are allowed; score other candidates as desired. A 0-5 grid with one row per candidate, marked Andre 5, Blake 0, Carmen 1, David 4, Ella 4. Below the grid: This election will use Bloc STAR Voting to elect 3 winners. In Bloc STAR Voting, the two highest scoring candidates are finalists and your vote goes to the finalist you prefer. The finalist preferred by the most voters wins. This process repeats until all seats have been filled.">

*The ballot — drawn here from the [STAR Voting technical specifications](https://www.starvoting.org/technical_specifications) §3.b–3.d rather than screenshotted, because BetterVoting's live one prints neither the right method name nor the sentence that explains multi-winner. Only two things on this page mark it as a multi-seat race: the **seat count above the grid**, and the **last sentence below it**. Nothing is rationed — three seats are up and you still score every candidate, once. Full treatment, beside its single-winner twin: [the Bloc STAR ballot](01_Learn/bloc_star_ballot.md).*

Filling **several seats at once** — a city council, a board, a committee — with the same expressive STAR ballot. Bloc STAR is the *majoritarian* multi-winner method: it asks "who does the majority most want?" for every seat. Its proportional cousin, [STAR-PR](../03_STAR_PR/README.md), instead tries to give every faction its fair share. Which you want depends on the body you're electing — this folder teaches the majoritarian one and, just as importantly, **when not to use it**.

New to STAR itself? Learn the single-winner method first — [STAR — start here](../01_STAR/01_Learn/STAR_start_here.md) — because Bloc STAR is just that method, run once per seat.

**The concept pages live in [`01_Learn/`](01_Learn/README.md)** — the method, the majority sweep, the score leader who wins no seat, ties seat-by-seat, the at-large family, and the honest limits. This page is the folder's front door and the index of its runnable cases.

---

## How Bloc STAR works

You score every candidate 0–5, exactly like single-winner STAR. To fill **N seats**, the count runs single-winner STAR **N times**:

1. **Seat 1:** score everyone; the two highest advance to an automatic runoff; the runoff winner takes the seat.
2. **Remove that winner** from every ballot.
3. **Seat 2:** re-run the same STAR count on who's left. Repeat until all seats are filled.

*Worked example ([the baseline case, counted in full](02_Examples/cases/cases_pages/00_c3_b3_bloc-baseline-2-seats.md)):* 3 candidates, 2 seats. Score round: Alice 14, Bruno 12 are the top two; in the runoff Alice is preferred 2–1, so **Alice takes seat 1**. Remove Alice and re-run on the remaining two: **Bruno takes seat 2**.

## The one thing to understand: majoritarian, not proportional

Because every seat is decided by the *same* electorate on the *same* ballots, **a cohesive majority can win every seat.** If 55% of voters share a slate, that slate can sweep the whole council 5–0, leaving the 45% with no representation at all.

That is a **feature or a bug depending on what you're electing:**

- **Use Bloc STAR** when you *want* the body to reflect the majority as a unit — e.g. a slate of officers who must govern together, or any at-large seat where "the candidates most voters prefer" is the goal.
- **Don't use it** when you want minorities represented — a legislature, a diverse committee. There, a majority sweep is exactly the wrong outcome, and you want **[Proportional STAR (STAR-PR)](../03_STAR_PR/README.md)** instead.

This tension is the whole reason proportional methods exist. Gentle intro to the trade-off (approval side, counting only): [Electing a committee — making sure people have a voice](../04_Approval/01_Learn/Multiwinner_Approval/abc_rules_intro.md). Concept hub: [proportional representation](../03_STAR_PR/01_Learn/README.md).

## Learning path

1. **The method** — the elect-remove-rerun loop, what the removal step does and doesn't do: [Bloc STAR](01_Learn/bloc_star.md). See the paper it runs on first if you'd rather start concrete: [the Bloc STAR ballot](01_Learn/bloc_star_ballot.md) — three seats change three lines of text and nothing about how you mark it. Its smallest runnable form is [the baseline case](02_Examples/cases/cases_pages/00_c3_b3_bloc-baseline-2-seats.md) (3 candidates, 2 seats), then [a 2-seat committee election](02_Examples/cases/cases_pages/01_c4_b2_bloc-star-2-seats.md) (4 candidates; the CURRICULUM 201.5 file).
2. **Watch a majority sweep** — internalize why Bloc is majoritarian: [The majority sweep](01_Learn/majority_sweep.md). Worked at whiteboard scale in [exercise 12](../01_STAR/05_Practice/ex12_bloc_vs_proportional.md) (60% takes both seats, then the same ten ballots counted proportionally), and against four other counts on one electorate in [Food-Truck Row](../method_comparisons/food_truck_row/README.md). Contrast: [STAR-PR](../03_STAR_PR/README.md) and [Bloc Plurality / SNTV](../method_comparisons/multi_member_plurality/README.md).
3. **The compromise candidate, shut out** — [the score leader can win no seat](01_Learn/score_leader_no_seat.md), worked on the first case here at a realistic electorate (100 voters, 4 seats): [BV1835](02_Examples/bv1835_8h3yrx_score_leader_no_seat.md). Ava leads every scoring round by sixty-three points and takes nothing, losing all four runoffs 51–49. Read it for what the **runoff** step does: Bloc seats whoever is *preferred*, not whoever accumulates points. Note this is the *opposite* configuration to a sweep — two even camps splitting the seats 2–2.
4. **Edge cases & trust (201/301)** — [ties, seat by seat](01_Learn/bloc_tiebreaks.md): how the STAR ladder runs once per seat, how a seat-1 coin toss can change *who* wins seat 2, and where BetterVoting's display diverges. The reference cases below are the receipts.
5. **The honest version** — [what Bloc STAR concedes](01_Learn/bloc_honest_limits.md), and [how it sits among the other at-large methods](01_Learn/bloc_star_vs_other_bloc_methods.md).
6. **The criteria, as runnable elections (201/301)** — [`03_Criteria/`](03_Criteria/README.md): the properties single-winner STAR is usually asked about, *checked* for the multi-winner version rather than inherited. [Participation](03_Criteria/participation/README.md) — an honest joiner ends up with a worse council; [seat order](03_Criteria/seat_order/README.md) — the candidate who beats everyone head-to-head is seated second; [the committee spoiler](03_Criteria/committee_spoiler/README.md) — a candidate who wins nothing changes who does. Five BetterVoting elections, BV and LH agreeing exactly, no tie-break anywhere.

Curriculum context: [201.5 — Multi-winner intro: Bloc STAR](../07_Concepts/CURRICULUM.md).

---

## The reference cases

Every YAML carries `expected_winners` and is auto-checked by the test suite; BV-backed cases also keep a frozen `_bv_export.json` and a two-view `.md`. Many of these were built to expose or confirm a specific **tie-breaking or reporting** behavior in BetterVoting.

**How to read the link cells.** Every case is linked as an article first and a data file second: **page** / **count** is the readable write-up (scenario, ballots, the engine's full count) — start there; **lesson** is the hand-written two-view comparison (BetterVoting's result beside the independent LH count) that BV-backed cases also carry; **yaml** is the raw source you feed the engine to run it yourself.

**Start here (teaching):**

| Case | Seats | What it shows | Read · run |
|---|:--:|---|---|
| `00` — pure baseline | 2 | The clean elect-remove-rerun loop, no tiebreak — read this first. | [page](02_Examples/cases/cases_pages/00_c3_b3_bloc-baseline-2-seats.md) · [yaml](02_Examples/cases/00_c3_b3_bloc-baseline-2-seats.yaml) |
| `01` — basic two-seat | 2 | 4 candidates, 2 seats — the CURRICULUM 201.5 intro file. | [page](02_Examples/cases/cases_pages/01_c4_b2_bloc-star-2-seats.md) · [yaml](02_Examples/cases/01_c4_b2_bloc-star-2-seats.yaml) |
| Shadow STAR — Lackner & Skowron | 4 | Bloc STAR on the academic running example used across the multi-winner literature. | [page](02_Examples/cases/cases_pages/lackner_skowron_shadow_bloc_star_c7_b12.md) · [yaml](02_Examples/cases/lackner_skowron_shadow_bloc_star_c7_b12.yaml) |
| Lot path-dependence — **A** | 2 | A matched pair, LH-only. Identical ballots; only the published lot differs. Seat 1 is a perfect tie (score 15–15, five-star 3–3 — the rung is *live* and still can't separate them), so the lot decides it — and that choice changes **who wins seat 2**, not just the order. Lot `[Nadia, Omar, Priya]` → **Nadia, Priya**. | [page](02_Examples/cases/cases_pages/bloc_lot_path_dependence_a_c3_b5.md) · [yaml](02_Examples/cases/bloc_lot_path_dependence_a_c3_b5.yaml) |
| Lot path-dependence — **B** | 2 | The same five ballots, lot reversed to `[Omar, Nadia, Priya]` → **Omar, Nadia**. Priya is on the council in A and absent from B. The demonstration behind [ties, seat by seat](01_Learn/bloc_tiebreaks.md). | [page](02_Examples/cases/cases_pages/bloc_lot_path_dependence_b_c3_b5.md) · [yaml](02_Examples/cases/bloc_lot_path_dependence_b_c3_b5.yaml) |
| A race nobody can lose — **the control** | 2 | The seven ballots of BV2269 with one seat removed, so they count normally. Pair it with the three-seat file below: Celia wins nothing here and is a board member there, on the same ballots. | [page](02_Examples/cases/cases_pages/race_nobody_can_lose_two_seat_control.md) · [yaml](02_Examples/cases/race_nobody_can_lose_two_seat_control.yaml) |

**Tie-breaking & BetterVoting reproductions (201/301):**

| BV id | Scenario | Seats | Tie? | BV status / issue | Read · run |
|-------|----------|:--:|------|-------------------|------|
| BV1815 | 3c/2s — seat 2 by **score** tiebreak | 2 | runoff (seat 2) | Passed | [lesson](02_Examples/bv1815_bloc_3c2s_basic.md) · [count](02_Examples/cases/cases_pages/bv1815_bloc_3c2s_basic.md) · [yaml](02_Examples/cases/bv1815_bloc_3c2s_basic.yaml) |
| BV132 | verify votes cast — flat ballots dropped | 2 | flat/no-pref | Failed · [#1073](https://github.com/Equal-Vote/bettervoting/issues/1073) | [lesson](02_Examples/bv132_verify_votes_bloc.md) · [count](02_Examples/cases/cases_pages/bv132_verify_votes_bloc.md) · [yaml](02_Examples/cases/bv132_verify_votes_bloc.yaml) |
| BV131 | Guido example — **hidden lot-decided tie** (seat 1) | 2 | lot (seat 1) | "Passed" (but a coin toss; `tieBreakType` mislabeled `none`) | [lesson](02_Examples/bv131_guido_bloc.md) · [count](02_Examples/cases/cases_pages/bv131_guido_bloc.md) · [yaml](02_Examples/cases/bv131_guido_bloc.yaml) |
| BV129 | 3c/2w — seat 2 by **score** tiebreak | 2 | runoff (seat 2) | count OK; "Failed" = method-name label [#1086](https://github.com/Equal-Vote/bettervoting/issues/1086) ([note](02_Examples/bv129_1086_method_name_note.md)) | [lesson](02_Examples/bv129_score_tiebreak_bloc.md) · [count](02_Examples/cases/cases_pages/bv129_score_tiebreak_bloc.md) · [yaml](02_Examples/cases/bv129_score_tiebreak_bloc.yaml) |
| BV126 | "ties every step" | — | yes | Failed · [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) | *pending* |
| BV750 | tie-breaking — all ballots identical (5,5,5) | 2 | lot (both seats) | Failed — every ballot dropped (`nTallyVotes 0`) [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) | [lesson](02_Examples/bv750_tie_breaking_bloc.md) · [count](02_Examples/cases/cases_pages/bv750_tie_breaking_bloc.md) · [yaml](02_Examples/cases/bv750_tie_breaking_bloc.yaml) |
| BV130 | 6c/3w — original (clean, no tie) | 3 | none | tabulation OK; reporting fix (tabs → pages) star-server#731 | [lesson](02_Examples/bv130_bloc_pagination_731.md) · [count](02_Examples/cases/cases_pages/bv130_bloc_pagination_731.md) · [yaml](02_Examples/cases/bv130_bloc_pagination_731.yaml) |
| BV130-r2 | 6c/3w — **dead-rung lot tie** (seat 1) | 3 | lot (seat 1) | Passed (`9ff9jk`); lot-decided seat, `tieBreakType` reads `none` | [lesson](02_Examples/bv130r2_dead_rung_bloc.md) · [count](02_Examples/cases/cases_pages/bv130r2_dead_rung_bloc.md) · [yaml](02_Examples/cases/bv130r2_dead_rung_bloc.yaml) |
| BV1525 | 5c/4w — **Condorcet-loser ties for seat 1** (electowiki) | 4 | lot (seat 1) | LH reproduces First–Fourth; STAR 2.0 random-tie non-reproducible | [lesson](02_Examples/bv1525_condorcet_loser_bloc.md) · [count](02_Examples/cases/cases_pages/bv1525_condorcet_loser_bloc.md) · [yaml](02_Examples/cases/bv1525_condorcet_loser_bloc.yaml) |
| BV2105 | Favorite ice cream demo — a partial ballot filed as an abstention | 2 | — | Failed (2025 baseline) · [#1478](https://github.com/Equal-Vote/bettervoting/issues/1478) — *not* #1056, a different bug on the same election | [lesson](02_Examples/bv2105_r4dqvd_ice_cream_bloc.md) · [count](02_Examples/cases/cases_pages/bv2105_r4dqvd_ice_cream_bloc.md) · [yaml](02_Examples/cases/bv2105_r4dqvd_ice_cream_bloc.yaml) |
| BV2105-r2 | the same four ballots, re-cast a year later | 2 | — | Failed again — **still reproduces** (2026-08-04); filed as [#1478](https://github.com/Equal-Vote/bettervoting/issues/1478) | [lesson](02_Examples/bv2105r2_w3vvff_ice_cream_recheck.md) · [count](02_Examples/cases/cases_pages/bv2105r2_w3vvff_ice_cream_recheck.md) · [yaml](02_Examples/cases/bv2105r2_w3vvff_ice_cream_recheck.yaml) |
| BV1835 | 5c/4w, **100 voters** — the score leader is the Condorcet loser and wins nothing (all four runoffs 51–49) | 4 | none | Passed (`8h3yrx`); LH and BV agree exactly | [lesson](02_Examples/bv1835_8h3yrx_score_leader_no_seat.md) · [count](02_Examples/cases/cases_pages/bv1835_8h3yrx_score_leader_no_seat.md) · [yaml](02_Examples/cases/bv1835_8h3yrx_score_leader_no_seat.yaml) |
| — (`484mbm`) | 3c/2s — **every rung ties** (score, pairwise, five-star) on rotating ballots | 2 | lot (seat 1) | LH reproduces BV once the perm is pinned; BV skips pairwise on 3-way ties and its top-level `tieBreakType` reads `none` | [lesson](02_Examples/b484mbm_tie_every_rung.md) · [count](02_Examples/cases/cases_pages/b484mbm_tie_every_rung.md) · [yaml](02_Examples/cases/b484mbm_tie_every_rung.yaml) |
| BV2269 | 3c/**3s** — a race nobody can lose: as many seats as candidates | 3 | none | The engines disagree on the *premise*: LH refuses the file (exit 1, no tally); BV accepts it, counts seats 1–2 normally and reports "Celia is the only candidate, and wins by default" for seat 3 | [lesson](02_Examples/bv2269_t488h9_race_nobody_can_lose.md) · [count](02_Examples/cases/cases_pages/bv2269_t488h9_race_nobody_can_lose.md) · [yaml](02_Examples/cases/bv2269_t488h9_race_nobody_can_lose.yaml) |

## Related

- **The concept pages for this method:** [`01_Learn/`](01_Learn/README.md) — [the method](01_Learn/bloc_star.md) · [the ballot](01_Learn/bloc_star_ballot.md) · [the majority sweep](01_Learn/majority_sweep.md) · [the score leader wins no seat](01_Learn/score_leader_no_seat.md) · [ties, seat by seat](01_Learn/bloc_tiebreaks.md) · [the at-large family](01_Learn/bloc_star_vs_other_bloc_methods.md) · [honest limits](01_Learn/bloc_honest_limits.md) · [glossary](01_Learn/glossary_bloc_star.md)
- **Proportional multi-winner** (the contrast): [Proportional STAR](../03_STAR_PR/README.md) · concept: [proportional representation](../03_STAR_PR/01_Learn/README.md)
- **Other multi-winner methods:** [Bloc Plurality / SNTV](../method_comparisons/multi_member_plurality/README.md) · [a six-method governance election](../method_comparisons/pets_governance/README.md)
- **Single-winner foundation:** [STAR — start here](../01_STAR/01_Learn/STAR_start_here.md) · [the benefits of STAR](../01_STAR/01_Learn/getting_started/STAR_benefits.md)
- **Conversation scripts:** [What's so good about STAR](../01_STAR/01_Learn/reference/whats_so_good_about_STAR_Voting.md) · [full index](../07_Concepts/about_this_repo/conversation_scripts.md)

# file: README.md
