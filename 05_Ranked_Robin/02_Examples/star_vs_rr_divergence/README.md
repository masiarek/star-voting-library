# STAR vs Ranked Robin — 24 divergence samples (auto-generated)

*24 small elections where **STAR and [Ranked Robin](../../README.md) elect different winners**, deliberately spread across candidate-field size, electorate size, and structure — with **RCV-IRV, Approval and Plurality** on the same ballots. Every winner is the LH engine's (from each case's `_tabulated` mirror). **Each YAML's `scenario_description` states the exact cause of its divergence.** Empirical companion to the [STAR-vs-RR simulation](../../../06_Other/simulations/README.md#star-vs-ranked-robin-divergence-simulation).*

> **Regenerating this folder?** Take the winners from the **engine** — `star_winner_engine()` in the simulation, or each case's `_tabulated` mirror. The simulation's fast numpy model (`star_winner()`) now implements the engine's tie-breaks and is test-checked against it, but the engine is right by construction and cannot drift; an earlier version of that model did drift, and mislabelled one of the original 30 at birth. Then verify with:
>
> ```bash
> python STARVote_LH_tabulation_engine/tools_adam/scripts/check_star_vs_rr_labels.py
> python STARVote_LH_tabulation_engine/tools_adam/scripts/check_star_vs_rr_causes.py
> ```
>
> The first checks all five places a sample names a **winner** — `expected_winners`, the title, the description, the `_tabulated` mirror and the table below — against a real tabulation (`--fix` relabels the yamls). The second checks what the descriptions claim about **why** the methods diverge: that each cycle chain (`A>I>G>A`) is a real chain of pairwise wins that closes, that a cycle sample really has no Condorcet winner, and that a dark horse really is the Condorcet winner with the score rank, totals and missed finalists it claims. A sample can name both winners correctly and still assert a link that does not exist, so the two are complementary — winners vs. causes. [`tests/test_star_vs_rr_labels.py`](../../../STARVote_LH_tabulation_engine/tests/test_star_vs_rr_labels.py) and [`tests/test_star_vs_rr_causes.py`](../../../STARVote_LH_tabulation_engine/tests/test_star_vs_rr_causes.py) run them on every commit.

> **Why 24, not 30?** Twice now, correcting the engine's Copeland tiebreak has dissolved some of these divergences — which is worth knowing about the set: a sample here demonstrates a disagreement between two *implementations* as much as between two methods, and the implementation can turn out to be wrong.
>
> The set was minted as 30, labelled by a helper that ranked Copeland by RAW wins. When `copeland_winner()` was corrected to the real Copeland tally (a draw = ½ to each side — the key the RR report itself sorts by), four samples (`cycle_C03_medV45_noise_2`, `cycle_C05_fewV15_noise_1`, `cycle_C07_fewV28_bloc_2`, `cycle_C10_medV148_bloc_1`) turned out to elect the SAME winner under STAR and RR, so they were retired (2026-08-09). A fifth, `cycle_C05_fewV28_bloc_1`, stayed but was relabelled (RR elects E, not C).
>
> On **2026-08-19** the engine gained the tiebreak rung it had been missing — Ranked Robin's [1st Degree](../../03_Criteria/rr_tiebreaks/degrees_of_ties.md), margins among the tied finalists, which outranks the total-margin rung the engine had been using — and two more samples stopped diverging: `cycle_C07_largeV598_bloc_1` (RR now elects C, with STAR) and `cycle_C07_medV149_bloc_2` (RR now elects F, with STAR). Retired on the same terms; all their page URLs redirect here.

## The spread (what varies)

- **Candidate field:** 4 × 3, 5 × 5, 6 × 7, 9 × 10 (few → large).
- **Electorate:** few (~15–30) and medium (~45–150) voters. The one large-electorate sample (598 voters) was among those retired on 2026-08-19, so the set no longer reaches that size.
- **Structure:** 11 **grouped** (a few voter factions/blocs) vs 13 **ungrouped** (independent random ballots).
- **Flavor:** 15 **cycles** + 9 **dark horses** — dark horses are rarer and cluster at *higher candidate counts and grouped electorates* (a broadly-liked compromise only emerges when there's structure to compromise around).

## The two causes (also spelled out per file)

- **Cycle** — no Condorcet winner (rock-paper-scissors). RR resolves by Copeland/margin; STAR by score-runoff. A structural coin-flip electorate.
- **Dark horse** — a Condorcet winner exists but **misses STAR's score top-two**: a broadly-preferred, low-intensity compromise. The [preference-vs-support](../../../07_Concepts/scores_and_ranks/preference_vs_support.md) split; a real [RR limit](../../01_Learn/RCV_RR_honest_limits.md).

## Who sides with whom

On these 24 STAR≠RR elections, the other three methods **scatter** — there is *no* clean alignment:

| method | agrees w/ STAR | agrees w/ RR | picks a **third** candidate |
|---|:--:|:--:|:--:|
| **Approval** | 12 | 4 | **8** |
| **RCV-IRV** | 10 | 8 | **6** |
| **Plurality** | 11 | 8 | **5** |

The honest read: all three lean *mildly* toward STAR's winner over RR's, but the striking fact is that **a quarter to a third of the time each of them elects a candidate that is *neither* STAR's nor RR's winner** — the field fragments, especially with more candidates. (In a *narrower* 3–5-candidate sample the split looks cleaner — Approval→STAR, IRV/Plurality→RR, matching the support-vs-order intuition — but that alignment **washes out** once large fields are included. So the robust claim is only the modest one: STAR and RR genuinely disagree here, and the other methods don't reliably break the tie for either side.)

## The table

| flavor | cands | voters | electorate | STAR | RR | IRV | Appr | Plur | file |
|---|:--:|:--:|---|:--:|:--:|:--:|:--:|:--:|---|
| cycle | 3 | 15 | random | **A** | **B** | A | A | A | [`cycle_C03_fewV15_noise_1`](star_vs_rr_divergence_pages/cycle_C03_fewV15_noise_1.md) |
| cycle | 3 | 15 | random | **A** | **C** | A | A | A | [`cycle_C03_fewV15_noise_2`](star_vs_rr_divergence_pages/cycle_C03_fewV15_noise_2.md) |
| cycle | 3 | 45 | random | **A** | **B** | A | B | A | [`cycle_C03_medV45_noise_1`](star_vs_rr_divergence_pages/cycle_C03_medV45_noise_1.md) |
| cycle | 5 | 15 | random | **A** | **E** | A | D | A | [`cycle_C05_fewV15_noise_2`](star_vs_rr_divergence_pages/cycle_C05_fewV15_noise_2.md) |
| cycle | 5 | 28 | grouped | **A** | **E** | A | A | A | [`cycle_C05_fewV28_bloc_1`](star_vs_rr_divergence_pages/cycle_C05_fewV28_bloc_1.md) |
| cycle | 5 | 45 | random | **A** | **B** | A | E | A | [`cycle_C05_medV45_noise_1`](star_vs_rr_divergence_pages/cycle_C05_medV45_noise_1.md) |
| cycle | 5 | 45 | random | **D** | **B** | B | B | A | [`cycle_C05_medV45_noise_2`](star_vs_rr_divergence_pages/cycle_C05_medV45_noise_2.md) |
| cycle | 7 | 15 | random | **D** | **A** | A | A | A | [`cycle_C07_fewV15_noise_1`](star_vs_rr_divergence_pages/cycle_C07_fewV15_noise_1.md) |
| cycle | 10 | 15 | random | **A** | **C** | H | A | A | [`cycle_C10_fewV15_noise_1`](star_vs_rr_divergence_pages/cycle_C10_fewV15_noise_1.md) |
| cycle | 10 | 15 | random | **J** | **F** | B | F | G | [`cycle_C10_fewV15_noise_2`](star_vs_rr_divergence_pages/cycle_C10_fewV15_noise_2.md) |
| cycle | 10 | 28 | grouped | **C** | **F** | C | C | C | [`cycle_C10_fewV28_bloc_1`](star_vs_rr_divergence_pages/cycle_C10_fewV28_bloc_1.md) |
| cycle | 10 | 29 | grouped | **C** | **B** | B | A | B | [`cycle_C10_fewV29_bloc_2`](star_vs_rr_divergence_pages/cycle_C10_fewV29_bloc_2.md) |
| cycle | 10 | 45 | random | **E** | **G** | A | C | A | [`cycle_C10_medV45_noise_1`](star_vs_rr_divergence_pages/cycle_C10_medV45_noise_1.md) |
| cycle | 10 | 45 | random | **A** | **I** | A | A | A | [`cycle_C10_medV45_noise_2`](star_vs_rr_divergence_pages/cycle_C10_medV45_noise_2.md) |
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

- **Auto-generated stress tests, not real elections** — they show the *mechanism*; for a *rate*, use the [simulation](../../../06_Other/simulations/README.md#star-vs-ranked-robin-divergence-simulation).
- **The IRV column is noisy.** On small/tied score ballots the rank IRV reads is often decided by candidate-priority tie-breaking (the engine flags it per case). STAR, RR and Approval read scores/pairwise directly and are robust.
- RR = Copeland (LH's margin-then-lot tiebreak); STAR/RR winners are the engine's. Sincere normalized 0–5 scores.
- Each case is a normal STAR YAML — re-run it with the LH engine to see the full `[Divergence from STAR]` block, the pairwise matrix, and the IRV rounds.
