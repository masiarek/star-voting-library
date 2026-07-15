# 02_STAR_Bloc — Bloc STAR (multi-winner, majoritarian)

Filling **several seats at once** — a city council, a board, a committee — with the same expressive STAR ballot. Bloc STAR is the *majoritarian* multi-winner method: it asks "who does the majority most want?" for every seat. Its proportional cousin, [STAR-PR](../03_STAR_PR/), instead tries to give every faction its fair share. Which you want depends on the body you're electing — this folder teaches the majoritarian one and, just as importantly, **when not to use it**.

New to STAR itself? Learn the single-winner method first — [STAR — start here](../00_start_here/STAR_Voting/STAR_start_here.md) — because Bloc STAR is just that method, run once per seat.

---

## How Bloc STAR works

You score every candidate 0–5, exactly like single-winner STAR. To fill **N seats**, the count runs single-winner STAR **N times**:

1. **Seat 1:** score everyone; the two highest advance to an automatic runoff; the runoff winner takes the seat.
2. **Remove that winner** from every ballot.
3. **Seat 2:** re-run the same STAR count on who's left. Repeat until all seats are filled.

*Worked example ([the baseline case](_main/00_c3_b3_bloc-baseline-2-seats.yaml)):* 3 candidates, 2 seats. Score round: Alice 14, Bruno 12 are the top two; in the runoff Alice is preferred 2–1, so **Alice takes seat 1**. Remove Alice and re-run on the remaining two: **Bruno takes seat 2**.

## The one thing to understand: majoritarian, not proportional

Because every seat is decided by the *same* electorate on the *same* ballots, **a cohesive majority can win every seat.** If 55% of voters share a slate, that slate can sweep the whole council 5–0, leaving the 45% with no representation at all.

That is a **feature or a bug depending on what you're electing:**

- **Use Bloc STAR** when you *want* the body to reflect the majority as a unit — e.g. a slate of officers who must govern together, or any at-large seat where "the candidates most voters prefer" is the goal.
- **Don't use it** when you want minorities represented — a legislature, a diverse committee. There, a majority sweep is exactly the wrong outcome, and you want **[Proportional STAR (STAR-PR)](../03_STAR_PR/)** instead.

This tension is the whole reason proportional methods exist. Gentle intro to the trade-off (approval side, counting only): [Electing a committee — making sure people have a voice](../00_start_here/Approval_Voting/abc_rules_intro.md). Concept hub: [proportional representation](../00_start_here/proportional_representation/).

## Learning path

1. **The baseline** — the smallest Bloc election that decides something (3 cand, 2 seats): [`00_c3_b3_bloc-baseline-2-seats`](_main/00_c3_b3_bloc-baseline-2-seats.yaml).
2. **A basic two-seat race** — see the elect-remove-rerun loop on a slightly bigger field: [`01_c4_b2_bloc-star-2-seats`](_main/01_c4_b2_bloc-star-2-seats.yaml) (the CURRICULUM 201.5 file).
3. **Watch a majority sweep** — internalize why Bloc is majoritarian, then contrast with the same electorate under [STAR-PR](../03_STAR_PR/) and [Bloc Plurality / SNTV](../method_comparisons/multi_member_plurality/).
4. **Edge cases & trust (201/301)** — how ties resolve seat-by-seat, and where BetterVoting's display diverges: the reference cases below.

Curriculum context: [201.5 — Multi-winner intro: Bloc STAR](../00_start_here/CURRICULUM.md).

---

## The reference cases

Every YAML carries `expected_winners` and is auto-checked by the test suite; BV-backed cases also keep a frozen `_bv_export.json` and a two-view `.md`. Many of these were built to expose or confirm a specific **tie-breaking or reporting** behavior in BetterVoting.

**Start here (teaching):**

| Case | Seats | What it shows |
|---|:--:|---|
| [`00` — pure baseline](_main/00_c3_b3_bloc-baseline-2-seats.yaml) | 2 | The clean elect-remove-rerun loop, no tiebreak — read this first. |
| [`01` — basic two-seat](_main/01_c4_b2_bloc-star-2-seats.yaml) | 2 | 4 candidates, 2 seats — the CURRICULUM 201.5 intro file. |
| [Shadow STAR — Lackner & Skowron](_main/lackner_skowron_shadow_bloc_star_c7_b12.yaml) | 4 | Bloc STAR on the academic running example used across the multi-winner literature. |

**Tie-breaking & BetterVoting reproductions (201/301):**

| BV id | Scenario | Seats | Tie? | BV status / issue | Case |
|-------|----------|:--:|------|-------------------|------|
| BV1815 | 3c/2s — seat 2 by **score** tiebreak | 2 | runoff (seat 2) | Passed | [page](_main/_main_pages/bv1815_bloc_3c2s_basic.md) · [yaml](_main/bv1815_bloc_3c2s_basic.yaml) |
| BV132 | verify votes cast — flat ballots dropped | 2 | flat/no-pref | Failed · [#1073](https://github.com/Equal-Vote/bettervoting/issues/1073) | [page](_main/bv132_verify_votes_bloc.md) · [yaml](_main/bv132_verify_votes_bloc.yaml) |
| BV131 | Guido example — **hidden lot-decided tie** (seat 1) | 2 | lot (seat 1) | "Passed" (but a coin toss; `tieBreakType` mislabeled `none`) | [page](_main/_main_pages/bv131_guido_bloc.md) · [yaml](_main/bv131_guido_bloc.yaml) |
| BV129 | 3c/2w — seat 2 by **score** tiebreak | 2 | runoff (seat 2) | count OK; "Failed" = method-name label [#1086](https://github.com/Equal-Vote/bettervoting/issues/1086) | [page](_main/_main_pages/bv129_score_tiebreak_bloc.md) · [yaml](_main/bv129_score_tiebreak_bloc.yaml) |
| BV126 | "ties every step" | — | yes | Failed · [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) | *pending* |
| BV750 | tie-breaking — all ballots identical (5,5,5) | 2 | lot (both seats) | Failed — every ballot dropped (`nTallyVotes 0`) [#1052](https://github.com/Equal-Vote/bettervoting/issues/1052) | [page](_main/_main_pages/bv750_tie_breaking_bloc.md) · [yaml](_main/bv750_tie_breaking_bloc.yaml) |
| BV130 | 6c/3w — original (clean, no tie) | 3 | none | tabulation OK; reporting fix (tabs → pages) star-server#731 | [page](_main/_main_pages/bv130_bloc_pagination_731.md) · [yaml](_main/bv130_bloc_pagination_731.yaml) |
| BV130-r2 | 6c/3w — **dead-rung lot tie** (seat 1) | 3 | lot (seat 1) | Passed (`9ff9jk`); lot-decided seat, `tieBreakType` reads `none` | [page](_main/_main_pages/bv130r2_dead_rung_bloc.md) · [yaml](_main/bv130r2_dead_rung_bloc.yaml) |
| BV1525 | 5c/4w — **Condorcet-loser ties for seat 1** (electowiki) | 4 | lot (seat 1) | LH reproduces First–Fourth; STAR 2.0 random-tie non-reproducible | [page](_main/_main_pages/bv1525_condorcet_loser_bloc.md) · [yaml](_main/bv1525_condorcet_loser_bloc.yaml) |
| BV2105 | Favorite ice cream demo | 2 | — | Failed (regression) | [yaml](_main/bv2105_r4dqvd_ice_cream_bloc.yaml) |

## Related

- **Proportional multi-winner** (the contrast): [Proportional STAR](../03_STAR_PR/) · concept: [proportional representation](../00_start_here/proportional_representation/)
- **Other multi-winner methods:** [Bloc Plurality / SNTV](../method_comparisons/multi_member_plurality/) · [a six-method governance election](../method_comparisons/pets_governance/)
- **Single-winner foundation:** [STAR — start here](../00_start_here/STAR_Voting/STAR_start_here.md) · [the benefits of STAR](../00_start_here/STAR_Voting/STAR_benefits.md)
- **Conversation scripts:** [What's so good about STAR](../00_start_here/STAR_Voting/whats_so_good_about_STAR_Voting.md) · [full index](../00_start_here/about_this_repo/conversation_scripts.md)

# file: README.md
