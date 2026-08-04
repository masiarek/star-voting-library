# The weak Condorcet loser — the candidate who beats nobody

*A **Condorcet loser** loses every head-to-head. A **weak Condorcet loser** is the ties-allowed version: they lose **or tie** every head-to-head — equivalently, **they beat nobody.** The gap between the two is exactly one pairwise tie, and that single word "or ties" is the difference between a criterion **STAR passes** and one it **fails**. This page defines the term and then shows it happening, on five voters you can re-run, across STAR, Ranked Robin, Approval, RCV-IRV and Plurality.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/c73pfw) · **[results ↗](https://bettervoting.com/c73pfw/results)** (election `c73pfw`, BV2249) — one election, **three races** on these same five voters: STAR, Approval, and Ranked Robin.

→ Sibling: [the Condorcet loser paradox](../../07_Concepts/voting_paradoxes/condorcet_loser_paradox.md) (the strict version, and a method electing one anyway) · [Condorcet topic hub](../../07_Concepts/topics/condorcet/README.md) · [criteria at a glance](../../07_Concepts/topics/criteria_at_a_glance.md) · Glossary: [`weak Condorcet winner / weak Condorcet loser`](../../07_Concepts/GLOSSARY.md).

---

## The definition, and the two things that surprise people

| | Beats | Ties | Loses |
|---|---|---|---|
| **Condorcet loser** (strict) | nobody | nobody | **everybody** |
| **Weak Condorcet loser** | nobody | some | the rest |

**1. A weak Condorcet loser need not be unique.** A strict Condorcet loser is alone by definition — two candidates can't each lose to the other. But two candidates who *tie each other* and lose to everyone else are **both** weak Condorcet losers. That happens in the election below, and it is what makes the failure unavoidable there.

**2. In a total pairwise tie, everyone is both a weak Condorcet winner and a weak Condorcet loser.** If every matchup is a dead heat, every candidate is unbeaten (weak winner) *and* beats nobody (weak loser). The two categories are not opposites; they're both "boundary" conditions and they can overlap.

Every strict Condorcet loser is also a weak one. The converse fails — which is why the **weak** criterion ("never elect a candidate who beats nobody") is *strictly stronger* than the familiar Condorcet-loser criterion, and why methods that pass the familiar one can still fail this.

## The election

Five voters, three candidates — **Ada**, **Ben**, **Cora**. Ada is polarizing: three voters give her a 5, two give her a 0. Ben and Cora are the broadly-acceptable middle.

| Voter | Ada | Ben | Cora | reads as |
|---|:--:|:--:|:--:|---|
| 1 | 5 | 4 | 4 | loves Ada; Ben and Cora equally fine |
| 2 | 5 | 4 | 1 | loves Ada, tolerates Ben, dislikes Cora |
| 3 | 5 | 4 | 3 | loves Ada, tolerates both others |
| 4 | 0 | 3 | 4 | rejects Ada, prefers Cora |
| 5 | 0 | 3 | 4 | rejects Ada, prefers Cora |

**The pairwise facts** — read them off the round-robin, they are the whole basis of the page:

```
   Ada   beats Ben    3 – 2
   Ada   beats Cora   3 – 2
   Ben   ties  Cora   2 – 2
```

So **Ada is the Condorcet winner**, and **Ben and Cora each beat nobody** — both are weak Condorcet losers. Neither is a *strict* Condorcet loser, because neither loses to the other; they tie.

## What each method does

| Method | Winner | Elects a weak Condorcet loser? |
|---|:--:|:--:|
| **Ranked Robin** (Condorcet) | **Ada** | ✅ no |
| **RCV-IRV** | **Ada** | ✅ no |
| **Plurality** | **Ada** | ✅ no |
| **STAR** | **Ben** | ⚠️ **yes** |
| **Approval** | **Ben** | ⚠️ **yes** |

Runnable: [`wcl_c3_b5_star.yaml`](cases/wcl_c3_b5_star.yaml) · [`wcl_c3_b5_approval.yaml`](cases/wcl_c3_b5_approval.yaml). Full reports: [STAR](cases/cases_pages/wcl_c3_b5_star.md) · [Approval](cases/cases_pages/wcl_c3_b5_approval.md).

### Ranked Robin — it's right there in the report

Ranked Robin ranks by win count, and a weak Condorcet loser has **zero wins**. The engine prints the signature directly — look at the `Beats` column:

```
Win–loss record — Copeland score = wins + ½·ties
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–0–0         2      +2  Ben, Cora
    2  Ben        0–1–1       0.5      -1  —
    3  Cora       0–1–1       0.5      -1  —

Winner — Ranked Robin (RCV-RR): Ada
   beats every opponent head-to-head — the Condorcet winner.
```

**`Beats: —` is the weak-Condorcet-loser marker.** That is what the term looks like in practice: a candidate whose "beats" list is empty, even though their record isn't all losses.

And it gives Ranked Robin a clean guarantee: since RR elects the candidate with the most wins, it can only elect a zero-win candidate when **every** candidate has zero wins — the total-tie case from point 2 above, where the distinction has collapsed anyway. Outside that degenerate case, **Ranked Robin never elects a weak Condorcet loser.** It's the strongest record any method here has on this criterion, and it follows directly from counting wins rather than points.

### STAR — the tie is the loophole

--8<-- "method_comparisons/weak_condorcet_loser/cases/cases_pages/wcl_c3_b5_star.md:report"
Two things had to go wrong together, and both are visible above.

**The Condorcet winner was eliminated in the scoring round.** Ada's 5/5/5/0/0 profile totals 15 — less than either moderate. That part is ordinary STAR behavior and has its own page ([three notions of "winner"](../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md)).

**Then the runoff tied.** One voter scored Ben and Cora both 4 — [Equal Support](../../07_Concepts/GLOSSARY.md) — leaving 2 vs 2 among the voters with a preference. STAR's first tiebreaker is the higher score, and Ben takes it.

Here is the precise reason this is a **weak**-only failure, and it's worth stating carefully because it's the sharpest thing on this page:

> A **strict** Condorcet loser loses to *every* candidate, including whichever finalist they face — so they lose the runoff, always. **STAR can never elect a strict Condorcet loser.** A **weak** one slips through because *a tie is not a loss*: the runoff doesn't resolve, control passes to the tiebreaker, and the tiebreaker is a score comparison that knows nothing about pairwise records.

And in this election STAR had no way out: **both finalists beat nobody**, so whichever won the tiebreak was going to be a weak Condorcet loser. The scoring round, not the runoff, is where the outcome was decided.

This refines a claim made elsewhere in this library — that "STAR's runoff buys back Condorcet-loser protection that plain Score voting lacks." True, and it stays true. It just buys the **strict** guarantee, not the weak one.

### Approval — it can't even see the problem

Approval elects Ben 5–4–3, on the same voters approving everyone they scored 3 or higher.

But the interesting part isn't the scoreboard. Run the pairwise comparison on the **approval ballots alone** and **Ben beats Ada 2–0** — because three voters approved both, and a yes/no ballot records that as a tie. Coarsening 0–5 down to 0–1 destroyed the very margins (`Ada 5, Ben 4`) that made Ada the Condorcet winner in the first place.

So Approval doesn't so much *choose* the weak Condorcet loser as **lose the information that would have identified one**. That's a [preference-vs-support](../../07_Concepts/scores_and_ranks/preference_vs_support.md) point, not a scoreboard point — and it's the same fragility the [approval-cutoff sweep](../star_vs_approval_divergence.md) measures from the other direction. A different cutoff gives a different election; that ambiguity is Approval's standing caveat, not a quirk of this case.

### RCV-IRV and Plurality — right answer, unrelated reason

Ada is the first choice of three of five voters — an outright majority — so Plurality elects her immediately and IRV never reaches a second round. Both dodge the weak Condorcet loser here, but neither is *protecting* against one; they simply happen to agree with the pairwise winner because she leads on first choices. Change the profile so Ada is many voters' second choice instead of their first and IRV squeezes her out ([center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md)) — which is the far more common real-world failure.

*(One engine note, carried honestly: voter 1 scored Ben and Cora equally, so converting that ballot to a strict ranking required a tiebreak, and the engine flags it. It doesn't affect these winners — Ada leads first choices 3–2 no matter how that one tie is ordered, and Ada's 2–0 pairwise record is likewise untouched — but it is exactly the [strict-vs-weak ranks](../../07_Concepts/scores_and_ranks/strict_vs_weak_ranks.md) problem: most IRV rules cannot record "these two are equal.")*

## Cross-checked against BetterVoting

The case is live as **BV2249** (`c73pfw`), and BetterVoting's independent tabulator agrees with the LH engine on **all three races** — winners, scores, and Copeland records. Two details in BV's own export are worth pulling out, because they corroborate this page rather than merely matching it:

**BV records *which rung* broke the tie.** The STAR race's result carries `tieBreakType: "score"` — exactly the LH ladder's *Runoff 1* rung (higher total score). That matters for reproducibility: LH and BetterVoting [differ at only two rungs](../../01_STAR/01_Learn/Tie_Breaking_STAR/tie_breaking.md#lh-vs-bettervoting-where-the-two-star-ladders-differ), the 3-way scoring tie and the terminal floor, where BV shuffles **randomly** and a result can't be frozen. This election resolves well above that floor, so its winner is a function of the ballots in both engines — unlike a case that ties all the way down, which has to stay LH-only.

**BV's own data says Ben beats nobody.** Each candidate in the export carries a `winsAgainst` map. In the STAR race, Ben's and Cora's are all `false` while Ada's are `true, true` — BetterVoting is independently publishing the weak-Condorcet-loser fact this page is built on. The Ranked Robin race prints it as Copeland scores: Ada **2**, Ben **0.5**, Cora **0.5** — the halves being ties, not wins.

**And the Approval race confirms the ballot-blindness point.** In *that* race BV computes `winsAgainst` from the **approval** ballots — where Ben `winsAgainst` Ada is **`true`**. Same voters, same election, opposite pairwise verdict, purely because the yes/no ballot cannot record `Ada 5, Ben 4`. That is the "Approval can't even see the problem" claim above, verified by an engine that isn't ours.

## Reading this fairly

**This is a possibility result, not a warning.** It needs an exact pairwise tie between the two finalists. Ties get rarer fast as the electorate grows — in any real public election with thousands of ballots, an exact 2–2-style deadlock between the top two is vanishingly unlikely. What this election proves is that STAR **fails the weak Condorcet loser criterion**, which is a statement about guarantees, not about frequency. The [severity × frequency](../paradoxes_and_whoops/reading_these_fairly.md) rule applies: state both, and never quote the failure without the rarity.

**It also cuts against the methods this library likes**, which is the point of keeping it. STAR and Approval fail; Ranked Robin passes cleanly and RCV-IRV passes here. If the scorecard only ever came out one way it wouldn't be worth having.

**And it doesn't move the headline comparison.** STAR's Condorcet-loser guarantee — the one people actually invoke — is the strict one, and it holds absolutely. This is the boundary case where the guarantee's fine print shows.

## See also

- [The Condorcet loser paradox](../../07_Concepts/voting_paradoxes/condorcet_loser_paradox.md) — the strict version, worked on 7 voters
- [Three notions of "winner"](../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md) — why the Condorcet winner can miss STAR's runoff
- [The Smith set](../../07_Concepts/topics/smith_set.md) — the generalized Condorcet winner; a Condorcet loser is never in it
- [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) · [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) — ties and cycles are different things
- [Criteria at a glance](../../07_Concepts/topics/criteria_at_a_glance.md) · [STAR's criteria failures](../../01_STAR/01_Learn/properties_and_limits/star_criteria_failures.md)
- [Reading these fairly](../paradoxes_and_whoops/reading_these_fairly.md)
