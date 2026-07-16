# Favorite Betrayal — Does *Only* RCV Avoid It?
### Voting 301 · advanced · the deep-dive behind Slide 4

This is the hardest-to-keep-straight idea in the whole STAR-vs-RCV debate, so this file goes slow and over-explains on purpose. If you only remember one thing:

> **"Favorite Betrayal" and "Later-No-Harm" are two DIFFERENT promises. RCV-IRV keeps the second one and breaks the first. People — including RCV advocates — mix them up constantly.**

**The 30-second intuition** — think of **two doors** (the full version is §9):

- 🚪 **Favorite Betrayal = the front door.** *Is it safe to walk your favorite in **first**?* In RCV-IRV, sometimes **no** — your favorite can be knocked out early for having too few first-place votes. In STAR, almost always yes.
- 🚪 **Later-No-Harm = the back door.** *Is it safe to let your **backups** in too?* In RCV-IRV, yes. In Score/Approval, no. In STAR, almost always yes.

RCV advocates say *"you never have to betray your favorite"* — that's the **front-door** promise — but what they're really describing is the **back door** (Later-No-Harm). RCV-IRV locks the back and leaves the front open. **That swap is the entire lesson; everything below is the proof.**

---

## 1. The context — what was actually challenged

**The slide.** In the deck [`Why_STAR_Voting.md`](../../topics/Why_STAR_Voting.md), **Slide 4** is titled **"You Never Have to Betray Your Favorite,"** with bullets like *"Score both high — no forced ranking, no wasted vote"* and *"Honesty is your best ballot."*

**The challenge to the slide.** *"Isn't this overstated? RCV-IRV proponents claim that **only** in IRV do you never betray your favorite, and that STAR *can* make you betray your favorite. Are they right?"*

**The short answer.** The slide is true in the everyday, practical sense, and overstated only as a strict theorem. And the RCV-IRV claim is **false** — RCV-IRV does *not* protect you from favorite betrayal; it protects a *different* thing. Below is why, with numbers.

---

## 2. Two promises that sound identical but aren't

Imagine you sincerely like **A (favorite) > B (compromise) > C (worst).**

### Promise A — Favorite Betrayal Criterion (FBC)
> *"It is always safe to support your favorite the most. You never get a better result by pretending someone else is your favorite."*

A method **passes FBC** if you can always put A at the top (rank 1, or score 5) without that choice ever backfiring. A method **fails FBC** if there are situations where you'd get a better outcome by *insincerely* ranking/scoring B above A — i.e., **betraying** your favorite A.

### Promise B — Later-No-Harm (LNH)
> *"Adding or raising a LOWER choice can never hurt your favorite."*

A method **passes LNH** if marking B and C *at all* (after A) can never cause A to lose. It **fails LNH** if expressing support for your second choice can pull the win away from your first choice.

### The crucial difference
- **FBC is about your FIRST mark** — is it safe to put your favorite on top?
- **LNH is about your LATER marks** — is it safe to also support your backups?

They are not the same question, and — this is the punchline — **no voting method can satisfy both at once** (Section 6). So every method has to give up at least one. RCV-IRV gives up FBC. Cardinal methods (Approval/Score) give up LNH.

---

## 3. Why everyone conflates them

When an RCV advocate says *"in Ranked Choice you never have to betray your favorite,"* they are almost always describing the feeling of **Later-No-Harm**: "I can rank my favorite first AND rank my backups, and ranking the backups won't hurt my favorite." That part is true of RCV-IRV.

But "you never have to betray your favorite" is the **FBC** sentence, and RCV-IRV **fails** that one. The advocate has swapped a true LNH claim for a false FBC claim without noticing. Your job in a debate is to gently separate the two.

---

## 4. Worked example: RCV-IRV *fails* favorite betrayal (Alaska 2022)

This is the cleanest real-world proof. Three candidates, roughly on a spectrum:

- **Peltola** (Democrat / left)
- **Begich** (Republican / center-right)
- **Palin** (Republican / right)

**Approximate first-choice tally:**

| Candidate | First choices |
|-----------|---------------|
| Peltola | ~40% |
| Palin | ~31% |
| Begich | ~29% |

**What RCV-IRV does:** Begich has the *fewest* first choices, so he's **eliminated first**. His ballots transfer (mostly to Palin, some to Peltola, some [exhausted](../../RCV_IRV/exhausted_ballots_301.md)). In the final round **Peltola beats Palin ~51.5% to 48.5%.** Peltola wins.

**But look at the head-to-heads (who beats whom one-on-one):**
- Begich beats Peltola (~53–47).
- Begich beats Palin (~61–39).

So **Begich beats *both* others head-to-head — he's the candidate a majority actually preferred** (the [Condorcet winner](../../topics/condorcet/)). RCV-IRV eliminated him in the first round because few people ranked him *first*. That's the **[center squeeze](../../topics/center_squeeze/).**

**Now the favorite-betrayal part — the key move, read slowly:**

Take the **Palin voters.** They ranked Palin 1st (honest), Begich 2nd, Peltola last. By being honest:
- Begich (their 2nd choice) got eliminated,
- Palin (their 1st) then lost the final,
- so they ended up with **Peltola — their LAST choice.**

If *enough* of those Palin voters had **betrayed Palin** and ranked **Begich 1st** instead, Begich would not have been eliminated, and Begich would have **won** (he beats Peltola head-to-head). Begich is their 2nd choice — strictly better than Peltola, their 3rd.

> **Ranking their true favorite (Palin) first gave them their worst outcome. Betraying her gave them a better one. That is a favorite-betrayal failure — in a real, high-profile election.** RCV-IRV did exactly the thing its advocates say only it prevents.

(Burlington, Vermont 2009 is the same story with a left-leaning twist: Montroll was the head-to-head winner, eliminated early for too few first-place votes.)

---

## 5. "But you admit STAR fails FBC too!" — yes, and here's the honest difference

Concede it cleanly: **STAR is also not formally FBC-compliant.** Equal Vote's criteria chart marks STAR ❌ on Favorite Betrayal — it's a *binary* pass/fail, with **no percentage attached.** (You may have seen "~98%" quoted, including in earlier drafts of this repo. That figure has **no FBC source** — it was borrowed from STAR's *accuracy* score, Voter Satisfaction Efficiency ~91–98%, which measures something else entirely. Don't use it.)

So instead of quoting a number we can't defend, we **measured** FBC directly — see `06_Other/simulations/fbc_simulation.py`, which brute-forces every voter's best favorite-betrayal across thousands of random elections. Two honest results:

- **On raw frequency, neither method is FBC-proof — and STAR is *not* better than RCV-IRV.** Under a realistic spatial model STAR is FBC-compliant in ~92–96% of elections and RCV-IRV in ~95–97% — essentially a tie, IRV slightly ahead. (FBC is an *existence* test, and STAR's score ballot simply offers far more betrayal ballots in which to find one that helps.) So *"STAR fails FBC less often than IRV"* is **not** a claim the numbers support — drop it.
- **The real, measurable difference is whether betrayal ever pays.** Of the favorite-betrayals that actually change who wins, only **~2% help the voter under STAR** — the other ~98% backfire — versus **~7–12% under RCV-IRV.** Betrayal is several times more likely to pay off in IRV, and STAR's rare wins need extreme ballots plus near-perfect knowledge of everyone else's vote. *That* is the only defensible "98%": not "FBC-compliant 98% of the time," but **"favorite betrayal backfires ~98% of the time you'd try it."**

**Where STAR's FBC leak comes from — the runoff.**
- **Pure Score voting PASSES FBC.** You can always give your favorite a 5; since the winner is just the highest total, maxing your favorite can never hurt you.
- But pure Score has a different weakness: **exaggeration** ("I'll give my favorite 5 and everyone else 0 to inflate them"). That distorts results.
- **STAR adds the automatic runoff to neutralize that exaggeration.** And it works — but the runoff is *also* what introduces the sliver of FBC vulnerability, because now your scores can change *which two candidates are finalists*, and in rare, delicately balanced cases moving your favorite's score can change the finalist pairing in a way that helps you.

So STAR's FBC leak is a **deliberate trade**: it gives up a sliver of FBC to buy a genuine majority finish and immunity to score-exaggeration.

**Why the two failures aren't the same animal** (this, not frequency, is the point):
- STAR's failures are **fragile and unactionable** — extreme ballots, perfect information, and a betrayal that backfires ~98% of the time you'd try it. They essentially don't occur in real elections.
- RCV-IRV's failure is **systematic and predictable** — the *center squeeze* — and it bites in exactly the competitive 3-viable-candidate races reform is meant to fix, where a squeezed wing can often see it coming (Alaska, Burlington).

> **One-liner:** *"Neither of us is favorite-betrayal-proof — on paper we fail about equally often. The difference: in STAR the betrayal backfires almost every time you'd try it; your center-squeeze failure is predictable enough that a whole wing has a reason to betray."*

---

## 6. The theorem that ends the argument: you can't have both

**Favorite-Betrayal and Later-No-Harm are provably incompatible.** No deterministic ranked or rated method can satisfy both at the same time. (Woodall-style impossibility; the synced deck states it as *"Many criteria are mutually exclusive, including 'Favorite Betrayal' and 'Later No Harm.'"*)

So *every* method must give up at least one:

| Method | Favorite Betrayal (safe to top your favorite?) | Later-No-Harm (safe to mark backups?) |
|--------|:---:|:---:|
| Choose-One Plurality | ❌ | n/a (only one mark) |
| **RCV-IRV** | **❌** (center squeeze) | ✅ |
| Approval | ✅ | ❌ |
| Score | ✅ | ❌ |
| **STAR** | ❌ rare — and betrayal backfires ~98% of the time it's tried | ❌ rare |

Read across the STAR row: it commits to neither criterion fully, accepting rare failures of *each* in exchange for a majority-backed, exaggeration-resistant result. The payoff isn't that STAR passes FBC more often than RCV-IRV (it doesn't — see `06_Other/simulations/`) — it's that in STAR a favorite-betrayal almost never pays off, so honesty stays your safest ballot.

**The reframe to leave them with:** Later-No-Harm sounds nice, but it's the very property that *forces* center squeeze — guaranteeing your later choices never help your favorite is mathematically the same as guaranteeing a broadly-liked compromise can't be rescued by being everyone's strong second. STAR gives that up on purpose, because "your honest support for a compromise should be allowed to help elect them" is the *better* value.

---

## 7. The debate — an RCV advocate vs a STAR advocate

The claim in the wild is rarely a calm question; it's an argument. So here's the same lesson as the confrontation you'll actually have — the **RCV advocate** making the strongest version of the case, the **STAR advocate** separating the two criteria and conceding what's true.

**RCV Advocate:** In Ranked Choice you never have to betray your favorite. Rank the person you love first, add your backups below, done — and supporting those backups can't hurt your favorite. STAR can't promise that.

**STAR Advocate:** You've just folded two different promises into one, and that's where this whole argument goes wrong. *"Is it safe to rank my favorite **first**?"* is one criterion — Favorite Betrayal. *"Is it safe to **also** mark my backups?"* is a completely different one — Later-No-Harm. RCV-IRV keeps the second promise. It does **not** keep the first.

**RCV Advocate:** That's a distinction without a difference. If marking my backups never hurts my favorite, my favorite is safe. What more is there?

**STAR Advocate:** The two come apart in real elections. "My backups don't hurt my favorite" says nothing about whether *ranking my favorite first* was safe in the first place — because in RCV-IRV your favorite can be eliminated for having too few first-place votes before your backups ever get counted.

**RCV Advocate:** When has that actually happened?

**STAR Advocate:** Alaska, 2022. Begich beat *both* other candidates head-to-head — a majority preferred him to Peltola, and a majority preferred him to Palin. But he had the fewest *first* choices, so IRV eliminated him in the very first round. Honest Palin voters — Palin first, Begich second, Peltola last — watched their second choice get cut, then their first lose the final, and ended up with Peltola: their *last* choice.

**RCV Advocate:** …and you're going to tell me ranking Begich first would have fixed that.

**STAR Advocate:** It would. Begich survives the first round and wins — he beats Peltola head-to-head. Those voters get their second choice instead of their last. Ranking their *true* favorite first is the thing that hurt them. That is a favorite-betrayal failure, in a real, high-profile race, in the system you just told me is the only one that prevents it.

**RCV Advocate:** Fine — but you can't sit there and claim STAR is favorite-betrayal-*proof*. It isn't. Your own criteria chart marks STAR ❌ on Favorite Betrayal.

**STAR Advocate:** Correct, and I won't pretend otherwise: STAR is **not** formally FBC-compliant. On raw frequency we fail it about as often as you do — some simulations put IRV slightly ahead. And I'm not going to quote you a "98% compliant" figure, because that number doesn't exist; it was borrowed from a different metric and it's wrong.

**RCV Advocate:** Then what exactly is your advantage?

**STAR Advocate:** Whether the betrayal ever *pays*. We measured it directly. Of the favorite-betrayals in STAR that would actually change the winner, about **98% backfire** — you'd hurt yourself trying. Only ~2% help, and those need extreme ballots plus near-perfect knowledge of how everyone else votes. In IRV, betrayal pays several times more often — and your failure has a name and a shape, the **center squeeze**, so an entire wing can see it coming and has a standing reason to betray. Mine are lab constructions; yours turns up in exactly the competitive three-candidate races reform is supposed to fix.

**RCV Advocate:** So strip away the rhetoric and you're just choosing which criterion to fail.

**STAR Advocate:** We *both* are — that's a theorem, not a dodge. No method can satisfy Favorite Betrayal and Later-No-Harm at once. You keep Later-No-Harm and give up favorite-betrayal resistance. We give up Later-No-Harm on purpose — because guaranteeing your later support can *never* help your favorite is the same math that lets a broadly-liked compromise get squeezed out. We think your honest support for a second choice *should* be allowed to help elect them. That's the real disagreement, stated honestly — not "only one of us fails."

---

## 8. How to deploy it

- **Don't open with this.** It's Voting 301. Raise it only when an RCV advocate makes the "only RCV avoids favorite betrayal" claim. With a general audience, Slide 4 stands on its own.
- **Lead by separating the two criteria** before you argue — half the disagreement evaporates once "first mark" vs "later marks" is on the table.
- **Concede STAR fails FBC too — immediately, and without a percentage.** Say "betrayal almost always backfires in STAR," not "STAR is 98% compliant." Your candor is the credibility that makes the center-squeeze point land.
- **End on the value, not the math:** Later-No-Harm *causes* center squeeze; STAR trades it away so a consensus candidate can actually win.

## 9. A mental model to hold onto

- **Favorite Betrayal** = *the front door.* Is it safe to walk your favorite in first? (RCV-IRV: no. Score/Approval: yes. STAR: almost always.)
- **Later-No-Harm** = *the back door.* Is it safe to let your backups in too? (RCV-IRV: yes. Score/Approval: no. STAR: almost always.)
- You **cannot** lock both doors. RCV-IRV locks the back and leaves the front open (center squeeze). STAR keeps both *mostly* shut and refuses to fully sacrifice either — and the front-door failures it does have almost never reward the burglar.

---

## Cross-references
- Slide 4 in [`Why_STAR_Voting.md`](../../topics/Why_STAR_Voting.md) (the claim this defends) and its Part 2 talking point **#12**.
- [`are_equal_score_votes_discounted.md`](../reference/are_equal_score_votes_discounted.md) — the runoff / Equal-Support sibling of this concede-then-reframe argument.
- [`LINKS.md`](../../LINKS.md) → **Full Deck 2025** ("RCV Common False Claims", "Alaska '22", "Burlington 2009", the pass/fail criteria slides); **Why STAR 2**.
- [`fbc_simulation.py`](../../../06_Other/simulations/fbc_simulation.py) + [`06_Other/simulations/README.md`](../../../06_Other/simulations/README.md) — the brute-force FBC measurement behind Section 5 (FBC compliance frequency and the betrayal works:backfires ratio, STAR vs RCV-IRV).
- [`residual_vote_splitting.md`](residual_vote_splitting.md) — the same "only top-two advance" root cause seen as vote-splitting: STAR's self-inflicted bullet-voting / chicken-dilemma edge case, with the [`split_voting/05a`](../../../method_comparisons/split_voting/_main/_main_pages/05a_residual_split_bullet-voting.md)–[`05b`](../../../method_comparisons/split_voting/_main/_main_pages/05b_residual_split_expressive-fix.md) matched demo.
