# Combined Approval Voting (CAV)

**Level: 201 → 301 · deep dive**

**Combined Approval Voting** gives every voter three options for each candidate: vote **For**, vote **Against**, or **abstain**. The count is a subtraction — each candidate's **net score** is their approvals minus their disapprovals — and the largest net score wins.

|  | For | Abstain | Against |
|---|:--:|:--:|:--:|
| **What the voter marks** | ☑ in the *For* column | neither box | ☑ in the *Against* column |
| **What it's worth** | **+1** | **0** | **−1** |

It is a *reference* method here, kept in `06_Other/` alongside [RCV-IRV](../RCV_IRV/), [Range](../Range/), [STV](../STV/) and [3-2-1](../three_two_one/) — **not** one of the three [Equal Vote Coalition](https://www.equal.vote) methods ([STAR, Approval, Ranked Robin](../../07_Concepts/topics/choosing_among_evc_methods.md)).

## The ballot

CAV's ballot is the **two-column grid** that US voters already meet on ballot measures — a *For* box and an *Against* box on each row, with the instruction to check at most one:

| Check off *at most one box* in each row: | For | Against |
|---|:--:|:--:|
| Jane Doe | ☑ | ☐ |
| Jonn Jones | ☐ | ☐ |
| Clark Kent | ☑ | ☐ |
| Joe Smith | ☐ | ☑ |
| John Stewart | ☐ | ☑ |

*A CAV ballot that treats blanks as abstentions: support for two candidates, opposition to two, and abstention from one. Jonn Jones's empty row is the method's distinguishing feature — it is worth exactly nothing, neither help nor harm.*

That two-column layout is also the practical argument its advocates make for it: an *approve / disapprove / neither* row is the same thing a jurisdiction already prints for a referendum question, so CAV is the one non-standard score scale that runs on voting equipment already certified to handle for-and-against questions. Treat that as a claim about **equipment**, not about **outcomes** — it says nothing about whether the method picks better winners.

## Where the name comes from — and the other six

CAV has been reinvented repeatedly, which is why it answers to so many names. **Dan Felsenthal** proposed it in 1989, in a paper comparing it head to head with ordinary approval voting; "combined approval voting" is his own coinage, contrasted there with "regular approval voting" (RAV). **José Carlos Alcantud and Annick Laruelle** later gave it an axiomatic characterisation and a second name, **Dis&approval voting**.

| Name | Who uses it |
|---|---|
| **Combined Approval Voting (CAV)** | Felsenthal 1989; the usual name in English-language reform circles |
| **Dis&approval voting** | Alcantud & Laruelle's characterisation |
| **Balanced Approval Voting (BAV)** | a reform-advocacy branding |
| **Evaluative Voting (EV-3)** | the French experimental-economics literature |
| **Net approval voting** | descriptive; names the subtraction |
| Approval with abstention option (AWAO) · True weight voting (TWV1) | rarer, mostly single-source |

Felsenthal is the same author whose paradox examples this repo already runs — including [two demonstrations of ordinary Approval failing badly](../../method_comparisons/felsenthal_paradoxes/) ([missing a Condorcet winner](../../method_comparisons/felsenthal_paradoxes/bv2152_r6ctvy_felsenthal_ex5_approval_cw.md), and [electing a Pareto-dominated candidate](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md)). CAV is what he proposed in the same period as the fix. Whether the third option actually fixes those failures is the interesting question, and the answer is mostly no — see [What the third option buys](#what-the-third-option-buys-and-what-it-doesnt) below.

*Sourcing note: the name inventory above draws on [electowiki](https://electowiki.org/wiki/Combined_approval_voting) and [Wikipedia](https://en.wikipedia.org/wiki/Combined_approval_voting). electowiki is **advocacy-adjacent** — reliable for what a method's proponents call it and how it works, weak for verdicts about whether it is good. The criteria and empirical claims below are sourced to the academic literature instead.*

## The engine (and why it's here)

**No off-the-shelf CAV tabulator exists** — BetterVoting, the LH `starvote` engine, `pref_voting`, `abcvoting` and `pyrankvote` all lack it. So [`cav_tabulation.py`](cav_tabulation.py) is a clean-room implementation of the published rule.

It is not a homegrown guess, because CAV is exactly **three-level score voting on a shifted scale** — which means every count can be checked two independent ways, and the engine runs both on every election:

1. **Affine invariance, checked rather than asserted.** A (0,1,2) mark is the (−1,0,+1) mark plus one, so over *n* ballots each candidate's (0,1,2) total must exceed their net total by *exactly n* — and the two scales must rank the field identically. The engine computes both and verifies the identity.
2. **An independent engine.** The equivalent (0,1,2) profile is handed to [`pref_voting`](https://pref-voting.readthedocs.io)'s `grade_methods.score_voting` — a library nobody here wrote — and the winners must match. If `pref_voting` isn't installed the check is skipped with a note rather than silently passing.

```
$ python cav_tabulation.py --selftest
  vector 1 (net beats raw approvals): winner=B expected=B affine=ok OK
  vector 2 (abstentions are free): winner=B expected=B affine=ok OK
  vector 3 (unanimous disapproval still ranks): winner=B expected=B affine=ok OK
  vector 4 (all-abstain ties, column order decides): winner=A expected=A affine=ok OK
  blank-cell guard: refused a grid with an empty cell OK
  mark-range guard: refused a mark outside 0..2 OK
CAV engine self-test: all checks passed ✓
```

### Blanks are the whole point — and the encoding trap

Ballot marks are **2 = For, 1 = abstain, 0 = Against**, and **a CAV case file must mark every cell explicitly.** An abstention is written `1`. It is never left blank.

That rule exists because this library's shared parser folds blanks and every [marker character](../../07_Concepts/GLOSSARY.md) into score 0 — which on the CAV scale reads as a vote **Against**, the exact opposite of what an empty row means on a real CAV ballot. The engine therefore **refuses** a grid containing a blank cell rather than quietly miscounting it:

```
$ python cav_tabulation.py a_file_with_blanks.yaml
Error: this file is not a valid CAV ballot grid.
  - ballot row 2 has an empty cell — a CAV ballot must mark every candidate
    2 (For), 1 (abstain) or 0 (Against). An abstention is written 1, NOT left blank.
```

This is not a quirk of the file format. It is the method's one genuinely distinctive property, showing up as a parsing problem: **CAV scores a blank as a middle grade, where every other score ballot in this library scores it as the lowest grade.** The worked example below is built entirely on that difference.

## Worked example — the newcomer nobody dislikes

Twelve neighbours elect one seat on a town library board. Alma and Byron are the known quantities and both are polarising: each has about four voters For and four Against. **Cleo** is a newcomer — three voters have met her and all three vote For; the other nine have no opinion and abstain. Nobody votes Against her.

Cleo wins, and it isn't close. Her nine abstentions cost her nothing, so three unopposed approvals carry her to **+3**, ahead of Byron's +1 and Alma's −1:

<!-- report:cav_library_board_c3_b12 -->
```text
--- Combined Approval Voting (CAV, single winner) ---
  Library board by Combined Approval Voting — the newcomer nobody dislikes
 Tabulating 12 ballots on the three-level For / abstain / Against
 ballot. Highest NET score (approvals − disapprovals) wins.

[Scenario]
  Twelve neighbours elect one seat on a town library board.
  
  Alma and Byron are the known quantities, and both are polarising: four voters
  vote For each of them, and roughly as many vote Against. Cleo is a newcomer.
  Only three voters have met her — all three vote For — and the other nine have
  no opinion and abstain. Nobody votes Against her.
  
  Under CAV an abstention is genuinely free: it adds nothing and subtracts
  nothing. So Cleo's nine blanks cost her nothing, her three approvals stand
  unopposed, and she wins on net score (+3) ahead of Byron (+1) and Alma (−1).
  
  The companion file `cav_library_board_blank_is_zero_c3_b12.yaml` gives these
  twelve voters the SAME marks on an ordinary score ballot, where an unmarked
  candidate scores 0 — the bottom of the scale rather than the middle. That one
  change reverses the field completely: Byron 10, Alma 8, Cleo 6. Read the pair
  together; the difference is entirely in what a blank is taken to mean.

Ballots (2 = For, 1 = abstain, 0 = Against):
  Alma, Byron, Cleo
  2, 0, 1
  2, 0, 1
  2, 0, 1
  2, 0, 1
  0, 2, 1
  0, 2, 1
  0, 2, 1
  0, 2, 1
  1, 1, 2
  0, 1, 2
  1, 1, 2
  1, 2, 1

Vote tally:
          For   Abstain   Against      Net
  Cleo      3         9         0       +3  ← winner
  Byron     5         3         4       +1
  Alma      4         3         5       -1

Verification 1 — affine invariance (the (0,1,2) reading):
  The same marks summed as 0/1/2 must exceed the net total by exactly
  the ballot count (12) for every candidate, and must rank the field
  the same way. That is what makes CAV 'three-level score voting'.
    Cleo   net   +3   +12 =   15  (0/1/2 sum 15)
    Byron  net   +1   +12 =   13  (0/1/2 sum 13)
    Alma   net   -1   +12 =   11  (0/1/2 sum 11)
  ✓ holds — the (−1,0,+1) and (0,1,2) scales agree.

Verification 2 — pref_voting score_voting on the (0,1,2) profile: Cleo
  (✓ agrees with the CAV count)

Winner — Combined Approval Voting (single winner)
  Cleo
```
<!-- /report -->

### The same twelve voters, one word changed

Now hand those twelve people an ordinary score ballot and ask them to mark it the same way: top grade for a candidate they're For, bottom grade for one they're Against, and **leave the row blank** when they have no opinion. Nothing about anyone's opinion has changed. The only thing that changed is what a blank is *worth* — 0 out of 0–5 is the bottom of the scale, the same mark a voter uses to say "worst possible candidate," rather than the middle of −1…+1.

The field reverses end to end:

<!-- report:cav_library_board_blank_is_zero_c3_b12 -->
```text
--- Range / Score Voting (single winner) ---
  Library board on a blank-is-zero score ballot — the same twelve voters
 Tabulating 12 ballots on a 0–2 scale (range/score: highest total wins, no runoff).

[Scenario]
  The counterfactual twin of `cav_library_board_c3_b12.yaml`. Same twelve
  neighbours, same library board seat, same opinions — and the same physical
  marks: a voter who was For a candidate gives them the top grade, a voter who
  was Against gives them the bottom, and a voter with no opinion leaves the row
  blank.
  
  The one thing that changes is what a blank MEANS. On a CAV ballot an unmarked
  row is an abstention worth 0 on a −1…+1 scale, i.e. the MIDDLE. On an ordinary
  score ballot an unmarked row is worth 0 on a 0…5 scale, i.e. the BOTTOM — the
  same mark a voter uses to say "worst possible candidate."
  
  That single reinterpretation reverses the entire field. Cleo, the newcomer
  whom nine voters simply don't know, is charged nine bottom grades she never
  cast, and drops from first (+3 net under CAV) to last (6 points here). Byron
  wins with 10, Alma takes 8.
  
  This is the mechanism behind the empirical finding in the 2012 French
  evaluative-voting experiments: moving from a (0,1,2) scale to a (−1,0,+1)
  scale left polarising candidates roughly where they were but raised the scores
  of broadly-liked and, especially, lesser-known candidates. The scales are
  affine-equivalent on identical ballots; they are not equivalent once voters
  leave rows blank.

Ballots:
  Alma, Byron, Cleo
  2, 0, 0
  2, 0, 0
  2, 0, 0
  2, 0, 0
  0, 2, 0
  0, 2, 0
  0, 2, 0
  0, 2, 0
  0, 0, 2
  0, 0, 2
  0, 0, 2
  0, 2, 0

Total score (sum of all grades):
  Byron          10  ← winner
  Alma           8
  Cleo           6

Cross-check — pref_voting score_voting: Byron  (✓ agrees with the hand count)

Winner — Range / Score Voting (single winner)
  Byron
```
<!-- /report -->

| | CAV (blank = middle) | Score (blank = bottom) |
|---|---|---|
| **1st** | **Cleo** (+3) | **Byron** (10) |
| **2nd** | Byron (+1) | Alma (8) |
| **3rd** | Alma (−1) | **Cleo** (6) |

Cleo goes from first to last. Nine voters who said *nothing at all* about her were counted, on the second ballot, as having said she was the worst candidate on it.

**Which answer is right?** That depends on a question the arithmetic can't settle: when a voter leaves a row blank, are they saying *"no opinion"* or *"no support"*? CAV commits to the first reading, the 0–5 score ballot to the second. Neither is obviously correct — a blank is also what a lazy or hurried voter leaves — and the choice is worth roughly the whole election for any candidate the electorate doesn't know well.

This is the mechanism behind a real empirical finding. In the 2012 French presidential election, Baujard, Gavrel, Igersheim, Laslier and Lebon ran an *in situ* experiment with 2,340 participants, grading candidates on several scales including (0,1,2) and (−1,0,+1). Moving to the scale with negative grades left **polarising** candidates roughly where they were, nudged **broadly-liked** candidates up, and raised the scores of **lesser-known** candidates substantially. Their conclusion is the same as this example's: the scales are not linearly equivalent in practice, notably because of the symbolic weight of a negative grade — voters do not use them interchangeably even when the arithmetic says they could.

> **Read the two files together:** [CAV count](cases/cases_pages/cav_library_board_c3_b12.md) · [blank-is-zero twin](cases/cases_pages/cav_library_board_blank_is_zero_c3_b12.md). Sources: [`cav_library_board_c3_b12.yaml`](cases/cav_library_board_c3_b12.yaml) · [`cav_library_board_blank_is_zero_c3_b12.yaml`](cases/cav_library_board_blank_is_zero_c3_b12.yaml).

## Properties

CAV is three-level [score voting](../Range/concepts/range_voting.md), so it inherits score voting's criteria compliances exactly.

| Criterion | CAV | Note |
|---|:--:|---|
| [Favorite betrayal](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) | ✔ | Voting **For** your honest favorite is always safe — it never costs you |
| [Monotonicity](../../07_Concepts/topics/monotonicity) | ✔ | Raising a candidate's mark never hurts them |
| [Participation](../../07_Concepts/topics/participation) | ✔ | Additive: showing up and voting your opinion never backfires |
| [Independence of irrelevant alternatives](../../07_Concepts/topics/spoiler_effect.md) | ✔ | On fixed marks, adding or dropping a candidate leaves everyone else's total untouched |
| [Independence of clones](../../05_Ranked_Robin/03_Criteria/clone_independence) | ✔ | No first-choice count to split |
| [Summable](../../07_Concepts/topics/summability) | ✔ | One running total per candidate; precinct-summable, unlike [IRV](../RCV_IRV/concepts/RCV-IRV-Hare.md) |
| [Majority favorite](../../07_Concepts/topics/majority_criterion/README.md) | ✘ | Fails, as all score methods do — a majority's favorite can lose to a broadly-tolerated rival |
| [Condorcet winner](../../07_Concepts/topics/condorcet/) | ✘ | Not Condorcet-efficient |
| [Later-no-harm](../../01_STAR/01_Learn/the_count/STAR_second_round_FAQ.md) | ✘ | Voting For a second candidate can beat your favorite |

## What the third option buys — and what it doesn't

CAV's pitch is that the extra option lets you say something Approval can't: *this candidate is actively bad*, as distinct from *I'm not backing them*. Two things are worth knowing before accepting that.

**Under strategy it collapses into Approval — provably.** A voter maximising their influence should never use the middle option, because an abstention spends half the available voting power on that candidate for nothing. Suppose every voter uses only For and Against. Then each candidate's net is `(#For) − (#Against) = (#For) − (n − #For) = 2·(#For) − n`, and *n* is the same for every candidate — so ranking by net score is **identical** to ranking by approvals. A CAV election among strategic voters *is* an [Approval](../../04_Approval/01_Learn/approval_voting.md) election, with a constant offset. The third option is expressive, not decisive; the honest voters are the ones who use it, and they are the ones it moves.

**It doesn't repair Approval's known failures.** Felsenthal's own Approval paradoxes — [electing someone who loses every head-to-head matchup](../../method_comparisons/felsenthal_paradoxes/bv2152_r6ctvy_felsenthal_ex5_approval_cw.md), or [a candidate every single voter likes less than another](../../method_comparisons/felsenthal_paradoxes/felsenthal_ex6_pareto.md) — come from summing thresholded opinions with no head-to-head stage. Adding a third threshold level makes the ballot finer-grained; it doesn't add the comparison step, so the same constructions survive. This is the gap [STAR](../../01_STAR/01_Learn/README.md) closes from the other direction: keep the score ballot, then settle it with an [automatic runoff](../../01_STAR/01_Learn/the_count/) between the top two, which *is* a head-to-head comparison.

**Where it lands.** CAV is a genuine improvement in *expressiveness* over Approval at almost no cost in ballot complexity, and its equipment story is real. It is not a Condorcet method, not a runoff method, and under strategic pressure not distinguishable from the method it improves on. Judged against this library's usual yardstick — [what makes a good winner](../../07_Concepts/topics/what_makes_a_good_winner.md) — it belongs on the shelf beside Score, one notch more expressive and subject to the same limits.

## References

- Felsenthal, D. S. (1989). "On combining approval with disapproval voting." *Behavioral Science* **34**(1), 53–60. [DOI](https://doi.org/10.1002/bs.3830340105) — the original proposal, comparing CAV against regular approval voting.
- Alcantud, J. C. R., & Laruelle, A. (2014). "Dis&approval voting: a characterization." *Social Choice and Welfare* **43**, 1–10. [DOI](https://doi.org/10.1007/s00355-013-0766-7) — the axiomatic characterisation (circulated as a working paper from 2012, which is the date usually cited for the name).
- Baujard, A., Gavrel, F., Igersheim, H., Laslier, J.-F., & Lebon, I. (2014). "Who's favored by evaluative voting? An experiment conducted during the 2012 French presidential election." *Electoral Studies* **34**, 131–145. [HAL open access](https://hal.science/hal-00803024)
- Baujard, A., Gavrel, F., Igersheim, H., Laslier, J.-F., & Lebon, I. (2018). "How voters use grade scales in evaluative voting." *European Journal of Political Economy* **55**, 14–28. — the scale-calibration study behind the (0,1,2) vs (−1,0,+1) comparison above.
- [Combined approval voting — Wikipedia](https://en.wikipedia.org/wiki/Combined_approval_voting) · [electowiki](https://electowiki.org/wiki/Combined_approval_voting) (advocacy-adjacent; see the sourcing note above)

**See also:** [Approval Voting](../../04_Approval/01_Learn/approval_voting.md) · [Approval's honest limits](../../04_Approval/01_Learn/approval_honest_limits.md) · [Range / Score voting](../Range/concepts/range_voting.md) · [3-2-1 voting](../three_two_one/README.md) (the other three-level rated method here) · [Hillinger's evaluative voting](../../method_comparisons/hillinger_evaluative_voting/) (the same EV-3 ballot, made runnable from the paper) · [Cardinal utility](../../07_Concepts/topics/cardinal_utility.md) · [Strategic voting](../../07_Concepts/topics/strategic_voting.md)

# file: README.md
