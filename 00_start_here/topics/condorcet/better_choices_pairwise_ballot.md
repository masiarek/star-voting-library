# Better Choices — a Condorcet method with the pairwise matchups *printed on the ballot*

*A fresh reform idea, read fairly. **Better Choices** (as described by **Taylor Eigen Fisher**, "[Better Choices Has a Neat Idea](https://eigentaylor.github.io/blog/better-choices/)", eigentaylor.github.io) is a Top-3 [Condorcet method](README.md) with an unusual front-end: instead of a ranking, the final ballot shows the three head-to-head races as **separate bubble questions**. This page explains the mechanic, credits what's genuinely clever about it, maps it onto this repo's [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) engine, and claim-checks the post's specific claims. Fisher is candidly an **Approval-voting advocate** and says so — his conclusion is conditional, not a sales pitch, which makes the post a good model of [reading advocacy critically](fairvote_condorcet_claim_check.md). We lean pro-STAR here and say so too; the checks below cut in every direction.*

→ Related: [Ranked Robin (Copeland)](../../RCV_Ranked_Robin/ranked_robin.md) · [cycle resolution — Minimax / Ranked Pairs / Schulze](../../RCV_Ranked_Robin/cycle_resolution.md) · [pairwise counting](../pairwise_counting.md) · [3-2-1 Voting](../three_two_one_voting.md) (the other named rated-system explainer) · [the ranked-ballot method zoo](../ranked_ballot_methods_zoo.md).

---

## The ballot and the count

With three finalists — Fisher's cast is **Alice, Bob, Clark** — the final ballot presents **three different races**:

- Alice vs. Bob
- Alice vs. Clark
- Bob vs. Clark

You bubble a winner in each. The count, in Fisher's words:

> "If a candidate wins both of their matchups, they are elected. If no candidate wins both matchups, the candidate with the 'least bad loss' (the one who lost by the smallest margin) is elected."

That "least bad loss" rule is **[Minimax](../../RCV_Ranked_Robin/cycle_resolution.md)** — elect the candidate whose *worst single defeat is the smallest*. So Better Choices is, mechanically, **Condorcet-with-Minimax-completion**, presented on a bubble ballot rather than a ranking.

## What's genuinely clever — credit where it's due

Two real ideas here, and they're worth naming:

1. **The pairwise matrix *is* the ballot.** A repo staple is that any Condorcet method [computes a pairwise matrix](../pairwise_counting.md) from ranked or scored ballots — the voter ranks, the machine derives the head-to-heads. Better Choices inverts that: it asks the head-to-heads **directly**, in the familiar bubble format people already use for [Choose-One](../plurality.md). No ranking to explain, no "what if I only rank two." For a public that rejects reforms it finds confusing, cutting the ballot down to "pick a winner in each of three races" is a real usability bet.

2. **It surfaces the pairwise logic voters never see.** Under RCV-IRV a [center squeeze](../center_squeeze/) is invisible on the ballot — the eliminated [Condorcet winner](README.md) leaves no trace. Here the head-to-heads are the ballot, so "who beats whom" is the thing voters actually mark. That's pedagogically honest.

## The wrinkle Fisher flags: intransitive ballots

Because the three bubbles are **independent**, a voter can mark a cycle:

> "you can vote intransitively. Rock over Scissors, Scissors over Paper, Paper over Rock. You literally can't do that in a ranked method."

**True, and it's the honest cost of the clever ballot.** A ranked ballot *cannot* express A>B>C>A — the ordering enforces transitivity at the pen. Splitting the question into three independent bubbles gives that constraint up. In practice most voters won't vote a personal cycle, and it doesn't break the count (Minimax still returns a winner from the aggregate). But it's a genuine trade: the friendlier ballot admits an incoherent vote the ranked ballot structurally forbids. Worth teaching as a clean example of **ballot design shaping what voters can even say** — the same lesson as [scores vs. ranks](../../scores_and_ranks/scores_vs_ranks.md).

## Where it lands in this repo: it's Ranked Robin's cousin

When a **Condorcet winner exists** — the ordinary case — Better Choices' "wins both matchups → elected" rule elects exactly that candidate. So does [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md), so does STAR [very often](README.md), so does every Condorcet method. On the repo's runnable Condorcet-winner cases (e.g. the [symmetric 47/47/3/3 centrist, BV2170](../../../method_comparisons/symmetric_centrist_bv2170/bv2170_pp2q4q_symmetric_centrist.md), or [FairVote's own 40/15/40 hypothetical, BV2168](../../../method_comparisons/fairvote_condorcet_claims/cases/cases_pages/bv2168_6w2gq7_fairvote_40_15_40_moderate_cw.md)), Better Choices would elect the same head-to-head winner the pairwise matrix already prints. Nothing new to tabulate — the winner is whoever tops the matrix.

The methods only part company in a **[cycle](../../RCV_Ranked_Robin/cycle_resolution.md)** — and there's a precise nuance the post glides over.

## Claim check

### Claim 1 — "At three candidates, Minimax agrees with Ranked Pairs and Schulze."

Verbatim, Minimax "agrees with Ranked Pairs and Schulze, which are top-shelf Condorcet methods."

**True — and the repo already demonstrates it.** When a Condorcet winner exists, *all* Condorcet methods agree trivially. In a genuine three-way cycle, Minimax, Ranked Pairs, and Schulze all elect the candidate whose worst loss is smallest — with three candidates they cannot diverge. That's exactly the convergence shown, runnably, in [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md).

**But the missing footnote matters for *this* repo:** Better Choices' completion (Minimax) is **not** the same as [Ranked Robin / Copeland](../../RCV_Ranked_Robin/ranked_robin.md), the repo's default Condorcet engine. In a true three-way cycle (rock-paper-scissors), each candidate goes 1–1, so **Copeland ties all three** and has to fall to a [tiebreak](../../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md); Minimax instead reads the *margins* and picks a unique winner. So "Better Choices = Ranked Robin" is *almost* right and *usually* right (whenever there's a Condorcet winner), but its cycle behavior is Minimax's, not Copeland's. A small correction, but it's the difference between "ties, needs a coin" and "picks by margin," which is precisely the axis this repo tracks.

### Claim 2 — "STAR lost in 2024 with over 64% voting 'no'."

**True, with the scope named.** This is **Eugene, Oregon — Measure 20-349** (May 2024), a *municipal* STAR measure for Mayor and City Council, which failed roughly 64% no. It is a fair data point about **adoption difficulty**, and this repo won't wave it away: complex-sounding reforms lose at the ballot box, and STAR has to clear that bar like anything else. Two honest qualifiers keep it in proportion: (a) it was a **single local measure**, not a statewide verdict on STAR; and (b) the *same* adoption headwind sank RCV in multiple 2024 jurisdictions and is the entire reason [Alaska may repeal its RCV-IRV system](../../../method_comparisons/alaska_2022/alaska_301.md) — so "voters found it confusing" is a cost every reform pays, not a STAR-specific indictment. The point Fisher is actually making — that mathematical elegance and political viability don't automatically align — is correct, and it's one we make too.

### Claim 3 — "Pair it with an Approval primary, not Choose-One."

Fisher's core recommendation:

> "If this system uses the choose-one primary, we will still be plagued by vote splitting and spoilers, with no nursery effect for broadly acceptable candidates."

**Analytically sound, and it generalizes past his own proposal.** A Top-N runoff is only as good as the primary that fills the N slots: a [Choose-One](../plurality.md) primary re-imports [vote-splitting and the spoiler effect](../spoiler_effect.md) at the qualifying stage, and can eliminate a broadly-liked candidate *before* the clever general ever sees them — the same failure that makes [California's Top-2](../two_party_dominance.md) shut out compromise candidates. Using [Approval](../../Approval_Voting/approval_voting.md) (already live as "Approval Top-2" in **St. Louis**) to seed the finalists is a defensible fix. The repo-flavored footnote: **STAR needs no separate primary at all** — its 0–5 ballot does the [semifinal (top-two) and the final runoff in one pass](../../STAR_Voting/the_count/STAR_Automatic_Runoff.md), which is a different answer to the same "don't let a bad primary spoil a good final" concern.

### The ballot-data experiment

Fisher reports a real profile where "the Approval winner won by over 130 votes, but the Condorcet winner was a different candidate who won by a single vote, with 27 voters abstaining." That's a clean illustration of the repo's central theme — **[Approval measures breadth, Condorcet measures head-to-head preference, and they can name different winners](../../scores_and_ranks/preference_vs_support.md)** — and exactly the kind of divergence the [divergence ledger](../../../method_comparisons/divergence_review/INDEX.md) catalogs on this library's own elections.

## Better Choices vs. STAR — close cousins, real trade-offs

| | **STAR** | **Better Choices** (as described) |
|---|---|---|
| Ballot | Score each candidate 0–5 | Bubble a winner in each of the three head-to-head races |
| Tabulation | Add scores → top 2 → automatic pairwise runoff | Win both matchups → elected; else Minimax (least-bad-loss) |
| Family | Score / cardinal | Condorcet / ordinal (Minimax completion) |
| Condorcet winner | Elects it [very often](README.md), not guaranteed | Elects it **by construction** |
| Center squeeze | Avoids | Avoids |
| Intransitive ballot | Impossible (scores are a total order) | **Possible** (independent bubbles) |
| Expresses *strength* | Yes — 0–5 captures "love vs. tolerate" | No — each matchup is win/lose only |
| Primary needed? | No — one ballot does semifinal + final | Yes — Fisher argues it must be **Approval**, not Choose-One |
| Real-world status | Eugene measure lost 2024 (~64% no); used by [Equal Vote orgs](../advocacy_organizations.md) | Proposal; Approval Top-2 (a relative) live in St. Louis |

**The one-line difference:** Better Choices asks *which candidate you prefer* in each pair (ordinal, pairwise); STAR asks *how much you like each candidate* (cardinal, strength). Better Choices guarantees the Condorcet winner and gives a friendlier-looking ballot; STAR captures preference *strength* the pairwise bubbles throw away, and needs no primary. Whether the guarantee or the strength matters more is the real [scores-vs-ranks](../../scores_and_ranks/scores_vs_ranks.md) question, not a knockout either way.

## Bottom line

Better Choices is a **genuinely neat idea**: a Condorcet method that puts its own pairwise logic on the ballot in bubbles voters already understand. Its honest costs are that it discards preference *strength*, admits an intransitive ballot a ranking can't, and — like every Top-N system — lives or dies by the primary that feeds it (Fisher is right to want Approval there, not Choose-One). For this repo it's best filed as **Minimax-completed Condorcet with a novel front-end** — a cousin of [Ranked Robin](../../RCV_Ranked_Robin/ranked_robin.md) that differs only in the [cycle](../../RCV_Ranked_Robin/cycle_resolution.md), and a useful foil for the [scores-vs-ranks](../../scores_and_ranks/scores_vs_ranks.md) conversation. The single correction worth making to the post: at three candidates Minimax matches Ranked Pairs and Schulze, but **not** Copeland/Ranked Robin, which ties a three-cycle and breaks it separately.

---

*Source read for this page: Taylor Eigen Fisher, "[Better Choices Has a Neat Idea](https://eigentaylor.github.io/blog/better-choices/)" (eigentaylor.github.io), plus his linked [satisficing-voter simulations](https://eigentaylor.github.io/satisficing-voter-sim/). Fisher advocates Approval voting and discloses it; this repo advocates STAR and discloses that. Every tabulated claim above links to a re-runnable election. Glossary: [`Condorcet`](../../GLOSSARY.md) · [`Minimax`](../../RCV_Ranked_Robin/cycle_resolution.md).*
