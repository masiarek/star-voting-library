# STAR vs Ranked Robin — 30 divergence samples (auto-generated)

*A dump of **30 small elections where STAR and [Ranked Robin](../README.md) elect different winners**, with the same ballots run through **RCV-IRV, Approval and Plurality** so you can see who sides with whom. The empirical companion to the [STAR-vs-RR divergence simulation](../../06_Other/simulations/README.md#star-vs-ranked-robin-divergence-simulation); every winner here is the **LH engine's**, read from each case's `_tabulated` mirror (`[Divergence from STAR]` block).*

## The two flavors (why STAR ≠ RR)

A Condorcet winner who reaches STAR's runoff wins it, so STAR ≠ RR needs one of two things — and this dump has **15 of each**:
- **Cycle** — no Condorcet winner exists; RR (Copeland) and STAR resolve the unresolvable differently.
- **Dark horse** — a Condorcet winner exists but **misses STAR's score top-two** (a broadly-preferred, low-intensity compromise). The [preference-vs-support](../../00_start_here/scores_and_ranks/preference_vs_support.md) split; a real [RR limit](../../00_start_here/RCV_Ranked_Robin/RCV_RR_honest_limits.md).

## Who sides with whom (the interesting part)

On these 30 STAR≠RR elections, the other methods split along the **support-vs-order axis**:

| method | sides with… |
|---|---|
| **Approval** | STAR **15** · RR **6** · neither 9 — the *score* family leans **STAR** |
| **RCV-IRV** | STAR **9** · RR **16** · neither 5 — the *order* family leans **Ranked Robin** |
| **Plurality** | STAR **7** · RR **15** · neither 8 — also leans **RR** here |

**Approval (a score ballot) tracks STAR; IRV and Plurality (which read only order/first-choices) track Ranked Robin.** The STAR-vs-RR fault line *is* the support-vs-order fault line, and the other methods fall on the side that matches how they read the ballot.

## The table

| file | flavor | STAR | RR | IRV | Approval | Plurality |
|---|---|:--:|:--:|:--:|:--:|:--:|
| [`darkhorse_01_c5_v21`](star_vs_rr_divergence_pages/darkhorse_01_c5_v21.md) | dark horse (CW≠STAR) | **A** | **B** | B | A | A |
| [`darkhorse_02_c4_v15`](star_vs_rr_divergence_pages/darkhorse_02_c4_v15.md) | dark horse (CW≠STAR) | **A** | **C** | C | D | C |
| [`darkhorse_03_c5_v15`](star_vs_rr_divergence_pages/darkhorse_03_c5_v15.md) | dark horse (CW≠STAR) | **E** | **C** | C | E | C |
| [`darkhorse_04_c4_v21`](star_vs_rr_divergence_pages/darkhorse_04_c4_v21.md) | dark horse (CW≠STAR) | **D** | **A** | A | B | A |
| [`darkhorse_05_c5_v21`](star_vs_rr_divergence_pages/darkhorse_05_c5_v21.md) | dark horse (CW≠STAR) | **E** | **B** | B | E | B |
| [`darkhorse_06_c4_v15`](star_vs_rr_divergence_pages/darkhorse_06_c4_v15.md) | dark horse (CW≠STAR) | **D** | **B** | B | D | B |
| [`darkhorse_08_c5_v21`](star_vs_rr_divergence_pages/darkhorse_08_c5_v21.md) | dark horse (CW≠STAR) | **C** | **D** | D | C | D |
| [`darkhorse_10_c5_v21`](star_vs_rr_divergence_pages/darkhorse_10_c5_v21.md) | dark horse (CW≠STAR) | **D** | **E** | C | D | D |
| [`darkhorse_11_c5_v21`](star_vs_rr_divergence_pages/darkhorse_11_c5_v21.md) | dark horse (CW≠STAR) | **D** | **E** | A | C | A |
| [`darkhorse_12_c5_v21`](star_vs_rr_divergence_pages/darkhorse_12_c5_v21.md) | dark horse (CW≠STAR) | **B** | **C** | B | B | C |
| [`darkhorse_15_c5_v21`](star_vs_rr_divergence_pages/darkhorse_15_c5_v21.md) | dark horse (CW≠STAR) | **B** | **A** | A | E | A |
| [`darkhorse_16_c4_v15`](star_vs_rr_divergence_pages/darkhorse_16_c4_v15.md) | dark horse (CW≠STAR) | **C** | **D** | D | B | D |
| [`darkhorse_18_c4_v21`](star_vs_rr_divergence_pages/darkhorse_18_c4_v21.md) | dark horse (CW≠STAR) | **D** | **A** | D | A | D |
| [`darkhorse_19_c4_v15`](star_vs_rr_divergence_pages/darkhorse_19_c4_v15.md) | dark horse (CW≠STAR) | **C** | **D** | D | B | B |
| [`darkhorse_20_c5_v15`](star_vs_rr_divergence_pages/darkhorse_20_c5_v15.md) | dark horse (CW≠STAR) | **B** | **C** | B | B | B |
| [`cycle_01_c5_v21`](star_vs_rr_divergence_pages/cycle_01_c5_v21.md) | cycle (no CW) | **D** | **C** | B | D | B |
| [`cycle_02_c5_v15`](star_vs_rr_divergence_pages/cycle_02_c5_v15.md) | cycle (no CW) | **D** | **C** | C | C | C |
| [`cycle_03_c5_v21`](star_vs_rr_divergence_pages/cycle_03_c5_v21.md) | cycle (no CW) | **E** | **A** | A | D | D |
| [`cycle_04_c5_v21`](star_vs_rr_divergence_pages/cycle_04_c5_v21.md) | cycle (no CW) | **E** | **A** | A | E | A |
| [`cycle_05_c5_v15`](star_vs_rr_divergence_pages/cycle_05_c5_v15.md) | cycle (no CW) | **B** | **D** | A | D | B |
| [`cycle_06_c4_v21`](star_vs_rr_divergence_pages/cycle_06_c4_v21.md) | cycle (no CW) | **C** | **D** | C | C | D |
| [`cycle_07_c4_v21`](star_vs_rr_divergence_pages/cycle_07_c4_v21.md) | cycle (no CW) | **C** | **B** | A | B | A |
| [`cycle_09_c3_v21`](star_vs_rr_divergence_pages/cycle_09_c3_v21.md) | cycle (no CW) | **A** | **B** | B | C | B |
| [`cycle_10_c4_v15`](star_vs_rr_divergence_pages/cycle_10_c4_v15.md) | cycle (no CW) | **C** | **A** | C | A | A |
| [`cycle_11_c4_v21`](star_vs_rr_divergence_pages/cycle_11_c4_v21.md) | cycle (no CW) | **D** | **A** | D | A | B |
| [`cycle_12_c3_v15`](star_vs_rr_divergence_pages/cycle_12_c3_v15.md) | cycle (no CW) | **B** | **C** | C | B | A |
| [`cycle_13_c5_v21`](star_vs_rr_divergence_pages/cycle_13_c5_v21.md) | cycle (no CW) | **E** | **A** | A | B | A |
| [`cycle_14_c3_v21`](star_vs_rr_divergence_pages/cycle_14_c3_v21.md) | cycle (no CW) | **A** | **B** | A | A | A |
| [`cycle_15_c5_v21`](star_vs_rr_divergence_pages/cycle_15_c5_v21.md) | cycle (no CW) | **C** | **D** | C | C | B |
| [`cycle_16_c3_v15`](star_vs_rr_divergence_pages/cycle_16_c3_v15.md) | cycle (no CW) | **A** | **C** | A | A | A |

## Caveats (read before quoting)

- **Auto-generated, tiny electorates** (15–21 voters, 3–5 candidates, sincere normalized 0–5 scores) — a stress test, not real elections. They exist to *show the mechanism*, not to estimate a rate (that's the [simulation](../../06_Other/simulations/README.md#star-vs-ranked-robin-divergence-simulation)).
- **The IRV column is noisy.** With so few voters and a 0–5 scale, many ballots have **equal scores**, so the rank IRV reads is often decided by candidate-priority tie-breaking — the engine flags this per case (`Note: … equal non-zero scores … may be an artifact`). STAR, RR and Approval read the scores/pairwise directly and are robust; treat IRV here as indicative.
- RR = Copeland (LH's margin-then-lot tiebreak); STAR and RR winners are the engine's.

## Reproduce / regenerate

The generator and the winner-parser are ad-hoc (scratch) scripts; the *reproducible* study is [`06_Other/simulations/star_vs_rr_divergence.py`](../../06_Other/simulations/star_vs_rr_divergence.py). Each case here is a normal STAR YAML — re-run any with the LH engine to see the full `[Divergence from STAR]` block, the pairwise matrix, and the IRV rounds.
