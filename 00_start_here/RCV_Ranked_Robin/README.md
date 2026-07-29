# Ranked Robin (RCV-RR) — concept pages

Everything explaining **Ranked Robin** — the same ranked ballot as RCV-IRV, counted a different way: run every candidate head-to-head against every other (a round-robin), and elect the one with the best win-loss record (Copeland). It's a **Condorcet / consensus** method — when a candidate beats everyone, they win; the interesting question is what happens when nobody does (a cycle).

New here? Start with **[Ranked Robin (the method)](ranked_robin.md)**.

## The method

- [**Why Ranked Robin**](why_ranked_robin.md) — the positive case: the friendly upgrade for ranked ballots (start here for the "why").
- [Ranked Robin (aka Consensus Voting)](ranked_robin.md) — the pairwise round-robin and the win-count
- [A naming decoder](condorcet_naming_decoder.md) — round-robin / Copeland / Condorcet / Ranked Robin, which word means what
- [A blank is ranked *last*](rr_blank_means_last.md) — what a blank means, why rank *numbers* don't matter (it's not Borda), and the universal ballot wording
- [Condorcet methods — a reading list](../topics/condorcet/condorcet_reading_list.md) — the books and papers behind the decoder, each with its lean marked
- [Ranked Robin vs. Consensus Choice](ranked_robin_vs_consensus_choice.md) — the sibling brand: same count, different cycle rule, different proposal scope
- [Summability](RCV_RR_summability.md) — the pairwise matrix adds (unlike IRV)
- [Clone independence](rr_clone_independence.md) — crowding, teaming, and the tiebreak that matters
- [Tiebreaks — LH vs. BetterVoting](rr_tiebreak_lh_vs_bv.md) — a documented engine divergence
- [Honest limits](RCV_RR_honest_limits.md)

## Condorcet & cycles

- [Ranked Robin vs. "the Condorcet winner"](ranked_robin_vs_condorcet.md) — same animal, until there's a cycle
- [Cycle resolution](cycle_resolution.md) — why Minimax, Ranked Pairs, and Schulze exist
- [The math behind Condorcet](the_math_behind_condorcet.md) — tournaments, the Smith set, and cycles

## Worked examples — run them yourself

Every claim on these pages has a runnable election behind it. The case folders live in **[`05_Ranked_Robin/`](../../05_Ranked_Robin/)**:

- [The worked intro](../../05_Ranked_Robin/_main/) — RR elects the consensus center 3–0 over the two poles that hold more first choices
- [Condorcet vs. Ranked Robin](../../05_Ranked_Robin/condorcet_vs_ranked_robin/) — a clean Condorcet winner, a genuine rock/paper/scissors cycle, and a real 0-wins record
- [RR vs. IRV vs. plurality](../../05_Ranked_Robin/rr_vs_irv_plurality/) — one ranked ballot set, three different winners (the Tennessee center squeeze)
- [The Copeland score — a draw is worth half a win](../../05_Ranked_Robin/copeland_score/) — why "most head-to-head wins" is a shorthand, and the case where the ½-credit decides
- [Most matchups won ≠ Condorcet winner](../../05_Ranked_Robin/most_wins_vs_condorcet/) — its mirror image: strictly the most wins, and still beaten head-to-head
- [Tiebreaks](../../05_Ranked_Robin/rr_tiebreaks/) — the Equal Support column and the full ladder down to lot
- [Burial](../../05_Ranked_Robin/burial/) — the signature wart, worked as a sincere/buried pair on both engines
- [STAR vs RR — 30 divergence samples](../../05_Ranked_Robin/star_vs_rr_divergence/) — where the two methods part ways, each sample stating its own cause

## Reference

- Glossary: [Ranked Robin & the Condorcet family](glossary_ranked_robin.md)

*(Other tabulations of the same ranked ballot: [RCV-IRV](../RCV_IRV/README.md) (instant runoff), [STV](../proportional_representation/) (proportional). Condorcet efficiency topic hub: [topics/condorcet](../topics/condorcet/README.md). Up: the docs hub [`00_START_HERE`](../00_START_HERE.md).)*
