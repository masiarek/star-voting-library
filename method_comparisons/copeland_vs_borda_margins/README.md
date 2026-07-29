# Margins matter — one electorate, four different answers

*Twelve voters rank three gelato flavours and the pairwise contests form a loop: **Almond beats Berry 7–5, Berry beats Cocoa 8–4, Cocoa beats Almond 7–5**. There is no [Condorcet winner](../../00_start_here/topics/condorcet/README.md). What happens next depends entirely on one question — **does your method look at the size of each victory, or only at who won?** [Copeland](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) throws the margins away and ties all three. [Borda](../../06_Other/other_ranked_methods/borda.md) is the same tournament weighted by those margins, and it separates them cleanly. Plurality and [RCV-IRV](../../00_start_here/RCV_IRV/README.md) each pick a third and fourth answer. Four rules, four verdicts, twelve ballots.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/kdjjkq) · **[results ↗](https://bettervoting.com/kdjjkq/results)** (election `kdjjkq`, Test ID **BV2251** — four races on the same 12 ballots: Choose-One, STAR, RCV-IRV, Ranked Robin).

→ **Level: Voting 301.** See also: [the cycle–cocycle decomposition](../../00_start_here/topics/cycle_cocycle_decomposition.md) (the theorem behind this page) · [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · [the minimal tilted cycle](../minimal_tilted_cycle/README.md) (five voters — the smallest lopsided cycle) · [Condorcet's 1788 rebuttal to Borda](../borda_condorcet_1788/README.md) (the mirror image: Borda's *sincere* failure) · [the social welfare function](../../00_start_here/topics/social_welfare_function.md)

---

## The ballots

| Voters | Ranking |
|---:|---|
| 5 | Almond > Berry > Cocoa |
| 3 | Berry > Cocoa > Almond |
| 2 | Cocoa > Almond > Berry |
| 2 | Cocoa > Berry > Almond |

Twelve individual ballots, no weighting. Every voter's own ranking is perfectly transitive; the loop is manufactured entirely by adding them up.

## The tournament, with and without weights

```
Almond  beats Berry    7 – 5      (margin +2)
Berry   beats Cocoa    8 – 4      (margin +4)
Cocoa   beats Almond   7 – 5      (margin +2)
```

**Unweighted — Copeland counts wins only.** Each flavour goes 1–1–0, so all three tie and the Copeland winning set is `{Almond, Berry, Cocoa}`. The rule has no way to say that Berry's victory was twice the size of anyone else's, because it never looked.

**Weighted — sum the signed margins and you have the Borda count.** This is the *symmetric* Borda score, Σ Net(x > y) over every opponent:

```
Almond = +2 − 2 =  0
Berry  = −2 + 4 = +2      ← Borda winner
Cocoa  = +2 − 4 = −2
```

Those two paragraphs are the entire lesson. **Copeland and Borda are the same tournament read twice — once ignoring the labels on the arrows, once summing them.**

## Where each method lands

| Method | Winner | What it is looking at |
|---|---|---|
| [Choose-One (Plurality)](../../00_start_here/topics/plurality.md) | **Almond** | first choices only (5 / 3 / 4) |
| [RCV-IRV](../../00_start_here/RCV_IRV/README.md) | **Cocoa** | first choices, then transfers |
| [Borda](../../06_Other/other_ranked_methods/borda.md) | **Berry** | every margin, weighted |
| [Copeland (raw)](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) | **nobody** — 3-way tie | who won each pair, not by how much |
| [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) (LH) | **Berry** | Copeland, then total margin as tiebreak |
| [STAR](../../00_start_here/STAR_Voting/README.md) (ranks → 5/3/0) | **Almond** | Borda's scoring round, then a head-to-head |

**RCV-IRV eliminates the Borda winner first.** Berry has the fewest first choices (3), so instant runoff drops the flavour that wins every margin-weighted measure before the count really begins. All three Berry ballots transfer intact to Cocoa, which wins 7–5. Full round-by-round → [`margins_irv.md`](cases/cases_pages/margins_irv.md).

**Keep it fair:** this is *not* a center-squeeze indictment of IRV. There is no Condorcet winner here for IRV to miss — the pairwise contests genuinely cycle, so no method can elect "the candidate who beats everyone." Every rule in the table is making a defensible choice about what to do when no such candidate exists. The disagreement is the point, not a scandal.

## The engine already prints the Borda score — it just calls it "Margin"

Look at the Ranked Robin output ([full report →](cases/cases_pages/margins_ranked_robin.md)):

```
Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Berry      1–1–0         1      +2  Cocoa
    2  Almond     1–1–0         1      +0  Berry
    3  Cocoa      1–1–0         1      -2  Almond

Winner — Ranked Robin (RCV-RR): Berry
   *** 3 candidates tie for the most wins (Almond, Berry, Cocoa) — a Condorcet cycle.
       Resolved by total margin, then lot order.
```

The **Copeland** column ties at 1. The **Margin** column reads `+2 / 0 / −2` — and that is precisely the symmetric Borda score computed above. So **the LH engine's cycle tiebreak is a Borda count**, applied only after Copeland has failed to decide. That is a real and slightly surprising fact about how this repo's Ranked Robin behaves in a cycle, and it is worth knowing before you cite an RR result from a cycling election.

BetterVoting does *not* do this. Its ladder tries a head-to-head between the tied candidates, which only works for a clean two-way tie; on a three-way tie it falls through to a **random** pick. See [RR tiebreak — LH vs BV](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).

## BetterVoting vs. the LH engine — and one race that can't be frozen

All four races ran live on BetterVoting ([BV2251 `kdjjkq`](https://bettervoting.com/kdjjkq/results)) on the same twelve ballots:

| Race | BetterVoting | LH engine | |
|---|---|---|---|
| Choose-One (Plurality) | Almond | Almond | ✓ agree |
| STAR | Almond | Almond | ✓ agree |
| RCV-IRV | Cocoa | Cocoa | ✓ agree |
| Ranked Robin | Almond — `tieBreakType: random` | **Berry** (total margin) | **documented divergence** |

The three deterministic races agree exactly. The Ranked Robin race is the one that cannot be frozen, and BetterVoting's own export says so: the result carries **`tieBreakType: random`**. Its ladder has a head-to-head rung that only works for a clean *two*-way tie; on this genuine three-way tie it falls through to a random pick. LH's ladder instead uses total margin — the symmetric Borda score — and elects Berry.

**So on the live results page, read the Ranked Robin *pairwise table*, not its crowned winner.** The table is deterministic and is the artifact; the name at the top of that one race is a coin flip and would land differently if the election were re-run. This is the same LH-vs-BV split written up in [rr_tiebreak_lh_vs_bv.md](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md), and it is worth seeing live: a real public election where the platform itself flags that it guessed.

Frozen export: [`margins_star_bv_export.json`](cases/margins_star_bv_export.json).

## STAR, and an honest caveat

Ranks carry no intensity, so running a score method on a ranked profile means inventing one. On an even **5 / 3 / 0** spacing the scoring round reproduces Borda exactly — Berry first — and then the automatic runoff runs the direct contest Borda never runs, and Almond takes it 7–5:

```
[Runoff Reversal]
 - Score Round Winner(s) = (Berry)
 - Runoff Round Winner   = (Almond)

[Condorcet Winner]
  No Condorcet winner (majority cycle: Almond > Berry > Cocoa > Almond)

[Divergence from STAR]
  STAR     = Almond
  RCV-IRV  = Cocoa   (differs from STAR)
  Approval = Berry   (differs from STAR)
  RCV-RR   = Berry   (differs from STAR)
```

**The caveat, which belongs on the page and not in a footnote:** unlike [Condorcet's 1788 profile](../borda_condorcet_1788/README.md), this result is **not robust to the spacing**. Almond wins under 5/3/0, 5/4/0, 5/2/0 and 4/2/0 — but under a polarized **5/1/0** the scoring round promotes Cocoa over Berry into the runoff, and **Cocoa wins instead**. With no Condorcet winner to anchor the outcome, the rank-to-score conversion is doing real work. That is exactly the objection the [Borda page](../../06_Other/other_ranked_methods/borda.md) raises against fabricating intensities, and it applies to our own method here. See [the 5/1/0 challenge](../star_5_1_0_challenge/README.md).

Full report → [`margins_star.md`](cases/cases_pages/margins_star.md).

## About the size of this example

The profile is the twelve-ballot structural twin of a textbook profile that is printed with **304 voters** (102 / 101 / 100 / 1). The shrink is exact where it counts:

| | printed (304 ballots) | this page (12 ballots) |
|---|---|---|
| pairwise margins | 100 / 102 / 100 | 2 / 4 / 2 |
| Copeland | 0, 0, 0 → tie of all three | 0, 0, 0 → tie of all three |
| **symmetric Borda** | **0, +2, −2 → Borda winner b** | **0, +2, −2 → Borda winner Berry** |
| asymmetric Borda | 304, 305, 303 | 12, 13, 11 |
| Plurality | a | Almond |
| RCV-IRV | c | Cocoa |

Identical symmetric Borda scores, identical Copeland tie, identical winners — and the textbook's own affine identity `Borda^asym = n + ½·Borda^sym` checks out at both sizes.

**Two things the printed size shows that the small one cannot**, and they are the reason the 304-ballot version is kept as a reference file:

1. **The margins are near-identical** — 100 / 102 / 100. Margin-weighting breaks a dead heat *by a hair*. At twelve ballots the same structure reads 2 / 4 / 2, which makes Berry's edge look decisive when the original's point is that it is razor-thin.
2. **The bloc counts are coprime** (gcd = 1), so the printed profile is not a scaled-up copy of anything smaller — and the lone 1-voter is **load-bearing**, not decoration. Delete it and the symmetric Borda scores become `+2 / +2 / −4`: a **tie** between a and b, destroying the "unique Borda winner" the passage is built on, while RCV-IRV flips from c to a.

So this is a shrink that preserves *structure*, not a rescaling — there is no rescaling to be had. The reference copy lives at [`margins_paper_exact_304.md`](cases/cases_pages/margins_paper_exact_304.md) (LH-only, no BetterVoting election). The general rule this case worked out is written up in [TIPS — choosing voter counts](../../00_start_here/tips/TIPS_choosing_voter_counts.md#lifting-a-profile-out-of-a-paper).

## Reproduce it

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/copeland_vs_borda_margins/cases/margins_ranked_robin.yaml
```

The LH engine has no Borda tabulator, so the Borda and Copeland figures are cross-checked with [`pref_voting`](../../00_start_here/tabulation_engines/cross_checking_with_pref_voting.md):

```bash
uv run python -c "
from pref_voting.profiles import Profile
from pref_voting.scoring_methods import borda, plurality
from pref_voting.c1_methods import copeland
n={'Almond':0,'Berry':1,'Cocoa':2}; names=list(n)
rows=[(5,['Almond','Berry','Cocoa']),(3,['Berry','Cocoa','Almond']),(2,['Cocoa','Almond','Berry']),(2,['Cocoa','Berry','Almond'])]
P=Profile([tuple(n[c] for c in o) for _,o in rows], rcounts=[c for c,_ in rows])
print('borda scores ->', P.borda_scores())
print('borda        ->', [names[w] for w in borda(P)])
print('copeland     ->', [names[w] for w in copeland(P)])
print('plurality    ->', [names[w] for w in plurality(P)])
print('condorcet    ->', P.condorcet_winner())"
```

```
borda scores -> {0: 12, 1: 13, 2: 11}
borda        -> ['Berry']
copeland     -> ['Almond', 'Berry', 'Cocoa']      ← all three, exactly as the chapter reports
plurality    -> ['Almond']
condorcet    -> None
```

An independent engine, the same four verdicts.

## Notes on the source

The 304-voter profile is `P₂` from **William S. Zwicker, "Introduction to the Theory of Voting,"** Chapter 2 of the *Handbook of Computational Social Choice* — the chapter that also gives this repo its [social welfare function](../../00_start_here/topics/social_welfare_function.md) definitions. The chapter uses `P₂` to contrast the Copeland rule (which "disregards the margins of victory or defeat") with the symmetric Borda score defined as the sum of net preferences, and reports the Copeland three-way tie and the Borda winner set `{b}`.

The flavour names are this repo's; the source uses bare `a` / `b` / `c`, which the [reference copy](cases/cases_pages/margins_paper_exact_304.md) keeps for fidelity. The initials are preserved on purpose — **A**lmond, **B**erry, **C**ocoa map onto the book's a, b, c.
