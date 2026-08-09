# Score averages — which denominator, and why

**Level: 201 · deep dive**

**One line:** a candidate's score **total** is a single unambiguous number, but the *average* behind it is not — it depends entirely on **what you divide by**, and a blank ballot is counted one way by the tabulation and the other way by the average. The LH report prints **both** readings, labelled, whenever they can differ.

→ This is the scoring-round twin of [Reading the Runoff Percentages — two denominators](../the_count/runoff_percentages.md), which asks the same question one stage later. Reading the table itself: [The Score Distribution table](reporting_LH/score_distribution.md). How the arithmetic is done and rounded: [the one float that sneaks in](score_distribution_and_averages.md).

---

## One total, several possible averages

Scores are added, so a **total** has no ambiguity: `5 + 5 + 0 + 2 + 3 = 15`, and 15 is what the Scoring Round ranks on. But the moment you divide that 15 to get "stars per voter," you have to answer a question the total never had to answer:

> **Does a voter who left this candidate blank belong in the denominator?**

Both answers are defensible, and they are not close to each other. That is the whole of it — there is no rounding subtlety here, no floating-point trick, no disagreement about the count. Just a denominator.

## What the report prints

From the [five-styles case](../../02_Examples/cases/cases_pages/03d_c5_b5_style-gallery-five-more.md) — five candidates, five ballots, one of them a partial ballot that scored only Clara and Diego:

```text title="Abridged — the Score Distribution block only"
[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total  Avg all  Avg rated
Alice      2  0  1  1  0  0    1  |    15      3.0        3.8
Bruno      0  0  1  1  1  1    1  |     6      1.2        1.5
Clara      3  0  2  0  0  0    0  |    21      4.2        4.2
Diego      0  0  2  2  0  1    0  |    10      2.0        2.0
Erin       0  0  2  0  0  2    1  |     6      1.2        1.5
  Avg all   = Total / all ballots — a blank counts as 0, so this is the Total the Scoring Round ranks on, per ballot.
  Avg rated = Total / the ballots that scored this candidate (Abs excluded) — support among voters who had an opinion.
```

Read **Clara's row against Alice's**: Clara was scored by everyone, so her two averages are the same number and the columns say nothing new. Alice was left blank by one voter, and her two averages are `3.0` and `3.8`. Same 15 stars, same 5 ballots, two honest answers.

## The two denominators

| | denominator | Alice | the question it answers |
|---|---|---:|---|
| **`Avg all`** | every ballot cast (5) | `15 ÷ 5 = 3.0` | *How much support per voter, across the whole electorate?* The blank is scored **0** here, exactly as the tabulation scores it — so this is nothing but the `Total` restated per ballot, and it ranks candidates in the Scoring Round's own order. **The only one that decides anything.** |
| **`Avg rated`** | ballots that scored her (4) | `15 ÷ 4 = 3.8` | *How does she poll among voters who had an opinion?* Decides nothing — but it separates **unknown** from **disliked**, which the totals alone cannot. |

The two columns appear **only when some ballot abstained.** With no `Abs`, the denominators are the same number and the table prints a single plain `Avg` with no note — which is why most reports in this repo show one column.

## The gap is the abstention drag

An explicit **`0`** and a **blank** are different marks, and the two columns are where the difference becomes visible:

- an explicit `0` is a cast opinion — it sits in the `0` column and pulls **both** averages down;
- a blank sits in `Abs` and pulls down **only `Avg all`**.

So the **gap between the columns** measures how much of a candidate's weak total is *people not rating them* rather than *people rating them low*. Bruno and Erin above both total 6, both read `1.2` / `1.5` — genuinely weak. A candidate reading `1.2` / `4.5` would be something else entirely: nearly unknown, but liked by everyone who knew them. The Scoring Round would treat those two candidates identically, and it would be right to — but only one of them would be worth running again.

Note what this does **not** license: `Avg rated` is not a "fairer" score, and swapping it in would break STAR. A candidate scored 5 by one voter and left blank by 999 would read `5.0` and top the table. Being unrated is not the same as being liked, which is exactly why the deciding column is the one with everybody in the denominator.

## A third denominator, which is a bug

BetterVoting's report has been observed dividing by a denominator that matches **neither** — the subject of [BV2105](../../../02_STAR_Bloc/02_Examples/bv2105_r4dqvd_ice_cream_bloc.md). On four ballots (one fully blank, one partial), BV classifies *both* the blank and the partial as abstentions and averages over the remaining **2**. The partial voter's score is still inside the total; only their ballot has been removed from the denominator, so the published average reconciles with nothing.

That case is the strongest argument for printing the label rather than the number alone: the defect is invisible if you only see an average, and obvious the moment the report says what it divided by. (BetterVoting's results page carries [four different denominators](../../../07_Concepts/tabulation_engines/BV/reading_a_bv_results_page.md) across its four decks — worth knowing before comparing any two percentages on it.)

## Why the column rounds instead of printing an exact fraction

The LH engine is otherwise obsessive about exactness — every tabulation quantity is a `Fraction`, and a proportional allocation prints as an exact mixed number like `34 +5745/21952` rather than a lying `34.3`. So it's fair to ask why this column settles for `3.8`. Three reasons, and the third is decisive:

1. **Nothing is lost.** Every input to the division is already on the same row — `Total`, `Abs`, and the ballot count in the header line — and the note names both denominators. The exact value is one division away, reconstructible by hand.
2. **No average decides anything.** Finalists come from `Total`, an integer printed exactly; the runoff counts ballots; tiebreaks use scores. `Avg all` orders candidates identically to `Total` by construction. There is no decision a rounded average could corrupt — unlike a PR allocation, where the exact fraction is a deep intermediate whose inputs are *not* on the page and where a rounded value could hide a threshold crossing. That is where exactness earns its keep: [BV2130](../../../03_STAR_PR/02_Examples/bv2130_presidential_board_star_pr.md).
3. **At real sizes the exact form actively obscures the denominator.** `Fraction` reduces. In the [461-ballot pet race](../../04_Real_Elections/pet_real_bv_election/cases/cases_tabulated/best_pet_c7_b461_tabulated.txt), Bird's exact `Avg rated` is `163/72` — but **432** ballots rated Bird. The exact form would print a denominator that appears nowhere else in the report and contradicts the note directly above it. Cat's would be `875/223` against 446 rating ballots; Rat's `31/22` against 430.

So the exact column would be more ink, less clarity, and no new information. The rounding itself is still done properly — from an exact rational, **half-up**, never a binary float, which is [its own story](score_distribution_and_averages.md).

## The house rule this is an instance of

**Name the denominator inline; never make the reader infer it.** The repo already made this call once, for the runoff: rather than print a bare `52%`, the engine prints *"Voters with a preference: 363 of 461 (98 Equal Support). Dog 190 (52%) vs Cat 173 (48%); majority = 182"* — the denominator, the excluded bucket, and the threshold, all stated. → [Runoff percentages](../the_count/runoff_percentages.md).

Averages in the scoring round are the same problem with a different set-aside bucket: `Equal Support` is to the runoff what `Abs` is to the score average. In both places a single unlabelled percentage or average would be smaller, tidier, and impossible to check.

## The one-sentence version

Totals are unambiguous and decide the election; averages need a denominator, so the report prints **both** honest ones side by side — the electorate-wide `Avg all` that mirrors the total, and the opinion-holders' `Avg rated` that tells unknown from disliked.

## See also

- [The Score Distribution table](reporting_LH/score_distribution.md) — how to read every column, and `0` vs blank.
- [The Score Distribution table — and the one float that sneaks in](score_distribution_and_averages.md) — exact-rational arithmetic, half-up rounding, and why `1.25` once printed as `1.2`.
- [Reading the Runoff Percentages](../the_count/runoff_percentages.md) — the same denominator question, one round later.
- [BV2105 — a real denominator defect](../../../02_STAR_Bloc/02_Examples/bv2105_r4dqvd_ice_cream_bloc.md) · [Where the two reports differ](reporting_diff_BV_LH.md).
- [`GLOSSARY`](../../../07_Concepts/GLOSSARY.md) — abstention, Equal Support.
