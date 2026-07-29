# Approval Voting — concept pages

Everything explaining **Approval** (mark every candidate you approve — **1** — leave the rest **0**; most approvals wins). New here? Start with **[Approval Voting](approval_voting.md)** — how the ballot and the count work. Approval is Score voting at **one-bit resolution**: the simplest equal-vote upgrade to Choose-One, and the natural stepping-stone to STAR.

**Run it:** the 101 case lives in [the Approval examples](../) — and the [Black Curtain set](../../method_comparisons/black_curtain/) counts the *same* five voters by Approval vs STAR vs RCV-IRV vs Score (Approval flips the winner in election 1).

## Single-winner Approval

- [Approval Voting](approval_voting.md) — the ballot, the one decision it asks (*where's my approval line?*), reading a result, and where it fits in the scored family
- [Approval + Top-Two](approval_top_two.md) — the reform package (St. Louis): an Approval primary feeding a head-to-head general, and why the runoff **must** be a second election — the exact package STAR folds into one ballot
- [Honest limits](approval_honest_limits.md) — no preference strength or order, and the unavoidable threshold choice (the gap STAR was designed to close)
- [Approval in the theory literature (301)](approval_in_the_literature.md) — the six arguments and five criticisms as academia states them (two of the five don't survive), the **three incompatible readings of what "approve" means** and why the strategy argument can't settle until you pick one, and *Approval = Borda = Condorcet* on dichotomous preferences — with the runnable case that shows why that equivalence doesn't transfer to a real election
- [The case for approval voting — Hamlin & Hua (2023), claim-checked (301)](hamlin_hua_2023.md) — the Approval camp's own academic case, and the companion article to [the STAR paper](../../01_STAR/concepts/reference/wolk_quinn_ogren_2023.md) in the same journal issue. Section 4 answers four critiques (majority criterion, later-no-harm, bullet voting, expressiveness); its §4.1 example is fully runnable, so the page is mostly engine output — including the paper's own utility defence, written down and counted

## Multi-winner & committees

The same 0/1 ballot fills several seats. See the **[Multiwinner_Approval/](Multiwinner_Approval/)** subfolder:

- [Approval — Multi-Winner](Multiwinner_Approval/approval_multiwinner.md) — bloc (at-large) counting and the proportional adaptations (SPAV, PAV)
- [Electing a committee — a gentle intro (101)](Multiwinner_Approval/abc_rules_intro.md) — "most approved" vs "cover everyone" vs proportional, counting only
- [ABC rules & the utilitarian–egalitarian spectrum (301)](Multiwinner_Approval/abc_rules_spectrum.md) — the approval-committee formalism (AV / PAV / Chamberlin–Courant / Phragmén), verified with `abcvoting`
- [Thiele methods (301)](Multiwinner_Approval/thiele_methods.md) — AV/PAV/CC as one parameterised family, and where STAR-PR (RRV) fits

## Reference

- Glossary: [Approval terms](glossary_approval.md)

*(Parallel method hub: [STAR Voting](../../01_STAR/concepts/README.md). Up: the docs hub [`00_START_HERE`](../../00_start_here/00_START_HERE.md).)*
