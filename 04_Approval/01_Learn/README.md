# Approval Voting — concept pages

Everything explaining **Approval** (mark every candidate you approve — **1** — leave the rest **0**; most approvals wins). New here? Start with **[Approval Voting](approval_voting.md)** — how the ballot and the count work. Approval is Score voting at **one-bit resolution**: the simplest equal-vote upgrade to Choose-One, and the natural stepping-stone to STAR.

<img src="img/approval_ballot_single_bubble.png" width="420" alt="An Approval ballot: one bubble per candidate — Andre, Blake, Carmen, David, Erin — under the instruction 'Vote for ALL candidates you approve of'. This voter has filled the bubbles for Andre, Carmen and David."> <img src="img/approval_ballot_yes_no_double_bubble.png" width="420" alt="The Yes/No variant of the same Approval ballot: an explicit Yes and No bubble for each of Andre, Blake, Carmen, David and Erin. This voter marks Yes for Andre, Carmen and David, No for Blake and Erin.">

*The two Approval ballots ([Equal Vote](https://www.equal.vote/approval)): the plain **single bubble** — mark everyone you approve — and the **Yes / No "double bubble"**, where a blank is distinguishable from a deliberate No (the ballot-security hardening in [honest limits §6](approval_honest_limits.md)). Either way the count is the same: add up the approvals. The repo's own case art draws the Yes/No form — see the ballots on [Approval Voting](approval_voting.md#reading-an-approval-result) and on [the folder front door](../README.md).*

**Run it:** the 101 case lives in [the Approval examples](../) — and the [Black Curtain set](../../method_comparisons/black_curtain/) counts the *same* five voters by Approval vs STAR vs RCV-IRV vs Score (Approval flips the winner in election 1).

## Single-winner Approval

- [Approval Voting](approval_voting.md) — the ballot, the one decision it asks (*where's my approval line?*), reading a result, and where it fits in the scored family
- [Approval + Top-Two](approval_top_two.md) — the reform package (St. Louis): an Approval primary feeding a head-to-head general, and why the runoff **must** be a second election — the exact package STAR folds into one ballot
- [Honest limits](approval_honest_limits.md) — no preference strength or order, and the unavoidable threshold choice (the gap STAR was designed to close)
- [Approval in the theory literature (301)](approval_in_the_literature.md) — the six arguments and five criticisms as academia states them (two of the five don't survive), the **three incompatible readings of what "approve" means** and why the strategy argument can't settle until you pick one, and *Approval = Borda = Condorcet* on dichotomous preferences — with the runnable case that shows why that equivalence doesn't transfer to a real election
- [Is Approval's outcome arbitrary? The Saari–Van Newenhizen critique (301)](approval_indeterminacy.md) — the sharpest academic attack on Approval (a voter who prefers `a > b > c` has no ballot that says so), why the Brams–Fishburn–Merrill defense conceded too much, and Hillinger's inversion — **one approval result, two opposite Borda winners**, runnable. Plus the popular-press version ("the whole election can become random"), split into the half that holds and the half that doesn't
- [The case for approval voting — Hamlin & Hua (2023), claim-checked (301)](hamlin_hua_2023.md) — the Approval camp's own academic case, and the companion article to [the STAR paper](../../01_STAR/01_Learn/reference/wolk_quinn_ogren_2023.md) in the same journal issue. Section 4 answers four critiques (majority criterion, later-no-harm, bullet voting, expressiveness); its §4.1 example is fully runnable, so the page is mostly engine output — including the paper's own utility defence, written down and counted

## The three-option variant

- [Combined Approval Voting (CAV)](../../06_Other/Combined_Approval/README.md) — Approval plus an explicit **Against**: For (+1) / abstain (0) / Against (−1), highest net wins. Proposed by Dan Felsenthal in 1989 as the answer to the Approval failures [his own paradox examples](../../method_comparisons/felsenthal_paradoxes/) demonstrate. Lives in `06_Other/` because it isn't an EVC method, but it belongs to this family — and it carries the sharpest lesson about **what a blank means**: CAV reads an unmarked row as the middle grade, every other score ballot here reads it as the lowest, and a runnable pair of elections shows the same twelve voters reversing end-to-end on that one word

## Multi-winner & committees

The same 0/1 ballot fills several seats. See the **[Multiwinner_Approval/](Multiwinner_Approval/)** subfolder:

- [Approval — Multi-Winner](Multiwinner_Approval/approval_multiwinner.md) — bloc (at-large) counting and the proportional adaptations (SPAV, PAV)
- [Electing a committee — a gentle intro (101)](Multiwinner_Approval/abc_rules_intro.md) — "most approved" vs "cover everyone" vs proportional, counting only
- [ABC rules & the utilitarian–egalitarian spectrum (301)](Multiwinner_Approval/abc_rules_spectrum.md) — the approval-committee formalism (AV / PAV / Chamberlin–Courant / Phragmén), verified with `abcvoting`
- [Thiele methods (301)](Multiwinner_Approval/thiele_methods.md) — AV/PAV/CC as one parameterised family, and where STAR-PR (RRV) fits
- [Satisfaction Approval Voting — SAV (301)](Multiwinner_Approval/satisfaction_approval_voting.md) — Brams & Kilgour's rule: one vote per **ballot**, split evenly among your marks, so approving four gives each ¼. Their own example elects a committee **disjoint** from bloc Approval's on identical ballots; it punishes clones where AV rewards them; and the authors prove the cases where it does *worse* than AV. Used for real in Peoria, Illinois, since 1991 — plus a claim-check of the mangled Wikipedia retelling

## Reference

- Glossary: [Approval terms](glossary_approval.md)
- [Criteria at a glance](../../07_Concepts/topics/criteria_at_a_glance.md) — Approval's pass/fail row beside STAR, Ranked Robin and RCV-IRV, with the ✗s linked to runnable elections
- [Approval voting — Wikipedia](https://en.wikipedia.org/wiki/Approval_voting) — the neutral reference for the history (papal conclaves, Venice, Greece), the adoption **and repeal** record, and the criteria table. Where a campaign source would be weakest, this is the one to cite

*(Parallel method hub: [STAR Voting](../../01_STAR/01_Learn/README.md). Up: the docs hub [`00_START_HERE`](../../07_Concepts/00_START_HERE.md).)*
