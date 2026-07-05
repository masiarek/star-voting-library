# BV_Library — real BetterVoting elections, imported and verified

Parity cases: real BetterVoting results re-tabulated by the LH engine to confirm the two agree, across every method BetterVoting runs — STAR, Approval, Plurality, and Ranked Robin — including the tricky tiebreak paths. Each `expected_winners` is guarded by the positive test harness.

Read the reader-friendly **pages** (`BV_Library_pages/`); the `.yaml` beside each is the tabulatable source.

## STAR

| Page (read this) | What it shows | src |
|---|---|:--:|
| [Condorcet winner](BV_Library_pages/BV_Library_star_condorcet_winner.md) | highest-scoring candidate is also the pairwise winner | [`.yaml`](BV_Library_star_condorcet_winner.yaml) |
| [runoff](BV_Library_pages/BV_Library_star_runoff.md) | the lower score total wins the automatic runoff | [`.yaml`](BV_Library_star_runoff.yaml) |
| [runner-up tie](BV_Library_pages/BV_Library_star_runnerup_tie.md) | second finalist decided by tiebreak — Allison wins | [`.yaml`](BV_Library_star_runnerup_tie.yaml) |
| [runoff tie → score](BV_Library_pages/BV_Library_star_runoff_tie_score_resolves.md) | a tied runoff broken by score total | [`.yaml`](BV_Library_star_runoff_tie_score_resolves.yaml) |
| [runoff & score tie → five-star](BV_Library_pages/BV_Library_star_runoff_score_tie_five_star.md) | both tied, resolved by the five-star tiebreaker | [`.yaml`](BV_Library_star_runoff_score_tie_five_star.yaml) |

## STAR_PR (Allocated Score) — multi-winner

Ported from BetterVoting's `AllocatedScore.test.ts`. LH's `allocated` method reproduces BetterVoting's elected committee in each case. (BetterVoting's four fractional-surplus variants all elect the same committee, {Allison, Doug}; one representative is included. Random-tiebreak and vote-count-sanitization cases are omitted.)

| What it shows | src |
|---|:--:|
| basic two-seat allocation — elect top scorer, spend a quota, second seat follows | [`.yaml`](BV_Library_star_pr_basic_two_seats.yaml) |
| fewer voters than seats — every seat still fills, in score order | [`.yaml`](BV_Library_star_pr_voters_fewer_than_seats.yaml) |
| fractional surplus — 8 supporters vs a quota of 6 → ballots reweighted to 0.25 | [`.yaml`](BV_Library_star_pr_fractional_surplus.yaml) |

## Approval · Plurality · Ranked Robin

| Page (read this) | What it shows | src |
|---|---|:--:|
| [Approval](BV_Library_pages/BV_Library_approval_single_winner.md) | most approvals wins | [`.yaml`](BV_Library_approval_single_winner.yaml) |
| [Plurality](BV_Library_pages/BV_Library_plurality_single_winner.md) | choose-one: most first-marks wins | [`.yaml`](BV_Library_plurality_single_winner.yaml) |
| [Ranked Robin](BV_Library_pages/BV_Library_ranked_robin_single_winner.md) | Condorcet winner, equal ranks allowed | [`.yaml`](BV_Library_ranked_robin_single_winner.yaml) |
| [Ranked Robin — tie](BV_Library_pages/BV_Library_ranked_robin_ties.md) | a Copeland tie broken by tiebreak order | [`.yaml`](BV_Library_ranked_robin_ties.yaml) |

Up: [method_comparisons — same ballots, different methods](../)

# file: README.md
