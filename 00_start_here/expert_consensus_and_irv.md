# Do the experts really think RCV-IRV is "bad"? — grading a common claim

*One of the most repeated arguments in electoral reform is that the **voting-science community** — mathematicians, game theorists, statisticians — is critical of instant-runoff voting (RCV-IRV) and favors **cardinal** methods (Approval, Score, STAR), while the general public wrongly treats RCV-IRV as the ultimate fix. This page takes that argument seriously and grades it: what's solidly true, what's overstated, and what it leaves out. It is **not** a verdict that RCV-IRV is "bad" — it's about how strong the popular version of the claim actually is.*

**Level: Voting 201 → 301.** Prerequisites: [What makes a "good" winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md) · [advocacy organizations](advocacy_organizations.md).

## The claim, in its forceful form

A common and confident version of the argument runs:

> The public thinks RCV-IRV is the ultimate election fix, but if you look at the academics and statisticians who actually *measure* these systems, the math proves RCV-IRV is mathematically flawed and inferior to other models — which is why the experts favor Approval, Score, and STAR instead.

It's usually backed by naming figures like **Warren Smith**, **Steven Brams**, and **Jameson Quinn** (bios at the bottom). There's a real pattern underneath this — and two moves in it that don't survive scrutiny.

## What's solidly true

- **RCV-IRV has genuine, provable flaws.** It fails **[monotonicity](STAR_Voting/STAR_monotonicity.md)** — ranking a candidate *higher* can, in constructed cases, cause them to *lose* — and it is prone to **[center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md)**: a broadly-acceptable middle candidate can be eliminated early for lacking first-place votes, even when a majority would prefer them head-to-head. These aren't rhetoric; they're theorems, with worked elections in this repo ([Brams's IRV pathologies](../method_comparisons/paradoxes_and_whoops/bv2159_f4cjpy_brams_irv_pathologies.md), the [center-squeeze set](../method_comparisons/center_squeeze/)). IRV also isn't **summable** — precincts can't report simple subtotals — which complicates auditing.
- **Simulation studies do tend to rank cardinal/hybrid methods above RCV-IRV.** Under **[VSE / Bayesian Regret](what_makes_a_good_winner.md#measuring-it-empirically-vse--bayesian-regret)** the ordering is consistently roughly **STAR ≳ Approval > RCV-IRV > Plurality**. That is a real, repeatable result and a legitimate point in cardinal methods' favor.
- **Many theorists genuinely do prefer cardinal methods.** The preference the claim describes is not invented — a substantial part of the social-choice and simulation community rates Approval/Score/STAR highly and is critical of IRV.

So the *core observation* — "the people who model these systems tend to be harder on IRV than the public is" — is largely fair.

## What's overstated or missing

**1. "The math *proves* it's inferior" is too strong.** The math proves *specific* failures (monotonicity, center squeeze). It does **not** prove overall inferiority, because there is no single scale of "better":

- **Arrow's and Gibbard–Satterthwaite's theorems** guarantee that *no* method satisfies every reasonable fairness criterion at once. "Best" is therefore always relative to *which* criteria you weight — a choice, not a proof. (RCV-IRV actually *satisfies* some criteria the cardinal methods fail; see below.)
- **VSE and Bayesian Regret are evidence under a model, not proof.** Every such result is conditional on the assumed voter model and on how strategically voters behave — this repo's own [simulation-models page](election_simulation_models.md) opens by insisting "*every conclusion is conditional on the model.*" Change the electorate model or the strategy assumption and the *middle* of the ranking can reshuffle. Robust as a trend; not a QED.
- **Utility itself is contested.** VSE scores a method by summed voter *utility* — but whether one person's "5" is comparable to another's "5" (interpersonal utility comparison) is a real, old objection to the whole cardinal-utilitarian framing. It's a genuine argument *for* ranked ballots that the "the math proves it" framing simply omits.

**2. The named "measurers" are also advocates.** This is the biggest omission. Presenting Smith, Brams, and Quinn as disinterested referees is misleading in the same way an appeal to FairVote would be:

- **Warren Smith** *founded* the [Center for Range Voting](https://rangevoting.org) — he is Score voting's leading advocate.
- **Steven Brams** is *the* best-known academic champion of **Approval** voting.
- **Jameson Quinn** was a board member of the **Center for Election Science** (the Approval advocacy group).

Their work is serious and worth engaging — but they are arguing *for* the methods their numbers favor, and the pro-IRV side (chiefly **FairVote**) produces its own favorable analyses. [Advocacy pages from every camp mix solid points with overreach](advocacy_organizations.md) — *including pro-STAR ones*. "Cite the experts" cuts in more than one direction.

**3. "Public vs. experts" is a loaded frame.** Cardinal advocates *are* experts; so are the political scientists who study RCV-IRV's adoption, legitimacy, and real-world effects and weigh things axiom-counting ignores (ballot familiarity, the simplicity of the majoritarian story, a large track record). It isn't science-vs-ignorance; it's **one expert camp vs. another**, plus a public that mostly knows only RCV-IRV because it has the *adoption momentum*, not because anyone proved it best.

## RCV-IRV's honest virtues (steelmanning the other side)

A fair page has to state what RCV-IRV does *well*, because the cardinal methods this repo favors don't:

- **Later-no-harm.** In RCV-IRV, ranking a second choice can never hurt your first choice. STAR, Approval, and Score **fail** this — a high score for your backup *can* help it beat your favorite in the runoff or tally. For many voters this is the intuitively "safe" property, and it's a real cost of the cardinal trade-off.
- **The majority criterion**, cleanly: a candidate who is the first choice of an outright majority always wins. (STAR meets this in spirit but has [subtler majority behavior](../01_STAR/majority_criterion/).)
- **Resistance to some strategies.** Because it reads rankings, RCV-IRV doesn't invite the score-inflation / "min-max" incentives that pull Score voting toward Approval under pressure.
- **A large real-world record**, which cardinal methods largely lack at government scale — an empirical, not axiomatic, point that legitimately matters to practitioners.
- **Monotonicity failures appear rare in realistic elections** — how rare is debated, but "it fails monotonicity" is a possibility result, not a claim that real IRV elections routinely misbehave.

None of this makes RCV-IRV *better* than STAR on the simulation metrics — it doesn't. It makes "experts have *proven* IRV inferior" the wrong summary of a genuine, criterion-dependent disagreement.

## The honest takeaway

Stated carefully, the defensible version is:

> On the metrics voting scientists most often use — axiomatic criteria like monotonicity and center-squeeze resistance, and simulated voter satisfaction (VSE) — **cardinal and hybrid methods (Approval, Score, STAR) tend to score better than RCV-IRV**, and much of the theory community prefers them. That's a real point in their favor. It is **not** a proof that RCV-IRV is "bad," because "better" depends on which criteria you value, the simulations are conditional on their models, and RCV-IRV satisfies things (later-no-harm, a clean majority guarantee) that the cardinal methods give up. The experts most cited for the claim are also advocates — as is the other side.

That's the version this repo will stand behind: STAR looks strong here, honestly — and we say *why the claim is strong* without borrowing certainty the math doesn't supply.

## The people named (accurately)

| Person | Background | What they contributed | Advocacy |
|---|---|---|---|
| **Warren D. Smith** | Ph.D. in applied math, Princeton | **Bayesian Regret** simulations; argued Score/Range outperforms RCV-IRV | Founder, **Center for Range Voting** (Score advocate) |
| **Steven Brams** | Game theorist, Professor of Politics, NYU | Co-author of *Approval Voting* (1983); many papers on RCV-IRV paradoxes incl. monotonicity | Leading academic **Approval** advocate |
| **Jameson Quinn** | Harvard-trained statistician | **Voter Satisfaction Efficiency (VSE)** — the modern simulation metric; modeling favorable to STAR/Approval | Former board member, **Center for Election Science** (Approval) |

Naming them is fair *evidence*; naming them as neutral *authorities* is the move to resist. Read their work, note their affiliations, and check the claims against countable elections — which is the whole method of this repo.

## Related

- [What makes a "good" winner?](what_makes_a_good_winner.md) · [What makes a voting method good?](what_makes_a_voting_method_good.md) — the criteria and the VSE framing
- [Election simulation models](election_simulation_models.md) — why every VSE number is conditional on its assumptions
- [Advocacy organizations](advocacy_organizations.md) — who champions what (every camp) · [FairVote's Condorcet article, claim-checked](topics/condorcet/fairvote_condorcet_claim_check.md) — the same even-handed check, in the other direction
- [STAR vs RCV-IRV](rcv_irv_vs_star.md) · [STAR's honest limits](STAR_Voting/STAR_honest_limits.md) — where this repo turns the candor on STAR
- IRV-specific behavior: [monotonicity](STAR_Voting/STAR_monotonicity.md) · [center squeeze](RCV_IRV/RCV_IRV_center_squeeze.md) · [exhausted ballots](RCV_IRV/RCV_IRV_exhausted_ballots.md)
