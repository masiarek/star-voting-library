---
tags:
  - criteria
  - reform
---

# FairVote's claims, checked — a standing ledger

*FairVote is the largest and oldest US voting-reform organization, and its materials are the ones a STAR or Ranked Robin advocate is most likely to meet in an actual debate. This page is the running index of every FairVote claim this repo has checked against a **countable election** or a **published theorem** — the ones that hold, the ones that overreach, and the ones that are false. It is meant to keep growing; each row links to the full check.*

**Level: 301 · for debaters**

## How to use this page (read this first)

**This is a ledger, not an attack page, and the distinction is the whole point.** A page that collected only errors would be worth exactly nothing in a debate — the first true FairVote claim anyone quoted would sink it. What makes this list usable is that it records **verdicts**, including "holds," and that some of those verdicts land against STAR and stay on the page anyway. Three of the checks below concede a real STAR weakness; one runs FairVote's own strategic example and confirms it works.

**Three rules this ledger follows**, from the repo's [fairness discipline](../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md):

1. **Quote before you check.** Every row quotes FairVote's own wording. A paraphrase you can argue against is not a claim they made.
2. **Check against something that can say no** — a runnable election or a theorem, never a preference.
3. **Disclose both leans.** FairVote advocates RCV-IRV; this repo teaches STAR. Neither lean is a defect; concealing either one is.

And the standing tone rule for this repo: [sing STAR's and Ranked Robin's virtues rather than attacking RCV](rcv_irv_vs_star.md). RCV voters are the natural allies of a better count — Ranked Robin uses their exact ballot. Use these checks to correct a specific claim once, then get back to what the methods do well.

---

## The ledger

Verdicts: **✅ holds** — accurate as written · **⚠️ overreaches** — a true core stated too strongly, or a standard applied to one side only · **❌ false** — checkably wrong.

| Source | Claim | Verdict | The check |
|---|---|:--:|---|
| [Comparison chart](https://fairvote.org/resources/electoral-systems/comparing-voting-methods/) (undated) | *"RCV … satisfies both the Independence of Irrelevant Alternatives and Independence of Clones criteria"* | ❌ | Impossible by Arrow, and refuted by **Burlington 2009** and **Alaska 2022** — the two elections FairVote itself names as its Condorcet failures. [Run the counterfactuals](../../method_comparisons/fairvote_comparison_table/README.md#3-resistance-to-spoilers-false-as-stated) |
| Comparison chart | *"Plurality, approval, score, and STAR voting … fail … the Condorcet Loser Criterion"* | ❌ | **STAR passes it** — the automatic runoff makes it structural. FairVote's own 2018 white paper concedes this. [The row](../../method_comparisons/fairvote_comparison_table/README.md#5-condorcet-efficiency-mostly-holds-one-sentence-is-false) |
| Comparison chart | *"proportional analogs to Condorcet, approval, score … have seen … little study or advocacy"* | ❌ | The literature starts with **Thiele (1895)** and **Phragmén**, has a 2023 Springer textbook, and a reference implementation this repo runs as an engine. [The row](../../method_comparisons/fairvote_comparison_table/README.md#8-compatibility-with-fair-multi-winner-elections-holds-one-false-clause) |
| Comparison chart | *"strategic voting is not a concern in jurisdictions and among voters that use RCV"* | ⚠️ | Later-no-harm and burial-immunity are real and conceded. But **compromising is favorite betrayal**, and Burlington 2009 is a live case — the same paragraph concedes it, then generalizes past it. [The row](../../method_comparisons/fairvote_comparison_table/README.md#2-resistant-to-strategic-voting-overreaches) |
| Comparison chart | *"These methods are vulnerable to the election of a candidate who lacks majority support"* (of approval/score/STAR) | ⚠️ | STAR's runoff is a head-to-head majority; what it can fail is **majority *favorite***, which is a different criterion. The failure is real, the stated consequence is not. [The row](../../method_comparisons/fairvote_comparison_table/README.md#4-majority-cohesion-holds-with-a-false-consequence) |
| Comparison chart | *"the 'beats-all' winner only lost twice"* in ~500 US RCV elections | ✅ | Real, checkable, and the best argument on the page. Our own caveat is about **field size**, not the number. [Measured](condorcet/condorcet_efficiency_measured.md) |
| Comparison chart | *"RCV and Condorcet methods are more complex than a simple arithmetic sum"* | ✅ | FairVote grades its own method Low here. Correct — with one omission, [summability](summability/README.md), where RCV and Condorcet methods are opposites. |
| Comparison chart | STAR/score/Condorcet *"have never been used in a public election for government office"* | ✅ | True, and the guinea-pig risk it names is a real political cost. [The row](../../method_comparisons/fairvote_comparison_table/README.md#1-well-tested-in-government-elections-holds) |
| ["Explaining FairVote's position on STAR Voting"](https://fairvote.org/explaining-fairvotes-position-on-star-voting/) (Richie & Penrose, 2018) | STAR fails **Later-No-Harm** | ✅ | True and conceded — and it is the whole disagreement, not a slip. STAR's camp argues LNH is what *forces* [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md). [Full check](../../method_comparisons/fairvote_star_whitepaper/README.md) |
| 2018 white paper | STAR fails **majority-favorite** and **mutual-majority** | ✅ | True and conceded. [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) |
| 2018 white paper | A coordinated faction can **bury** a centrist out of STAR's runoff (French 2017, Washington 2010) | ⚠️ | **The burial works — we ran both.** The overreach is what goes unsaid: it needs *every* rival faction to bury the centrist *and* rate its enemies a 4, and RCV-IRV on those same strategic ballots elects **Le Pen**. [Both examples, tabulated](../../method_comparisons/fairvote_star_whitepaper/README.md) |
| ["Why the Condorcet Criterion Is Less Important Than It Seems"](https://fairvote.org/why-the-condorcet-criterion-is-less-important-than-it-seems/) (Slatky, 2010) | *"Condorcet winners are centrist by nature, regardless of the preferences of the electorate"* | ❌ | Self-contradictory — the Condorcet winner is *defined by* those preferences. Shift the electorate left and the pole candidate becomes the Condorcet winner. [Run it (BV2169)](condorcet/fairvote_condorcet_claim_check.md) |
| 2010 Condorcet article | *"the impossibility of victory under Condorcet methods"* for voters who lean to one side | ❌ | Non-moderates win whenever a majority prefers them pairwise. It is the **compromise** candidate who faces impossibility — under the *first-choice* methods. [Run it (BV2170)](condorcet/fairvote_condorcet_claim_check.md) |
| 2010 Condorcet article | Electing the pairwise winner is *"the fallacy of the middle ground"* | ❌ | Category error — the middle-ground fallacy is about the truth of propositions, not the aggregation of expressed preferences. [The check](condorcet/fairvote_condorcet_claim_check.md) |
| 2010 Condorcet article | No single ideal of a "best" winner exists, so "Condorcet isn't everything" | ✅ | The article's one genuinely good point, and this repo makes it too. [What makes a good winner?](what_makes_a_good_winner.md) |

## The pattern across all three documents

Not "FairVote lies" — something more specific and more useful to name in a debate:

- **The standard slides between rows.** Spoiler resistance grades RCV on *fixed ballots* and cardinal methods on *hypothetical voter behavior*. A strategy is excused for RCV as too risky and coordination-heavy, and the same reasoning is not extended to STAR.
- **Criteria get conflated.** Majority *favorite* is stated as "lacks majority support." IIA is described in prose and clone-independence is cited as the proof. Burial (a strategy) is used to grade the *spoiler* row, which has its own row two criteria earlier.
- **The best claims are empirical, and they hold.** The 2-in-~500 Condorcet figure, later-no-harm, STV's record, the representation research — these are strong and should be conceded first in any exchange. The errors cluster in the *mathematical* claims, which is exactly where they are checkable.

## Adding a row

New check? Follow the recipe rather than improvising it — it is what makes this list quotable:

1. **Quote it verbatim**, with the document and a retrieval date.
2. **Build the smallest election that settles it** ([keep examples small](../tips/TIPS_choosing_voter_counts.md)), or cite the theorem that does.
3. **Run it** and paste a generated report block — never a hand-typed table ([why](../../method_comparisons/fairvote_comparison_table/README.md)).
4. **Write the verdict against yourself first.** If the claim holds, say so and mark it ✅. A ledger with no ✅ rows is not evidence, it is a grievance.
5. Add the row here and put the full check on a page of its own.

## Related

- [Advocacy organizations — who says what, and where each one leans](advocacy_organizations.md)
- [RCV-IRV vs STAR](rcv_irv_vs_star.md) — the comparison itself, written to keep RCV voters as allies
- [Criteria at a glance](criteria_at_a_glance.md) — our own pass/fail grid, with the same warning label
- Claim-checks pointed at *other* sources, including our own side: [Wikipedia's Condorcet criterion](condorcet/condorcet_criterion_claim_check.md) · [the "majority illusion"](majority_criterion/the_majority_illusion_claim_checked.md) · [cardinal-voting claims](../scores_and_ranks/cardinal_voting_claims_checked.md) · [Edelman's Condorcet myth](condorcet/edelman_condorcet_myth.md) · [Hamlin & Hua on approval](../../04_Approval/01_Learn/hamlin_hua_2023.md)
