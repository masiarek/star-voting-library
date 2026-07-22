# How to Learn About Voting Methods — a reading path

Voting theory gets deep fast, and it's easy to get lost. This page is a **guided path**, from complete beginner to advanced, threaded through this library's own pages — so at every step you can not just *read* the idea but *run the election* behind it.

It follows the three-level structure of **Marcus Ogren's [How to Learn About Voting Methods](https://voting-in-the-abstract.medium.com/how-to-learn-about-voting-methods-4e6c0e4d38d9)**, used with his kind permission. Where Marcus surveys the *whole field* (and, transparently, leans toward Condorcet methods), this version walks the same three levels through *this repo's* worked examples. The two are complementary — read his for the field-wide view and a different preference ordering; read this for the runnable, example-first version.

> **Newcomer?** Read the levels in order. **Already know the basics?** Skip ahead. For the STAR-specific deep track, see the [101 / 201 / 301 Curriculum](../CURRICULUM.md).
>
> **Our transparency note** (in the spirit of Marcus stating his own bias): this is a *STAR-centered* library, so STAR gets the most coverage. But it works hard to be even-handed — every method here has an honest-limits page, and Level 3 sends you to the opposing viewpoints on purpose. Take the STAR emphasis as *where the examples are richest*, not as a verdict.

---

## Level 1 — Basics

Start here with zero background.

- **What a voting method even is** → [a ballot and a count](voting_method_ballot_and_count.md) — the one foundational split (the *ballot* vs. the *tabulation*), and why "most votes" isn't "over half."
- **The terminology people trip on** → [Ballot & Terminology Basics](ballot_and_terminology_basics.md) — RCV vs. IRV, scores vs. ranks, what even counts as "ranked."
- **The problem being solved** → [Choose-One / Plurality](plurality.md) and [the spoiler effect](spoiler_effect.md).
- **Two kinds of ballot** → [scores vs. ranks](../scores_and_ranks/scores_vs_ranks.md) — the split that sorts every method below.
- **The single-winner methods**, one page each:
  - [Approval](../Approval_Voting/approval_voting.md) — mark the ones you like.
  - [STAR](../STAR_Voting/STAR_start_here.md) — score 0–5, then an automatic runoff.
  - [RCV-IRV (Hare)](../RCV_IRV/RCV-IRV-Hare.md) — rank, then eliminate-and-transfer.
  - [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) — rank, then compare every pair (a Condorcet method).
- **Multi-winner / proportional** → [proportional STAR](../proportional_representation/STAR_PR/README.md) and [STV](../proportional_representation/stv/proportional_stv_vs_star.md) — how representation (not just a single winner) is chosen.

---

## Level 2 — Analyzing and comparing methods

Now the tools for judging methods against each other. *(Prereq: Level 1.)*

- **Strategic voting** → [strategic voting across the Equal Vote methods](strategic_voting.md) — the four kinds of insincere vote, and when honesty pays.
- **The classic failure scenarios** → [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) and the chicken-dilemma / [residual vote-splitting](../STAR_Voting/properties_and_limits/residual_vote_splitting.md).
- **Simulations & VSE** → [Voter Satisfaction Efficiency and the favorite-betrayal simulation](../STAR_Voting/properties_and_limits/favorite_betrayal_voting_301.md), built on the repo's [Monte-Carlo scripts](../../06_Other/simulations/README.md).
- **Three notions of "winner"** → [Condorcet vs. score vs. runoff](../STAR_Voting/properties_and_limits/STAR_three_winner_notions.md) — why "best" is ambiguous.
- **The head-to-head comparisons** → [Choosing among the Equal Vote methods](choosing_among_evc_methods.md) (STAR / Approval / Ranked Robin, even-handed) and [RCV-IRV vs. STAR](rcv_irv_vs_star.md).
- **Where methods disagree, worked** → [method comparisons](../../method_comparisons/README.md) and the [paradoxes & whoops](../../method_comparisons/paradoxes_and_whoops/README.md) collection (read under its [reading-these-fairly](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) discipline).

---

## Level 3 — More perspectives

Empirical evidence, theory, more methods, and — deliberately — the arguments *against* the methods this repo emphasizes. *(Prereq: Levels 1–2.)*

- **Real-world evidence** → [the Alternative Vote in Australia](../RCV_IRV/case_studies/RCV_IRV_australia.md) (a century, assessed evenhandedly), [Alaska 2022](../RCV_IRV/case_studies/RCV_IRV_alaska_2022.md), and [North Carolina](../RCV_IRV/case_studies/RCV_IRV_north_carolina.md).
- **The party-system question** → [Two-Party Dominance — pros, cons, and what changes it](two_party_dominance.md), and why *proportional* (not single-winner) reform is the lever.
- **Impossibility theorems** → Arrow and Gibbard–Satterthwaite (defined in the [Glossary](../GLOSSARY.md)) — why *no* method is perfect, so every choice is a trade-off.
- **The method zoo** → beyond the headline four: [3-2-1 voting](../../06_Other/three_two_one/README.md), [Borda](../other_ranked_methods/borda.md), [agenda voting](../other_ranked_methods/agenda_voting.md), and the ranked-method family in the [Glossary](../GLOSSARY.md#other-methods-for-contrast) (Ranked Pairs, Schulze, Minimax…).
- **Opposing viewpoints (read these on purpose):**
  - Each method's honest limits — [STAR](../STAR_Voting/properties_and_limits/STAR_honest_limits.md), [Approval](../Approval_Voting/approval_honest_limits.md), [Ranked Robin](../RCV_Ranked_Robin/RCV_RR_honest_limits.md).
  - Claims we check both ways — [RCV-IRV claims, fact-checked](../RCV_IRV/rcv_irv_false_claims.md).
  - **Marcus's own guide** for a **Condorcet-preferring** perspective different from this library's STAR emphasis — [How to Learn About Voting Methods](https://voting-in-the-abstract.medium.com/how-to-learn-about-voting-methods-4e6c0e4d38d9).

---

## Further reading (beyond this repo)

- **Books** — the [annotated books shelf](../books/README.md): the popular introductions ([Poundstone](../books/popular_introductions.md), Szpiro, Saari) and the scholarly classics ([Arrow](../books/social_choice_theory.md), Sen, Balinski & Laraki), each with a cover and an honest "the lean."
- **Marcus Ogren** — [Voting in the Abstract](https://voting-in-the-abstract.medium.com/) (the model for this page; field-wide, Condorcet-leaning).
- **Academic & nonpartisan overviews** — the [Stanford Encyclopedia of Philosophy: Voting Methods](https://plato.stanford.edu/entries/voting-methods/) (the rigorous, neutral scholarly survey) and the [League of Women Voters of Washington — *Review of Election Methods*](https://www.lwvwa.org/resources/Documents/Review%20of%20Election%20Methods%202-12-20.pdf) (a nonpartisan side-by-side comparison, 2020).
- **Organizations** — the [Equal Vote Coalition](https://www.equal.vote), [STAR Voting](https://www.starvoting.org), the [Center for Election Science](https://electionscience.org), and [FairVote](https://fairvote.org) (the primary IRV advocate — read for the case this repo often argues *against*). Who's who among them: [voting-reform people](whos_who_voting_reform.md).
- **Simulations & data** — [Jameson Quinn](in_memoriam_jameson_quinn.md)'s [Voter Satisfaction Efficiency](https://electionscience.github.io/vse-sim/) (background: [social utility efficiency](https://en.wikipedia.org/wiki/Social_utility_efficiency)) · [PrefLib](https://www.preflib.org/) — a database of real ranked-preference elections.
- **Independent tabulation libraries** (used to cross-check this repo's engine) — [pref_voting](https://pref-voting.readthedocs.io/) and [abcvoting](https://abcvoting.readthedocs.io/).
- **Reference** — [electowiki](https://electowiki.org) for the method encyclopedia.
- **Finding the primary literature yourself** — voting research is split across three literatures that barely cite each other, and each is indexed differently:
  - **Economics / social choice** → search [RePEc-IDEAS](https://ideas.repec.org/), EconLit or [SSRN](https://www.ssrn.com/) by **JEL code**. The ones that matter: **D71** (social choice — the theory core), **D72** (political processes: *elections and voting behavior* — the most on-target single code), **D63** (equity/justice and other normative criteria — where welfare metrics like VSE sit), **C70/C72** (game theory — strategic voting), plus **D70/D79** (the general and catch-all buckets), **D02** (institutions) and **D82** (mechanism design). Worked example: [Wolk, Quinn & Ogren](../STAR_Voting/reference/wolk_quinn_ogren_2023.md) classify themselves **D72 · D63 · D71 · C70**.
  - **Math & computer science** (algorithms, complexity, *computational* social choice) → [arXiv](https://arxiv.org/), categories **cs.GT** (game theory), **econ.TH** (theoretical economics) and **cs.MA** (multiagent systems). Much of the newest work appears here first, free.
  - **Political science** (empirical: real elections, turnout, adoption, ballot errors) → not JEL-indexed; look to *Electoral Studies* and *Journal of Theoretical Politics*.
  - **Journals that regularly carry method papers:** *Social Choice and Welfare* (the flagship), *Public Choice*, *Constitutional Political Economy*, *Mathematical Social Sciences*, *Electoral Studies*.

  Same discipline as everywhere else here: an academic paper earns trust for *rigor*, not for agreeing with you — check who funded it and what the model assumes before you quote its number.
- **Watch** — [PBS *Infinite Series*: Voting Systems and the Condorcet Paradox](https://www.youtube.com/watch?v=HoAnYQZrNrQ) — a clear explainer of why majority preferences can cycle.

*(These include strong advocates on several sides. Read them the way this repo reads FairVote — critically, and for the argument, not the conclusion.)*

## Related

- [101 / 201 / 301 Curriculum](../CURRICULUM.md) — the STAR-specific deep track
- [Start Here](../00_START_HERE.md) — the method-neutral front door
- [Glossary](../GLOSSARY.md) · [Choosing among the Equal Vote methods](choosing_among_evc_methods.md)
