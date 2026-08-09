# The Score Distribution table

**One line:** the **Score Distribution** is the LH engine's breakdown of *how many ballots gave each score* to each candidate — the raw shape behind the score totals. It's where you can see at a glance whether a candidate is broadly liked, polarizing, or unknown — and it keeps an honest line between an explicit **0** and a **blank**.

→ Hub: [STAR Reporting](../README.md) · the full report: [How the LH engine reports](README.md) · what counts as a blank: [`GLOSSARY`](../../../../07_Concepts/GLOSSARY.md).

Not in the default on-screen report — read it in the saved `_tabulated.txt` (always included) or put it on screen with the `--full` flag. (A file may still set `options: { show_score_counts: true }` to opt it on.)

---

## A worked example

From the flat-scores teaching election (Apple / Banana / Cherry, 8 ballots):

```text title="Abridged — the Score Distribution block only"
[Score Distribution] (how many ballots gave each star rating)
                Score
Candidate  5  4  3  2  1  0  Abs  | Total  Avg all  Avg rated
Apple      2  1  2  0  0  2    1  |    20      2.5        2.9
Banana     4  1  1  0  0  1    1  |    27      3.4        3.9
Cherry     0  0  1  1  2  3    1  |     7      0.9        1.0
  Avg all   = Total / all ballots — a blank counts as 0, so this is the Total the Scoring Round ranks on, per ballot.
  Avg rated = Total / the ballots that scored this candidate (Abs excluded) — support among voters who had an opinion.
```

## How to read each part

- **The `5 4 3 2 1 0` columns** — under the `Score` group header — count *how many ballots* gave that score. Each row adds up to the number of ballots: Apple = `2+1+2+0+0+2 (+1 Abs) = 8`.
- **`Abs`** = ballots that left this candidate **blank** (no score recorded). An explicit **`0`** is different — it's a *cast* "I rate you zero," so it sits in the `0` column, not in `Abs`. (Here the only blank is the one fully-blank ballot, so every row shows `Abs 1`.) This is the same **0-vs-blank** distinction that drives the [abstention discussion](../../../04_Real_Elections/pet_real_bv_election/small_case_abstention_lesson.md).
- **`Total`** = the sum of stars = the Scoring Round number: Apple = `5·2 + 4·1 + 3·2 = 20`.
- **`Avg all`** = `Total ÷ every ballot cast` — Apple = `20 ÷ 8 = 2.5`. A blank is scored **0** by the tabulation, so this is nothing more than the `Total` restated per ballot: it ranks the candidates in exactly the order the Scoring Round does. **This is the average that decides things.**
- **`Avg rated`** = `Total ÷ (ballots − Abs)` — the mean among voters **who actually scored** this candidate (blanks excluded, explicit zeros **included**). Apple = `20 ÷ 7 = 2.9`. It decides nothing, but it separates *unknown* from *disliked*: the two explicit zeros pull Apple down in **both** columns, while the blank pulls down only `Avg all`.
- **Why two columns at all** — because a blank is counted **one way by the tabulation and the other way by the average**, and both readings are true. The gap between them is exactly the abstention drag: the wider it is, the more of the candidate's weak total is *people not rating them* rather than *people rating them low*. The pair appears only when some ballot abstained; with no `Abs` the two are the same number and the table prints a single `Avg`. → [which denominator, and why](../score_averages.md) · [how the averages are computed and rounded](../score_distribution_and_averages.md).

## What the shape tells you

- **Banana** (4 fives, total 27, rated 3.9) — broad, strong support → the winner.
- **Apple** (2 fives but also 2 zeros, rated 2.9) — liked by many, dismissed by some (more polarizing than Banana).
- **Cherry** (no 4s or 5s, mostly 1s and 0s, rated 1.0) — little support; finishes last.

The distribution is the **why** behind the Scoring Round totals: same totals can come from very different ballot shapes, and this table shows which. (BetterVoting reports the *totals* in its Scores Table; this per-score breakdown is the LH engine's alone.)

## It is not BetterVoting's "Range of Scores"

The two are easy to confuse — both are histograms built from the same ballots — but they collapse the grid along **opposite margins**. This table reads **down a column** (one candidate, every voter). BetterVoting's *Range of Scores* chart reads **across a row** (one voter, every candidate: `max − min`, i.e. how much of the 0–5 ballot that voter used). Neither can be derived from the other, and each report has exactly one of them. → [Two views of the same scores](../score_matrix_two_views.md).
