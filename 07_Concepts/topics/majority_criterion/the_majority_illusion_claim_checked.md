# "The Majority Illusion," claim-checked

**Level: 301 · for debaters**

**One line:** the Center for Election Science's tour of what "majority" actually means is the best short taxonomy of the word in advocacy writing — and its two load-bearing arguments both slide, in the same direction, at the same joint: from *"this kind of winner doesn't always exist"* to *"so the criterion asking for one is a poor yardstick."*

> **Hamlin, A.** ["The Majority Illusion: What Voting Methods Can and Cannot Do."](https://electionscience.org/research-hub/the-majority-illusion-what-voting-methods-can-and-cannot-do) Center for Election Science, Research Hub.

Runnable companion: [the article's own example, counted](../../../method_comparisons/ces_majority_illusion/README.md). Same [claim-check recipe](../../../method_comparisons/fairvote_star_whitepaper/) this library runs on every camp — concede the kernel, test what's testable, flag the overreach, disclose the lean. Companions: [the Majority Criterion](README.md) · ["majority candidate" — five senses](majority_and_minority_candidates.md) · [false majorities](../false_majorities.md).

---

## Why this one matters here

It is the single most-linked plain-English piece on the majority concept, it is written by a co-founder of one of the two organisations this repo cites most, and about **three-quarters of it is correct and genuinely useful** — including a section (the legislature-level false majority) this library did not cover at all until it prompted [a page of its own](../false_majorities.md).

It is also the piece an Approval advocate will hand you when you say "but STAR can fail the majority criterion." So it is worth knowing exactly which parts of it survive contact with an engine.

## The kernel — what's solid (concede it)

- **The taxonomy is clean and correct.** Plurality (most first preferences), absolute majority (over half of them), Condorcet winner (beats each rival head-to-head) are three different things that get called "the majority winner," and confusing them is the commonest error in this debate. This library sorts [five senses](majority_and_minority_candidates.md) rather than three, but that's an extension of his frame, not a correction to it.
- **"It's impossible to guarantee an absolute majority under any voting method when there are more than two candidates."** True, and stated more crisply than most textbooks manage. The candidate need not exist; no rule can conjure one.
- **"If you have an absolute majority winner, then that person is also your Condorcet winner."** True, and it's the direction people get backwards. [We prove it](condorcet_implies_majority.md) — and it's the reason STAR's ✗ on Condorcet and its ✗ on majority are one failure, not two.
- **The runoff section is the sharpest thing in the piece.** *"You can always get an absolute majority winner when there are just two candidates. The problem is who you knock off to get to those last two."* That is the whole [center squeeze](../center_squeeze/) argument in two sentences, it applies identically to top-two primaries and to IRV, and this library agrees with it without reservation.
- **IRV's "majority" is a majority of *active* ballots.** Correct, and one of the most consequential facts in the reform debate. He asserts it; [we count it](../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md#4-the-manufactured-majority-majority-of-remaining-ballots) — Alaska 2022, where Peltola's "51.5% majority" was 48.4% of ballots actually cast, and Burnett & Kogan's 600,000-ballot study where **all four** California IRV elections were won with less than a majority of ballots cast. The article would be stronger with those numbers in it.
- **The false-majority section is right, and was our gap.** Winner-take-all legislatures routinely manufacture majorities; independent redistricting doesn't fix it; proportional representation largely does. Canada checks out precisely — see below.
- **The catch-22 he catches is real.** Critics who attack cardinal methods *both* for electing the high-utility candidate over the majority's favorite *and* for provoking universal strategy that would elect the majority's favorite are holding a position no outcome can satisfy. That's a fair hit, and worth keeping.

## Read it critically — where it doesn't hold

**1. The central slide: non-existence is not an argument against a criterion.** Twice — once for Condorcet, once for the majority criterion — the article moves from *this winner doesn't always exist* to *so this criterion is a weak yardstick*. Those are unrelated claims. No criterion has ever asserted that its winner exists; the majority criterion says only **when one exists, elect them**, and it is perfectly well-defined on the elections where none does. "A voting method could satisfy the Condorcet criterion and yet still make inferior decisions when those Condorcet winners weren't there" is true and is not a criticism of the Condorcet criterion — it's an observation that a criterion constrains a method only where it applies, which is what a criterion is.

There is a real argument in the neighbourhood, and the article partly makes it: *how often* does the case arise, and *how bad* is the miss? That's the frequency-×-severity framing this library uses everywhere, and the same organisation states it properly in [its academic paper](../../../04_Approval/01_Learn/hamlin_hua_2023.md). Here it's replaced by the weaker existence argument.

**2. The frequency claim is asserted without a number, and the number cuts the other way.** *"These Condorcet winners are less likely to exist in competitive elections with more candidates."* Directionally true and quantitatively misleading by omission: in every structured electorate model, a Condorcet winner exists in **95–100%** of elections, and real-election [cycle rates run about 1–5%](../strategic_pathologies.md). The 63.6%-at-seven-candidates figure that would support the article's framing comes from impartial culture — [the model neither camp should argue from](../condorcet/condorcet_efficiency_measured.md). A reader finishes this paragraph believing Condorcet winners are frequently missing. They almost always exist.

**3. The centerpiece example is doing more than its heading says — and one of the methods in it disagrees with the conclusion.** This is the finding worth carrying, and it's [fully counted](../../../method_comparisons/ces_majority_illusion/README.md):

| | 21 voters | 10 voters | 10 voters |
|---|---|---|---|
| article's utilities | A(10) > B(9) > C(0) | B(10) > C(0) > A(0) | C(10) > B(9) > A(0) |

Printed under the heading **"Condorcet Winner"** to show that the Condorcet winner isn't always best — A wins every head-to-head, B has nearly double the average utility.

- **A doesn't merely beat everyone head-to-head; A holds an outright absolute majority** — 21 of 41 first preferences, 51.2%. So the example is not about the Condorcet criterion at all. It's about the **majority criterion**, which by the article's own taxonomy is the *stronger* claim. This makes his thesis better and his section heading wrong.
- **STAR elects A.** B leads the scoring round 174–105; A reaches the runoff second and wins it **21–20**. The article's conclusion is that cardinal methods "target a different metric altogether" — true of Score and Approval, false of STAR, whose [automatic runoff](../../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) is a majority check. An argument that cardinal methods trade majority for utility contains, in its own example, a cardinal method that doesn't.

**4. "Weak majority criterion" is doing quiet work.** The claim: because a majority *could* bullet-vote to force their favorite, Approval and Score pass a weakened majority criterion. The premise is true and the label oversells it. What it establishes is that the majority has a **strategy available**, not that the method has a property — the same move would let you say plurality "weakly" passes almost anything, since voters can always coordinate. It also concedes the thing the article elsewhere disputes: that these methods give a majority a reason to abandon honest scoring of their second choice. Equal Vote's [Relaxed Majority Criterion](README.md#the-relaxed-majority-criterion-equal-votes-answer) asks the sharper question — can the majority support a second choice *honestly*, at max−1, and still win? — and it is the question on which Score and Approval fail and STAR passes. Notably, **the article's own example sits exactly on that line**: A's majority gives B a 9 out of 10, and A survives. Give C a 3 as well and A loses.

**5. Douglas Amy's two frequency figures are quoted secondhand and I could not verify either.** "Close to half the time" for winner-take-all and "less than 10%" under PR are attributed to *Real Choices/New Voices*; neither figure appears in any source I could reach, and the article's own text gives "more than 40%" in one place and "close to half" in another for what should be the same statistic. The *direction* is well supported — the standard academic reference is Blais & Massicotte, "The impact of electoral formulae on the creation of majority governments," *Electoral Studies* 5 (1986) — but treat the two percentages as unverified until someone opens the book. [Our page](../false_majorities.md) flags them the same way.

## What checks out exactly

The Canadian claims are precise, and worth having because they're the cleanest available demonstration that redistricting reform is the wrong lever:

| Election | Vote share | Seat share | Majority? |
|---|--:|--:|---|
| **2011** Conservatives | 39.6% | 166/308 = **53.9%** | yes — manufactured |
| **2015** Liberals | 39.5% | 184/338 = **54.4%** | yes — manufactured |

And Canada has drawn its federal boundaries through independent, judge-chaired commissions since the [Electoral Boundaries Readjustment Act](https://en.wikipedia.org/wiki/Electoral_Boundaries_Readjustment_Act) of **1964** — so these are manufactured majorities with gerrymandering ruled out. The article's inference is sound: the distortion is in single-member districts themselves, not in who draws them.

## The question it raises and doesn't answer

**What *is* a majority on a score ballot?** The article poses this well — half the maximum score? then two candidates can both have one. Total score as the denominator? then almost nobody ever does. Translate to rankings? then you've thrown away the information the ballot existed to collect — and then it moves on. It's a real question and it deserved more than a paragraph. Worked out: [What "majority" means on a score ballot](majority_and_minority_candidates.md#what-majority-means-on-a-score-ballot).

## The scoreboard

| Article's claim | Verdict |
|---|---|
| Three senses of "majority" get confused | ✅ correct, and the best short statement of it |
| No method guarantees an absolute-majority winner at 3+ candidates | ✅ correct |
| Absolute majority ⇒ Condorcet winner | ✅ correct |
| A runoff's "majority" is an artifact of having two candidates | ✅ correct, and the strongest passage |
| IRV's "majority" is of active ballots only | ✅ correct — and understated; the real numbers are worse |
| Winner-take-all manufactures legislative majorities; PR mostly doesn't | ✅ correct in direction; **two frequency figures unverified** |
| Canada 2011/2015; commissions since 1964 | ✅ verified exactly |
| Condorcet winners often don't exist in competitive races | ⚠️ **misleading** — 95–100% in structured models, cycles ~1–5% |
| Non-existence weakens the Condorcet / majority criteria | ❌ **doesn't follow** — a criterion is conditional by construction |
| The example shows the Condorcet winner isn't always best | ⚠️ it's an **absolute-majority** winner, and **STAR elects her** |
| Cardinal methods "target a different metric altogether" | ⚠️ true of Score/Approval, **false of STAR** |
| Approval/Score pass a "weak majority criterion" | ⚠️ true but overlabelled — it's a strategy, not a property |
| Critics' cardinal catch-22 | ✅ a fair hit |

**Lean disclosure.** The Center for Election Science is Approval voting's advocacy organisation and the author is its co-founder; the piece is arguing for cardinal methods. By the repo's [sourcing tiers](../../../CLAUDE.md) that makes it solid for *definitions* and weak for *verdicts*, which is how it reads — the taxonomy is excellent and the two places it leans are both places where a criterion inconvenient to Approval gets softened. **And the lean cuts our way too:** everything above that damages the article's conclusion for Score and Approval leaves the article's *thesis* — that "majority" is a slipperier word than anyone assumes — completely intact. It's right about that. It's just that STAR is on the majority's side more often than the piece lets on, and criteria survive the existence problem better than it says.

## Related

- [The Majority Criterion](README.md) — the method property, RMC, the Later-No-Harm identity
- ["Majority candidate" — five senses](majority_and_minority_candidates.md) — the words, extended past the article's three
- [Condorcet implies majority](condorcet_implies_majority.md) — the proof behind his one-line aside
- [False majorities](../false_majorities.md) — the legislature-level section, built out
- [Hamlin & Hua (2023), claim-checked](../../../04_Approval/01_Learn/hamlin_hua_2023.md) — the same organisation's academic case
- [The article's example, counted](../../../method_comparisons/ces_majority_illusion/README.md)
