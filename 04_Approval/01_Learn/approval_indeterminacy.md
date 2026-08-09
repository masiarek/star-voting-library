# Is Approval's outcome arbitrary? The Saari–Van Newenhizen critique

*The sharpest academic attack on Approval Voting says the method is **indeterminate**: a voter with a real preference `a > b > c` has no way to say so, must arbitrarily pick a ballot, and — the criticism runs — those arbitrary picks can decide the election. It is a serious argument, it has a serious answer, and the answer is not the one Approval's defenders gave. This page works all three, plus the popular-press version of the same complaint.*

**Level: 301 · for debaters** → Companions: [Approval Voting](approval_voting.md) (the ballot and the count) · [honest limits](approval_honest_limits.md) (the threshold, from the practical side) · [in the theory literature](approval_in_the_literature.md) (Zwicker's five criticisms, of which this is #1 and #2 sharpened) · [cardinal utility](../../07_Concepts/topics/cardinal_utility.md) (the framework the rebuttal comes from) · runnable: [Hillinger's paper](../../method_comparisons/hillinger_evaluative_voting/README.md). Curriculum: [301.5](../../07_Concepts/CURRICULUM.md).

---

## The exchange, in one paragraph

Three papers, one 1988 issue of *Public Choice*:

1. **Saari & Van Newenhizen** — "The problem of indeterminacy in approval, multiple, and truncated voting systems." The attack, aimed at Approval and generalized to cardinal voting at large. Hereafter **SVN**.
2. **Brams, Fishburn & Merrill** — "The responsiveness of approval voting: Comments on Saari and Van Newenhizen." The defense, by three of Approval's principal architects. Hereafter **BFM**.
3. **SVN again** — "Is approval voting an 'unmitigated evil'?" The rejoinder.

Saari restated the criticism in his 1994 and 1995 books. Claude Hillinger's verdict on the whole exchange, which is hard to argue with: **the two sides talked past each other.**

## The criticism, at full strength

State it the way SVN do, without softening:

> A voter strictly prefers `a` to `b` to `c`. The approval ballot offers them `(1,0,0)` or `(1,1,0)` — approve the favorite alone, or approve the top two. **Neither ballot expresses the preference they actually hold.** The voter must choose arbitrarily. And one can construct profiles in which, depending on how the arbitrary choices fall, *any* candidate wins.

The last clause is what gives it teeth. This isn't "Approval loses some information" — the [expressivity complaint](approval_honest_limits.md#1-no-preference-strength-or-order) everyone already concedes. It's the stronger claim that the information Approval loses is **outcome-determining**, so the winner is a function of something the method never asked about and voters have no principled way to decide.

It also isn't only about Approval. SVN aim it at "a wide range of voting methods including AV and more generally cardinal voting" — which is why a STAR advocate cannot file it under someone else's problem. See [what it does to STAR](#what-it-does-to-star), below.

## Why the defense didn't land

BFM defended Approval on its own terms. Hillinger's objection is that they defended it from inside the enemy's framework — they "live in a halfway house, not having completely abandoned the traditional ordinal framework." Two consequences:

- **Approval's scale is too coarse to win the argument on.** With one bit per candidate, it is genuinely hard to claim the ballot is an accurate representation of what a voter thinks. Every defense has to concede the compression and then argue it doesn't matter.
- **Conceding that rankings are the real preferences concedes the case.** Once the strict ordering is the ground truth, an approval ballot *is* a lossy, arbitrary projection of it, and SVN have already won. The disagreement was never about the arithmetic.

This is worth noticing as a debate pattern in its own right, separate from Approval: **when a criticism smuggles in a premise about what a ballot is supposed to be approximating, answering it inside that premise is answering a rigged question.** Compare the [criterion-built-to-fit-the-method](../../method_comparisons/single_winner_scorecard/README.md) tell.

## Hillinger's inversion — and it is runnable

Hillinger's move is to refuse the premise. The whole force of SVN's argument, he notes, depends on assuming that **the given strict orderings are exact expressions of the true preferences.** Assume instead that the *cardinal marks* are what voters mean, and the arbitrariness reverses direction: it is now the rankings, and every Borda count derived from them, that are under-determined.

His Table 3 makes it concrete. Seven voters, three candidates. Here are the approval ballots — this part everybody agrees on:

<!-- report:hillinger_t3_arbitrariness -->
```text
--- Approval Voting (single winner) ---
 Tabulating 7 ballots (any non-zero score = approval).

Ballots:
   columns = Ada, Ben, Cora      (1 = approve; 0 = not approved)
     3 × 1,0,0
     2 × 0,1,1
     2 × 1,0,1

   Ada  -- 5 (71%) -- Elected
   Cora -- 4 (57%)
   Ben  -- 2 (29%)

[Approval Distribution] (how many candidates each ballot approved)
   11 approvals across 7 ballots — average 1.6 of 3 (range 1–2).
     approved 1: 3 ballots
     approved 2: 4 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
         |  Ada   |  Cora  |  Ben   |
   ----------------------------------
   Ada   |   --   |  40%   |   0%   |
   Cora  |  50%   |   --   |  50%   |
   Ben   |   0%   |  100%  |   --   |

Winner — Approval Voting (single winner)
  Ada
```
<!-- /report -->

**Ada 5, Ben 2, Cora 4.** Now complete each ballot to a strict ranking. The marks constrain you — `(1,0,0)` puts Ada on top, `(0,1,1)` puts Ben and Cora above Ada, `(1,0,1)` puts Ada and Cora above Ben — but they do not pin the order down. **Two different completions are consistent with these exact same ballots:**

| | 3 voters | 2 voters | 2 voters | [Borda](../../06_Other/other_ranked_methods/borda.md) totals | Borda winner |
|---|---|---|---|---|---|
| **Reading 1** | Ada > Ben > Cora | Ben > Cora > Ada | Ada > Cora > Ben | Ada **10**, Ben 7, Cora 4 | **Ada** |
| **Reading 2** | Ada > Cora > Ben | Cora > Ben > Ada | Cora > Ada > Ben | Ada 8, Ben 2, Cora **11** | **Cora** |

Same seven voters. Same seven ballots. Nothing has changed about what anyone marked. **The Borda winner flips from Ada to Cora** — and note that Cora was the *runner-up* on the approval count, so this is not a tie being broken two ways, it is a genuine reversal.

Cross-checked against [`pref_voting`](../../07_Concepts/tabulation_engines/cross_checking_with_pref_voting.md)'s independent Borda: `Ada 10, Ben 7, Cora 4 → Ada` and `Ada 8, Ben 2, Cora 11 → Cora`, matching the paper's printed Score column exactly.

**The claim this licenses, stated precisely:** *for a given approval score, the strict orderings are arbitrary.* SVN said a score is arbitrary given a ranking; Hillinger says a ranking is arbitrary given a score. Both are true. Which one is the *defect* depends entirely on which object you think is real — and that is a question about voters, not a question about mathematics.

### A typo the engine caught

Running Table 3 turns up a second slip in the paper, of the same kind [the Table 4 page already documents](../../method_comparisons/hillinger_evaluative_voting/README.md).

The "Alt. Order" row labels its middle column **`bca`** — the same order as in the initial row. But the Alt. BC marks printed beneath it are `(0,1,2)`, which is **`cba`**, and only `cba` reproduces his own Score column of `8,2,11`. Take the label at face value and the totals come out `Ada 8, Ben 4, Cora 9`.

**Cora wins either way**, so nothing in his argument depends on it — but if you quote the numbers, quote them from `cba`.

## Ford's version — the wishy-washy middle

A second criticism Hillinger takes up, from Lawrence Ford (then chair of mathematics at Idaho State) answering a *Scientific American* reader question. Ford's claim: voters are decided about their favorites and decided about the ones they dislike, but **wishy-washy in the middle** — and if they choose more or less randomly for or against approval in that middle range, "the whole election can become random."

*(A reading note: as printed, Ford says voters are "fairly positive of their favorites and fairly positive of those they hate" — almost certainly "positive" in the sense of **certain**, not favorable. The argument only parses that way.)*

Hillinger grants it "some validity," and the concession he makes is the right one: **under Approval, not approving is equivalent to being against.** There is no mark for *I don't know enough to judge*. The voter is forced to be for or against a candidate they have no information about. On a scale with a genuine middle — his EV-3 `(−1, 0, +1)` — a zero is neutral, and the voter is under no compulsion to lump the unknown in with the disliked.

**Is it a valid criticism?** Partly, and the split is worth being precise about, because the valid half is stronger than the half people quote.

**What holds:**

- **The bind is real and it is Approval-specific.** A one-bit ballot cannot distinguish *no opinion* from *no*. That is the [threshold dilemma](approval_honest_limits.md#2-the-approval-threshold-dilemma-the-central-critique) restated from the ignorance side rather than the strategy side, and it is the same thing Zwicker's survey calls the deep criticism.
- **The middle is exactly where the decision lives.** Nobody agonizes over their favorite or their worst. The whole content of an approval ballot is the line, and the line sits in the region voters are least sure about.
- **A neutral middle option genuinely fixes this specific complaint.** Hillinger's EV-3 and STAR's 0–5 both let a voter say *lukewarm* without saying *no*.

**What overreaches — "the whole election can become random":**

- **Independent random noise does not randomize an aggregate; it averages out.** If uncertain voters effectively flip coins, each candidate's total picks up variance around its mean, and the variance grows like √n while the electorate grows like n. The noise decides the winner only when the race is already inside the noise band — which is recount territory, where *every* method is decided by something arbitrary. "Can become random" is true of a near-tie and false of an election.
- **The version that would bite is the one Ford didn't make.** If the middle-range choices are *correlated* rather than random — every uncertain voter moving their line in response to the same polling — then it is not noise, it is a systematic shift, and it does move outcomes. That is [Laslier's (2009) finding](approval_in_the_literature.md#why-the-strategy-argument-never-settles): the strategically best line sits near the expected winner's utility, and voters roughly behave that way. **Poll-dependence is a much better criticism of Approval than randomness**, and it is the one this library makes.
- **The comparison class is missing.** Under [Choose-One](../../07_Concepts/topics/plurality.md) the wishy-washy middle has no expression whatsoever. Under [RCV-IRV](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md) they are forced into a *strict* order and must invent distinctions they don't feel — the identical complaint from the ranked side, which is [the case for weak ranks](../../07_Concepts/scores_and_ranks/strict_vs_weak_ranks.md). Uncertainty in the middle is a fact about voters, not a defect of Approval. What differs between methods is whether the ballot lets you *say* you're uncertain, and Approval's answer — "no" — is a real demerit in a field where most alternatives answer worse.

So: a genuine and well-aimed critique of the **one-bit ballot**, deployed with a conclusion its own mechanism doesn't support. Use the bind, drop the "random."

## What it does to STAR

The house rule is that [fairness has to cut both ways](../../07_Concepts/topics/how_to_learn_about_voting_methods.md), so: SVN aimed at cardinal voting generally, and a 0–5 ballot does not walk away clean.

**Where STAR is genuinely better off.** Six levels are enough to express *any* strict ranking of up to six candidates exactly, so for most real races the SVN voter who "cannot express `a > b > c`" simply can — they score 5/3/1 and the ordering is recorded. The indeterminacy argument is at its absolute strongest against a 1-bit ballot and weakens monotonically as levels are added. **Approval is EV-2**; that is the whole difference.

**Where it still bites.** Three places, and they should be conceded plainly:

1. **Seven or more candidates and the pigeonhole returns.** Six levels cannot strictly order seven candidates; some voters are forced into ties they don't feel, and we are back inside SVN's argument — a point [the scale note](../../01_STAR/01_Learn/properties_and_limits/STAR_nonstandard_scale.md#why-05-in-the-first-place) already makes.
2. **STAR's 0 is not a neutral middle.** Hillinger's answer to Ford leans on a scale with a negative pole, where zero means *indifferent or abstaining*. On 0–5 the bottom of the scale is the bottom, so a voter who has never heard of a candidate gives them the same 0 as the candidate they loathe. The repo's [abstention markers](../../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md) record the *intent* but still tabulate as 0. STAR relieves the bind (you may be lukewarm) without solving the ignorance problem (you may not say *no opinion*).
3. **The runoff re-imports the ordinal question.** [STAR's second round](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) is a pairwise comparison, so it reads the ballot's *order* between two finalists — and a voter who scored them equally has, by construction, not answered. That is [Equal Support](../../07_Concepts/GLOSSARY.md), which the library treats as an honest expression rather than a gap; SVN would treat it as exactly the indeterminacy they described. Both descriptions fit the same fact.

## The short version

- **The criticism is real and it is aimed at the ballot's coarseness**, not at approval-counting. It gets weaker with every level you add to the scale, which is why it is devastating against a checkbox and merely interesting against 0–5.
- **The standard defense (BFM) concedes too much** by arguing inside the assumption that a strict ranking is the true preference. Don't reuse it.
- **Hillinger's inversion is the better answer, and it is a standoff, not a win.** A coarse score under-determines the ranking exactly as a ranking under-determines the score — Table 3 shows one approval result compatible with two opposite Borda winners. Which under-determination counts as the *flaw* is a question about what voters actually hold in their heads, and neither side settled it in 1988.
- **Ford's popular version:** keep the bind (no mark for "I don't know"), drop the conclusion (aggregates don't go random). The correlated-line version — outcomes moving with the polls — is the criticism worth making.
- **Say what it does to STAR** before an opponent does. Seven-plus candidates, no neutral zero, and a runoff that asks an ordinal question.

---

## Sources and their lean

- **Saari, D. G. & Van Newenhizen, J.** (1988), "The problem of indeterminacy in approval, multiple, and truncated voting systems," *Public Choice* 59(2); and the rejoinder, "Is approval voting an 'unmitigated evil'?", same issue. **Lean:** Saari is the leading academic advocate of [Borda](../../06_Other/other_ranked_methods/borda.md) and a consistent critic of cardinal methods — a committed position, argued rigorously.
- **Brams, S. J., Fishburn, P. C. & Merrill, S. III** (1988), "The responsiveness of approval voting: Comments on Saari and Van Newenhizen," *Public Choice* 59(2). **Lean:** Brams and Fishburn are Approval's principal academic architects; this is the defense by the interested party.
- **Hillinger, C.** (2004), "Voting and the Cardinal Aggregation of Judgments," Munich Discussion Paper 2004-9, §10 and Table 3. **Lean:** advocates for cardinal/evaluative voting; this library's own side of the argument, which is why the Table 3 numbers are re-derived here rather than quoted.
- **Ford, L.**, *Scientific American*, "Ask the Experts," quoted in Hillinger §10. **Lean:** popular-press remark, not a peer-reviewed claim; treat accordingly.

## See also

- [Approval in the theory literature](approval_in_the_literature.md) — the five standard criticisms, two of which don't survive; and *Approval = Borda = Condorcet* on dichotomous preferences
- [Approval — honest limits](approval_honest_limits.md) — the same territory from the practical side
- [Hamlin & Hua (2023)](hamlin_hua_2023.md) — the advocacy side's academic case, claim-checked
- [Cardinal utility](../../07_Concepts/topics/cardinal_utility.md) — measurability vs. comparability, the vNM trap, and Hillinger's argument in full
- [The fidelity ladder](../../07_Concepts/scores_and_ranks/fidelity_ladder.md) — what each score↔rank conversion drops and what it invents; Table 3 is the rung the ladder doesn't cover
- [When compression moves the Condorcet winner](../../method_comparisons/black_curtain/condorcet_compression.md) — the same loss, five ballots, fully worked
- [Hillinger's paper, made runnable](../../method_comparisons/hillinger_evaluative_voting/README.md) — Table 3 and Table 4 as case files

# file: approval_indeterminacy.md
