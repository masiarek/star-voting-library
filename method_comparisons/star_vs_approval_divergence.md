# How often do STAR and Approval disagree?

*A common question with a deceptively honest answer: **there is no single number** — and the reason *why* is the actual lesson. This page measures the divergence rate (with a runnable, seeded simulation), explains why the two methods split, and links the worked elections where you can watch it happen on real ballots.*

**Level: 301.** Companion: [What makes a good winner?](../00_start_here/what_makes_a_good_winner.md) · [election simulation models](../00_start_here/election_simulation_models.md) · the worked cases in [Black Curtain](black_curtain/).

## Why there's no single rate

STAR has a **canonical sincere ballot**: min-max your feelings onto 0–5. Approval does **not** — every voter must choose a **0/1 cutoff**, and *where they draw it* changes the winner. So the divergence rate depends on two modelling choices, not one:

1. the **electorate model** (how voters' preferences are generated), and
2. the **approval-cutoff rule** (how a voter turns feelings into approvals).

Quote a divergence percentage without both and it's meaningless — the same house rule the repo applies to every simulated number ([301.6/301.9](../00_start_here/CURRICULUM_301.md); [simulations README](../06_Other/simulations/)).

## The measured rates

From [`star_vs_approval_divergence.py`](../06_Other/simulations/star_vs_approval_divergence.py) (20,000 elections per cell, 51 voters, seed 12345; sincere ballots, no strategy):

| Electorate model | 3 candidates | 5 candidates |
|---|:---:|:---:|
| **Spatial** (voters & candidates as points in issue space — the realistic model) | **~12%** | **~25%** |
| **Impartial culture** (every utility independent & uniform — an adversarial stress test) | **~23%** | **~35%** |

Two robust takeaways:

- **Divergence grows with the size of the field** — with only two candidates they can't disagree; the more candidates, the more room for the two methods to pick differently.
- **The electorate model dominates the sincere cutoff.** The two sincere cutoffs tested — *approve above your average* and *approve the top half of your range* — give nearly identical rates; realistic (spatial) electorates disagree far less than the impartial-culture stress test. (The cutoff *can* matter at the extreme: an electorate that **bullet-votes** collapses Approval toward [Plurality](../00_start_here/plurality.md) and would diverge much more — but that's a strategic degenerate, not a sincere model, so it's a bound, not a rate.)

So a fair one-liner is: **in realistic 3–5 candidate elections, sincere STAR and Approval pick the same winner roughly 75–90% of the time; when they split, it's the *intensity-vs-breadth* disagreement below.**

## Why they diverge (when they do)

Both methods reward broad support — that's why they agree most of the time. They split on the **intensity-vs-breadth** axis:

- **STAR reads intensity and runs a runoff.** Its 0–5 ballot records *how much*, and the automatic runoff then asks *how many prefer A to B* among the two strongest. So STAR leans toward the candidate a **majority actively prefers** head-to-head.
- **Approval is a coarse 0/1 and has no runoff.** It elects whoever is **acceptable to the most voters** — the broadest common denominator — and can't distinguish "approve enthusiastically" from "approve as a tolerable compromise."

So the classic split is: a **broadly-tolerable consensus** candidate (Approval's pick) vs. an **intensely-preferred majority favorite** (STAR's pick, surfaced by the runoff). Neither is "wrong" — it's the [good-winner](../00_start_here/what_makes_a_good_winner.md) question (utilitarian-broad vs. majoritarian) showing up as a method disagreement.

## Watch it on real ballots — worked examples

The [**Black Curtain**](black_curtain/) set is exactly this, made countable: the *same* small electorate counted by Approval, STAR (and RCV-IRV / Range), so you can see where they agree and where they part:

- [Hidden consensus](black_curtain/black_curtain_pages/) — a broadly-liked compromise that Approval elects and STAR's runoff can pass over.
- [Near-clones](black_curtain/) and [polarized](black_curtain/) variants — how the split appears (or doesn't) as the preference structure changes.
- [Range vs the rest](black_curtain/black_curtain_range.md) — the same ballots under Score, for contrast.

For the single-election view in the engine, any Approval or STAR file prints a **[Divergence from STAR]** block when the methods disagree ([divergence review ledger](divergence_review/)).

## Run it yourself

```bash
python3 06_Other/simulations/star_vs_approval_divergence.py                 # default sweep
python3 06_Other/simulations/star_vs_approval_divergence.py --candidates 5 --voters 101
python3 06_Other/simulations/star_vs_approval_divergence.py --selftest      # known-answer checks
```

It reuses the electorate models and STAR tabulator from [`fbc_simulation.py`](../06_Other/simulations/fbc_simulation.py), is fully **seeded** (reproducible), and **self-tests** its tabulators (a known Approval count and a constructed STAR≠Approval divergence) before every run. Everything it reports carries its model and cutoff — because, as above, the number is meaningless without them.

## The honest caveats

- **Sincere only.** This measures *sincere* ballots. Real Approval voters adjust their cutoff to the race (polls, frontrunners), which is a *different* study.
- **Model-bounded.** Spatial ≈ realistic; impartial culture ≈ adversarial upper bound. The truth for any real electorate sits between and depends on its actual preference structure.
- **Tie rules fixed.** STAR and Approval ties are broken deterministically (documented in the script); a different tie rule would nudge the edges.

## Related

- [Black Curtain](black_curtain/) — the worked STAR-vs-Approval(-vs-others) elections
- [Runoff-reversal & FBC simulations](../06_Other/simulations/) — the sibling brute-force studies
- [Choosing among the Equal Vote methods](../00_start_here/choosing_among_evc_methods.md) · [Criteria at a glance](../00_start_here/criteria_at_a_glance.md)
