# Favorite Betrayal — Does *Only* RCV Avoid It?

*The claim, in its strongest form: RCV advocates say Ranked Choice is the only voting method where you never have to betray your favorite — and that STAR can force you to. This page pulls apart the two different promises that claim quietly fuses, shows RCV-IRV breaking the favorite-betrayal promise in a real, high-profile election, concedes honestly that STAR is not favorite-betrayal-proof either — and measures the difference instead of asserting it — then closes with the theorem that says no method can keep both promises at once. This is Voting 301: the hardest-to-keep-straight idea in the whole STAR-vs-RCV debate, so it goes slow and over-explains on purpose.*

→ Companions: [criteria at a glance (the full pass/fail map)](../criteria_at_a_glance.md) · [STAR's honest limits](STAR_honest_limits.md) · [RCV-IRV false-claims index](../RCV_IRV/rcv_irv_false_claims.md) · [are equal-score votes "discounted"? (the concede-then-reframe sibling)](are_equal_score_votes_discounted.md) · [residual vote-splitting](residual_vote_splitting.md)

---

If you only remember one thing:

> **"Favorite Betrayal" and "Later-No-Harm" are two DIFFERENT promises. RCV-IRV keeps the second one and breaks the first. People — including RCV advocates — mix them up constantly.**

## The claim being examined

In the deck [Why STAR Voting](../Why_STAR_Voting.md), Slide 4 is titled **"You Never Have to Betray Your Favorite,"** with bullets like *"Score both high — no forced ranking, no wasted vote"* and *"Honesty is your best ballot."*

The challenge to it runs: "This isn't *completely* true, right? And RCV-IRV proponents claim that **only** in IRV do you never betray your favorite, and that STAR *can* make you betray your favorite. Are they right?"

The short answer: the slide is true in the everyday, practical sense, and overstated only as a strict theorem. And the RCV-IRV claim is **false** — RCV-IRV does *not* protect you from favorite betrayal; it protects a *different* thing. Below is why, with numbers.

## Two promises that sound identical but aren't

Imagine you sincerely like **A (favorite) > B (compromise) > C (worst).**

### Promise A — Favorite Betrayal Criterion (FBC)

> *"It is always safe to support your favorite the most. You never get a better result by pretending someone else is your favorite."*

A method **passes FBC** if you can always put A at the top (rank 1, or score 5) without that choice ever backfiring. A method **fails FBC** if there are situations where you'd get a better outcome by *insincerely* ranking/scoring B above A — i.e., **betraying** your favorite A.

### Promise B — Later-No-Harm (LNH)

> *"Adding or raising a LOWER choice can never hurt your favorite."*

A method **passes [LNH](../GLOSSARY.md)** if marking B and C *at all* (after A) can never cause A to lose. It **fails LNH** if expressing support for your second choice can pull the win away from your first choice.

### The crucial difference

- **FBC is about your FIRST mark** — is it safe to put your favorite on top?
- **LNH is about your LATER marks** — is it safe to also support your backups?

They are not the same question, and — this is the punchline — **no voting method can satisfy both at once** (the theorem below). So every method has to give up at least one. RCV-IRV gives up FBC. Cardinal methods (Approval/Score) give up LNH.

## Why everyone conflates them

When an RCV advocate says *"in Ranked Choice you never have to betray your favorite,"* they are almost always describing the feeling of **Later-No-Harm**: "I can rank my favorite first AND rank my backups, and ranking the backups won't hurt my favorite." That part is true of RCV-IRV.

But "you never have to betray your favorite" is the **FBC** sentence, and RCV-IRV **fails** that one. The advocate has swapped a true LNH claim for a false FBC claim without noticing. The whole job of this page is to gently separate the two.

## Worked example: RCV-IRV *fails* favorite betrayal (Alaska 2022)

This is the cleanest real-world proof — [Alaska's August 2022 special election](../RCV_IRV/RCV_IRV_alaska_2022.md). Three candidates, roughly on a spectrum:

- **Peltola** (Democrat / left)
- **Begich** (Republican / center-right)
- **Palin** (Republican / right)

**Approximate first-choice tally:**

| Candidate | First choices |
|-----------|---------------|
| Peltola | ~40% |
| Palin | ~31% |
| Begich | ~29% |

**What RCV-IRV does:** Begich has the *fewest* first choices, so he's **eliminated first**. His ballots transfer (mostly to Palin, some to Peltola, some [exhausted](../RCV_IRV/exhausted_ballots_301.md)). In the final round **Peltola beats Palin ~51.5% to 48.5%.** Peltola wins.

**But look at the head-to-heads (who beats whom one-on-one):**

- Begich beats Peltola (~53–47).
- Begich beats Palin (~61–39).

So **Begich beats *both* others head-to-head — he's the candidate a majority actually preferred** (the [Condorcet winner](../topics/condorcet/README.md)). RCV-IRV eliminated him in the first round because few people ranked him *first*. That's the [**center squeeze**](../topics/center_squeeze/README.md).

**Now the favorite-betrayal part — the key move, read slowly:**

Take the **Palin voters.** They ranked Palin 1st (honest), Begich 2nd, Peltola last. By being honest:

- Begich (their 2nd choice) got eliminated,
- Palin (their 1st) then lost the final,
- so they ended up with **Peltola — their LAST choice.**

If *enough* of those Palin voters had **betrayed Palin** and ranked **Begich 1st** instead, Begich would not have been eliminated, and Begich would have **won** (he beats Peltola head-to-head). Begich is their 2nd choice — strictly better than Peltola, their 3rd.

> **Ranking their true favorite (Palin) first gave them their worst outcome. Betraying her gave them a better one. That is a favorite-betrayal failure — in a real, high-profile election.** RCV-IRV did exactly the thing its advocates say only it prevents.

(Burlington, Vermont 2009 is the same story with a left-leaning twist: Montroll was the head-to-head winner, eliminated early for too few first-place votes.)

## "But STAR fails FBC too!" — yes, and here's the honest difference

Concede it cleanly: **STAR is also not formally FBC-compliant.** Equal Vote's criteria chart — the STAR campaign's own scorecard, so here it's conceding a point against interest — marks STAR ❌ on Favorite Betrayal. It's a *binary* pass/fail, with **no percentage attached.** (You may have seen "~98%" quoted, including in earlier drafts of this repo. That figure has **no FBC source** — it was borrowed from STAR's *accuracy* score, [Voter Satisfaction Efficiency](../strategic_voting.md) ~91–98%, which measures something else entirely. Don't use it.)

So instead of quoting a number we can't defend, we **measured** FBC directly — see [`fbc_simulation.py`](../../06_Other/simulations/fbc_simulation.py) (writeup: [simulations README](../../06_Other/simulations/README.md)), which brute-forces every voter's best favorite-betrayal across thousands of random elections. Two honest results:

- **On raw frequency, neither method is FBC-proof — and STAR is *not* better than RCV-IRV.** Under a realistic spatial model STAR is FBC-compliant in ~92–96% of elections and RCV-IRV in ~95–97% — essentially a tie, IRV slightly ahead. (FBC is an *existence* test, and STAR's score ballot simply offers far more betrayal ballots in which to find one that helps.) So *"STAR fails FBC less often than IRV"* is **not** a claim the numbers support — drop it.
- **The real, measurable difference is whether betrayal ever pays.** Of the favorite-betrayals that actually change who wins, only **~2% help the voter under STAR** — the other ~98% backfire — versus **~7–12% under RCV-IRV.** Betrayal is several times more likely to pay off in IRV, and STAR's rare wins need extreme ballots plus near-perfect knowledge of everyone else's vote. *That* is the only defensible "98%": not "FBC-compliant 98% of the time," but **"favorite betrayal backfires ~98% of the time you'd try it."**

**Where STAR's FBC leak comes from — the runoff.**

- **Pure Score voting PASSES FBC.** You can always give your favorite a 5; since the winner is just the highest total, maxing your favorite can never hurt you.
- But pure Score has a different weakness: **exaggeration** ("I'll give my favorite 5 and everyone else 0 to inflate them"). That distorts results.
- **STAR adds the [Automatic Runoff](STAR_Automatic_Runoff.md) to neutralize that exaggeration.** And it works — but the runoff is *also* what introduces the sliver of FBC vulnerability, because now your scores can change *which two candidates are finalists*, and in rare, delicately balanced cases moving your favorite's score can change the finalist pairing in a way that helps you. (The same top-two bottleneck, seen as vote-splitting instead of betrayal, is [residual vote-splitting](residual_vote_splitting.md).)

So STAR's FBC leak is a **deliberate trade**: it gives up a sliver of FBC to buy a genuine majority finish and immunity to score-exaggeration.

**Why the two failures aren't the same animal** (this, not frequency, is the point):

- STAR's failures are **fragile and unactionable** — extreme ballots, perfect information, and a betrayal that backfires ~98% of the time you'd try it. They essentially don't occur in real elections.
- RCV-IRV's failure is **systematic and predictable** — the *center squeeze* — and it bites in exactly the competitive 3-viable-candidate races reform is meant to fix, where a squeezed wing can often see it coming (Alaska, Burlington).

> **One-liner:** *"Neither of us is favorite-betrayal-proof — on paper we fail about equally often. The difference: in STAR the betrayal backfires almost every time you'd try it; your center-squeeze failure is predictable enough that a whole wing has a reason to betray."*

## The theorem that ends the argument: you can't have both

**Favorite-Betrayal and Later-No-Harm are provably incompatible.** No deterministic ranked or rated method can satisfy both at the same time. (Woodall-style impossibility; the synced deck states it as *"Many criteria are mutually exclusive, including 'Favorite Betrayal' and 'Later No Harm.'"*)

So *every* method must give up at least one:

| Method | Favorite Betrayal (safe to top your favorite?) | Later-No-Harm (safe to mark backups?) |
|--------|:---:|:---:|
| Choose-One Plurality | ❌ | n/a (only one mark) |
| **RCV-IRV** | **❌** (center squeeze) | ✅ |
| Approval | ✅ | ❌ |
| Score | ✅ | ❌ |
| **STAR** | ❌ rare — and betrayal backfires ~98% of the time it's tried | ❌ rare |

Read across the STAR row: it commits to neither criterion fully, accepting rare failures of *each* in exchange for a majority-backed, exaggeration-resistant result. The payoff isn't that STAR passes FBC more often than RCV-IRV (it doesn't — see the [simulation](../../06_Other/simulations/README.md)) — it's that in STAR a favorite-betrayal almost never pays off, so honesty stays your safest ballot. (This row pair sits inside the wider [criteria-at-a-glance](../criteria_at_a_glance.md) map.)

**The reframe to leave them with:** Later-No-Harm sounds nice, but it's the very property that *forces* center squeeze — guaranteeing your later choices never help your favorite is mathematically the same as guaranteeing a broadly-liked compromise can't be rescued by being everyone's strong second. STAR gives that up on purpose, because "your honest support for a compromise should be allowed to help elect them" is the *better* value.

## A mental model to hold onto

- **Favorite Betrayal** = *the front door.* Is it safe to walk your favorite in first? (RCV-IRV: no. Score/Approval: yes. STAR: almost always.)
- **Later-No-Harm** = *the back door.* Is it safe to let your backups in too? (RCV-IRV: yes. Score/Approval: no. STAR: almost always.)
- You **cannot** lock both doors. RCV-IRV locks the back and leaves the front open (center squeeze). STAR keeps both *mostly* shut and refuses to fully sacrifice either — and the front-door failures it does have almost never reward the burglar.

## The takeaway

"Only RCV avoids favorite betrayal" swaps a true Later-No-Harm statement for a false Favorite-Betrayal one. RCV-IRV fails favorite betrayal in the most consequential way possible — predictably, via center squeeze, in real elections like Alaska 2022 and Burlington 2009. STAR fails it too, about as often on paper, but its failures are lab constructions in which the betrayal backfires ~98% of the time it's tried — so honesty stays your safest ballot. And since no method can keep both promises, the real question isn't "who passes?" but "which promise is worth keeping?" — STAR trades Later-No-Harm away on purpose, so your honest support for a compromise is allowed to help elect them. <!-- terminology-ok: quotes the advocates' loose "RCV" -->

---

## Where this fits in the teaching

This is **Voting 301 objection-handling material** — don't open with it. Raise it only when an RCV advocate makes the "only RCV avoids favorite betrayal" claim; with a general audience, Slide 4 stands on its own. When you do deploy it: **lead by separating the two criteria** before you argue (half the disagreement evaporates once "first mark" vs "later marks" is on the table); **concede STAR fails FBC too — immediately, and without a percentage** (say "betrayal almost always backfires in STAR," not "STAR is 98% compliant" — your candor is the credibility that makes the center-squeeze point land); and **end on the value, not the math** (Later-No-Harm *causes* center squeeze; STAR trades it away so a consensus candidate can actually win). <!-- terminology-ok: quotes the advocates' loose "RCV" -->

The page defends **Slide 4** of [Why STAR Voting](../Why_STAR_Voting.md) and its Part 2 talking point **#12**. Presenters: the matching slides are indexed by short name in [LINKS.md](../LINKS.md) — **Full Deck 2025** ("RCV Common False Claims", "Alaska '22", "Burlington 2009", the pass/fail criteria slides) and **Why STAR 2** — and the episode roadmap (this is episode 12) lives in [conversation scripts](../conversation_scripts.md).
