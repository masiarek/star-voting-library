# STAR Voting FAQ — the mechanics, answered with worked examples

The [official STAR Voting FAQ](https://www.starvoting.org/faq) answers dozens of questions in prose. This page mirrors the **mechanics** questions — the ones about *how the count works* — and answers each with a **runnable example**: a small YAML election you can tabulate yourself, with the engine's own output shown inline. Seeing the numbers move beats being told they do.

For the **political, legal, and historical** questions (cost, constitutionality, security, the League of Women Voters, presidential use, Oregon history…), the [official FAQ](https://www.starvoting.org/faq) is the right source — those aren't things a tabulation engine can demonstrate.

New to the terms? Start with [Ballot & Terminology Basics](../ballot_and_terminology_basics.md) and the [Glossary](../GLOSSARY.md).

---

## The one election behind half these answers

Most of the runoff questions below are really the same question. Here's a 10-voter STAR election that shows all of them at once — **Berry** is broadly liked and wins the Scoring Round, but more voters *strictly prefer* **Almond**, who wins the Automatic Runoff. One voter scores both finalists 5 (Equal Support).

Run it yourself: [`faq_runoff_reversal_c3_b10.yaml`](../../01_STAR/_main/faq_runoff_reversal_c3_b10.yaml) · reader page: [faq_runoff_reversal_c3_b10](../../01_STAR/_main/_main_pages/faq_runoff_reversal_c3_b10.md).

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

Because the highest *total score* rewards **breadth**, while the runoff rewards **preference**. In the example above, Berry racks up the most stars (lots of 4s), but when you ask *"Almond or Berry?"* six voters say Almond and only three say Berry — so **Almond wins**. Dropping the runoff would elect Berry over the candidate a clear majority actually prefers. The runoff is what makes STAR's winner majority-backed rather than merely popular-on-average — and it's why a lone voter can't inflate a compromise choice to victory by scoring strategically.

This "score leader ≠ runoff winner" outcome is a **Runoff Reversal**, and it's the honest core of the STAR debate — worked from both sides (when it helps, when it's arguable) in [STAR's second round — an FAQ](STAR_second_round_FAQ.md), with real elections in [runoff reversal cases](../../01_STAR/runoff_overturns_leader/README.md). Deeper: [The Automatic Runoff](STAR_Automatic_Runoff.md).

## Q: What if I give both finalists the same score?

Then your ballot expresses **no preference between them** — that's **Equal Support**, and it's counted honestly: it did its job in the Scoring Round (helping *both* advance), and in the runoff it goes to *neither* finalist's column. In the example, the `5,5,0` voter shows up as the `Equal Support -- 1` line, and the runoff is decided among the **9 voters who did express a preference** (majority = 5, not 6). Crucially, equal scores never split your vote or hurt you — giving your two favorites both a 5 helps them both. Full treatment: [Abstention vs. a zero vs. NOTA](abstention_vs_zero_vs_nota.md).

## Q: "Wasted votes" — what's the difference between an exhausted ballot in RCV and an Equal Support vote in STAR?

A big one. In **RCV-IRV**, an *exhausted* ballot — one whose ranked candidates are all eliminated — is **set aside and does not count in the deciding round**; its voter has no say in the final outcome. In **STAR**, an *Equal Support* ballot **is counted** — the voter deliberately expressed no preference between the two finalists, and that intent is recorded (see the `Equal Support` line above), not discarded. One is a ballot the system *dropped*; the other is a preference the voter *chose not to state*. Worked example: [Exhausted ballots (IRV)](../RCV_IRV/RCV_IRV_exhausted_ballots.md).

## Q: Does STAR give everyone exactly one equal vote?

Yes. However many stars you hand out in the Scoring Round, the **Automatic Runoff gives every voter exactly one vote** — for whichever finalist they scored higher (or none, if they scored them equally). In the example, all 10 voters cast one runoff vote each: 6 for Almond, 3 for Berry, 1 Equal Support. No one's ballot counts twice, and scoring a candidate 5 vs 4 carries the same runoff weight as 5 vs 0 — it's one vote either way. That's how STAR satisfies one-person-one-vote. See [The Automatic Runoff](STAR_Automatic_Runoff.md).

## Q: Why is a blank — or a skipped candidate — counted as a zero?

Because a blank means "I did not support this candidate," which is exactly what a 0 encodes — it can't help that candidate advance. But STAR's engine keeps *why* a zero is a zero: this library records a small **marker vocabulary** — `-` blank · `~` race abstention · `&` candidate abstention · `?` spoiled · `%` spoiled+reissued — all of which tabulate as 0 but are reported distinctly, so a deliberate abstention isn't confused with an active low score. A *whole* ballot left blank (or all-equal) is set aside as an abstention (turnout only), not folded into the tally. Full detail: [Abstention vs. a zero vs. NOTA](abstention_vs_zero_vs_nota.md) and ["Preference" — the word that causes half the confusion](../preference.md).

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

Read the top row: **Almond beats Berry 6–3** (with 1 Equal Support) and **beats Cocoa 7–3** — Almond is preferred head-to-head over *everyone*, which is why the runoff crowns Almond. This grid is also how you'd spot a [Condorcet winner or cycle](../RCV_Ranked_Robin/ranked_robin.md).

## Q: Does STAR fail Later-No-Harm? Should I "bury" a strong second choice?

STAR does not formally pass **Later-No-Harm** (LNH) — but that's a feature-tradeoff, not a flaw, and burying rarely pays. LNH and the **Favorite-Betrayal Criterion** are *provably incompatible* — no method has both — and people routinely confuse the two. In STAR, honestly scoring your second choice can, in rare constructions, help them beat your favorite in the runoff; but *under-scoring* them to prevent that risks throwing the election to someone you like even less, and the play backfires far more often than it works. The measured, worked-out answer (with a brute-force simulation) is in [Favorite Betrayal — Voting 301](favorite_betrayal_voting_301.md).

## Q: Are STAR Voting ballots summable?

Yes — STAR is **batch summable**. Each precinct can add up its own star totals and its own pairwise-preference counts, and those partial sums combine into the final result without any central re-count. That's a genuine advantage over RCV-IRV, whose elimination rounds need the *whole* ballot set in one place. Worked side-by-side: [STAR summability](STAR_summability.md) and the [summability demo](../../method_comparisons/summability_demo/README.md).

## Q: Why doesn't RCV-IRV break two-party domination the way its advocates hope?

Because IRV's elimination order can knock out a broadly-liked **centrist** before the final round — the **center squeeze** — handing the win to a more polarizing candidate and re-teaching voters to abandon their sincere favorite. STAR's score-then-runoff structure doesn't eliminate the center the same way. This is IRV-specific (it's not a property of all ranked ballots — Ranked Robin isn't squeezed). Worked examples: [center squeeze](../RCV_IRV/RCV_IRV_center_squeeze.md) and the [center-squeeze cases](../../method_comparisons/center_squeeze/README.md). Method-to-method: [RCV-IRV vs. STAR](../rcv_irv_vs_star.md).

---

## For everything else

Cost, constitutionality, security, One-Person-One-Vote law, presidential use, endorsements, and STAR's history are covered at the **[official STAR Voting FAQ](https://www.starvoting.org/faq)**. This page stays in its lane: the tabulation mechanics, shown with examples you can run.

**See also:** [Curriculum (101/201/301)](../CURRICULUM.md) · [Why STAR Voting?](../Why_STAR_Voting.md) · [Scored vs. ranked ballots](../scoring-methods-vs-ranked-voting.md) · [Glossary](../GLOSSARY.md)
