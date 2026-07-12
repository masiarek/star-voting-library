# silly_two_cand_STAR — deliberately-trivial two-candidate cases (parked)

These are **two-candidate** STAR elections. They live here, off the learning path, on purpose.

## Why they're parked

With only **two candidates**, STAR has nothing distinctive to show a newcomer:

- Both candidates are *always* the two finalists (there's no one else to leave out), so the **Scoring Round never has to choose** — the interesting half of STAR is a no-op.
- The **Automatic Runoff** just asks "which of the two did you score higher?" — which is exactly what an ordinary one-mark ballot already asks. So STAR agrees with plain majority voting here by construction.

In other words, a two-candidate STAR example teaches the *mechanics of the count* but hides the whole reason STAR exists: reading a **full ballot across three or more candidates** so the broad compromise can surface and vote-splitting can't bury it. Leading a first-time learner with one of these is actively misleading — it makes STAR look like a fancy way to do something they already know.

That's why the [`STAR — start here`](../../00_start_here/STAR_Voting/STAR_start_here.md) page and the [`_main` progression](../_main/) now open on the **three-candidate team-lunch example** instead.

## Why they're kept

- **Engine test fixtures.** They're small, exact, and still run in the single-winner STAR test suite (they sit under `01_STAR/`, so they're discovered automatically) — useful for pinning down runoff-denominator and Equal-Support edge behavior at the smallest possible scale.
- **Completeness.** One of them (`01a_c2_b2`) is a real, live BetterVoting election; the set documents the "smallest possible STAR election," "add a second ballot," "a 5-and-0 ballot," and "Equal Support" at N = 2.

## The files

| Page | What it isolates |
|---|---|
| [`01a_c2_b1_two-candidates`](silly_two_cand_STAR_pages/01a_c2_b1_two-candidates.md) | The smallest possible STAR election — one voter, two flavors. |
| [`01a_c2_b2_two-candidates`](silly_two_cand_STAR_pages/01a_c2_b2_two-candidates.md) | The same, with a second ballot. *(Live on BetterVoting: [`my82v6`](https://bettervoting.com/my82v6/results).)* |
| [`01b_c2_b2_two-candidates`](silly_two_cand_STAR_pages/01b_c2_b2_two-candidates.md) | A 5-and-0 ballot added. |
| [`01c_c2_b3_two-candidates`](silly_two_cand_STAR_pages/01c_c2_b3_two-candidates.md) | Equal Support ("I like both flavors") at its smallest. |

Equal Support and the runoff denominator are taught *properly* — with a real field of candidates — back in [`_main`](../_main/) ([`equal_support_runoff_demo`](../_main/_main_pages/equal_support_runoff_demo.md)) and the [pet election](../pet_real_bv_election/).

---

Up: [01_STAR — single-winner STAR Voting](../) · Concept docs: [STAR — start here](../../00_start_here/STAR_Voting/STAR_start_here.md)
