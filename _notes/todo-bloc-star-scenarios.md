# TODO — Bloc STAR: the scenarios `02_STAR_Bloc/` still needs

Working notes to pick up later. Not site content (excluded via `todo-*.md` in `mkdocs.yml`). Delete sections as they're done.

Built 2026-08-04 by inventorying [`02_STAR_Bloc/`](../02_STAR_Bloc/README.md) against a criterion-by-criterion checklist, then *searching* for the gaps rather than assuming they exist: an independent re-implementation of the elect–remove–re-run loop scanned random profiles, and every hit was re-run through the real LH engine before it was believed. Method and reproduction in [§6](#6-how-the-search-was-run).

**Headline: four items are build-now, not research** — §2 carries engine-verified profiles, paste-ready. The one worth *thinking* about rather than building is monotonicity (§3.1): the search found no failure, and the 2-seat case looks provable, which would be a positive result the folder can state instead of a gap.

> **Update 2026-08-04 — §2.1, §2.2 and §2.3 are DONE.** All three shipped as
> [`02_STAR_Bloc/03_Criteria/`](../02_STAR_Bloc/03_Criteria/README.md), backed by five
> BetterVoting elections minted the same day — BV2264 `j3hqvb` / BV2265 `th3pbp`
> (participation), BV2266 `k7pfqt` (seat order), BV2267 `my9jd9` / BV2268 `6m3gxq`
> (committee spoiler). BV reproduces the LH count exactly in all five, with
> `tieBreakType: none` at every seat. §3 is untouched and still the live list.
>
> **Update 2026-08-04 (later) — §2.4 is DONE too.** Adam authorised the mint, so the
> probe was run: BV2269 [`t488h9`](https://bettervoting.com/t488h9/results), written up
> as [a race nobody can lose](../02_STAR_Bloc/02_Examples/bv2269_t488h9_race_nobody_can_lose.md).
> **All of §2 is now closed.**

---

## 1. Already covered — do not rebuild

| Scenario | Where it lives |
|---|---|
| The elect–remove–re-run loop, clean | [`00` baseline](../02_STAR_Bloc/02_Examples/cases/cases_pages/00_c3_b3_bloc-baseline-2-seats.md) · [`01` 4c/2s](../02_STAR_Bloc/02_Examples/cases/cases_pages/01_c4_b2_bloc-star-2-seats.md) |
| Majority sweep (majoritarian, not proportional) | [majority_sweep.md](../02_STAR_Bloc/01_Learn/majority_sweep.md) · [ex12](../01_STAR/05_Practice/ex12_bloc_vs_proportional.md) · [Food-Truck Row](../method_comparisons/food_truck_row/README.md) |
| A landslide buys *one* seat; seat 2 goes to a candidate most scored 0 | [over_50_percent.md](../02_STAR_Bloc/01_Learn/over_50_percent.md) |
| Score leader shut out of every seat | [score_leader_no_seat.md](../02_STAR_Bloc/01_Learn/score_leader_no_seat.md) · [BV1835](../02_STAR_Bloc/02_Examples/bv1835_8h3yrx_score_leader_no_seat.md) |
| A seat-1 tie changes *who* wins seat 2 (lot path dependence) | [bloc_tiebreaks.md](../02_STAR_Bloc/01_Learn/bloc_tiebreaks.md) · [lot A](../02_STAR_Bloc/02_Examples/cases/cases_pages/bloc_lot_path_dependence_a_c3_b5.md) / [lot B](../02_STAR_Bloc/02_Examples/cases/cases_pages/bloc_lot_path_dependence_b_c3_b5.md) |
| Tie rungs per seat: score rung, five-star, dead rung, all-identical ballots | BV1815 · BV129 · BV131 · BV130-r2 · BV750 |
| Condorcet loser ties for seat 1 | [BV1525](../02_STAR_Bloc/02_Examples/bv1525_condorcet_loser_bloc.md) |
| Academic running example | [Lackner & Skowron shadow](../02_STAR_Bloc/02_Examples/cases/cases_pages/lackner_skowron_shadow_bloc_star_c7_b12.md) |
| BV reporting: flat ballots dropped, pagination, method-name label | BV132 ([#1073](https://github.com/Equal-Vote/bettervoting/issues/1073)) · BV130 (star-server#731) · [#1086 note](../02_STAR_Bloc/02_Examples/bv129_1086_method_name_note.md) |
| At-large family comparison (SNTV, Limited, Bloc Approval, Bloc RR) | [bloc_star_vs_other_bloc_methods.md](../02_STAR_Bloc/01_Learn/bloc_star_vs_other_bloc_methods.md) |

What that inventory says about the shape of the folder: **it is strong on ties and on BetterVoting reproductions, and empty on criteria.** Every scenario above is either the method working, the method being majoritarian, or a tiebreak. Not one is a criterion failure with a name — which is why 01_STAR has an [`03_Criteria/`](../01_STAR/03_Criteria/README.md) folder and Bloc has none (see §5).

---

## 2. Build now — profiles in hand, engine-verified

All four were confirmed with `.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py`. The full YAML for 2.1–2.3 is in [§4](#4-the-verified-profiles-paste-ready); no round in any of them touches a tiebreak rung, so nothing here depends on a lot order.

### 2.1 Participation failure — voting made the joiner's council worse ⭐ top pick

4 candidates, 2 seats, 6 ballots elect **{A, B}**. One more voter shows up and scores `A3 B2 C5 D0` — honestly. The council becomes **{A, D}**: they traded a candidate they scored 2 for one they scored 0, and their own ballot rates the new council 3 where the old one rated 5.

The mechanism is the teachable part, and it is specific to Bloc: their support lifted their favourite **C** from 11 points to 16, which pushed C past B into the *seat-2 runoff* — where C lost to D 4–2. **Helping your favourite reach the runoff is what handed the seat to the candidate you scored zero.** There is no reweighting step to absorb this, and it repeats once per seat.

Why it earns a page: the repo teaches the [no-show paradox](../07_Concepts/voting_paradoxes/no_show.md) only on ranked ballots (Burlington, Felsenthal Ex.4, the two RCV-IRV cases) — and STAR is *unmoved* in the Felsenthal pair, which currently reads as "STAR is fine here." The multi-winner form has a different, sharper shape: not "my favourite lost" but "the body I sit under got worse." Pairs with [honest limits §5](../02_STAR_Bloc/01_Learn/bloc_honest_limits.md). Tag `paradoxes: [no_show]`; a twin-paradox variant (clone the joiner) is a cheap second case.

### 2.2 The Condorcet winner is seated *second*

7 ballots, 4 candidates, 2 seats. Seat 1 → **D** (scores D24, B22; runoff D 2 – B 1, 4 Equal Support). Seat 2 → **A** (runoff A 4 – B 2). But A beats **every** rival head-to-head: A>B 4–2, A>C 5–2, **A>D 4–3**. The candidate the majority prefers to everyone finishes behind someone they beat.

Two reasons this is worth a case rather than a footnote:

- **Seat order is not cosmetic.** Plenty of at-large bodies give the top finisher something — chair, mayor, the longer term, the tiebreaking vote. Under Bloc STAR "first seated" is not "most preferred," and this profile is the receipt.
- **It is the single-winner failure with the sting removed.** Run the same ballots for one seat and it is a plain STAR Condorcet failure — A loses outright. The second seat *rescues* A. That is a genuinely nice thing to be able to show right after [three notions of winner](../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md).

Tag `paradoxes: [condorcet_winner_paradox]`. Level 301.

### 2.3 The committee spoiler — a candidate who wins nothing changes who does

Same 7 ballots counted twice. With three candidates the council is **{C, A}**. Add **D** — who takes no seat — and the council is **{C, B}**: A is displaced without D ever winning anything. D's arrival changes the *seat-2 finalist pair* (D 17 outscores B 16), and B beats D there while A never reaches a runoff at all.

The [IIA/cycle spoiler set](../01_STAR/03_Criteria/iia_cycle_spoiler/README.md) does this for one seat and needs a genuine cycle to do it. The Bloc version needs no cycle — the removal step manufactures a fresh finalist pair every seat, so an also-ran gets N chances to reshuffle the pair rather than one. Tag `paradoxes: [spoiler_scc]`.

### 2.4 Degenerate seat counts — the engine refuses, and BV probably doesn't

LH behaviour, confirmed:

| Input | LH engine |
|---|---|
| 3 candidates, 3 seats | `Error: cannot fill 3 seats from 3 candidate(s). num_winners must be smaller than the number of candidates.` |
| 3 candidates, 4 seats | same error |
| `voting_method: Bloc STAR`, `num_winners: 1` | `Error: Bloc STAR elects multiple winners, but got seats=1 (requires seats >= 2).` |

`Star.ts` takes `nWinners` and keeps running rounds until candidates run out, sorting the overflow into `elected` / `tied` / `other` — so BV very likely *accepts* a 3-candidate 3-seat race and seats everyone, with a scoring round and runoff printed for a contest that cannot decide anything. **Open question, and the answer belongs in the folder either way** ("what happens if you post a race nobody can lose"), because org admins create exactly this by accident.

Checking it means minting a BV election, and BV titles/descriptions are permanent — **ask before minting**, then follow the nine-step loop in the `bettervoting` skill. The LH half needs no permission and can be written today.

> **~~Held back on purpose~~ — ANSWERED 2026-08-04.** This was held back when the other
> three were minted, because asking the question meant creating a permanent, undeletable
> election whose public title had to describe a degenerate contest — Adam's call, not a
> default. He authorised it the same day, and the probe ran as **BV2269**
> [`t488h9`](https://bettervoting.com/t488h9/results).
>
> **The answer: BetterVoting accepts it, and reports it honestly.** All three candidates
> are seated in score order; seats 1 and 2 run genuine STAR rounds (28/23/16, then runoffs
> won 5–2 and 5–2, `tieBreakType: none` throughout); and seat 3 — the round with one
> candidate and nothing to run against — prints **"Celia is the only candidate, and wins
> by default"**, with an empty `runner_up` and an empty `logs` array in the JSON.
>
> So the prediction above was wrong in the informative direction: BV does *not* print a
> meaningless scoring round and runoff for the undecidable seat. It degrades into saying
> so. Written up as
> [a race nobody can lose](../02_STAR_Bloc/02_Examples/bv2269_t488h9_race_nobody_can_lose.md),
> with a two-seat control on the same ballots.
>
> One thing worth carrying forward: the mint nearly went out as a **duplicate BV2264**.
> The collision gate read case YAMLs only as far as their `ballots:` block, and
> BV2264–BV2268 carry `bv_test_id:` *below* the ballots, so it could not see any of the
> five it had just handed out. Fixed in `create_bv_test_election.py` before minting.

---

## 3. Open — needs a search, a proof, or a decision

Ordered by what the folder gains.

### 3.1 Monotonicity — settle it, most likely as a *positive* result

01_STAR states plainly that [STAR is monotone](../01_STAR/01_Learn/properties_and_limits/STAR_monotonicity.md). Bloc STAR is sequential, and sequential methods are where monotonicity usually dies, so the folder should say something. Current evidence says it survives:

- ~377,000 tie-free profiles across 8 shapes (4–6 candidates, 7–11 voters, 2–3 seats), raising a seated candidate by +1 on one ballot: **0 failures**.
- A targeted hunt at ~48,000 qualifying profiles — restricted to the only mechanism that could produce one (seat 1 decided by runoff *reversal*, so that a raise can evict the reversal winner from the finalist pair), raising on up to 5 ballots at once: **0 failures**.

And the 2-seat case looks provable. Sketch, worth checking properly before it goes on a page: let `w` take seat 2. To win it, `w` had to be a finalist there, and the seat-2 pool always contains the overall score leader `X` (removing the seat-1 winner cannot demote `X` unless `X` *is* the seat-1 winner) — so `w` beat `X` head-to-head. Now raise `w`. The only way that disturbs seat 1 is by lifting `w` into the finalist pair, and the pair then contains `X` — whom `w` beats. So `w` wins seat 1 instead. If `w` stays out of the pair, seat 1 is untouched, the seat-2 field is unchanged, and single-winner monotonicity keeps `w` seated. Either way `w` holds a seat.

**To do:** extend the induction past 2 seats or find the counterexample there; state the tie caveat (any lot-decided rung breaks monotonicity trivially, as it does single-winner); then either a `02_STAR_Bloc/03_Criteria/monotonicity/` set showing it *holding* seat by seat, or the counterexample if the induction fails.

### 3.2 Reinforcement / multiple districts

Bloc STAR is summable ([honest limits](../02_STAR_Bloc/01_Learn/bloc_honest_limits.md) leans on this), but summable ≠ consistent: the [reinforcement set](../method_comparisons/reinforcement_paradox/README.md) already shows STAR electing one winner in each half and a different one in the whole. The Bloc question is sharper and unasked — *two districts that each elect {X, Y}, combined electing neither*. Reuse the existing district ballots; search for a 2-seat version.

### 3.3 Clones and teaming

[Honest limits §4](../02_STAR_Bloc/01_Learn/bloc_honest_limits.md) claims Bloc STAR "rewards slate discipline" and has no runnable case behind it. The mechanical version: run a near-clone of a strong candidate and take a second seat with it — the removal step guarantees the clone inherits the field. Compare against SNTV on the same ballots, where the *opposite* error (running one candidate too many) loses everything. That contrast is the whole argument of [the at-large family page](../02_STAR_Bloc/01_Learn/bloc_star_vs_other_bloc_methods.md), and it is currently prose.

### 3.4 Strategy: the min-max bloc, seat by seat

Same page, same problem — the claim that "the margin recurs N times" needs an honest-vs-strategic pair: one electorate, sincere ballots, then a faction min-maxing (its slate 5, everything else 0), showing the seat it gains and what it costs the faction if the gamble fails. Level 301, and it wants the [Gibbard](../07_Concepts/topics/gibbard_satterthwaite_theorem.md) framing so it doesn't read as an attack on STAR specifically.

### 3.5 The silent ballot and the per-seat denominator

Once your candidate is seated, your ballot may express *no* preference between the survivors — you land in Equal Support for every later runoff, and each seat's runoff percentage has a different denominator. Visible already in 2.1's profile: seat 1 runs 2 of 6 voters with a preference, seat 2 runs 5 of 6. This is not ballot exhaustion (your scores still count in every scoring round), and the difference is worth teaching precisely rather than by analogy to IRV. Connects to the denominator question in the BV work ([#1471](https://github.com/Equal-Vote/bettervoting/issues/1471)) and to [runoff percentages](../01_STAR/01_Learn/the_count/runoff_percentages.md). Cheap: one case, `show_runoff_percent: true`, an explicit per-seat table.

### 3.6 Proportionality axioms — showing the failure formally

The folder says Bloc STAR is not proportional and shows a sweep. The modern statement is that it fails **justified representation** (JR), and a JR violation is checkable by hand on a tiny profile: a cohesive group of `n/k` voters gets nothing. Worth one 301 case in the STAR-PR direction, since it is the axiom that adjudicates Bloc vs [STAR-PR](../03_STAR_PR/README.md) rather than an anecdote about a sweep. Needs a glossary entry first — "justified representation" appears nowhere in `GLOSSARY.md`.

### 3.7 One electorate, every at-large count

[Food-Truck Row](../method_comparisons/food_truck_row/README.md) does five counts; the at-large *family* page names six methods (SNTV, Limited, Block Plurality, Bloc Approval, Bloc STAR, Bloc RR) with no single profile running all of them. The engine now covers every one of those (Bloc RR and SNTV included). A `method_comparisons/at_large_family/` set would retire a lot of prose.

### 3.8 Real elections

`04_Real_Elections/` exists for 01_STAR and not for Bloc. Are there Bloc STAR races with published ballots — org boards, party committees, BV-hosted elections whose results are public? If yes, one workup is worth more than three constructed cases. If no, record that as the answer so it stops being re-asked.

### 3.9 BetterVoting leftovers

- **BV126 "ties every step"** is still *pending* in the folder's case table — the only row with no case behind it.
- **`tieBreakType: none` on lot-decided seats** (BV131, BV130-r2) is reported in two case write-ups but has never been filed upstream. Decide: file it or record why not.
- **Per-seat runoff denominators** in BV's multi-winner display — the #1471 question, asked once per seat.

---

## 4. The verified profiles (paste-ready)

**Superseded 2026-08-04** — all three are now real cases with real candidate names and frozen BV exports, under [`02_STAR_Bloc/03_Criteria/`](../02_STAR_Bloc/03_Criteria/README.md). What follows is the letter-named originals, kept because they are the record of what the search actually returned and are quicker to re-run than the case files.

Ballot headers are the first line of the `ballots:` block; no separate `candidates:` key. Options shown are the house multi-winner minimal block.

### 4.1 Participation failure (§2.1) — two files, before and after

```yaml
# before — 6 ballots, council {A, B}
num_winners: 2
voting_method: Bloc STAR
ballots: |-
  A,B,C,D
  3,5,1,3
  4,5,2,4
  4,0,1,4
  2,2,5,1
  3,1,1,1
  5,0,1,5
expected_winners: [A, B]
```

```yaml
# after — the joiner's honest ballot is the last row; council {A, D}
num_winners: 2
voting_method: Bloc STAR
ballots: |-
  A,B,C,D
  3,5,1,3
  4,5,2,4
  4,0,1,4
  2,2,5,1
  3,1,1,1
  5,0,1,5
  3,2,5,0
expected_winners: [A, D]
```

Counts: before — seat 1 scores A21 D18 B13 C11, runoff A 2 – D 0 (4 Equal Support); seat 2 scores D18 B13 C11, runoff B 3 – D 2. After — seat 1 scores A24 D18 C16 B15, runoff A 3 – D 0 (4 ES); seat 2 scores D18 C16 B15, runoff D 4 – C 2. Joiner's own valuation: {A,B} = 5, {A,D} = 3.

### 4.2 Condorcet winner seated second (§2.2)

```yaml
num_winners: 2
voting_method: Bloc STAR
ballots: |-
  A,B,C,D
  4,2,3,2
  1,5,5,5
  4,3,0,3
  5,4,0,3
  4,2,2,3
  1,1,4,3
  2,5,1,5
expected_winners: [D, A]
```

Seat 1: scores D24 B22 A21 C15 → runoff D 2 – B 1 (4 ES). Seat 2: B22 A21 C15 → runoff A 4 – B 2 (1 ES). Pairwise A>B 4–2, A>C 5–2, A>D 4–3. Set `show_condorcet: true` and `matrix_finalists_only: false` on this one — the full grid is the point.

### 4.3 Committee spoiler (§2.3) — two files, without and with D

```yaml
# without D — council {C, A}
num_winners: 2
voting_method: Bloc STAR
ballots: |-
  A,B,C
  5,3,3
  0,3,4
  1,0,1
  0,5,2
  4,2,4
  1,0,1
  0,3,2
expected_winners: [C, A]
```

```yaml
# with D, who wins nothing — council {C, B}
num_winners: 2
voting_method: Bloc STAR
ballots: |-
  A,B,C,D
  5,3,3,0
  0,3,4,2
  1,0,1,5
  0,5,2,1
  4,2,4,1
  1,0,1,5
  0,3,2,3
expected_winners: [C, B]
```

Without D — seat 1 C17 B16 A11, runoff C 4 – B 2; seat 2 B16 A11, runoff A 4 – B 3. With D — seat 1 C17 D17 B16 A11, runoff C 4 – D 3; seat 2 D17 B16 A11, runoff B 4 – D 2.

Names: these are placeholder letters. Rename to the folder's convention (Nadia/Omar/Priya-style or a themed slate) before promoting — letters are fine for a working note, not for a case page.

---

## 5. Structure and indexing chores

- ~~**`02_STAR_Bloc/03_Criteria/` does not exist.**~~ **Done 2026-08-04** — created with `participation/`, `seat_order/` and `committee_spoiler/`, each mirroring [01_STAR/03_Criteria](../01_STAR/03_Criteria/README.md) (README table with levels, `cases/` inside). §3.1–3.3 now have somewhere to land.
- **Tag the *existing* Bloc YAMLs with `paradoxes:`.** Partly done: the four new cases carry `no-show` / `spoiler-scc`, so the folder finally has rows in [PARADOX_index.md](../07_Concepts/YAML_test_case_index/PARADOX_index.md) (168 tagged cases now, up from 164). The older ones are still bare — BV1525 → `condorcet-loser`, BV1835 → check first (Ava is described there as the Condorcet *loser*, so `absolute-loser` may be the right tag, or both). Note the tag vocabulary is hyphenated (`condorcet-winner`, `spoiler-scc`, `no-show`), and BV2266 was left **untagged** on purpose: `condorcet-winner` means the Condorcet winner is *not elected*, and Anika is elected — just second.
- **Glossary gaps** for the terms these pages would bold: "justified representation" (absent), and check that "participation / no-show," "clone," and "reinforcement" have entries that say what they mean *for multi-winner* rather than only single-winner.
- **`01_Learn/` will need one new page**, not more sections bolted onto [honest limits](../02_STAR_Bloc/01_Learn/bloc_honest_limits.md) — that page is already at its useful length. Suggested: *"What Bloc STAR keeps and what it drops"* — monotonicity (§3.1, likely kept), participation (§2.1, dropped), IIA (§2.3, dropped), summability (kept) — with each claim linked to its case. The [`03_Criteria/` index](../02_STAR_Bloc/03_Criteria/README.md) sketches this list already; the prose page is still owed, and `01_Learn/README.md` does not yet link the new folder (the folder README does).

---

## 6. How the search was run

Scripts sat in the session scratchpad, not the repo; they are ~120 lines and cheap to rewrite, but keep the shape if you extend the hunt:

1. **Independent re-implementation** of Bloc STAR (score → top two → head-to-head runoff → remove → repeat) used only to *find* profiles. Nothing was believed from it — every hit was re-run through `starvote_larry_hastings.py`, and every number quoted above is the engine's.
2. **Strict mode.** A profile is discarded if *any* round in *either* branch needs a tiebreak rung. That is what makes the §2 findings lot-independent; it also removes ~50% of random profiles at 4 candidates / 7 voters, which is worth knowing before you read a "0 failures" result.
3. **Uniform random ballots, 0–5 independent per candidate.** Deliberately unrealistic — it explores corners real electorates don't — but it means a *null* result (§3.1) is weaker than it looks, since the mechanism that would break monotonicity needs correlated ballots. That is exactly why the targeted hunt was added; if you resume, bias generation toward slate structure rather than raising the trial count.
4. **Search sizes:** participation ~400k trials to first hits (hits are common — this is not a rare corner); seat-order and spoiler likewise common; monotonicity 8 configurations × 120k trials, plus the reversal-targeted hunt.

# file: todo-bloc-star-scenarios.md
