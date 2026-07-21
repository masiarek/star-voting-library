# STAR vs Ranked Robin — 30 divergence samples (auto-generated)

*30 small elections where **STAR and [Ranked Robin](../README.md) elect different winners**, deliberately spread across candidate-field size, electorate size, and structure — with **RCV-IRV, Approval and Plurality** on the same ballots. Every winner is the LH engine's (from each case's `_tabulated` mirror). **Each YAML's `scenario_description` states the exact cause of its divergence.** Empirical companion to the [STAR-vs-RR simulation](../../06_Other/simulations/README.md#star-vs-ranked-robin-divergence-simulation).*

## The spread (what varies)

- **Candidate field:** 5 × 3, 6 × 5, 9 × 7, 10 × 10 (few → large).
- **Electorate:** few (~15–30), medium (~45–150), and large (up to ~600) voters.
- **Structure:** 15 **grouped** (a few voter factions/blocs) vs 15 **ungrouped** (independent random ballots).
- **Flavor:** 21 **cycles** + 9 **dark horses** — dark horses are rarer and cluster at *higher candidate counts and grouped electorates* (a broadly-liked compromise only emerges when there's structure to compromise around).

## The two causes (also spelled out per file)

- **Cycle** — no Condorcet winner (rock-paper-scissors). RR resolves by Copeland/margin; STAR by score-runoff. A structural coin-flip electorate.
- **Dark horse** — a Condorcet winner exists but **misses STAR's score top-two**: a broadly-preferred, low-intensity compromise. The [preference-vs-support](../../00_start_here/scores_and_ranks/preference_vs_support.md) split; a real [RR limit](../../00_start_here/RCV_Ranked_Robin/RCV_RR_honest_limits.md).

## Who sides with whom

On these 30 STAR≠RR elections, the other three methods **scatter** — there is *no* clean alignment:

| method | agrees w/ STAR | agrees w/ RR | picks a **third** candidate |
|---|:--:|:--:|:--:|
| **Approval** | 12 | 8 | **10** |
| **RCV-IRV** | 12 | 8 | **10** |
| **Plurality** | 13 | 8 | **9** |

The honest read: all three lean *mildly* toward STAR's winner over RR's, but the striking fact is that **about a third of the time each of them elects a candidate that is *neither* STAR's nor RR's winner** — the field fragments, especially with more candidates. (In a *narrower* 3–5-candidate sample the split looks cleaner — Approval→STAR, IRV/Plurality→RR, matching the support-vs-order intuition — but that alignment **washes out** once large fields are included. So the robust claim is only the modest one: STAR and RR genuinely disagree here, and the other methods don't reliably break the tie for either side.)

## The table

| flavor | cands | voters | electorate | STAR | RR | IRV | Appr | Plur | file |
|---|:--:|:--:|---|:--:|:--:|:--:|:--:|:--:|---|
| cycle | 3 | 15 | random | **A** | **B** | A | A | A | [`cycle_C03_fewV15_noise_1`](star_vs_rr_divergence_pages/cycle_C03_fewV15_noise_1.md) |
| cycle | 3 | 15 | random | **A** | **C** | A | A | A | [`cycle_C03_fewV15_noise_2`](star_vs_rr_divergence_pages/cycle_C03_fewV15_noise_2.md) |
| cycle | 3 | 45 | random | **A** | **B** | A | B | A | [`cycle_C03_medV45_noise_1`](star_vs_rr_divergence_pages/cycle_C03_medV45_noise_1.md) |
| cycle | 3 | 45 | random | **B** | **C** | A | C | A | [`cycle_C03_medV45_noise_2`](star_vs_rr_divergence_pages/cycle_C03_medV45_noise_2.md) |
| cycle | 5 | 15 | random | **B** | **E** | A | E | B | [`cycle_C05_fewV15_noise_1`](star_vs_rr_divergence_pages/cycle_C05_fewV15_noise_1.md) |
| cycle | 5 | 15 | random | **A** | **E** | A | D | A | [`cycle_C05_fewV15_noise_2`](star_vs_rr_divergence_pages/cycle_C05_fewV15_noise_2.md) |
| cycle | 5 | 28 | grouped | **A** | **C** | A | A | A | [`cycle_C05_fewV28_bloc_1`](star_vs_rr_divergence_pages/cycle_C05_fewV28_bloc_1.md) |
| cycle | 5 | 45 | random | **A** | **B** | A | E | A | [`cycle_C05_medV45_noise_1`](star_vs_rr_divergence_pages/cycle_C05_medV45_noise_1.md) |
| cycle | 5 | 45 | random | **D** | **B** | B | B | A | [`cycle_C05_medV45_noise_2`](star_vs_rr_divergence_pages/cycle_C05_medV45_noise_2.md) |
| cycle | 7 | 15 | random | **D** | **A** | A | A | A | [`cycle_C07_fewV15_noise_1`](star_vs_rr_divergence_pages/cycle_C07_fewV15_noise_1.md) |
| cycle | 7 | 28 | grouped | **D** | **A** | D | A | D | [`cycle_C07_fewV28_bloc_2`](star_vs_rr_divergence_pages/cycle_C07_fewV28_bloc_2.md) |
| cycle | 7 | 149 | grouped | **F** | **C** | F | C | A | [`cycle_C07_medV149_bloc_2`](star_vs_rr_divergence_pages/cycle_C07_medV149_bloc_2.md) |
| cycle | 7 | 598 | grouped | **C** | **E** | F | A | A | [`cycle_C07_largeV598_bloc_1`](star_vs_rr_divergence_pages/cycle_C07_largeV598_bloc_1.md) |
| cycle | 10 | 15 | random | **A** | **C** | H | A | A | [`cycle_C10_fewV15_noise_1`](star_vs_rr_divergence_pages/cycle_C10_fewV15_noise_1.md) |
| cycle | 10 | 15 | random | **J** | **F** | B | F | G | [`cycle_C10_fewV15_noise_2`](star_vs_rr_divergence_pages/cycle_C10_fewV15_noise_2.md) |
| cycle | 10 | 28 | grouped | **C** | **F** | C | C | C | [`cycle_C10_fewV28_bloc_1`](star_vs_rr_divergence_pages/cycle_C10_fewV28_bloc_1.md) |
| cycle | 10 | 29 | grouped | **C** | **B** | B | A | B | [`cycle_C10_fewV29_bloc_2`](star_vs_rr_divergence_pages/cycle_C10_fewV29_bloc_2.md) |
| cycle | 10 | 45 | random | **E** | **G** | A | C | A | [`cycle_C10_medV45_noise_1`](star_vs_rr_divergence_pages/cycle_C10_medV45_noise_1.md) |
| cycle | 10 | 45 | random | **A** | **I** | A | A | A | [`cycle_C10_medV45_noise_2`](star_vs_rr_divergence_pages/cycle_C10_medV45_noise_2.md) |
| cycle | 10 | 148 | grouped | **E** | **G** | J | B | J | [`cycle_C10_medV148_bloc_1`](star_vs_rr_divergence_pages/cycle_C10_medV148_bloc_1.md) |
| cycle | 10 | 149 | grouped | **I** | **H** | A | A | C | [`cycle_C10_medV149_bloc_2`](star_vs_rr_divergence_pages/cycle_C10_medV149_bloc_2.md) |
| dark horse | 3 | 15 | random | **A** | **C** | A | A | A | [`darkhorse_C03_fewV15_noise_1`](star_vs_rr_divergence_pages/darkhorse_C03_fewV15_noise_1.md) |
| dark horse | 5 | 599 | grouped | **A** | **E** | A | A | A | [`darkhorse_C05_largeV599_bloc_1`](star_vs_rr_divergence_pages/darkhorse_C05_largeV599_bloc_1.md) |
| dark horse | 7 | 30 | grouped | **D** | **C** | C | D | C | [`darkhorse_C07_fewV30_bloc_1`](star_vs_rr_divergence_pages/darkhorse_C07_fewV30_bloc_1.md) |
| dark horse | 7 | 45 | random | **E** | **A** | A | E | A | [`darkhorse_C07_medV45_noise_1`](star_vs_rr_divergence_pages/darkhorse_C07_medV45_noise_1.md) |
| dark horse | 7 | 147 | grouped | **F** | **D** | D | F | D | [`darkhorse_C07_medV147_bloc_1`](star_vs_rr_divergence_pages/darkhorse_C07_medV147_bloc_1.md) |
| dark horse | 7 | 597 | grouped | **D** | **E** | B | C | B | [`darkhorse_C07_largeV597_bloc_1`](star_vs_rr_divergence_pages/darkhorse_C07_largeV597_bloc_1.md) |
| dark horse | 7 | 598 | grouped | **E** | **G** | G | A | G | [`darkhorse_C07_largeV598_bloc_2`](star_vs_rr_divergence_pages/darkhorse_C07_largeV598_bloc_2.md) |
| dark horse | 10 | 598 | grouped | **G** | **F** | F | D | F | [`darkhorse_C10_largeV598_bloc_1`](star_vs_rr_divergence_pages/darkhorse_C10_largeV598_bloc_1.md) |
| dark horse | 10 | 599 | grouped | **B** | **E** | C | B | E | [`darkhorse_C10_largeV599_bloc_2`](star_vs_rr_divergence_pages/darkhorse_C10_largeV599_bloc_2.md) |

## Caveats (read before quoting)

- **Auto-generated stress tests, not real elections** — they show the *mechanism*; for a *rate*, use the [simulation](../../06_Other/simulations/README.md#star-vs-ranked-robin-divergence-simulation).
- **The IRV column is noisy.** On small/tied score ballots the rank IRV reads is often decided by candidate-priority tie-breaking (the engine flags it per case). STAR, RR and Approval read scores/pairwise directly and are robust.
- RR = Copeland (LH's margin-then-lot tiebreak); STAR/RR winners are the engine's. Sincere normalized 0–5 scores.
- Each case is a normal STAR YAML — re-run it with the LH engine to see the full `[Divergence from STAR]` block, the pairwise matrix, and the IRV rounds.
