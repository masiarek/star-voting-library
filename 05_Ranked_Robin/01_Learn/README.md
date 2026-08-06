# Ranked Robin (RCV-RR) — concept pages

Everything explaining **Ranked Robin** — the same ranked ballot as RCV-IRV, counted a different way: run every candidate head-to-head against every other (a round-robin), and elect the one with the best win-loss record (Copeland). It's a **Condorcet / consensus** method — when a candidate beats everyone, they win; the interesting question is what happens when nobody does (a cycle).

New here? Start with **[Ranked Robin (the method)](ranked_robin.md)**.

## The method

- [**Why Ranked Robin**](why_ranked_robin.md) — the positive case: the friendly upgrade for ranked ballots (start here for the "why").
- [Ranked Robin](ranked_robin.md) — the pairwise round-robin and the win-count
- [A naming decoder](condorcet_naming_decoder.md) — round-robin / Copeland / Condorcet / Ranked Robin, which word means what
- [What should we call this method?](what_to_call_this_method.md) — the naming options weighed, pros and cons: the brand, the algorithm, the family, and what each choice costs
- [A blank is ranked *last*](rr_blank_means_last.md) — what a blank means, why rank *numbers* don't matter (it's not Borda), and the universal ballot wording
- [Condorcet methods — a reading list](../../07_Concepts/topics/condorcet/condorcet_reading_list.md) — the books and papers behind the decoder, each with its lean marked
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

Every claim on these pages has a runnable election behind it — one case folder per idea:

- [The worked intro](../02_Examples/README.md) — RR elects the consensus center 3–0 over the two poles that hold more first choices
- [Condorcet vs. Ranked Robin](../02_Examples/condorcet_vs_ranked_robin/README.md) — a clean Condorcet winner, a genuine rock/paper/scissors cycle, and a real 0-wins record
- [RR vs. IRV vs. plurality](../02_Examples/rr_vs_irv_plurality/README.md) — one ranked ballot set, three different winners (the Tennessee center squeeze)
- [The Copeland score — a draw is worth half a win](../02_Examples/copeland_score/README.md) — why "most head-to-head wins" is a shorthand, and the case where the ½-credit decides
- [Most matchups won ≠ Condorcet winner](../02_Examples/most_wins_vs_condorcet/README.md) — its mirror image: strictly the most wins, and still beaten head-to-head
- [Tiebreaks](../03_Criteria/rr_tiebreaks/README.md) — the Equal Support column and the full ladder down to lot
- [Burial](../03_Criteria/burial/README.md) — the signature wart, worked as a sincere/buried pair on both engines
- [STAR vs RR — 30 divergence samples](../02_Examples/star_vs_rr_divergence/README.md) — where the two methods part ways, each sample stating its own cause

## Reference

- Glossary: [Ranked Robin & the Condorcet family](glossary_ranked_robin.md)

*(Other tabulations of the same ranked ballot: [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md) (instant runoff), [STV](../../03_STAR_PR/01_Learn/README.md) (proportional). Condorcet efficiency topic hub: [topics/condorcet](../../07_Concepts/topics/condorcet/README.md). Up: the docs hub [`00_START_HERE`](../../07_Concepts/00_START_HERE.md).)*
