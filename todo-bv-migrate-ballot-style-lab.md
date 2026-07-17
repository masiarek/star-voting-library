# TODO — BV-migrate the ballot-style lab (+ parked backlog from 2026-07-17)

Working notes to pick up later. Not site content (excluded in `mkdocs.yml`). Delete sections as they're done.

## 1. The headline task: take the ballot-style lab live on BetterVoting

`06_Other/ballot_style_lab/` holds ten frozen scenario yamls with **no BV elections yet** — the single-winner set (01–06) and the new multi-winner wing (07a/07b Herb Garden Council Bloc-vs-PR same-ballots pair, 08 Quota Circus STAR-PR, 09 Park Bloc 4-seats). Migrate them the way the exercises set went live (BV2191–2202): specs in `bv_election_specs.py`, next free Test IDs from the registry (**BV2211+** as of this writing), create via `create_bv_test_election.py`, verify winners via `/API/ElectionResult/<id>`, freeze UI exports, wire `bv_*` fields into the yamls, regen registry, note BV-vs-LH agreement per case page.

Cautions, learned 2026-07-17:

- **07a's Bloc final seat hangs on an 83–82 score rung** — confirm the whole ladder resolves deterministically on BV before freezing; any lot/random-decided seat stays **LH-only** (don't migrate it). The lab's hunter already rejected lot-decided seeds, but verify one champion by hand.
- **Every STAR_PR race will banner "Tied!" spuriously** (`tieBreakType: random`, no tie) — the serializer quirk with three confirmed instances (`89wwvr`, `jwxr3j`, `fvg8y8`). Seats compute correctly; note the quirk in each case page rather than treating it as a divergence.
- **If any scenario ever gets an STV race:** a count whose eliminations leave one hopeful who then reaches quota **crashes BV** (`06_Other/STV/bv_stv_sole_survivor_crash/`) — design the endgame with a hopeful standing, or wait for the fix.
- **Coordination:** the lab is another session's active thread (commit `51f0a30`); pick this up there or after its index churn settles.

## 2. Loose ends from the 2026-07-17 session (BV2203–BV2210 + Burlington)

- **Push:** `git push https://github.com/masiarek/star-voting-library.git master`
- **File the STV crash issue** on Equal-Vote/bettervoting — ready-to-file text sits in [06_Other/STV/bv_stv_sole_survivor_crash/README.md](06_Other/STV/bv_stv_sole_survivor_crash/README.md).
- **Freeze UI exports** when convenient: `7mckyg`, `b6xrdr` (FBC pair) · `7q6by8`, `fxhw6g` (burial pair) · `fvg8y8` (food-truck row) · `39py93` (STV control). The crashers `gvtg2h`/`8xwx43` export without Results until BV ships the fix — re-export then.
- **divergence_review builder nit:** its generated page for `bv2206…` says "Ranked Robin and Condorcet agree with STAR" while its own table shows RR = Bluebell ≠ STAR = Clover — the boilerplate doesn't read its own numbers. Fix in `build_divergence_index.py`, regen.
- Recorded, no action needed: the burial pair's **live BV descriptions** carry a wrong slim-vs-blowout aside (permanent); corrected analysis lives in the repo yamls + `05_Ranked_Robin/burial/README.md`.

## 3. Parked proposal backlog (from the kick-the-tires menu, unbuilt)

Each line is meant to be enough to start cold. Rough priority within groups.

**Criterion cases (BV-backable pairs unless noted):**

- **STAR fails mutual majority** — a solid 60% coalition over {A, B} splits its scores and C wins; the honest "IRV beats STAR on this criterion" case. No mutual-majority case exists anywhere in the repo.
- **STAR elects outside the Smith set** — the score round promotes a candidate the whole top cycle beats; repo has zero Smith-set cases.
- **Reversal symmetry** — flip every ballot; IRV can elect the *same* winner both directions ("the favorite and least-favorite are the same person"). New paradox-tag candidate for the index.
- **The IRV "majority" asterisk** — a winner whose final-round "majority" is under 50% of ballots *cast* (exhaustion). Targets the exact sentence "IRV guarantees a majority winner"; sits beside `bv2183`.
- **STAR exaggeration pair** — same opinions, honest 0–5 vs everyone min-maxing (collapses to approval-style); what strategy buys and costs in STAR. Pairs with ex13.

**Multi-winner wing (deepens ex12/ex14 + food_truck_row):**

- **STV vs STAR-PR electing *different* sets from the same opinions** — two proportional methods disagreeing about what proportionality means; lead with the same-opinion line-up table.
- **Droop rounding at 3 seats, 60/40** — do both PR methods give 2–1?
- **Free-riding in STAR-PR** — a voter deflates a sure-winner's score to boost their second pick; the PR-world strategy nobody demos.
- **Multi-winner tie shelf (LH-only)** — STV bottom-two elimination tie, STAR-PR final-seat tie, Bloc final-seat tie; document LH's deterministic lot vs BV's random (extends the tie-ladder shelf into multi-winner, currently empty).

**Real elections (PrefLib pipeline proven by Burlington — see memory note + `method_comparisons/burlington_2009/`):**

- **Alaska 2022 special** — the Burlington sibling: center squeeze + non-monotonicity + no-show on real ballots (Graham-Squire & McCune, arXiv:2301.12075); worked prose already in `favorite_betrayal_voting_301.md` §4, needs the runnable case.
- **Eurovision** — public jury/televote data is literal score voting; a real, familiar election for the STAR intro shelf.

**Engine robustness (cheap LH negative/edge tests):**

- `num_winners` ≥ candidate count; a 1-candidate election; an all-abstain electorate; duplicate candidate names; CJK/emoji names vs report column alignment; equal-ranks input `A>B=C` (pin: clear error or support); a case exercising the `%` spoiled-and-reissued marker end-to-end.

**Tooling:**

- **Cross-engine agreement fuzzer** — random small elections through LH vs `pref_voting` (same method: STAR, IRV, Copeland), diff winners; any disagreement is a tiebreak-policy doc item or a real bug. Industrializes the RR triple-check; extends the existing `find_divergence` miners (which hunt cross-*method*, not cross-*engine*).

# file: todo-bv-migrate-ballot-style-lab.md
