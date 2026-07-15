# STAR Voting FAQ — the mechanics, answered with worked examples

The [official STAR Voting FAQ](https://www.starvoting.org/faq) answers dozens of questions in prose. This page mirrors the **mechanics** questions — the ones about *how the count works* — and answers each with a **runnable example**: a small YAML election you can tabulate yourself, with the engine's own output shown inline. The aim is an **impartial walk-through of the mechanics**: where STAR fails a criterion or carries an honest tradeoff, this page says so and links a worked case, rather than arguing the method. (For the case *for* STAR, see [Why STAR Voting?](../topics/Why_STAR_Voting.md); for its limits, [STAR's honest limits](STAR_honest_limits.md).)

For the **political, legal, and historical** questions (cost, constitutionality, security, the League of Women Voters, presidential use, Oregon history…), the [official FAQ](https://www.starvoting.org/faq) is the right source — those aren't things a tabulation engine can demonstrate.

New to the terms? Start with [Ballot & Terminology Basics](../topics/ballot_and_terminology_basics.md) and the [Glossary](../GLOSSARY.md).

---

## The one election behind half these answers

Most of the runoff questions below are really the same question. Here's a 10-voter STAR election that shows all of them at once — **Berry** is broadly liked and wins the Scoring Round, but more voters *strictly prefer* **Almond**, who wins the Automatic Runoff. One voter scores both finalists 5 (Equal Support).

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/tg4779) · **[results ↗](https://bettervoting.com/tg4779/results)** (BV2182, election `tg4779`). Run it locally: [`bv2182_tg4779_faq_runoff_reversal.yaml`](../../01_STAR/_main/bv2182_tg4779_faq_runoff_reversal.yaml) · reader page: [bv2182_tg4779_faq_runoff_reversal](../../01_STAR/_main/_main_pages/bv2182_tg4779_faq_runoff_reversal.md).

```
Count × Almond,Berry,Cocoa
    4 ×      5,    4,    1
    3 ×      0,    5,    2
    2 ×      5,    4,    0
    1 ×      5,    5,    0        ← scores both finalists 5 = Equal Support

Scoring Round
   Berry         -- 44 -- First place      ← highest total score
   Almond        -- 35 -- Second place
   Cocoa         -- 10
 Berry and Almond advance.

Automatic Runoff Round
   Almond        -- 6 -- First place       ← preferred head-to-head
   Berry         -- 3
   Equal Support -- 1
 Almond wins.
   Voters with a preference: 9 of 10 (1 Equal Support).
   Almond 6 (67%) vs Berry 3 (33%); majority = 5.
```

---

## Q: Why bother with the automatic runoff? Why not just elect the highest scorer?

The two rounds measure different things: total *score* rewards **breadth** (how many stars a candidate collects), the runoff rewards **pairwise preference** (which of the two front-runners more voters scored higher). In the example, Berry collects the most stars, but asked *"Almond or Berry?"* six of the nine decided voters pick Almond — so **Almond wins**. Note the scope of that claim: the runoff decides **only between the two top-scored finalists**. It does **not** guarantee the overall majority or [Condorcet](STAR_three_winner_notions.md) winner — a third candidate can beat *both* finalists head-to-head yet never reach the runoff, which is a genuine STAR failure mode ([the Condorcet winner who scores third](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md)).

This "score leader ≠ runoff winner" outcome is a **Runoff Reversal**, and whether it's the right call is genuinely contested: sometimes the runoff rescues a majority-preferred candidate from vote-splitting, sometimes it overrides broad average support on a thin pairwise margin. Both readings are worked out — not just the favourable one — in [STAR's second round — an FAQ](STAR_second_round_FAQ.md), with real elections in [runoff reversal cases](../../01_STAR/runoff_overturns_leader/README.md). Deeper: [The Automatic Runoff](STAR_Automatic_Runoff.md).

## Q: What if I give both finalists the same score?

Then your ballot expresses **no preference between them** — that's **Equal Support**. It's counted, not discarded: it did its job in the Scoring Round (helping *both* candidates' totals) and in the runoff it goes to *neither* finalist's column. In the example, the `5,5,0` voter is the `Equal Support -- 1` line, and the runoff is decided among the **9 voters who did express a preference** (majority = 5, not 6). The tradeoff to be clear-eyed about: scoring the two finalists equally means you **give up your say in the runoff between them** — so if you *do* have a preference there, express it. And while equal scores don't split your vote in the Scoring Round, STAR is not entirely immune to vote-splitting — see the rare [residual vote-splitting](residual_vote_splitting.md) case. Full treatment: [Abstention vs. a zero vs. NOTA](abstention_vs_zero_vs_nota.md).

## Q: "Wasted votes" — what's the difference between an exhausted ballot in RCV and an Equal Support vote in STAR?

The *outcome* can look similar — neither ballot affects the final pairwise decision — but the mechanism differs, and that's the honest distinction. In **RCV-IRV**, an *exhausted* ballot (all its ranked candidates eliminated) is **set aside in the deciding round**; the voter didn't choose that — elimination did. In **STAR**, an *Equal Support* ballot reaches the runoff, but the voter **rated the two finalists equally**, so it contributes to neither — a choice the voter made, and one where the ballot's scores still counted in the Scoring Round. So the difference is **agency and stage** (involuntary drop late vs. voluntary no-preference, ballot still counted earlier), *not* that one voter matters and the other doesn't — a STAR voter can equally decline to help decide the runoff by scoring both finalists the same. Worked example: [Exhausted ballots (IRV)](../RCV_IRV/RCV_IRV_exhausted_ballots.md).

## Q: Does STAR give everyone exactly one equal vote?

In the **runoff**, yes. However many stars you gave out, the Automatic Runoff counts **one vote per voter** — for whichever finalist you scored higher (or none, if you scored them equally). In the example all 10 voters cast one runoff vote each (6 Almond, 3 Berry, 1 Equal Support); scoring 5-vs-4 carries the same runoff weight as 5-vs-0. But be precise about scope: the **Scoring Round is different by design** — a score ballot lets *intensity and breadth* count, so a voter who spreads 5/3/1 shapes *which candidates become finalists* differently than one who bullet-votes 5/0/0. STAR's one-person-one-vote claim is specifically about the runoff step, not a claim that every voter has identical influence in round one. See [The Automatic Runoff](STAR_Automatic_Runoff.md) and [the equally-weighted vote](equally_weighted_vote.md).

## Q: Why is a blank — or a skipped candidate — counted as a zero?

Because a blank means "I did not support this candidate," which is exactly what a 0 encodes — it can't help that candidate advance. But STAR's engine keeps *why* a zero is a zero: this library records a small **marker vocabulary** — `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all of which tabulate as 0 but are reported distinctly, so a deliberate abstention isn't confused with an active low score. A *whole* ballot left blank (or all-equal) is set aside as an abstention (turnout only), not folded into the tally. Full detail: [Abstention vs. a zero vs. NOTA](abstention_vs_zero_vs_nota.md) and ["Preference" — the word that causes half the confusion](../topics/preference.md).

## Q: What is a preference matrix?

It's the **head-to-head grid**: for every pair of candidates, how many voters prefer each, and how many express Equal Support. It's what the runoff reads, and it lets you check *any* pairwise contest at a glance. The engine prints one for the example above:

```
--- Runoff (Preference) Matrix ---
Legend: For - Equal Support - Against   (* = Top-2 Finalist)
                 |  * Almond   |  * Berry    |    Cocoa    |
-------------------------------------------------------------
      * Almond > |     ---     | 6 -  1 -  3 | 7 -  0 -  3 |
       * Berry > |  3 - 1 -  6 |    ---      |10 -  0 -  0 |
         Cocoa > |  3 - 0 -  7 | 0 -  0 - 10 |    ---      |
```

Read the top row: **Almond beats Berry 6–3** (with 1 Equal Support) and **beats Cocoa 7–3** — here Almond happens to be the [Condorcet](STAR_three_winner_notions.md) winner (beats everyone head-to-head), so the runoff lands on the same candidate. The matrix is also how you **audit** STAR against itself: in other elections it exposes when the score-and-runoff winner is **not** the Condorcet winner (a real STAR failure — [the Condorcet winner who scores third](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md)) or when there's no Condorcet winner at all (a [cycle](../RCV_Ranked_Robin/ranked_robin.md)). It's the same pairwise grid a Condorcet method reads.

## Q: Does STAR fail Later-No-Harm? Should I "bury" a strong second choice?

STAR **fails** Later-No-Harm (LNH): honestly scoring a second choice can, in constructions, help that candidate beat your favorite in the runoff. That's a real, admitted property — worth stating plainly, not waving away. Two things put it in context, without denying it: (1) LNH and the **Favorite-Betrayal Criterion** are *provably incompatible* — **no** method satisfies both, so every system fails one of the pair, and the two are routinely confused. (2) Whether *deliberately* burying a rival pays in STAR is a measurable question, not a rhetorical one: a brute-force [simulation](favorite_betrayal_voting_301.md) finds it rarely helps and backfires more often than it works, because under-scoring a strong rival risks electing someone you like even less. So it's a genuine tradeoff STAR accepts and this repo *quantifies* rather than dismisses — see [Favorite Betrayal — Voting 301](favorite_betrayal_voting_301.md) and [STAR's honest limits](STAR_honest_limits.md).

## Q: Are STAR Voting ballots summable?

Yes — STAR is **batch summable**: each precinct can total its own stars and its own pairwise-preference counts, and those partial sums combine into the final result. RCV-IRV is **not** summable that way — its sequential eliminations depend on the full ballot set, so the deciding round can't be reconstructed from precinct subtotals alone. That's a real, method-inherent difference in how the count composes (it bears on precinct-level reporting and auditing); how much it *should* weigh against other properties is a judgment for the reader, not this page. Worked side-by-side: [STAR summability](STAR_summability.md) and the [summability demo](../../method_comparisons/summability_demo/README.md).

## Q: Can RCV-IRV eliminate a broadly-liked centrist? (the center squeeze)

It can. IRV eliminates each round by *fewest first-choice votes*, so a centrist who is many voters' **second** choice but few voters' **first** choice can be knocked out early — the **center squeeze** — leaving two more-polarized finalists. This is a property of IRV's **elimination mechanic specifically**; it is *not* a property of ranked ballots in general (a Condorcet / [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) count of the *same* ballots isn't squeezed). STAR's score-then-runoff doesn't eliminate the centre the same way — but to be even-handed, **STAR is not immune to failure either**: it can miss the Condorcet winner (above) and it fails LNH, so this isn't "STAR wins on everything." Worked examples: [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) and the [center-squeeze cases](../../method_comparisons/center_squeeze/README.md). Method-to-method, evenhandedly: [RCV-IRV vs. STAR](../topics/rcv_irv_vs_star.md).

---

## Where STAR falls short (so this stays honest)

No method escapes the impossibility results (Arrow, Gibbard–Satterthwaite) — every system trades something away, and STAR is no exception. Its documented weaknesses:

- **It can miss the Condorcet winner** — the score-and-runoff winner isn't always the candidate who beats everyone head-to-head. Worked case: [the Condorcet winner who scores third](../../method_comparisons/paradoxes_and_whoops/bv2156_3grpbb_star_misses_condorcet.md).
- **It fails Later-No-Harm** — see the LNH question above.
- **It has rare residual vote-splitting** — [residual vote-splitting](residual_vote_splitting.md).
- **The runoff can override strong average support** on a thin pairwise margin — the "jarring" side of a [runoff reversal](STAR_second_round_FAQ.md).

The full, honest catalogue is [STAR's honest limits](STAR_honest_limits.md) and [Three notions of "winner"](STAR_three_winner_notions.md) — read those alongside the answers above, not instead of them.

---

## For everything else

Cost, constitutionality, security, One-Person-One-Vote law, presidential use, endorsements, and STAR's history are covered at the **[official STAR Voting FAQ](https://www.starvoting.org/faq)**. This page stays in its lane: the tabulation mechanics, shown with examples you can run.

**See also:** [Curriculum (101/201/301)](../CURRICULUM.md) · [Why STAR Voting?](../topics/Why_STAR_Voting.md) · [Scored vs. ranked ballots](../topics/scoring-methods-vs-ranked-voting.md) · [Glossary](../GLOSSARY.md)
