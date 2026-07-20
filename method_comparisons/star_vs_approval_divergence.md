# How often do STAR and Approval disagree?

*A common question with a deceptively honest answer: **there is no single number** — and the reason *why* is the actual lesson. This page measures the divergence rate (with a runnable, seeded simulation), explains why the two methods split, and links the worked elections where you can watch it happen on real ballots.*

**Level: 301.** Companion: [What makes a good winner?](../00_start_here/topics/what_makes_a_good_winner.md) · [election simulation models](../00_start_here/topics/election_simulation_models.md) · the worked cases in [Black Curtain](black_curtain/).

## Why there's no single rate

STAR has a **canonical sincere ballot**: min-max your feelings onto 0–5. Approval does **not** — every voter must choose a **0/1 cutoff**, and *where they draw it* changes the winner. So the divergence rate depends on two modelling choices, not one:

1. the **electorate model** (how voters' preferences are generated), and
2. the **approval-cutoff rule** (how a voter turns feelings into approvals).

Quote a divergence percentage without both and it's meaningless — the same house rule the repo applies to every simulated number ([301.6/301.9](../00_start_here/curriculum/CURRICULUM_301.md); [simulations README](../06_Other/simulations/)).

## The measured rates — the approval cutoff is the knob

Because Approval has no canonical sincere ballot, the honest way to report this is to **sweep the cutoff**. Read each voter's 0–5 STAR ballot as approvals at threshold *N* (approve everything scored ≥ *N*): *ge5* = approve only your top (near-[bullet](../00_start_here/topics/plurality.md)), *ge1* = approve anyone but your worst. From [`star_vs_approval_divergence.py`](../06_Other/simulations/star_vs_approval_divergence.py) (20,000 elections, 51 voters, seed 12345, sincere):

**3 candidates** — divergence by where the approval line is drawn:

| Approve scores ≥ | Spatial (realistic) | Impartial (stress) |
|---|:---:|:---:|
| **5** — only your top (near-bullet) | 14% | 22% |
| **4** | **10%** ← *most STAR-like* | 22% |
| **3** — top half of the scale | 12% | 23% |
| **2** | 20% | 24% |
| **1** — anyone but your worst | **27%** | 27% |

Four findings:

- **The cutoff is the dominant knob under a realistic electorate.** Just moving the approval line swings divergence from ~10% to ~27% (3 candidates); at 4 candidates it's ~15% to ~39%. So "how often do STAR and Approval disagree?" has *no answer* until you say **where voters approve** — which is the whole point.
- **It's non-monotonic, with a sweet spot.** Agreement is *highest* at a **moderate** cutoff (approve your top ~half, ge3–ge4) and *worst at the generous extreme* (ge1): approving everyone but your worst discards nearly all intensity and collapses Approval toward "least-hated" — exactly where it parts from STAR's majority-preferred runoff winner.
- **More candidates → more divergence**, at every cutoff.
- **The electorate model still matters** (impartial > spatial), but under the realistic model the *cutoff* moves the number more than the model does. (An earlier version of this page tested only two *similar* cutoffs and wrongly concluded the cutoff barely mattered — the sweep corrects that.)

A fair one-liner: **with a sensible sincere cutoff (approve your top half) in realistic 3–5 candidate elections, STAR and Approval agree ~80–90% of the time; loosen the cutoff toward "approve almost everyone" and they part far more often** — because that's when Approval stops measuring intensity. When they split, it's the *intensity-vs-breadth* disagreement below.

## Why they diverge (when they do)

Both methods reward broad support — that's why they agree most of the time. They split on the **intensity-vs-breadth** axis:

- **STAR reads intensity and runs a runoff.** Its 0–5 ballot records *how much*, and the automatic runoff then asks *how many prefer A to B* among the two strongest. So STAR leans toward the candidate a **majority actively prefers** head-to-head.
- **Approval is a coarse 0/1 and has no runoff.** It elects whoever is **acceptable to the most voters** — the broadest common denominator — and can't distinguish "approve enthusiastically" from "approve as a tolerable compromise."

So the classic split is: a **broadly-tolerable consensus** candidate (Approval's pick) vs. an **intensely-preferred majority favorite** (STAR's pick, surfaced by the runoff). Neither is "wrong" — it's the [good-winner](../00_start_here/topics/what_makes_a_good_winner.md) question (utilitarian-broad vs. majoritarian) showing up as a method disagreement.

## Watch it on real ballots — worked examples

The [**Black Curtain**](black_curtain/) set is exactly this, made countable: the *same* small electorate counted by Approval, STAR (and RCV-IRV / Range), so you can see where they agree and where they part:

- [Hidden consensus](black_curtain/cases/cases_pages/Black_Curtain_01_c3_b5_hidden-consensus.md) — a broadly-liked compromise that Approval elects and STAR's runoff can pass over.
- [Near-clones](black_curtain/) and [polarized](black_curtain/) variants — how the split appears (or doesn't) as the preference structure changes.
- [Range vs the rest](black_curtain/black_curtain_range.md) — the same ballots under Score, for contrast.

For the single-election view in the engine, any Approval or STAR file prints a **[Divergence from STAR]** block when the methods disagree ([divergence review ledger](divergence_review/)).

## Run it yourself

```bash
python3 06_Other/simulations/star_vs_approval_divergence.py                       # default: sweep score cutoffs ge5..ge1
python3 06_Other/simulations/star_vs_approval_divergence.py --candidates 5 --voters 101
python3 06_Other/simulations/star_vs_approval_divergence.py --cutoffs mean midpoint   # utility cutoffs instead
python3 06_Other/simulations/star_vs_approval_divergence.py --selftest            # known-answer checks
```

The **`--cutoffs`** parameter is the one that matters: `geN` reads the STAR ballot as approvals at threshold *N* (the sweep above); `mean`/`midpoint` are utility-based cutoffs. Sweeping it is how you *see* that the "divergence rate" is a function of the approval rule, not a fixed fact.

It reuses the electorate models and STAR tabulator from [`fbc_simulation.py`](../06_Other/simulations/fbc_simulation.py), is fully **seeded** (reproducible), and **self-tests** its tabulators (a known Approval count and a constructed STAR≠Approval divergence) before every run. Everything it reports carries its model and cutoff — because, as above, the number is meaningless without them.

## The honest caveats

- **Sincere only.** This measures *sincere* ballots. Real Approval voters adjust their cutoff to the race (polls, frontrunners), which is a *different* study.
- **Model-bounded.** Spatial ≈ realistic; impartial culture ≈ adversarial upper bound. The truth for any real electorate sits between and depends on its actual preference structure.
- **Tie rules fixed.** STAR and Approval ties are broken deterministically (documented in the script); a different tie rule would nudge the edges.

## Related

- [Black Curtain](black_curtain/) — the worked STAR-vs-Approval(-vs-others) elections
- [Brams' grading paradox, counted](brams_grading_paradox/) — the cutoff dependence in one 3-voter example: four reasonable 0/1 cuts of the same grades elect Adams, Baker, or a tie
- [Runoff-reversal & FBC simulations](../06_Other/simulations/) — the sibling brute-force studies
- [Choosing among the Equal Vote methods](../00_start_here/topics/choosing_among_evc_methods.md) · [Criteria at a glance](../00_start_here/topics/criteria_at_a_glance.md)
