# Alaska 2022 · 301 — every pathology, and is this fair?

*You've counted the rounds ([201](alaska_201.md)). This page does two harder things: (1) shows that Alaska hit **several** of IRV's known failures at once, and (2) confronts the honest question — **is it fair to keep pointing at IRV's failures, when a critic could construct STAR failures too?** The second half matters more than the first.*

Sources: Graham-Squire & McCune, [arXiv:2301.12075](https://arxiv.org/abs/2301.12075) (the empirical database this case is scaled from) · [what makes a good winner](../../00_start_here/topics/what_makes_a_good_winner.md) · run it: [the model](README.md).

---

## Part 1 — one election, four failures

Alaska is the most-cited real IRV misfire because it triggered several distinct pathologies in a single high-profile race. All four are reproducible in the [200-voter model](cases/bv2213_k3fmwv_alaska_2022.yaml).

**1. Condorcet failure.** Begich beats both rivals head-to-head (93–84 and 107–68) but isn't elected. The consensus candidate loses. *(This is the headline — see [201](alaska_201.md).)*

**2. Spoiler effect.** Remove the *losing* candidate Palin from the ballots entirely, and **Begich wins** (his voters plus Palin's transfers beat Peltola). Palin could not win — but her *presence* changed who did. That is the textbook definition of a [spoiler](../../00_start_here/topics/spoiler_effect.md), and RCV-IRV is marketed as the method that *ends* spoilers.

**3. Upward monotonicity failure.** Take the real result (Peltola wins) and give the **winner** *more* support: had ~6,000 Palin-only voters (≈6 in the model) instead ranked **Peltola first**, Peltola would have **lost**. Why? Those votes pull Palin below Begich in Round 1, so **Palin** is eliminated instead of Begich; Begich then beats Peltola head-to-head in the final. **Ranking the winner higher made the winner lose.** A voting method should never punish a candidate for gaining support — IRV can.

**4. Majoritarian failure (ballot exhaustion).** The winner's 96 votes are **48% of all 200 ballots** — a majority only of the 188 that survived after 12 exhausted. IRV's "majority winner" is a majority of *remaining* ballots, on a denominator quietly shrunk by truncated ballots.

*(The paper documents a fifth, the no-show / truncation paradox: some `Palin>Begich` voters would have gotten a better result by **not voting** at all. Same root cause — elimination order is fragile.)*

Every one of these traces to the **same** mechanism: **eliminating candidates on first-choice counts.** Methods that read the whole ballot — Ranked Robin, any [Condorcet method](../../00_start_here/topics/condorcet/), and STAR through its runoff — avoid all five, because none of them gate survival on first choices.

**Another way to see it — breadth of support.** Working the same Cast Vote Record, STAR's founder Mark Frohnmayer highlights a measure IRV never looks at: how many voters backed each candidate as *either* first **or** second choice. A **super-majority** of Alaskans put **Begich** in their top two; by contrast a **majority expressed no support at all** for Peltola, and a majority none for Palin. IRV eliminated the one candidate with broad support precisely because it counts only *first* choices each round and ignores every "backup" expression until a ballot's top choice is gone — the [preference-vs-support](../../00_start_here/scores_and_ranks/preference_vs_support.md) blind spot, live in a real election. *(Source: Frohnmayer, [What the heck happened in Alaska?](https://nardopolo.medium.com/what-the-heck-happened-in-alaska-3c2d7318decc) — a STAR-founder writeup, so **advocacy-leaning**, but its factual core matches the [Clelland](https://arxiv.org/abs/2303.00108) and [Graham-Squire & McCune](https://arxiv.org/abs/2301.12075) analyses this page is built on.)*

---

## Part 1½ — what if Alaska had used STAR or Approval? (Clelland's counterfactual)

The reduced model above *shows* STAR electing Begich. [Clelland (2023)](https://arxiv.org/abs/2303.00108) *proves* it, working the full Cast Vote Record by hand — and the comparison with Approval is the interesting part, because it isolates what STAR's **automatic runoff** actually buys you:

- **Under STAR, Begich almost certainly wins.** He's the Condorcet winner, and STAR's runoff floor (a second choice earns 1–4 stars, never 0) means his overwhelming second-place support carries him. Clelland's conclusion: *"Begich would almost certainly win the election"* under STAR, and Palin — the Condorcet **loser** — *"could not win this election under any circumstances"* (the runoff guarantees no Condorcet loser).
- **Under Approval, the outcome is indeterminate.** Her Table 5 shows the winner ranges across **all three candidates** depending on where voters set their approval threshold — it likely favors Peltola, but Begich is realistic, and it can't even structurally rule out the Condorcet *loser*, Palin.

Same score ballots; the whole difference is the runoff. STAR converts an indeterminate result into a **robust, Condorcet-friendly** one. (That's also why this case runs STAR and Ranked Robin but *not* a single Approval race — a lone Approval instance would fake a determinacy the method doesn't have. It's a virtue worth stating plainly, not a knock on Approval, which earns its keep on simplicity — see [choosing among the Equal Vote methods](../../00_start_here/topics/choosing_among_evc_methods.md).)

---

## Part 2 — is this fair? (the honest reckoning)

A fair critic should be squirming a little by now: *couldn't someone build a bad-looking STAR election too?* Yes. So here is how this library stays honest instead of just cheerleading.

### It is fair *because we say how rare it is*

The empirical finding of the very paper this case is built from: across **182 US RCV elections (2004–2022), exactly two** had a Condorcet failure — **Burlington 2009 and Alaska 2022.** So the honest claim is **not** "IRV fails all the time." It is:

> IRV usually works fine. But when it fails, it fails in one **specific, predictable, structural** way (center squeeze), and that has now happened in real, high-profile US elections.

Stating the rarity out loud is what separates teaching from propaganda — and it's *more* persuasive, because it's checkable. Explore the other 180 elections that worked fine on Equal Vote's [Real RCV](https://realrcv.equal.vote) tool; the failures are the exception, and that's exactly the point.

### It is fair *because the same test applies to both methods*

The library judges every claimed failure by a [four-part test](../paradoxes_and_whoops/reading_these_fairly.md). Apply it symmetrically:

| Test | IRV's center squeeze (Alaska) | STAR's usual "gotcha" (favorite betrayal) |
|---|---|---|
| **Structural?** (a whole region of electorates, not a knife-edge) | **Yes** — any center candidate between two wings | No — hand-tuned, knife-edge score margins |
| **Sincere?** (no strategy needed) | **Yes** — every ballot here is honest | No — requires voters to coordinate a betrayal |
| **Realistic?** (ordinary politics) | **Yes** — two wings + a bridge-builder | Rarely |
| **Really happened?** (a real election) | **Yes** — Alaska 2022, Burlington 2009 | Not observed in a real STAR election |

The fair conclusion isn't "STAR never fails." It's: **STAR's failures are contrived, strategic, and knife-edge; IRV's center squeeze is structural, sincere, and real.** A failure that needs a hand-built ballot and coordinated dishonesty is not the same animal as one that shows up in a US House race on honest ballots.

### It is fair *because STAR's real cost is conceded, openly*

STAR is **not** perfect, and this library says so on its own pages. STAR's genuine honest limit is the [runoff reversal](../../01_STAR/runoff_overturns_leader/README.md): a broadly-liked, high-average candidate can lose the automatic runoff to a *polarizing* candidate a bare majority ranks higher. That's a real philosophical cost (utility vs. majority), documented plainly in [STAR's Honest Limits](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md) — STAR is also not [Condorcet-compliant](../../00_start_here/STAR_Voting/properties_and_limits/STAR_honest_limits.md), not favorite-betrayal-proof, and gives up Later-No-Harm by design. Teaching Alaska *next to* those admissions is what makes the comparison trustworthy rather than a sales pitch.

### So how do you answer FairVote?

Not with "STAR is flawless" — that loses. With three moves:
1. **Concede** STAR's real limits up front (runoff reversal; not FBC-proof).
2. **Insist on the symmetric test** — is *your* STAR example structural and sincere and real, or a knife-edge construction? Alaska is the former; most anti-STAR examples are the latter.
3. **Cite the empirics** — center squeeze has shown up in real US elections; the STAR failure modes have not. Both methods beat Choose-One by a mile; the honest debate is between *good* options.

### Postscript — the same cast, six months later, and IRV got it *right*

The best evidence that this critique is fair comes from the very next election. In **November 2022**, the *same* three candidates ran again in the general — and this time RCV-IRV produced a perfectly good result. IRV again eliminated the centrist Begich early, but per Equal Vote's own [Real RCV analysis of the general](https://realrcv.equal.vote/alaska22general), **Peltola was the Condorcet winner this time** — the electorate had shifted, she'd have beaten both rivals head-to-head, and IRV elected her. **No Condorcet failure.**

That is the honest headline, and it *strengthens* the case rather than weakening it:

- IRV's failure is **conditional, not guaranteed.** The center-squeeze *mechanism* (eliminate the centrist on first choices) fired in both elections — but it only produces a *wrong* result when the eliminated centrist was actually the Condorcet winner. In August, Begich was; in November, he wasn't.
- So "IRV is broken" is the wrong claim. The right one: **IRV has a structural failure mode that triggers in a specific, identifiable configuration** (a genuine centrist Condorcet winner with few first choices) — and that configuration really occurred, in Alaska, in August 2022.
- This is exactly why we insist on stating **rarity**: of these *two* back-to-back Alaska races, **one** was a Condorcet failure, not both. A critic who claimed otherwise would be wrong, and we'd lose the argument. Precision is the whole game.

*(Equal Vote attributes the November shift to a larger, more left-leaning general electorate and an "electability bias" that moved from Palin — the best-known name in August — to Peltola, the incumbent by November.)*

**Run the counterpart:** the general is a [runnable model too](../alaska_2022_general/README.md) — same cast, but all four counts agree on Peltola. Put side by side, the pair *is* the fairness argument: one election where IRV failed the Condorcet winner, one where it elected them, same mechanism, opposite outcome.

---

## Challenge your understanding

<details><summary><strong>Q1.</strong> Explain the upward-monotonicity failure in your own words: how can giving Peltola *more* first-place votes make her lose?</summary>

Extra first-place votes for Peltola have to come from *somewhere* — here, from Palin-first voters switching. That drops **Palin** below Begich in Round 1, so Palin (not Begich) is eliminated first. Begich then survives to the final and **beats Peltola head-to-head**. The elimination *order* flipped, and the new order is bad for Peltola. IRV's outcome depends on fragile elimination order, so more support can backfire.
</details>

<details><summary><strong>Q2.</strong> A FairVote advocate shows you a STAR election where a voter benefits from dishonest scoring. Give the three-move response.</summary>

(1) **Concede** — yes, STAR isn't strategy-proof or favorite-betrayal-proof; no method with 3+ candidates is (Gibbard). (2) **Apply the symmetric test** — is your example *structural and sincere*, or a knife-edge that needs coordinated dishonesty? STAR's failures are typically the latter; Alaska's center squeeze is the former (structural, honest ballots). (3) **Cite the empirics** — center squeeze has occurred in real US elections; STAR's failure modes haven't been observed in one. The honest debate is between two good methods, both far better than Choose-One.
</details>

<details><summary><strong>Q3.</strong> Why is it *more* persuasive — not less — to admit that Condorcet failures are rare (2 in 182 elections)?</summary>

Because it's checkable and it targets the real claim. Overstating ("IRV always fails") is easy to refute and reads as propaganda. The true claim — "IRV usually works, but its failures are *structural and predictable*, and have hit real high-profile races" — survives scrutiny, and it reframes the argument as "why adopt a method with a known structural failure mode when STAR/Ranked Robin avoid it?" Rarity + predictability beats exaggeration.
</details>

<details><summary><strong>Q4.</strong> Name STAR's own honest costs. Why include them on a page criticizing IRV?</summary>

STAR is not Condorcet-compliant, not favorite-betrayal-proof, gives up Later-No-Harm by design, and has the *runoff reversal* (a high-average consensus candidate can lose to a polarizing bare-majority favorite). They belong here because a comparison that hides one side's costs isn't a comparison — it's advertising. Conceding STAR's limits is exactly what earns the Alaska critique its credibility.
</details>

<details><summary><strong>Q5.</strong> All four methods were run on the same electorate. Which failed the Condorcet winner, which didn't, and what single design choice separates the two groups?</summary>

**Failed:** Choose-One and RCV-IRV (both → Peltola). **Passed:** Ranked Robin and STAR (both → Begich). The dividing line is **whether the method eliminates/decides on *first choices only* (Plurality, IRV) or reads the *whole ballot* (Ranked Robin's head-to-heads, STAR's scores + runoff).** First-choice elimination is the step that squeezes out the consensus candidate.
</details>

<details><summary><strong>Q6.</strong> In the November general election, IRV again eliminated the centrist Begich — yet there was no Condorcet failure. Why not, and what does that teach us?</summary>

Because in the general the Condorcet winner was **Peltola**, not Begich — the electorate had shifted, and Peltola would beat both rivals head-to-head. IRV eliminating Begich no longer removed the "beats-everyone" candidate, so IRV's winner (Peltola) *was* the Condorcet winner. The lesson: the center-squeeze **mechanism** fires whenever a centrist has few first choices, but it only causes a **failure** when that centrist is the Condorcet winner. IRV's failure is conditional — which is exactly why we state its rarity precisely rather than claiming IRV is always wrong.
</details>

---

*Back to [the model & four counts](README.md) · [101](alaska_101.md) · [201](alaska_201.md) · the prose write-up with real vote totals: [RCV-IRV case study](../../00_start_here/RCV_IRV/case_studies/RCV_IRV_alaska_2022.md).*
